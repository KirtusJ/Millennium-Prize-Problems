"""Verify the common winding operators and read back the two Z4 control trajectories."""
import argparse
import hashlib
import importlib.util
import json
import re
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
from zipfile import ZipFile

import numpy as np

ROOT=Path(__file__).resolve().parent
PIN="ba42e57d46d7c4096ce3937127d7929b0c54c832"
SOURCE_MAP_SHA256="225916876afe15cebb8b680758fc88bb22bbe4a61dc5936a059cc51ac7ec82c4"

def bridge(module,sampler):
    rng=np.random.default_rng(20261123)
    u=rng.normal(size=(96,3,4))
    u/=np.linalg.norm(u,axis=-1,keepdims=True)
    u=np.concatenate((u,u*np.array([1,-1,1])[None,:,None],
                      np.tile(np.array([1.,0.,0.,0.]),(1,3,1))))
    v=u[...,1:]
    s=(v*v).sum(-1)
    adj=(4*u[...,0]**2-1)/3
    e=np.stack([adj[:,j]-adj[:,k] for j,k in [(1,2),(2,0),(0,1)]],axis=1)
    w=u[...,0,None]*v
    t=np.stack([(w[:,j]*w[:,k]).sum(-1) for j,k in [(1,2),(2,0),(0,1)]],axis=1)
    z=module.operators(u)
    z_e=z["E"][:,:,0]
    z_t=z["T2"][:,:,0]
    np.testing.assert_allclose(t,z_t[:,[2,1,0]],atol=2e-14,rtol=0)
    np.testing.assert_allclose(e@e.T/3,(32/9)*(z_e@z_e.T/2),atol=2e-14,rtol=0)
    if sampler:
        # A constant spatial configuration of fourth roots has the requested windings on N=4.
        theta=np.arctan2(np.linalg.norm(v,axis=2),u[...,0])
        norm=np.linalg.norm(v,axis=2)
        factor=np.divide(np.sin(theta/4),norm,out=np.zeros_like(norm),where=norm>0)
        roots=np.concatenate([np.cos(theta/4)[...,None],factor[...,None]*v],axis=2)
        packet="".join(" ".join(f"{a:.17g}" for a in row.ravel())+"\n" for row in roots)
        out=subprocess.check_output([sampler,"holonomies"],input=packet,text=True)
        observed=np.array([list(map(float,line.split())) for line in out.splitlines()])
        np.testing.assert_allclose(observed,np.hstack((e,t)),atol=1e-13,rtol=0)
    return len(u)

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def fixed_windows(ana,data):
    """Differenced E, t0=0, with the starting time explicitly fixed."""
    c,m=data["E"]
    ids=np.arange(len(c))
    def matrix(subset):
        v=ana.connected(c,m,subset)
        return v[...,:-1]-v[...,1:]
    full=matrix(ids)
    norm=np.sqrt(abs(np.diagonal(full[...,0])))
    def masses(v):
        lev=ana.gevp_levels(v,0,norm)
        with np.errstate(invalid="ignore",divide="ignore"):
            return np.log(lev[:-1]/lev[1:])
    central=masses(full)
    reps=np.stack([masses(matrix(np.delete(ids,i))) for i in ids])
    se=ana.jk_err(reps)
    values=[]
    for start in (1,2,3):
        w=slice(start,start+2)
        wt=1/se[w]**2
        avg=(wt*central[w]).sum()/wt.sum()
        error=ana.jk_err((reps[:,w]*wt).sum(axis=1)/wt.sum())
        values.append((float(avg),float(error)))
    return values

def audit(sampler=None):
    with ZipFile(ROOT/"z4-controls.zip") as arch,TemporaryDirectory() as tmp:
        manifest=json.loads(arch.read("manifest.json"))
        assert manifest["revision"]==PIN
        blob_map=json.dumps(manifest["git_blobs"],sort_keys=True,separators=(",",":")).encode()
        assert hashlib.sha256(blob_map).hexdigest()==SOURCE_MAP_SHA256
        assert set(arch.namelist())==set(manifest["sha256"])|{"manifest.json"}
        for k,d in manifest["sha256"].items():
            b=arch.read(k)
            assert hashlib.sha256(b).hexdigest()==d
            if k.startswith("author/"):
                h=hashlib.sha1(f"blob {len(b)}".encode()+bytes([0])+b).hexdigest()
                assert h==manifest["git_blobs"][k]
        arch.extractall(tmp)
        root=Path(tmp)
        module=load(root/"author/i1-mc3/mc3.py","z4_mc3")
        tests=bridge(module,sampler)
        ana=load(root/"author/i1-mc3/analyse3.py","z4_analysis")
        archived=json.loads((root/"author/i1-mc3/results/analysis_prereg.json").read_bytes())["runs"]
        for beta in (1,2,4,64,256,1024,4096):
            assert any(r["D"]==3 and r["beta"]==beta for r in archived)
        at4096=next(r for r in archived if r["D"]==3 and r["beta"]==4096)
        assert all(at4096["ch"][k]["PLAT"] and abs(at4096["ch"][k]["mb3"]/ref-1)<.08
                   for k,ref in [("E",3.0125),("T2",3.0125),("A1",3.6028)])
        print(f"{tests} holonomy triples; archived beta=4096 E, T2, A1:",*[round(at4096["ch"][ch]["mb3"],5) for ch in ("E","T2","A1")])
        measured=json.loads((root/"rerun/prereg.json").read_bytes())["runs"]
        measured+=json.loads((root/"rerun/prereg_T48.json").read_bytes())["runs"]
        for beta,tag in ((2,"d3_b2"),(4,"d3_b4"),(4,"d3_b4_T48")):
            prefix=root/"rerun"/tag
            info,data,_=ana.load(str(prefix))
            author=json.loads((root/f"author/i1-mc3/results/{tag}.json").read_bytes())
            assert all(info[k]==author[k] for k in ("D","T","beta","NCH","NTHERM","NMEAS","seed"))
            assert all(info["pre"][k] for k in ("PRE1","PRE2","PRE3"))
            ref=next(r for r in measured if r["beta"]==beta and r["T"]==info["T"])
            record=next(r for r in archived if r["D"]==3 and r["beta"]==beta and r["T"]==info["T"])
            for ch in ("E","T2","A1"):
                m,_=ana.analyse_channel(*data[ch],float(beta))
                expected=ref["ch"][ch]
                assert m["PLAT"]==expected["PLAT"]
                np.testing.assert_allclose([m["m"],m["err"]],[expected["m"],expected["err"]],atol=2e-8,rtol=2e-7,equal_nan=True)
            print(f"beta {beta}, T {info['T']}, E rule and mass: G4 {ref['ch']['E']['PLAT']} {ref['ch']['E']['m']:.6g}, Z4 {record['ch']['E']['PLAT']} {record['ch']['E']['m']:.6g}")
            vals=fixed_windows(ana,data)
            print("differenced fixed-window masses, starts 1, 2, 3:", " ".join(f"{x:.5f}({e:.5f})" for x,e in vals))
        for label,script,extra in (("ctrl0","ctrl0.py",[]),("ctrl_diff","diffan.py",["ctrl"])):
            archive_dir=root/"rerun"
            target=root/(label+"-all.md")
            subprocess.run([sys.executable,"-B",root/"author/i1-mc3"/script,*extra,target,
                            "d3_b2","d3_b4","d3_b4_T48"],cwd=archive_dir,check=True,capture_output=True)
            def controls(path):
                raw=path.read_text(encoding="utf8")
                return re.findall(r"^  CTRL0-PLAT (.+)$",raw,re.M)
            want=controls(archive_dir/(label+".md"))+controls(archive_dir/(label+"_T48.md"))
            got=controls(target)
            assert len(got)==len(want)==3
            for a,b in zip(got,want,strict=True):
                pat=r"[-+]?\d+(?:\.\d+)?"
                assert re.sub(pat,"#",a)==re.sub(pat,"#",b)
                np.testing.assert_allclose(list(map(float,re.findall(pat,a))),list(map(float,re.findall(pat,b))),atol=2e-5,rtol=1e-6)
        print("one-site raw block analysis replayed; fixed-box and fixed-scale limits are distinct")

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--sampler",type=Path)
    a=p.parse_args()
    audit(a.sampler.resolve() if a.sampler else None)

"""Check archived observations, scientific reductions, recursive registers and formal scope."""
import argparse
import csv
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import runpy
import subprocess
import sys
from tempfile import TemporaryDirectory
from zipfile import ZipFile

import numpy as np
import analysis
import fits
import momenta

ROOT=Path(__file__).resolve().parent
G4=ROOT.parents[1]
BUILDERS=("scale","spectral-weight","blocking","minorization","electric-control","lean")
REVIEWS={"isotropic-review":("isotropic.md",),"electric-review":("electric.md",),
         "collective-review":("collective.md",),"methods-review":("methods.md",),
         "results-review":("results.md","README.md","methods.md"),"joint-review":("../../../joint-refinement/README.md","../../../joint-refinement/liminf.md"),
         "exterior-review":("../../../joint-refinement/exterior.md",)}
Z4_REVIEWS={"z4-liminf":("h1-liminf/LIMINF.md",),"z4-recovery":("g2-conv/SCALING_LIMIT.md",)}
SOURCES=(".gitattributes","README.md","isotropic.md","electric.md","methods.md","collective.md",
         "results.md","checks.md","Refinement.lean","mutations.json","calibration.py","analysis.py",
         "momenta.py","fits.py","electric.py","transfer-control.py","verify.py","matched.rs","samples.zip",
         "../two-site-gap/wilson_mc.rs","../all-readings/verify.py","../../site/check_site.py",
         "../../contact-blocks/verify.py","../../exterior/verify.py",
         "../../../joint-refinement/README.md","../../../joint-refinement/liminf.md","../../../joint-refinement/exterior.md","../../../joint-refinement/readback.py",
         "../../../joint-refinement/z4-controls.zip")

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def shared():
    spec=importlib.util.spec_from_file_location("register_checks",ROOT.parent/"all-readings/verify.py")
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.ROOT,m.BUILDERS,m.REVIEWS=ROOT,BUILDERS,REVIEWS
    return m

def check_rows(reducer,path,saved,count_numeric):
    stream=io.StringIO()
    reducer(path,stream)
    actual=list(csv.reader(io.StringIO(stream.getvalue())))
    expected=list(csv.reader(io.StringIO(saved.decode())))
    assert expected[0]==actual[0]
    for a,b in zip(actual[1:],expected[1:],strict=True):
        assert a[:-count_numeric]==b[:-count_numeric]
        np.testing.assert_allclose(np.array(a[-count_numeric:],float),np.array(b[-count_numeric:],float),
                                   rtol=3e-6,atol=2e-9,equal_nan=True)
    return len(actual)-1

def observations(z,sampler):
    streams=json.loads(z.read("samples.json"))
    assert len(streams)==len(set(streams))==70
    counts={}
    with ZipFile(ROOT/"samples.zip") as samples:
        assert set(samples.namelist())==set(streams) and len(samples.namelist())==len(streams)
        for name,digest in streams.items():
            mode,n,t,beta,seed,hot,burn,count,stride=Path(name).stem.split("_")
            n,t,burn,count=map(int,(n,t,burn,count))
            assert mode in ("open","sf","modes","smooth")
            raw=samples.read(name)
            assert sha(raw)==digest
            if mode=="sf":expected=count*8
            else:expected=count*(t+1)*(26 if mode=="modes" else 14)*4
            assert len(raw)==expected
            key=(mode,n,t,burn,count)
            counts[key]=counts.get(key,0)+1
            if mode in ("smooth","modes"):
                reference=samples.read(f"open_{n}_{t}_{beta}_{seed}_{hot}_{burn}_320_{stride}.bin")
                p=np.frombuffer(reference,"<f4").reshape(320,t+1,14)[:count,:,0]
                check=np.frombuffer(raw,"<f4").reshape(count,t+1,-1)[:,:,0]
                if mode=="smooth":np.testing.assert_array_equal(check,p)
                else:np.testing.assert_allclose(check,p,atol=6e-8,rtol=0)
        expected={}
        for n in (5,6,7,8,10):
            for key,m in [(("sf",n,n,192,256),2),(("sf",n,n,384,1024),2),
                          (("open",n,6*n,112,96),2),(("open",n,6*n,384,320),4),
                          (("smooth",n,6*n,384,192),2)]:
                expected[key]=m
            if n in (5,10):expected["open",n,8*n,160,144]=2
            if n in (5,7,10):expected["modes",n,6*n,384,192]=2
        assert counts==expected
        if sampler:
            subprocess.run([sampler,"check"],check=True)
            with TemporaryDirectory() as tmp:
                for mode in ("sf","open","smooth","modes"):
                    name=next(k for k in sorted(streams) if k.startswith(mode+"_5_"))
                    parts=Path(name).stem.split("_")
                    expected=samples.read(name)
                    original=int(parts[-2])
                    parts[-2]="2"
                    path=Path(tmp)/name
                    subprocess.run([sampler,*parts,path],check=True)
                    assert path.read_bytes()==expected[:len(expected)*2//original]

def verify(args):
    common=shared()
    source=(ROOT/"Refinement.lean").read_bytes()
    with ZipFile(ROOT/"evidence.zip") as z:
        manifest=json.loads(z.read("manifest.json"))
        assert set(z.namelist())==set(manifest["entries"])|{"manifest.json"}
        assert len(z.namelist())==len(manifest["entries"])+1 and set(manifest["sources"])==set(SOURCES)
        assert all(sha(z.read(k))==v for k,v in manifest["entries"].items())
        assert all(sha((ROOT/k).read_bytes())==v for k,v in manifest["sources"].items())
        regs=common.workers(z,source)
        with TemporaryDirectory() as folder,ZipFile(ROOT/"../../../joint-refinement/z4-controls.zip") as peer:
            common.ROOT=Path(folder)
            common.BUILDERS,common.REVIEWS=(),Z4_REVIEWS
            for pages in Z4_REVIEWS.values():
                for page in pages:
                    f=common.ROOT/page
                    f.parent.mkdir(parents=True,exist_ok=True)
                    f.write_bytes(peer.read("author/"+page))
            regs.extend(common.workers(z,source))
        compiler=runpy.run_path(str(G4/"contact-blocks/verify.py"))["check_compiler"]
        rec,count=compiler(z,"compiler",source,"Millennium.G4.Refinement")
        mutations=(ROOT/"mutations.json").read_bytes()
        assert count==8 and rec["mutations_sha256"]==sha(mutations)
        assert b"warning:" not in z.read("compiler/child/positive.log")
        for rule,item in zip(json.loads(mutations),rec["records"][1:],strict=True):
            name=rule["label"]
            assert item["label"]==name and item["exit_code"]!=0
            old,new=rule["find"].encode(),rule["replace"].encode()
            assert source.count(old)==1 and z.read("compiler/child/"+name+".lean")==source.replace(old,new)
            assert rule["diagnostic"].encode() in z.read("compiler/child/"+name+".log")
        regs.extend(("compiler","compiler/child"))
        native=runpy.run_path(str(G4/"exterior/verify.py"))
        native["verify_native"](z,source)
        assert json.loads(z.read("native/receipt.json"))["kernel_sha256"]==common.KERNEL
        if args.runtime:native["deep_replay"](z,regs,args.runtime,args.method)
        observations(z,args.sampler)
        for program in ("electric","transfer-control"):
            live=subprocess.check_output([sys.executable,"-B",ROOT/(program+".py")],text=True).splitlines()
            assert live==z.read("results/"+program+".txt").decode().splitlines()
        path=ROOT/"samples.zip"
        readings=z.read("results/readings.csv")
        nr=check_rows(analysis.write,path,readings,2)
        nm=check_rows(momenta.write,path,z.read("results/momenta.csv"),4)
        comp=list(fits.results(csv.DictReader(io.StringIO(readings.decode()))))
        saved=json.loads(z.read("results/fits.json"))
        for (name,*actual),(key,*old) in zip(comp,saved,strict=True):
            assert name==key
            np.testing.assert_allclose(actual,old,rtol=1e-8,atol=1e-9)
        peer_args=[sys.executable,"-B",ROOT/"../../../joint-refinement/readback.py"]
        if args.sampler:peer_args.extend(["--sampler",args.sampler])
        subprocess.run(peer_args,check=True)
    return dict(trajectory_files=70,spectral_and_scale_rows=nr,momentum_rows=nm,
                lean_declarations=count,rejected_mutations=5,registered_jobs=len(regs),
                registers_deep_replayed=len(regs) if args.runtime else 0,
                sampler_prefixes_regenerated=4 if args.sampler else 0)

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("runtime","method","sampler"):p.add_argument("--"+name,type=Path)
    args=p.parse_args()
    if bool(args.runtime)!=bool(args.method):p.error("supply both runtime and method")
    if args.sampler:args.sampler=args.sampler.resolve()
    print(json.dumps(verify(args),indent=2))

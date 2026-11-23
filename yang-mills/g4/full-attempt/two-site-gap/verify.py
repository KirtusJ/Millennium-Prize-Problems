"""Replay the G4 even-box Wilson checks and optionally re-execute native instruments."""
import argparse
import csv
from importlib.util import module_from_spec, spec_from_file_location
import io
import json
from math import isclose, isnan
from pathlib import Path
import runpy
import subprocess
import sys
from zipfile import ZipFile

import cube
import measurements

ROOT=Path(__file__).resolve().parent
G4=ROOT.parents[1]
BUILDERS=("valley","freeze","full-kernel","signed-cube","integration","cube-lean","dressing",
          "electric-gap","open-boundary","flat-slab")
REVIEWS={"kernel-review":("kernel.md",),"fast-review":("fast-vacuum.md",),
         "slab-review":("flat-slab.md",),"data-review":("measurements.md",),
         "chain-review":("README.md","flat-slab.md")}
SOURCES=(".gitattributes","README.md","kernel.md","flat-slab.md","fast-vacuum.md","measurements.md","checks.md",
         "TwoSite.lean","mutations.json","coefficients.csv","cube.py","quadrature.py","harmonic.py","controls.py",
         "wilson_mc.rs","measurements.py","wilson-blocks.zip","verify.py",
         "figures/starts.json","figures/starts.svg","figures/starts.receipt.txt",
         "../all-readings/verify.py","../../contact-blocks/verify.py","../../site/check_site.py","../../exterior/verify.py")


def shared():
    spec=spec_from_file_location("g4_worker_checks",ROOT.parent/"all-readings/verify.py")
    common=module_from_spec(spec)
    spec.loader.exec_module(common)
    common.ROOT,common.BUILDERS,common.REVIEWS=ROOT,BUILDERS,REVIEWS
    return common


def close(a,b):
    return (isnan(a) and isnan(b)) or isclose(a,b,rel_tol=2e-9,abs_tol=3e-12)


def measurements_check(archive,host):
    actual=io.StringIO()
    measurements.report(ROOT/"wilson-blocks.zip",actual)
    live=csv.reader(io.StringIO(actual.getvalue()))
    saved=csv.reader(io.StringIO(archive.read("controls/measurements.csv").decode()))
    assert next(live)==next(saved)
    rows=0
    for x,y in zip(live,saved,strict=True):
        assert x[:-2]==y[:-2] and all(close(float(a),float(b)) for a,b in zip(x[-2:],y[-2:])),(x,y)
        rows+=1
    spec=(ROOT/"figures/starts.json").read_bytes()
    plot=json.loads(spec)
    assert plot==measurements.start_plot(ROOT/"wilson-blocks.zip")
    svg=(ROOT/"figures/starts.svg").read_bytes()
    digest=shared().sha(svg)
    receipt=(ROOT/"figures/starts.receipt.txt").read_bytes()
    assert digest.encode() in receipt and b"SVG digest matches" in receipt
    if host:
        assert subprocess.check_output([host,"plot"],input=spec)==svg
        for test in (digest,"0"*64):
            obj=json.dumps({"plot":plot,"expected_svg_sha256":test})
            res=subprocess.run([host,"instrument","visualization.ranges",obj],capture_output=True)
            assert (b"SVG digest matches" in res.stdout)==(test==digest)
            if test==digest:
                assert res.returncode==0 and res.stdout.splitlines()==receipt.splitlines()
    return rows


def rerun_samples(exe):
    with ZipFile(ROOT/"wilson-blocks.zip") as data:
        for seed in (101,1102,1304):
            name,=[s for s in data.namelist() if f"-seed{seed}-" in s]
            opened,l,t,b,s,h,burn,n,sweeps=measurements.SPEC.fullmatch(name).groups()
            sample=subprocess.check_output([exe,l,t,b,s,h,burn,n,sweeps,"open" if opened else "periodic"])
            assert sample.splitlines()==data.read(name).splitlines(),name


def verify(args):
    common=shared()
    source=(ROOT/"TwoSite.lean").read_bytes()
    comp=runpy.run_path(str(G4/"contact-blocks/verify.py"))["check_compiler"]
    native=runpy.run_path(str(G4/"exterior/verify.py"))
    with ZipFile(ROOT/"evidence.zip") as archive:
        m=common.record(archive,"manifest.json")
        assert set(archive.namelist())==set(m["entries"])|{"manifest.json"}
        assert len(archive.namelist())==len(m["entries"])+1 and set(m["sources"])==set(SOURCES)
        assert all(common.sha(archive.read(k))==v for k,v in m["entries"].items())
        assert all(common.sha((ROOT/k).read_bytes())==v for k,v in m["sources"].items())
        registers=common.workers(archive,source)
        receipt,count=comp(archive,"compiler",source,"Millennium.G4.TwoSite")
        mutations=(ROOT/"mutations.json").read_bytes()
        assert count==7 and receipt["mutations_sha256"]==common.sha(mutations)
        assert b"warning:" not in archive.read("compiler/child/positive.log")
        assert b"invalid field 'popcount'" in archive.read("development/missing-popcount.log")
        assert b"Invalid mutation label" in archive.read("development/mutation-label.log")
        for spec,item in zip(json.loads(mutations),receipt["records"][1:],strict=True):
            a,b,label=spec["find"].encode(),spec["replace"].encode(),spec["label"]
            assert source.count(a)==1 and item["label"]==label and item["exit_code"]!=0
            assert archive.read(f"compiler/child/{label}.lean")==source.replace(a,b)
            assert spec["diagnostic"].encode() in archive.read(f"compiler/child/{label}.log")
        registers.extend(("compiler","compiler/child"))
        assert common.record(archive,"native/receipt.json")["kernel_sha256"]==common.KERNEL
        native["verify_native"](archive,source)
        if args.runtime:
            native["deep_replay"](archive,registers,args.runtime,args.method)
        expected=list(csv.reader((ROOT/"coefficients.csv").read_text().splitlines()))
        assert expected[0]==["n","diagonal","mixed"] and len(expected)==20
        a,b=cube.projected_coeffs(18)
        assert expected[1:]==[[str(i),str(p),str(q)] for i,(p,q) in enumerate(zip(a,b))]
        assert a[2]-b[2]==cube.Q(3,4)
        intervals=[(10001871769,10001871770),(10031940150,10031940151),(10650411052,10650411053),
                   (14857870993,14858182415),(32208559549,39742782161)]
        for beta,limits in zip(map(cube.Q,["1/8","1/4","1/2","3/4","1"]),intervals):
            assert cube.outward(cube.ratio_bracket((a,b),beta),10)==limits
        for name in ("controls","harmonic"):
            live=subprocess.check_output([sys.executable,"-B",ROOT/(name+".py")],text=True).splitlines()
            saved=archive.read("controls/"+name+".txt").decode().splitlines()
            for line,want in zip(live,saved,strict=True):
                for x,y in zip(line.replace(","," ").split(),want.replace(","," ").split(),strict=True):
                    try:
                        assert close(float(x),float(y))
                    except ValueError:
                        assert x==y
        rows=measurements_check(archive,args.plot_host)
    if args.sampler:
        rerun_samples(args.sampler)
    return dict(lean_declarations=count,negative_compiles=len(json.loads(mutations)),registered_jobs=len(registers),
                deep_replayed=len(registers) if args.runtime else 0,measured_rows=rows,
                rational_coefficients=2*len(a),regenerated_streams=3 if args.sampler else 0)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("runtime","method","plot-host","sampler"):
        p.add_argument("--"+name,type=Path)
    args=p.parse_args()
    if bool(args.runtime)!=bool(args.method):
        p.error("Supply both --runtime and --method for deep replay.")
    print(json.dumps(verify(args),indent=2))

"""Check the Wilson sheet scaling and optionally replay the recursive PCP witnesses."""
import argparse
from importlib.util import module_from_spec, spec_from_file_location
import json
from math import isclose
from pathlib import Path
import runpy
import subprocess
import sys
from zipfile import ZipFile


ROOT=Path(__file__).resolve().parent
G4=ROOT.parents[1]
BUILDERS=("area","strip","rounding")
REVIEWS={"paper":("README.md","strip.md","../all-readings/area.md")}
SOURCES=("README.md","strip.md","checks.md","SheetScaling.lean","mutations.json","check.py","verify.py",
         "../all-readings/verify.py","../all-readings/sheet.py","../all-readings/area.md",
         "../../contact-blocks/verify.py","../../site/check_site.py","../../exterior/verify.py")


def research_evidence():
    # Reuse the earlier wire-format checks with this packet's sources and participant roles.
    base=spec_from_file_location("wilson_worker_records",ROOT.parent/"all-readings/verify.py")
    module=module_from_spec(base)
    base.loader.exec_module(module)
    module.ROOT,module.BUILDERS,module.REVIEWS=ROOT,BUILDERS,REVIEWS
    return module


def compare_control(recorded):
    current=json.loads(subprocess.check_output([sys.executable,"-B",ROOT/"check.py"]))
    for name in ("cubature","spatial_transfer"):
        for row,saved in zip(current.pop(name),recorded.pop(name),strict=True):
            assert row.keys()==saved.keys()
            for key,value in row.items():
                if isinstance(value,float):
                    assert isclose(value,saved[key],rel_tol=1e-12,abs_tol=2e-13)
                else:
                    assert value==saved[key]
    for name in ("growth","prefactor"):
        assert isclose(current.pop(name),recorded.pop(name),rel_tol=1e-13)
    assert current==recorded


def verify(runtime,method):
    common=research_evidence()
    compiler=runpy.run_path(str(G4/"contact-blocks/verify.py"))["check_compiler"]
    exterior=runpy.run_path(str(G4/"exterior/verify.py"))
    source=(ROOT/"SheetScaling.lean").read_bytes()
    with ZipFile(ROOT/"evidence.zip") as archive:
        manifest=common.record(archive,"manifest.json")
        entries=manifest["entries"]
        assert len(archive.namelist())==len(entries)+1 and set(archive.namelist())==set(entries)|{"manifest.json"}
        assert all(common.sha(archive.read(k))==v for k,v in entries.items())
        assert set(manifest["sources"])==set(SOURCES)
        assert all(common.sha((ROOT/k).read_bytes())==v for k,v in manifest["sources"].items())
        registers=common.workers(archive,source)
        candidate=common.lf(archive.read("rounding/draft/model_reply.txt"))
        signature=b"lemma edge_rounding (x y a b"
        assert signature in candidate and signature in source
        assert b"expected no space before" in archive.read("development/absolute-value.log")
        assert b"Mutation target must occur exactly once" in archive.read("development/selector.log")
        receipt,count=compiler(archive,"compiler",source,"Millennium.G4.SheetScaling")
        positive,*rejected=receipt["records"]
        assert count==5 and positive["label"]=="positive" and positive["exit_code"]==0
        assert b"warning:" not in archive.read("compiler/child/positive.log")
        mutations=(ROOT/"mutations.json").read_bytes()
        assert len(rejected)==4 and receipt["mutations_sha256"]==common.sha(mutations)
        for spec,item in zip(json.loads(mutations),rejected,strict=True):
            old,new,label=spec["find"].encode(),spec["replace"].encode(),spec["label"]
            assert source.count(old)==1 and item["label"]==label and item["exit_code"]!=0
            assert archive.read(f"compiler/child/{label}.lean")==source.replace(old,new)
            assert spec["diagnostic"].encode() in archive.read(f"compiler/child/{label}.log")
        registers.extend(("compiler","compiler/child"))
        native=common.record(archive,"native/receipt.json")
        assert native["kernel_sha256"]==common.KERNEL
        assert all(item["start_ns"]<=item["exit_observed_ns"]<=item["readback_ns"] for item in native["observations"])
        exterior["verify_native"](archive,source)
        compare_control(common.record(archive,"controls.json"))
        if runtime:
            exterior["deep_replay"](archive,registers,runtime,method)
    return dict(declarations=count,rejected_mutations=len(rejected),native_cases=len(native["observations"]),
                registers_replayed=len(registers) if runtime else 0,registers=len(registers),
                source_sha256=common.sha(source),series_coefficients_checked=41)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime",type=Path)
    parser.add_argument("--method",type=Path)
    args=parser.parse_args()
    if bool(args.runtime)!=bool(args.method):
        parser.error("Supply both runtime and method for deep replay.")
    print(json.dumps(verify(args.runtime,args.method),indent=2))

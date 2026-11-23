"""Replay the published relative-slice controls and inspect their PCP receipts."""
import argparse
import hashlib
import json
from pathlib import Path
import runpy
import subprocess
import sys
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent
AUDITS = ('compression', 'cylinder', 'discriminate', 'sample', 'finite', 'final')
SOURCE = "ae865e8b285f3206f869be9acab8b5f5ec24e3fc566fb12a366068db37341404"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def verify(runtime,method):
    ext = runpy.run_path(str(ROOT.parent/"exterior/verify.py"))
    compiler = runpy.run_path(str(ROOT.parent/"contact-blocks/verify.py"))["check_compiler"]
    source = (ROOT/"RelativeGap.lean").read_bytes()
    assert digest(source)==SOURCE
    registers = ["compiler","compiler/child"]
    with ZipFile(ROOT/"evidence.zip") as archive:
        def read(name):
            return json.loads(archive.read(name))
        manifest = read("manifest.json")
        entries = manifest["entries"]
        assert len(archive.namelist())==len(entries)+1
        assert set(archive.namelist())==set(entries)|{"manifest.json"}
        assert all(digest(archive.read(k))==v for k,v in entries.items())
        assert all(digest((ROOT/k).read_bytes())==v for k,v in manifest["sources"].items())
        assert read("controls.json")==json.loads(subprocess.check_output([sys.executable,"-B",ROOT/"controls.py"]))
        receipt,count = compiler(archive,"compiler",source,"Millennium.G4.RelativeGap")
        assert count==8
        mutations = (ROOT/"mutations.json").read_bytes()
        assert receipt["mutations_sha256"]==digest(mutations)
        good,*bad = receipt["records"]
        assert good["label"]=="positive" and good["exit_code"]==0
        for spec,row in zip(json.loads(mutations),bad,strict=True):
            name=spec["label"]
            old,new=spec["find"].encode(),spec["replace"].encode()
            assert row["label"]==name and row["exit_code"]!=0 and source.count(old)==1
            assert archive.read(f"compiler/child/{name}.lean")==source.replace(old,new)
            assert spec["diagnostic"].encode() in archive.read(f"compiler/child/{name}.log")
        for name in (*AUDITS,"formalizer"):
            receipt=read(name+"/receipt.json")
            labels=["draft","challenge"] if name=="formalizer" else ["challenge"]
            if name=="formalizer":
                candidate=archive.read(name+"/draft/model_reply.txt")
                assert candidate.decode().replace("\r\n","\n").strip() in source.decode()
            else:
                candidate=archive.read("inputs/"+name+".txt")
            assert receipt["passed"] and receipt["candidate_sha256"]==digest(candidate)
            assert archive.read(name+"/review-task.txt").endswith(candidate)
            if name=="final":
                assert candidate==b"\n".join((ROOT/k).read_bytes() for k in ("README.md","compression.md","wilson-box.md","controls.md"))
            registers.append(name)
            for label,row in zip(labels,receipt["records"],strict=True):
                path=name+"/"+label
                raw=archive.read(path+"/receipt.json")
                child=json.loads(raw)
                assert row["label"]==label and row["passed"] and row["exit_code"]==0
                assert row["start_ns"]<=row["exit_observed_ns"]<=row["readback_ns"]
                assert digest(raw)==row["receipt_sha256"]
                assert child["verification"]["ok"] and child["exit_code"]==0
                assert child["readback_sha256"]==digest(archive.read(path+"/model_reply.txt"))
                registers.append(path)
        ext["verify_native"](archive,source)
        if runtime:
            ext["deep_replay"](archive,registers,runtime,method)
    return {"lean":count,"rejected_mutations":len(bad),"native_cases":9,
            "deep_registers":len(registers) if runtime else 0,"source":SOURCE}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime",type=Path)
    parser.add_argument("--method",type=Path)
    args=parser.parse_args()
    if bool(args.runtime)!=bool(args.method):
        parser.error("Supply both --runtime and --method")
    print(json.dumps(verify(args.runtime,args.method),indent=2))

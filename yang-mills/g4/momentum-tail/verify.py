"""Verify the momentum-tail evidence and optionally replay the PCP registers."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import runpy
import subprocess
import sys
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parent
REVIEWS=("paths","mass","fejer","initial","final","direction_initial","direction")
BLOBS={"README.md":"989090190a0554de5cb54ada4e786321f8c71cc8",
       "JointMomentum.lean":"cdd7216db40a75c10a600df03a2491fd8bae78d5",
       "check.py":"3e34ba8a60b9b4c1300e7d8abd3fbf5e5a01ba0c"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def verify(runtime,method):
    ext=runpy.run_path(str(ROOT.parent/"exterior/verify.py"))
    compiler=runpy.run_path(str(ROOT.parent/"contact-blocks/verify.py"))["check_compiler"]
    src=(ROOT/"MomentumTail.lean").read_bytes()
    folders=["compiler","compiler/child"]
    with ZipFile(ROOT/"evidence.zip") as z:
        def read(k):
            return json.loads(z.read(k))
        manifest=read("manifest.json")
        entries=manifest["entries"]
        assert len(z.namelist())==len(entries)+1
        assert set(z.namelist())==set(entries)|{"manifest.json"}
        assert all(sha(z.read(k))==v for k,v in entries.items())
        assert all(sha((ROOT/k).read_bytes())==v for k,v in manifest["sources"].items())
        assert read("controls.json")==json.loads(subprocess.check_output([sys.executable,"-B",ROOT/"check.py"]))
        receipt,count=compiler(z,"compiler",src,"Millennium.G4.MomentumTail")
        assert count==4
        specs=(ROOT/"mutations.json").read_bytes()
        assert sha(specs)==receipt["mutations_sha256"]
        good,*bad=receipt["records"]
        assert good["label"]=="positive" and good["exit_code"]==0
        for spec,row in zip(json.loads(specs),bad,strict=True):
            name=spec["label"]
            old,new=spec["find"].encode(),spec["replace"].encode()
            assert row["label"]==name and row["exit_code"]!=0 and src.count(old)==1
            assert z.read(f"compiler/child/{name}.lean")==src.replace(old,new)
            assert spec["diagnostic"].encode() in z.read(f"compiler/child/{name}.log")
        for name in (*REVIEWS,"formalizer"):
            generated=name=="formalizer"
            if generated:
                data=z.read(f"{name}/draft/model_reply.txt")
                assert data.decode().replace("\r\n","\n").strip() in src.decode()
            else:
                data=z.read("inputs/"+name+".txt")
            if name=="final":
                assert data.endswith((ROOT/"README.md").read_bytes())
            if name=="direction":
                assert data.endswith((ROOT/"directions.md").read_bytes())
            parent=read(f"{name}/receipt.json")
            assert parent["passed"] and parent["method"]["matches_required"]
            assert sha(data)==parent["candidate_sha256"]
            assert z.read(f"{name}/review-task.txt").endswith(b"SOURCE TO AUDIT:\n"+data)
            folders.append(name)
            for label,row in zip(("draft","challenge") if generated else ("challenge",),parent["records"],strict=True):
                folder=f"{name}/{label}"
                raw=z.read(folder+"/receipt.json")
                child=json.loads(raw)
                assert row["label"]==label and row["passed"] and row["exit_code"]==0
                assert row["start_ns"]<=row["exit_observed_ns"]<=row["readback_ns"]
                assert sha(raw)==row["receipt_sha256"] and child["verification"]["ok"] and child["exit_code"]==0
                assert child["readback_sha256"]==sha(z.read(folder+"/model_reply.txt"))
                folders.append(folder)
        for name,blob in BLOBS.items():
            data=z.read("c4/"+name).replace(b"\r\n",b"\n")
            assert hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()==blob
        names=re.findall(rb"^#print axioms (\w+)\r?$",z.read("c4/JointMomentum.lean"),re.M)
        log=z.read("c4/lean.log")
        assert b"error:" not in log and b"sorryAx" not in log
        assert len(names)==6 and re.findall(rb"^'JointMomentum\.(\w+)'",log,re.M)==names
        checks=z.read("c4/arithmetic.log")
        assert b"160 signed path pairs" in checks and b"375 three-dimensional" in checks
        ext["verify_native"](z,src)
        if runtime:
            ext["deep_replay"](z,folders,runtime,method)
    return {"lean":count,"rejected":len(bad),"recompiled_c4":len(names),"native":9,
            "registers":len(folders),"deep":len(folders) if runtime else 0,"source":sha(src)}


if __name__=="__main__":
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--runtime",type=Path)
    cli.add_argument("--method",type=Path)
    args=cli.parse_args()
    if bool(args.runtime)!=bool(args.method):
        cli.error("Supply both --runtime and --method")
    print(json.dumps(verify(args.runtime,args.method),indent=2))

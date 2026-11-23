"""Verify the scalar block proof evidence; optionally replay its PCP registers."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import runpy
import subprocess
import sys
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent
SOURCE = "8917a409631ce3e4430d56cba68faf7c8541853073c5126eba7d545d4e452a20"
REVIEWS = ("ward","heat","spectrum","peer","profile","witness","uniform","ab4",
           "z4","enclosure","first_final","second_final","final")
DRAFTS = ("path_formalizer","harmonic_formalizer")
PAPERS = ("README.md","wilson.md","heat.md","spectrum.md","correlation-time.md")
PEER_BLOBS = {"WilsonRate.lean":"d270cb5a1a685077e228e0d6a6e0b5b437ec01bd",
              "check.py":"c0b5fb170e183f1972463de7aebb0420cd96613a",
              "heat.md":"640efe04b1baf1483e9861f7dc5dc384fa572f37",
              "spectrum.md":"185a8445555370baa4fd98256631794adec6d4b9",
              "ward.md":"241c461f44cbd673617dff7660755db334529d8c"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check_job(archive, name, source):
    is_draft = name in DRAFTS
    labels = ("draft","challenge") if is_draft else ("challenge",)
    candidate = archive.read(f"{name}/draft/model_reply.txt" if is_draft else f"inputs/{name}.txt")
    if is_draft:
        assert " ".join(candidate.decode().split()) in " ".join(source.decode().split())
    if name in ("final","second_final"):
        full=b"\n".join((ROOT/k).read_bytes() for k in PAPERS)
        if name=="second_final":
            wrong=b"upper bound on the operator norm"
            assert candidate.count(wrong)==1 and candidate.replace(wrong,b"lower bound on the operator norm")==full
        else:
            assert digest(full).encode() in candidate and b"lower bound on the operator norm" in candidate
    if name=="enclosure":
        assert candidate.endswith(digest((ROOT/"enclosure.py").read_bytes()).encode())
    parent=json.loads(archive.read(f"{name}/receipt.json"))
    assert parent["passed"] and parent["candidate_sha256"]==digest(candidate)
    assert parent["method"]["matches_required"]
    assert archive.read(f"{name}/review-task.txt").endswith(b"SOURCE TO AUDIT:\n"+candidate)
    registers=[name]
    for label,row in zip(labels,parent["records"],strict=True):
        path=f"{name}/{label}"
        raw=archive.read(path+"/receipt.json")
        child=json.loads(raw)
        assert row["label"]==label and row["passed"] and row["exit_code"]==0
        assert row["start_ns"]<=row["exit_observed_ns"]<=row["readback_ns"]
        assert digest(raw)==row["receipt_sha256"] and child["verification"]["ok"]
        assert child["exit_code"]==0 and child["readback_sha256"]==digest(archive.read(path+"/model_reply.txt"))
        registers.append(path)
    return registers


def check_peer(archive):
    for name,blob in PEER_BLOBS.items():
        raw=archive.read("c4/"+name).replace(b"\r\n",b"\n")
        assert hashlib.sha1(f"blob {len(raw)}\0".encode()+raw).hexdigest()==blob
    candidate=archive.read("inputs/peer.txt")
    for name in ("ward.md","heat.md","spectrum.md"):
        assert archive.read("c4/"+name) in candidate
    symbols=re.findall(rb"^#print axioms (\w+)\r?$",archive.read("c4/WilsonRate.lean"),re.M)
    log=archive.read("c4/lean.log")
    assert len(symbols)==9 and b"error:" not in log and b"sorryAx" not in log
    assert re.findall(rb"^'WilsonRate\.(\w+)'",log,re.M)==symbols
    controls=archive.read("c4/controls.log")
    assert all(term in controls for term in (b"144 oriented",b"Five root-dependent",b"36 four-dimensional",
                                             b"order 3, lag 128"))
    return len(symbols)


def verify(runtime, method):
    ext=runpy.run_path(str(ROOT.parent/"exterior/verify.py"))
    compiler=runpy.run_path(str(ROOT.parent/"contact-blocks/verify.py"))["check_compiler"]
    source=(ROOT/"BlockCriticality.lean").read_bytes()
    assert digest(source)==SOURCE
    registers=["compiler","compiler/child"]
    with ZipFile(ROOT/"evidence.zip") as archive:
        manifest=json.loads(archive.read("manifest.json"))
        entries=manifest["entries"]
        assert len(archive.namelist())==len(entries)+1
        assert set(archive.namelist())==set(entries)|{"manifest.json"}
        assert all(digest(archive.read(k))==v for k,v in entries.items())
        assert all(digest((ROOT/k).read_bytes())==v for k,v in manifest["sources"].items())
        current=json.loads(subprocess.check_output([sys.executable,"-B",ROOT/"controls.py"]))
        assert current==json.loads(archive.read("controls.json"))
        receipt,count=compiler(archive,"compiler",source,"Millennium.G4.BlockCriticality")
        assert count==10
        mutations=(ROOT/"mutations.json").read_bytes()
        assert receipt["mutations_sha256"]==digest(mutations)
        good,*bad=receipt["records"]
        assert good["label"]=="positive" and good["exit_code"]==0
        for spec,row in zip(json.loads(mutations),bad,strict=True):
            name=spec["label"]
            old,new=spec["find"].encode(),spec["replace"].encode()
            assert row["label"]==name and row["exit_code"]!=0 and source.count(old)==1
            assert archive.read(f"compiler/child/{name}.lean")==source.replace(old,new)
            assert spec["diagnostic"].encode() in archive.read(f"compiler/child/{name}.log")
        for name in (*REVIEWS,*DRAFTS):
            registers.extend(check_job(archive,name,source))
        for name in ("z4-timeout","final-timeout","enclosure-timeout"):
            assert not json.loads(archive.read(f"development/{name}/receipt.json"))["passed"]
            assert json.loads(archive.read(f"development/{name}/challenge/model_process.json"))["returncode"]!=0
        full=b"\n".join((ROOT/k).read_bytes() for k in PAPERS)
        assert archive.read("development/final-timeout/review-task.txt").endswith(full)
        assert archive.read("development/enclosure-timeout/review-task.txt").endswith((ROOT/"enclosure.py").read_bytes())
        for name in ("integral","notation"):
            assert not json.loads(archive.read(f"development/{name}/receipt.json"))["passed"]
            assert b"error:" in archive.read(f"development/{name}/positive.log")
        peer=check_peer(archive)
        ext["verify_native"](archive,source)
        if runtime:
            ext["deep_replay"](archive,registers,runtime,method)
    return {"lean_declarations":count,"c4_recompiled":peer,"rejected_mutations":len(bad),
            "native_cases":9,"hosted_registers":len(registers),
            "deep_registers":len(registers) if runtime else 0,"source":SOURCE}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime",type=Path)
    parser.add_argument("--method",type=Path)
    args=parser.parse_args()
    if bool(args.runtime)!=bool(args.method):
        parser.error("Supply both --runtime and --method")
    print(json.dumps(verify(args.runtime,args.method),indent=2))

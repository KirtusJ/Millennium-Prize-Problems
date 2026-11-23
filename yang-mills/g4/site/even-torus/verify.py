"""Replay the published even-torus site controls and inspect their PCP receipts."""
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
AUDITS = ('audit', 'critical', 'peer', 'final')
SOURCE = "09bb8ab4cd8fe6fe6f415f19a93e503833f9dfb1e5e5c18c7b48366e91c80bea"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def verify(runtime,method):
    ext = runpy.run_path(str(ROOT.parents[1]/"exterior/verify.py"))
    compiler = runpy.run_path(str(ROOT.parents[1]/"contact-blocks/verify.py"))["check_compiler"]
    source = (ROOT/"EvenSite.lean").read_bytes()
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
        receipt,count = compiler(archive,"compiler",source,"Millennium.G4.EvenSite")
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
                assert candidate==b"\n".join((ROOT/k).read_bytes() for k in ('README.md', 'periodic-tail.md', 'criticality.md'))
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
        assert not read("development/receipt.json")["passed"]
        failed = read("development/challenge/model_process.json")
        assert failed["returncode"] != 0
        assert read("development/challenge/receipt.json")["exit_code"] != 0
        peer_blobs = {"PeriodicCriticality.lean":"7cba1b8785b09a3265d91f67f9158730705e5d02",
                      "check.py":"a285b77d43117dd3b207d426589ce1977d372f19",
                      "pressure.md":"dd73b4fbd136943ba2a8667309c76b3e74fe7e44",
                      "spectral.md":"8ebc105895d08c80efe7e0712e1315f5af9ff26f"}
        for name,blob in peer_blobs.items():
            raw = archive.read("c4/"+name).replace(b"\r\n",b"\n")
            assert hashlib.sha1(f"blob {len(raw)}\0".encode()+raw).hexdigest()==blob
        reviewed = b"\n".join(archive.read("c4/"+name) for name in ("spectral.md","pressure.md"))
        assert archive.read("inputs/peer.txt").endswith(reviewed)
        symbols = re.findall(rb"^#print axioms (\w+)\r?$",archive.read("c4/PeriodicCriticality.lean"),re.M)
        log = archive.read("c4/lean.log")
        assert len(symbols)==10 and b"error:" not in log and b"sorryAx" not in log
        assert re.findall(rb"^'PeriodicCriticality\.(\w+)'",log,re.M)==symbols
        numerical = archive.read("c4/runtime.log")
        assert all(prefix in numerical for prefix in (b"54 reflected blocks",b"Five SU(2) Haar",
                   b"64 raw quaternion",b"36 exact-box time Fourier"))
        ext["verify_native"](archive,source)
        if runtime:
            ext["deep_replay"](archive,registers,runtime,method)
    return {"lean":count,"c4_recompiled":len(symbols),"rejected_mutations":len(bad),"native_cases":9,
            "deep_registers":len(registers) if runtime else 0,"source":SOURCE}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime",type=Path)
    parser.add_argument("--method",type=Path)
    args=parser.parse_args()
    if bool(args.runtime)!=bool(args.method):
        parser.error("Supply both --runtime and --method")
    print(json.dumps(verify(args.runtime,args.method),indent=2))

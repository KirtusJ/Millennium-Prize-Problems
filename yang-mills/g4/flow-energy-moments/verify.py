"""Replay the deterministic controls and inspect the PCP compiler and review receipts."""
import argparse
import json
from pathlib import Path
import runpy
import subprocess
import sys
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent
SHA = "b203d99776530f4aff1e9f61e84260fbfe343e63cd1bc1c35565c1275a73d362"
AUDITS = ("analytic","inverse","edge","obstruction","jackson")


def verify(runtime, method):
    shared = runpy.run_path(str(ROOT.parent/"exterior/verify.py"))
    check_compiler = runpy.run_path(str(ROOT.parent/"contact-blocks/verify.py"))["check_compiler"]
    digest = shared["digest"]
    source = (ROOT/"EnergyMoments.lean").read_bytes()
    assert digest(source) == SHA
    registers = ["compiler","compiler/child"]
    with ZipFile(ROOT/"evidence.zip") as z:
        def read(path):
            return json.loads(z.read(path))
        manifest = read("manifest.json")
        entries = manifest["entries"]
        assert set(z.namelist()) == set(entries) | {"manifest.json"}
        assert len(z.namelist()) == len(entries)+1
        assert all(digest(z.read(n)) == h for n,h in entries.items())
        assert manifest["source"] == SHA and manifest["control"] == digest((ROOT/"control.py").read_bytes())
        outputs = subprocess.check_output([sys.executable,"-B",ROOT/"control.py"])
        assert json.loads(outputs) == read("controls.json")
        receipt,count = check_compiler(z,"compiler",source,"Millennium.G4.EnergyMoments")
        assert count == 7
        mutations = (ROOT/"mutations.json").read_bytes()
        assert receipt["mutations_sha256"] == digest(mutations)
        good,*adverse = receipt["records"]
        assert good["label"] == "positive" and good["exit_code"] == 0
        for spec,r in zip(json.loads(mutations),adverse,strict=True):
            label = spec["label"]
            old,new = spec["find"].encode(),spec["replace"].encode()
            assert source.count(old)==1 and r["label"]==label and r["exit_code"]!=0
            assert z.read(f"compiler/child/{label}.lean")==source.replace(old,new)
            assert spec["diagnostic"].encode() in z.read(f"compiler/child/{label}.log")
        for name in (*AUDITS,"formalizer"):
            parent = read(f"{name}/receipt.json")
            regs = ["draft","challenge"] if name=="formalizer" else ["challenge"]
            if name=="formalizer":
                candidate = z.read(f"{name}/draft/model_reply.txt")
                assert candidate.decode().replace("\r\n","\n").strip() in source.decode()
            else:
                candidate = z.read(f"inputs/energy-moments-{name}.txt")
            assert parent["passed"] and parent["candidate_sha256"] == digest(candidate)
            assert z.read(f"{name}/review-task.txt").endswith(candidate)
            registers.append(name)
            for child,row in zip(regs,parent["records"],strict=True):
                path = f"{name}/{child}"
                child_receipt = z.read(path+"/receipt.json")
                rec = json.loads(child_receipt)
                assert row["label"]==child and row["passed"] and row["exit_code"]==0
                assert row["start_ns"]<=row["exit_observed_ns"]<=row["readback_ns"]
                assert row["receipt_sha256"]==digest(child_receipt)
                assert rec["exit_code"]==0 and rec["verification"]["ok"]
                assert rec["readback_sha256"]==digest(z.read(path+"/model_reply.txt"))
                registers.append(path)
        shared["verify_native"](z,source)
        if runtime:
            shared["deep_replay"](z,registers,runtime,method)
    return {"lean":count,"mutations":len(adverse),"native_cases":9,
            "deep_registers":len(registers) if runtime else 0,"source":SHA}


if __name__=="__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime",type=Path)
    parser.add_argument("--method",type=Path)
    args = parser.parse_args()
    if bool(args.runtime)!=bool(args.method):
        parser.error("Supply both --runtime and --method")
    print(json.dumps(verify(args.runtime,args.method),indent=2))

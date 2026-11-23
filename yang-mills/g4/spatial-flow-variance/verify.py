"""Verify the mathematical controls, Lean receipts and optional hosted PCP replay."""
import argparse
import json
from pathlib import Path
import runpy
import subprocess
import sys
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent


def verify(runtime, method):
    common = runpy.run_path(str(ROOT.parent/"exterior/verify.py"))
    check_compiler = runpy.run_path(str(ROOT.parent/"contact-blocks/verify.py"))["check_compiler"]
    digest = common["digest"]
    source = (ROOT/"MagneticVariance.lean").read_bytes()
    with ZipFile(ROOT/"evidence.zip") as archive:
        def read_json(name):
            return json.loads(archive.read(name))

        manifest = read_json("manifest.json")
        entries = manifest["entries"]
        assert set(archive.namelist()) == set(entries) | {"manifest.json"}
        assert len(archive.namelist()) == len(entries)+1
        assert all(digest(archive.read(n)) == h for n,h in entries.items())
        assert manifest["source"] == digest(source)
        assert manifest["control"] == digest((ROOT/"control.py").read_bytes())
        assert read_json("controls.json") == json.loads(subprocess.check_output(
            [sys.executable,"-B",ROOT/"control.py"]))
        rec, count = check_compiler(archive,"compiler",source,"Millennium.G4.MagneticVariance")
        assert count == 9
        mutations = (ROOT/"mutations.json").read_bytes()
        assert rec["mutations_sha256"] == digest(mutations)
        good, *adverse = rec["records"]
        assert good["exit_code"] == 0 and good["label"] == "positive"
        for spec, run in zip(json.loads(mutations),adverse,strict=True):
            label = spec["label"]
            old, new = spec["find"].encode(), spec["replace"].encode()
            assert source.count(old) == 1 and run["label"] == label and run["exit_code"] != 0
            assert source.replace(old,new) == archive.read(f"compiler/child/{label}.lean")
            assert spec["diagnostic"].encode() in archive.read(f"compiler/child/{label}.log")
        registers = ["compiler","compiler/child"]
        jobs = {"probability":"floor","force":"floor","band":"band","concentration":"sharp",
                "formalizer":None}
        for name, packet in jobs.items():
            parent = read_json(f"{name}/receipt.json")
            assert parent["passed"] and parent["verification"]["ok"]
            if packet:
                candidate = archive.read(f"inputs/magnetic-{packet}-brief.txt")
            else:
                candidate = archive.read("formalizer/draft/model_reply.txt")
                assert candidate.decode().replace("\r\n","\n").strip() in source.decode()
            assert parent["candidate_sha256"] == digest(candidate)
            assert archive.read(f"{name}/review-task.txt").endswith(candidate)
            expected = ["challenge"] if packet else ["draft","challenge"]
            assert [r["label"] for r in parent["records"]] == expected
            registers.append(name)
            for record in parent["records"]:
                child = name+"/"+record["label"]
                assert record["passed"] and record["exit_code"] == 0
                assert record["start_ns"] <= record["exit_observed_ns"] <= record["readback_ns"]
                assert record["receipt_sha256"] == digest(archive.read(child+"/receipt.json"))
                receipt = read_json(child+"/receipt.json")
                assert receipt["exit_code"] == 0 and receipt["verification"]["ok"]
                assert receipt["readback_sha256"] == digest(archive.read(child+"/model_reply.txt"))
                registers.append(child)
        common["verify_native"](archive, source)
        if runtime:
            common["deep_replay"](archive,registers,runtime,method)
    return {"lean":count,"rejected":len(adverse),"native_cases":9,
            "deep_registers":len(registers) if runtime else 0,"source_sha256":digest(source)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime",type=Path)
    parser.add_argument("--method",type=Path)
    args = parser.parse_args()
    if bool(args.runtime) != bool(args.method):
        parser.error("Supply both --runtime and --method")
    print(json.dumps(verify(args.runtime,args.method),indent=2))

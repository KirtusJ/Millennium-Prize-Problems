"""Check the published local-spectral-weight evidence and optionally replay PCP registers."""
import argparse
import hashlib
import json
from pathlib import Path
import runpy
import subprocess
import sys
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent
SOURCE_SHA = "b5a6e5f8ce8c0f738fe90e1a572bfdffc891984ec18001bc1d33d5cee96f8eec"
AUDITS = ("fourier", "weights", "lag", "asymptotic", "upperwindow", "preliminary", "final")
MATH_FILES = ("README.md", "momentum.md", "lags.md")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def check_audits(archive, source):
    registers = []
    for name in (*AUDITS, "formalizer"):
        receipt = json.loads(archive.read(f"{name}/receipt.json"))
        children = ["draft", "challenge"] if name == "formalizer" else ["challenge"]
        if name == "formalizer":
            candidate = archive.read("formalizer/draft/model_reply.txt")
            assert candidate.decode().replace("\r\n", "\n").strip() in source.decode()
        else:
            candidate = archive.read(f"inputs/local-edge-{name}.txt")
        assert receipt["passed"] and receipt["candidate_sha256"] == sha(candidate)
        assert archive.read(f"{name}/review-task.txt").endswith(candidate)
        if name == "final":
            assert candidate == b"\n".join((ROOT/n).read_bytes() for n in MATH_FILES)
        registers.append(name)
        for child, process in zip(children, receipt["records"], strict=True):
            path = f"{name}/{child}"
            child_bytes = archive.read(path+"/receipt.json")
            result = json.loads(child_bytes)
            assert process["label"] == child and process["passed"] and process["exit_code"] == 0
            assert process["start_ns"] <= process["exit_observed_ns"] <= process["readback_ns"]
            assert process["receipt_sha256"] == sha(child_bytes)
            assert result["exit_code"] == 0 and result["verification"]["ok"]
            assert result["readback_sha256"] == sha(archive.read(path+"/model_reply.txt"))
            registers.append(path)
    return registers


def verify(runtime, method):
    source = (ROOT/"LocalScalarEdge.lean").read_bytes()
    assert sha(source) == SOURCE_SHA
    shared = runpy.run_path(str(ROOT.parent/"exterior/verify.py"))
    compiler = runpy.run_path(str(ROOT.parent/"contact-blocks/verify.py"))["check_compiler"]
    with ZipFile(ROOT/"evidence.zip") as archive:
        manifest = json.loads(archive.read("manifest.json"))
        entries = manifest["entries"]
        assert len(archive.namelist()) == len(entries)+1
        assert set(archive.namelist()) == set(entries) | {"manifest.json"}
        assert all(sha(archive.read(k)) == v for k,v in entries.items())
        assert manifest["source"] == SOURCE_SHA
        assert manifest["control"] == sha((ROOT/"control.py").read_bytes())
        replay = subprocess.check_output([sys.executable, "-B", ROOT/"control.py"])
        assert json.loads(replay) == json.loads(archive.read("controls.json"))
        result,count = compiler(archive, "compiler", source, "Millennium.G4.LocalScalarEdge")
        assert count == 9
        mutations = (ROOT/"mutations.json").read_bytes()
        assert result["mutations_sha256"] == sha(mutations)
        good,*bad = result["records"]
        assert good["label"] == "positive" and good["exit_code"] == 0
        for spec,row in zip(json.loads(mutations), bad, strict=True):
            label = spec["label"]
            old,new = spec["find"].encode(),spec["replace"].encode()
            assert source.count(old) == 1 and row["label"] == label and row["exit_code"] != 0
            assert archive.read(f"compiler/child/{label}.lean") == source.replace(old,new)
            assert spec["diagnostic"].encode() in archive.read(f"compiler/child/{label}.log")
        registers = ["compiler", "compiler/child"] + check_audits(archive, source)
        shared["verify_native"](archive, source)
        if runtime:
            shared["deep_replay"](archive, registers, runtime, method)
    return {"lean":count, "mutations":len(bad), "native_cases":9,
            "deep_registers":len(registers) if runtime else 0, "source":SOURCE_SHA}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", type=Path)
    parser.add_argument("--method", type=Path)
    args = parser.parse_args()
    if bool(args.runtime) != bool(args.method):
        parser.error("Supply both --runtime and --method")
    print(json.dumps(verify(args.runtime,args.method), indent=2))

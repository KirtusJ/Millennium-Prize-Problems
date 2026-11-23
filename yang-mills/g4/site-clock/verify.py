"""Verify the site-clock evidence and optionally replay the PCP OS registers."""
import argparse
from difflib import unified_diff
import hashlib
import json
from pathlib import Path
import re
import runpy
import subprocess
import sys
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parent
REVIEWS = ("clock", "chebyshev", "forest", "initial", "clarified", "spectra", "final",
           "envelope_initial", "envelope")
PAPERS = ("README.md", "certificate.md", "precision-limit.md", "clock.py")
A4_BLOBS = {
    "README.md": "29a991f1801da0a9552be8aa4399bf24a05cbe18",
    "SiteScalar.lean": "ddb7a312f3ebbe717f3f78ec49511bc071128300",
    "check_scalar.py": "8d1a4c7ad59ea7917f58acd994ed26b0ccc6903f",
    "check_strip.py": "681393b2ddb5f1ae484b4caa7eddff47b98a292a",
}
FINGERPRINT = "7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def verify_release_delta(archive):
    baseline = archive.read("inputs/spectra.txt").decode()
    remaining = baseline.split("\n\n" + PAPERS[0] + "\n\n", 1)[1]
    changes = []
    for index, name in enumerate(PAPERS):
        if index + 1 < len(PAPERS):
            previous, remaining = remaining.split("\n\n" + PAPERS[index + 1] + "\n\n", 1)
        else:
            previous = remaining
        current = (ROOT / name).read_bytes().decode().replace("\r\n", "\n")
        changes.extend(unified_diff(previous.splitlines(keepends=True), current.splitlines(keepends=True),
                                    fromfile="previous/" + name, tofile="release/" + name, n=3))
    assert changes and archive.read("inputs/final.txt").decode().split("\n", 1)[1] == "".join(changes)


def verify_workers(archive, source):
    verify_release_delta(archive)
    folders = []
    for name in (*REVIEWS, "formalizer"):
        generated = name == "formalizer"
        if generated:
            candidate = archive.read(name + "/draft/model_reply.txt")
            assert candidate.decode().replace("\r\n", "\n").strip() in source.decode()
        else:
            candidate = archive.read("inputs/" + name + ".txt")
        if name == "envelope":
            assert candidate == (ROOT / "envelope.md").read_bytes()
        parent = json.loads(archive.read(name + "/receipt.json"))
        assert parent["passed"] and parent["method"]["matches_required"]
        assert parent["method"]["release_fingerprint"] == FINGERPRINT
        assert sha(candidate) == parent["candidate_sha256"]
        assert archive.read(name + "/review-task.txt").endswith(b"SOURCE TO AUDIT:\n" + candidate)
        folders.append(name)
        for role, record in zip(("draft", "challenge") if generated else ("challenge",),
                                parent["records"], strict=True):
            folder = f"{name}/{role}"
            raw = archive.read(folder + "/receipt.json")
            child = json.loads(raw)
            assert record["label"] == role and record["passed"] and record["exit_code"] == 0
            assert record["start_ns"] <= record["exit_observed_ns"] <= record["readback_ns"]
            assert sha(raw) == record["receipt_sha256"] and child["verification"]["ok"]
            assert child["exit_code"] == 0
            assert child["readback_sha256"] == sha(archive.read(folder + "/model_reply.txt"))
            folders.append(folder)
    return folders


def verify_a4(archive):
    for name, blob in A4_BLOBS.items():
        data = archive.read("a4/" + name).replace(b"\r\n", b"\n")
        header = f"blob {len(data)}\0".encode()
        assert hashlib.sha1(header + data).hexdigest() == blob
    lean = archive.read("a4/SiteScalar.lean")
    names = re.findall(rb"^#print axioms (?:YangMills\.SiteScalar\.)?(\w+)\r?$", lean, re.M)
    log = archive.read("a4/lean.log")
    assert len(names) == 7 and b"sorryAx" not in log and b"error:" not in log
    assert re.findall(rb"^'YangMills\.SiteScalar\.(\w+)'", log, re.M) == names
    controls = archive.read("a4/arithmetic.log")
    assert b"192 exact reflected" in controls and b"972 displaced" in controls
    assert b"182 exact buffered clock bounds" in controls
    return len(names)


def verify(runtime, method):
    exterior = runpy.run_path(str(ROOT.parent / "exterior/verify.py"))
    check_compiler = runpy.run_path(str(ROOT.parent / "contact-blocks/verify.py"))["check_compiler"]
    source = (ROOT / "SiteClock.lean").read_bytes()
    with ZipFile(ROOT / "evidence.zip") as archive:
        manifest = json.loads(archive.read("manifest.json"))
        entries = manifest["entries"]
        assert len(archive.namelist()) == len(entries) + 1
        assert set(archive.namelist()) == set(entries) | {"manifest.json"}
        assert all(sha(archive.read(k)) == digest for k, digest in entries.items())
        assert all(sha((ROOT / k).read_bytes()) == digest for k, digest in manifest["sources"].items())
        checks = json.loads(subprocess.check_output([sys.executable, "-B", ROOT / "check.py"]))
        assert checks == json.loads(archive.read("controls.json"))
        receipt, count = check_compiler(archive, "compiler", source, "Millennium.G4.SiteClock")
        spec = (ROOT / "mutations.json").read_bytes()
        assert count == 5 and sha(spec) == receipt["mutations_sha256"]
        good, *failures = receipt["records"]
        assert good["label"] == "positive" and good["exit_code"] == 0
        for mutation, record in zip(json.loads(spec), failures, strict=True):
            label = mutation["label"]
            old, new = mutation["find"].encode(), mutation["replace"].encode()
            assert record["label"] == label and record["exit_code"] != 0 and source.count(old) == 1
            assert archive.read(f"compiler/child/{label}.lean") == source.replace(old, new)
            assert mutation["diagnostic"].encode() in archive.read(f"compiler/child/{label}.log")
        folders = verify_workers(archive, source) + ["compiler", "compiler/child"]
        a4 = verify_a4(archive)
        exterior["verify_native"](archive, source)
        if runtime:
            exterior["deep_replay"](archive, folders, runtime, method)
    return {"lean": count, "rejected": len(failures), "a4_lean": a4, "native_cases": 9,
            "pcp_registers": len(folders), "deep_replayed": len(folders) if runtime else 0,
            "source_sha256": sha(source), "controls": checks}


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--runtime", type=Path)
    cli.add_argument("--method", type=Path)
    options = cli.parse_args()
    if bool(options.runtime) != bool(options.method):
        cli.error("Supply both --runtime and --method for deep replay.")
    print(json.dumps(verify(options.runtime, options.method), indent=2))

"""Verify the fixed-volume Wilson calculation and optionally replay its PCP registers."""
import argparse
import hashlib
import json
from math import isclose, pi
from pathlib import Path
import runpy
import subprocess
import sys
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parent
SOURCES = {"README.md", "proof.md", "determinant.md", "step.md", "box-size.md", "execution.md",
           "PeriodicZeroModes.lean", "mutations.json", "check.py", "quadrature.py", "size_check.py", "verify.py"}
REVIEWS = ("pivot", "forest", "expansion", "coefficient", "determinant", "step", "full", "finite", "size")
PAPERS = {"full": ("proof.md", "determinant.md"), "finite": ("README.md", "step.md"),
          "size": ("box-size.md",)}
METHOD = "7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707"
KERNEL = "d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def lf(data):
    return data.replace(b"\r\n", b"\n")


def report(archive, entry):
    return json.loads(archive.read(entry))


def check_workers(archive, source):
    registers = []
    for name in (*REVIEWS, "formalizer"):
        parent = report(archive, name + "/receipt.json")
        method = parent["method"]
        assert parent["passed"] and parent["verification"]["ok"]
        assert method["matches_required"] and method["files"] == 58
        assert method["release_fingerprint"] == METHOD
        generated = name == "formalizer"
        if generated:
            candidate = archive.read(name + "/draft/model_reply.txt")
            assert lf(candidate) in lf(source)
        else:
            candidate = archive.read("inputs/" + name + ".txt")
        if name in PAPERS:
            chunks = []
            for filename in PAPERS[name]:
                chunks.extend([filename.encode(), lf((ROOT / filename).read_bytes())])
            assert lf(candidate).split(b"\n\n", 1)[1] == b"\n\n".join(chunks)
        assert sha(candidate) == parent["candidate_sha256"]
        task = archive.read(name + "/review-task.txt")
        assert task.endswith(b"SOURCE TO AUDIT:\n" + candidate)
        registers.append(name)
        roles = ("draft", "challenge") if generated else ("challenge",)
        for role, item in zip(roles, parent["records"], strict=True):
            folder = name + "/" + role
            raw = archive.read(folder + "/receipt.json")
            child = json.loads(raw)
            model = report(archive, folder + "/model_process.json")
            prompt = lf(archive.read(folder + "/delivered_prompt.txt"))
            reply = archive.read(folder + "/model_reply.txt")
            expected_prompt = lf(task if role == "challenge" else archive.read("inputs/formalizer.txt"))
            # The provider strips terminal newlines. A generated Windows reply can
            # carry its own CRLF inside the enclosing review task.
            assert lf(prompt).endswith(expected_prompt.rstrip(b"\r\n"))
            assert model["prompt_sha256"] == sha(prompt) and model["output_sha256"] == sha(lf(reply))
            assert model["returncode"] == 0 and not model["unexpected_item_types"]
            assert model["start_ns"] <= model["exit_observed_ns"] <= model["post_exit_readback_ns"]
            assert item["label"] == role and item["passed"] and item["exit_code"] == 0
            assert item["start_ns"] <= item["exit_observed_ns"] <= item["readback_ns"]
            assert item["receipt_sha256"] == sha(raw)
            assert child["exit_code"] == 0 and child["verification"]["ok"]
            assert child["readback_sha256"] == sha(reply)
            registers.append(folder)
    return registers


def check_quadrature(archive):
    saved = report(archive, "quadrature.json")
    run = json.loads(subprocess.check_output([sys.executable, "-B", ROOT / "quadrature.py"]))
    assert saved["samples"] == run["samples"] == 65536
    assert saved["shell"] == run["shell"] == [0.25, 0.75]
    assert [row["beta"] for row in run["estimates"]] == [1e8, 1e32]
    for row, record in zip(run["estimates"], saved["estimates"], strict=True):
        assert row.keys() == record.keys()
        assert all(isclose(row[k], record[k], rel_tol=1e-6, abs_tol=1e-6) for k in row)
    large = run["estimates"][-1]
    assert abs(large["coefficient"] - 1/(8*pi**2)) < 0.00015
    assert abs(large["mean_scaled_action"] - 3) < 0.03
    assert abs(large["unit_laplace_transform"] - 1/8) < 0.003
    return run


def verify(runtime, method):
    exterior = runpy.run_path(str(ROOT.parent / "exterior/verify.py"))
    check_compiler = runpy.run_path(str(ROOT.parent / "contact-blocks/verify.py"))["check_compiler"]
    source = (ROOT / "PeriodicZeroModes.lean").read_bytes()
    with ZipFile(ROOT / "evidence.zip") as archive:
        manifest = report(archive, "manifest.json")
        entries = manifest["entries"]
        assert set(archive.namelist()) == set(entries) | {"manifest.json"}
        assert len(archive.namelist()) == len(entries) + 1
        assert all(sha(archive.read(k)) == digest for k, digest in entries.items())
        assert set(manifest["sources"]) == SOURCES
        assert all(sha((ROOT / k).read_bytes()) == digest for k, digest in manifest["sources"].items())
        checks = json.loads(subprocess.check_output([sys.executable, "-B", ROOT / "check.py"]))
        assert checks == report(archive, "controls.json")
        sizes = json.loads(subprocess.check_output([sys.executable, "-B", ROOT / "size_check.py"]))
        recorded_sizes = report(archive, "size_check.json")
        assert sizes["sides"] == recorded_sizes["sides"]
        assert isclose(sizes["unit_torus_log_determinant"], recorded_sizes["unit_torus_log_determinant"], abs_tol=1e-6)
        assert all(isclose(a, b, abs_tol=1e-6) for a, b in
                   zip(sizes["spectral_finite_parts"], recorded_sizes["spectral_finite_parts"], strict=True))
        quadrature = check_quadrature(archive)
        registers = check_workers(archive, source)
        receipt, count = check_compiler(archive, "compiler", source, "Millennium.G4.PeriodicZeroModes")
        positive, *rejected = receipt["records"]
        mutations = (ROOT / "mutations.json").read_bytes()
        assert count == 7 and positive["label"] == "positive" and positive["exit_code"] == 0
        assert b"warning:" not in archive.read("compiler/child/positive.log")
        assert len(rejected) == 5 and sha(mutations) == receipt["mutations_sha256"]
        for spec, item in zip(json.loads(mutations), rejected, strict=True):
            old, new, label = spec["find"].encode(), spec["replace"].encode(), spec["label"]
            assert item["label"] == label and item["exit_code"] != 0 and source.count(old) == 1
            assert archive.read(f"compiler/child/{label}.lean") == source.replace(old, new)
            assert spec["diagnostic"].encode() in archive.read(f"compiler/child/{label}.log")
        registers.extend(("compiler", "compiler/child"))
        native = report(archive, "native/receipt.json")
        assert native["kernel_sha256"] == KERNEL
        assert all(c["start_ns"] <= c["exit_observed_ns"] <= c["readback_ns"] for c in native["observations"])
        exterior["verify_native"](archive, source)
        if runtime:
            exterior["deep_replay"](archive, registers, runtime, method)
    return {"lean": count, "rejected": len(rejected), "native_cases": len(native["observations"]),
            "pcp_registers": len(registers), "deep_replayed": len(registers) if runtime else 0,
            "source_sha256": sha(source), "controls": checks, "quadrature": quadrature, "box_sizes": sizes}


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--runtime", type=Path)
    cli.add_argument("--method", type=Path)
    args = cli.parse_args()
    if bool(args.runtime) != bool(args.method):
        cli.error("Supply both --runtime and --method for deep replay.")
    print(json.dumps(verify(args.runtime, args.method), indent=2))

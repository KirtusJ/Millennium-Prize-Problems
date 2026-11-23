"""Verify the slab attempt, its figure, and optionally its archived PCP registers."""
import argparse
from fractions import Fraction
import hashlib
import json
from math import exp, isclose, sqrt
from pathlib import Path
import runpy
import subprocess
import sys
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parent
BUILDERS = ("chain", "electric", "parity", "magnetic", "identity", "formalizer", "shell", "profile")
PAPERS = {"construction-review": ("README.md", "construction.md"), "electric-review": ("electric.md",),
          "magnetic-review": ("magnetic.md",), "resolutions-review": ("resolutions.md",),
          "profile-review": ("profile.md", "electric.md")}
SOURCES = {".gitattributes", "README.md", "construction.md", "electric.md", "magnetic.md", "resolutions.md",
           "profile.md", "execution.md", "FullAttempt.lean", "mutations.json", "controls.py", "transfer_check.py",
           "profile_check.py", "verify.py",
           "figures/slab.json", "figures/slab.svg", "figures/slab.receipt.txt"}
METHOD = "7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707"
DESCRIPTOR = "9f5998dd75e921afe490687783787847916428f7ee7bcea410a88dad04646fb0"
KERNEL = "d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def lf(data):
    return data.replace(b"\r\n", b"\n")


def record(archive, name):
    return json.loads(archive.read(name))


def check_workers(archive, source):
    registers = []
    for name in (*BUILDERS, *PAPERS):
        parent = record(archive, name+"/receipt.json")
        assert parent["passed"] and parent["verification"]["ok"] and not parent["independent_party_review"]
        method = parent["method"]
        assert method["matches_required"] and method["files"] == 58
        assert method["release_fingerprint"] == METHOD and method["core_descriptor_sha256"] == DESCRIPTOR
        request = archive.read("inputs/"+name+".txt")
        if name in PAPERS:
            chunks = []
            for paper in PAPERS[name]:
                chunks.extend([paper.encode(), lf((ROOT/paper).read_bytes())])
            assert lf(request).split(b"\n\n", 1)[1] == b"\n\n".join(chunks)
            candidate, roles = request, ("challenge",)
        else:
            candidate = archive.read(name+"/draft/model_reply.txt")
            roles = ("draft", "challenge")
        if name == "formalizer":
            assert lf(candidate) in lf(source)
        assert digest(candidate) == parent["candidate_sha256"]
        review = archive.read(name+"/review-task.txt")
        assert review.endswith(b"SOURCE TO AUDIT:\n"+candidate)
        registers.append(name)
        for role, item in zip(roles, parent["records"], strict=True):
            folder = name+"/"+role
            raw = archive.read(folder+"/receipt.json")
            child = json.loads(raw)
            model = record(archive, folder+"/model_process.json")
            prompt = lf(archive.read(folder+"/delivered_prompt.txt"))
            reply = archive.read(folder+"/model_reply.txt")
            task = review if role == "challenge" else request
            # On Windows the enclosing text writer also serializes the embedded reply's CRLF.
            assert lf(prompt).endswith(lf(task).rstrip(b"\r\n"))
            assert digest(prompt) == model["prompt_sha256"] and digest(lf(reply)) == model["output_sha256"]
            assert model["returncode"] == 0 and not model["unexpected_item_types"]
            assert model["start_ns"] <= model["exit_observed_ns"] <= model["post_exit_readback_ns"]
            assert item["label"] == role and item["passed"] and item["exit_code"] == 0
            assert item["start_ns"] <= item["exit_observed_ns"] <= item["readback_ns"]
            assert digest(raw) == item["receipt_sha256"]
            assert child["exit_code"] == 0 and child["verification"]["ok"]
            assert child["method"] == method and digest(reply) == child["readback_sha256"]
            registers.append(folder)
    return registers


def check_figure(host):
    folder = ROOT/"figures"
    spec_bytes = (folder/"slab.json").read_bytes()
    spec = json.loads(spec_bytes)
    spatial, temporal = spec["series"]
    assert spec["x_domain"] == [0, 8] and spec["y_domain"] == [0, 1]
    assert len(spatial["data"]) == len(temporal["data"]) == 9
    for k in range(9):
        edge = sqrt(1+12*4**k)
        for series, value in ((spatial, (edge-1)/(edge+1)), (temporal, exp(-1))):
            index, lo, hi = series["data"][k]
            assert index == k and Fraction(lo) == Fraction(hi) == Fraction(round(value*10**6), 10**6)
    svg = (folder/"slab.svg").read_bytes()
    receipt = (folder/"slab.receipt.txt").read_bytes()
    assert digest(svg).encode() in receipt and b"SVG digest matches" in receipt
    assert b"18 rows including 0 intervals" in receipt
    if host:
        assert subprocess.check_output([host, "plot"], input=spec_bytes) == svg
        request = {"plot": spec, "expected_svg_sha256": digest(svg)}
        output = subprocess.check_output([host, "instrument", "visualization.ranges", json.dumps(request)])
        assert lf(output) == lf(receipt)
    return digest(svg)


def run_program(name):
    return json.loads(subprocess.check_output([sys.executable, "-B", ROOT/(name+".py")]))


def verify(runtime, method, plot_host):
    exterior = runpy.run_path(str(ROOT.parent/"exterior/verify.py"))
    check_compiler = runpy.run_path(str(ROOT.parent/"contact-blocks/verify.py"))["check_compiler"]
    source = (ROOT/"FullAttempt.lean").read_bytes()
    with ZipFile(ROOT/"evidence.zip") as archive:
        manifest = record(archive, "manifest.json")
        entries = manifest["entries"]
        assert set(archive.namelist()) == set(entries) | {"manifest.json"}
        assert len(archive.namelist()) == len(entries)+1
        assert all(digest(archive.read(k)) == h for k,h in entries.items())
        assert set(manifest["sources"]) == SOURCES
        assert all(digest((ROOT/k).read_bytes()) == h for k,h in manifest["sources"].items())
        assert run_program("controls") == record(archive, "controls.json")
        assert run_program("profile_check") == record(archive, "profile.json")
        current = run_program("transfer_check")
        for row, saved in zip(current, record(archive, "transfer.json"), strict=True):
            assert row.keys() == saved.keys() and row["tetra_orbits"] == saved["tetra_orbits"] == 76
            assert all(isclose(row[k], saved[k], abs_tol=3e-6, rel_tol=0) for k in row)
        figure = check_figure(plot_host)
        registers = check_workers(archive, source)
        receipt, count = check_compiler(archive, "compiler", source, "Millennium.G4.FullAttempt")
        positive, *rejected = receipt["records"]
        mutations = (ROOT/"mutations.json").read_bytes()
        assert positive["label"] == "positive" and positive["exit_code"] == 0 and count == 8
        assert b"warning:" not in archive.read("compiler/child/positive.log")
        assert len(rejected) == 6 and digest(mutations) == receipt["mutations_sha256"]
        for spec, item in zip(json.loads(mutations), rejected, strict=True):
            old, new, label = spec["find"].encode(), spec["replace"].encode(), spec["label"]
            assert item["label"] == label and item["exit_code"] != 0 and source.count(old) == 1
            assert archive.read(f"compiler/child/{label}.lean") == source.replace(old, new)
            assert spec["diagnostic"].encode() in archive.read(f"compiler/child/{label}.log")
        registers.extend(("compiler", "compiler/child"))
        native = record(archive, "native/receipt.json")
        assert native["kernel_sha256"] == KERNEL
        assert all(c["start_ns"] <= c["exit_observed_ns"] <= c["readback_ns"] for c in native["observations"])
        exterior["verify_native"](archive, source)
        if runtime:
            exterior["deep_replay"](archive, registers, runtime, method)
    return {"source_sha256": digest(source), "declarations": count, "rejected_mutations": len(rejected),
            "native_cases": len(native["observations"]), "registers": len(registers),
            "registers_deep_replayed": len(registers) if runtime else 0, "magnetic_couplings": [r["g"] for r in current],
            "figure_sha256": figure, "figure_rerendered": bool(plot_host)}


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--runtime", type=Path, help="PCP_OS_Python directory for deep replay")
    cli.add_argument("--method", type=Path, help="corresponding PCP/Method packet")
    cli.add_argument("--plot-host", type=Path, help="pcpos executable from the pinned plotting branch")
    args = cli.parse_args()
    if bool(args.runtime) != bool(args.method):
        cli.error("Supply both --runtime and --method for deep replay.")
    print(json.dumps(verify(args.runtime, args.method, args.plot_host), indent=2))

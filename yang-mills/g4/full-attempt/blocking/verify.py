"""Verify the blocked Wilson transfer calculation and optionally replay its PCP registers."""
import argparse
import hashlib
import json
from math import isclose
from pathlib import Path
import runpy
import subprocess
import sys
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parent
G4 = ROOT.parents[1]
SOURCES = ("README.md", "checks.md", "Blocking.lean", "mutations.json", "check.py", "verify.py", "../transfer_check.py")
ROLES = {"blocking": ("draft", "challenge"), "formalizer": ("draft", "challenge"), "paper": ("challenge",),
         "hamiltonian": ("challenge",)}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def lf(data):
    return data.replace(b"\r\n", b"\n")


def verify(runtime, method):
    compiler = runpy.run_path(str(G4/"contact-blocks/verify.py"))["check_compiler"]
    exterior = runpy.run_path(str(G4/"exterior/verify.py"))
    base = runpy.run_path(str(ROOT.parent/"verify.py"))
    source = (ROOT/"Blocking.lean").read_bytes()
    folders = []
    with ZipFile(ROOT/"evidence.zip") as archive:
        def read(name):
            return json.loads(archive.read(name))

        manifest = read("manifest.json")
        assert set(archive.namelist()) == set(manifest["entries"]) | {"manifest.json"}
        assert len(archive.namelist()) == len(manifest["entries"])+1
        assert all(sha(archive.read(k)) == h for k,h in manifest["entries"].items())
        assert set(manifest["sources"]) == set(SOURCES)
        assert all(sha((ROOT/k).read_bytes()) == h for k,h in manifest["sources"].items())
        for name, roles in ROLES.items():
            req = archive.read("inputs/"+name+".txt")
            raw_review = archive.read(name+"/review-task.txt")
            parent = read(name+"/receipt.json")
            candidate = archive.read(name+"/draft/model_reply.txt") if "draft" in roles else req
            assert parent["passed"] and parent["verification"]["ok"]
            assert parent["method"]["release_fingerprint"] == base["METHOD"] and parent["method"]["files"] == 58
            assert parent["method"]["matches_required"] and parent["method"]["core_descriptor_sha256"] == base["DESCRIPTOR"]
            assert sha(candidate) == parent["candidate_sha256"] and raw_review.endswith(b"SOURCE TO AUDIT:\n"+candidate)
            if name == "paper":
                assert lf(req).endswith(b"\n\nREADME.md\n\n"+lf((ROOT/"README.md").read_bytes()))
            if name == "hamiltonian":
                heading = b"### Physical time at fixed spatial spacing\n"
                page = lf((ROOT/"checks.md").read_bytes()).split(heading,1)[1].split(b"### Director results",1)[0]
                paper = lf((ROOT/"README.md").read_bytes())
                source_packet = b"\n\n".join((b"README.md", paper, b"checks.md, physical-time section", heading+page))
                assert lf(req).split(b"\n\n",1)[1] == source_packet
            if name == "formalizer":
                assert lf(candidate).replace(b"field_simp [h] <;> ring", b"field_simp [h]\n  ring") in lf(source)
            folders.append(name)
            for role,item in zip(roles, parent["records"], strict=True):
                folder = name+"/"+role
                folders.append(folder)
                raw = archive.read(folder+"/receipt.json")
                child = json.loads(raw)
                model = read(folder+"/model_process.json")
                prompt = lf(archive.read(folder+"/delivered_prompt.txt"))
                answer = archive.read(folder+"/model_reply.txt")
                assert lf(prompt).endswith(lf(raw_review if role=="challenge" else req).rstrip(b"\r\n"))
                assert sha(raw) == item["receipt_sha256"] and item["label"] == role and item["passed"]
                assert item["start_ns"] <= item["exit_observed_ns"] <= item["readback_ns"] and item["exit_code"] == 0
                assert model["start_ns"] <= model["exit_observed_ns"] <= model["post_exit_readback_ns"]
                assert model["returncode"] == 0 and not model["unexpected_item_types"]
                assert sha(prompt) == model["prompt_sha256"] and sha(lf(answer)) == model["output_sha256"]
                assert child["readback_sha256"] == sha(answer) and child["verification"]["ok"]
        receipt, count = compiler(archive, "compiler", source, "Millennium.G4.Blocking")
        assert count == 4 and b"warning:" not in archive.read("compiler/child/positive.log")
        rejected = receipt["records"][1:]
        mutations = (ROOT/"mutations.json").read_bytes()
        assert len(rejected) == 3 and sha(mutations) == receipt["mutations_sha256"]
        for item,spec in zip(rejected, json.loads(mutations), strict=True):
            old, new, label = spec["find"].encode(), spec["replace"].encode(), spec["label"]
            assert item["label"] == label and item["exit_code"] != 0 and source.count(old) == 1
            assert archive.read(f"compiler/child/{label}.lean") == source.replace(old,new)
            assert spec["diagnostic"].encode() in archive.read(f"compiler/child/{label}.log")
        folders.extend(("compiler","compiler/child"))
        exterior["verify_native"](archive, source)
        native = read("native/receipt.json")
        assert native["kernel_sha256"] == base["KERNEL"]
        assert all(x["start_ns"] <= x["exit_observed_ns"] <= x["readback_ns"] for x in native["observations"])
        computed = json.loads(subprocess.check_output([sys.executable,"-B",ROOT/"check.py"]))
        recorded = read("matrix.json")
        for x,y in zip(computed["physical_time"]["electric_slopes"],recorded["physical_time"]["electric_slopes"],strict=True):
            assert isclose(x,y,rel_tol=0,abs_tol=1e-10)
        for key in ("hamiltonian_slope", "slope_without_vacuum_term"):
            assert isclose(computed["physical_time"][key],recorded["physical_time"][key],rel_tol=0,abs_tol=1e-10)
        for row, saved in zip(computed["pairings"],recorded["pairings"],strict=True):
            assert all(row[k] == saved[k] for k in ("g","states","length"))
            assert isclose(row["link_ratio"],saved["link_ratio"],abs_tol=1e-10)
            for p,s in zip(row["pairings"],saved["pairings"],strict=True):
                assert p["n"] == s["n"]
                assert all(isclose(p[k],s[k],rel_tol=0,abs_tol=2e-10) for k in ("measured","formula"))
        if runtime:
            exterior["deep_replay"](archive,folders,runtime,method)
    return {"declarations":count, "rejected":len(rejected), "native_cases":len(native["observations"]),
            "registers":len(folders), "deep_replayed":len(folders) if runtime else 0,
            "magnetic_pairings":sum(len(row["pairings"]) for row in computed["pairings"]),
            "physical_time_slope":computed["physical_time"]["hamiltonian_slope"], "source_sha256":sha(source)}


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--runtime",type=Path)
    cli.add_argument("--method",type=Path)
    args = cli.parse_args()
    if bool(args.runtime) != bool(args.method):
        cli.error("Supply both the hosted runtime and its method packet for deep replay.")
    print(json.dumps(verify(args.runtime,args.method), indent=2))

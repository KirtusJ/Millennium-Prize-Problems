"""Verify archived inputs, PCP worker readbacks, Lean controls and native source."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import runpy
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent
G4 = ROOT.parents[1] / "g4"
METHOD = "7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707"
KERNEL = "d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f"


def digest(raw):
    return sha256(raw).hexdigest()


def verify(runtime, method):
    with ZipFile(ROOT / "evidence.zip") as archive:
        read = archive.read
        manifest = json.loads(read("manifest.json"))
        entries = manifest["entries"]
        assert len(archive.namelist()) == len(entries) + 1
        assert set(archive.namelist()) == set(entries) | {"manifest.json"}
        for name, pin in entries.items():
            assert digest(read(name)) == pin, name
        for name, pin in manifest["sources"].items():
            data = (ROOT/name).read_bytes()
            assert digest(data if name.endswith(".zip") else data.replace(b"\r\n", b"\n")) == pin, name
        folders = []
        for job in manifest["models"]:
            request = read("inputs/" + job + ".txt")
            parent = json.loads(read(job + "/receipt.json"))
            assert parent["passed"] and parent["verification"]["ok"]
            assert parent["method"]["release_fingerprint"] == METHOD and parent["method"]["files"] == 58
            roles = [item["label"] for item in parent["records"]]
            assert roles in (["challenge"], ["draft", "challenge"])
            candidate = request if roles == ["challenge"] else read(job + "/draft/model_reply.txt")
            assert digest(candidate) == parent["candidate_sha256"]
            folders.append(job)
            for item in parent["records"]:
                folder = job + "/" + item["label"]
                child_raw = read(folder + "/receipt.json")
                child = json.loads(child_raw)
                assert item["passed"] and digest(child_raw) == item["receipt_sha256"]
                assert child["verification"]["ok"] and child["method"] == parent["method"]
                assert digest(read(folder + "/model_reply.txt")) == child["readback_sha256"]
                process = json.loads(read(folder + "/model_process.json"))
                prompt = read(folder + "/delivered_prompt.txt").replace(b"\r\n", b"\n")
                assert process["returncode"] == 0 and digest(prompt) == process["prompt_sha256"]
                expected = request if item["label"] == "draft" else read(job + "/review-task.txt")
                # The host strips outer whitespace, including a numbered empty source line.
                assert prompt.replace(b"\r\n",b"\n").rstrip().endswith(expected.replace(b"\r\n",b"\n").rstrip())
                folders.append(folder)
        for job, pages in manifest["manuscripts"].items():
            request = read("inputs/" + job + ".txt").replace(b"\r\n", b"\n")
            assembled = []
            for name in pages:
                assembled += [("../../../joint-refinement/" + ROOT.name + "/" + name).encode(),
                              (ROOT/name).read_bytes().replace(b"\r\n", b"\n")]
            assert request.split(b"\n\n", 1)[1] == b"\n\n".join(assembled)
        source = (ROOT/"Checks.lean").read_bytes()
        checker = runpy.run_path(str(G4/"contact-blocks/verify.py"))["check_compiler"]
        rec, count = checker(archive, "compiler", source, "Millennium.G4.RareCoarse")
        controls = (ROOT/"mutations.json").read_bytes()
        assert count == 5 and rec["mutations_sha256"] == digest(controls)
        for mutation in json.loads(controls):
            label = mutation["label"]
            before = mutation["find"].encode()
            assert source.count(before) == 1
            assert read("compiler/child/" + label + ".lean") == source.replace(before, mutation["replace"].encode())
            assert mutation["diagnostic"].encode() in read("compiler/child/" + label + ".log")
        native = runpy.run_path(str(G4/"exterior/verify.py"))
        native["verify_native"](archive, source)
        assert json.loads(read("native/receipt.json"))["kernel_sha256"] == KERNEL
        folders.extend(["compiler", "compiler/child"])
        if runtime is not None:
            native["deep_replay"](archive, folders, runtime, method)
        print(f"{len(folders)} PCP registers, {count} Lean declarations, two rejected mutations")
        if runtime is not None:
            print("All registers replayed with stored objects.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--runtime", type=Path)
    parser.add_argument("--method", type=Path)
    args = parser.parse_args()
    if bool(args.runtime) != bool(args.method):
        parser.error("supply runtime and method together")
    verify(args.runtime, args.method)

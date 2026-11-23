"""Read back PCP and compiler evidence, mutation controls, and the archived source pins."""
import argparse
import hashlib
import json
from pathlib import Path
import runpy
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent
YM = ROOT.parents[1]
METHOD = "7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707"
KERNEL = "d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def verify(runtime, method):
    source = (ROOT/"Covariance.lean").read_bytes()
    with ZipFile(ROOT/"evidence.zip") as z:
        manifest = json.loads(z.read("manifest.json"))
        assert set(z.namelist()) == set(manifest["entries"]) | {"manifest.json"}
        assert len(z.namelist()) == len(set(z.namelist()))
        for name, digest in manifest["entries"].items():
            assert sha(z.read(name)) == digest, name
        for name, digest in manifest["sources"].items():
            data = (ROOT/name).read_bytes()
            assert sha(data if name.endswith((".zip",".npz")) else data.replace(b"\r\n",b"\n")) == digest, name
        regs = []
        for name in manifest["models"]:
            parent = json.loads(z.read(name+"/receipt.json"))
            assert parent["passed"] and parent["verification"]["ok"]
            assert parent["method"]["release_fingerprint"] == METHOD and parent["method"]["files"] == 58
            regs.append(name)
            request = z.read("inputs/"+name+".txt")
            roles = [r["label"] for r in parent["records"]]
            assert roles in (["challenge"], ["draft","challenge"])
            candidate = request if roles==["challenge"] else z.read(name+"/draft/model_reply.txt")
            assert sha(candidate) == parent["candidate_sha256"]
            for item in parent["records"]:
                prefix = name+"/"+item["label"]
                report = z.read(prefix+"/receipt.json")
                child = json.loads(report)
                reply = z.read(prefix+"/model_reply.txt")
                process = json.loads(z.read(prefix+"/model_process.json"))
                assert item["passed"] and child["verification"]["ok"] and child["method"] == parent["method"]
                assert sha(report) == item["receipt_sha256"] and sha(reply) == child["readback_sha256"]
                assert process["returncode"] == 0 and not process["unexpected_item_types"]
                prompt = z.read(prefix+"/delivered_prompt.txt").replace(b"\r\n",b"\n")
                assert sha(prompt) == process["prompt_sha256"]
                expected = request if item["label"]=="draft" else z.read(name+"/review-task.txt")
                # The Windows prompt writer serializes imported CRLF replies twice.
                assert prompt.replace(b"\r\n",b"\n").endswith(expected.replace(b"\r\n",b"\n").rstrip(b"\r\n"))
                regs.append(prefix)
        for key, pages in manifest["manuscripts"].items():
            received = z.read("inputs/"+key+".txt").replace(b"\r\n",b"\n").split(b"\n\n",1)[1]
            parts = []
            for page in pages:
                parts += [("../../../joint-refinement/"+(ROOT/page).resolve().relative_to(ROOT.parent).as_posix()).encode(),
                          (ROOT/page).read_bytes().replace(b"\r\n",b"\n")]
            assert received == b"\n\n".join(parts)
        formal = runpy.run_path(str(YM/"g4/contact-blocks/verify.py"))
        rec, count = formal["check_compiler"](z,"compiler",source,"Millennium.G4.Covariance")
        assert count==7 and rec["mutations_sha256"]==sha((ROOT/"mutations.json").read_bytes())
        for mutation in json.loads((ROOT/"mutations.json").read_bytes()):
            label = mutation["label"]
            assert source.count(mutation["find"].encode()) == 1
            assert z.read(f"compiler/child/{label}.lean") == source.replace(mutation["find"].encode(),mutation["replace"].encode())
            assert mutation["diagnostic"].encode() in z.read(f"compiler/child/{label}.log")
        regs += ["compiler","compiler/child"]
        native = runpy.run_path(str(YM/"g4/exterior/verify.py"))
        native["verify_native"](z,source)
        assert json.loads(z.read("native/receipt.json"))["kernel_sha256"] == KERNEL
        if runtime:
            native["deep_replay"](z,regs,runtime,method)
        print(len(regs),"PCP registers checked;",count,"Lean declarations; two rejected mutations")
        if runtime:
            print("All register chains and stored objects replayed.")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--runtime",type=Path)
    p.add_argument("--method",type=Path)
    args = p.parse_args()
    if bool(args.runtime) != bool(args.method):
        p.error("supply runtime and method together")
    verify(args.runtime,args.method)

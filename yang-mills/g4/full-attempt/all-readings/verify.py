"""Replay the G4 all-reading, optimizer, shorted-energy, and Wilson-sheet results."""
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
BUILDERS = ("labels","optimizer","components","sheet","filling","lean","energy")
REVIEWS = {"transfer-review": ("README.md","../blocking/README.md","../magnetic.md"),
           "optimizer-review": ("README.md","optimizer.md"),"sheet-review": ("area.md",),
           "energy-review": ("energy.md","README.md","optimizer.md")}
PROGRAMS = ("geometry","spectrum","sheet","nonabelian")
SOURCES = ("README.md","optimizer.md","area.md","energy.md","checks.md","AllReadings.lean","mutations.json",
           "verify.py",*(name+".py" for name in PROGRAMS),"../transfer_check.py","../magnetic.md",
           "../blocking/README.md","../../site/check_site.py","../../contact-blocks/verify.py","../../exterior/verify.py",
           "figures/comparison.json","figures/comparison.svg","figures/comparison.receipt.txt")
METHOD = "7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707"
DESCRIPTOR = "9f5998dd75e921afe490687783787847916428f7ee7bcea410a88dad04646fb0"
KERNEL = "d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def lf(raw):
    return raw.replace(b"\r\n",b"\n")


def record(archive, name):
    return json.loads(archive.read(name))


def workers(archive, source):
    registers = []
    for name in (*BUILDERS,*REVIEWS):
        parent = record(archive,name+"/receipt.json")
        method = parent["method"]
        assert parent["passed"] and parent["verification"]["ok"] and not parent["independent_party_review"]
        assert method["files"]==58 and method["matches_required"] and method["release_fingerprint"]==METHOD
        assert method["core_descriptor_sha256"]==DESCRIPTOR
        request = archive.read("inputs/"+name+".txt")
        if name in REVIEWS:
            delivered = b"\n\n".join(item for f in REVIEWS[name] for item in (f.encode(),lf((ROOT/f).read_bytes())))
            assert lf(request).split(b"\n\n",1)[1]==delivered
            roles,candidate = ("challenge",),request
        else:
            roles,candidate = ("draft","challenge"),archive.read(name+"/draft/model_reply.txt")
        if name=="lean":
            raw = lf(candidate).strip()
            assert raw.startswith(b"```lean\n") and raw.endswith(b"```")
            assert raw.split(b"\n",1)[1].rsplit(b"\n",1)[0] in lf(source)
        review = archive.read(name+"/review-task.txt")
        assert sha(candidate)==parent["candidate_sha256"] and review.endswith(b"SOURCE TO AUDIT:\n"+candidate)
        registers.append(name)
        for role,item in zip(roles,parent["records"],strict=True):
            folder = name+"/"+role
            report = archive.read(folder+"/receipt.json")
            child = json.loads(report)
            model = record(archive,folder+"/model_process.json")
            prompt = lf(archive.read(folder+"/delivered_prompt.txt"))
            reply = archive.read(folder+"/model_reply.txt")
            # The Windows prompt writer serializes embedded CRLF in a child's reply a second time.
            assert lf(prompt).endswith(lf(review if role=="challenge" else request).rstrip(b"\r\n"))
            assert sha(prompt)==model["prompt_sha256"] and sha(lf(reply))==model["output_sha256"]
            assert model["returncode"]==0 and not model["unexpected_item_types"]
            assert model["start_ns"]<=model["exit_observed_ns"]<=model["post_exit_readback_ns"]
            assert item["passed"] and item["exit_code"]==0 and item["label"]==role
            assert item["start_ns"]<=item["exit_observed_ns"]<=item["readback_ns"]
            assert sha(report)==item["receipt_sha256"] and child["exit_code"]==0 and child["verification"]["ok"]
            assert child["method"]==method and sha(reply)==child["readback_sha256"]
            registers.append(folder)
    return registers


def figure(host):
    from spectrum import plot_spec
    folder = ROOT/"figures"
    spec = (folder/"comparison.json").read_bytes()
    assert json.loads(spec)==plot_spec()
    svg = (folder/"comparison.svg").read_bytes()
    receipt = (folder/"comparison.receipt.txt").read_bytes()
    assert sha(svg).encode() in receipt and b"SVG digest matches" in receipt and b"16 rows" in receipt
    if host:
        assert subprocess.check_output([host,"plot"],input=spec)==svg
        for digest in (sha(svg),"0"*64):
            body = json.dumps({"plot":json.loads(spec),"expected_svg_sha256":digest})
            result = subprocess.run([host,"instrument","visualization.ranges",body],capture_output=True)
            if digest==sha(svg):
                assert result.returncode==0 and lf(result.stdout)==lf(receipt)
            else:
                assert b"SVG digest matches" not in result.stdout and (
                    result.returncode or b"differs" in result.stdout or b"mismatch" in result.stdout)
    return sha(svg)


def controls(archive):
    for name in PROGRAMS:
        result = json.loads(subprocess.check_output([sys.executable,"-B",ROOT/(name+".py")]))
        expected = record(archive,"controls/"+name+".json")
        if name=="nonabelian":
            current = result.pop("two_component_response")
            saved = expected.pop("two_component_response")
            assert current.keys()==saved.keys()
            for key in current:
                absolute = 2e-14 if key in ("largest_offdiagonal_gram","measured_energy_coefficient") else 2e-11
                assert isclose(current[key],saved[key],abs_tol=absolute,rel_tol=0)
        if name=="spectrum":
            for key in ("largest_norm","winding_norm","largest_higher_spin"):
                assert isclose(result["smallest_torus"].pop(key),expected["smallest_torus"].pop(key),rel_tol=5e-13)
        assert result==expected


def verify(runtime,method,plot_host):
    compiler = runpy.run_path(str(G4/"contact-blocks/verify.py"))["check_compiler"]
    exterior = runpy.run_path(str(G4/"exterior/verify.py"))
    source = (ROOT/"AllReadings.lean").read_bytes()
    with ZipFile(ROOT/"evidence.zip") as archive:
        manifest = record(archive,"manifest.json")
        entries = manifest["entries"]
        assert len(archive.namelist())==len(entries)+1 and set(archive.namelist())==set(entries)|{"manifest.json"}
        assert all(sha(archive.read(key))==digest for key,digest in entries.items())
        assert set(manifest["sources"])==set(SOURCES)
        assert all(sha((ROOT/key).read_bytes())==digest for key,digest in manifest["sources"].items())
        registers = workers(archive,source)
        receipt,count = compiler(archive,"compiler",source,"Millennium.G4.AllReadings")
        positive,*rejected = receipt["records"]
        assert positive["exit_code"]==0 and positive["label"]=="positive" and count==7
        assert b"warning:" not in archive.read("compiler/child/positive.log")
        mutations = (ROOT/"mutations.json").read_bytes()
        assert len(rejected)==5 and receipt["mutations_sha256"]==sha(mutations)
        for spec,run in zip(json.loads(mutations),rejected,strict=True):
            old,new,label = spec["find"].encode(),spec["replace"].encode(),spec["label"]
            assert source.count(old)==1 and run["label"]==label and run["exit_code"]!=0
            assert archive.read(f"compiler/child/{label}.lean")==source.replace(old,new)
            assert spec["diagnostic"].encode() in archive.read(f"compiler/child/{label}.log")
        assert b"List.prod" in archive.read("development/missing-import.log")
        registers.extend(("compiler","compiler/child"))
        native = record(archive,"native/receipt.json")
        assert native["kernel_sha256"]==KERNEL
        assert all(c["start_ns"]<=c["exit_observed_ns"]<=c["readback_ns"] for c in native["observations"])
        exterior["verify_native"](archive,source)
        controls(archive)
        chart = figure(plot_host)
        if runtime:
            exterior["deep_replay"](archive,registers,runtime,method)
    return dict(declarations=count,rejected_mutations=len(rejected),native_cases=len(native["observations"]),
                registers=len(registers),deep_replayed=len(registers) if runtime else 0,source_sha256=sha(source),
                figure_sha256=chart,figure_rerendered=bool(plot_host),control_programs=list(PROGRAMS))


if __name__=="__main__":
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--runtime",type=Path)
    cli.add_argument("--method",type=Path)
    cli.add_argument("--plot-host",type=Path)
    args=cli.parse_args()
    if bool(args.runtime)!=bool(args.method):
        cli.error("Deep replay needs the hosted runtime and its method packet.")
    print(json.dumps(verify(args.runtime,args.method,args.plot_host),indent=2))

"""Replay the three native PCP workers and verify their assembled Lean file."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from reproduce import checked, digest, guest, work

TASKS = ["lateral-parity", "strip-channel", "transfer-defect"]
KERNEL = "d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f"
MEASUREMENT = "0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3"
PCP = "92623fa6759bbb4e4f27ce5aa381de213a55ae0c"
MATHLIB = "c44e0c8ee63ca166450922a373c7409c5d26b00b"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("pcp-os", "kernel", "qemu", "desk", "delegate", "lake", "mathlib", "out"):
        parser.add_argument("--" + name, required=True, type=Path)
    parser.add_argument("--firmware", type=Path)
    args = parser.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    config = {k: str(getattr(args, k).absolute()) for k in ("qemu", "kernel", "desk", "delegate")}
    config["firmware"] = str(args.firmware.absolute()) if args.firmware else None
    pcp = args.pcp_os.resolve(strict=True)
    mathlib = args.mathlib.resolve(strict=True)
    lake = args.lake.absolute()
    for repo, head in ((pcp, PCP), (mathlib, MATHLIB)):
        if checked(["git", "-C", repo, "rev-parse", "HEAD"]).strip() != head:
            raise RuntimeError(f"revision mismatch at {repo}")
    measure = pcp / "PCP_OS_Rust/crates/pcpos-kernel/tools/measure.py"
    config["measurement"] = checked([sys.executable, measure, config["kernel"]]).strip()
    config["kernel_sha256"] = digest(Path(config["kernel"]).read_bytes())
    if (config["kernel_sha256"], config["measurement"]) != (KERNEL, MEASUREMENT):
        raise RuntimeError("kernel digest or load measurement differs from the recorded run")
    (out / "run.json").write_text(json.dumps(config, indent=2) + "\n")
    linker = pcp / "examples/resident-workers/fixture/link.ld"
    checked(["gcc", "-std=c11", "-Os", "-Wall", "-Wextra", "-Werror", "-ffreestanding",
             "-fno-stack-protector", "-fno-pie", "-mno-red-zone", "-mcmodel=large", "-nostdlib",
             "-static", "-Wl,--build-id=none,-T," + str(linker), HERE / "worker.c",
             "-o", out / "worker.elf"])
    wrong = guest(out, config, [1, 2, 3], "wrong-face-count", 5)
    if "LEAN-BEGIN" in wrong or re.search(r"^NEXT ", wrong, re.M):
        raise RuntimeError("the incorrect face count produced a certificate")
    db = out / "desk.redb"
    checked([config["desk"], "init", db, "2", "3", "3"])
    checked([config["delegate"], db, TASKS[0], TASKS[0], "--", sys.executable, __file__,
             "worker", str(out), "0", "0", "0"])
    desk = checked([config["desk"], "status", db])
    (out / "desk.json").write_text(desk)
    nodes = json.loads(desk)["nodes"]
    if [(n["id"], n["parent"], n["state"], n["label"]) for n in nodes] != [
            (i+1, i or None, "Finished", name) for i, name in enumerate(TASKS)]:
        raise RuntimeError("unexpected desk closure")
    root = out / TASKS[0]
    proof = (root / "subtree.lean").read_bytes()
    if digest(proof) != (root / "subtree.sha256").read_text().strip():
        raise RuntimeError("root read-back mismatch")
    released = HERE / "LocalResponse.lean"
    if released.exists() and released.read_bytes() != proof:
        raise RuntimeError("source differs from the release")
    env = dict(os.environ, PATH=str(lake.parent) + os.pathsep + os.environ["PATH"])
    version = checked([lake, "env", "lean", "--version"], cwd=mathlib, env=env)
    if "version 4.19.0" not in version:
        raise RuntimeError(version)

    def verify(name, source):
        path = out / (name + ".lean")
        path.write_bytes(source)
        result = subprocess.run([lake, "env", "lean", path], cwd=mathlib, env=env,
                                text=True, capture_output=True)
        log = result.stdout + result.stderr
        (out / (name + ".log")).write_text(log)
        return result.returncode, log

    status, log = verify("LocalResponse", proof)
    reports = re.findall(r"'[\w.]+'.*?(?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", log, re.S)
    allowed = {"propext", "Classical.choice", "Quot.sound"}
    if (status or len(reports) != 17 or "warning:" in log or "sorryAx" in log or
            any(a.strip() not in allowed for report in reports if report for a in report.split(","))):
        raise RuntimeError("proof or axiom audit failed, see LocalResponse.log")
    for old, new, name, diagnostic in (
            (b"false = 353", b"false = 354", "WrongParity", "is false"),
            (b"(32/91", b"(33/91", "WrongChannel", "unsolved goals"),
            (b"Faces = [0, 511]", b"Faces = [0, 510]", "WrongTorus", "is false")):
        if proof.count(old) != 1:
            raise RuntimeError("mutation target missing or duplicated")
        code, message = verify(name, proof.replace(old, new))
        if code == 0 or diagnostic not in message:
            raise RuntimeError(f"unexpected {name} result")
    print(f"17 theorems accepted, three nodes closed, four adverse controls rejected. {digest(proof)}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        main()

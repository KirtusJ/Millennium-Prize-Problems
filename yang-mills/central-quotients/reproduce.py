"""Generate CentralQuotient.lean in three PCP OS guests and check it with hosted Lean."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
TASKS = ["find-witness", "verify-lifts", "count-fluxes"]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked(args, cwd=None, env=None):
    result = subprocess.run(args, cwd=cwd, env=env, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(f"{args[0]} exited {result.returncode}: {result.stdout}{result.stderr}")
    return result.stdout


def guest(out, config, task, label, expected_exit):
    stage = out / label
    stage.mkdir()
    shutil.copyfile(out / "worker.elf", stage / "worker.elf")
    (stage / "task.bin").write_bytes(bytes(task))
    command = [config["qemu"], "-machine", "microvm,isa-serial=on,pic=on,pit=on,rtc=on",
               "-accel", "tcg,tb-size=4", "-icount", "shift=3,align=off,sleep=off",
               "-cpu", "max", "-m", "32M", "-nodefaults", "-nic", "none",
               "-display", "none", "-monitor", "none", "-serial", "stdio", "-no-reboot",
               "-kernel", config["kernel"], "-initrd", "worker.elf,task.bin",
               "-append", "auto=worker.elf then=off image=" + config["measurement"],
               "-device", "isa-debug-exit,iobase=0xf4,iosize=0x04"]
    if config["firmware"]:
        command.extend(["-L", config["firmware"]])
    result = subprocess.run(command, cwd=stage, capture_output=True, timeout=90)
    (stage / "serial.log").write_bytes(result.stdout)
    (stage / "qemu.stderr").write_bytes(result.stderr)
    serial = result.stdout.decode().replace("\r\n", "\n")
    elf_hash = digest((stage / "worker.elf").read_bytes())
    starts = re.findall(r"^starting worker\.elf \(\d+ bytes, SHA-256 ([0-9a-f]{64})\)", serial, re.M)
    exits = re.findall(r"^worker\.elf ended (\w+): exit (\d+)\b", serial, re.M)
    outcome = "DONE" if expected_exit == 0 else "FAILED"
    if (result.returncode != 33 or starts != [elf_hash] or exits != [(outcome, str(expected_exit))]
            or config["measurement"] + " (measured; equal to the value the loader named)" not in serial
            or "ALL SELF-TESTS PASS" not in serial):
        raise RuntimeError(f"{label}: QEMU {result.returncode}, starts {starts}, exits {exits}; see {stage}")
    return serial


def work(out, task):
    config = json.loads((out / "run.json").read_text())
    depth = task[0]
    stage = out / TASKS[depth]
    serial = guest(out, config, task, TASKS[depth], 0)
    fragments = re.findall(r"^LEAN-BEGIN\n(.*?)^LEAN-END$", serial, re.S | re.M)
    requests = re.findall(r"^NEXT (\d+) (\d+) (\d+)$", serial, re.M)
    if len(fragments) != 1 or len(requests) != int(depth < 2):
        raise RuntimeError(f"ill-formed guest output at depth {depth}")
    proof = fragments[0].encode()
    if requests:
        successor = tuple(map(int, requests[0]))
        if successor[0] != depth + 1 or not all(1 <= v <= 4 for v in successor[1:]):
            raise ValueError(f"invalid child request {requests[0]}")
        if depth and tuple(task[1:]) != successor[1:]:
            raise ValueError("witness changed in transit")
        checked([config["delegate"], "-", TASKS[depth+1], TASKS[depth+1], "--",
                 sys.executable, __file__, "worker", str(out), *map(str, successor)])
        child = out / TASKS[depth+1]
        suffix = (child / "subtree.lean").read_bytes()
        if digest(suffix) != (child / "subtree.sha256").read_text().strip():
            raise ValueError("child result digest mismatch on post-exit read-back")
        proof += suffix
    (stage / "subtree.lean").write_bytes(proof)
    (stage / "subtree.sha256").write_text(digest(proof) + "\n")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ("pcp-os", "kernel", "delegate", "desk", "qemu", "lean", "out"):
        p.add_argument("--" + key, required=True, type=Path)
    p.add_argument("--firmware", type=Path)
    args = p.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    kernel = args.kernel.resolve(strict=True)
    pcp = args.pcp_os.resolve(strict=True)
    measurement = checked([sys.executable, pcp / "PCP_OS_Rust/crates/pcpos-kernel/tools/measure.py",
                           kernel]).strip()
    config = {k: str(getattr(args, k).resolve(strict=True)) for k in ("qemu","desk","delegate","lean")}
    config.update(kernel=str(kernel), measurement=measurement,
                  kernel_sha256=digest(kernel.read_bytes()),
                  firmware=str(args.firmware.resolve(strict=True)) if args.firmware else None)
    (out / "run.json").write_text(json.dumps(config, indent=2) + "\n")
    checked(["gcc", "-std=c11", "-Os", "-Wall", "-Wextra", "-Werror", "-ffreestanding",
             "-fno-stack-protector", "-fno-pie", "-mno-red-zone", "-mcmodel=large",
             "-nostdlib", "-static", "-Wl,--build-id=none,-T," + str(pcp / "examples/resident-workers/fixture/link.ld"),
             HERE / "worker.c", "-o", out / "worker.elf"])
    control = guest(out, config, [1,2,2], "equal-axis-control", 5)
    if "LEAN-BEGIN" in control or re.search(r"^NEXT ", control, re.M):
        raise RuntimeError("invalid witness produced a proof or request")
    db = out / "desk.redb"
    checked([config["desk"], "init", db, "2", "3", "3"])
    checked([config["delegate"], db, TASKS[0], TASKS[0], "--", sys.executable,
             __file__, "worker", str(out), "0", "0", "0"])
    desk = checked([config["desk"], "status", db])
    (out / "desk.json").write_text(desk)
    nodes = json.loads(desk)["nodes"]
    if len(nodes) != len(TASKS):
        raise RuntimeError(f"expected three node records, found {len(nodes)}")
    for i, node in enumerate(nodes):
        if (node["id"], node["parent"], node["state"], node["label"]) != (i+1, i or None, "Finished", TASKS[i]):
            raise RuntimeError(f"unexpected desk entry {node}")
    root = out / TASKS[0]
    proof = (root / "subtree.lean").read_bytes()
    if digest(proof) != (root / "subtree.sha256").read_text().strip():
        raise RuntimeError("root read-back mismatch")
    released = HERE / "CentralQuotient.lean"
    if released.exists() and proof != released.read_bytes():
        raise RuntimeError("generated source differs from the published file")
    (out / "CentralQuotient.lean").write_bytes(proof)
    shutil.copyfile(HERE / "Model.lean", out / "Model.lean")
    env = dict(os.environ, LEAN_PATH=str(out))
    checked([config["lean"], "-o", "Model.olean", "Model.lean"], cwd=out, env=env)
    run = subprocess.run([config["lean"], "-o", "CentralQuotient.olean", "CentralQuotient.lean"],
                         cwd=out, text=True, capture_output=True, env=env)
    (out / "lean.log").write_text(run.stdout + run.stderr)
    if run.returncode or "sorryAx" in run.stdout or "warning:" in run.stdout:
        raise RuntimeError("Lean check failed; see lean.log")
    reports = [s for s in run.stdout.splitlines() if "axioms" in s]
    if (len(reports) != 9 or
            any(not s.endswith(("does not depend on any axioms", "depends on axioms: [propext]"))
                for s in reports)):
        raise RuntimeError("unexpected axiom reports; see lean.log")
    mutation = proof.replace(b"fluxes.count 0 = 46", b"fluxes.count 0 = 47")
    if mutation == proof:
        raise RuntimeError("negative-control target missing")
    (out / "Adverse.lean").write_bytes(mutation)
    adverse = subprocess.run([config["lean"], "Adverse.lean"], cwd=out, text=True,
                             capture_output=True, env=env)
    (out / "adverse.log").write_text(adverse.stdout + adverse.stderr)
    if (adverse.returncode == 0 or "List.count 0 fluxes = 47" not in adverse.stdout
            or "is false" not in adverse.stdout):
        raise RuntimeError("wrong census survived the control")
    print(f"Three finished nodes. Lean accepted {digest(proof)}. Both adverse controls rejected.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "worker":
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])))
    else:
        main()

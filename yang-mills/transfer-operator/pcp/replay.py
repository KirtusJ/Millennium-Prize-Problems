"""Regenerate the marked Lean proof bodies in PCP OS guests and check the assembled file."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CHECKED = HERE.parent / "TwoSector.lean"
KERNEL_SHA = "d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f"
MEASUREMENT = "0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3"
PCP = "92623fa6759bbb4e4f27ce5aa381de213a55ae0c"
MATHLIB = "c44e0c8ee63ca166450922a373c7409c5d26b00b"
THEOREMS = {"pivot_identity", "comparison_iff", "block_defect", "energy_floor", "equal_sector_witness",
            "soft_energy", "no_uniform_floor", "soft_transfer", "one_link_floor"}
AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def invoke(args, **opts):
    return subprocess.run(args, check=True, **opts)


def strip_proofs():
    basis = CHECKED.read_bytes()
    for number, name in enumerate(("comparison", "collapse"), start=1):
        first = f"  -- PCP begin {name}\n".encode()
        last = f"  -- PCP end {name}\n".encode()
        if basis.count(first) != 1 or basis.count(last) != 1:
            raise ValueError(f"expected one proof region for {name}")
        before, rest = basis.split(first)
        _, after = rest.split(last)
        basis = before + first + bytes([number]) + last + after
    return basis


def guest(cfg, name, order, inputs):
    out = Path(cfg["out"])
    folder = out / name
    folder.mkdir()
    shutil.copyfile(out / "worker.elf", folder / "worker.elf")
    for filename, raw in {"order": order, **inputs}.items():
        (folder / filename).write_bytes(raw)
    modules = ",".join(["worker.elf", "order", *inputs])
    args = [cfg["qemu"]]
    if cfg["firmware"]:
        args += ["-L", cfg["firmware"]]
    args += ["-machine", "microvm,isa-serial=on,pic=on,pit=on,rtc=on", "-accel", "tcg,tb-size=4",
             "-icount", "shift=3,align=off,sleep=off", "-cpu", "max", "-m", "32M",
             "-nodefaults", "-nic", "none", "-display", "none", "-monitor", "none", "-serial", "stdio",
             "-no-reboot", "-kernel", cfg["kernel"], "-initrd", modules, "-append",
             f"auto=worker.elf then=off image={MEASUREMENT}", "-device", "isa-debug-exit,iobase=0xf4,iosize=0x04"]
    proc = subprocess.run(args, cwd=folder, capture_output=True, timeout=120)
    (folder / "serial.log").write_bytes(proc.stdout)
    (folder / "emulator.log").write_bytes(proc.stderr)
    log = proc.stdout.decode().splitlines()
    worker_hash = digest((folder / "worker.elf").read_bytes())
    starts = [s for s in log if s.startswith("starting worker.elf (")]
    exits = [s for s in log if s.startswith("worker.elf ended ")]
    if (proc.returncode != 33 or len(starts) != 1 or worker_hash not in starts[0]
            or len(exits) != 1 or not re.search(r": exit 0\b", exits[0])
            or not any(MEASUREMENT + " (measured; equal to the value the loader named)" in s for s in log)):
        raise RuntimeError(f"{name} boot failed; inspect {folder}/serial.log and emulator.log")
    frames = [s[8:] for s in log[log.index(starts[0])+1:log.index(exits[0])] if s.startswith("LEANHEX ")]
    if not frames or any(not re.fullmatch(r"(?:[0-9a-f]{2}){1,48}", f) for f in frames):
        raise RuntimeError(f"invalid serial proof frames in {name}")
    raw = bytes.fromhex("".join(frames))
    (out / (name + ".out")).write_bytes(raw)
    return raw


def child(cfg, name):
    invoke([cfg["delegate"], "-", name, name, "--", sys.executable, str(Path(__file__).resolve()),
            "--node", name, cfg["out"]])


def check_lean(cfg, source, error=None):
    out = Path(cfg["out"])
    result = subprocess.run([cfg["lake"], "env", "lean", str(source)], cwd=cfg["mathlib"],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=180)
    (out / (source.stem + ".log")).write_text(result.stdout)
    if error is not None:
        if result.returncode == 0 or error not in result.stdout:
            raise RuntimeError(f"adverse case {source.name} was not rejected")
        return
    reports = re.findall(r"'Millennium\.YangMills\.Transfer\.(\w+)' depends on axioms: \[([^\]]*)\]", result.stdout)
    if (result.returncode or len(reports) != len(THEOREMS) or {n for n, _ in reports} != THEOREMS
            or any(set(raw.split(", ")) != AXIOMS for _, raw in reports) or "warning:" in result.stdout):
        raise RuntimeError(f"Lean or axiom read-back failed; inspect {source.stem}.log")


def task(node, out):
    cfg = json.loads((out / "config.json").read_text())
    if node in ("comparison", "collapse"):
        guest(cfg, node, b"C" if node == "comparison" else b"W", {})
    elif node == "generate":
        for part in ("comparison", "collapse"):
            child(cfg, part)
        parts = {name: (out / (name + ".out")).read_bytes() for name in ("comparison", "collapse")}
        generated = guest(cfg, "assembly", b"A", {"basis": strip_proofs(), **parts})
        (out / "TwoSector.lean").write_bytes(generated)
    elif node == "root":
        child(cfg, "generate")
        regenerated = out / "TwoSector.lean"
        if regenerated.read_bytes() != CHECKED.read_bytes():
            raise RuntimeError("regenerated proof differs from the checked-in source")
        check_lean(cfg, regenerated)
        source = regenerated.read_text()
        for name, before, after, error in [
            ("WrongPivot", "(h c (u-m))", "(h (-c) (u-m))", "error: application type mismatch"),
            ("WeakWitness", "m/3", "m/2", "error: linarith failed to find a contradiction"),
        ]:
            if before not in source:
                raise ValueError(f"mutation site missing for {name}")
            mutant = out / (name + ".lean")
            mutant.write_text(source.replace(before, after))
            check_lean(cfg, mutant, error=error)
    else:
        raise ValueError(node)


def main():
    if len(sys.argv) == 4 and sys.argv[1] == "--node":
        return task(sys.argv[2], Path(sys.argv[3]))
    p = argparse.ArgumentParser(description=__doc__)
    for k in ("kernel", "pcp", "mathlib", "out"):
        p.add_argument("--" + k, required=True, type=Path)
    p.add_argument("--firmware", type=Path)
    p.add_argument("--qemu", default="qemu-system-x86_64")
    args = p.parse_args()
    if digest(args.kernel.read_bytes()) != KERNEL_SHA:
        p.error("kernel differs from the pinned public ISO")
    for checkout, revision in [(args.mathlib, MATHLIB), (args.pcp, PCP)]:
        if subprocess.check_output(["git", "-C", checkout, "rev-parse", "HEAD"], text=True).strip() != revision:
            p.error(f"{checkout} differs from the reviewed revision")
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    cfg = {"out": str(out), "kernel": str(args.kernel.resolve()), "mathlib": str(args.mathlib.resolve()),
           "firmware": str(args.firmware.resolve()) if args.firmware else None}
    for key, tool in [("qemu", args.qemu), ("delegate", "pcp-delegate"), ("desk", "parrots-all-the-way-down"),
                      ("lake", "lake")]:
        path = shutil.which(tool)
        if not path:
            p.error(f"missing {tool}")
        cfg[key] = str(Path(path).resolve())
    (out / "config.json").write_text(json.dumps(cfg))
    invoke(["cc", "-std=c11", "-O2", "-Wall", "-Wextra", "-Werror", "-ffreestanding", "-fno-stack-protector",
            "-fno-pie", "-mno-red-zone", "-mcmodel=large", "-c", HERE / "worker.c", "-o", out / "worker.o"])
    link = args.pcp / "PCP_OS_Rust/crates/pcpos-kernel/programs/pcp-fib/link.ld"
    invoke(["ld", "--build-id=none", "-z", "noexecstack", "-T", link, out / "worker.o", "-o", out / "worker.elf"])
    desk = out / "team.redb"
    invoke([cfg["desk"], "init", desk, "2", "3", "4"])
    invoke([cfg["delegate"], desk, "root", "root", "--", sys.executable, str(Path(__file__).resolve()),
            "--node", "root", out])
    status = subprocess.check_output([cfg["desk"], "status", desk], text=True)
    state = json.loads(status)
    topology = [(n["id"], n["parent"], n["label"], n["state"]) for n in state["nodes"]]
    if topology != [(1, None, "root", "Finished"), (2, 1, "generate", "Finished"),
                    (3, 2, "comparison", "Finished"), (4, 2, "collapse", "Finished")]:
        raise RuntimeError("post-exit PCP desk read-back failed")
    (out / "desk.json").write_text(status)
    print(status.strip())
    print("Lean source SHA-256", digest((out / "TwoSector.lean").read_bytes()))
    print("Three measured PCP OS guests, nine Lean declarations, two rejected mutations.")


if __name__ == "__main__":
    main()

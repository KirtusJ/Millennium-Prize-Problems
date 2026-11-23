"""Rebuild the electric-staple spectral certificates in a recursive PCP desk and two native boots."""
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

from controls import run as check_controls

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "transfer-operator" / "pcp"))
from replay import AXIOMS, KERNEL_SHA, MATHLIB, PCP, digest, guest

SOURCE = HERE / "StapleSpectrum.lean"
ASSEMBLER = "1cb649a9954be008a7f74ada3fb1494f1949d7947b85bf221875c655ea59afcd"
THEOREMS = {
    'polynomialReadings', 'reconstruct', 'slabOffset', 'checkerboard', 'phaseNorm', 'endpointAverage',
    'upperDispersion', 'transverseCorner', 'lowerDispersion', 'cornerCoefficient', 'irCoefficient', 'edgeRatio', 'zeroMomentumWeight', 'zeroMomentumIR', 'continuumShell', 'shellToPoint',
}


def run(args, **opts):
    return subprocess.run(args, check=True, **opts)


def child(cfg, node):
    run([cfg["delegate"], "-", node, node, "--", sys.executable, str(HERE / "replay.py"),
         "--node", node, cfg["out"]])


def native(cfg, out):
    folder = out / "native"
    folder.mkdir()
    run(["cc", "-std=c11", "-O2", "-Wall", "-Wextra", "-Werror", "-ffreestanding",
         "-fno-stack-protector", "-fno-pie", "-mno-red-zone", "-mcmodel=large", "-c",
         HERE / "certificate.c", "-o", folder / "certificate.o"])
    script = Path(cfg["pcp"]) / "PCP_OS_Rust/crates/pcpos-kernel/programs/pcp-fib/link.ld"
    run(["ld", "--build-id=none", "-z", "noexecstack", "-T", script, folder / "certificate.o",
         "-o", folder / "worker.elf"])
    raw = guest({**cfg, "out": str(folder)}, "search", (out / "counts.bin").read_bytes(), {})
    (out / "certificate").write_bytes(raw)


def lean(cfg, path, expected_error=None, region=None):
    result = subprocess.run([cfg["lake"], "env", "lean", str(path)], cwd=cfg["mathlib"],
                            capture_output=True, text=True, timeout=180)
    log = result.stdout + result.stderr
    path.with_suffix(".log").write_text(log)
    if expected_error is not None:
        errors = re.findall(rf"{re.escape(path.name)}:(\d+):\d+: error: ([^\n]*)", log)
        if (not result.returncode or not errors
                or any(not region[0] <= int(line) <= region[1]
                       or expected_error not in "error: " + message for line, message in errors)):
            raise RuntimeError(f"missing intended rejection in {path.name}")
        return
    reports = re.findall(r"'Millennium\.YangMills\.StapleSpectrum\.(\w+)' depends on axioms: \[([^\]]+)\]", log)
    if (result.returncode or "warning:" in log or len(reports) != len(THEOREMS)
            or {name for name, _ in reports} != THEOREMS
            or any({x.strip() for x in axioms.split(",")} != AXIOMS
                   for name, axioms in reports)):
        raise RuntimeError(f"unexpected Lean verification in {path.name}")


def task(node, out):
    cfg = json.loads((out / "config.json").read_text())
    if node == "links":
        check_controls(out)
        source = HERE.parents[1] / "observable-normalization/energy-density/staple-response/StapleResponse.lean"
        if digest(source.read_bytes()) != "7e8b05b28b7572751bde5fe4643dbcd0366bfb7529a817a249ca10eff889b87b":
            raise ValueError("unexpected A4 input module")
        peer = run([cfg["lake"], "env", "lean", source], cwd=cfg["mathlib"], capture_output=True, text=True)
        log = peer.stdout + peer.stderr
        if len(re.findall(r"^'YangMills\.StapleResponse\.", log, re.M)) != 11 or "sorryAx" in log:
            raise ValueError("A4 axiom read-back failed")
        (out / "A4.log").write_text(log)
    elif node == "certificate":
        native(cfg, out)
    elif node == "generation":
        child(cfg, "links")
        child(cfg, "certificate")
        basis = SOURCE.read_bytes()
        for tag, name in enumerate(("geometry", "certificate"), start=1):
            start = f"-- PCP begin {name}\n".encode()
            stop = f"-- PCP end {name}\n".encode()
            before, middle = basis.split(start)
            _, after = middle.split(stop)
            basis = before + start + bytes([tag]) + stop + after
        regenerated = guest(cfg, "assembly", b"A", {"basis": basis, "comparison": (out / "geometry").read_bytes(),
                                                     "collapse": (out / "certificate").read_bytes()})
        (out / SOURCE.name).write_bytes(regenerated)
    elif node == "root":
        child(cfg, "generation")
        checked = out / SOURCE.name
        if checked.read_bytes() != SOURCE.read_bytes():
            raise ValueError("native output differs from tracked source")
        lean(cfg, checked)
        for name, old, new, error in [
                ("Offset", "x^j*x = x^(j+1)", "x^j*x = x^j", "error: type mismatch"),
                ("Corner", "= 3*r/(64*p^3)", "= 3*r/(32*p^3)", "error: unsolved goals"),
                ("Checker", "a j * (1 + (-1:ℂ))", "a j * (1 + (1:ℂ))", "error: simp made no progress"),
                ("Polarizations", "+8*q^4/15)/8", "+4*q^4/15)/8", "error: unsolved goals"),
                ("Upper", "u+v ≤ 2*w := by", "u+v ≤ w := by", "error: linarith failed"),
        ]:
            src = checked.read_text()
            if old not in src:
                raise ValueError("missing mutation target")
            path = out / (name + ".lean")
            before, rest = src.split(old, 1)
            body = rest.split("\n\n", 1)[0]
            path.write_text(before + new + body + "\nend\nend Millennium.YangMills.StapleSpectrum\n")
            first = src[:src.index(old)].count("\n") + 1
            remaining = src.split(old, 1)[1].split("\n\n", 1)[0]
            last = first + remaining.count("\n")
            lean(cfg, path, expected_error=error, region=(first, last))
    else:
        raise ValueError(node)


def main():
    if len(sys.argv) == 4 and sys.argv[1] == "--node":
        return task(sys.argv[2], Path(sys.argv[3]))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base", type=Path, help="output of ../pcp/replay.py")
    parser.add_argument("pcp", type=Path, help="pinned PCP OS source checkout")
    parser.add_argument("out", type=Path, help="new run directory")
    args = parser.parse_args()
    cfg = json.loads((args.base / "config.json").read_text())
    for repo, commit in [(args.pcp, PCP), (cfg["mathlib"], MATHLIB)]:
        if run(["git", "-C", repo, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip() != commit:
            parser.error(f"unexpected revision in {repo}")
    if digest(Path(cfg["kernel"]).read_bytes()) != KERNEL_SHA or digest((args.base / "worker.elf").read_bytes()) != ASSEMBLER:
        parser.error("kernel or assembly worker differs from the pinned build")
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    cfg.update(out=str(out), pcp=str(args.pcp.resolve()))
    (out / "config.json").write_text(json.dumps(cfg))
    shutil.copyfile(args.base / "worker.elf", out / "worker.elf")
    desk = out / "team.redb"
    run([cfg["desk"], "init", desk, "2", "3", "4"])
    run([cfg["delegate"], desk, "root", "root", "--", sys.executable, str(HERE / "replay.py"), "--node", "root", out])
    state = run([cfg["desk"], "status", desk], capture_output=True, text=True).stdout
    (out / "desk.json").write_text(state)
    tree = [(n["id"], n["parent"], n["label"], n["state"]) for n in json.loads(state)["nodes"]]
    if tree != [(1, None, "root", "Finished"), (2, 1, "generation", "Finished"),
                (3, 2, "links", "Finished"), (4, 2, "certificate", "Finished")]:
        raise RuntimeError("incomplete post-exit read-back")
    print(tree)
    print((out / "checks.json").read_text().strip())
    print("Lean SHA-256", digest((out / SOURCE.name).read_bytes()))


if __name__ == "__main__":
    main()

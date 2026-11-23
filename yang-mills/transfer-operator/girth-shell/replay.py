"""Rebuild the Wilson girth-shell certificates in a recursive PCP desk and two native boots."""
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

SOURCE = HERE / "GirthShell.lean"
ASSEMBLER = "1cb649a9954be008a7f74ada3fb1494f1949d7947b85bf221875c655ea59afcd"
THEOREMS = {
    "centeredInner", "vacuumLeak", "gramPowers", "longitudinal", "transverse", "incidenceSymbol",
    "bandEdges", "corner", "coreCompletion", "cubeHessian", "intertwinePowers", "stepError",
    "jointSymbol", "schurRows", "cornerEnergy", "cornerTrial", "cubeLimits",
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
    reports = re.findall(r"'Millennium\.YangMills\.GirthShell\.(\w+)' depends on axioms: \[([^\]]+)\]", log)
    if (result.returncode or "warning:" in log or len(reports) != len(THEOREMS)
            or {name for name, _ in reports} != THEOREMS
            or any({x.strip() for x in axioms.split(",")} != ({"propext"} if name == "coreCompletion" else AXIOMS)
                   for name, axioms in reports)):
        raise RuntimeError(f"unexpected Lean verification in {path.name}")


def task(node, out):
    cfg = json.loads((out / "config.json").read_text())
    if node == "links":
        check_controls(out)
        source = HERE.parent / "connected-rectangles/ConnectedRectangles.lean"
        if digest(source.read_bytes()) != "bf01f35c29f8c0ba9ec3f3c7428a30d4daf3784bca986c31e766d4cd27d5ddae":
            raise ValueError("unexpected connected-rectangle source")
        peer = run([cfg["lake"], "env", "lean", source], cwd=cfg["mathlib"], capture_output=True, text=True)
        log = peer.stdout + peer.stderr
        if len(re.findall(r"^'Millennium\.YangMills\.ConnectedRectangles\.", log, re.M)) != 26 or "sorryAx" in log:
            raise ValueError("connected-rectangle read-back failed")
        (out / "Rectangles.log").write_text(log)
        band = HERE.parents[1] / "observable-normalization/replica-gap"
        formal = band / "ReplicaGap.lean"
        control = band / "check_band.py"
        if digest(formal.read_bytes()) != "8b13f1924fcac8721b6c8c4ba0e3692f40f4dea6ce342435222606232954b462" or digest(control.read_bytes()) != "7a034bb640ede45f013959f3f4765a45adf4533120ea69adfb6911362cdaf387":
            raise ValueError("unexpected A4 band input")
        result = run([cfg["lake"], "env", "lean", formal], cwd=cfg["mathlib"], capture_output=True, text=True)
        band_log = result.stdout + result.stderr
        if len(re.findall(r"^'YangMills\.ReplicaGap\.\w+' depends on axioms:", band_log, re.M)) != 13 or "sorryAx" in band_log:
            raise ValueError("A4 band formal read-back failed")
        (out / "ReplicaGap.log").write_text(band_log)
        result = run([sys.executable, control], capture_output=True, text=True)
        (out / "A4-band.log").write_text(result.stdout)
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
                ("WrongCenter", "⟪x,y⟫ - ⟪u,x⟫", "⟪x,y⟫ + ⟪u,x⟫", "error: unsolved goals"),
                ("WrongCube", "= 1/256", "= 1/128", "error: unsolved goals"),
                ("WrongBand", "4+2*(a+b+c) ≤ 10", "4+2*(a+b+c) ≤ 9", "error: linarith failed"),
                ("WrongCorner", "108/25 ≤", "109/25 ≤", "error: linarith failed"),
                ("WrongBoundary", "5*x^2 ≤", "6*x^2 ≤", "error: linarith failed"),
                ("WrongMix", "z^2,2*x*y,2*x*z", "z^2,3*x*y,2*x*z", "error: unsolved goals"),
                ("WrongCover", "(faceMask a = 3 ∨", "(faceMask a = 2 ∨", "error: tactic 'decide' proved that the proposition"),
        ]:
            src = checked.read_text()
            if old not in src:
                raise ValueError("missing mutation target")
            path = out / (name + ".lean")
            before, rest = src.split(old, 1)
            body = rest.split("\n\n", 1)[0]
            path.write_text(before + new + body + "\nend\nend Millennium.YangMills.GirthShell\n")
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

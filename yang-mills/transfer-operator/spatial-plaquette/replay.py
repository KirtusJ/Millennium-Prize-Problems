"""Search the central link assignment, boot the PCP assembly guest, and check every face in Lean."""
import argparse
import itertools
import json
from pathlib import Path
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "pcp"))
from replay import digest, guest

PAIRS = ((0, 1), (0, 2), (1, 2))
SOURCE = HERE / "WilsonSlice.lean"


def search(out):
    # A link sign is the parity of a linear form in the site coordinates.
    # Flipping coordinate i of link j changes its exponent by bit i of mask j.
    for masks in itertools.product(range(8), repeat=3):
        if all(((masks[j] >> i) ^ (masks[i] >> j)) & 1 for i, j in PAIRS):
            break
    else:
        raise RuntimeError("no linear assignment")
    rows = []
    for axis, mask in enumerate(masks):
        terms = [f"parity (x {j})" for j in range(3) if mask & (1 << j)]
        rows.append(f"  | {axis} => " + (" + ".join(terms) or "0"))
    (out / "links").write_text("\n".join(rows) + "\n")
    (out / "masks.json").write_text(json.dumps(masks))


def torus_control(out):
    masks = json.loads((out / "masks.json").read_text())
    def exponent(mask, site):
        return sum(x for j, x in enumerate(site) if mask & (1 << j)) % 2

    results = []
    for length in (2, 3, 4, 5, 6):
        ones = total = 0
        for site in itertools.product(range(length), repeat=3):
            for i, j in PAIRS:
                xi, xj = list(site), list(site)
                xi[i] = (xi[i] + 1) % length
                xj[j] = (xj[j] + 1) % length
                parity = (exponent(masks[i], site) + exponent(masks[j], xi)
                          - exponent(masks[i], xj) - exponent(masks[j], site)) % 2
                ones += parity
                total += 1
        if (ones == total) != (length % 2 == 0):
            raise RuntimeError(f"unexpected wraparound control at L={length}")
        results.append([length, ones, total])
    (out / "counts.json").write_text(json.dumps(results))


def child(cfg, node, out):
    subprocess.run([cfg["delegate"], "-", node, node, "--", sys.executable,
                    str(Path(__file__).resolve()), "--node", node, str(out)], check=True)


def task(node, out):
    cfg = json.loads((out / "config.json").read_text())
    if node == "search":
        search(out)
    elif node == "control":
        torus_control(out)
        (out / "proof").write_text("  fin_cases i <;> fin_cases j <;>\n"
                                  "    norm_num [face, link, step, map_add, ZMod.cast_one h] at *\n")
    elif node == "generation":
        child(cfg, "search", out)
        child(cfg, "control", out)
        basis = SOURCE.read_bytes()
        for n, label in enumerate(("links", "proof"), start=1):
            start = f"  -- PCP begin {label}\n".encode()
            stop = f"  -- PCP end {label}\n".encode()
            before, inside = basis.split(start)
            _, after = inside.split(stop)
            basis = before + start + bytes([n]) + stop + after
        inputs = {"basis": basis, "comparison": (out / "links").read_bytes(),
                  "collapse": (out / "proof").read_bytes()}
        raw = guest(cfg, "assembly", b"A", inputs)
        (out / "WilsonSlice.lean").write_bytes(raw)
    elif node == "root":
        child(cfg, "generation", out)
        raw = (out / "WilsonSlice.lean").read_bytes()
        if raw != SOURCE.read_bytes():
            raise RuntimeError("source differs from the guest output")
        needle = b"  | 2 => parity (x 0) + parity (x 1)"
        if raw.count(needle) != 1:
            raise RuntimeError("control site missing")
        for filename, content in [("WilsonSlice", raw), ("MissingY", raw.replace(needle, b"  | 2 => parity (x 0)"))]:
            file = out / (filename + ".lean")
            file.write_bytes(content)
            run = subprocess.run([cfg["lake"], "env", "lean", str(file)], cwd=cfg["mathlib"],
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=180)
            (out / (filename + ".log")).write_text(run.stdout)
            if filename == "WilsonSlice":
                expected = "'Millennium.YangMills.WilsonSlice.every_face' depends on axioms: [propext, Classical.choice, Quot.sound]"
                if run.returncode or run.stdout.strip() != expected:
                    raise RuntimeError("Lean or axiom check failed")
            elif run.returncode == 0 or "unsolved goals" not in run.stdout:
                raise RuntimeError("missing-link mutation was not rejected at the face theorem")
    else:
        raise ValueError(node)


def main():
    if len(sys.argv) == 4 and sys.argv[1] == "--node":
        return task(sys.argv[2], Path(sys.argv[3]))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("transfer_run", type=Path, help="successful output directory of ../pcp/replay.py")
    parser.add_argument("out", type=Path, help="new run directory")
    args = parser.parse_args()
    cfg = json.loads((args.transfer_run / "config.json").read_text())
    out = args.out.resolve()
    out.mkdir(parents=True)
    cfg["out"] = str(out)
    (out / "config.json").write_text(json.dumps(cfg))
    shutil.copyfile(args.transfer_run / "worker.elf", out / "worker.elf")
    desk = out / "team.redb"
    subprocess.run([cfg["desk"], "init", desk, "2", "3", "4"], check=True)
    subprocess.run([cfg["delegate"], desk, "root", "root", "--", sys.executable,
                    str(Path(__file__).resolve()), "--node", "root", out], check=True)
    state = subprocess.check_output([cfg["desk"], "status", desk], text=True)
    (out / "desk.json").write_text(state)
    tree = [(n["id"], n["parent"], n["label"], n["state"]) for n in json.loads(state)["nodes"]]
    if tree != [(1, None, "root", "Finished"), (2, 1, "generation", "Finished"),
                (3, 2, "search", "Finished"), (4, 2, "control", "Finished")]:
        raise RuntimeError("incomplete PCP desk read-back")
    print(state.strip())
    print("L, negative plaquettes, total:", (out / "counts.json").read_text())
    print("Lean source SHA-256", digest((out / "WilsonSlice.lean").read_bytes()))


if __name__ == "__main__":
    main()

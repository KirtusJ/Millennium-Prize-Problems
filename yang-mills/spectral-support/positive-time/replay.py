"""Replay three measured PCP OS guests and compare their Lean output byte for byte."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.dont_write_bytecode = True
from native_guest import boot_guest, build_guest, digest, kernel_package

MARKER = b"-- BEGIN PCP OS generated signed-spectrum control\n"
DIFFERENCE_MARKER = b"-- BEGIN PCP OS generated time-difference control\n"
STAGES = ("factor", "square", "assemble")
ADJOINT_MARKER = b"-- BEGIN PCP OS generated spherical divergence\n"


def result_spec(mode):
    if mode == "loop":
        return (HERE.parent / "ordinary-loop/OrdinaryLoop.lean",
                b"-- BEGIN PCP OS generated trace contractions\n", "wick")
    if mode == "graph":
        return (HERE.parent / "graph-holonomies/GraphHolonomies.lean",
                b"-- BEGIN PCP OS generated shared-path control\n", "words")
    if mode == "scale":
        return (HERE.parent / "electric-scale/ElectricScale.lean",
                b"-- BEGIN PCP OS generated star flux\n", "flux")
    if mode == "finite":
        return (HERE.parent / "finite-readings/FiniteReadings.lean",
                b"-- BEGIN PCP OS generated electric readings\n", "moments")
    if mode == "adjoint":
        return HERE.parent / "adjoint-band/AdjointBand.lean", ADJOINT_MARKER, "divergence"
    if mode == "difference":
        return HERE / "vacuum/GapAboveVacuum.lean", DIFFERENCE_MARKER, "square"
    return HERE / "PositiveTime.lean", MARKER, "square"


def launch(stage, folder, config):
    command = [sys.executable, "-I", __file__, "--worker", stage, str(folder)]
    if config["dispatcher"]:
        register = config["register"] if stage == "factor" else "-"
        prefix = {"adjoint": "adjoint-", "finite": "readings-", "scale": "electric-", "graph": "graph-", "loop": "loop-"}.get(config["mode"], "positive-")
        command = [config["dispatcher"], "--register", register, config["actor"],
                   prefix + stage, "--", *command]
    subprocess.run(command, check=True)


def worker(stage, folder):
    config = json.loads((folder / "config.json").read_text())
    mode = config["mode"]
    filename, marker, intermediate = result_spec(mode)
    coefficient = {"positive": 2, "difference": 1, "adjoint": 3, "finite": 4, "scale": 6, "graph": 7, "loop": 8}[mode]
    if stage == "factor":
        request = b"F" + bytes([coefficient])
    elif stage == intermediate:
        request = b"S" + (folder / "factor.out").read_bytes()
    else:
        request = b"A"
    (folder / "request").write_bytes(request)
    modules = ["request"]
    if stage == "assemble":
        modules.extend(["analytic", "certificate"])
    output, serial = boot_guest(folder, config["kernel"], config["qemu"], config["firmware"], modules)
    (folder / (stage + ".serial")).write_bytes(serial)
    if stage == "factor":
        expected_factor = {"adjoint": bytes([3, 3, 4]), "finite": bytes([3, 8])}.get(
            mode, bytes([1, coefficient]))
        if mode == "scale":
            expected_factor = bytes((1 << i) | (1 << j) for i in range(6)
                                    for j in range(i + 1, 6) if i // 2 != j // 2)
        if mode == "graph":
            expected_factor = bytes((a % 3 + (-1 if a >= 3 else 1) * (b % 3)) % 3
                                    + 3 * ((a // 3 + b // 3) % 2)
                                    for a in range(6) for b in range(6))
        if mode == "loop":
            from itertools import permutations
            payload = [2, 8]
            for p in permutations(range(3)):
                parity = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2
                payload.extend([parity, *p])
            from math import factorial
            for n in range(1, 4):
                payload.extend(factorial(2 * n + 1).to_bytes(2, "little"))
            expected_factor = bytes(payload)
        if output != expected_factor:
            raise ValueError("unexpected guest coefficient vector")
        (folder / "factor.out").write_bytes(output)
        launch(intermediate, folder, config)
    elif stage == intermediate:
        if not output.startswith(marker):
            raise ValueError("missing generated control boundary")
        (folder / "certificate").write_bytes(output)
        launch("assemble", folder, config)
    else:
        (folder / filename.name).write_bytes(output)


def generate(folder, kernel, pcp_source, qemu, firmware, template, dispatcher=None,
             register=None, actor="Director-D4", difference=False, adjoint=False, mode=None):
    if mode is None:
        mode = "adjoint" if adjoint else ("difference" if difference else "positive")
    filename, _, _ = result_spec(mode)
    package = kernel_package(kernel, pcp_source)
    flags = ["-DD4_POSITIVE_TIME"]
    if mode == "loop":
        flags.append("-DD4_ORDINARY_LOOP")
    elif mode == "graph":
        flags.append("-DD4_GRAPH_HOLONOMIES")
    elif mode == "scale":
        flags.append("-DD4_ELECTRIC_SCALE")
    elif mode == "finite":
        flags.append("-DD4_FINITE_READINGS")
    elif mode == "adjoint":
        flags.append("-DD4_ADJOINT_BAND")
    elif mode == "difference":
        flags.append("-DD4_DIFFERENCE")
    build_guest(folder, package, flags)
    config = dict(kernel=str(kernel), qemu=qemu, firmware=str(firmware) if firmware else None,
                  dispatcher=str(dispatcher) if dispatcher else None,
                  register=str(register) if register else None, actor=actor, mode=mode)
    (folder / "config.json").write_text(json.dumps(config))
    (folder / "analytic").write_bytes(template)
    launch("factor", folder, config)
    return (folder / filename.name).read_bytes()


def main():
    if len(sys.argv) == 4 and sys.argv[1] == "--worker" and sys.argv[2] in (*STAGES, "divergence", "moments", "flux", "words", "wick"):
        worker(sys.argv[2], Path(sys.argv[3]))
        return
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--kernel", type=Path, required=True)
    p.add_argument("--pcp-source", type=Path, required=True)
    p.add_argument("--qemu", default="qemu-system-x86_64")
    p.add_argument("--firmware", type=Path)
    p.add_argument("--dispatcher", type=Path, help="optional PCP register-mode process launcher")
    p.add_argument("--register", type=Path)
    p.add_argument("--actor", default="Director-D4")
    modes = p.add_mutually_exclusive_group()
    modes.add_argument("--ordinary-loop", dest="mode", action="store_const", const="loop",
                       help="replay the ordinary Wilson trace and Wick module")
    modes.add_argument("--graph-holonomies", dest="mode", action="store_const", const="graph",
                       help="replay the coarse holonomy and shared-path module")
    modes.add_argument("--electric-scale", dest="mode", action="store_const", const="scale",
                       help="replay the electric flux and shell module")
    modes.add_argument("--finite-readings", dest="mode", action="store_const", const="finite",
                       help="replay the finite correlation-matrix module")
    modes.add_argument("--adjoint", dest="mode", action="store_const", const="adjoint", help="replay the adjoint plaquette module")
    modes.add_argument("--difference", dest="mode", action="store_const", const="difference", help="replay the gap-above-vacuum module")
    args = p.parse_args()
    if bool(args.dispatcher) != bool(args.register):
        p.error("--dispatcher and --register must be supplied together")
    mode = args.mode or "positive"
    filename, marker, intermediate = result_spec(mode)
    expected = filename.read_bytes()
    if expected.count(marker) != 1:
        raise ValueError("expected one guest control boundary")
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        actual = generate(folder, args.kernel.resolve(), args.pcp_source.resolve(), args.qemu,
                          args.firmware.resolve() if args.firmware else None, expected.split(marker)[0],
                          args.dispatcher.resolve() if args.dispatcher else None,
                          args.register.resolve() if args.register else None, args.actor, mode=mode)
        if actual != expected:
            raise ValueError("native pipeline produced different Lean bytes")
        print("guest ELF", digest((folder / "d4.elf").read_bytes()))
        print("Lean source", digest(actual), f"({len(actual)} bytes)")
        for stage in ("factor", intermediate, "assemble"):
            print(stage, digest((folder / (stage + ".serial")).read_bytes()))


if __name__ == "__main__":
    main()

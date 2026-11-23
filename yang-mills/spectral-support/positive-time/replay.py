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
STAGES = ("factor", "square", "assemble")


def launch(stage, folder, config):
    command = [sys.executable, "-I", __file__, "--worker", stage, str(folder)]
    if config["dispatcher"]:
        register = config["register"] if stage == "factor" else "-"
        command = [config["dispatcher"], "--register", register, config["actor"],
                   "positive-" + stage, "--", *command]
    subprocess.run(command, check=True)


def worker(stage, folder):
    config = json.loads((folder / "config.json").read_text())
    if stage == "factor":
        request = b"F\x02"
    elif stage == "square":
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
        if output != bytes([1, 2]):
            raise ValueError("unexpected linear factor")
        (folder / "factor.out").write_bytes(output)
        launch("square", folder, config)
    elif stage == "square":
        if not output.startswith(MARKER):
            raise ValueError("missing generated control boundary")
        (folder / "certificate").write_bytes(output)
        launch("assemble", folder, config)
    else:
        (folder / "PositiveTime.lean").write_bytes(output)


def generate(folder, kernel, pcp_source, qemu, firmware, template, dispatcher=None,
             register=None, actor="Director-D4"):
    package = kernel_package(kernel, pcp_source)
    build_guest(folder, package, ["-DD4_POSITIVE_TIME"])
    config = dict(kernel=str(kernel), qemu=qemu, firmware=str(firmware) if firmware else None,
                  dispatcher=str(dispatcher) if dispatcher else None,
                  register=str(register) if register else None, actor=actor)
    (folder / "config.json").write_text(json.dumps(config))
    (folder / "analytic").write_bytes(template)
    launch("factor", folder, config)
    return (folder / "PositiveTime.lean").read_bytes()


def main():
    if len(sys.argv) == 4 and sys.argv[1] == "--worker" and sys.argv[2] in STAGES:
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
    args = p.parse_args()
    if bool(args.dispatcher) != bool(args.register):
        p.error("--dispatcher and --register must be supplied together")
    expected = (HERE / "PositiveTime.lean").read_bytes()
    if expected.count(MARKER) != 1:
        raise ValueError("expected one guest control boundary")
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        actual = generate(folder, args.kernel.resolve(), args.pcp_source.resolve(), args.qemu,
                          args.firmware.resolve() if args.firmware else None, expected.split(MARKER)[0],
                          args.dispatcher.resolve() if args.dispatcher else None,
                          args.register.resolve() if args.register else None, args.actor)
        if actual != expected:
            raise ValueError("native pipeline produced different Lean bytes")
        print("guest ELF", digest((folder / "d4.elf").read_bytes()))
        print("Lean source", digest(actual), f"({len(actual)} bytes)")
        for stage in STAGES:
            print(stage, digest((folder / (stage + ".serial")).read_bytes()))


if __name__ == "__main__":
    main()

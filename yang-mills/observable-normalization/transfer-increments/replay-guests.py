"""Boot each requested worker and compare its serial output with the checked Lean source."""
import argparse
import hashlib
from pathlib import Path
import subprocess
import tempfile
import time

HERE = Path(__file__).resolve().parent
KERNEL_MEASUREMENTS = {
    "e1b3d972eea2e7825fee09bf8f792e06260f132144ca97d1cf2d81bfa645c414":
        "e90d5278060aaae6bef083d6e45d7b182206db7ac8fe6402b7e16b667c886dc6",
    "d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f":
        "0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_worker(args, directory, role, request):
    name = f"w{role}.elf"
    elf = directory / name
    subprocess.run(["gcc", "-Os", "-ffreestanding", "-mcmodel=large", "-fno-pie",
                    "-nostdlib", "-static", f"-Wl,--build-id=none,-T,{HERE.parent / 'link.ld'}",
                    f"-DROLE={role}", str(args.proof.parent / "worker.c"), "-o", str(elf)], check=True)
    serial = directory / f"{role}.serial"
    command = [args.qemu]
    if args.firmware:
        command += ["-L", str(args.firmware.resolve())]
    command += ["-machine", "pc", "-cpu", "max", "-m", "128M", "-nic", "none",
                "-display", "none", "-monitor", "none", "-serial", f"file:{serial}",
                "-no-reboot", "-kernel", str(args.kernel.resolve()),
                "-append", f"auto={name} image={args.measurement} then=off", "-initrd", name]
    proc = subprocess.Popen(command, cwd=directory)
    try:
        deadline = time.monotonic() + args.timeout
        while True:
            lines = serial.read_bytes().splitlines() if serial.exists() else []
            if any(line.startswith(b"ALL SELF-TESTS PASS.") for line in lines):
                break
            if proc.poll() is not None or time.monotonic() >= deadline:
                raise RuntimeError(f"{name} terminated early or timed out")
            time.sleep(0.1)
    finally:
        if proc.poll() is None:
            proc.terminate()
        proc.wait()
    lines = serial.read_text().splitlines()
    start = f"starting {name} ({elf.stat().st_size} bytes, SHA-256 {digest(elf)})"
    begin = lines.index(start)
    end = next(i for i in range(begin + 1, len(lines))
               if lines[i].startswith(f"{name} ended DONE: exit 0 "))
    output = lines[begin + 1:end]
    requests = [line for line in output if line.startswith("A4 CHILD ")]
    if requests != ([f"A4 CHILD {request}"] if request else []) or output[-1:] != ["A4 FINISHED"]:
        raise RuntimeError(f"unexpected completion or child request from {name}")
    if not any(args.measurement in line and "equal to the value the loader named" in line for line in lines[:begin]):
        raise RuntimeError("kernel measurement missing")
    print(name, digest(elf), next(line for line in lines[end:] if line.startswith("kernel register:")))
    return [line.removeprefix("A4 LEAN ") for line in output if line.startswith("A4 LEAN ")]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kernel", type=Path)
    parser.add_argument("--proof", type=Path, default=HERE / "TransferIncrement.lean",
                        help="Expected Lean file; its sibling worker.c generates it")
    parser.add_argument("--qemu", default="qemu-system-x86_64")
    parser.add_argument("--firmware", type=Path)
    parser.add_argument("--timeout", type=float, default=120)
    args = parser.parse_args()
    args.measurement = KERNEL_MEASUREMENTS.get(digest(args.kernel))
    if args.measurement is None:
        raise ValueError("kernel differs from the pinned run")
    generated = []
    with tempfile.TemporaryDirectory() as temp:
        for role, request in enumerate(["spectrum", "limit", None]):
            generated.extend(run_worker(args, Path(temp), role, request))
    source = ("\n".join(generated) + "\n").encode()
    if source != args.proof.read_bytes():
        raise ValueError("guest output differs from committed Lean bytes")
    print("generated source SHA-256", hashlib.sha256(source).hexdigest())


if __name__ == "__main__":
    main()

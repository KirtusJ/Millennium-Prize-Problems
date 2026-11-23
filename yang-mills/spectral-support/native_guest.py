"""Compile, measure and boot a freestanding D4 proof guest on the pinned PCP kernel."""
import hashlib
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
EXPECTED_KERNEL = "d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f"
EXPECTED_MEASUREMENT = "0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def kernel_package(kernel, source):
    if digest(kernel.read_bytes()) != EXPECTED_KERNEL:
        raise ValueError("kernel file differs from the recorded image")
    package = source / "PCP_OS_Rust/crates/pcpos-kernel"
    measurement = subprocess.check_output(
        [sys.executable, package / "tools/measure.py", kernel], text=True
    ).strip()
    if measurement != EXPECTED_MEASUREMENT:
        raise ValueError("kernel measurement differs from the recorded image")
    return package


def build_guest(work, package, flags):
    subprocess.run([
        "cc", *flags, "-std=c11", "-O2", "-Wall", "-Wextra", "-Werror", "-ffreestanding",
        "-fno-stack-protector", "-fno-pie", "-mno-red-zone", "-mgeneral-regs-only",
        "-mcmodel=large", "-c", HERE / "emit_e1.c", "-o", "guest.o"
    ], check=True, cwd=work)
    subprocess.run([
        "ld", "--build-id=none", "-z", "noexecstack", "-T", package / "programs/pcp-fib/link.ld",
        "guest.o", "-o", "d4.elf"
    ], check=True, cwd=work)


def boot_guest(work, kernel, qemu, firmware, modules):
    measurement = EXPECTED_MEASUREMENT
    guest_hash = digest((work / "d4.elf").read_bytes())
    command = [qemu]
    if firmware:
        command += ["-L", str(firmware)]
    command += [
        "-machine", "microvm,isa-serial=on,pic=on,pit=on,rtc=on", "-accel", "tcg,tb-size=4",
        "-icount", "shift=3,align=off,sleep=off", "-cpu", "max", "-m", "32M",
        "-nodefaults", "-nic", "none", "-display", "none", "-monitor", "none",
        "-serial", "stdio", "-no-reboot", "-kernel", str(kernel), "-initrd", ",".join(["d4.elf", *modules]),
        "-append", f"auto=d4.elf then=off image={measurement}",
        "-device", "isa-debug-exit,iobase=0xf4,iosize=0x04"
    ]
    result = subprocess.run(command, cwd=work, capture_output=True, timeout=90)
    log = result.stdout.decode("utf-8").replace("\r", "")
    receipts = [
        f"{measurement} (measured; equal to the value the loader named)" in log,
        re.search(r"^starting d4\.elf .*" + guest_hash, log, re.M),
        re.search(r"^d4\.elf ended \w+: exit 0\b", log, re.M),
    ]
    if result.returncode != 33 or not all(receipts):
        raise RuntimeError(f"QEMU {result.returncode}\n{log[-1500:]}\n{result.stderr.decode()}")
    frames = re.findall(r"^D4 ([0-9a-f]+)$", log, re.M)
    emitted = bytes.fromhex("".join(frames))
    return emitted, result.stdout

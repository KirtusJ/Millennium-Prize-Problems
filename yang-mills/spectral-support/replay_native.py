"""Regenerate the committed Lean bytes using a measured PCP OS guest."""
import argparse
from pathlib import Path
import sys
import tempfile

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
from native_guest import boot_guest, build_guest, digest, kernel_package

MARKER = b"-- BEGIN PCP OS generated finite certificate\n"


def replay(kernel, source, qemu, firmware, diagonal=False):
    package = kernel_package(kernel, source)
    filename = "diagonal/CoherentDiagonal.lean" if diagonal else "SpectralLimit.lean"
    marker = b"-- BEGIN PCP OS generated array control\n" if diagonal else MARKER
    flags = ["-DD4_DIAGONAL"] if diagonal else []
    committed = (HERE / filename).read_bytes()
    if committed.count(marker) != 1:
        raise ValueError("expected a single certificate boundary")
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        (work / "template").write_bytes(committed.split(marker)[0])
        build_guest(work, package, flags)
        emitted, _ = boot_guest(work, kernel, qemu, firmware, ["template"])
        guest_hash = digest((work / "d4.elf").read_bytes())
    if emitted != committed:
        raise ValueError("generated Lean source differs from the committed file")
    print(f"guest ELF {guest_hash}\nLean source {digest(emitted)} ({len(emitted)} bytes)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kernel", type=Path, required=True)
    parser.add_argument("--pcp-source", type=Path, required=True)
    parser.add_argument("--qemu", default="qemu-system-x86_64")
    parser.add_argument("--firmware", type=Path)
    parser.add_argument("--diagonal", action="store_true", help="replay the coherent-diagonal module")
    args = parser.parse_args()
    replay(args.kernel.resolve(), args.pcp_source.resolve(), args.qemu,
           args.firmware.resolve() if args.firmware else None, args.diagonal)

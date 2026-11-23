"""Check that strengthening a bound or changing the star fails at its declaration."""
import argparse
from pathlib import Path
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).with_name("ElectricScale.lean").read_text()
    changes = [
        ("free endpoint", "1-l/u=2*(1-c) := by", "1-l/u=(1-c) := by", "freeEnd"),
        ("smaller ultraviolet leakage", "m ≤ 8*eps := by", "m ≤ 4*eps := by", "twistLeakage"),
        ("missing star face", "24, 40]", "24, 24]", "starSpectrum"),
        ("wrong spectral multiplicity", "(12, 16), (16, 9)", "(12, 15), (16, 10)", "starSpectrum"),
    ]
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "Negative.lean"
        for label, old, new, theorem in changes:
            assert source.count(old) == 1
            altered = source.replace(old, new)
            path.write_text(altered)
            start = altered[:altered.index("theorem " + theorem + " ")].count("\n") + 1
            end = altered.index("\n\n", altered.index("theorem " + theorem + " "))
            last = altered[:end].count("\n") + 1
            run = subprocess.run(["lake", "env", "lean", str(path)], cwd=args.mathlib,
                                 capture_output=True, text=True)
            messages = [line for line in (run.stdout + run.stderr).splitlines()
                        if ": error:" in line and line.startswith(str(path) + ":")]
            if run.returncode == 0 or not any(start <= int(line.split(":")[1]) <= last for line in messages):
                raise RuntimeError(f"{label}: {messages}")
            print(f"{label}: rejected at {theorem}", flush=True)


if __name__ == "__main__":
    main()

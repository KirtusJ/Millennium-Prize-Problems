"""Check that changing a trace order, weight, or time bound fails at its declaration."""
import argparse
from pathlib import Path
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).with_name("OrdinaryLoop.lean").read_text()
    changes = [
        ("reverse cubic orientation", "((a*c*b).re-(a*b*c).re)", "((a*b*c).re-(a*c*b).re)", "orientedWord"),
        ("double determinant coefficient", "wick K terms=6*", "wick K terms=12*", "determinantWick"),
        ("remove triangle pairing", "matchings 3 (List.range 6)=8", "matchings 3 (List.range 6)=7", "squarePairings"),
        ("overstate tail suppression", "≤ exp (-h*R)*", "≤ exp (-h*R-1)*", "tiltedTail"),
        ("erase winding rank", "4*(a*c-b^2)", "2*(a*c-b^2)", "windingGram"),
        ("wrong radial Wick count", "Nat.factorial 7=5040", "Nat.factorial 7=5039", "radialCounts"),
        ("double dimensionless weight", "32*((3/2)*k^2)^3", "64*((3/2)*k^2)^3", "orientedRatio"),
    ]
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "Negative.lean"
        for label, old, new, theorem in changes:
            assert source.count(old) == 1
            altered = source.replace(old, new)
            path.write_text(altered)
            start = altered[:altered.index("theorem " + theorem)].count("\n") + 1
            end = altered.index("\n\n", altered.index("theorem " + theorem))
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

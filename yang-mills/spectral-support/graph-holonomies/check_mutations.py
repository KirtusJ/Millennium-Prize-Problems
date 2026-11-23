"""Check that strengthening a bound or changing the star fails at its declaration."""
import argparse
from pathlib import Path
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).with_name("GraphHolonomies.lean").read_text()
    changes = [
        ("reversed density budget", "(1-δ^2)/w ≤ 2-w", "(1+δ^2)/w ≤ 2-w", "reciprocalSecant"),
        ("discarding cheaply", "(1:ℝ) ≤ 2*(1-x) := by", "(1:ℝ) ≤ (1-x) := by", "discardedClock"),
        ("doubling the path heat time", "β/(2*(6*β*x))", "β/(6*β*x)", "sixStapleTime"),
        ("independent duplicated path", "[18,9,9,0,0,0]", "[6,6,6,6,6,6]", "sharedWord"),
        ("incorrect next mean", "bulk=1/2 := by", "bulk=1/4 := by", "limitingBias"),
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

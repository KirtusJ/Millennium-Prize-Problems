"""Check that changing a slab identity, dispersion factor, or face count fails at its declaration."""
import argparse
from pathlib import Path
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).with_name("ElectricSlab.lean").read_text()
    changes = [
        ("insert an extra centered term", "⟫_ℝ-m^2 := by", "⟫_ℝ-2*m^2 := by", "slabCenter"),
        ("reverse cutoff product term", "b*(∑ i ∈ s, (a-f i)) -", "b*(∑ i ∈ s, (a-f i)) +", "cutoffLaplacian"),
        ("alter two-particle phase angular weight", "=4*phase E k := by", "=3*phase E k := by", "angularIntegral"),
        ("remove the threshold weight", "phase k k=8/15*k^4", "phase k k=0", "threshold"),
        ("share a face on adjacent slabs", "faceCount 4=0 ∧", "faceCount 4=1 ∧", "latticeIncidence"),
        ("replace the traceless angular node", "3*h^2-10*h*s+3*s^2) := by ring", "3*h^2-9*h*s+3*s^2) := by ring", "splitChannels"),
        ("double the fourth connected ratio", "(16*18:ℚ)/(2*18)^2=2/9", "(16*18:ℚ)/(2*18)^2=4/9", "collinearWeights"),
        ("shift the marginal normalization", "z^2*phase 1 z)=16/105", "z^2*phase 1 z)=15/105", "marginalIntegral"),
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

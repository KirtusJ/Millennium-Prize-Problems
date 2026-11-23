"""Check that changing a response sign, normalization or native residue fails at its declaration."""
import argparse
from pathlib import Path
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).with_name("ScalarResponse.lean").read_text()
    changes = [
        ("reverse the tilt sign", "(-(v/Z b - (N b/Z b)*(u/Z b)))", "((v/Z b - (N b/Z b)*(u/Z b)))", "tilt"),
        ("remove one explicit coupling", "2*(b^2*k)-b*", "(b^2*k)-b*", "integratedResponse"),
        ("change the integrated slope", "x*(3*v₁) := by", "x*(2*v₁) := by", "firstRadialTerm"),
        ("lose the circle improvement", "(1/3)/4", "(1/4)/4", "radialMatch"),
        ("change the character sphere", "15/6^2)=5/48", "15/6^2)=6/48", "sphereAtUnit"),
        ("alter a native Wilson pair", "List Nat := [1, 23, 1, 84", "List Nat := [1, 24, 1, 84", "boxResidues"),
        ("force temporal Wilson null", "timeWilson2 < 0 := by", "timeWilson2 = 0 := by", "timeFilter"),
        ("reverse transverse response", "spaceWilson2 < 0 := by", "spaceWilson2 > 0 := by", "spaceFilter"),
        ("alter a native filtered residue", "List Nat := [64, 95, 0, 0, 32]", "List Nat := [64, 95, 0, 0, 33]", "nullResidues"),
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

"""Check that changing a duality sign, response normalization or native residue fails at its declaration."""
import argparse
from pathlib import Path
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).with_name("DualScalar.lean").read_text()
    changes = [
        ("lose the inverse determinant", "toBlocks₂₂.det=A.det", "toBlocks₂₂.det=2*A.det", "schurReciprocity"),
        ("reverse cycle parity", "=-(x*y*z) := by", "=(x*y*z) := by", "oddCycle"),
        ("alter reciprocal source contact", "-w+w*(w-1)", "-2*w+w*(w-1)", "radialDifference"),
        ("erase surviving Abelian weight", "=3/4*g*h := by", "=0*g*h := by", "halfDiagonal"),
        ("halve radial action response", "(-10*k)*(3/8*x)", "(-5*k)*(3/8*x)", "actionDependence"),
        ("change leading distance coefficient", "1/(6*p^2)*", "1/(5*p^2)*", "asymptoticRatio"),
        ("alter a reconstructed cube residue", "(999983, 768003)", "(999983, 768004)", "certifiedCube"),
        ("reverse twisted Wilson comparison", "(1440/100000:ℚ)^2<", "(1440/100000:ℚ)^2>", "twistedSignal"),
        ("reverse link-disjoint Wilson bound", "(4105/100000:ℚ)^2<", "(4105/100000:ℚ)^2>", "skewSignal"),
        ("negate the reconstructed link-disjoint cube numerator", "validInteger (-508038751613375745825329566542397440)", "validInteger (508038751613375745825329566542397440)", "certifiedSkewCube"),
        ("change dual Gaussian triangle", "List Nat := [24, 77, 84", "List Nat := [24, 76, 84", "measuredBoundary"),
        ("omit the finite-twist diagonal term", "List Nat := [90, 90, 123, 70, 97]", "List Nat := [90, 90, 123, 70, 0]", "measuredTwist"),
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

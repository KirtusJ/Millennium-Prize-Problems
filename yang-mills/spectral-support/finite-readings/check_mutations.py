"""Reject false variations of the complete Lean module with the same host checker."""
import argparse
from pathlib import Path
import subprocess
import tempfile


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--mathlib", type=Path, required=True)
    options = cli.parse_args()
    source = Path(__file__).with_name("FiniteReadings.lean").read_text()
    variants = {
        "missing null-space control": ("(upper : (q • H - K).PosSemidef)",
                                       "(upper : (q • H + K).PosSemidef)"),
        "overstated open-window mass": (
            "(Ioo q 1).indicator (fun _ => (1-q)^2/4) u := by",
            "(Ioo q 1).indicator (fun _ => (1-q)^2/8) u := by"),
        "unearned local kinetic constant": ("∧ K ≤ 256*g^2/3 := by", "∧ K ≤ 128*g^2/3 := by"),
        "reversed measured cross term": ("[(65, -63),", "[(65, 63),"),
        "wrong inertia": ("= [0,1,1,2] ∧", "= [0,1,0,2] ∧"),
        "insufficient Ritz allowance": ("= 4/6953764855522223076923 := by",
                                       "= 3/6953764855522223076923 := by"),
        "overstated positive-time margin": ("15/16384 ≤ measured := by", "16/16384 ≤ measured := by"),
    }
    with tempfile.TemporaryDirectory() as temp:
        target = Path(temp)/"Negative.lean"
        for label, (old, new) in variants.items():
            if source.count(old) != 1:
                raise ValueError(label)
            target.write_text(source.replace(old, new))
            run = subprocess.run(["lake", "env", "lean", str(target)], cwd=options.mathlib,
                                 capture_output=True, text=True)
            errors = [line for line in (run.stdout+run.stderr).splitlines() if "error:" in line]
            if run.returncode == 0 or not errors or "unknown module" in errors[0]:
                raise RuntimeError(f"{label}: {run.stdout[-500:]} {run.stderr[-500:]}")
            print(label, errors[0].replace(str(target), "Negative.lean"), flush=True)


if __name__ == "__main__":
    main()

"""Replay the three-level PCP commission and check the generated Lean proof."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "local-response"))
from replay import run_case, work

TASKS = ["collect-hankel-form", "bound-exponential-base", "certify-signed-form"]
MUTATIONS = (
    (b"u+v+2*R := by ring", b"u+v+R := by ring", "WrongPlane", "unsolved goals"),
    (b"384*m 2+4246", b"384*m 2+4096", "MissingProduct", "unsolved goals"),
    ("3678/10000 ≤ Real.exp".encode(), "3681/10000 ≤ Real.exp".encode(), "WrongExponentialBound", "linarith failed"),
    (b"three moment " + "≤ -100151644".encode(), "three moment ≤ -200151644".encode(), "OverstatedSign", "linarith failed"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "FlowReflection", 14, MUTATIONS)

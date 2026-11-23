"""Replay the three guest generations and mutation-check their Lean output."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "central-quotients" / "local-response"))
from replay import run_case, work

TASKS = ["component-range", "pair-weights", "occupation"]
MUTATIONS = (
    (b" = 8 := by decide", b" = 7 := by decide", "WrongCorners", "is false"),
    (b"= 2*((x-y)^2", b"= 3*((x-y)^2", "WrongRange", "unsolved goals"),
    (b"_ = (p+p*s)*a*h := by ring", b"_ = (p-p*s)*a*h := by ring",
     "WrongPair", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "PeriodicVacuum", 4, MUTATIONS)

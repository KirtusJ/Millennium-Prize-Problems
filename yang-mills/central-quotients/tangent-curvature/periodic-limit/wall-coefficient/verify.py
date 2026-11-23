"""Replay the angular chart and coefficient checks."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["chart-dimension", "angular-jacobian", "signed-total"]
MUTATIONS = (
    (b"= 8 :=", b"= 9 :=", "WrongCount", "is false"),
    (b"-3*h+2*h^2", b"-2*h+2*h^2", "WrongFirst", "unsolved goals"),
    (b"= -10*q", b"= -9*q", "WrongSecond", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "WallCoefficient", 3, MUTATIONS)

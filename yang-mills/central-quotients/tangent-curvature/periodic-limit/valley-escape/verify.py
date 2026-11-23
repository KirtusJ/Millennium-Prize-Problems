"""Replay the normal-area and Gaussian-moment checks."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["normal-pairs", "normal-area", "gaussian-variance"]
MUTATIONS = (
    (b"= 2401 :=", b"= 2400 :=", "WrongCount", "is false"),
    (b"(x*t-y*z)^2", b"(x*t+y*z)^2", "WrongFirst", "unsolved goals"),
    (b"5*(4*v)^2", b"4*(4*v)^2", "WrongSecond", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "ValleyEscape", 3, MUTATIONS)

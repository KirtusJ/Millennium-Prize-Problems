"""Replay the angular-rate and adjacent-difference checks."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["angular-order", "first-gap", "second-gap"]
MUTATIONS = (
    (b"= 220 :=", b"= 219 :=", "WrongCount", "is false"),
    (b"(b-c)*v", b"(b+c)*v", "WrongFirst", "unsolved goals"),
    (b"(a-c)*u", b"(a+c)*u", "WrongSecond", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "TensorCone", 3, MUTATIONS)

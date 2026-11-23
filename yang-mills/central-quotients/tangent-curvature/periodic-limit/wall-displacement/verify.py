"""Replay the magnetic-shift and Gaussian-moment checks."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["wall-support", "magnetic-shift", "endpoint-square"]
MUTATIONS = (
    (b"= 3204 :=", b"= 3205 :=", "WrongCount", "is false"),
    (b"-4*y*d*h^2", b"-3*y*d*h^2", "WrongFirst", "unsolved goals"),
    (b"=h^2 := ", b"=h^3 := ", "WrongSecond", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "WallShift", 3, MUTATIONS)

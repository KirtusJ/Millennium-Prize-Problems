"""Replay the recursive PCP OS rational controls for the time-independent term."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "central-quotients" / "local-response"))
from replay import run_case, work

TASKS = ["center-images", "midpoint-share", "contrast-cancellation"]
MUTATIONS = (
    (b"= 2*d^2", b"= 3*d^2", "WrongOrbit", "unsolved goals"),
    (b"2/10000000000", b"4/10000000000", "WrongShare", "unsolved goals"),
    (b"-(13/3)*d+d", b"-(12/3)*d+d", "WrongContrast", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "StaticFloor", 4, MUTATIONS)

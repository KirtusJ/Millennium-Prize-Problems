"""Run three linked native PCP OS workers and check their emitted Lean declarations."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["spline-mass", "four-rays", "normal-axis"]
MUTATIONS = (
    (b'= (151, 315) :=', b'= (150, 315) :=', 'WrongDensity', 'is false'),
    (b'= (25217, 1620) :=', b'= (25216, 1620) :=', 'WrongEdge', 'is false'),
    (b'= (43186, 315) :=', b'= (43185, 315) :=', 'WrongRest', 'is false'),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "DirectionalTail", 3, MUTATIONS)

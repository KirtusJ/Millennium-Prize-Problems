"""Run three linked native PCP OS workers and check their emitted Lean declarations."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["angular-density", "cone-edge", "small-momentum"]
MUTATIONS = (
    (b'= (2646, 1105) :=', b'= (2645, 1105) :=', 'WrongDensity', 'is false'),
    (b'= (5586, 1105) :=', b'= (5585, 1105) :=', 'WrongEdge', 'is false'),
    (b'= (92169, 16384) :=', b'= (92168, 16384) :=', 'WrongRest', 'is false'),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "MomentumRatio", 4, MUTATIONS)

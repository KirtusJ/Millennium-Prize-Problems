"""Run three linked native PCP OS workers and check their emitted Lean declarations."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["periodic-seams", "cube-tilt", "rate-constants"]
MUTATIONS = (
    (b'= 7 :=', b'= 5 :=', 'WrongCoefficient', 'is false'),
    (b'= 4096 :=', b'= 4095 :=', 'WrongMoment', 'is false'),
    (b'=(z/3-3*s/2)^2', b'=(z/3+3*s/2)^2', 'WrongCentering', 'unsolved goals'),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "ActionDeviation", 4, MUTATIONS)

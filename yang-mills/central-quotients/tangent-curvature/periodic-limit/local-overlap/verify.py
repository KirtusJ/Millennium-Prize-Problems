"""Run three linked native PCP OS workers and check their emitted Lean declarations."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["dispersion-symbol", "separate-clocks", "midpoint-overlap"]
MUTATIONS = (
    (b'= 1295 :=', b'= 1294 :=', 'WrongCoefficient', 'is false'),
    (b'= 2 :=', b'= 3 :=', 'WrongMoment', 'is false'),
    (b'= 84 :=', b'= 83 :=', 'WrongWindow', 'is false'),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "LocalOverlap", 4, MUTATIONS)

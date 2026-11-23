"""Run three linked native PCP OS workers and check their emitted Lean declarations."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["shared-link", "face-moments", "score-variance"]
MUTATIONS = (
    (b'= 512 :=', b'= 5 :=', 'WrongCoefficient', 'is false'),
    (b'= 8 :=', b'= 7 :=', 'WrongMoment', 'is false'),
    (b'-13*a^8', b'-12*a^8', 'WrongSign', 'unsolved goals'),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "ElectricScore", 4, MUTATIONS)

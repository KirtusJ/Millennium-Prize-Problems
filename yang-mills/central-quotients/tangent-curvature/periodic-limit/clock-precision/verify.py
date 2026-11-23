"""Run three linked native PCP OS workers and check their emitted Lean declarations."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["binomial-tail", "stride-residue", "lifted-polynomial"]
MUTATIONS = (
    (b'= 18 :=', b'= 5 :=', 'WrongCoefficient', 'is false'),
    (b'= 47840 :=', b'= 7 :=', 'WrongMoment', 'is false'),
    (b'=u^2*(-2+', b'=u^2*(-3+', 'WrongLift', 'unsolved goals'),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "ClockPrecision", 4, MUTATIONS)

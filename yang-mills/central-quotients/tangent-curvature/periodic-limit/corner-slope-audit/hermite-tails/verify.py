"""Run three linked native PCP OS workers and check their emitted Lean declarations."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "local-response"))
from replay import run_case, work

TASKS = ["hermite-ode", "moment-brackets", "edge-witness"]
MUTATIONS = (
    (b'= 91 :=', b'= 5 :=', 'WrongOdeCount', 'is false'),
    (b'= 135 :=', b'= 4095 :=', 'WrongMinorCount', 'is false'),
    (b'2*z^4+z^3', b'2*z^4-z^3', 'WrongMajorant', 'unsolved goals'),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "HermiteTail", 4, MUTATIONS)

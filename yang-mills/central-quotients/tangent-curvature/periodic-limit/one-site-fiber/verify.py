"""Run three linked native PCP OS workers and check their emitted Lean declarations."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["angular-polynomials", "frozen-radius", "fourth-moment"]
MUTATIONS = (
    (b'= 14 :=', b'= 5 :=', 'WrongAngular', 'is false'),
    (b'= 14464 :=', b'= 4095 :=', 'WrongBlock', 'is false'),
    (b'+(2-3*a+b)/6', b'+(2-2*a+b)/6', 'WrongConstant', 'unsolved goals'),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "OneSiteFiber", 4, MUTATIONS)

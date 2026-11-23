"""Run three linked native PCP OS workers and check their emitted Lean declarations."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["physical-corners", "shared-link-average", "truncated-moments"]
MUTATIONS = (
    (b'= 26880 :=', b'= 5 :=', 'WrongReturns', 'is false'),
    (b'= 1024 :=', b'= 4095 :=', 'WrongLinkCount', 'is false'),
    (b'=(2*k+1)/8', b'=(2*k+3)/8', 'WrongVariance', 'unsolved goals'),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "CornerSlopeAudit", 4, MUTATIONS)

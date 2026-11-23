"""Replay the native PCP flow commission on a fresh desk and check its Lean output."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "local-response"))
from replay import run_case, work

TASKS = ["count-visible-shells", "bound-reflected-form", "check-magnetic-density"]
MUTATIONS = (
    (b"= (4,8)", b"= (4,4)", "MissedTemporalSign", "is false"),
    (b"upperWitness = -9862", b"upperWitness = 9862", "ReversedReflectionSign", "is false"),
    (b"= (5,8)", b"= (8,5)", "ExchangedThresholds", "is false"),
    (b")=4/3", b")=3/4", "FlowNormalization", "unsolved goals"),
    (b"=a-2*b+c := by ring", b"=a-b+c := by ring", "MissingCrossTerm", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "SpatialFlow", 19, MUTATIONS)

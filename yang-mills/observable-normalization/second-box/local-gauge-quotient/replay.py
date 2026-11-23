"""Run the finite checks using the repository's three-level PCP OS supervisor."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "central-quotients" / "local-response"))
from replay import run_case, work

TASKS = ["orbit-rank", "density-coefficient", "endpoint-sums"]
MUTATIONS = (
    (b"= (51 : Nat) :=", b"= (50 : Nat) :=", "WrongModes", "is false"),
    (b"= 14 :=", b"= 13 :=", "WrongMargin", "is false"),
    (b"= 192 :=", b"= 191 :=", "WrongCenters", "is false"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "LocalGauge", 3, MUTATIONS)

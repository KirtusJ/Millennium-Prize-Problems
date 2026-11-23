"""Run the finite checks using the repository's three-level PCP OS supervisor."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "central-quotients" / "local-response"))
from replay import run_case, work

TASKS = ["hard-modes", "curvature-sign", "center-relabeling"]
MUTATIONS = (
    (b"= 42 :=", b"= 48 :=", "WrongModes", "is false"),
    (b"(6-1-2)^2", b"(6-1-3)^2", "WrongMargin", "is false"),
    (b"= 64 :=", b"= 63 :=", "WrongCenters", "is false"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "FlatHolonomies", 3, MUTATIONS)

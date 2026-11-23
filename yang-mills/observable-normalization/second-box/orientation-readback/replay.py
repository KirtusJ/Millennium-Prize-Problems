"""Run the finite checks using the repository's three-level PCP OS supervisor."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "central-quotients" / "local-response"))
from replay import run_case, work

TASKS = ["inverse-weight", "signed-shell", "scalar-control"]
MUTATIONS = (
    (b"= 29 :=", b"= 28 :=", "WrongModes", "is false"),
    (b"= 88 :=", b"= 87 :=", "WrongMargin", "is false"),
    (b"= 24*21/2 :=", b"= 24*20/2 :=", "WrongCenters", "is false"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "Orientation", 3, MUTATIONS)

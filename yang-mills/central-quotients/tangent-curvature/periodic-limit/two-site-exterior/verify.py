"""Run the native rank, center-character and magnetic-remainder checks."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["curl-ranks", "sector-signs", "affine-remainder"]
MUTATIONS = (
    (b"= 42 :=", b"= 41 :=", "WrongRank", "is false"),
    (b"= 56 :=", b"= 57 :=", "WrongOrthogonality", "is false"),
    (b"(e*v+r)^2", b"(e*v-r)^2", "WrongSquare", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "TwoSiteExterior", 3, MUTATIONS)

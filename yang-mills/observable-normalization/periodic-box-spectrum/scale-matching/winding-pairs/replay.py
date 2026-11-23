"""Run the finite checks using the repository's three-level PCP OS supervisor."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "central-quotients" / "local-response"))
from replay import run_case, work

TASKS = ["diagonal-floor", "spectral-weight", "common-mixing"]
MUTATIONS = (
    (b"(1-w)*l+w*u :=", b"(1-w)*l-w*u :=", "DiagonalSign", "error:"),
    ("r-q ≤ (1-q)*w".encode(), "r-q ≥ (1-q)*w".encode(), "WeightDirection", "error:"),
    (b"+c*d-a*b :=", b"-c*d-a*b :=", "ProductSign", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "WindingPairs", 4, MUTATIONS)

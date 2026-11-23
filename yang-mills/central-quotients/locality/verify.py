"""Boot three native PCP workers and check the generated locality lemmas."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "local-response"))
from replay import run_case, work

TASKS = ["count-link-midpoints", "bound-weighted-walks", "integrate-time-kernels"]
MUTATIONS = (
    (b"(4,8,4)", b"(4,7,4)", "MissingCorner", "is false"),
    (b"diagonalTwo = 28", b"diagonalTwo = 16", "LostReturn", "is false"),
    (b"(6,120,5040)", b"(2,24,720)", "EvenDenominator", "is false"),
    (b"r^2 \xe2\x89\xa4 2*y := by", b"r^2 \xe2\x89\xa4 y := by", "FalsePhaseCost", "linarith failed"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "Locality", 14, MUTATIONS)

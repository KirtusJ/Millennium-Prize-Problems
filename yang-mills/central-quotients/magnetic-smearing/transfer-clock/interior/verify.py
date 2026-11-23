"""Run the three measured native generations and check their Lean output."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["check-interior-width", "square-shifted-filter", "sum-seventh-harmonics"]
MUTATIONS = (
    (b"(u-1/2)^2+v^2 < (u+1/2)", b"(u-1/2)^2+v^2 > (u+1/2)", "ReversedTail", "linarith failed"),
    (b"= 25281 := by decide", b"= 25280 := by decide", "WrongFilterNorm", "is false"),
    (b"= 309248 := by decide", b"= 309247 := by decide", "WrongSeventhMoment", "is false"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "InteriorClock", 11, MUTATIONS)

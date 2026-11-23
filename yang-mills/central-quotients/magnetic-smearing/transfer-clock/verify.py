"""Replay the three native PCP generations and audit the generated Lean proof."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "local-response"))
from replay import run_case, work

TASKS = ["bound-clock-error", "check-stationary-flux", "project-haar-character"]
MUTATIONS = (
    (b"*(9/64)>1/64", b"*(9/64)>1/32", "ExcessClockFloor", "unsolved goals"),
    (b".length = 36", b".length = 35", "WrongSeam", "is false"),
    (b"(3-(4*x^2-1))/8", b"(3-(4*x^2-1))/4", "WrongCharacter", "unsolved goals"),
    (b"*(1/4-1/8)=1/4", b"*(1/4-1/8)=1/8", "WrongHaarMoment", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "TransferClock", 18, MUTATIONS)

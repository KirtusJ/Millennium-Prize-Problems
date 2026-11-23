"""Run the native census, pair comparison, and periodicity checks."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["barrier-multiplicities", "pair-comparison", "center-periodicity"]
MUTATIONS = (
    (b"= 4 :=", b"= 5 :=", "WrongMultiplicity", "is false"),
    (b"= 17424 :=", b"= 17423 :=", "WrongCount", "is false"),
    (b"2*s*(1+2*a)", b"2*s*(1+a)", "WrongDerivative", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "SecondBoxHolonomy", 3, MUTATIONS)

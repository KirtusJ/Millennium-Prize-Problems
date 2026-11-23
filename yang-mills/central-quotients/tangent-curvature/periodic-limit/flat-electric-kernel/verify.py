"""Run the native hopping, Weyl-sector and remainder checks."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["twisted-hopping", "common-weyl", "center-remainder"]
MUTATIONS = (
    (b"= 96 :=", b"= 95 :=", "WrongHopping", "is false"),
    (b"= 8 :=", b"= 0 :=", "WrongWeyl", "is false"),
    (b"(1-2*t)", b"(1-t)", "WrongAngle", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "FlatElectric", 3, MUTATIONS)

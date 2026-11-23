"""Run the native shell-count and Fourier coefficient checks."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["hard-shells", "fourth-derivative", "symbol-coefficient"]
MUTATIONS = (
    (b"= 216 :=", b"= 215 :=", "WrongTrace", "is false"),
    (b"= [6,12,8] :=", b"= [6,11,8] :=", "WrongCount", "is false"),
    (b"24*(4-8*s)", b"24*(4-7*s)", "WrongSymbol", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "FlatRefinement", 3, MUTATIONS)

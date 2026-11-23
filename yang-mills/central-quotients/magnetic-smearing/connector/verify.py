"""Boot the connector commission, assemble the guest fragments, and challenge the Lean result."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "local-response"))
from replay import run_case, work

TASKS = ["isolate-trunk", "bound-two-step", "select-quadratic-mode"]
MUTATIONS = (
    (b"= (1,0,1)", b"= (0,0,1)", "AdjacentSlice", "is false"),
    (b"= (6,0,2)", b"= (6,0,3)", "HaarSecondMoment", "is false"),
    (b"=Real.exp (-2*", b"=Real.exp (-3*", "WrongEnergyBound", "unsolved goals"),
    (b"=4*h*(z+h)*(1-k)", b"=2*h*(z+h)*(1-k)", "LostAngularFactor", "unsolved goals"),
    (b"[8,12,16]", b"[4,12,16]", "LinearHermiteMode", "is false"),
    (b"=1/1120", b"=1/560", "SimplexFactor", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "MagneticConnector", 24, MUTATIONS)

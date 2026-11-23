"""Run the finite checks using the repository's three-level PCP OS supervisor."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "central-quotients" / "local-response"))
from replay import run_case, work

TASKS = ["wall-support", "potential", "correction"]
MUTATIONS = (
    (b"+l^2*u^2 :=", b"-l^2*u^2 :=", "BadWall", "unsolved goals"),
    (b"+2*b^2*u^3 :=", b"+3*b^2*u^3 :=", "BadPotential", "unsolved goals"),
    (b"-1/2-2*l :=", b"-1/2+2*l :=", "BadCorrection", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "CurvedWall", 3, MUTATIONS)

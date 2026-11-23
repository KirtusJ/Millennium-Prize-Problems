"""Run the finite checks using the repository's three-level PCP OS supervisor."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "central-quotients" / "local-response"))
from replay import run_case, work

TASKS = ["flow-products", "quadratic-error", "inverse-side"]
MUTATIONS = (
    (b"=(c-f)*a", b"=(c+f)*a", "AffineSign", "unsolved goals"),
    (b"= -(c-f)*k*c*f", b"= (c-f)*k*c*f", "CurvatureSign", "unsolved goals"),
    (b"= 6860 :=", b"= 6861 :=", "SideResidual", "is false"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "PhysicalScalar", 3, MUTATIONS)

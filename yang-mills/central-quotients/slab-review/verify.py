"""Generate finite controls in three measured PCP OS guests and check their Lean output."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "local-response"))
from replay import run_case, work

TASKS = ["project-center", "check-flat-seams", "interpolate-slices"]
MUTATIONS = (
    (b"(14096 : Nat)", b"(14095 : Nat)", "WrongProjection", "is false"),
    (b"= (19008 : Nat)", b"= (19007 : Nat)", "WrongSeamTotal", "is false"),
    (b"1-4*x*g", b"1-2*x*g", "DroppedEndpoint", "unsolved goals"),
    (b"*5 = 3*800", b"*4 = 3*800", "OneSidedError", "is false"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "SlabReview", 8, MUTATIONS)

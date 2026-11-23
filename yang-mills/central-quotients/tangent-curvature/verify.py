"""Replay the rooted-curvature hierarchy and independently check its output with Lean."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "local-response"))
from replay import run_case, work

TASKS = ["enumerate-cells", "reduce-incidence", "check-curvature-symbol"]
MUTATIONS = (
    (b"[16,32,24,8,1]", b"[16,32,23,8,1]", "OmittedFace", "is false"),
    (b"= (17,7)", b"= (18,7)", "SpuriousRank", "is false"),
    (b"/(a+b+c+d)=3", b"/(a+b+c+d)=4", "FourthPolarization", "unsolved goals"),
    (b"(Nat.choose 8 4)", b"(Nat.choose 8 3)", "LostFaceDensity", "is false"),
    (b"=4/p^2", b"=8/p^2", "DoubledDipole", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "TangentCurvature", 22, MUTATIONS)

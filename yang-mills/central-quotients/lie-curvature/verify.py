"""Run the three native PCP roles, compile the result and challenge its constants."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "local-response"))
from replay import run_case, work

TASKS = ["close-cube-paths", "contract-face-covariance", "count-color-channels"]
MUTATIONS = (
    (b"paths.length = 6", b"paths.length = 5", "MissingFace", "is false"),
    (b"= (216,0,24)", b"= (216,12,24)", "MixedCubeTerm", "is false"),
    (b"= (24,144)", b"= (24,48)", "UnnormalizedTrace", "is false"),
    (b"= (144,7776)", b"= (144,10368)", "UnprojectedFourthTensor", "is false"),
    (b"(0,80,360)", b"(0,144,360)", "ConfusedChargeChannels", "is false"),
    (b"3*(d*c*x^3)^2", b"4*(d*c*x^3)^2", "WrongSingletRatio", "unsolved goals"),
    (b"(7*d*c^2/64)", b"(5*d*c^2/64)", "MissingQuadraticSector", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "LieCurvature", 29, MUTATIONS)

"""Replay the recursive PCP proof and require rejection of six altered conclusions."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "local-response"))
from replay import run_case, work

TASKS = ["enumerate-walk", "retain-exit-mass", "derive-spectral-powers"]
MUTATIONS = (
    (b"= (16,8)", b"= (16,4)", "WrongLaziness", "is false"),
    (b"= (64,24)", b"= (72,16)", "UnstoppedEndpoints", "is false"),
    (b"= (12,16)", b"= (8,12)", "MissingDifference", "is false"),
    (b"1/(2*p^2*(2*m+1)", b"1/(4*p^2*(2*m+1)", "HalfDensity", "unsolved goals"),
    (b"moment-(-moment-mass)=0", b"moment-(-moment+mass)=0", "WrongReflectedBase", "linarith failed"),
    (b"stoppedTwo.length = 256", b"stoppedTwo.length = 192", "LostMass", "is false"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "MagneticSmearing", 21, MUTATIONS)

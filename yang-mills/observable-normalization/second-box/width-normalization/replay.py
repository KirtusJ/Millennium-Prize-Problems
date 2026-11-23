"""Run the finite checks using the repository's three-level PCP OS supervisor."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "central-quotients" / "local-response"))
from replay import run_case, work

TASKS = ["mode-inversion", "gaussian-moments", "angle-variance"]
MUTATIONS = (
    (b"= 170 :=", b"= 169 :=", "WrongModes", "is false"),
    (b"= -2*k*v :=", b"= -3*k*v :=", "WrongOscillator", "unsolved goals"),
    (b"=4*L^3 :=", b"=3*L^3 :=", "WrongCutoff", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "Width", 3, MUTATIONS)

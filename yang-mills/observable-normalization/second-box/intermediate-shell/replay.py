"""Run the finite checks using the repository's three-level PCP OS supervisor."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "central-quotients" / "local-response"))
from replay import run_case, work

TASKS = ["shell-cover", "transverse-oscillator", "cutoff-error"]
MUTATIONS = (
    (b"= 4095 :=", b"= 4094 :=", "WrongModes", "is false"),
    (b"=4*p^2*q^2 :=", b"=3*p^2*q^2 :=", "WrongOscillator", "unsolved goals"),
    (b"-2*(a*c+b*d) :=", b"-3*(a*c+b*d) :=", "WrongCutoff", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "Shell", 3, MUTATIONS)

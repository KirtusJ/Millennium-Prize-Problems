"""Replay the three-level native PCP momentum commission and audit its Lean output."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "local-response"))
from replay import run_case, work

TASKS = ["convolve-time-filter", "evaluate-cone-threshold", "bound-zero-mode-form"]
MUTATIONS = (
    (b"2*x-3*x^2", b"2*x-4*x^2", "WrongFilter", "unsolved goals"),
    (b"120)/4=1/480", b"120)/4=1/240", "WrongThreshold", "unsolved goals"),
    (b"a*b-x*y = (a-x)*b+x*(b-y)", b"a*b-x*y = (a-x)*b-x*(b-y)", "WrongHeatDeficit", "unsolved goals"),
    ("c ≤ -9674/1000000".encode(), "c ≤ -9774/1000000".encode(), "WrongProjectedSign", "linarith failed"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "FlowMomentum", 17, MUTATIONS)

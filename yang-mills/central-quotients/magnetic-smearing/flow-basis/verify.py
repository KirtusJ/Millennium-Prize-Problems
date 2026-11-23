"""Replay the measured three-generation PCP deployment and check the generated Lean."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "local-response"))
from replay import run_case, work

TASKS = ["bound-analytic-clock", "collect-fejer-weights", "check-rayleigh-form"]
MUTATIONS = (
    (b"(1458,2430)", b"(1458,2431)", "WrongPicardBound", "is false"),
    (b"+96*x^2-256", b"+95*x^2-256", "WrongFejerWeight", "unsolved goals"),
    (b")=5/16 := by norm_num", b")=3/16 := by norm_num", "WrongTailMoment", "unsolved goals"),
    ("δ*(2*E+δ)".encode(), "δ*(E+δ)".encode(), "DroppedWindowTerm", "unsolved goals"),
    (b"comp term < 0", b"comp term > 0", "ReversedRayleigh", "linarith failed"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "FlowBasis", 21, MUTATIONS)

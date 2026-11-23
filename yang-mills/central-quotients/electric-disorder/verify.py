"""Replay the PCP-generated central-shift proofs and the adverse controls."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "local-response"))
from replay import run_case, work

TASKS = ["locate-frustrated-faces", "measure-shift-energy", "count-band-vectors"]
MUTATIONS = (
    (b"contains p).length = 1", b"contains p).length = 4", "IdenticalCuts", "is false"),
    (b"shiftEnergy 0 = 8", b"shiftEnergy 0 = 2", "SingleFace", "is false"),
    (b"=(81,192)", b"=(27,64)", "CountSites", "is false"),
    (b"(93:\xe2\x84\x9a) <", b"(94:\xe2\x84\x9a) <", "InflatedRank", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "ElectricDisorder", 19, MUTATIONS)

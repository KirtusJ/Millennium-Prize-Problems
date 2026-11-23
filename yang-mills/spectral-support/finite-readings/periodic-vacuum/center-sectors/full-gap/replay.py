"""Replay the recursive PCP OS checks of the rational endpoints."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "central-quotients" / "local-response"))
from replay import run_case, work

TASKS = ["polynomial-residual", "angular-parity", "spectral-order"]
MUTATIONS = (
    (b"< 17/100000", b"< 16/100000", "BadEnvelope", "unsolved goals"),
    (b"=1+2*u*v*w", b"=1-2*u*v*w", "WrongHandedness", "unsolved goals"),
    (b"< 195/10000", b"< 194/10000", "FalseSeparation", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "FullGap", 4, MUTATIONS)

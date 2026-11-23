"""Replay the recursive PCP OS checks of the rational endpoints."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "central-quotients" / "local-response"))
from replay import run_case, work

TASKS = ["magnetic-tail", "center-multiplicity", "thermal-threshold"]
MUTATIONS = (
    (b"< 1/1000000 :=", b"< 1/10000000 :=", "WrongTail", "unsolved goals"),
    (b":= 3*(494/532)", b":= 1*(494/532)", "WrongMultiplicity", "unsolved goals"),
    (b"(2730:", b"(7300:", "WrongThreshold", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "CenterSectors", 4, MUTATIONS)

"""Generate the momentum certificates in three measured guests and check hosted Lean."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "local-response"))
from replay import run_case, work

TASKS = ["integrate-private-links", "bound-window-mass", "measure-spatial-support"]
MUTATIONS = (
    (b"privateEdgeCount 2 = 2", b"privateEdgeCount 2 = 4", "CollapsedLinks", "is false"),
    (b"(26,710,9)", b"(26,710,3)", "OpenEndpoint", "is false"),
    (b"(13,63)", b"(13,13)", "MissingSecondRing", "is false"),
)


if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "Momentum", 15, MUTATIONS)

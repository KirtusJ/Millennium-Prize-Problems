"""Run three linked native PCP OS workers and check their emitted Lean declarations."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["sort-spatial-paths", "distinguish-momentum-aliases", "test-two-leg-cone"]
MUTATIONS = (
    (b'= (540,972) := by decide', b'= (541,972) := by decide', 'WrongArea', 'is false'),
    (b'= (24,0) := by decide', b'= (0,0) := by decide', 'MissedAliases', 'is false'),
    (b'= (14,7332) := by decide', b'= (14,7331) := by decide', 'WrongCone', 'is false'),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "JointMomentum", 6, MUTATIONS)

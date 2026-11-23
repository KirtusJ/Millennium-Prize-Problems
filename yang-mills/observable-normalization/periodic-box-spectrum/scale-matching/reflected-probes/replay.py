"""Run the finite checks using the repository's three-level PCP OS supervisor."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "central-quotients" / "local-response"))
from replay import run_case, work

TASKS = ["reflected-gram", "independent-determinant", "pooled-floor"]
MUTATIONS = (
    (b"=(x*v-y*u)^2", b"=(x*v+y*u)^2", "GramSign", "unsolved goals"),
    (b"+d*c-2*b*e", b"+d*c+2*b*e", "CrossSign", "unsolved goals"),
    (b"29865 * 175", b"29865 * 176", "OverstatedFloor", "is false"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "ReflectedProbes", 3, MUTATIONS)

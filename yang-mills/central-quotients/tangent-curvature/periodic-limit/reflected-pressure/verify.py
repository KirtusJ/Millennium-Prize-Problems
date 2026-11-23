"""Run three linked native PCP OS workers and check their emitted Lean declarations."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["tile-incidence", "folded-holonomy", "seam-character"]
MUTATIONS = (
    (b'= 33888 :=', b'= 5 :=', 'WrongFaceCount', 'is false'),
    (b'= 7776 :=', b'= 4095 :=', 'WrongSquareCount', 'is false'),
    (b'=12*l^2-12*l+4', b'=12*l^2+12*l+4', 'WrongSeamDensity', 'unsolved goals'),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "ReflectedPressure", 4, MUTATIONS)

"""Check the finite supporting lemmas in three native PCP OS generations."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["bound-fiber-width", "expand-clock-filter", "compute-fifth-harmonic"]
MUTATIONS = (
    (b"48^2*81", b"40^2*81", "SmallFiberConstant", "is false"),
    (b" = 81 := by decide", b" = 1 := by decide", "IgnoreCancellation", "is false"),
    (b" = 2560 := by decide", b" = 128 := by decide", "WrongHarmonic", "is false"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "MovingThreshold", 10, MUTATIONS)

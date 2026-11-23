"""Replay the native forest, reflection and spectral checks."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "local-response"))
from replay import run_case, work

TASKS = ["count-temporal-forest","reflect-unit-faces","check-spectral-edge"]
MUTATIONS = (
    (b'= (832, 576) := by decide', b'= (768, 576) := by decide', 'DroppedSeam', 'is false'),
    (b'= (144, 4) := by decide', b'= (144, 2) := by decide', 'MissedFace', 'is false'),
    (b'^9 < 3^9 := by decide', b'^9 > 3^9 := by decide', 'WrongCrossing', 'is false'),
    (b'z^n < b*q^n := by', b'z^n > b*q^n := by', 'ReversedRate', 'type mismatch'),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int,sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "PeriodicCriticality", 10, MUTATIONS)

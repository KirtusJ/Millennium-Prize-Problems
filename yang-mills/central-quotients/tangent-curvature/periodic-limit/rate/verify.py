"""Replay the cube, walk and transfer checks in three measured guests."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["trace-cube-swaps", "sum-lazy-differences", "compare-double-lag"]
MUTATIONS = (
    (b'= (63, 3) := by decide', b'= (62, 3) := by decide', 'MissingFace', 'is false'),
    (b'= 140 := by decide', b'= 70 := by decide', 'HalfVariation', 'is false'),
    (b'= (65536 :', b'= (65535 :', 'WrongLag', 'is false'),
    ('q*A ≤ B := by'.encode(), 'q*A ≥ B := by'.encode(), 'ReversedRatio', 'but is expected to have type'),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int,sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "WilsonRate", 9, MUTATIONS)

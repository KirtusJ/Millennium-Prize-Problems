"""Replay the three native spatial block checks and their Lean read-back."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["convolve-block", "count-spatial-paths", "bound-band-weight"]
MUTATIONS = (
    (b'= (264,24576) := by decide', b'= (263,24576) := by decide', 'WrongBlock', 'is false'),
    (b'= 900 := by decide', b'= 901 := by decide', 'WrongVisits', 'is false'),
    (b'= 8 := by decide', b'= 7 := by decide', 'WrongBand', 'is false'),
    ('m ≤ -Real.log c/n := by'.encode(), 'm ≥ -Real.log c/n := by'.encode(),
     'ReversedGap', 'linarith failed'),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int,sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "WilsonBlock", 8, MUTATIONS)

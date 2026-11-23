"""Generate and verify the clustering certificates on the pinned PCP/Lean stack."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "local-response"))
from replay import run_case, work

TASKS = ["extract-circle-coefficient", "split-spectrum", "balance-physical-clock"]
MUTATIONS = (
    (b"(0,10240)", b"(0,1024)", "WrongCoefficient", "is false"),
    (b"(16,11)", b"(23,4)", "LoseEndpoint", "is false"),
    (b" = 292 := by decide", b" = 484 := by decide", "LinearBalance", "is false"),
    (b"7/12 \xe2\x89\xa4 w := by", b"2/3 \xe2\x89\xa4 w := by", "InflatedMass", "linarith failed"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "Clustering", 16, MUTATIONS)

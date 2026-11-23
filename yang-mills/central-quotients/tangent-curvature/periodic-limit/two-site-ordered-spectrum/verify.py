"""Run the native scale, transverse-probe and center checks."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "local-response"))
from replay import run_case, work

TASKS = ["matching-scales", "soft-probes", "center-orbits"]
MUTATIONS = (
    (b"= 40 :=", b"= 41 :=", "WrongScale", "is false"),
    (b"= 343 :=", b"= 57 :=", "WrongCount", "is false"),
    (b"2*(a^2+b^2+c^2)", b"3*(a^2+b^2+c^2)", "WrongProbe", "unsolved goals"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "TwoSiteOrdered", 3, MUTATIONS)

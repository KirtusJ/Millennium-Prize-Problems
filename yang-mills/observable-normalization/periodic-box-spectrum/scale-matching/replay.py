"""Run the finite checks using the repository's three-level PCP OS supervisor."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "central-quotients" / "local-response"))
from replay import run_case, work

TASKS = ["flow-brackets", "scalar-subtraction", "tensor-subtraction"]
MUTATIONS = (
    (b"= 4 :=", b"= 3 :=", "LostBracket", "is false"),
    (b"= 2269639 :=", b"= 2269640 :=", "ScalarShift", "is false"),
    (b"= 1897780 :=", b"= 1897781 :=", "TensorShift", "is false"),
)

if __name__ == "__main__":
    if sys.argv[1:2] == ["worker"]:
        work(Path(sys.argv[2]), list(map(int, sys.argv[3:])), tasks=TASKS, entry=__file__)
    else:
        run_case(HERE, __file__, TASKS, "ScaleMatching", 3, MUTATIONS)

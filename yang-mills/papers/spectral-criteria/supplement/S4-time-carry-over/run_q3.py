"""c2-grow Q2 driver. usage: python3 run_q3.py <tag> <weight file> <base seed> <nconf>
Design fixed before the run: 16 chains i = 0..15, seed = base + 7919 i, hot = i % 2, beta 3.276133577, side 6, T 12,
1000 discarded cycles (prior q2), nconf configurations 1 cycle apart (prior q2: tau_int <= 0.86 cycles). 2 chains at a time.
Outputs results_q2/<tag>/c<i>.txt (create_new in q3) and cmds.list (mode x). Sampler predicates Q3-P1..P4 asserted in build/q3."""
import subprocess, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT = Path(__file__).resolve().parent
def one(a):
    tag, wf, base, nconf, i = a
    cmd = [str(ROOT / "build/q3"), "3.276133577", str(base + 7919 * i), str(i % 2), "1000", str(nconf), "1", "6", "12", wf, str(ROOT / "results_q2" / tag / f"c{i}")]
    r = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return " ".join(cmd) + "\n# " + r.stderr.replace("\n", " | ")
tag, wf, base, nconf = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
(ROOT / "results_q2" / tag).mkdir(parents=True, exist_ok=False)
with ThreadPoolExecutor(2) as ex: cmds = list(ex.map(one, [(tag, wf, base, nconf, i) for i in range(16)]))
with open(ROOT / "results_q2" / tag / "cmds.list", "x") as fh: fh.write("\n".join(cmds) + "\n")
print(tag, "done")

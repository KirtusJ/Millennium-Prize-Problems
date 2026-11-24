"""d2-time production driver for build/z1mx5 'time'. usage: python3 prodt.py <tag> <skeleton> <weights file> <base seed>
Design (fixed before the first production run, 01:33):
  32 streams i = 0..31, seed = base + 7919 i, hot = i % 2, 576 discarded conditional heat-bath sweeps, 1152 measurements
  6 sweeps apart, side 6, T 12, beta 3.276133577 (prior record). TRAIN = streams 0..15, HELD = 16..31 (8 hot + 8 cold each).
  2 streams concurrently (brief: at most 2 cores). Fresh seeds (base 21100001 at -I, 21300001 clear), i.e. independent of
  the prior runs on which the weight vectors were fitted (prior G-d0 seeds 11100001; clear weights refitted by fitw.py
  from a z1mx5 'fixed' reproduction of prior G-clear0, seeds 11300001).
  Weights file rows: w_L4, w_L1 (embedded in 308), f4 (1/4 on B.xy000.g00..g11).
Outputs results/<tag>/s<i>.{meta.txt, series.csv, mom.txt} (create_new) + commands.txt (mode 'x').
INTERPRETATION RULE (from the brief, fixed here before any production run):
  For Y = Y^loc and Y = Y^tr separately, with R2 = R^2_held(1) of the regression of m = w_L4.X(0) on all 308 Y_k(1)
  (+ intercept; fitted on TRAIN, evaluated on HELD; error = delete-one-held-stream jackknife se):
   'the slow local mode persists in physical time' := R2(-I) - R2(clear) > 3 sqrt(se(-I)^2 + se(clear)^2)  AND  R2(-I) > 0.1;
   'it does not' := R2(-I) < 0.02 with se(-I) < 0.01;  otherwise 'not resolved'.
  The verdict is stated per definition (loc, tr); if they differ both are reported and the overall verdict is 'not resolved'.
"""
import subprocess, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT = Path(__file__).resolve().parent
EXE = ROOT / "build" / "z1mx5"
def one(args):
    tag, skel, wf, base, i = args
    cmd = [str(EXE), "time", "3.276133577", str(base + 7919 * i), str(i % 2), "576", "1152", "6", "6", "12", str(skel), str(wf), "0",
           str(ROOT / "results" / tag / f"s{i}")]
    subprocess.run(cmd, check=True); return " ".join(cmd)
tag, skel, wf, base = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
(ROOT / "results" / tag).mkdir(parents=True, exist_ok=False)
with ThreadPoolExecutor(2) as ex: cmds = list(ex.map(one, [(tag, skel, wf, base, i) for i in range(32)]))
with open(ROOT / "results" / tag / "commands.txt", "x") as fh: fh.write("\n".join(cmds) + "\n")
print(tag, "done")

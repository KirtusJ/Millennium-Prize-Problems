"""Q1 driver (a2-mixb). usage: python3 run_q1.py <tag> <beta> <skeleton> <base seed> <burn>
Design (fixed before the first run): 8 streams i=0..7, seed = base + 7919 i, hot = i % 2, <burn> discarded
conditional heat-bath sweeps (beta 6: 1152; beta 12: 2304; i.e. 2x and 4x the prior 576, because larger beta
thermalises more slowly), 576 measurements 6 sweeps apart, side 6, period 12. Two streams concurrently.
Outputs results_q1/<tag>/s<i>.{csv,colours.csv,meta.txt}; never overwritten (create_new / 'x').
Predicates evaluated in reduce_q1.py (fixed here, before the first run):
 T1 streams >= 8 (half hot, half cold).
 T2 hot/cold: cold and hot strata of J1/Var1 and J4/Var4 differ by <= 2 sigma_d, sigma_d = 2 * pooled jackknife
    error (prior record's rule; 2 sigma ~ 95% band).
 T2p hot/cold mean plaquette and T2s hot/cold mean spread: |mean_cold - mean_hot| <= 2 sigma_d,
    sigma_d = sqrt(s_c^2/4 + s_h^2/4) from the per-stream sample sd (ddof 1) in each stratum.
 T3 sampler asserts (exit 0).  T5 mean pair proposals per draw < 1000 (cost guard only).
 Rule if T2/T2p/T2s fails: one rerun with doubled burn-in and base+50000 (tag suffix -r); if it fails again the run
 is reported with NO number. Since 14 runs x 4 checks at 2 sigma give ~2-3 chance failures, a failure is first
 attributed to chance only if the rerun passes.
"""
import subprocess, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT = Path(__file__).resolve().parent
EXE = ROOT / "build" / "a2m"
N, T, SAMPLES, SPACING, STREAMS = "6", "12", "576", "6", 8

def one(a):
    tag, beta, skel, base, burn, i = a
    pre = ROOT / "results_q1" / tag / f"s{i}"
    cmd = [str(EXE), "fixed", beta, str(base + 7919 * i), str(i % 2), burn, SAMPLES, SPACING, N, T, str(skel), str(pre)]
    subprocess.run(cmd, check=True)
    return " ".join(cmd)

tag, beta, skel, base, burn = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), sys.argv[5]
(ROOT / "results_q1" / tag).mkdir(parents=True, exist_ok=False)
with ThreadPoolExecutor(2) as ex:
    cmds = list(ex.map(one, [(tag, beta, skel, base, burn, i) for i in range(STREAMS)]))
with open(ROOT / "results_q1" / tag / "commands.txt", "x") as fh:
    fh.write("\n".join(cmds) + "\n")
print(tag, "done")

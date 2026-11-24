"""Q2 driver (a2-mixb). usage: python3 run_q2.py <tag> <base seed>
Design (fixed before the first production run): beta = 3.276133577, side 6, period 12, unconditioned Wilson measure,
16 independent chains i = 0..15, seed = base + 7919 i, hot = i % 2 (8 hot, 8 cold), 1000 discarded cycles
(cycle = heat-bath sweep + over-relaxation sweep), then 30000 configurations 1 cycle apart. Two chains concurrently.
Outputs results_q2/<tag>/c<i>.txt (create_new). Program: build/q2 (asserts Q2-P1 gauge invariance <= 1e-10, Q2-P2).
Predicates evaluated in reduce_q2.py (fixed here):
 Q2-T1 chains >= 8, half hot half cold.
 Q2-T2 thermalisation: cold vs hot strata of (a) mean plaquette, (b) ungated C(1)/C(0), (c) fraction in gate 1.2
       differ by <= 2 sigma_d, sigma_d = sqrt(s_c^2/n_c + s_h^2/n_h) from per-chain values (ddof 1). 2 sigma ~ 95% band.
 Q2-T3 tau_int (Sokal window, c = 6) per chain of the per-configuration series plaquette, S2_all[0], S2_all[1],
       S2_gate1.2[1], count_gate1.2: max over chains and series of 2 tau_int <= nconf/100 (>= 100 effective
       samples per chain). Errors come from the delete-one-chain jackknife (chains independent), so tau_int only
       qualifies chain length.
 Q2-T4 burn-in: per chain, plaquette mean of the first and second half of the measured configurations: the
       across-chain mean difference (first - second) within 2 standard errors (sd/sqrt(16)).
Significance of a difference between gates: |z| > 2 with z = jackknife(diff)/jackknife error (paired by chain).
"""
import subprocess, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT = Path(__file__).resolve().parent
EXE = ROOT / "build" / "q2"
BETA, BURN, NCONF, GAP, N, T, CHAINS = "3.276133577", "1000", "30000", "1", "6", "12", 16

def one(a):
    tag, base, i = a
    cmd = [str(EXE), BETA, str(base + 7919 * i), str(i % 2), BURN, NCONF, GAP, N, T, str(ROOT / "results_q2" / tag / f"c{i}")]
    subprocess.run(cmd, check=True)
    return " ".join(cmd)

tag, base = sys.argv[1], int(sys.argv[2])
(ROOT / "results_q2" / tag).mkdir(parents=True, exist_ok=False)
with ThreadPoolExecutor(2) as ex:
    cmds = list(ex.map(one, [(tag, base, i) for i in range(CHAINS)]))
with open(ROOT / "results_q2" / tag / "commands.txt", "x") as fh:
    fh.write("\n".join(cmds) + "\n")
print(tag, "done")

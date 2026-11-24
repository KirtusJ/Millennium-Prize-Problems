"""LARGE production driver z1-mix6 (24 streams x 1152 measurements; otherwise identical to run.py): side 6, T=12, beta=3.276133577, own sampler build/z1m6.

usage: python3 run.py <tag> <skeleton file> <base seed>
Design (fixed before the first run): 8 streams i=0..7, seed = base + 7919 i, hot flag = i % 2
(even = cold start of free links, odd = hot), 576 discarded conditional heat-bath sweeps,
576 measurements 6 conditional sweeps apart. Two streams run concurrently (2 cores, brief allows 2).
Outputs in results/<tag>/s<i>.{csv,colours.csv,meta.txt}; never overwritten (create_new / mode 'x').
Predicates evaluated in reduce.py (fixed here):
 T1 number of streams >= 4 (here 8).
 T2 thermalisation: cold-stratum and hot-stratum four-face ratio J4/Var4 differ by at most 2 sigma_d,
    sigma_d = 2 * (delete-one-stream error of the pooled ratio) (each stratum has half the streams,
    variance ~ 2 e^2 each). Same for the one-face ratio. 2 sigma: conventional ~95% band.
 T3 P2/P3 asserts inside the sampler (exit code 0 required by pcp check --expect-exit 0).
"""
import subprocess, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).resolve().parent
EXE = ROOT / "build" / "z1m6"
BETA, N, T = "3.276133577", "6", "12"
BURN, SAMPLES, SPACING, STREAMS = "576", "1152", "6", 24


def one(args):
    tag, skel, base, i = args
    pre = ROOT / "results" / tag / f"s{i}"
    cmd = [str(EXE), "fixed", BETA, str(base + 7919 * i), str(i % 2), BURN, SAMPLES, SPACING, N, T, str(skel), str(pre)]
    subprocess.run(cmd, check=True)
    return " ".join(cmd)


def main():
    tag, skel, base = sys.argv[1], sys.argv[2], int(sys.argv[3])
    (ROOT / "results" / tag).mkdir(parents=True, exist_ok=False)
    with ThreadPoolExecutor(2) as ex:
        cmds = list(ex.map(one, [(tag, skel, base, i) for i in range(STREAMS)]))
    with open(ROOT / "results" / tag / "commands.txt", "x") as fh:
        fh.write("\n".join(cmds) + "\n")
    print(tag, "done", len(cmds), "streams")


if __name__ == "__main__":
    main()

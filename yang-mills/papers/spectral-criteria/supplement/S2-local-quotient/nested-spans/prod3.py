"""b2-matrix production driver for the EXTRA run with build/z1mx3 (35 marks: z1mx2 list + 4 yz plaquettes of the face (2,0,4)). Otherwise identical to prod.py. usage: python3 prod.py <tag> <skeleton file> <base seed>
Design (fixed before the first run): 32 streams i=0..31, seed = base + 7919 i, hot = i % 2,
576 discarded conditional heat-bath sweeps, 1152 measurements 6 sweeps apart, side 6, T 12,
beta 3.276133577 (fixed.md, prior record). TRAIN = streams 0..15, HELD-OUT = streams 16..31
(each half: 8 hot, 8 cold). 2 streams concurrently (brief: at most 2 cores).
Outputs results/<tag>/s<i>.{csv,colours.csv,meta.txt,X.csv,Dc.txt} via build/z1mx (create_new; never overwritten).
Predicates: sampler asserts P1-P3, P5 (exit 0 required); analysis predicates in analyze.py.
"""
import subprocess, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT = Path(__file__).resolve().parent
EXE = ROOT / "build" / "z1mx3"
BETA, N, T = "3.276133577", "6", "12"
BURN, SAMPLES, SPACING, STREAMS = "576", "1152", "6", 32

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

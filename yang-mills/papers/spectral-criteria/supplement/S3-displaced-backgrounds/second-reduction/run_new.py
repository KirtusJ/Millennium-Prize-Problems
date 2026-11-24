"""Production driver e2-repair new run (design fixed in REGISTRATION.md, sha256 in REGISTRATION.sha256).
usage: python3 run_new.py <tag> <skeleton> <base seed>
32 streams i=0..31, seed = base + 7919 i, hot flag = i % 2 (numerical ID parity), burn 1152, 1152 measurements 6 sweeps apart,
side 6, T 12, beta 3.276133577. 2 concurrent streams. Output results/<tag>/s<i>.* created new by the sampler (create_new);
directory must not exist (exist_ok=False); commands.txt mode 'x'.
Predicate here: R1 every sampler call exits 0 (check=True -> nonzero exit of this driver otherwise).
"""
import subprocess, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT = Path(__file__).resolve().parent
EXE = ROOT / "build" / "z1m6"
BETA, N, T, BURN, SAMPLES, SPACING, STREAMS = "3.276133577", "6", "12", "1152", "1152", "6", 32

def one(args):
    tag, skel, base, i = args
    cmd = [str(EXE), "fixed", BETA, str(base + 7919 * i), str(i % 2), BURN, SAMPLES, SPACING, N, T, str(skel), str(ROOT / "results" / tag / f"s{i}")]
    subprocess.run(cmd, check=True)
    return " ".join(cmd)

def main():
    tag, skel, base = sys.argv[1], Path(sys.argv[2]).resolve(), int(sys.argv[3])
    (ROOT / "results" / tag).mkdir(parents=True, exist_ok=False)
    with ThreadPoolExecutor(2) as ex:
        cmds = list(ex.map(one, [(tag, skel, base, i) for i in range(STREAMS)]))
    with open(ROOT / "results" / tag / "commands.txt", "x") as fh:
        fh.write("\n".join(cmds) + "\n")
    print(tag, "done", len(cmds), "streams")

if __name__ == "__main__":
    main()

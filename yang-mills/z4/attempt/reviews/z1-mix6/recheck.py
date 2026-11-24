"""Recorded re-execution of steps first run outside the register.
 R1 (P4 again): build/z1m6 at skeleton d0 with G4 seeds 1700451 (cold) and 1708370 (hot) -> results/p4b; first five columns
    byte-identical to results/ctl_g4seeds/minus6-s{0,1}.csv.
 R2 skeleton files: regenerating W_delta,B quaternions reproduces the data lines of skeletons/*.txt exactly.
 R3 every results/<tag>/summary.json pooled ratio1/ratio4/var4/J4 equals a fresh in-memory recomputation from the raw CSVs (rel. 1e-12).
Exit 0 iff all hold."""
import subprocess, math, json, sys
import numpy as np
from pathlib import Path
ok = True
Path("results/p4b").mkdir(exist_ok=False)
for i, (seed, hot) in enumerate(((1700451, 0), (1708370, 1))):
    subprocess.run(["build/z1m6", "fixed", "3.276133577", str(seed), str(hot), "288", "144", "6", "6", "12", "skeletons/d0.txt", f"results/p4b/s{i}"], check=True)
    mine = ["single,average,spread,j_single,j_average"] + [",".join(l.split(",")[:5]) for l in Path(f"results/p4b/s{i}.csv").read_text().splitlines()[1:]]
    same = ("\n".join(mine) + "\n").encode() == Path(f"results/ctl_g4seeds/minus6-s{i}.csv").read_bytes()
    print("R1 stream", i, "byte-identical", same); ok &= same
BETA = 3.276133577
for name, d in (("d0", 0.0), ("d0.5", 0.5 / BETA), ("d1", 1 / BETA), ("d2", 2 / BETA), ("d4", 4 / BETA)):
    W = (-math.cos(d), 0.0, 0.0, math.sin(d))
    line = "2 1 " + " ".join(f"{v:.17e}" for v in W)
    good = line in Path(f"skeletons/{name}.txt").read_text().splitlines()
    print("R2", name, good); ok &= good
for tag in ["d0", "d0.5", "d1", "d2", "L-d0", "L-d0.5", "L-d1", "L-d2", "L-d4", "clear0", "clear2", "clear4"]:
    s = json.load(open(f"results/{tag}/summary.json"))
    rows = [np.loadtxt(f"results/{tag}/s{i}.csv", skiprows=1, delimiter=",") for i in range(s["streams"])]
    D = np.concatenate(rows)
    fresh = {"ratio1": D[:, 3].mean() / D[:, 0].var(), "ratio4": D[:, 4].mean() / D[:, 1].var(), "var4": D[:, 1].var(), "J4": D[:, 4].mean()}
    good = all(abs(fresh[k] - s["pooled"][k][0]) <= 1e-12 * abs(fresh[k]) for k in fresh)
    print("R3", tag, good); ok &= good
sys.exit(0 if ok else 1)

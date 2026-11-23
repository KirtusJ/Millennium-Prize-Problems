"""Binning analysis of per-sweep plaquette files. Bin size 20 (fixed in advance).
Checks P3 (cold/hot agree within 3 sigma) and P4 (P(8.0) > P(2.3)).
Also prints errors at other bin sizes for information only.
Usage: python analyze.py OUTFILE   (OUTFILE must not exist). Exit 0 iff P3 and P4 hold."""
import math, os, sys

BIN = 20
R = "results"


def load(fn):
    return [float(l) for l in open(fn) if not l.startswith("#")]


def binned(v, b):
    nb = len(v) // b
    m = [sum(v[i * b:(i + 1) * b]) / b for i in range(nb)]
    mu = sum(m) / nb
    var = sum((x - mu) ** 2 for x in m) / (nb - 1)
    return sum(v[:nb * b]) / (nb * b), math.sqrt(var / nb), nb


out = sys.argv[1]
if os.path.exists(out):
    print("refusing to overwrite", out); sys.exit(3)
lines = []
res = {}
for beta in ("2.3", "8.0"):
    for st in ("cold", "hot"):
        v = load(f"{R}/b{beta}_{st}.txt")
        m, e, nb = binned(v, BIN)
        res[(beta, st)] = (m, e)
        extra = " ".join(f"b{b}:{binned(v, b)[1]:.2e}" for b in (1, 5, 10, 20, 50, 100, 250))
        lines.append(f"beta={beta} {st}: N={len(v)} P={m:.6f} +- {e:.6f} (bin {BIN}, {nb} bins) | {extra}")
ok3 = True
for beta in ("2.3", "8.0"):
    (mc, ec), (mh, eh) = res[(beta, "cold")], res[(beta, "hot")]
    s = math.sqrt(ec ** 2 + eh ** 2)
    ok = abs(mc - mh) < 3 * s
    ok3 &= ok
    # combined (inverse-variance weighted) value
    w1, w2 = 1 / ec ** 2, 1 / eh ** 2
    comb = (mc * w1 + mh * w2) / (w1 + w2); ce = 1 / math.sqrt(w1 + w2)
    lines.append(f"beta={beta}: |cold-hot|={abs(mc-mh):.2e}, {abs(mc-mh)/s:.2f} sigma -> P3 {ok}; combined P={comb:.6f} +- {ce:.6f}")
ok4 = res[("8.0", "cold")][0] > res[("2.3", "cold")][0] and res[("8.0", "hot")][0] > res[("2.3", "hot")][0]
lines.append(f"P4 P(8.0)>P(2.3): {ok4}")
txt = "\n".join(lines)
print(txt)
with open(out, "x") as f:
    f.write(txt + "\n")
sys.exit(0 if ok3 and ok4 else 2)

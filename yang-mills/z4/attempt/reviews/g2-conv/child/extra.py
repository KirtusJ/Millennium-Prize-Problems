"""Extra (measured only, no predicate): beta=16 and 64 c1=1 trend with N. Uses lam.build, grid 2N+20."""
import json, lam
out = {}
for beta, Ns in [(16, [16, 40, 48, 56]), (64, [32, 56])]:
    for N in Ns:
        H, D, tot = lam.build(beta, N, 2*N+20, True, 0)
        L1 = float(lam.lam(H, D, 1)); L0 = float(lam.lam(H, D, 0))
        out[f"{beta}_{N}"] = dict(dim=tot, L0=L0, L1=L1, s0=beta**(1/3)*L0, s1=beta**(1/3)*L1); print(beta, N, out[f"{beta}_{N}"], flush=True)
with open("result_extra.json", "x") as fh: json.dump(out, fh, indent=1)

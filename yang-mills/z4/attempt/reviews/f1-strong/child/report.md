# T69 report (item 4: c_max for SU(2) Wilson LGT on (Z/2)^4)

**Control (control.txt):** single plaquette, Q=-1, Ric=1: eigenvalues of Ric+Hess V are `1-2*beta` (x3) and `1` (x9). Checked by finite differences of V at beta=1 and 2.5, error <1e-6 (results/p1.txt).

## Results
- **c_max found = 8** (c_H,max found = 8). Both are attained at the pi-flux configuration (c_full = c_H = 8.000000000 by eigh; a perturbed pi-flux ascended to 7.9999997, no higher). Full spectrum there (from the grandchild's FD run): -8 (x9), -6 (x36), -4 (x54), -2 (x36), 0 (x57). The horizontal spectrum is the same except 0 has multiplicity 12 (gauge rank 45, horizontal dim 147).
- **Random starts: 24 seeded starts** (rng default_rng(1000+k), k=0..23, Haar-random U), 30 ascent iterations each. They reached only c = 6.3 to 7.29, best 7.286 (seed 16). **The ascents were not converged** (all used all 30 iterations, still rising), so this is a lower-bound search, not a proof of c_max. 8 is the best value found; I have not shown it is the maximum.
- Start "one link = -1" (link 0): c = 4.6756, and the ascent did not move. Probable cause is a degenerate lowest eigenvalue, where the Hellmann-Feynman gradient is unreliable. This is my method's limit, not a result about the true maximum there. The identity has c = 0.
- **The 12 bound was never exceeded.** All 744 ascent iterates (248 per chunk) plus 27 final or special configs had c <= 12; the maximum seen was 8.
- The claim that pi-flux has c = 8 exactly, also horizontally, holds numerically to 1e-9 and is independently confirmed by finite differences (7.99999866).
- c_H at the random-start ends was at most 0.01 below c_full (e.g. 7.2866 vs 7.2788 at c2).

## Predicates
Met:
- control C1.
- F1b (Hessian vs FD < 1e-5; errors ~1e-8, also at pi-flux).
- F3 (qform == t^T H t to 1e-12).
- H1 (pi-flux c = c_H = 8 within 1e-9).
- S1/H2: 248/248 iterates in each chunk, and 27/27 final configs, satisfy c <= 12 (for-all claim tested per case, not proven).
Failed (kept in results/):
- F1/F2 in p1 (FD tolerance 1e-5 with |t|~14): **my own expectation** (step too large). results/p1.txt.
- F2b (h^2 scaling ratio, p1b): **my own expectation**. The errors are at the roundoff floor ~1e-8, so no h^2 trend shows. This is not a Hessian defect. results/p1b.txt.
- The first trial of p2 (60 iterations, one start) was too slow (73 s). I optimized it and cut it to 30 iterations (budget).
Measured only: per-start final c (results/p2_{a,b,c}.txt); the H3 and H4 ascents.
Caveat: tolerances in the 1e-5 to 1e-9 range are from FD truncation or eigh accuracy, as stated in each docstring. The search is budget-limited (about 6 minutes), so the maximum is not certified.

## Grandchild
Question: independently recompute c at pi-flux by pure finite differences, with a known-answer control first. Task id **T70** (admitted under T69, released). Control passed (-2 x3, 0 x9). Result: c_full = c_H = 7.99999866 with the multiplicities above. I reread results.txt and reran its program (copy in results/gc_rerun): identical numbers. Its prose said "24 plaquettes", which is a slip: the code asserts all plaquettes in its list `pl` have Q = -1 (not re-counted by me).

## PCP OS
See verify lines in the final section below.

## Rerun
```
cd /home/user/z4-workers/f1-strong/child
python3 p1_control_fd.py   # (result files open mode x; move results/ aside first)
python3 p1b_fd_unit.py
python3 p2_search.py 0 8 a; python3 p2_search.py 8 16 b; python3 p2_search.py 16 24 c
python3 p3_special.py
cd grandchild && python3 fd_piflux.py
```

### PCP OS verify (last lines)
- Python `verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- Rust `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
- Register note: p1_control_fd and p1b_fd_unit were recorded with exit 1 (expected 0), the failed predicates above.

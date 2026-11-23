# T130 report: free lattice Maxwell correlator G(n)

Control: control.txt = 0.333333 (written first).

## Table (g130.py; midpoint grids N=48..384 on the reduced 3-torus, Richardson h^4)
| n | G(n) | pi^2 n^4 G | n^2 (pi^2 n^4 G - 1) |
|---|------|-----------|------|
| 0 | 0.5000000000 | | |
| 1 | 6.8874745841e-02 | 0.679766 | -0.3202 |
| 2 | 1.1152717660e-02 | 1.761167 | 3.0447 |
| 3 | 2.2622376448e-03 | 1.808519 | 7.2767 |
| 4 | 6.0539626230e-04 | 1.529606 | 8.4737 |
| 5 | 2.1313129258e-04 | 1.314701 | 7.8675 |
| 6 | 9.3343333444e-05 | 1.193955 | 6.9824 |
| 7 | 4.7648158258e-05 | 1.129115 | 6.3266 |
| 8 | 2.7023207362e-05 | 1.092437 | 5.9160 |

Accuracy: Richardson levels (48/96, 96/192, 192/384) agree to <=6e-14 absolute; I claim 1e-12 (the spread is the only source; no analytic error bound).

## Verdicts
| item | verdict | evidence |
|---|---|---|
| (a) G(0)=1/2 | STANDS (numerically) | 0.500000000000 to ~1e-12; not a proof |
| (b) G(n)>0, n=1..8 | STANDS | all G(n) >= 2.7e-5, error ~1e-12 |
| (c) pi^2 n^4 G -> 1 | STANDS within range checked, trend only | 1.76,1.81,1.53,1.31,1.19,1.13,1.09 for n=2..8, decreasing toward 1 from n=3 |
| (c) n^2(...) bounded n=2..8 | STANDS | max 8.47 (n=4), then decreasing 5.9 at n=8 |
| (c) exact O(n^-6) asymptotics, n->infinity | NOT CHECKED | n<=8 only; bounded values over 2..8 do not prove it |

## Hypotheses used
H1 (the hint, k0 integral exact): used, and checked independently against brute-force 4D midpoint grid (N=24 per k-interval, 48 pts/axis) for n=0,1,2: agree to 8 printed digits (this check is limited by the coarse 4D grid, not by 1e-12).
H2: cubic symmetry replaces (a1+a2) by (2/3)s (exact by symmetry of k1,k2,k3).
H3: grid error ~h^4 (non-smooth point at k=0); supported by the observed convergence, not proven.

## Failed predicates
None failed. Predicates P_a (tol 1e-6), P_b, P_c2 (<10), P_h (1e-3) were fixed in the g130.py docstring before the first run; all passed. The tolerances 1e-6, 1e-3, 10 were my own choices, not derived. Caveat: P_c1 ("decreasing toward 1") is not mechanically tested in code; n=2 (1.76) -> n=3 (1.81) is a rise, so the sequence is not monotone from n=2; I judged it by reading the table.

## Delegation
Question: independent G(1) by a heat-kernel (Schwinger) 1D Bessel integral. Task id T131 (admitted, released). Result: 0.0688747458405 (err est 1e-12); mine 0.068874745841: agree to ~1e-12. Control 1.000000 passed. I reread its notes and reran its script in rerun/ (copy; PREDICATES PASS, same numbers). Its error estimate is self-consistency spread, not a bound.

## Not checked
No rigorous error bound; no n>8; no analytic proof of (a); no analytic derivation of the n^-4 coefficient or the O(n^-6) next term; sign behaviour for n>8.

## Process notes
g130_result.txt was rerun under pcp check after I moved the first copy aside (/tmp/claude-0/g130_result_keep.txt, identical by diff), because result files open with mode "x". The grandchild rerun was run directly, not under pcp check (a shell -c wrapper was blocked by the harness).

## Rerun
cd /home/user/z4-workers/m1-wild/child; rm/move g130_result.txt first, then: python3 g130.py (about 3 s)
Grandchild: copy grandchild/g1_schwinger.py and control.txt to a fresh dir and run python3 g1_schwinger.py.
PCP: P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P verify --ws pcp
 - Python verify last line: "A pass is a fact about these bytes..." was preceded by "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
 - Rust verify last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
Register holds one check (g130, exit 0); the grandchild rerun is not in it.

Counts: met 5 (a, b, c-bounded, c-trend, delegation agreement), failed 0, measured only 1 (asymptotic limit n->inf).

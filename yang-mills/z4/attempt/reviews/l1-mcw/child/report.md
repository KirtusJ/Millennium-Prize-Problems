# T124 report

Control: control.txt = 6.493939 (=pi^4/15; numerical trapezoid agrees).

## Verdict / answers (all exact Gaussian, T->inf = T=512, no MC; details in results.md)
| item | S | A1 | E |
|---|---|---|---|
| C_X(0) | 3.5 (7/2) | 12.75 (51/4) | 3.125 (25/8) |
| C(1)/C(0) | 0.01772599482 | 0.01610170543 | 0.01883051160 |
| C(2)/C(0) | 4.198088516e-4 | 3.595403284e-4 | 4.607914475e-4 |
| E1 | 3.5254943 = 4 asinh(1) | same | same |
| w1 (abs) / w1/C(0) | 1.5 / 3/7=0.4285714286 | 4.5 / 6/17=0.3529411765 | 1.5 / 0.48 |

Q1 for T=32,48,64 equal T->inf to ~1e-17 (tables in results.md; t=0..6). Q2: spatial plaquette mean 0.679604436266, variance 0.307908126528 (=1.5 P_pp^2), P_pp=0.4530696241773, T-independent. Q3: auditor's E1 3.52549435 agrees (2e-9 rounding); auditor's weight 0.046875=3/64 matches none of the normalised weights; equals w1(S)/32 (guess about their normalisation; unverified).

## Failed predicates
None failed. (Fixed predicates P1-P7 in t124.py docstring, F1-F4 in fit.py.) P7 and P3 (T=256 vs 512) were not coded as separate asserts in t124.py; I checked them by reading data_v1.json/prints (spread 3e-16; T=32..512 diffs 1e-17), and the fit.py F4 covered T convergence. My own wrong expectation en route: I first read the orientation printout as spatial T-dependent; that was my index error (first three entries are temporal plaquettes, P_pp = limit - 1/(8T)), not a target defect. Fit extrapolation to t=9..12 deviates 4e-10..8e-8 relative: roundoff in P(tau) growing with t, not a spectrum defect (fit fixed to t<=8).

## Not checked
- No independent analytic derivation of the pair-photon spectrum beyond the exact 3-term fit match; no check that other lattices/L behave alike.
- T->inf is T=512, not an analytic transfer-matrix limit.
- Per-site P_pp spread checked only at T>=256. Temporal-plaquette -1/(8T) law checked T=16..256 only numerically.
- mk.py (results.md writer) ran outside pcp check (x-mode file so not rerunnable); the main run and fit are recorded.
- The auditor's weight definition is unknown.

## Grandchild (task T127, released)
Question: independently (dense SVD, T=10, own indexing, own Wick derivation) recompute mean/variance of a spatial plaquette energy, C_S(t) t=0..4, C_A1(0). Control first: Var(phi^2/2)=0.5 passed. It returned P_pp=0.453069632, var 0.3079081372, C_S(0)=3.500000133, C(1)/C(0)=0.01772601374, C_A1(0)=12.7500004 (rank 237). I reread its answer.txt and main.py, and reproduced all digits with my Fourier code at T=10 (differences from T->inf are the finite-T e^{-3.5T}~1e-7 effect). Its toy MC check supports only the formula Cov=1.5 P^2 loosely (0.1355 vs 0.1350, within MC). Outcome: agreement.

## Rerun commands (cwd = this dir; result files are x-mode, use a new tag/dir)
python3 t124.py v2      # writes data_v2.json (~1 s)
python3 fit.py          # reads data_v1.json (edit name for v2); output to stdout
python3 grandchild/main.py  # fails if answer.txt exists; copy dir first
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P verify --ws pcp

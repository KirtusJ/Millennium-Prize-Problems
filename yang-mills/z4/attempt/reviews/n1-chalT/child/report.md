# T136 report — splitting of the circle walk, claim -log(m)/sqrt(beta) -> c* = 4.6054132

**Verdict: STANDS (consistent with the claim, not proven).** The ratio rises monotonically toward c* but is still 0.176 below it at beta=4096. The fitted c is 4.5635, about 0.9% under c*.

Control: `control.txt` = 4.605413 (matches c*).

## Method
Sectors even under a->-a live on [0,pi/2] (midpoint grid, reflections handled by images).
- S = reflecting-at-0 part, B = image part about pi/2; A_e = S+B, A_o = S-B (both PSD).
- Exact identity: lam_e - lam_o = 2<g_o,B g_e>/<g_o,g_e>, and m = log1p((lam_e-lam_o)/lam_o). No eigenvalue difference is taken.
- Eigenvectors come from repeated squaring of the matrix with rescaling (60 squarings; 75 checked). Tails down to 1e-64 stay representable in double.
- Grid step h = ceil-based n = ceil(pi/2*5*sqrt(beta)), i.e. h <= 1/(5 sqrt(beta)). The run is repeated at h/2.

## Results (grid h/2; n = 126, 252, 504, 1006)
| beta | log m | -log m / sqrt(beta) |
|---|---|---|
| 64 | -31.18520 | 3.898150 |
| 256 | -66.64787 | 4.165492 |
| 1024 | -138.50948 | 4.328421 |
| 4096 | -283.48296 | 4.429421 |

Fit -log m = c sqrt(beta) + b log(beta) + c0 (4 points, 3 parameters, 1 degree of freedom):
- c = 4.5635, b = -0.789, c0 = -2.03. Residuals are up to 0.034.
- With Richardson h^2 extrapolation of log m: c = 4.5635, unchanged.
- Exact solve on the three largest beta: c = 4.569, b = -0.90.
- 2-parameter fit without the log term: c = 4.509.

Gap c* - ratio: 0.707, 0.440, 0.277, 0.176. The gap shrinks by about 0.63 per factor 4 in beta; sqrt(beta) alone would give 0.5 and a log(beta)/sqrt(beta) correction gives a slower shrink.

## Predicates
- P0 control = 4.605413: **met**.
- P1 grid change |ratio(h)-ratio(h/2)| < 1e-3: **met** for all 4 beta (changes 5.8e-4, 2.3e-4, 9.4e-5, 3.8e-5). Tolerance: I chose it from the claim's 1e-3 scale; the midpoint error is O(h^2) because of the |a| kink in eps.
- P2 squaring 60 vs 75: log m agrees to 1e-9: **met** (identical to printed digits). The tolerance is my choice; double rounding is about 1e-13.
- P3 beta=64 independent route, |dlog m| < 1e-6: **met**. The grandchild T137 got -31.180578395507449 and I got -31.18057839550745 (about 1e-14 apart). The tolerance is my choice.
- P4 |c_fit - c*| < 0.03 c* (0.138): **met**, |c-c*| = 0.042. The tolerance is my choice; the fit has only 1 degree of freedom, so this is weak evidence.
- P5 ratio increasing in beta: **met**.
- Naive eigh difference at beta=64: **measured only**. lam_e-lam_o = 2.109e-14 versus the identity's 2.094e-14, 0.7% off. It already degrades at beta=64 and is useless beyond that. This confirms the warning, and was not a failed predicate.
- Failed predicates: none.
- Not tested: the limit beta -> infinity itself, and any beta above 4096.
- The 3-term fit leaves residuals up to 0.03, so the log-correction form is not exactly right. That limits how much the fitted c, and hence the verdict, can be trusted.

## Grandchild
- Task id **T137** (admitted with parent T136, released).
- It passed its known-answer control: the top eigenvalue of [[2,1],[1,2]] came out as 3.
- Pure `decimal` arithmetic at 90 digits, on the same discretization at beta=64, n=63.
- Result: log m = -31.180578395507448542, agreeing with my double-precision identity value.
- I reread its `run.py` and reran it in `gc_rerun/` (PCP check K4); it reproduced the same number.

## PCP OS
- `pcp_os.py init` reported the method packet as not found, as expected.
- Checks K1 to K4 were recorded (control, split, fit, grandchild rerun).
- Last line of `pcp_os.py verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)".
- Last line of `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

## Rerun
```
cd /home/user/z4-workers/n1-chalT/child
export OMP_NUM_THREADS=1
python3 control.py                      # 4.605413
python3 split.py                        # needs split_results.json absent (mode "x"); ~10 s
python3 fit.py
cd grandchild && python3 run.py         # needs its control.txt/results.txt removed first; ~20 s
```

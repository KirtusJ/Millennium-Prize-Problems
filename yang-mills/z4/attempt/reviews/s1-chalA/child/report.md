# T165 report (1D continuum model, claim: -log(Delta)/sqrt(beta) -> c*, not 2c*)
Control: control.txt = 0.718282 (e-2). Grandchild control: 0.718282.

## Verdicts
- **-log(Delta)/sqrt(beta) -> c* (not 2c*): STANDS (numerically, trend only).** Values 3.94, 4.18, 4.33, 4.43 for beta=64..4096 (ratio to c*: 0.855, 0.907, 0.941, 0.962). c*-A shrinks by a near-constant factor 0.64 per 4x in beta (0.640, 0.639, 0.640). 2c*=9.21 is far off. The limit itself is not proven by 4 points, and the decay rate (~beta^-0.32) is empirical.
- **-log(m)/sqrt(beta) has the same limit: STANDS.** m = -log(1-Delta/lam_e) so B-A = log(lam_e)/sqrt(beta) to 1e-15 (identity, P5). B: 3.898, 4.165, 4.328, 4.429.
- **(log g(0)-log g(pi/2))/sqrt(beta) -> c*/2: STANDS (trend only).** 1.926, 2.064, 2.152, 2.207 vs c*/2=2.3027; c*/2-C shrinks by ~0.63-0.64 per 4x in beta.
- **c* = 4.6054132: STANDS.** Mine 4.605413195 (Gauss-Legendre after a=t^2, 400 nodes); grandchild 4.605413195.
- **Identity method vs direct subtraction: STANDS.** beta=16 rel diff 3.7e-10; beta=36 rel diff 1.4e-6 (direct is the noisy one).

## Numbers (grid n; alt = 1.5n grid)
| beta | n | h*sqrt(b) | lam_e | Delta | -logD/sqrt(b) | alt grid | -log m/sqrt(b) | (log g0-log g(pi/2))/sqrt(b) |
|---|---|---|---|---|---|---|---|---|
| 64 | 101 | 0.1244 | 0.72897 | 2.0870e-14 | 3.93756 | 3.93771 | 3.89804 | 1.92587 |
| 256 | 202 | 0.1244 | 0.81797 | 9.2947e-30 | 4.17801 | 4.17807 | 4.16545 | 2.06432 |
| 1024 | 403 | 0.1247 | 0.88069 | 6.1825e-61 | 4.33237 | 4.33240 | 4.32840 | 2.15153 |
| 4096 | 805 | 0.1249 | 0.92298 | 7.0844e-124 | 4.43067 | 4.43068 | 4.42941 | 2.20662 |
c* = 4.6054132, c*/2 = 2.3027066. Direct check: beta=16 (n=51) Delta direct 6.138935183e-7 vs identity 6.138935181e-7; beta=36 (n=76) 1.22423e-10 both (rel diff 1.4e-6).
All top eigenvectors strictly positive. At beta=1024, 4096 the minimum matrix entries underflow to 0 (far-from-diagonal entries; harmless, squaring refills them from chains).

## Predicates (fixed in run_main.py docstring before first run)
P1, P2, P3, P4, P5 all PASSED. No predicate failed in my programs. Tolerance origins: P1 = max(1e-6, 1e3*machine eps*lam_e/Delta) (rounding amplified by cancellation); P2 1e-3 = my expectation, grid error from the kink of eps at 0, pi (h^2); observed max 1.6e-4. P3/P4 15% = my expectation (finite-beta corrections ~log(beta)/sqrt(beta)), not derived; observed 3.8% and 4.2% at 4096, non-increasing in beta. P5 is a near-tautology (algebra), kept as a code check.
Caveats: P3/P4 were chosen before I saw the data, and the real decay (0.64 per 4x) is slower than 1/sqrt(beta) (0.5 per 4x), so the "O(log b/sqrt b)" expectation was loose. "g" is the eigenfunction of the symmetrised T (with e^{-eps/2} factors); g(0), g(pi/2) are the first/last midpoint grid values (x=h/2 and pi/2-h/2), a small bias of order h*gradient not separately quantified (alt grid shifts C by <=7e-5).
Failed predicate of the grandchild (its own P2: two grids at beta=16 agree to 1e-6): failed, diff 6.07e-4; this was its own over-tight expectation (kink => O(h^2) error), not a defect of the target. Extrapolated 3.57650. My beta=16 value 3.57586 (n=51) differs by 6.4e-4, same scale as that grid error.

## Grandchild
Task id T166 (admitted with --parent T165, released event 333). Outcome: control OK, c* 4.605413195, beta=16 -log(Delta)/sqrt(beta)=3.5765 (extrapolated), Delta ~ 6.1233e-7. I reread grandchild/report.md and reran run.py in a scratch copy (pcp check K3 exit 0): identical numbers.

## Rerun
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1; (results.json is mode 'x': remove it first)
python3 run_main.py          # ~16 s
python3 check_preds.py       # predicates from results.json
cd grandchild && python3 run.py   # needs report.md removed (mode 'x')

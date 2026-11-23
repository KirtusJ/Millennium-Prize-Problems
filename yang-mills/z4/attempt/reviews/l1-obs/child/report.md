# T125 report (l1-obs child)
**Control:** arccosh(3) = 1.76274717 (control.txt).

## Q1 (matrix spectrum, ordered-pair convention mu=3/2 sum_{v,v'} a a')
| box | E (matrix) | weight | closed form E | auditor E / weight | sum a(v) |
|---|---|---|---|---|---|
| (2,2,2) | 3.52549435 | 0.04687500 | 3.52549435 | 3.52549435 / 0.046875 | 0.45306962 |
| (3,3,3) | 3.13359847 | 0.01410935 | 3.13359847 | 3.13359847 / 0.01410935 | 0.49085147 |
| (3,2,5) | 3.13359847 | 0.00285714 | 3.13359847 | 3.13359847 / 0.00285714 | 0.46651745 |
All three match closed form and auditor (P1,P2,P3 met). Note: weight matches auditor only with ordered pairs (unordered would be half).

## Q2
| N | N*E-4pi | N^8 mu-24pi^2 | rates (log2 ratio) |
|---|---|---|---|
| 4 | -2.0307074 | -108.87051 | |
| 8 | -0.6012602 | -40.662509 | 1.756 / 1.421 |
| 16 | -0.1584654 | -11.602194 | 1.924 / 1.809 |
| 32 | -0.0401796 | -3.0068436 | 1.980 / 1.948 |
Both converge ~ 1/N^2 (E) and ~1/N^2 (mu; local rate 1.95 at N=32, still rising). Matrix vs closed form at N=4, 8 agree to ~1e-14 relative (P4 met). N=16,32 closed form only (matrix 3n=12288 too large for budget).

## Predicates: met 4 (P1,P2,P3,P4; plus grandchild cf check and agreement), failed 0, measured only 1 (convergence rates)
No predicate failed, so no failure to attribute.

## Not checked
Weight convention other than ordered pairs; closed form beyond tested boxes (e.g. boxes with N<3 sides other than (2,2,2); other plaquette orientations); N=16,32 by matrix/Fourier sum; asymptotic exponent beyond fitted local rates; the claim "N>=3 closed-form threshold mass" for N=3 only through Q1.

## Delegated
Task T126 (admitted, released). Control (2,2,2) passed. Boxes (5,2,3),(2,5,3),(3,2,5): E = 2.23329063, 2.23329063, 3.13359847; weights 0.00171185, 0.00171185, 0.00285714. Closed form with max(N1,N2) matches all; max over all three sides fails for (3,2,5); min(N1,N2) fails. I reread run.py and reran with my own code (rerun.py, out_rerun.txt): agrees to 1e-8.

## Rerun
cd child; python3 q.py ; python3 rerun.py (outputs to new files; result files are never overwritten—use fresh dir/names). Register: pcp/ (checks K1 q, K2 rerun).

## Verify (last lines)
- pcp_os verify: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- pcpos verify: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.

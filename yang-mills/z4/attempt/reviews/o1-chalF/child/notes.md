# notes
- control.txt written (I_0(1))
- scipy/mpmath absent: control via midpoint rule (spectrally accurate for periodic integrand), value 1.266066 (I_0(1)=1.266066). Bessel must be self-implemented in numpy.
- wrote barta.py (predicates P1-P5 in docstring); next: run via pcp check
- run1 (pcp check K1) exit 1: P4 failed 5/108 cases (103 qualify). Cause: B underflows to denormal/0 for beta=4096 (s=.3 rho=.999,1; s=1 rho>=.99) so relative change is NaN/1e-4 on denormals. Defect of MY predicate (relative change on underflowed values), not of the target. res1.csv/res_conv.csv/summary.csv from run1 are kept (never overwritten); sup B is unaffected (attained at rho<=0.3).
- grandchild T143 returned B(0;64,0.3)=0.5576952560
- report.md written, T143 released, verifies passed

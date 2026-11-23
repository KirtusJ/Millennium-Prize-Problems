# notes
- control: I1(1)/I0(1)=0.446390 (power series, written to control.txt)
- Q1 done: see q1_result.txt (series Decimal vs midpoint-trapezoid integral)
- Q2 (q2.py): red rule converged A=-0.0833333333 (=-1/12 numerically), B=0.1982495197. Predicate Q4 FAILED: full(10,8,16) B off by 1.6e-5 vs tol 1e-8. Cause: MY expectation (tolerance too tight for a coarse 6-D rule; red N=10 already differs 2.8e-6), not a defect in target. Retest with finer full rule in q2b.py (new predicate fixed in docstring).
- Sub-agent T75 returned A=-0.083333333333, B=0.198249519694, control 0.446390 (to be rerun/reread).
- report.md written; T75 released

# notes
- control: I=1/sqrt5=0.447214 (midpoint quadrature agrees), control.txt written. pcp register initialised (method not found, expected).
- gquad.py done (gquad_result.json): 3D midpoint L=32..512, O(L^-4) convergence; G(0)=0.5000000000019, G(1)=0.06887474584, G(2)=0.01115271766; last-grid diff 2.8e-11. Q1-Q3 met.
- grandchild (direct 4D grid L=24,32) control G(0)=0.5 exact; G(1)=0.0688747429, G(2)=0.0111527058 at L=32; agrees with mine to 3e-9 / 1.2e-7 (its error est 1e-8 / 5.6e-8; G(2) gap 1.2e-7 is a bit above its own estimate -> its grid is coarse; mine is the converged one).
- cov.py first run failed (K2): my own bug (leftover junk line computing Dg), not target; removed, no result file written.
- cov.py run 1 (cov_result.json): C1,C3,C6 true; C2,C5,C4(n=2) FAILED: my expectation error: at N=4, p2 is at x0=4 on the shell, F_p2 identically 0 (b=0 -> nan). Not target defect. Amended and rerun -> cov2_result.json.
- report.md written; PCP verify PASS.

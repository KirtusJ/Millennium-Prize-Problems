# notes T136
- Step 1: control (control.py -> control.txt) = 4.605413, matches c* 4.6054132 to 6 d.p. (Gauss-Legendre 4000 pts, endpoint-smoothing substitution).
- Step 2: split.py (identity method, squaring eigvecs) 4 betas x grids h,h/2 and 75 squarings -> split_results.json. Grid change <=6e-4 in ratio; squaring 60 vs 75 identical.
- Step 3: fit.py: c(fit with b log beta)=4.5635 (h/2), 4.5635 (Richardson); P4 met (|c-c*|=0.042 <0.138). Ratio still 0.176 below c* at beta=4096, increasing.
- Step 4: grandchild T137 (decimal 90 digits, beta=64) log m=-31.180578395507449 vs mine -31.18057839550745: agree ~1e-14. Rerun in gc_rerun/ reproduced exactly. Naive eigh difference 2.109e-14 vs exact 2.094e-14 (0.7% off, as expected). T137 released.

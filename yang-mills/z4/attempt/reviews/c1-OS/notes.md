# notes c1-OS
Step 0: control.txt = 0.272341 (-ln tanh 1)
Step 1: read ledger+reduction; child admitted T7 (child_admit.log); child control = lattice G_1(0) d=4 = 0.127112 (my value 0.12711185041, heat-kernel and N=32,48 momentum sums agree to 1e-15)
Step 2: child-run1 exit 0 in 145 s; child control 0.127112 = mine (PASS graded before reading rest); T7 released
Step 3: wrote freefield_S.py with predicates P0-P9 in docstring (before first run)
Step 4: freefield_S run K2 exit 0: 32 met 4 failed (P0 own quadrature cutoff 1e-8; P3 t/space axis degenerate =normalization point, own predicate; P3 (0.3,0.4) sign change, own expectation). Source reader: projecteuclid blocked; OS axioms via KQR arXiv:2104.02090 Sec 2.2, 9.2 eq 9.18 (full text, secondary); ADC 1912.07973 abstract; DKKMO 2012.11672 abstract; Sakai math-ph/0510093 abstract; OS-Seiler snippets only.
Step 5: child rerun K3 identical; THEOREM_S.md written
Step 6: register verified (py PASS, rust pass line); report.md written. Done.

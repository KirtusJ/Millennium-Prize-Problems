# notes T156
- control: 1.000000 (trapezoid on [-12,12])
- mc.py written, predicates in docstring; running via pcp check
- first run failed: scipy missing (environment, not target); replaced I2/I1 by trapezoid quadrature of density (2e6 pts)
- results_mc.json INVALID (own code defect: E-factor offset double-counted in delta1, found by review before evaluating predicates); fixed, output now results_mc2.json. Grandchild T157 released; its numbers rerun identically.
- report.md written

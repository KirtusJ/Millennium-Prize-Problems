# F6 boundary check
Statement: x^(2j) exp(-c x^2) <= (j/(e c))^j, equality at x^2 = j/c.
Method: Python decimal, 50 digits (mpmath not installed), j in {1,2,3,5,10,50,200}, c in {0.01,1,37}.
- Control: sin(1)-1+1/6 = 0.008138 (matches expected).
- Equality point: max |relative difference| = 9.353e-48 (rounding level; consistent with exact equality).
- At x^2 = (j/c)(1 +/- 1e-3): lhs < rhs in all 42 cases; relative slack is about 5e-7 for j=1 and about 1e-4 for j=200, growing roughly like j*1e-6/2 (second-order, as expected at a maximum). Min slack 4.997e-7.
Rerun: results.txt opens with mode 'x', so delete it first.

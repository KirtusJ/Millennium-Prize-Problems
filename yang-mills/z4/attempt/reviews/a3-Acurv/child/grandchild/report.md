# Report
Control: FD d2/dt2 Re Tr exp(tX) = -1.000000 (h=1e-3), analytic -1; agrees (tol 1e-5). Note scipy was unavailable; expm implemented in numpy (eigh of anti-Hermitian matrix).
Hessian (central FD only, 12x12, symmetric to 0):
- h=1e-2: min eig(I+H) = -0.999973; h=1e-3: min eig(I+H) = -0.99999973.
- Distinct eigenvalues of I+H (grouping tol 1e-5): -1.000000 (x3), +1.000000 (x9). (H itself: -2 x3, 0 x9.)
Trusted: h=1e-3 (truncation ~h^2 ~1e-7, roundoff ~1e-10); h=1e-2 differs by 2.7e-5, consistent with O(h^2) truncation. Control also converges at 1e-2 -> 1e-3 -> 1e-4 as O(h^2).
So I+H is NOT positive: smallest eigenvalue = -1 (3-fold; the three modes where U1 perturbation is not compensated, i.e. the plaquette at Q=-1 is a maximum of V).
Files: hess.py, results.txt, control.txt.

"""test_c3.py -- DK' at xi=256 in log space (test_c2 crashed there: exp(-765) underflow, own defect).
Usage: python3 test_c3.py <result_file>  (mode "x"). Predicate fixed before run:
 Q3b: log R_psi(256) >= 256/2 - log 3, with R_psi = C(2.5xi)/C(3xi), C(n) = w e^{-n/xi} + e^{-n}, log w = -3xi+3.
"""
import sys, math
def lse(a, b): M = max(a, b); return M + math.log(math.exp(a - M) + math.exp(b - M))
xi = 256; lw = -3 * xi + 3
lC = lambda n: lse(lw - n / xi, -n)
lr = lC(2.5 * xi) - lC(3 * xi); ok = lr >= xi / 2 - math.log(3)
with open(sys.argv[1], "x") as f: f.write(f"log R_psi(256) = {lr:.6f}; xi/2 - log3 = {xi/2-math.log(3):.6f}; Q3b {'MET' if ok else 'FAILED'}\n")
print(lr, ok); sys.exit(0 if ok else 1)

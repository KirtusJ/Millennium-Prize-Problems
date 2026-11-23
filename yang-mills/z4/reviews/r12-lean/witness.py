"""Mutation witness numeric check (k=1, b=1/5).
Predicate W1: |(2/b) sin(kb/2) - k| > b^2|k|^3/25 at k=1,b=1/5 (expect True; margin ~1.6e-7 abs).
Predicate W2: same lhs <= b^2|k|^3/24 (expect True).
Tolerance: none needed beyond float64; margins ~1e-7 >> 1e-15 rounding. Result file mode 'x'."""
import math, sys
k, b = 1.0, 0.2
lhs = abs((2/b)*math.sin(k*b/2) - k)
r25, r24 = b*b*abs(k)**3/25, b*b*abs(k)**3/24
with open(sys.argv[1], "x") as f:
    s = f"lhs={lhs:.12e} rhs25={r25:.12e} rhs24={r24:.12e} W1={lhs>r25} W2={lhs<=r24}"
    print(s); f.write(s+"\n")
sys.exit(0 if (lhs > r25 and lhs <= r24) else 1)

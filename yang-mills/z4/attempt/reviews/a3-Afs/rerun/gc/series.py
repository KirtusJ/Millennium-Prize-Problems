import math, os, sys

def I(n, x):
    s = 0.0
    k = 0
    while True:
        t = (x / 2) ** (2 * k + n) / (math.factorial(k) * math.factorial(k + n))
        s += t
        if t < 1e-18 and k > 0:
            break
        if k == 0 and x == 0:
            # all later terms are 0
            break
        k += 1
    return s

d = os.path.dirname(os.path.abspath(__file__))
c = I(0, 0.0)
if c != 1:
    print("control failed:", c); sys.exit(1)
with open(os.path.join(d, "control.txt"), "x") as f:
    f.write("I_0(0) = %r\n" % c)
r1 = I(1, 2.3) / I(0, 2.3)
r2 = I(2, 2.3) / I(1, 2.3)
r3 = I(2, 2) / I(1, 2)
nl = -math.log(r1)
out = ("I1(2.3)/I0(2.3) = %.8f\nI2(2.3)/I1(2.3) = %.8f\nI2(2)/I1(2) = %.8f\n-ln(I1(2.3)/I0(2.3)) = %.8f\n" % (r1, r2, r3, nl))
with open(os.path.join(d, "result.txt"), "x") as f:
    f.write(out)
print(out)

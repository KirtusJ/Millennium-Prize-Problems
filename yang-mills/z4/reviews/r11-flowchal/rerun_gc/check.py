from math import cos, cosh, sinh, acosh, pi
m2=2-2*cos(pi/8); w=acosh(1+m2/2)
rows=[];mx=0.0
for n in range(5):
    d=sum(cos(2*pi*l*n/16)/(m2+2-2*cos(2*pi*l/16)) for l in range(16))/16
    c=cosh(w*(8-n))/(2*sinh(w)*sinh(8*w))
    e=abs(d-c); mx=max(mx,e); rows.append((n,d,c,e))
tol=1e-13
with open('result.md','x') as f:
    f.write("# Periodic Green function check, N=16\n\n")
    f.write("m^2=2-2cos(pi/8)=%.15g, w=%.15g\n\n"%(m2,w))
    f.write("Derivation: denominator = 2cosh w - 2cos k; infinite-line G=e^{-w|n|}/(2 sinh w); periodic sum over images sum_j e^{-w|n+16j|}/(2 sinh w) = cosh(w(8-|n|))/(2 sinh w sinh 8w) for |n|<=16.\n\n")
    f.write("| n | direct | closed | abs diff |\n|---|---|---|---|\n")
    for n,d,c,e in rows: f.write("| %d | %.16g | %.16g | %.3g |\n"%(n,d,c,e))
    f.write("\nmax abs diff = %.3g\n"%mx)
    f.write("Tolerance 1e-13: float64 eps ~2.2e-16, values O(0.5-1), 16-term sums plus cosh/sinh rounding give errors of a few eps; 1e-13 is a safe margin. Control sum was -9.0e-16, consistent.\n")
    f.write("Result: %s\n"%("PASS" if mx<tol else "FAIL"))
print(open('result.md').read())

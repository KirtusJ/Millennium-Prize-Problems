"""prog1b_kmin.py -- rerun of predicate C10 of prog1_constants.py, whose failure was MY defect:
exp(b*cos th) overflowed at b=1e4 (nan). Predicate unchanged: for theta=R/sqrt(b), R=3,
k = b e^{b(cos th -1)}/(2 e^{-b}I1(b)) >= sqrt(2/pi) b^{3/2} e^{-R^2/2}; also R in {0.5,1,3,5} and b in {2,10,100,1e4,1e6}.
Tolerance: none (strict). Result file mode 'x'."""
import numpy as np, math
from numpy import sin, cos, exp, sqrt, pi
GLx,GLw=np.polynomial.legendre.leggauss(400)
def quad(f,a,b): return ((b-a)/2*GLw*f((b-a)/2*GLx+(a+b)/2)).sum()
def quadc(f,a,b,n=40):
    e=np.linspace(a,b,n+1); return sum(quad(f,e[i],e[i+1]) for i in range(n))
def I1s(b):
    f=lambda t: exp(-2*b*sin(t/2)**2)*cos(t); cut=min(pi,60/sqrt(b))
    return (quadc(f,0,cut)+(quadc(f,cut,pi) if cut<pi else 0))/pi
out=[];ok=True
for b in [2.,10.,100.,1e4,1e6]:
    for R in [0.5,1,3,5]:
        th=R/math.sqrt(b)
        if th>pi: continue
        k=b*math.exp(-2*b*math.sin(th/2)**2)/(2*I1s(b)); km=math.sqrt(2/pi)*b**1.5*math.exp(-R*R/2)
        ok&= k>=km; out.append(f'b={b:g} R={R}: k={k:.5g} kmin={km:.5g} ratio={k/km:.4f}')
out.append('C10b: '+('MET' if ok else 'FAILED'))
print('\n'.join(out)); open('result_prog1b.txt','x').write('\n'.join(out)+'\n')

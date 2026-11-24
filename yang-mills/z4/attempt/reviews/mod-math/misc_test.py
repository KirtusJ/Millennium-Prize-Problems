"""Miscellaneous checks. PREDICATES fixed first:
 M1 Remark r:three: T=diag(.95,.3), r=.8: F(v)=<v,(rI-T)(I-T)v> >0 on (1,+-1)/sqrt2, <0 on (1,0); displayed inequality of p:three holds/fails accordingly.
 M2 SU(2) character coefficients: c_n=(2/pi)int_0^pi sin(t) sin((n+1)t) e^{beta cos t} dt equals 2(n+1) I_{n+1}(beta)/beta (series), n=0..6, beta in {0.5,3.4}; rel err<1e-9; all >0.
 M3 Remark r:ret(b): p_{6 beta}(theta) at beta=3.399810242 for theta=.05,.2,.6 rounds to .00307,.156,.935; envelope bound holds on a grid.
 M4 R'(6) in (0.036885895,0.036885896) by exact rational series (60 terms, tail < 1e-30); R'(6)/beta^2 rounds to .00344 and .00319.
 M5 Remark r:budget recurrence, 40 steps, exact rationals: equality at every step, sum M_{i-1}kappa_i = d0(1-2^-n).
 M6 Remark r:ret(a) constant: M p <= 3 pi^2 sqrt(e) c^3/(32 N) identity at N=6..96, c=1, beta=2.
Output results_misc.txt (refuses to overwrite). No arguments, no randomness."""
import numpy as np, os, sys
from fractions import Fraction as F
from math import factorial, pi, e, sqrt
OUT='results_misc.txt'
if os.path.exists(OUT): sys.exit('refuse')
log=[]
T=np.diag([.95,.3]); r=.8; X=(r*np.eye(2)-T)@(np.eye(2)-T)
vals=[]
for v in ([1,1],[1,-1]): 
    v=np.array(v)/sqrt(2); vals.append(v@X@v); assert ((1+r)*v@T@v - v@T@T@v <= r*v@v)
v=np.array([1.,0]); vals.append(v@X@v); assert not ((1+r)*v@T@v - v@T@T@v <= r*v@v)
log.append(f'M1 F values {vals} '+('PASS' if vals[0]>0 and vals[1]>0 and vals[2]<0 else 'FAIL'))
def I(nu,x,terms=80): return sum((x/2)**(2*k+nu)/(factorial(k)*factorial(k+nu)) for k in range(terms))
def quad(f,a,b,n=200000):
    t=np.linspace(a,b,n+1); y=f(t); h=(b-a)/n
    return h/3*(y[0]+y[-1]+4*y[1:-1:2].sum()+2*y[2:-1:2].sum())
m2=0;pos=True
for beta in (0.5,3.4):
    for n in range(7):
        c=2/pi*quad(lambda t:np.sin(t)*np.sin((n+1)*t)*np.exp(beta*np.cos(t)),0,pi); ref=2*(n+1)*I(n+1,beta)/beta
        m2=max(m2,abs(c/ref-1)); pos&=c>0
log.append(f'M2 max rel err {m2:.2e}, all positive {pos} '+('PASS' if m2<1e-9 and pos else 'FAIL')+'; convolution eigenvalue on spin n/2 is c_n/(n+1)=2 I_{n+1}(beta)/beta')
def p(k,th): 
    g=lambda t:np.sin(t)**2*np.exp(k*(np.cos(t)-1)); return quad(g,0,th)/quad(g,0,pi)
b=3.399810242; pv=[p(6*b,t) for t in (.05,.2,.6)]
env=all(p(k,t)<=min(1,pi**2*sqrt(e)/4*(1+k)**1.5*t**3)+1e-12 for k in (0,.3,2,20,60) for t in np.linspace(0,pi,40))
log.append(f'M3 p_6beta = {[float(f"{x:.5f}") for x in pv]}, envelope {env} '+('PASS' if [round(x,5) for x in (round(pv[0],5),)] and abs(pv[0]-.00307)<5e-6 and abs(pv[1]-.156)<5e-4 and abs(pv[2]-.935)<5e-4 and env else 'FAIL'))
def Iex(nu,x,terms=60): return sum((x/2)**(2*k+nu)/(factorial(k)*factorial(k+nu)) for k in range(terms))
k=F(6); R=Iex(2,k)/Iex(1,k); Rp=1-3*R/k-R*R
log.append(f'M4 R\'(6) = {float(Rp):.12f} in interval {F(36885895,10**9)<Rp<F(36885896,10**9)}; /beta^2: {float(Rp)/3.276133577**2:.5f}, {float(Rp)/b**2:.5f} '+('PASS' if F(36885895,10**9)<Rp<F(36885896,10**9) else 'FAIL'))
d0=F(1,2); d=d0; M=F(1); s=F(0); good=True
for i in range(1,41):
    K=1+F(1,2**i); kap=d/2; s+=M*kap; dn=d0/(2**i*M*K); good&=(dn==(d-kap)/K); M*=K; d=dn
log.append(f'M5 equality every step {good}, budget sum == d0(1-2^-40) {s==d0*(1-F(1,2**40))}, d_40 = {float(d):.3e}, M_40 = {float(M):.4f} '+('PASS' if good and s==d0*(1-F(1,2**40)) else 'FAIL'))
m6=True
for N in (6,12,24,48,96):
    beta=2.;th=(1+6*beta)**-.5*N**(-4/3); Mg=3*(N//2)**3
    m6&= Mg*p(6*beta,th) <= 3*pi**2*sqrt(e)/(32*N)*(1+1e-12) and abs(Mg*pi**2*sqrt(e)/4*(1+6*beta)**1.5*th**3-3*pi**2*sqrt(e)/(32*N))<1e-12
log.append('M6 '+('PASS' if m6 else 'FAIL'))
open(OUT,'x').write('\n'.join(log)+'\n'); print('\n'.join(log))

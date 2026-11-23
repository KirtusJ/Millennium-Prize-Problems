"""T155. Predicates fixed before running:
P1 control: I = exp(rho^2/2) = e^2 = 7.389056 (numeric quadrature must agree to 1e-6).
P2 Delta_direct and Delta_identity agree to relative diff < 1e-6 if Delta > 1e-10*lambda; else direct is unresolved.
P3 direct subtraction resolvable iff Delta > 1e-16*lambda_+ (strictly, and practically >~1e3 times that).
Results written with mode 'x'.
"""
import numpy as np, math
b,rho=9.0,2.0
t=np.linspace(-12,12,2000001)
I=np.trapezoid(np.sqrt(b/(2*np.pi))*np.exp(-b*t**2/2)*np.exp(-rho*np.sqrt(b)*t),t)
with open('control.txt','x') as f: f.write("%.6f\n"%I)
beta=16.0
Nx=8*math.ceil(2*math.pi*math.sqrt(beta)/(0.25*8)); dx=2*math.pi/Nx
x=-np.pi+np.arange(Nx)*dx
eps=2*np.arcsinh(np.abs(np.sin(x)))
d=x[:,None]-x[None,:]
K=sum(np.sqrt(beta/(2*np.pi))*np.exp(-beta*(d+2*np.pi*k)**2/2) for k in (-1,0,1))
w=np.exp(-eps/2)
M=w[:,None]*K*w[None,:]*dx
A=np.arange(Nx//4,3*Nx//4)
TAA=M[np.ix_(A,A)]
R=M[np.ix_(A,(A+Nx//2)%Nx)]
Tp,Tm=TAA+R,TAA-R
ep,vp=np.linalg.eigh(Tp); em,vm=np.linalg.eigh(Tm)
lp,lm=ep[-1],em[-1]; g,fv=vp[:,-1],vm[:,-1]
Dd=lp-lm
Di=2*fv@R@g/(fv@g)
rel=abs(Dd-Di)/abs(Di)
res=Dd>1e3*1e-16*lp
s=f"""# T155 result
Nx={Nx}, dx={dx!r}, |A|={len(A)}
lambda_+ = {lp!r}
lambda_- = {lm!r}
Delta_direct = {Dd!r}
Delta_identity = {Di!r}
relative difference = {rel!r}
Delta/(1e-16*lambda_+) = {Dd/(1e-16*lp)!r}
Direct subtraction resolvable (Delta > 1e3 * 1e-16 lambda): {res}
control I = {I:.6f} (exp(2)={math.exp(2):.6f})

Rerun: cd /home/user/z4-workers/q1-paths/child/grandchild && rm -f control.txt result.md && python3 run.py
"""
with open('result.md','x') as f: f.write(s)
print(s)

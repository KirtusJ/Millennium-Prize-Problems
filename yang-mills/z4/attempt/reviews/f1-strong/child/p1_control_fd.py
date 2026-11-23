"""P1: control + Hessian validation.  Predicates fixed BEFORE first run:
 C1 (control): single plaquette Q=-1 (U1=-1, others 1), Ric=1: eigenvalues of Ric+Hess V computed by
    central finite differences of V itself (independent of lgt.py) must match 1-2*beta (x3), 1 (x9) within 1e-5
    (tolerance: FD h=1e-3 on a trigonometric function of the exact form, truncation ~h^2*|V''''|~1e-6*few; 1e-5 chosen).
 F1: analytic Hmat vs full-lattice finite-difference Hessian of V (exp-map geodesics, h=1e-3, 5-point-free central
    second differences, polarization) at 3 random U: max abs entry error on 20 random (t,t') pairs < 1e-5.
 F2: same at pi-flux config.
 F3: qform equals t^T Hmat t to 1e-10.
Writes control.txt and results/p1.txt (mode x)."""
import numpy as np, sys, lgt
from lgt import *
# ---- control: independent single-plaquette code
def plaqV(Us,beta=1.0):
    Q=Us[0]@Us[1]@inv(Us[2])@inv(Us[3]); return -(beta/2)*np.real(np.trace(Q))
def hess_single(beta,h=1e-3):
    U0=[-np.eye(2,dtype=complex),np.eye(2,dtype=complex),np.eye(2,dtype=complex),np.eye(2,dtype=complex)]
    def V(t): return plaqV([expm_su2(t[3*i:3*i+3])@U0[i] for i in range(4)],beta)
    H=np.zeros((12,12)); n=12; I=np.eye(12)
    for i in range(n):
        for j in range(n):
            H[i,j]=(V(h*(I[i]+I[j]))-V(h*(I[i]-I[j]))-V(h*(-I[i]+I[j]))+V(-h*(I[i]+I[j])))/(4*h*h)
    return H
out=open('results/p1.txt','x')
ok=True
for beta in (1.0,2.5):
    ev=np.linalg.eigvalsh(1*np.eye(12)+hess_single(beta))
    exp=np.sort([1-2*beta]*3+[1.0]*9)
    err=np.abs(ev-exp).max(); out.write(f"control beta={beta} eig={np.round(ev,6).tolist()} maxerr={err:.2e} {'PASS' if err<1e-5 else 'FAIL'}\n"); ok&=err<1e-5
with open('control.txt','x') as f: f.write("1-2*beta (x3) 1 (x9)\n")
# ---- lattice FD
def Vfd(U,t): return lgt.Vact(expm_su2(t.reshape(64,3))@U)
def fdH(U,t,tp,h=1e-3):
    return (Vfd(U,h*(t+tp))-Vfd(U,h*(t-tp))-Vfd(U,h*(-t+tp))+Vfd(U,-h*(t+tp)))/(4*h*h)
rng=np.random.default_rng(12345)
cases=[randU(rng) for _ in range(3)]+[piflux()]
for k,U in enumerate(cases):
    H=Hmat(U); worst=0;wq=0
    for _ in range(20):
        t=rng.normal(size=192);tp=rng.normal(size=192)
        worst=max(worst,abs(fdH(U,t,tp)-t@H@tp))
    for _ in range(5):
        t=rng.normal(size=192); wq=max(wq,abs(qform(U,t.reshape(64,3))-t@H@t))
    out.write(f"case{k} ({'piflux' if k==3 else 'random'}) FDerr={worst:.2e} {'PASS' if worst<1e-5 else 'FAIL'}; qform err={wq:.2e} {'PASS' if wq<1e-10 else 'FAIL'}\n")
    ok&=worst<1e-5 and wq<1e-10
out.write("ALL PASS\n" if ok else "SOME FAIL\n"); out.close()
print(open('results/p1.txt').read()); sys.exit(0 if ok else 1)

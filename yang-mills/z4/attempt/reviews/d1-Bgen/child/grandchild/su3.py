import numpy as np
# polar coords on plane th1+th2+th3=0; th_j = sqrt(2/3) r cos(phi+2pi j/3); dth1 dth2 = r dr dphi /sqrt3
# (Jacobian checked numerically below)
N=4000
phi=(np.arange(N)+.5)*2*np.pi/N
j=np.arange(3)
th=np.sqrt(2/3)*np.cos(phi[:,None]+2*np.pi*j/3)   # unit-radius point
# Jacobian check: d(th1,th2)/d(r,phi) at r=1
def T(r,p): 
    t=np.sqrt(2/3)*r*np.cos(p+2*np.pi*np.arange(2)/3); return t
h=1e-6; r0,p0=1.0,0.7
J=np.array([(T(r0+h,p0)-T(r0-h,p0))/(2*h),(T(r0,p0+h)-T(r0,p0-h))/(2*h)]).T
jac=abs(np.linalg.det(J))  # should be r/sqrt3
g=((th[:,0]-th[:,1])*(th[:,0]-th[:,2])*(th[:,1]-th[:,2]))**2
ang=g.sum()*2*np.pi/N   # expect pi/2
# region f<=s -> sum th^2<=6s -> r<=R=sqrt(6s); integral of r^6 * r dr = R^8/8 (Gauss-Legendre check)
x,w=np.polynomial.legendre.leggauss(8)
radial=sum(wi*0.5*(0.5*(xi+1))**7 for xi,wi in zip(x,w))  # int_0^1 r^7 dr
# V/s^4 = (1/6)(2pi)^-2 * jac_const * ang * radial * (6)^4  with R^8=(6s)^4
c=(1/6)/(2*np.pi)**2*(1/np.sqrt(3))*ang*radial*6**4
cf=9*np.sqrt(3)/(8*np.pi)
txt=f"""# SU(3) small-ball coefficient c = lim V(s)/s^4

Method: Weyl formula, small-s limit: |Delta|^2 -> prod(th_j-th_k)^2, f -> sum th^2/6, so region is disc r<=sqrt(6s) in plane sum th=0.
Polar coords th_j=sqrt(2/3) r cos(phi+2 pi j/3); dth1 dth2 = r dr dphi/sqrt3 (numeric Jacobian at r=1: {jac:.6f}, 1/sqrt3={1/np.sqrt(3):.6f}).
Angular integral of prod^2 (midpoint, N={N}, spectrally exact): {ang:.8f} (pi/2={np.pi/2:.8f}).
Radial: int r^7 dr via Gauss-Legendre = {radial:.8f} (1/8).

Deterministic quadrature: c = {c:.6f}
Closed form: Delta^2 = r^6 sin^2(3 phi)/2 (cubic discriminant), so
c = (1/6)(4 pi^2)^-1 (1/sqrt3) (pi/2)(1/8) 6^4 = 9 sqrt3/(8 pi) = 27/(8 sqrt3 pi) = {cf:.6f}
Agrees with prior MC ~0.620. No failures. (Limit only; no finite-s correction check done.)

Rerun: cd to this dir; python3 control.py; python3 su3.py  (files opened with mode 'x', delete outputs to rerun)
"""
with open('result.md','x') as f: f.write(txt)
print(txt)

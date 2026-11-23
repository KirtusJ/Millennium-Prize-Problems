"""Lattice 4D massive propagator G(n), xi=16, M^2=2(cosh(1/16)-1).
G(n)=int_0^inf exp(-a M^2) Ie_n(2a) Ie_0(2a)^3 da, Ie_n(z)=exp(-z)I_n(z)
 = (1/pi) int_0^pi exp(z(cos t-1)) cos(nt) dt (periodic trapezoid, N nodes).
Beyond cutoff A: asymptotic Ie_n ~ (2 pi z)^-1/2 (1-(4n^2-1)/(8z)), integrated to A+60/M^2.
Predicates (fixed before first run):
 P1 control.txt == 1.266066
 P2 R1 at two resolutions (h=0.5,A=12000,N=2048) and (h=0.25,A=16000,N=4096) agree within 1e-6 relative
 P3 1 < R1 < 10
 P4 Ie_n integral rep check vs own series at z=2 (n=8) agrees to 1e-10
Run: python3 g4d.py   (outputs opened with mode x; delete result files to rerun)
"""
import numpy as np, math
M2=2*(math.cosh(1/16)-1)
def Ie(ns,z,N):
    t=(np.arange(N)+0.5)*math.pi/N   # midpoint rule on [0,pi], even periodic -> exponentially accurate
    C=np.cos(np.outer(t,ns))
    out=np.empty((len(z),len(ns)))
    for i in range(0,len(z),512):
        zz=z[i:i+512]
        out[i:i+512]=np.exp(np.outer(zz,np.cos(t)-1))@C/N
    return out
def series(n,z):
    s=0.0;t=(z/2)**n/math.factorial(n);k=0
    while t>1e-30*max(s,1e-300) or k<5:
        s+=t;k+=1;t*=(z/2)**2/(k*(k+n))
        if k>200:break
    return s*math.exp(-z)
def simpson(f,h):
    return h/3*(f[0]+f[-1]+4*f[1:-1:2].sum()+2*f[2:-1:2].sum())
def G(h,A,N):
    m=int(round(A/h)); m+=m%2
    a=np.arange(m+1)*h
    z=2*a
    v=Ie(np.array([0,8,16]),z,N)
    w=np.exp(-a*M2)
    res=[]
    for j,n in ((1,8),(2,16)):
        res.append(simpson(w*v[:,j]*v[:,0]**3,h))
    # tail
    B=a[-1]+60/M2; hh=2.0; mt=int(round((B-a[-1])/hh)); mt+=mt%2
    at=a[-1]+np.arange(mt+1)*hh; zt=2*at
    tails=[]
    for n in (8,16):
        asy=lambda k:(2*math.pi*zt)**-.5*(1-(4*k*k-1)/(8*zt))
        tails.append(simpson(np.exp(-at*M2)*asy(n)*asy(0)**3,hh))
    return res[0]+tails[0],res[1]+tails[1],tails
if __name__=="__main__":
    p4=abs(Ie(np.array([8]),np.array([2.0]),2048)[0,0]-series(8,2.0))
    r1=G(0.5,12000,2048); r2=G(0.25,16000,4096)
    R1a=r1[0]/r1[1]; R1b=r2[0]/r2[1]
    rel=abs(R1a-R1b)/R1b
    ctrl=open("control.txt").read().strip()
    P=[ctrl=="1.266066", rel<1e-6, 1<R1b<10, p4<1e-10]
    txt=f"""# Result
R1 = G(8)/G(16) = {R1b:.10f}  (fine resolution)
- Res A (h=0.5, A=12000, N=2048): G(8)={r1[0]:.12e} G(16)={r1[1]:.12e} R1={R1a:.10f}
- Res B (h=0.25, A=16000, N=4096): G(8)={r2[0]:.12e} G(16)={r2[1]:.12e} R1={R1b:.10f}
- Tail contributions (res B, n=8,16): {r2[2][0]:.3e}, {r2[2][1]:.3e}
- Relative difference: {rel:.3e}; stated tolerance 1e-6 relative
- M^2 = {M2:.12e}
- Control I_0(1) = {ctrl}
Rerun: cd /home/user/z4-workers/a3-C/child/grandchild && python3 g4d.py (remove result.md first; mode x)
Predicates P1 control, P2 two-res<1e-6, P3 1<R1<10, P4 Bessel rep check ({p4:.2e}): {P}
Failed predicates: {[f"P{i+1}" for i,p in enumerate(P) if not p] or "none"}
"""
    with open("result.md","x") as f: f.write(txt)
    print(txt)

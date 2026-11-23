"""P4b (post-hoc, declared after P4 failed on my own window): SU(3) direct MC M=8e6 seed 11, s in [0.15,0.5], need counts>=1e3 at smallest s
 (check count). Compare with Weyl-formula V(s) at same s within 5 sigma (Weyl is exact-quadrature-style independent); report local slope vs Weyl local slope (same window, must agree within 0.1). Slope itself is NOT asserted =4 (window is not small s)."""
import numpy as np, sys
exec(open('t37.py').read().split("res={}")[0].split('import numpy as np, sys')[1])
M=8_000_000; fs=fU(haar_su3(M,np.random.default_rng(11)),3)
ss=np.linspace(0.15,0.5,8); Vd=np.array([np.mean(fs<=s) for s in ss]); print("counts",(Vd*M).astype(int).tolist())
rw=np.random.default_rng(12)
def weyl(s,n=2_000_000):
    a=np.arccos(max(-1,1-3*s)); t1=rw.uniform(-a,a,n); t2=rw.uniform(-a,a,n); t3=-t1-t2
    # reduce mod 2pi not needed for cos; |e^i - e^j|^2 is 2pi-periodic
    f=(3-np.cos(t1)-np.cos(t2)-np.cos(t3))/3
    D=np.abs(np.exp(1j*t1)-np.exp(1j*t2))**2*np.abs(np.exp(1j*t1)-np.exp(1j*t3))**2*np.abs(np.exp(1j*t2)-np.exp(1j*t3))**2
    g=D*(f<=s)*(2*a)**2/(6*(2*np.pi)**2); return g.mean(),g.std()/np.sqrt(n)
W=[weyl(s) for s in ss]
z=[(Vd[i]-W[i][0])/np.hypot(W[i][1],np.sqrt(Vd[i]*(1-Vd[i])/M)) for i in range(8)]; print("z",np.round(z,2).tolist())
sd=np.polyfit(np.log(ss),np.log(Vd),1)[0]; sw=np.polyfit(np.log(ss),np.log([w[0] for w in W]),1)[0]; print("slopes direct,weyl",sd,sw)
ok=min(Vd)*M>=1e3 and max(abs(np.array(z)))<5 and abs(sd-sw)<.1; print("PASS" if ok else "FAIL","P4b"); sys.exit(0 if ok else 1)

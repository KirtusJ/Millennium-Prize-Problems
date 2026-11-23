"""Compute C for lattice a(k) kernel, position-space FFT, with momentum-space cross-check.
Predicates (fixed before first run):
 P1 position-space C vs momentum-space C (FFT self-convolution of a, sum |fhat|^2 A2) agree rel 1e-10 at N=48
    (tolerance: double-precision roundoff over ~1e5 terms is ~1e-13; 1e-10 leaves margin).
 P2 same agreement at N=8 (rel 1e-10).
 P3 max|Im D| <= 1e-12*max|D| (a is even in k, so D must be real).
 P4 a(0)==0 and C>0.
 Ratio C*s^2.5/(b^3 sum f^2) is MEASURED ONLY (no expected value).
Result file results.json opened with mode 'x'.  No randomness used.
"""
import numpy as np, json, sys
def setup(N, t=0.0, s=0.005):
    l=1.0;b=l/N
    n=np.fft.fftfreq(N,1.0/N)           # integers, FFT order, in -N/2..N/2-1 (N/2 equiv to -N/2 for khat)
    kh1=(2/b)*np.sin(np.pi*n/N)         # k b/2 = pi n / N
    K1,K2,K3=np.meshgrid(kh1,kh1,kh1,indexing='ij')
    k2=K1**2+K2**2+K3**2; kh=np.sqrt(k2)
    with np.errstate(invalid='ignore',divide='ignore'):
        a=(K1**2+K2**2)/k2*(kh/2)*np.exp(-t*kh)*np.exp(-2*s*k2)
    a[0,0,0]=0.0
    u=np.arange(N)*b
    g=sum(np.exp(-(u-0.3-m)**2/(2*0.15**2)) for m in range(-2,3))
    f=g[:,None,None]*g[None,:,None]*g[None,None,:]
    return N,b,a,f
def pos_C(N,b,a,f):
    D=np.fft.ifftn(a)*N**3              # l^-3 sum_k e^{ik.bx} a(k)
    imx=np.abs(D.imag).max()/np.abs(D.real).max()
    D=D.real
    F=np.fft.fftn(f)
    corr=np.fft.ifftn(np.abs(F)**2).real   # sum_x f(x) f(x-z)
    return 2*b**6*np.sum(D**2*corr), imx
def mom_C(N,b,a,f):
    A=np.fft.fftn(a); A2=np.fft.ifftn(A*A).real   # sum_k a(k)a(q-k)
    fh2=(b**3*np.abs(np.fft.fftn(f)))**2
    return 2*np.sum(fh2*A2)
def run(N,s=0.005):
    N,b,a,f=setup(N,0.0,s)
    c1,imx=pos_C(N,b,a,f); c2=mom_C(N,b,a,f)
    return dict(N=N,C_pos=c1,C_mom=c2,rel=abs(c1-c2)/abs(c1),imagD_rel=imx,
                a0=float(a[0,0,0]),intf2=float(b**3*np.sum(f**2)),s=s)
if __name__=="__main__":
    out={}
    for N in (8,48): out[N]=run(N)
    r=out[48]; r['ratio']=r['C_pos']*r['s']**2.5/r['intf2']
    P={'P1':bool(out[48]['rel']<1e-10),'P2':bool(out[8]['rel']<1e-10),'P3':bool(out[48]['imagD_rel']<=1e-12),
       'P4':bool(out[48]['a0']==0 and out[48]['C_pos']>0)}
    out['predicates']=P
    with open('results_v2.json','x') as fh: json.dump(out,fh,indent=1)
    print(json.dumps(out,indent=1))
    sys.exit(0 if all(P.values()) else 1)

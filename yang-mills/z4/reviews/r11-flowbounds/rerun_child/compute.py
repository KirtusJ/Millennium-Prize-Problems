"""PCP child run1: C(0), M1/M0 on lattice, s=0.005, l=1.
Predicates (fixed before first run):
 P1 position-space vs momentum-space (cyclic autoconvolution of a, with |fhat|^2) agree, C0 and M1, rel diff < 1e-10
    (double precision, sums of <=1e5 terms of O(1..1e3) magnitude => roundoff ~1e-13; 1e-10 is generous).
 P2 N=16 brute-force double sum over k,k' (4095^2 pairs, no FFT convolution) agrees with P1 momentum value rel < 1e-10.
 P3 control: min nonzero khat at N=16 equals 32 sin(pi/16) within 1e-12.
 P4 C0>0, M0>0, M1>0 and finite (a>=0 so must hold).
 P5 f is Z-periodic and positive (trivially true by construction; measured).
No randomness (no seed needed; set numpy seed 0 anyway).
"""
import numpy as np, json, sys
np.random.seed(0)
l=1.0; s=0.005
def setup(N):
    b=l/N
    n=np.fft.fftfreq(N,1.0/N)  # integers; N/2 appears as -N/2, sin^2 identical (even fn)
    kh1=(2/b)*np.sin(np.pi*n/N)
    KX,KY,KZ=np.meshgrid(kh1,kh1,kh1,indexing='ij')
    kh2=KX**2+KY**2+KZ**2; kh=np.sqrt(kh2)
    kh2s=np.where(kh2==0,1,kh2)
    a=np.where(kh2==0,0.0,(KX**2+KY**2)/kh2s*kh/2*np.exp(-2*s*kh2))
    y=(np.arange(N)/N)
    Y1,Y2,Y3=np.meshgrid(y,y,y,indexing='ij')
    f=np.exp(0.8*np.cos(2*np.pi*Y1)+0.3*np.sin(4*np.pi*Y1)+0.6*np.cos(2*np.pi*Y2-0.4)+0.5*np.sin(2*np.pi*Y3)+0.3*np.cos(2*np.pi*(Y1-Y3)))
    return b,kh,a,f
def pos(N):
    b,kh,a,f=setup(N)
    D0=np.fft.ifft2(np.fft.ifftn(a)) if False else np.fft.ifftn(a).real*N**3/l**3
    D1=np.fft.ifftn(a*kh).real*N**3/l**3
    def S(G):  # sum_{x,y} f(x)f(y)G(x-y)
        return np.sum(f*np.fft.ifftn(np.fft.fftn(f)*np.fft.fftn(G)).real)  # sum_y G(x-y) f(y)
    C0=2*b**6*S(D0*D0); M1=2*b**6*S(2*D0*D1)
    return C0,M1
def mom(N):
    b,kh,a,f=setup(N)
    fh=b**3*np.fft.fftn(f)   # sum f e^{-i q b x}
    ac=np.fft.ifftn(np.fft.fftn(a)**2).real      # sum_{k+k'=q} a a'
    akc=np.fft.ifftn(2*np.fft.fftn(a)*np.fft.fftn(a*kh)).real  # sum a a' (kh+kh')
    w=np.abs(fh)**2
    return 2/l**6*np.sum(w*ac),2/l**6*np.sum(w*akc)
def brute(N):
    b,kh,a,f=setup(N)
    fh=b**3*np.fft.fftn(f)
    idx=np.array(np.meshgrid(*[np.arange(N)]*3,indexing='ij')).reshape(3,-1)
    m=a.ravel()>0; I=idx[:,m]; av=a.ravel()[m]; kv=kh.ravel()[m]
    C0=M1=0.0
    for j in range(I.shape[1]):
        q=(I[:,j:j+1]+I)%N
        w=np.abs(fh[q[0],q[1],q[2]])**2
        C0+=av[j]*np.sum(w*av); M1+=av[j]*np.sum(w*av*(kv[j]+kv))
    return 2/l**6*C0,2/l**6*M1
if __name__=="__main__":
    res={}; log=[]
    def chk(name,ok,meas): log.append((name,bool(ok),meas)); print(name,"PASS" if ok else "FAIL",meas)
    b,kh,a,f=setup(16)
    chk("P3",abs(kh[kh>0].min()-32*np.sin(np.pi/16))<1e-12,float(kh[kh>0].min()))
    chk("P5",f.min()>0,float(f.min()))
    for N in (16,32):
        C0,M1=pos(N); c0,m1=mom(N)
        d0=abs(C0-c0)/abs(C0); d1=abs(M1-m1)/abs(M1)
        chk(f"P1_N{N}",d0<1e-10 and d1<1e-10,[d0,d1])
        chk(f"P4_N{N}",np.isfinite([C0,M1]).all() and C0>0 and M1>0,[C0,M1])
        res[N]={"C0":C0,"M1_over_M0":M1/C0,"M1":M1,"C0_mom":c0,"M1_mom":m1}
    bc,bm=brute(16)
    chk("P2",abs(bc-res[16]["C0_mom"])/bc<1e-10 and abs(bm-res[16]["M1_mom"])/bm<1e-10,[bc,bm])
    for N in res: print(N,"C0=%.10g M1/M0=%.10g"%(res[N]["C0"],res[N]["M1_over_M0"]))
    with open("results_child_run1.json","x") as fo:
        json.dump({"s":s,"l":l,"results":{str(k):v for k,v in res.items()},"predicates":log},fo,indent=1)

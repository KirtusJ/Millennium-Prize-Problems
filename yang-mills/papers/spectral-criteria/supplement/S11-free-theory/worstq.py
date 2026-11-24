"""gamma at single coarse momenta for large N (same formulas as maxwell.py; imports its functions by exec).
Reports 1-rho^2 for q=(1,0,0),(1,1,0),(1,1,1),(0,0,0) and N up to 4096; also N=64 full minimum if 'full' given."""
import sys, numpy as np, itertools
src=open('maxwell.py').read(); exec(src[:src.index("def wmin")].replace('import sys, numpy as np, itertools',''))
def fib(N,q):
    S0=np.zeros((24,24),complex); S1=np.zeros((24,24),complex); K=np.zeros((3,24),complex)
    for a,n in enumerate(itertools.product((0,1),repeat=3)):
        p=[2*np.pi*(q[i]+n[i]*N//2)/N for i in range(3)]
        if all(abs(np.sin(x/2))<1e-12 for x in p): continue
        w=omega(p); M=Mmat(p); c=1/(2*np.sinh(w)); sl=slice(3*a,3*a+3)
        S0[sl,sl]=M*c; S1[sl,sl]=M*c*np.exp(-w)
        for r,(i,j) in enumerate(PL): K[r,3*a+r]=(1+np.exp(1j*p[i]))*(1+np.exp(1j*p[j]))
    C0=K@S0@K.conj().T; G=pinv_h(C0); KS0=K@S0; KS1=K@S1
    return 1-topcc(S0-KS0.conj().T@G@KS0, S1-KS0.conj().T@G@KS1, S0-KS1.conj().T@G@KS1)
for N in [16,32,64,128,256,1024,4096]:
    print(N, ["%.5f"%fib(N,q) for q in [(1,0,0),(1,1,0),(1,1,1),(0,0,0),(2,0,0)]])

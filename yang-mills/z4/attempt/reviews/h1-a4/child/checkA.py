"""Statement A. Predicates fixed before first run:
 PA1 (grid): for each (n,beta), n=8..4000 all integers, beta = 64 log-spaced pts 1..1e4,
     D = log(I_n/I_1) + (n/8)*log(1+n/beta) <= tol, tol = 1e-12*max(1,|(n/8)log(1+n/beta)|)
     (1e-12 relative on logs; double rounding of ~n summed logs).
 PA2: recurrence self-test (control): ratio I_1/I_0 at beta=1 must be 0.4463899658965 (known 0.446389965896...)
     and log(I_2/I_1) at beta=2 must equal log(0.6889484476987/1.590636854637)=... via known I_1(2)=1.5906368546, I_2(2)=0.6889484477.
 Reported: max D and argmax, min slack = min(-D), number of cases met/failed.
No scipy available -> own ratio recurrence (see notes)."""
import math, numpy as np
def logratios(beta, nmax):
    N = int(nmax + beta + 60*math.sqrt(beta) + 500)
    r = [0.0]*(N+2); rk1 = 0.0
    for k in range(N, 1, -1):
        rk1 = 1.0/(2*k/beta + rk1); r[k] = rk1
    return r  # r[k]=I_k/I_{k-1}, k>=2
def ctl():
    r=logratios(2.0,10); ok=abs(r[2]-0.6889484476987/1.5906368546373)<1e-10
    print("control I2/I1 at beta=2:",r[2],ok); return ok
if __name__=="__main__":
    assert ctl()
    betas=np.logspace(0,4,64)
    worst=(-1e300,None); minslack=(1e300,None); met=fail=0; failcases=[]
    for b in betas:
        b=float(b); r=logratios(b,4000); acc=0.0; terms=[]
        # cumulative sums via fsum prefix (exactness: use running fsum of list)
        lst=[]
        for n in range(2,4001):
            lst.append(math.log(r[n]))
            if n>=8:
                L=math.fsum(lst); B=-(n/8)*math.log1p(n/b)
                D=L-B; tol=1e-12*max(1,abs(B))
                if D>worst[0]: worst=(D,(n,b,L,B))
                if -D<minslack[0]: minslack=(-D,(n,b))
                if D<=tol: met+=1
                else: fail+=1; failcases.append((n,b,D))
    print("cases",met+fail,"met",met,"failed",fail)
    print("max D",worst); print("min slack",minslack); print(failcases[:10])

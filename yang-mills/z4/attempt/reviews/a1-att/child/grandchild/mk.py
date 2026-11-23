import math
def I(n,x):
    # scaled Bessel via series in log-safe form
    s=0.0;t=(x/2)**n/math.factorial(n);k=0
    # use exp scaling to avoid overflow for large x: use asymptotic-safe ratio via recurrence below
    return None
def ratio(x):
    # I1/I0 via continued fraction (Perron/Gauss): r_n=I_{n+1}/I_n = 1/(2(n+1)/x + r_{n+1}); backward from N
    N=int(x)+200
    r=0.0
    for n in range(N,-1,-1):
        r=1.0/(2*(n+1)/x+r)
    return r
def inv(c):
    lo,hi=1e-12,1e7
    for _ in range(300):
        m=math.sqrt(lo*hi) if lo>0 else (lo+hi)/2
        if ratio(m)<c: lo=m
        else: hi=m
    return lo
def step_wilson(b,d=4,B=2):
    c=ratio(b**(d-2)*B)**(B**0*b**2/b**(d-2)*1)  # placeholder replaced below
    return c
def step(beta,b=2,d=4):
    x=b**(d-2)*beta
    c1=ratio(x)**(b*b)   # decimation exponent b^2 (see notes)
    return inv(c1)
def step_villain(beta,b=2,d=4):
    return 1/(b**(4-d)/beta)
if __name__=="__main__":
    print("control",ratio(1.0))
    out=[]
    for b0 in [0.5,1,2,5,10,50]:
        be=b0;tr=[be]
        for n in range(30):
            be=step(be); tr.append(be)
            if be<1e-9 or be>1e5: break
        out.append((b0,tr))
        print("beta0=%g villain:%g"%(b0,step_villain(b0)),"wilson traj:",[float('%.5g'%v) for v in tr[:12]],"...",'%.5g'%tr[-1],"steps",len(tr)-1)
    with open('result.txt','x') as f:
        for b0,tr in out: f.write("beta0=%g: %s\n"%(b0," ".join('%.6g'%v for v in tr)))

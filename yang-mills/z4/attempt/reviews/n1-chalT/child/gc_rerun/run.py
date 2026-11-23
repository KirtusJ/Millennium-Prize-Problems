from decimal import Decimal as D, getcontext
getcontext().prec = 90
def atan_inv(n):
    x=D(1)/n; t=x; s=x; k=1; n2=n*n
    while abs(t)>D(10)**-95:
        t=-t/n2; k+=2; s+=t/k
    return s
PI = 4*(4*atan_inv(5)-atan_inv(239))
def sin(x):
    t=x; s=x; k=1
    while abs(t)>D(10)**-95:
        t=-t*x*x/((k+1)*(k+2)); k+=2; s+=t
    return s
def asinh(y): return (y+(y*y+1).sqrt()).ln()
def matsq(A):
    n=len(A); cols=list(zip(*A))
    return [[sum(map(D.__mul__,r,c)) for c in cols] for r in A]
def topeig(A, nsq=60, extra=5):
    n=len(A)
    for _ in range(nsq):
        A=matsq(A); m=max(max(r) for r in A); A=[[x/m for x in r] for r in A]
    # A ~ rank one; but eigenvalue of original needs power-of-2^k ratio; use Rayleigh with ORIGINAL via dominant column
    return A
def rayleigh(A0, P):
    n=len(A0)
    j=max(range(n), key=lambda j: sum(P[i][j]**2 for i in range(n)))
    v=[P[i][j] for i in range(n)]
    Av=[sum(map(D.__mul__,A0[i],v)) for i in range(n)]
    return sum(map(D.__mul__,v,Av))/sum(x*x for x in v)
def lam(A0, nsq=60, extra=5):
    P=A0; 
    for _ in range(nsq):
        P=matsq(P); m=max(max(r) for r in P); P=[[x/m for x in r] for r in P]
    l1=rayleigh(A0,P)
    for _ in range(extra):
        P=matsq(P); m=max(max(r) for r in P); P=[[x/m for x in r] for r in P]
    l2=rayleigh(A0,P)
    return l2, abs(l2-l1)
f=lambda x: format(x,'.30f') if abs(x)>=1e-3 else format(x,'.30e')
# control
c,d=lam([[D(2),D(1)],[D(1),D(2)]])
err=abs(c-3)
open("control.txt","x").write(f"top eig [[2,1],[1,2]] = {c}\nerror vs 3 = {err:.3E}\nconv change={d:.3E}\n{'PASS' if err<D(10)**-30 else 'FAIL'}\n")
beta=D(64); n=63; h=(PI/2)/n
pref=(beta/(2*PI)).sqrt()
def K(x): return pref*sum((-beta*(x+2*PI*k)**2/2).exp() for k in range(-2,3))
a=[(i+D(1)/2)*h for i in range(n)]
w=[(-(2*asinh(sin(x)))/2).exp() for x in a]
S=[[h*w[i]*w[j]*(K(a[i]-a[j])+K(a[i]+a[j])) for j in range(n)] for i in range(n)]
B=[[h*w[i]*w[j]*(K(a[i]+a[j]-PI)+K(a[i]-a[j]-PI)) for j in range(n)] for i in range(n)]
Ae=[[S[i][j]+B[i][j] for j in range(n)] for i in range(n)]
Ao=[[S[i][j]-B[i][j] for j in range(n)] for i in range(n)]
le,de=lam(Ae); lo,do=lam(Ao)
m=(le/lo).ln(); ml=m.ln()
out=f"""lam_e = {le:.30E}
lam_o = {lo:.30E}
conv change (60->65 sq): e {de:.3E}  o {do:.3E}
m = ln(lam_e/lam_o) = {m:.30E}
log(m) = {ml:.30f}
-log(m)/sqrt(beta) = {-ml/beta.sqrt():.30f}
control: {'PASS' if err<D(10)**-30 else 'FAIL'}
"""
open("results.txt","x").write(out); print(out)

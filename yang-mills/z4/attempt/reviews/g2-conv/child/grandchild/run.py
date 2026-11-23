import numpy as np, math
beta=16.0
def I(n,x):
    t=(x/2)**n/math.factorial(n); s=t; k=0
    while True:
        k+=1; t*=(x/2)**2/(k*(k+n)); s+=t
        if t<1e-18*s: break
    return s
with open('control.txt','x') as f: f.write("%.6f\n"%(-math.log(I(3,16.)/I(1,16.))))
NA,NT,N=80,40,12
x,w=np.polynomial.legendre.leggauss(NA); a=(x+1)*np.pi/2; wa=w*np.pi/2
xt,wt=np.polynomial.legendre.leggauss(NT)
def gegen(m,lam,c):
    if m==0: return np.ones_like(c)
    p0=np.ones_like(c); p1=2*lam*c
    for k in range(2,m+1):
        p0,p1=p1,(2*c*(k+lam-1)*p1-(k+2*lam-2)*p0)/k
    return p1
F={}
for L in range(0,N+1):
    for n in range(L,N+1):
        if n%2: continue
        f=np.sin(a)**L*gegen(n-L,L+1,np.cos(a))
        nr=np.sum(f*f*(2/np.pi)*np.sin(a)**2*wa); F[(n,L)]=f/np.sqrt(nr)
Pl=[np.polynomial.legendre.Legendre.basis(L)(xt)*np.sqrt(2*L+1) for L in range(N+1)]
states=[(n1,n2,L) for n1 in range(0,N+1,2) for n2 in range(0,N+1,2) for L in range(min(n1,n2)+1)]
D=len(states); print(D)
kap=lambda n: I(n+1,beta)/I(1,beta)
G=np.zeros((D,D))
wA=(2/np.pi)*np.sin(a)**2*wa
for i in range(NA):
    # grid over a2,t
    A2,T=np.meshgrid(np.arange(NA),np.arange(NT),indexing='ij')
    A2=A2.ravel();T=T.ravel()
    W=wA[i]*wA[A2]*wt[T]/2
    Vv=2*beta*np.sin(a[i])**2*np.sin(a[A2])**2*(1-xt[T]**2)
    B=np.empty((len(W),D))
    for j,(n1,n2,L) in enumerate(states):
        B[:,j]=F[(n1,L)][i]*F[(n2,L)][A2]*Pl[L][T]
    G+=B.T@(B*(W*Vv)[:,None])
kk=np.array([kap(s[0])*kap(s[1]) for s in states])
H=np.eye(D)-np.diag(kk)+G
H=(H+H.T)/2
Lv=np.array([s[2] for s in states])
S=np.linalg.eigvalsh(H)[0]
ev=Lv%2==0
E=np.linalg.eigvalsh(H[np.ix_(ev,ev)])[0]
O=np.linalg.eigvalsh(H[np.ix_(~ev,~ev)])[0]
# coupling check: L parity block-diagonal?
off=np.abs(H[np.ix_(ev,~ev)]).max()
out="dim %d\nall %.6f\nLeven %.6f\nLodd %.6f\nmax|even-odd coupling| %.2e\n"%(D,S,E,O,off)
print(out)
with open('result.txt','x') as f: f.write(out)

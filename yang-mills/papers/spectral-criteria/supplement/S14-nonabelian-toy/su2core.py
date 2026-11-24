import numpy as np, itertools, functools
from math import factorial, sqrt
from scipy.linalg import expm
def tw(j): return int(round(2*j))
@functools.lru_cache(maxsize=None)
def cg(j1,m1,j2,m2,J,M):
    """<j1 m1 j2 m2 | J M>, Condon-Shortley"""
    if abs(m1+m2-M)>1e-9 or J<abs(j1-j2)-1e-9 or J>j1+j2+1e-9 or abs(M)>J+1e-9: return 0.0
    f=lambda x: factorial(int(round(x)))
    pre=sqrt((2*J+1)*f(J+j1-j2)*f(J-j1+j2)*f(j1+j2-J)/f(j1+j2+J+1))
    pre*=sqrt(f(J+M)*f(J-M)*f(j1-m1)*f(j1+m1)*f(j2-m2)*f(j2+m2))
    s=0.0
    for k in range(0,int(round(j1+j2-J))+1):
        d=[k,j1+j2-J-k,j1-m1-k,j2+m2-k,J-j2+m1+k,J-j1-m2+k]
        if min(d)<-1e-9: continue
        s+=(-1)**k/np.prod([float(f(x)) for x in d])
    return pre*s
def ms(j): return [j-k for k in range(tw(j)+1)]          # m = j, j-1, ..., -j
def gens(j):
    m=np.array(ms(j)); n=len(m); Jz=np.diag(m).astype(complex); Jp=np.zeros((n,n),complex)
    for i in range(1,n): Jp[i-1,i]=sqrt(j*(j+1)-m[i]*(m[i]+1))
    return Jz,Jp,Jp.conj().T
def Dmat(j,g):
    """Wigner D^j(g) for g in SU(2) (2x2), with D^{1/2}(g) = g"""
    w,V=np.linalg.eig(g); H=V@np.diag(np.log(w))@np.linalg.inv(V)      # g = exp(H), H = -i theta n.sigma/2
    Jz,Jp,Jm=gens(j); Jx=(Jp+Jm)/2; Jy=(Jp-Jm)/(2j)
    sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex)
    cx,cy,cz=[np.trace(H@s)/1 for s in (sx,sy,sz)]        # H = (cx sx + cy sy + cz sz)/2
    return expm(cx*Jx+cy*Jy+cz*Jz)
@functools.lru_cache(maxsize=None)
def Lmat(j,jp,mu):
    """matrix [M, m] = <1/2 mu ; j m | jp M>"""
    A=np.zeros((tw(jp)+1,tw(j)+1))
    for a,M in enumerate(ms(jp)):
        for b,m in enumerate(ms(j)): A[a,b]=cg(0.5,mu,j,m,jp,M)
    return A

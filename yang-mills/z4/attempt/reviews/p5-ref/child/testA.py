"""Test A. Predicates fixed BEFORE first run (tolerances and their source in brackets).
Quadrature: k=rho*pi*(s,t,1) on each of 3 cube-pyramids (permutations), s,t in [0,1] (x8 sign symmetry, x3 pyramids
via explicit permutation), rho in [0,1] geometric panels (ratio 2 down to 2^-16) Gauss-Legendre. Resolution R1=(nGL 16 ang,10 rad),
R2=(24 ang,14 rad). Quadrature error estimate Eq = |G_R2 - G_R1| per n. Tol for claims = max(Eq, 1e-13) + claim rounding.
A1: (a) pointwise: 3-d residue integrand == k0-trapezoid (M=2000) of (k1h^2+k2h^2)/khat^2 cos(k0 n), n=0,1,3, 2000 random k3vec,
    max abs diff < 1e-11 [trapezoid exp. convergent; double rounding].  (b) 4-d midpoint grid N=40 vs 3-d for n=0,1: |diff|<1e-3
    [conical singularity at 0: grid error ~ change between N=24 and N=40, checked].
A2: |G(0)-1/2| < 10*Eq+1e-10.
A3: |G(1)-0.0688747| < 5e-8+Eq [claim has 7 decimals: rounding 5e-8].
A4: G(n)>0 and G(n+1)<G(n) for n=0..15 (count of qualifying n reported, 16 cases), with margins > Eq.
A5: pi^2*8^4*G(8) within 5e-4 of 1.092 [3 decimals]; limit 1: fit pi^2 n^4 G = c0 + c2/n^2 + c4/n^4 on n=8..20, |c0-1|<5e-3 [fixed here].
A6: v_n = n^6|G(n)-1/(pi^2 n^4)|, n=2..20: PASS if max(v_11..20) <= 1.5*max(v_2..10) and all v_n <= 14400/pi^2 (the A7 constant).
A7: LHS<=RHS for n=1..20 (count reported), margin > -Eq.
A8: 400000 random points in ball |k|<=1 (seed 12345, plus 100000 log-radius points down to 1e-6): max |g-g0|/|k|^3 <= 3.
"""
import numpy as np, json, sys, math
tag=sys.argv[1]
pi=math.pi
def nodes(nang,nrad):
    xa,wa=np.polynomial.legendre.leggauss(nang); xa=(xa+1)/2; wa=wa/2
    xr,wr=np.polynomial.legendre.leggauss(nrad); xr=(xr+1)/2; wr=wr/2
    edges=[2.0**(-j) for j in range(0,17)]+[0.0]
    R=[];W=[]
    for a,b in zip(edges[1:],edges[:-1]):
        R.append(a+(b-a)*xr); W.append((b-a)*wr)
    return xa,wa,np.concatenate(R),np.concatenate(W)
def gfun(k1,k2,k3):
    h=lambda k:4*np.sin(k/2)**2
    a=h(k1)+h(k2)+h(k3)
    m=2*np.arcsinh(np.sqrt(a)/2)
    sh=np.sqrt(a+a*a/4)
    return (h(k1)+h(k2))/(2*sh), m
def Gs(nmax,nang,nrad):
    xa,wa,R,W=nodes(nang,nrad)
    S,T=np.meshgrid(xa,xa,indexing='ij'); WS=np.outer(wa,wa)
    out=np.zeros(nmax+1)
    for rho,w in zip(R,W):
        c=rho*pi
        u=[c*S,c*T,c*np.ones_like(S)]
        for perm in [(0,1,2),(1,2,0),(2,0,1)]:
            k=[u[perm[0]],u[perm[1]],u[perm[2]]]  # permutation of coordinates
            g,m=gfun(*k)
            base=g*WS*w*rho**2*pi**3*8/(2*pi)**3
            for n in range(nmax+1):
                out[n]+=np.sum(base*np.exp(-m*n))
    return out
def Gs_fast(nmax,nang,nrad):
    return Gs(nmax,nang,nrad)
res={}
G1=Gs(20,16,10); G2=Gs(20,24,14)
Eq=np.abs(G2-G1); G=G2
res['G']=G.tolist(); res['Eq']=Eq.tolist()
out=[]
def rec(name,ok,info): out.append((name,bool(ok),info)); print(name,'PASS' if ok else 'FAIL',info,flush=True)
# A1
rng=np.random.default_rng(12345)
kk=rng.uniform(-pi,pi,(2000,3)); h=lambda k:4*np.sin(k/2)**2
M=2000; k0=(np.arange(M)+0.5)*2*pi/M-pi
mx=0
for n in (0,1,3):
    g,m=gfun(kk[:,0],kk[:,1],kk[:,2])
    a=h(kk[:,0])+h(kk[:,1])+h(kk[:,2])
    lhs=((h(kk[:,0])+h(kk[:,1]))[:,None]/(a[:,None]+h(k0)[None,:])*np.cos(k0*n)[None,:]).mean(1)
    rhs=g*np.exp(-m*n)
    mx=max(mx,np.abs(lhs-rhs).max())
rec('A1a',mx<1e-11,f'max pointwise diff {mx:.3e}')
def G4(N):
    k=(np.arange(N)+0.5)*2*pi/N-pi; hk=h(k)
    H=hk[:,None,None,None]*0
    s0=hk[:,None,None,None]; s1=hk[None,:,None,None]; s2=hk[None,None,:,None]; s3=hk[None,None,None,:]
    tot=s0+s1+s2+s3
    r=[]
    for n in (0,1):
        r.append((((s1+s2)/tot)*np.cos(k*n)[:,None,None,None]).mean())
    return r
r24=G4(24); r40=G4(40)
d=[abs(r40[0]-G[0]),abs(r40[1]-G[1])]
rec('A1b',max(d)<1e-3,f'4d N=40: G0={r40[0]:.6f} G1={r40[1]:.6f}; N=24: {r24[0]:.6f},{r24[1]:.6f}; 3d: {G[0]:.8f},{G[1]:.8f}; diffs {d[0]:.2e},{d[1]:.2e}')
rec('A2',abs(G[0]-.5)<10*Eq[0]+1e-10,f'G(0)={G[0]:.12f} Eq={Eq[0]:.2e}')
rec('A3',abs(G[1]-0.0688747)<5e-8+Eq[1],f'G(1)={G[1]:.10f} Eq={Eq[1]:.2e}')
cnt=sum(1 for n in range(16) if G[n]>0 and G[n]-G[n+1]>Eq[n]+Eq[n+1])
rec('A4',cnt==16,f'{cnt}/16 n qualify; G(0..20)={[float(f"{x:.6e}") for x in G]}')
q=pi**2*np.arange(21)**4*G
ns=np.arange(8,21); Amat=np.vstack([np.ones_like(ns),1/ns**2,1/ns**4]).T.astype(float)
co=np.linalg.lstsq(Amat,q[8:21],rcond=None)[0]
rec('A5a',abs(q[8]-1.092)<5e-4,f'pi^2 8^4 G(8)={q[8]:.6f}')
rec('A5b',abs(co[0]-1)<5e-3,f'fit c0={co[0]:.5f} c2={co[1]:.4f} c4={co[2]:.3f}; pi^2 n^4 G(n) n=1..20: {[round(float(x),5) for x in q[1:]]}')
v=np.array([n**6*abs(G[n]-1/(pi**2*n**4)) for n in range(1,21)])
errv=np.array([n**6*(Eq[n]) for n in range(1,21)])
ok=v[10:20].max()<=1.5*v[1:10].max() and v[1:20].max()<=14400/pi**2
rec('A6',ok,f'v_n n=2..20={[round(float(x),5) for x in v[1:]]}; quad-err on v={[float(f"{x:.1e}") for x in errv[1:]]}')
m1=math.acosh(1+2/pi**2)
cnt=0;marg=[]
for n in range(1,21):
    I=math.exp(-n)*(1/n+3/n**2+6/n**3+6/n**4)
    rhs=14400/(pi**2*n**6)+0.5*math.exp(-m1*n)+I/(6*pi**2)
    lhs=abs(G[n]-1/(pi**2*n**4))
    if lhs<=rhs+Eq[n]: cnt+=1
    marg.append(rhs/lhs if lhs>0 else float('inf'))
rec('A7',cnt==20,f'{cnt}/20 hold; rhs/lhs n=1..20 {[round(x,2) for x in marg]}')
rng=np.random.default_rng(12345)
pts=rng.normal(size=(400000,3)); pts/=np.linalg.norm(pts,axis=1)[:,None]
rad=rng.uniform(0,1,400000)**(1/3); P1=pts*rad[:,None]
pts=rng.normal(size=(100000,3)); pts/=np.linalg.norm(pts,axis=1)[:,None]
rad=10**rng.uniform(-6,0,100000); P2=pts*rad[:,None]
P=np.vstack([P1,P2]); nk=np.linalg.norm(P,axis=1)
g,_=gfun(P[:,0],P[:,1],P[:,2]); g0=(P[:,0]**2+P[:,1]**2)/(2*nk)
ratio=np.abs(g-g0)/nk**3
rec('A8',ratio.max()<=3,f'max ratio {ratio.max():.4f} (limit 3), at |k|={nk[ratio.argmax()]:.3g}; 500000 pts')
res['claims']=out
with open(f'results/A_{tag}.json','x') as f: json.dump(res,f,indent=1)
sys.exit(0 if all(o[1] for o in out) else 1)

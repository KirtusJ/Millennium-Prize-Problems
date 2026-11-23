"""xquad.py -- reference numbers by direct 6-D tensor quadrature over SU(2)^3 / conjugation (independent of basis code).
Z3(beta) = int e^{-V} dU1dU2dU3, X3(beta) = int chi_1(U1) chi_1(U2) e^{-V}, V = beta sum_{i<j} (1 - 1/2 Tr comm(U_i,U_j)).
Coordinates: U = cos a + i sin a n.sigma, Haar (2/pi) sin^2 a da dOmega/4pi; n1=z, n2 in xz plane, n3 general.
1/2 Tr comm = 1 - 2 s_i^2 s_j^2 (1-(n_i.n_j)^2)  (D2 of NUMERICS_2DIR; re-checked here vs explicit 2x2 matrices, predicate Q0).
Rules: Gauss-Chebyshev-U in a (M nodes), Gauss-Legendre in cos theta (M), trapezoid in phi (2M).
PREDICATES (fixed before first run):
 Q0 explicit-matrix commutator formula agrees with the invariant formula at 200 random points to 1e-13 (seed 7).
 Q1 beta=0: Z3 = 1 and X3 = 0 to 1e-13 (orthogonality of characters; exact polynomial integrands).
 Q2 Z3, X3 at beta=1,2 change by < 1e-10 between M=16 and M=24 (tolerance: integrand entire, exponential convergence;
    1e-10 is far above double rounding of sums of ~1e8 terms ~1e-13).
Usage: python3 xquad.py OUTFILE
"""
import sys, json, numpy as np
rng = np.random.default_rng(7)
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex)
def U(a,n): return np.cos(a)*np.eye(2)+1j*np.sin(a)*(n[0]*sx+n[1]*sy+n[2]*sz)
res={}; ok=True
err=0
for _ in range(200):
    a=rng.uniform(0,np.pi,2); n=rng.normal(size=(2,3)); n/= np.linalg.norm(n,axis=1)[:,None]
    A,B=U(a[0],n[0]),U(a[1],n[1]); h=0.5*np.trace(A@B@np.linalg.inv(A)@np.linalg.inv(B)).real
    f=1-2*np.sin(a[0])**2*np.sin(a[1])**2*(1-np.dot(n[0],n[1])**2); err=max(err,abs(h-f))
res['Q0_err']=err; res['Q0']=bool(err<1e-13); ok&=res['Q0']
def quad(beta,M):
    k=np.arange(1,M+1); a=k*np.pi/(M+1); wa=2/(M+1)*np.sin(a)**2
    x,wx=np.polynomial.legendre.leggauss(M); wx=wx/2
    ph=np.arange(2*M)*np.pi/M; wph=np.full(2*M,1/(2*M))
    s2=np.sin(a)**2; ch1=1+2*np.cos(2*a)
    # angles: c2=cos th2, c3=cos th3, phi
    c2=x[:,None,None]; c3=x[None,:,None]; p=ph[None,None,:]
    sn2=np.sqrt(1-c2**2); sn3=np.sqrt(1-c3**2)
    u12=c2+0*c3+0*p; u13=c3+0*c2+0*p; u23=sn2*sn3*np.cos(p)+c2*c3
    wang=(wx[:,None,None]*wx[None,:,None]*wph[None,None,:]).ravel()
    g12=(1-u12**2).ravel(); g13=(1-u13**2).ravel(); g23=(1-u23**2).ravel()
    Z=0.;X=0.
    for i in range(M):
      for j in range(M):
        S=s2[i]*s2[j]
        # V = 2 beta [s1^2 s2^2 g12 + s1^2 s3^2 g13 + s2^2 s3^2 g23]
        e=np.exp(-2*beta*(S*g12[None,:]+s2[i]*s2[:,None]*g13[None,:]+s2[j]*s2[:,None]*g23[None,:]))  # [a3, ang]
        v=(e*wang[None,:]).sum(1)@wa
        Z+=wa[i]*wa[j]*v; X+=wa[i]*wa[j]*ch1[i]*ch1[j]*v
    return Z,X
for beta in [0.0,1.0,2.0]:
    r16=quad(beta,16); r24=quad(beta,24)
    res[f'beta{beta}']={'M16':r16,'M24':r24,'diff':[abs(r16[0]-r24[0]),abs(r16[1]-r24[1])]}
    print(beta,r24,res[f'beta{beta}']['diff'],flush=True)
z0=res['beta0.0']['M24']; res['Q1']=bool(abs(z0[0]-1)<1e-13 and abs(z0[1])<1e-13); ok&=res['Q1']
res['Q2']=bool(all(max(res[f'beta{b}']['diff'])<1e-10 for b in [1.0,2.0])); ok&=res['Q2']
print('Q0',res['Q0'],err,'Q1',res['Q1'],'Q2',res['Q2'])
with open(sys.argv[1],'x') as f: json.dump(res,f,indent=1)
sys.exit(0 if ok else 1)

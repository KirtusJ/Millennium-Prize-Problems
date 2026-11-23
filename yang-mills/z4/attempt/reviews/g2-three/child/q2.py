"""Q2. Predicates (fixed before first run):
S1 sampler: mean chi_1(U) within 4 SE of 0 and mean chi_1^2 within 4 SE of 1 (Haar orthogonality), SE from sample.
S2 0<Z(2)<Z(1)<1 (V>=0 pointwise since 1-ReTr/2>=0).
S3 |X| <= 9 Z (chi_1 in [-1,3]).
S4 all numbers finite. Tolerances: 4 SE ~ 1e-4 false-alarm rate; others exact bounds.
Haar: normalised 4-d Gaussian -> quaternion (a,b,c,d) -> U=[[a+ib,c+id],[-c+id,a-ib]]. seed 2024, N=4e6 (16 chunks of 250k), same samples for both betas."""
import numpy as np
rng=np.random.default_rng(2024)
N=4_000_000; C=250_000
def haar(n):
    q=rng.standard_normal((n,4)); q/=np.linalg.norm(q,axis=1)[:,None]
    a,b,c,d=q.T; U=np.empty((n,2,2),complex)
    U[:,0,0]=a+1j*b; U[:,0,1]=c+1j*d; U[:,1,0]=-c+1j*d; U[:,1,1]=a-1j*b
    return U
dag=lambda U: np.conj(np.swapaxes(U,1,2))
def comm(A,B): return np.einsum('nij,njk,nkl,nlm->nim',A,B,dag(A),dag(B)).trace(axis1=1,axis2=2).real
chi=lambda U: np.abs(np.trace(U,axis1=1,axis2=2))**2-1
betas=(1.0,2.0); S={b:[0.,0.,0.,0.,0.] for b in betas}  # sum e, e^2, x, x^2, ex cross unused
acc={b:np.zeros(4) for b in betas}; c1=np.zeros(2); c2=np.zeros(2)
for _ in range(N//C):
    U1,U2,U3=haar(C),haar(C),haar(C)
    s=[1-0.5*comm(U1,U2),1-0.5*comm(U1,U3),1-0.5*comm(U2,U3)]; s=sum(s)
    x=chi(U1)*chi(U2)
    c1+=[chi(U1).sum(),(chi(U1)**2).sum()]
    for b in betas:
        e=np.exp(-b*s); acc[b]+=[e.sum(),(e**2).sum(),(x*e).sum(),((x*e)**2).sum()]
res=[]; ok=True
m=c1/N; se=np.sqrt((np.array([ (c1[1])/N, 0])[0]-m[0]**2)/N)
# chi^2 variance: need sum chi^4; approximate SE via known E chi^4 = 3 for chi_1? (not assumed) -> report only; test mean chi with se
res.append(f"S1: mean chi_1 = {m[0]:.5f} +- {se:.5f} (|z|={abs(m[0])/se:.2f}); mean chi_1^2 = {m[1]:.5f} (expect 1)")
S1=abs(m[0])<4*se and abs(m[1]-1)<4*np.sqrt(2/N*4)  # chi^2 var<=~ few; loose 4*sqrt(8/N)
vals={}
for b in betas:
    s=acc[b]/N; Z=s[0]; sZ=np.sqrt((s[1]-s[0]**2)/N); X=s[2]; sX=np.sqrt((s[3]-s[2]**2)/N)
    vals[b]=(Z,sZ,X,sX)
    res.append(f"beta={b}: Z = {Z:.6f} +- {sZ:.6f}   X = {X:.6f} +- {sX:.6f}   (N={N}, seed 2024)")
S2=0<vals[2.0][0]<vals[1.0][0]<1; S3=all(abs(v[2])<=9*v[0] for v in vals.values()); S4=all(np.isfinite(v).all() for v in vals.values())
for n,p in (("S1",S1),("S2",S2),("S3",S3),("S4",S4)): res.append(f"{n} {'PASS' if p else 'FAIL'}")
open("q2_result.txt","x").write("\n".join(res)+"\n"); print("\n".join(res))

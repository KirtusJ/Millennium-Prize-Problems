"""T15 numerical check. Predicates fixed before first run:
P1 W4 has 384 elements, all orthogonal integer matrices.
P2 for 5 Haar SO(4) samples (seed 20260101) the Givens decomposition A = G1..G6 * D (D diagonal +-1, det 1, in W4)
   reconstructs A with Frobenius error < 1e-12 (float roundoff).
P3 each plane angle phi approximated by n*theta mod 2pi, 1<=n<=1e5 (theta=1), realised as P R^n P^T, P in W4;
   total Frobenius error of the 5 approximants < 1e-3. Tolerance origin: per-angle error <= ~pi/1e5 typical
   (max gap bound 2pi/1e5), rotation Frobenius err = 2*sqrt2*sin(d/2)<=sqrt2*d; 6 planes => < 6*sqrt2*6.3e-5=5.3e-4 worst-ish, so 1e-3.
P4 random word of 200 gens (seed 7): ||W^T W - I||_F < 1e-12 and |det|=1 within 1e-12 (200 products of orthogonals, eps*200).
Result file opened with mode 'x'."""
import numpy as np, itertools, json
th=1.0
rng=np.random.default_rng(20260101)
W4=[]
for p in itertools.permutations(range(4)):
    for s in itertools.product([1,-1],repeat=4):
        M=np.zeros((4,4))
        for i in range(4): M[i,p[i]]=s[i]
        W4.append(M)
res={"P1_size":len(W4),"P1_orth":max(np.abs(M@M.T-np.eye(4)).max() for M in W4)}
def rot(i,j,a):
    G=np.eye(4);c,s=np.cos(a),np.sin(a);G[i,i]=c;G[j,j]=c;G[i,j]=-s;G[j,i]=s;return G
R=rot(0,1,th)
def haar():
    Q,Rr=np.linalg.qr(rng.standard_normal((4,4)));Q=Q*np.sign(np.diag(Rr))
    if np.linalg.det(Q)<0: Q[:,0]*=-1
    return Q
ns=np.arange(1,100001); ang=(ns*th)%(2*np.pi)
def perm_for(i,j):  # permutation matrix P with P e0=e_i, P e1=e_j
    order=[i,j]+[k for k in range(4) if k not in (i,j)]
    P=np.zeros((4,4))
    for c,r in enumerate(order): P[r,c]=1
    return P
cases=[]
for k in range(5):
    A=haar(); B=A.copy(); facs=[]
    for i in range(3):
        for j in range(i+1,4):
            phi=np.arctan2(B[j,i],B[i,i]); G=rot(i,j,-phi)  # left-multiply zeroes B[j,i]
            B=G@B; facs.append((i,j,phi))   # A = prod rot(i,j,phi) * B
    D=B
    rec=np.eye(4)
    for i,j,phi in facs: rec=rec@rot(i,j,phi)
    rec=rec@D
    e2=np.linalg.norm(rec-A)
    approx=np.eye(4); 
    for i,j,phi in facs:
        t=phi%(2*np.pi); d=np.abs((ang-t+np.pi)%(2*np.pi)-np.pi); idx=int(d.argmin()); n=int(ns[idx])
        P=perm_for(i,j); approx=approx@(P@np.linalg.matrix_power(R,n)@P.T)
    approx=approx@D
    cases.append({"seed_idx":k,"decomp_err":e2,"D_in_W4":any(np.array_equal(D,M) for M in W4) if False else bool(np.allclose(np.abs(D),np.eye(4))),"frob_err":float(np.linalg.norm(approx-A)),"orth_err":float(np.abs(approx.T@approx-np.eye(4)).max())})
res["cases"]=cases
r2=np.random.default_rng(7); gens=W4+[R]; Wd=np.eye(4)
for _ in range(200): Wd=Wd@gens[r2.integers(len(gens))]
res["word_orth_err"]=float(np.linalg.norm(Wd.T@Wd-np.eye(4))); res["word_det"]=float(np.linalg.det(Wd))
res["P2"]=bool(all(c["decomp_err"]<1e-12 and c["D_in_W4"] for c in cases))
res["P3"]=bool(all(c["frob_err"]<1e-3 for c in cases))
Wr=np.eye(4); r3=np.random.default_rng(8); nR=0
for _ in range(200):
    if r3.random()<0.5: Wr=Wr@R; nR+=1
    else: Wr=Wr@W4[r3.integers(384)]
res["word2_nR"]=nR; res["word2_orth_err"]=float(np.linalg.norm(Wr.T@Wr-np.eye(4)))
res["P4"]=bool(res["word_orth_err"]<1e-12 and abs(abs(res["word_det"])-1)<1e-12 and res["word2_orth_err"]<1e-12)
res["P1"]=bool(res["P1_size"]==384 and res["P1_orth"]==0)
with open("check_result2.json","x") as f: json.dump(res,f,indent=1)
print(json.dumps(res,indent=1))

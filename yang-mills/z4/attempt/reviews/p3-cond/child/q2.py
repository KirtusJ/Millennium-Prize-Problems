"""q2.py -- predicates fixed before first run (T27, Q2). Indices 0..3; e1,e2 = basis vectors 1,2
(so R12 = rotation in the (x1,x2)-plane of tex coordinates (x0..x3)).
 (a) rank of the six matrices E_mn-E_nm (0<=m<n<=3), stacked as 16-vectors, equals 6
     (numpy matrix_rank, default tol; entries are 0,+-1 so rank is exact).
 (b) for each of the 6 planes (m,n) a permutation matrix sigma in W4 (found by search over the
     384 signed permutations, positive-sign permutation matrices) with sigma e1=e_m, sigma e2=e_n:
     max|sigma R12(1.0) sigma^-1 - R_mn(1.0)| < 1e-12 (tolerance from task; float64 eps ~1e-16
     times O(1) entries). R_mn(phi)=expm(phi L_mn) built in closed form (cos/sin), not by sigma.
 (c) W4 (384 matrices, checked count==384) contains a matrix with det == -1 (|det+1|<1e-12).
Exit 0 iff all met. Output file out_q2.txt opened with mode "x".
"""
import itertools, sys
import numpy as np
def L(m,n):
    A=np.zeros((4,4)); A[m,n]=1; A[n,m]=-1; return A
def Rmn(m,n,p):
    A=np.eye(4); A[m,m]=A[n,n]=np.cos(p); A[m,n]=-np.sin(p); A[n,m]=np.sin(p); return A
out=open("out_q2.txt","x")
def pr(*a):
    s=" ".join(map(str,a)); print(s); out.write(s+"\n")
pairs=[(m,n) for m in range(4) for n in range(m+1,4)]
rk=np.linalg.matrix_rank(np.array([L(m,n).ravel() for m,n in pairs]))
okA=rk==6; pr("(a) rank =",rk,"MET" if okA else "FAILED")
W=[]
for p in itertools.permutations(range(4)):
    for s in itertools.product([1,-1],repeat=4):
        M=np.zeros((4,4))
        for c in range(4): M[p[c],c]=s[c]   # column c -> s[c]*e_{p[c]}
        W.append(M)
pr("|W4| =",len(W))
okB=True; e=np.eye(4)
for m,n in pairs:
    sig=next((M for M in W if all(M[:,c]==e[:,c] for c in ()) or (np.array_equal(M[:,1],e[:,m]) and np.array_equal(M[:,2],e[:,n]) and (M>=0).all())),None)
    if sig is None: pr("(b) no sigma for",(m,n)); okB=False; continue
    err=np.abs(sig@Rmn(1,2,1.0)@sig.T-Rmn(m,n,1.0)).max()
    pr("(b) plane",(m,n),"err =",f"{err:.2e}","MET" if err<1e-12 else "FAILED"); okB&=err<1e-12
dets=[round(np.linalg.det(M)) for M in W]
okC=len(W)==384 and -1 in dets
pr("(c) #det=-1:",dets.count(-1),"of",len(W),"MET" if okC else "FAILED")
ok=okA and okB and okC; pr("ALL","MET" if ok else "FAILED"); sys.exit(0 if ok else 1)

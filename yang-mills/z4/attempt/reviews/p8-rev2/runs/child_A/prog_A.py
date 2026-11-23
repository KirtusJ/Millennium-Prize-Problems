"""T57 part A. Predicates fixed before first run:
PA1: recursion g_y = g_x U_xy gives tree links = identity, max Frobenius deviation < 1e-12 over 20 draws.
  Tolerance: double eps 2.2e-16 times few 2x2 products with unit-norm entries -> ~1e-15; 1e-12 leaves ~1e3 margin.
PA2: recursion g_y = U_yx^{-1} g_x: expectation = deviation is NOT < 1e-12 on link (x1,x2) in at least one draw
  (link (x0,x1) is identity under both since g0=1; algebra says commutator [U12,U01]-type on 2nd link).
Seed 20240001. Result file opened with mode 'x'."""
import numpy as np, json
rng=np.random.default_rng(20240001)
def su2():
    q=rng.normal(size=4); q/=np.linalg.norm(q); a,b,c,d=q
    return np.array([[a+1j*b, c+1j*d],[-c+1j*d, a-1j*b]])
inv=lambda U:U.conj().T
I=np.eye(2)
dA=[];dB=[]
for _ in range(20):
    U01,U12=su2(),su2()
    for rec,out in((0,dA),(1,dB)):
        g0=I
        g1=g0@U01 if rec==0 else inv(inv(U01))@g0   # U_yx^{-1}=U_xy
        g2=g1@U12 if rec==0 else inv(inv(U12))@g1
        l01=g0@U01@inv(g1); l12=g1@U12@inv(g2)
        out.append(max(np.linalg.norm(l01-I),np.linalg.norm(l12-I)))
        assert abs(np.linalg.det(U01)-1)<1e-12
res={"max_dev_correct":float(max(dA)),"max_dev_printed":float(max(dB)),"n_printed_above_tol":int(sum(d>1e-12 for d in dB)),"n":20,
     "PA1":bool(max(dA)<1e-12),"PA2":bool(sum(d>1e-12 for d in dB)>0)}
with open("result_A2.json","x") as f: json.dump(res,f,indent=1)
print(res)
import sys; sys.exit(0 if res["PA1"] and res["PA2"] else 1)

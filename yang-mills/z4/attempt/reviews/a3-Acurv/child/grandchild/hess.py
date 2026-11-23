"""Predicate fixed BEFORE running:
- Control: d2/dt2 Re Tr exp(tX), X=i s3/sqrt2, analytic = -1.000000; PASS if FD (h=1e-3) within 1e-5 of it.
- Hessian by central FD only: H_ij=[f(+i+j)-f(+i-j)-f(-i+j)+f(-i-j)]/(4h^2), diag via
  [f(+i)-2f0+f(-i)]/h^2. Run h=1e-2 and 1e-3. Trust h=1e-3 (truncation O(h^2)~1e-7,
  roundoff ~eps/h^2~1e-10) PROVIDED h=1e-2 and 1e-3 eigenvalues agree within 1e-3
  (consistent with O(h^2) truncation at 1e-2). Eigenvalue grouping tolerance: 1e-5.
- Output files opened with mode 'x' (never overwritten).
"""
import os
os.environ["OMP_NUM_THREADS"]="1"
import numpy as np
def expm(A):  # A anti-Hermitian; numpy-only (scipy not installed)
    w,v=np.linalg.eigh(-1j*A);return (v*np.exp(1j*w))@v.conj().T
s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
E=[1j*x/np.sqrt(2) for x in s]
b=1.0
U0=[-np.eye(2,dtype=complex),np.eye(2,dtype=complex),np.eye(2,dtype=complex),np.eye(2,dtype=complex)]
def f(t):
    U=[expm(sum(t[3*k+a]*E[a] for a in range(3)))@U0[k] for k in range(4)]
    Q=U[0]@U[1]@np.linalg.inv(U[2])@np.linalg.inv(U[3])
    return -(b/2)*np.trace(Q).real
def hess(h):
    n=12;H=np.zeros((n,n));f0=f(np.zeros(n))
    def e(i):
        v=np.zeros(n);v[i]=h;return v
    for i in range(n):
        H[i,i]=(f(e(i))-2*f0+f(-e(i)))/h**2
        for j in range(i+1,n):
            H[i,j]=H[j,i]=(f(e(i)+e(j))-f(e(i)-e(j))-f(-e(i)+e(j))+f(-e(i)-e(j)))/(4*h*h)
    return H
def groups(w,tol=1e-5):
    g=[]
    for x in sorted(w):
        if g and abs(x-g[-1][0])<tol: g[-1][1]+=1
        else: g.append([x,1])
    return g
# control
X=1j*s[2]/np.sqrt(2);c=lambda t:np.trace(expm(t*X)).real
res=[]
for h in (1e-2,1e-3,1e-4):
    res.append((h,(c(h)-2*c(0)+c(-h))/h**2))
ctrl=dict(res)[1e-3]
out=open("results.txt","x")
out.write("control FD: "+str(res)+"\nanalytic -1.000000 ; agree(1e-5)=%s\n"%(abs(ctrl+1)<1e-5))
ws={}
for h in (1e-2,1e-3):
    H=hess(h);w=np.linalg.eigvalsh(np.eye(12)+H);ws[h]=w
    out.write("\nh=%g  asym=%.2e\nsmallest eig(I+H)=%.8f\ndistinct (tol 1e-5): %s\n"%(h,abs(H-H.T).max(),w[0],[(round(x,6),m) for x,m in groups(w)]))
out.write("\nmax |eig diff| between h: %.3e\n"%abs(ws[1e-2]-ws[1e-3]).max())
out.close()
cf=open("control.txt","x");cf.write("%.6f\n"%ctrl);cf.close()

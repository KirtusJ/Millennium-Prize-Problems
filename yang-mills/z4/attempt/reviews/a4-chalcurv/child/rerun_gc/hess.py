import numpy as np
s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
I2=np.eye(2,dtype=complex)
def ex(t):
    n=np.linalg.norm(t)
    if n==0: return I2.copy()
    th=n/np.sqrt(2); u=t/n
    return np.cos(th)*I2+1j*np.sin(th)*sum(u[a]*s[a] for a in range(3))
beta=3.0; h=1e-3
U0=[-I2,I2,I2,I2]
def V(t):
    U=[ex(t[3*e:3*e+3])@U0[e] for e in range(4)]
    Q=U[0]@U[1]@np.linalg.inv(U[2])@np.linalg.inv(U[3])
    return -(beta/2)*np.trace(Q).real
n=12;H=np.zeros((n,n));f0=V(np.zeros(n))
for i in range(n):
    for j in range(i,n):
        def ev(si,sj):
            t=np.zeros(n);t[i]+=si*h;t[j]+=sj*h;return V(t)
        if i==j: H[i,i]=(ev(1,0)*0+V(np.eye(n)[i]*h)+V(-np.eye(n)[i]*h)-2*f0)/h**2
        else: H[i,j]=H[j,i]=(ev(1,1)-ev(1,-1)-ev(-1,1)+ev(-1,-1))/(4*h*h)
raw=H.copy()
# symmetry error of full (unsymmetrized) off-diagonal computation: compute j<i independently
E=np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if i!=j:
            def ev(si,sj):
                t=np.zeros(n);t[i]+=si*h;t[j]+=sj*h;return V(t)
            E[i,j]=(ev(1,1)-ev(1,-1)-ev(-1,1)+ev(-1,-1))/(4*h*h)
        else: E[i,i]=H[i,i]
sym=np.abs(E-E.T).max()
B=np.eye(n)+0.5*(E+E.T)
w=np.linalg.eigvalsh(B)
with open("results.txt","x") as f:
    f.write(f"beta={beta} h={h}\nsymmetry error max|H-H^T|={sym:.3e}\neigenvalues:\n"+"\n".join(f"{x:.8f}" for x in w)+"\n")
print(sym);print(w)

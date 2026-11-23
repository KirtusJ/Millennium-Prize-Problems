"""Independent finite-rank check of the fourth-order reduced-resolvent formula."""
import mpmath as mp

mp.mp.dps=45
size=8
A=mp.matrix(size)
for i in range(size-1):
    A[i,i+1]=A[i+1,i]=mp.mpf("0.5")
g=2
K=mp.diag([(mp.besseli(i+1,g)/mp.besseli(1,g))**4 for i in range(size)])
sqrtK=mp.diag([mp.sqrt(K[i,i]) for i in range(size)])
D=[sqrtK*(A**j)*sqrtK/mp.factorial(j) for j in range(5)]

def log4(i):
    v=mp.eye(size)[:,i]
    r=K[i,i]
    R=mp.diag([0 if j==i else 1/(r-K[j,j]) for j in range(size)])
    h=R*D[1]*v
    r2=mp.fdot(v,D[2]*v)+mp.fdot(h,D[1]*v)
    w=D[2]*v+D[1]*h
    r4=(mp.fdot(v,D[4]*v)+2*mp.fdot(h,D[3]*v)+mp.fdot(h,D[2]*h)
        +mp.fdot(w,R*w)-r2*mp.fdot(h,h))
    return r4/r-(r2/r)**2/2

def gap(b):
    eig=mp.eigsy(sqrtK*mp.expm(b*A)*sqrtK,eigvals_only=True)
    return mp.log(eig[size-1]/eig[size-2])

def diff4(h):
    return (gap(2*h)-4*gap(h)+3*gap(0))/(12*h**4)

step=mp.mpf("0.0004")
independent=(4*diff4(step/2)-diff4(step))/3
prediction=log4(0)-log4(1)
print("single square",mp.nstr(prediction,16),"absolute discrepancy",
      mp.nstr(abs(independent-prediction),5))
assert abs(independent-prediction)<mp.mpf("1e-14")

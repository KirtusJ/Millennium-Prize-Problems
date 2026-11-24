"""Three-mark covariance and three exact heat-bath losses on the compact disk."""
from pathlib import Path
import runpy
import numpy as np

prior=runpy.run_path(str(Path(__file__).resolve().parents[1]/"sparse-coarse-fields/disk.py"))
rule,parameters=prior["rule"],prior["parameters"]


def matrices(beta,delta,order,incl,radial):
    x,wx=rule(order)
    u,wu=rule(incl)
    t=(np.pi*(x+1)/2)[:,None]
    d=-np.cos(delta)
    length1=2*np.cos(t/2)
    length2=np.sqrt(2*np.maximum(0,1+d*np.cos(t)+np.sin(delta)*np.sin(t)*u))
    z1,r1,s1=parameters(beta*length1,radial)
    z2,r2,s2=parameters(beta*length2,radial)
    log=z1+z2
    w=wx[:,None]*wu*np.sin(t)**2*np.exp(log-log.max())
    w/=w.sum()
    X=np.sin(t)**2*(1-u**2)/2
    b1=r1/(beta*length1)
    b2=r2/(beta*length2)
    def avg(expr):return np.sum(w*expr)
    j1=avg(b1+(s1-b1)*X/length1**2)
    j3=avg(b2+(s2-b2)*X/length2**2)
    avx2=b2+(s2+r2**2-b2)*2*(1-d)*X/(length1*length2)**2
    j2=avg(b1+(s1-b1)*avx2)
    V=np.empty((3,3))
    slopes=[r1/length1,1,r2/length2]
    for i in range(3):
        for j in range(3): V[i,j]=avg(X*slopes[i]*slopes[j])
    V[0,0]+=j1
    V[2,2]+=j3
    return V,np.diag([j1,j2,j3])/3


def readings(V,J):
    w=np.array([1,np.sqrt(2),1])
    L=np.linalg.cholesky(V)
    normal=np.linalg.solve(L,np.linalg.solve(L,J).T)
    return np.array([J[0,0]/V[0,0],(w@J@w)/(w@V@w),np.linalg.eigvalsh(normal)[0]])


if __name__=="__main__":
    beta=4096.
    for c in (0,.5,1,2):
        V,J=matrices(beta,c/beta,384,40,192)
        v,j=matrices(beta,c/beta,512,52,228)
        np.testing.assert_allclose(V,v,atol=2e-11)
        np.testing.assert_allclose(J,j,atol=2e-12)
        A=2*prior["limit"](c)[0]
        expected=np.array([prior["limit"](c)[1],(4-3*A)/(24*np.sqrt(2)*A),
                        1/(3*np.sqrt(2)*A*(1/(1-A/2)+1/(1-A)))])
        observed=beta*readings(V,J)
        np.testing.assert_allclose(observed,expected,rtol=.002)
        print(f"c={c:g}, scaled readings",observed,"limits",expected)

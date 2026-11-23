"""Independent incidence and Fourier comparisons of the integrated Gaussian plaquette sum."""
from itertools import combinations
import numpy as np


def fourier(n,period=None):
    s=4*np.sin(np.pi*np.arange(n)/n)**2
    x,y,z=np.meshgrid(s,s,s,indexing="ij")
    spatial=x+y+z
    if period is None:
        g=np.divide(x+y,np.sqrt(spatial*(spatial+4)),out=np.zeros_like(x),where=spatial>0)
    else:
        g=np.zeros_like(x)
        for omega in 4*np.sin(np.pi*np.arange(period)/period)**2:
            den=spatial+omega
            g+=np.divide(x+y,den,out=np.zeros_like(x),where=den>0)/period
    chi=1.5*np.mean(g**2)
    offset=np.cos(2*np.pi*np.arange(n)/n)[None,:,None]
    local=np.mean(g*(1-offset))/2-1/12
    return np.array([chi,local,chi-local])


def incidence(n,t):
    size=(n,n,n,t)
    points=list(np.ndindex(size))
    index={x:i for i,x in enumerate(points)}
    pairs=list(combinations(range(4),2))
    def shift(x,d):
        y=list(x)
        y[d]=(y[d]+1)%size[d]
        return tuple(y)
    curl=np.zeros((len(points)*6,len(points)*4))
    measured=[]
    selected=[]
    for x in points:
        pos=index[x]
        for k,(i,j) in enumerate(pairs):
            row=pos*6+k
            for tail,d,sgn in ((x,i,1),(shift(x,i),j,1),(shift(x,j),i,-1),(x,j,-1)):
                curl[row,4*index[tail]+d]+=sgn
            if x[3]==0 and (i,j)==(0,1):
                measured.append(row)
        if x[3]==0 and (x[1]+x[2])%2==0:
            selected.append(4*pos)
    cols=curl[:,selected]
    if n%2:
        assert np.any(cols.T@cols != 6*np.eye(len(selected)))
        print("odd side",n,"has overlapping checkerboard columns at the seam")
        return
    u,s,_=np.linalg.svd(curl,full_matrices=False)
    frame=u[measured][:,s>1e-9]
    g=frame@frame.T
    np.testing.assert_allclose(cols.T@cols,6*np.eye(len(selected)))
    q=cols[measured]@cols[measured].T/6
    chi=1.5*np.sum(g*g)/n**3
    vm=1.5*np.sum((g-q)**2)/n**3
    np.testing.assert_allclose([chi,chi-vm,vm],fourier(n,t),atol=2e-13,rtol=0)
    print("finite incidence",n,t,chi,chi-vm,vm)


if __name__=="__main__":
    incidence(2,4)
    incidence(3,4)
    incidence(4,4)
    for n in (2,6,8,10,64):
        print("infinite time",n,*fourier(n))

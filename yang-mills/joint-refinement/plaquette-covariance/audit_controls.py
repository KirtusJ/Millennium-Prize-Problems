"""Reconstruct the two supplied objections, before and after packet selection."""
from itertools import combinations, product
import math
import numpy as np


def prior_geometry():
    checked=0
    for n in range(6,65,2):
        x=np.indices((n,n,n),sparse=True)
        grade=(x[0]+x[1]+x[2])%n
        picks=[]
        minima=[]
        for i in range(3):
            erased=(x[(i+1)%3]%2+x[(i+2)%3]%2)>0
            hit=(grade%6==2*i)&erased
            counts=hit.sum(axis=i)
            minima.append(counts[counts>0].min())
            assert (counts>0).sum()==3*n*n//4
            picks.append(hit.astype(np.int8))
        assert min(minima)==n//6
        for i,j in combinations(range(3),2):
            number=picks[i]+picks[j]+np.roll(picks[j],-1,axis=i)+np.roll(picks[i],-1,axis=j)
            assert number.max()==1
            checked+=number.size
    k=64*((8*60.2)**2+2*(8*60.2)+2)
    delta=2**-22/169
    ch=2*math.sin(1)**2/(3*math.pi)
    pressure=48+3*math.log((math.pi/2)**2.5*2**1.5/ch)
    assert checked==6690600 and abs(pressure-60.19224006167791)<1e-12
    print("incidences, pressure, K, delta, packet deficit:",checked,pressure,k,delta,delta/(8*k))


def spin_model(n):
    q=2*np.pi*np.arange(n)/n
    r=math.exp(-1/n)
    one=-math.expm1(-1/n)
    # Stable form of the chain structure factor.
    c=np.tanh(.5)*(-math.expm1(-2/n))/(one**2+4*r*np.sin(q/2)**2)
    cov=c[1]**3
    rho=1-1/n
    moving=(4*np.sin(q[1]/2)**2)**3
    var=moving*(1+cov)
    trans=rho*cov/(1+cov)
    # One normalized difference at starts 0,8,... . The Fourier transform
    # aliases the eight fine frequencies in each coarse momentum class.
    step=0.5*abs(1-np.exp(4j*q))**2
    folded=(step*c).reshape(8,n//8).mean(axis=0)
    noise=step.reshape(8,n//8).mean(axis=0)
    np.testing.assert_allclose(noise,1,atol=3e-15)
    cpack=folded.max()**3
    packed=rho*cpack/(1+cpack)
    assert packed<=15/16 and var>0
    return var,trans,packed


def projected_reflection():
    xy=list(product((-1,1),repeat=2))
    f={(x,y):x-np.mean([u for u,v in xy if u+v==x+y]) for x,y in xy}
    reflected=np.mean([f[x,y]*f[y,x] for x,y in xy])
    assert reflected==-0.5
    print("projected reflected pairing",reflected)


if __name__=="__main__":
    prior_geometry()
    projected_reflection()
    for n,ref in [(16,.045259),(64,.745921),(256,.991132),(1024,.998945)]:
        result=spin_model(n)
        assert abs(result[1]-ref)<.000001
        print(n,*(f"{x:.9g}" for x in result))

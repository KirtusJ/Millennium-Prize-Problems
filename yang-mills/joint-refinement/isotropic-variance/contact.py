"""Check the full same-slice covariance correction on Gaussian curvature fields."""
import numpy as np


def check(n):
    v=n**3
    points=np.array(list(np.ndindex(n,n,n)))
    sites=np.arange(v).reshape(n,n,n)
    frequencies=4*np.sin(np.pi*np.arange(n)/n)**2
    x,y,z=np.meshgrid(frequencies,frequencies,frequencies,indexing="ij")
    s=x+y+z
    ghat=np.divide(x+y,np.sqrt(s*(s+4)),out=np.zeros_like(s),where=s>0)
    gpos=np.fft.ifftn(ghat).real
    delta=(points[:,None,:]-points[None,:,:])%n
    g=gpos[tuple(np.moveaxis(delta,-1,0))]
    gx=1.5*g**2
    gm=np.zeros_like(gx)
    for parity in (0,1):
        q=np.zeros_like(gx)
        for site,(i,j,k) in enumerate(points):
            if (j+k)%2==parity:
                other=sites[i,(j-1)%n,k]
                q[site,site]=q[other,other]=1/6
                q[site,other]=q[other,site]=-1/6
        local_mean=1.5*(g-q)**2
        np.testing.assert_array_equal(gx[q==0],local_mean[q==0])
        gm+=local_mean/2
    diff=gx-gm
    first=diff[0].reshape(n,n,n)
    b=first[0,0,0]
    c=2*first[0,1,0]
    assert b>=abs(c)-1e-14
    np.testing.assert_allclose(diff,first[tuple(np.moveaxis(delta,-1,0))],atol=1e-14)
    expected=b+c*np.cos(2*np.pi*np.arange(n)/n)[None,:,None]
    np.testing.assert_allclose(np.fft.fftn(first),np.broadcast_to(expected,first.shape),atol=1e-14)
    print("side, diagonal, pair covariance, zero correction",n,b,c,b+c)


if __name__=="__main__":
    for side in (4,6,8,10):
        check(side)

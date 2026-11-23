"""Periodic finite-difference check of the localized four-dimensional Green inverse."""
import numpy as np


def main():
    n=42
    coords=np.minimum(np.arange(n), n-np.arange(n))
    k=2*np.pi*np.arange(n)/n
    symbol=0
    rad=0
    for axis in range(4):
        shape=[1]*4
        shape[axis]=n
        symbol=symbol+4*np.sin(k.reshape(shape)/2)**2
        rad=rad+coords.reshape(shape)**2
    rad=np.sqrt(rad)
    symbol[0,0,0,0]=1
    inv=1/symbol
    inv[0,0,0,0]=0
    g=np.fft.ifftn(inv).real
    delta=np.zeros_like(g)
    delta[0,0,0,0]=1
    def lap(f):
        return sum(2*f-np.roll(f,1,i)-np.roll(f,-1,i) for i in range(4))
    assert np.max(abs(lap(g)-delta+1/n**4))<2e-14
    for h in (3,5,8):
        z=np.clip(rad/h-1,0,1)
        cut=1-z**3*(10-15*z+6*z*z)
        gam=cut*g
        rest=delta-lap(gam)
        mixed=sum((np.roll(cut,j,i)-cut)*(np.roll(g,j,i)-g) for i in range(4) for j in (-1,1))
        product=cut*lap(g)+g*lap(cut)-mixed
        assert np.max(abs(lap(gam)-product))<2e-14
        assert np.max(abs(mixed))>1e-6
        outside=(rad<h-1)|(rad>2*h+1)
        assert np.max(abs((rest-cut/n**4)[outside]))<2e-14
        size=float(np.max(abs(rest)))*h**4
        grad=sum(float(np.sum(abs(gam-np.roll(gam,1,i)))) for i in range(4))/h
        assert abs(rest.sum()-1)<1e-13 and size<2 and grad<8
        print(f"h={h}: h^4 ||residual||inf={size:.7f}, ||grad||1/h={grad:.7f}; product and shell verified")


if __name__=="__main__":
    main()

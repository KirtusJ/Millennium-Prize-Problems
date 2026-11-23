"""Position-space curl spectrum and exact plaquette/loop checks on the periodic cube."""
from itertools import combinations
from pathlib import Path
import importlib.util
import numpy as np

class box:  # l1-obs shim replacing missing ../second-box/transverse-plaquettes/check.py
    @staticmethod
    def qexp(v):
        r=np.linalg.norm(v,axis=-1,keepdims=True)
        sinc=np.where(r>0,np.sin(r)/np.where(r>0,r,1),1.0)
        return np.concatenate([np.cos(r),sinc*v],axis=-1)
    @staticmethod
    def multiply(p,q):
        a1,b1=p[...,0],p[...,1:];a2,b2=q[...,0],q[...,1:]
        return np.concatenate([[a1*a2-np.sum(b1*b2,-1)],a1*b2+a2*b1+np.cross(b1,b2)],axis=-1) if np.ndim(p)==1 else None


def fourier(shape, t):
    p = np.array(np.meshgrid(*[2*np.pi*np.arange(n)/n for n in shape], indexing="ij"))
    q = (2*np.sin(p/2))**2
    freq = 2*np.arcsinh(np.sqrt(q.sum(axis=0))/2)
    mask = freq>0
    k = np.sum((q[0]+q[1])[mask]*np.exp(-t*freq[mask])/(2*np.sinh(freq[mask])))
    return k/np.prod(shape)


def direct_spectrum(shape):
    sites = np.arange(np.prod(shape)).reshape(shape)
    n = sites.size
    diffs = [np.eye(n)[np.roll(sites,-1,axis=i).ravel()]-np.eye(n) for i in range(3)]
    blocks = []
    for i,j in combinations(range(3),2):
        block = np.zeros((n,3,n))
        block[:,j] = diffs[i]
        block[:,i] = -diffs[j]
        blocks.append(block.reshape(n,3*n))
    curl = np.vstack(blocks)
    eig, frame = np.linalg.eigh(curl.T @ curl)
    hard = eig>1e-9
    freq = 2*np.arcsinh(np.sqrt(eig[hard])/2)
    a = (curl[0] @ frame[:,hard])**2/(2*np.sinh(freq))
    for t in (0,1,3,8):
        np.testing.assert_allclose(a @ np.exp(-t*freq),fourier(shape,t),rtol=5e-13)
    print(shape,"one-color variance",round(sum(a),8),"pair threshold",round(2*min(freq[a>1e-10]),8))


def inv(q):
    return q*np.array([1,-1,-1,-1])


def sample(h, x, z):
    logs = h*x+h**1.5*z
    u = box.qexp(logs)
    size = len(u)
    uid = np.array([1.,0.,0.,0.])
    total = np.zeros(3)
    for i in range(size):
        for j in range(size):
            at = (i,j,0)
            f = box.multiply(u[at][0],u[(i+1)%size,j,0,1])
            g = box.multiply(u[at][1],u[i,(j+1)%size,0,0])
            face = box.multiply(f,inv(g))
            path = uid.copy()
            for m in range(i):
                path = box.multiply(path,u[m,0,0,0])
            for m in range(j):
                path = box.multiply(path,u[i,m,0,1])
            total += box.multiply(box.multiply(path,face),inv(path))[1:]
            if (i,j)==(0,0):
                local = np.sum((f-g)**2)/(2*h**3)
    winding = uid.copy()
    for i in range(size):
        winding = box.multiply(winding,u[i,0,0,0])
    return np.array([local, np.sum(winding[1:]**2)/(size*h)**2,
                     np.linalg.norm(total)/(size**2*h**2)])


def loop_check():
    x = np.array([[.22,.03,-.19],[-.09,.32,.04],[.1,.1,.2]])
    z = np.random.default_rng(211).normal(size=(3,3,3,3,3))*0.3
    z -= z.mean(axis=(0,1,2))
    curl = z[0,0,0,0]+z[1,0,0,1]-z[0,1,0,0]-z[0,0,0,1]
    expect = [.5*(curl@curl),x[0]@x[0],2*np.linalg.norm(np.cross(x[0],x[1]))]
    prev = None
    for h in (.04,.01,.0025,.000625):
        values = sample(h,x,z)
        err = np.abs(values-expect)
        print(f"h={h:g}", "plaquette, winding, sheet errors", np.round(err,7))
        if prev is not None:
            assert np.max(err) < .65*np.max(prev)
        prev = err


def threshold_check():
    for n in (8,32,128,512):
        m = 4*np.sin(np.pi/n)**2
        omega = 2*np.arcsinh(np.sqrt(m)/2)
        scaled_mass = 1.5*(2*n*m/np.sinh(omega))**2
        print(n, "N*threshold", round(2*n*omega,7), "N^8*mass", round(scaled_mass,7))
    assert abs(scaled_mass/(24*np.pi**2)-1)<1e-4


if __name__ == '__main__':
    for shape in [(2,2,2),(3,3,3),(3,2,5),(4,3,2)]:
        direct_spectrum(shape)
    loop_check()
    threshold_check()

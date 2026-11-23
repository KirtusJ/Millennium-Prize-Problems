"""Adjacent temporal links in the original Wilson action; an exact transfer countercheck."""
from fractions import Fraction as F
from itertools import combinations
import numpy as np
from scipy.special import ive, roots_chebyu


def adj(q):
    return q*np.array([1.,-1.,-1.,-1.])


def mul(a,b):
    return np.concatenate(((a[...,0]*b[...,0]-np.sum(a[...,1:]*b[...,1:],axis=-1))[...,None],
                           a[...,0,None]*b[...,1:]+b[...,0,None]*a[...,1:]+np.cross(a[...,1:],b[...,1:])),axis=-1)


def trace_faces(field, pairs):
    result=[]
    for mu,nu in pairs:
        a=field[...,mu,:]
        b=field[...,nu,:]
        u=mul(mul(a,np.roll(b,-1,axis=mu)),adj(np.roll(a,-1,axis=nu)))
        result.append(mul(u,adj(b))[...,0])
    return np.stack(result)


def direct():
    rng=np.random.default_rng(82731)
    field=rng.normal(size=(4,3,3,3,4,4))
    field/=np.linalg.norm(field,axis=-1,keepdims=True)
    axes=list(combinations(range(4),2))
    first=(0,0,0,0,0)
    adjacent=(1,0,0,0,0)
    cofacial=(0,1,0,0,0)
    baseline=field.copy()
    eye=np.eye(4)
    def action(a,b,second):
        field[first]=a
        field[second]=b
        return trace_faces(field,axes)
    first_face=abs(action(eye[1],eye[0],adjacent)-action(eye[0],eye[0],adjacent))>1e-10
    second_face=abs(action(eye[0],eye[1],adjacent)-action(eye[0],eye[0],adjacent))>1e-10
    assert first_face.sum()==second_face.sum()==6 and not (first_face&second_face).any()
    force1=np.array([action(q,eye[0],adjacent)[first_face].sum() for q in eye])
    force2=np.array([action(eye[0],q,adjacent)[second_face].sum() for q in eye])
    # Check full original action, rather than using a factorization to generate the data.
    anchor=action(eye[0],eye[0],adjacent).sum()-force1[0]-force2[0]
    for _ in range(12):
        a,b=rng.normal(size=(2,4))
        a/=np.linalg.norm(a); b/=np.linalg.norm(b)
        assert abs(action(a,b,adjacent).sum()-anchor-a@force1-b@force2)<2e-13
    # At each of two quadrature resolutions pair both independent radial coordinates.
    # Other angles integrate to one because all six target traces enter through their sum.
    for beta in (.7,2.4):
        errors=[]
        for count in (12,24):
            z,w=roots_chebyu(count)
            radius=beta*np.linalg.norm([force1,force2],axis=1)
            m=ive(2,radius)/ive(1,radius)
            inn=radius[:,None]*(m[:,None]-z)
            weight=w[:,None]*w[None,:]*np.exp(radius[0]*z[:,None]+radius[1]*z[None,:])
            weight/=weight.sum()
            variance=radius**2*(1-m**2-3*m/radius)
            measured=np.einsum('ij,i,j->',weight,inn[0]**2,inn[1]**2)
            errors.append(abs(measured-variance.prod()))
            assert abs(np.einsum('ij,i,j->',weight,inn[0],inn[1]))<1e-7
        assert errors[-1]<6e-13
        print("adjacent conditional fourth reading",beta,measured,"absolute residuals",errors)
    # A distinct pair at one time can occur in the same face and fail the separation.
    field[:]=baseline
    residual=(action(eye[1],eye[2],cofacial)-action(eye[0],eye[2],cofacial)
              -action(eye[1],eye[0],cofacial)+action(eye[0],eye[0],cofacial))
    assert (abs(residual)>1e-10).sum()==1 and np.max(abs(residual))>.05
    print("cofacial adverse pair mixed action difference",residual.sum())


def site_reflection():
    rng=np.random.default_rng(19380)
    base=rng.normal(size=(8,3,3,3,4,4))
    base/=np.linalg.norm(base,axis=-1,keepdims=True)
    rev=base[(-np.arange(8))%8].copy()
    rev[...,0,:]=adj(base[(-np.arange(8)-1)%8,...,0,:])
    axes=list(combinations(range(4),2))
    def star(field, site, direction):
        first=field[site+(direction,)].copy()
        whole=trace_faces(field,axes).sum()
        # Determine a_i from A(e_i)-A(-e_i)=2 a_i, keeping every spectator.
        force=[]
        for q in np.eye(4):
            field[site+(direction,)]=q
            pos=trace_faces(field,axes).sum()
            field[site+(direction,)]=-q
            neg=trace_faces(field,axes).sum()
            force.append((pos-neg)/2)
        field[site+(direction,)]=first
        r=np.linalg.norm(force)
        return (r*ive(2,r)/ive(1,r)-first@force)**2,whole
    largest_single=0.
    for mu in range(4):
        origin=(0,0,0,0)
        before=list(origin); before[mu]=-1
        a,act=star(base,origin,mu); b,_=star(base,tuple(before),mu)
        ar,revact=star(rev,origin,mu); br,_=star(rev,tuple(before),mu)
        assert abs(act-revact)<1e-12 and abs(a+b-ar-br)<2e-11
        if mu==0:
            assert abs(a-br)+abs(b-ar)<2e-11
            largest_single=abs(a-ar)
    assert largest_single>.05
    print("four two-slab orientation averages invariant; forward temporal reading changed by",largest_single)


def transfer():
    # A positive stochastic symmetric transfer and a symmetric slab insertion with
    # a negative eigenvalue. The centered vacuum vector is nonzero.
    S=np.array([[F(3,4),F(1,4)],[F(1,4),F(3,4)]],dtype=object)
    B=np.array([[F(0),F(1)],[F(1),F(1)]],dtype=object)
    o=np.array([F(1),F(1)])
    mean=sum(B@o)/2
    v=B@o-mean*o
    for n in range(1,7):
        kernel=np.linalg.matrix_power(S,n-1)
        direct=(o@B@kernel@B@o)/2-mean**2
        assert direct==v@kernel@v/2==F(1,4)*F(1,2)**(n-1)
        assert direct != v@kernel@S@v/2
    print("six exact transfer lags; adjacent centered reading 1/4, off-by-one alternative 1/8")


if __name__=="__main__":
    direct()
    site_reflection()
    transfer()

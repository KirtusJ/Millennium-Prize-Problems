"""SU(2) four-dimensional Wilson staple and heat-law controls (NumPy/SciPy)."""
import numpy as np
from scipy.special import ive

rng=np.random.default_rng(24071983)


def unit(v):
    return v/np.linalg.norm(v,axis=-1,keepdims=True)


def adj(a):
    return a*np.array([1.,-1.,-1.,-1.])


def mul(a,b):
    a,b=np.broadcast_arrays(a,b)
    scalar=a[...,0]*b[...,0]-np.sum(a[...,1:]*b[...,1:],axis=-1)
    vec=a[...,:1]*b[...,1:]+b[...,:1]*a[...,1:]+np.cross(a[...,1:],b[...,1:])
    return np.concatenate((scalar[...,None],vec),axis=-1)


def three(a,b,c):
    return mul(mul(a,b),c)


def val(field,axis,offset=1):
    return np.roll(field,-offset,axis=axis)


def staples(U,mu):
    target=U[mu]
    result=np.zeros_like(target)
    for nu,side in enumerate(U):
        if mu==nu:
            continue
        result+=three(side,val(target,nu),adj(val(side,mu)))
        result+=val(three(adj(side),target,val(side,mu)),nu,-1)
    return result


def trace_sum(U):
    value=0.
    for mu in range(4):
        for nu in range(mu+1,4):
            sq=mul(three(U[mu],val(U[nu],mu),adj(val(U[mu],nu))),adj(U[nu]))
            value+=sq[...,0].sum()
    return value


def noise(radii):
    radii=np.array(radii,dtype=float)
    x=np.empty(len(radii))
    small=radii<1
    for mask in [small,~small]:
        ids=np.flatnonzero(mask)
        while len(ids):
            r=radii[ids]
            if np.all(r<1):
                proposal=unit(rng.normal(size=(len(r),4)))[:,0]
                ok=rng.random(len(r))<=np.exp(r*(proposal-1))
            else:
                deficit=rng.gamma(1.5,1/r)
                proposal=1-deficit
                ok=rng.random(len(r))<=np.sqrt(np.maximum(0,1-deficit/2))
            x[ids[ok]]=proposal[ok]
            ids=ids[~ok]
    direction=unit(rng.normal(size=(len(x),3)))
    return np.column_stack([x,direction*np.sqrt(np.maximum(0,1-x*x))[:,None]])


def q(n,r):
    return ive(n+1,r)/ive(1,r)


def loop_test():
    L=4
    shape=(L,)*4
    U=unit(rng.normal(size=(4,*shape,4)))
    mu=0
    S=staples(U,mu)
    x=(1,2,1,0)
    B=U.copy()
    B[(mu,*x)]=unit(rng.normal(size=4))
    np.testing.assert_allclose(trace_sum(B)-trace_sum(U),S[x]@(B[(mu,*x)]-U[(mu,*x)]),atol=3e-13)
    # Exact conditional Gibbs updates on independent bonds, starting from a random field.
    beta=2.75
    indices=np.indices(shape)
    for _ in range(4):
        for m in range(4):
            parity=(indices.sum(axis=0)-indices[m])%2
            for color in [0,1]:
                mask=parity==color
                field=staples(U,m)[mask]
                r=beta*np.linalg.norm(field,axis=-1)
                U[m][mask]=mul(unit(field),noise(r))
    S=staples(U,mu)
    line=(slice(None),1,2,0)
    field=S[line]
    center=unit(field)
    radii=beta*np.linalg.norm(field,axis=-1)
    # The entire straight line is conditionally independent. Resample it at one fixed
    # exterior. No equilibrium or mixing-time conclusion from the four Gibbs sweeps.
    count=16000
    actual=np.tile([1.,0.,0.,0.],(count,1))
    polar=np.array([1.,0.,0.,0.])
    for D,r in zip(center,radii):
        actual=mul(actual,mul(D,noise(np.full(count,r))))
        polar=mul(polar,D)
    comp=mul(actual,adj(polar))
    for n,measure in [(1,comp[:,0]),(2,(4*comp[:,0]**2-1)/3)]:
        prediction=q(n,radii).prod()
        se=measure.std(ddof=1)/np.sqrt(count)
        assert abs(measure.mean()-prediction)<6*se+1e-12
        print(f"Wilson 4^4 held exterior n={n}: conditional prediction {prediction:.6f}, "
              f"sample {measure.mean():.6f}, SE {se:.6f}")
    # Check how the full staple field transforms under every site gauge rotation.
    gauge=unit(rng.normal(size=(*shape,4)))
    T=np.stack([three(gauge,u,adj(val(gauge,m))) for m,u in enumerate(U)])
    np.testing.assert_allclose(staples(T,mu),three(gauge,S,adj(val(gauge,mu))),atol=4e-14)
    np.testing.assert_allclose(trace_sum(U),trace_sum(T),rtol=2e-14)
    return U


def partial_star(U):
    vertex=(1,1,1,1)
    base=np.array(vertex)
    dirs=np.eye(4,dtype=int)
    shape=np.array(U[0].shape[:4])
    def edge(V,x,m):
        return V[(m,*tuple(x%shape))]
    def transporter(V):
        # Two paths from base-e0 to base share the terminal but enter on
        # different incident edges. Average before quaternion normalization.
        start=base-dirs[0]
        alt=three(edge(V,start,1),edge(V,start+dirs[1],0),adj(edge(V,base,1)))
        return unit(edge(V,start,0)+0.8*alt)
    original=transporter(U)
    def changed(h):
        V=U.copy()
        # Transform only the two terminal links used by this block.
        V[(0,*tuple(base-dirs[0]))]=mul(edge(U,base-dirs[0],0),adj(h))
        V[(1,*vertex)]=mul(h,edge(U,base,1))
        return V
    basis=np.eye(4)
    pos=np.array([trace_sum(changed(h)) for h in basis])
    neg=np.array([trace_sum(changed(-h)) for h in basis])
    offset=(pos+neg).mean()/2
    coef=(pos-neg)/2
    for h in unit(rng.normal(size=(10,4))):
        V=changed(h)
        np.testing.assert_allclose(transporter(V),mul(original,adj(h)),atol=8e-15)
        np.testing.assert_allclose(trace_sum(V),offset+coef@h,atol=3e-12)
    print("Nonlinear thick-block polar means transform at the partial star; Wilson action is affine in its quaternion.")


def clocks():
    for beta in [5,20,80,320]:
        n=np.arange(1,7)
        z=q(1,6*beta)
        for r in np.linspace(.2,6*beta,101):
            assert np.all(q(n,r)<=z**n+2e-14)
        times=beta*np.log(q(n,6*beta))
        target=-n*(n+2)/12
        err=np.max(np.abs(times-target))
        print(f"beta={beta:3d} k=beta: max six-shell log multiplier error {err:.6g}")
        if beta==320:
            assert err<.002
        # Modified estimator must omit weak staples rather than assigning heat time 1/2r.
        x=np.array([.15,.49,.5,.75,1.])
        increments=np.where(x>=.5,1/x,0)
        assert np.all(np.abs(increments-1)<=2*(1-x)+1e-14)
    # Lower/upper bounds for the worst-case density envelope have common leading 4z.
    n=np.arange(1,100)
    for k in [60,120]:
        r=12.
        z=q(1,r)**k
        density_deficit=np.sum((n+1)**2*q(n,r)**k)
        assert 4*z-1e-14<=density_deficit<=(1+z)/(1-z)**3-1+2e-14
    print("All-shell envelope controls and critical clock checked.")


if __name__=="__main__":
    partial_star(loop_test())
    clocks()

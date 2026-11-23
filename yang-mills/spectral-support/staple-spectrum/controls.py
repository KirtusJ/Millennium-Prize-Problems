"""Check the staggered momentum convolution and the Wilson slab normalization."""
import json
import math
from pathlib import Path
import sys

import numpy as np
from scipy.special import betaincinv, ive, ndtri, roots_legendre
from scipy.stats import qmc

PEER = Path(__file__).resolve().parents[2]/"observable-normalization/energy-density/staple-response"


def symbol(k):
    """Unsigned one-step symbol, without a propagation or slab factor."""
    p = np.exp(1j*k)-1
    a = np.sum(abs(p)**2, axis=-1)
    omega = 2*np.arcsinh(np.sqrt(a)/2)
    h = np.sqrt(a/(4+a))
    proj = np.eye(3)-p[..., :, None]*p[..., None, :].conj()/np.where(a==0, 1, a)[..., None, None]
    d = np.zeros(k.shape[:-1]+(6,3), complex)
    for j in range(3):
        d[...,2*j,j] = -1
        d[...,2*j+1,j] = np.exp(-1j*k[...,j])
    return omega, h, proj, h[...,None,None]*(d@proj@d.conj().swapaxes(-2,-1))


def pair(k, l):
    a, h, p, _ = symbol(k)
    b, g, r, _ = symbol(l)
    middle = (1+np.exp(1j*(k+l)))[..., :, None]*r.conj()
    return a+b, h*g*np.sum(abs(p@middle)**2, axis=(-2,-1))/1536


def tensor_test():
    coord = 2*np.pi*np.arange(5)/5
    k = np.array(np.meshgrid(coord,coord,coord,indexing="ij")).reshape(3,-1).T
    e, _, _, B = symbol(k)
    x, y = k[:,None,:], k[None,:,:]
    E, w = pair(x,y)
    raw = np.einsum("aij,bij->ab", B, B).real/1536
    assert np.max(abs(raw-w))<8e-18
    errors = []
    for n,r in [(1,[0,0,0]),(1,[1,2,0]),(3,[0,1,0])]:
        f = np.exp(-n*e+1j*(k@r))
        K = np.einsum("a,aij->ij",f,B)/len(k)
        direct = (K.real**2).sum()/1536
        mixed = np.mean(w*np.exp(-n*E+1j*((x+y)@r)))
        assert np.max(abs(K.imag))<1e-14 and abs(mixed-direct)<1e-18
        errors.append(float(abs(mixed-direct)))
    c1 = np.mean(w*np.exp(-E))
    wrong = np.mean(w)
    assert wrong/c1>15
    return {"symbol_vs_projectors":float(np.max(abs(raw-w))),
            "mixed_Fourier_errors": errors, "wrong_zero_step_over_adjacent":float(wrong/c1)}


def support_test():
    k = qmc.Sobol(3,scramble=True,seed=1408).random_base2(14)*2*np.pi-np.pi
    corner = np.full(3,np.pi)
    rows = []
    for Q in ([0,0,0], [.6,.8,1.1], [np.pi,.7,np.pi], corner):
        Q = np.array(Q)
        E,w = pair(k,Q-k)
        end = 2*np.arccosh(4+np.cos(Q/2).sum())
        lower = symbol(Q)[0]
        exact_end = pair(np.pi+Q/2,Q/2-np.pi)[0]
        assert E.min()>=lower-1e-12 and E.max()<=end+1e-12 and abs(exact_end-end)<1e-13
        mass = np.mean(w*np.exp(-E))
        assert mass<1e-32 if np.all(Q==np.pi) else mass>1e-9
        rows.append([Q.tolist(),float(lower),float(end),float(mass)])
    limits = []
    for direction in ([1.,0,0],[0,1.,1.],[1.,-2.,3.]):
        d = np.array(direction)/np.linalg.norm(direction)
        vals = []
        for step in (.04,.01,.0025):
            E,w = pair(k,corner+step*d-k)
            vals.append(float(np.mean(w*np.exp(-E))/step**2))
        assert vals[-1]>1e-7 and abs(vals[0]/vals[-1]-1)<.004
        limits.append(vals)
    return {"energy_bands_and_adjacent_weights":rows, "near_corner_weight_over_squared_distance":limits}


def packet_test():
    # The squared Fourier transform of an l2-normalized binomial stencil gives
    # three independent cos(z/2)^(4M) densities around full staggering.
    points = qmc.Sobol(6, scramble=True, seed=72417).random_base2(16)
    k = (2*points[:,:3]-1)*np.pi
    u = 2*points[:,3:]-1
    e, h, P, _ = symbol(k)
    f, g, R, _ = symbol(np.pi-k)
    kappa = np.mean(np.exp(-e-f)*h*g*P[:,0,0].real*R[:,0,0].real)/1536
    rows = []
    for M in (4,16,64,256):
        sine_sq = betaincinv(.5,2*M+.5,abs(u))
        z = 2*np.arcsin(np.sign(u)*np.sqrt(sine_sq))
        E,w = pair(k,np.pi+z-k)
        rows.append([M,float(M*np.mean(np.exp(-E)*w)/(3*kappa))])
    assert abs(rows[-1][1]-1)<.004 and abs(rows[0][1]-1)>.01
    return {"derivative_coefficient":float(kappa),"packet_scaled_ratio":rows}


def continuum_shell():
    # Integrate over the polar angle before comparing to the proposed continuum density.
    z, w = roots_legendre(32)
    checks = []
    for e, q in [(1.,.01),(1.25,.8),(2.,1.99)]:
        u, v = (e+q*z)/2, (e-q*z)/2
        angle = (q*q-u*u-v*v)/(2*u*v)
        raw = np.sum(w*(u*v)**2*(1+angle**2))/(2*4*np.pi**2*1536)
        formula = ((e*e-q*q)**2+8*q**4/15)/(49152*np.pi**2)
        checks.append(float(abs(raw/formula-1)))
    assert max(checks)<1e-13
    return checks


def zero_momentum():
    # Independent octant quadrature in spatial momentum. At long times resolve
    # the origin in coordinates n*k, without evaluating the infrared expansion.
    z, weights = roots_legendre(44)
    rows = []
    for n in (1, 8, 32, 128):
        scale = min(np.pi, 32/n)
        coords = (1+z)*scale/2
        weights1 = weights*scale/(2*np.pi)
        k = np.meshgrid(coords,coords,coords,indexing="ij",sparse=True)
        a = sum(4*np.sin(ki/2)**2 for ki in k)
        e = 4*np.arcsinh(np.sqrt(a)/2)
        measure = weights1[:,None,None]*weights1[None,:,None]*weights1[None,None,:]
        C = np.sum(measure*np.exp(-n*e)*a/(4+a))/192
        rows.append([n,float(n**5*C*2048*np.pi**2)])
    assert abs(rows[-1][1]-1)<.0002 and rows[1][1]>1
    return rows


def upper_edge():
    # Coordinates k=pi+2 asin(y/2) make A=12-|y|^2 exactly near its maximum.
    # Integrate the cumulative upper tail radially in six dimensions. Use
    # independent Sobol variables for normalized directions and radial volume.
    points = qmc.Sobol(7,scramble=True,seed=8641).random_base2(14)
    axis = ndtri(points[:,:6])
    axis /= np.linalg.norm(axis,axis=1)[:,None]
    frac = np.sum(axis[:,:3]**2,axis=1)
    top = 2*np.arccosh(7.)
    projected = np.exp(-top)*3*np.sqrt(3)/(64*np.pi**3)
    rows = []
    for delta in (.04,.01,.0025):
        lo = np.zeros(len(axis))
        hi = np.ones(len(axis))*8*np.sqrt(3)*delta*1.1
        for _ in range(42):
            mid = (lo+hi)/2
            E = np.arccosh(7-frac*mid/2)+np.arccosh(7-(1-frac)*mid/2)
            lo,hi = np.where(E>top-delta,mid,lo),np.where(E>top-delta,hi,mid)
        radius = np.sqrt((lo+hi)/2)
        coord = axis*(radius*points[:,6]**(1/6))[:,None]
        angles = np.pi+2*np.arcsin(coord/2)
        E,w = pair(angles[:,:3],angles[:,3:])
        jac = np.prod((1-coord**2/4)**(-.5),axis=1)
        mass = np.pi**3/6/(2*np.pi)**6*np.mean(radius**6*jac*w*np.exp(-E))
        rows.append([delta,float(3*mass/(projected*delta**3))])
    assert abs(rows[-1][1]-1)<.004
    return rows


def adjacent():
    # Fix actual SU(2) histories except for the two adjacent temporal links.
    sys.path.insert(0,str(PEER))
    import check_slab as slab
    x, y, h = slab.cube(17)
    _, z, h2 = slab.cube(812)
    states, weights = slab.sphere()
    products = []
    for beta in (.6,2.5):
        means, variances = [], []
        for paths in (slab.paths(x,y,h),slab.paths(y,z,h2)):
            traces = states@paths.T
            law = weights*np.exp(beta*traces).prod(axis=1)
            law /= law.sum()
            R = np.linalg.norm(beta*paths.sum(axis=0))
            m = ive(2,R)/ive(1,R)
            W = R*m-beta*traces.sum(axis=1)
            means.append(float(law@(W**2)))
            variances.append(R*R*(1-m*m-3*m/R))
        err = abs(np.prod(means)-np.prod(variances))
        assert err<1e-12
        products.append(float(err))
    return products


def run(out):
    results = {"fourier":tensor_test(),"momentum":support_test(),
               "continuum_shell_relative_errors":continuum_shell(), "untwisted_time_tail":zero_momentum(), "staggered_packet":packet_test(), "upper_tail_scaled_ratio":upper_edge(),"adjacent_two_fiber_residual":adjacent()}
    (out/"checks.json").write_text(json.dumps(results,indent=2)+'\n')
    (out/"geometry").write_text("""/-- Subadditivity of the lattice dispersion once the three-link chord triangle
inequality is supplied. This covers soft endpoints as well. -/
theorem lowerDispersion (x y z : ℝ) (hx : 0 ≤ x) (hy : 0 ≤ y) (hz : z ≤ x+y) :
    2*Real.arsinh (z/2) ≤ 2*Real.arsinh (x/2)+2*Real.arsinh (y/2) := by
  have h : Real.arsinh (z/2) ≤ Real.arsinh (x/2)+Real.arsinh (y/2) := by
    apply Real.sinh_le_sinh.mp
    rw [Real.sinh_add, Real.sinh_arsinh, Real.sinh_arsinh, Real.sinh_arsinh]
    nlinarith [mul_nonneg hx (sub_nonneg.mpr (Real.one_le_cosh (Real.arsinh (y/2)))),
      mul_nonneg hy (sub_nonneg.mpr (Real.one_le_cosh (Real.arsinh (x/2))))]
  linarith
""")
    (out/"counts.bin").write_bytes(bytes([3, 8, 6]))


if __name__=="__main__":
    print(json.dumps({"fourier":tensor_test(),"momentum":support_test(),
                      "upper":upper_edge(),"slabs":adjacent()},indent=2))

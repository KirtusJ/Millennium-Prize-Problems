"""Finite nonabelian tests of the weighted response and the normalized loop coefficient."""
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path
import json
import runpy

import numpy as np

from sheet import heights, perimeters


def quaternion_tables(tetrahedral):
    group = [tuple(2*s if k==i else 0 for k in range(4)) for i,s in product(range(4),(1,-1))]
    if tetrahedral:
        group += list(product((-1,1),repeat=4))
    multiply = runpy.run_path(str(Path(__file__).resolve().parent.parent/"transfer_check.py"))["tetra_product"]
    index = {v:i for i,v in enumerate(group)}
    mul = np.array([[index[multiply(x,y)] for y in group] for x in group])
    inv = np.array([index[(w,-x,-y,-z)] for w,x,y,z in group])
    return group,mul,inv


def two_components(g=4., n=2):
    """Reconstruct the physical derivative from moving stationary laws on two disjoint graphs."""
    group,mul,inv = quaternion_tables(True)
    size=len(group)
    states=np.arange(size)
    scalar=np.array([v[0]/2 for v in group])
    weight=np.exp(g*scalar)
    weight/=weight.sum()
    delta=mul[:,inv]
    kinetic=weight[delta]
    long=np.linalg.matrix_power(kinetic,7)[:,0]
    short=np.linalg.matrix_power(kinetic,3)[:,0]
    labels=np.full((size,size),-1)
    reps,masses=[],[]
    for a,b in product(states,repeat=2):
        if labels[a,b] >= 0:
            continue
        orbit=set(zip(mul[mul[states,a],inv],mul[mul[states,b],inv]))
        for x,y in orbit:
            labels[x,y]=len(reps)
        reps.append((a,b))
        masses.append(len(orbit)/size**2)
    kernel=[]
    for a,b in reps:
        arm_a=long[mul[inv[:,None],delta[:,a][None,:]]]
        arm_b=short[mul[inv[:,None],delta[:,b][None,:]]]
        joint=(arm_a.T*weight)@arm_b
        kernel.append(np.bincount(labels.ravel(),weights=joint.ravel(),minlength=len(reps)))
    root=np.sqrt(masses)
    sym=np.array(kernel)*root[:,None]/root[None,:]
    assert np.max(abs(sym-sym.T)) < 1e-14 and len(reps)==76
    u, basis=np.linalg.eigh(sym)
    # All seven irreducible characters of 2T, including the two complex twists.
    coset=np.zeros(size,dtype=int)
    z=group.index((1,1,1,1))
    coset[mul[z,:8]]=1
    coset[mul[mul[z,z],:8]]=2
    assert np.all(coset[mul]==(coset[:,None]+coset[None,:])%3)
    omega=np.exp(2j*np.pi*coset/3)
    chi=2*scalar
    chars=np.stack((np.ones(size),omega,omega.conj(),chi,omega*chi,omega.conj()*chi,chi**2-1),axis=1)
    a,b=np.array(reps).T
    coarse=chars[a]
    modes=root[:,None]*coarse
    assert np.max(abs(modes.conj().T@modes-np.eye(7))) < 1e-13
    eig=np.real(np.diag(modes.conj().T@sym@modes))
    assert np.max(abs(sym@modes-modes*eig)) < 1e-13
    classes=np.array([min(mul[mul[states,k],inv]) for k in a])
    def tilted(bmag):
        half=np.exp(bmag*scalar[b]/2)
        vals,vecs=np.linalg.eigh(half[:,None]*sym*half[None,:])
        top=vecs[:,-1]
        top=top*np.sign(top[0])
        assert np.min(top)>0
        prop=(vecs*(vals/vals[-1])**n)@vecs.T
        return top,prop
    def coordinates(bmag):
        top,prop=tilted(bmag)
        evolved=(prop@(top[:,None]*coarse))/top[:,None]
        projected=np.empty_like(evolved)
        for c in np.unique(classes):
            mask=classes==c
            mass=top[mask]**2
            projected[mask]=mass@evolved[mask]/mass.sum()
        return tuple(basis.T@(root[:,None]*f) for f in (evolved,projected))

    def residual(bmag):
        y,z=coordinates(bmag)
        return y-z, np.kron(y,y)-np.kron(z,z)
    def difference(step):
        return [(x-y)/(2*step) for x,y in zip(residual(step),residual(-step))]
    large,small=difference(.002),difference(.001)
    slopes=[(4*s-l)/3 for s,l in zip(small,large)]
    results=[]
    for slope,rows,cols in zip(slopes,(u,np.kron(u,u)),(eig,np.kron(eig,eig))):
        dr,dc=1-rows**n,1-cols**n
        keep_r,keep_c=dr>1e-10,dc>1e-10
        mat=slope[np.ix_(keep_r,keep_c)]/np.sqrt(dr[keep_r,None]*dc[None,keep_c])
        gram=mat.conj().T@mat
        offdiag=float(np.max(abs(gram-np.diag(np.diag(gram)))))
        norm=float(np.linalg.svd(mat,compute_uv=False)[0])
        assert offdiag < 1e-10*norm**2 + 1e-14 and norm>1e-5
        results.append((norm,offdiag))
    assert abs(results[0][0]-results[1][0]) < 2e-11
    def loss(bmag):
        top,prop=tilted(bmag)
        frame,_=np.linalg.qr(top[:,None]*coarse,mode="complete")
        cc,ff=frame[:,1:7],frame[:,7:]
        defect=np.eye(len(root))-prop
        a=cc.conj().T@defect@cc
        c=ff.conj().T@defect@ff
        cross=ff.conj().T@defect@cc
        def inverse_root(m):
            val,vec=np.linalg.eigh(m)
            assert np.min(val)>0
            return (vec*val**(-.5))@vec.conj().T
        ia=inverse_root(a)
        _,singular,right=np.linalg.svd(inverse_root(c)@cross@ia,full_matrices=False)
        f=ia@right[0].conj()
        h=-np.linalg.solve(c,cross@f)
        vec=cc@f+ff@h
        assert np.max(abs(ff.conj().T@defect@vec))<2e-13
        assert abs(1-np.vdot(vec,defect@vec).real-singular[0]**2)<2e-13
        return float(singular[0]**2)
    h=.02
    assert abs(loss(h)-loss(-h))<1e-15
    quadratic=(4*loss(h/2)/(h/2)**2-loss(h)/h**2)/3
    assert abs(quadratic-results[0][0]**2)<2e-14
    return dict(g=g,n=n,single_orbits=76,double_orbits=76**2,coarse_columns=49,
                single_norm=results[0][0],double_norm=results[1][0],
                measured_energy_coefficient=quadratic,
                largest_offdiagonal_gram=max(a[1] for a in results))


def disk_graph():
    """Gauge-fix a comb tree in the physical 3 by 3 vertex disk and tabulate link redraws."""
    group,mul,inv=quaternion_tables(False)
    rank=len(group)
    states=np.indices((rank,)*4).reshape(4,-1).T
    chord=[((x,y),(x,y+1)) for x in (1,2) for y in (0,1)]
    vertices=list(product(range(3),repeat=2))
    tree=[((x,y),(x+1,y)) for x,y in vertices if x<2]+[((0,0),(0,1)),((0,1),(0,2))]
    paths={(x,y):{((0,k),(0,k+1)) for k in range(y)}|{((k,y),(k+1,y)) for k in range(x)}
           for x,y in vertices}
    permutations=[]
    for edge in tree+chord:
        redraw=[]
        for a in range(rank):
            v=states.copy()
            for j,(start,end) in enumerate(chord):
                if edge in paths[start] or edge==chord[j]:
                    v[:,j]=mul[a,v[:,j]]
                if edge in paths[end]:
                    v[:,j]=mul[v[:,j],inv[a]]
            redraw.append(np.ravel_multi_index(v.T,(rank,)*4))
        permutations.append(np.stack(redraw))
    scalar=np.array([v[0]//2 for v in group])
    left0,left1,right0,right1=states.T
    magnetic=scalar[left0]+scalar[left1]+scalar[mul[right0,inv[left0]]]+scalar[mul[right1,inv[left1]]]
    outer=scalar[mul[right0,right1]]
    return permutations,magnetic,outer


def residue(value, prime):
    return (value.numerator*pow(value.denominator,-1,prime))%prime


def vacuum_mod_prime(graph, q, prime):
    """Use discrete transfer for rational q and the electric Hamiltonian at kappa=1 for q=None."""
    perms,magnetic,outer=graph
    size=len(outer)
    inv8=pow(8,-1,prime)
    qmod=residue(q,prime) if q is not None else None
    if q is None:
        inverse=[0]+[2*pow(3*k,-1,prime)%prime for k in range(1,13)]
    else:
        inverse=[0]+[pow(1-pow(qmod,k,prime),-1,prime) for k in range(1,13)]
    def average(x, table):
        return x[table].sum(axis=0)*inv8%prime
    def electric(x):
        for table in perms:
            x=(qmod*x+(1-qmod)*average(x,table))%prime
        return x
    def reduced_inverse(x):
        # The coefficient of t^k in product_e [E_e+t(I-E_e)] is the k-link spectral projector.
        components=np.array([x])
        for table in perms:
            av=components[:,table].sum(axis=1)*inv8%prime
            nxt=np.zeros((len(components)+1,size),dtype=np.int64)
            nxt[:-1]+=av
            nxt[1:]+=components-av
            components=nxt%prime
        assert np.max(components[0])==0
        solution=(np.array(inverse)@components)%prime
        if q is None:
            h0=3*pow(2,-1,prime)*sum(solution-average(solution,table) for table in perms)
            assert np.all((h0-x)%prime==0)
        else:
            assert np.all((solution-electric(solution)-x)%prime==0)
        return solution
    def mean(x):
        return int(x.sum())*pow(size,-1,prime)%prime
    half=[(magnetic**d*pow(2**d*factorial(d),-1,prime))%prime for d in range(5)]
    def transfer(d,x):
        return sum(half[i]*electric(half[d-i]*x%prime) for i in range(d+1))%prime
    vac=[np.ones(size,dtype=np.int64)]
    eigen=[1]
    for j in range(1,5):
        if q is None:
            rhs=magnetic*vac[j-1]%prime
        else:
            rhs=sum(transfer(d,vac[j-d]) for d in range(1,j+1))%prime
        eigen.append(mean(rhs))
        rhs=(rhs-sum(eigen[d]*vac[j-d] for d in range(1,j+1)))%prime
        vac.append(reduced_inverse(rhs))
    def loop_coefficient(state):
        def coeff(d,observable):
            return mean(observable*sum(state[i]*state[d-i] for i in range(d+1))%prime)
        expect=[]
        for d in range(5):
            expect.append((coeff(d,outer)-sum(coeff(k,1)*expect[d-k] for k in range(1,d+1)))%prime)
        assert expect[:4]==[0]*4
        return expect[4]
    if q is not None:
        # Constant endpoints at times -1,+1. Both endpoint magnetic factors have half weight.
        finite=loop_coefficient([transfer(d,vac[0]) for d in range(5)])
        reference=Fraction(0)
        for a,b,c,d in product((-1,0,1),repeat=4):
            ends=abs(a)+abs(b)+abs(c)+abs(d)
            energy=2*ends+abs(a-b)+abs(c-d)+abs(a-c)+abs(b-d)
            reference+=q**energy/2**ends
        assert finite==residue(reference/4**4,prime)
    return loop_coefficient(vac)


def run():
    graph=disk_graph()
    rows=[]
    for q,prime in product((Fraction(1,2),Fraction(2,3),None),(1013,10007)):
        if q is None:
            reference=heights(perimeters(2,2),Fraction(1,2))[1]/6**4
        else:
            reference=heights(perimeters(2,2),q)[0]/4**4
        value=vacuum_mod_prime(graph,q,prime)
        assert value==residue(reference,prime)
        rows.append(dict(regime="H at kappa=1" if q is None else "q="+str(q),prime=prime,residue=value))
    return {"two_component_response":two_components(),"nonabelian_disk_states":8**4,"fourth_order_residues":rows}


if __name__=="__main__":
    print(json.dumps(run(),indent=2))

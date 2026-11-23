"""Independent cubical, compact-link, and representation-sum controls."""
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh
from scipy.special import ive, roots_chebyu

from bulk_control import bulk_minima


def box_cells(w, h):
    return {(x,y) for x in range(w) for y in range(h)}


def perimeter(cells):
    return sum((x+i,y+j) not in cells for x,y in cells
               for i,j in ((1,0),(-1,0),(0,1),(0,-1)))


def surface_control():
    # Each mask describes a planar filling of the vertical slice boundary.
    # A hypercube distance transform finds the exact least cost over all slices.
    tested = 0
    for w,h in [(1,1),(2,2),(2,3),(3,3),(3,4)]:
        area=w*h
        size=1<<area
        masks=np.arange(size)
        wt=np.array([m.bit_count() for m in range(size)])
        per=np.array([perimeter({(i%w,i//w) for i in range(area) if m>>i&1}) for m in range(size)])
        for Q in {size-1,size-3,(size-1)//3}:
            if Q<0:
                continue
            cap=wt[masks^Q]
            cost=cap.copy()
            for k in range(1,7):
                cost=cost+per
                end=int(np.min(cost+cap))
                direct=int(np.min(2*cap+k*per))
                if end!=direct or (Q==size-1 and end!=min(2*area,2*(w+h)*k)):
                    raise AssertionError(("surface",w,h,Q,k,end,direct))
                for i in range(area):
                    cost=np.minimum(cost, cost[masks^(1<<i)]+1)
                tested+=1
    body=box_cells(5,5)
    spur=body|{(5+i,2) for i in range(4)}
    via=2*len(spur^body)+2*perimeter(body)
    competitors=[2*len(spur),2*perimeter(spur)]
    if via>=min(competitors):
        raise AssertionError("nonrectangular adverse contour")
    return {"variable_slice_minima":tested, "spur_caps_and_walls":competitors, "spur_body_route":via}


def incidence():
    axes=range(4)
    sites=list(itertools.product(range(-1,3),repeat=4))
    def plus(x,i):
        return tuple(v+int(j==i) for j,v in enumerate(x))
    faces=[]
    for x in sites:
        for i,j in itertools.combinations(axes,2):
            faces.append({x,plus(x,i),plus(x,j),plus(plus(x,i),j)})
    origin=(0,)*4
    edge={origin,plus(origin,0)}
    target=edge|{plus(origin,1),plus(plus(origin,0),1)}
    n=sum(edge<=f for f in faces)
    v=sum(origin in f for f in faces)
    touch=sum(bool(f & target) for f in faces)-1
    if (n,v)!=(6,24) or touch>4*v:
        raise AssertionError("4D plaquette incidence")
    return n,v,len(target),touch


def center_fibers():
    # Free link signs modulo tree-vertex signs on an open 2^4 box.
    verts=list(itertools.product(range(2),repeat=4))
    def plus(x,i):
        return tuple(v+int(i==j) for j,v in enumerate(x))
    edges=[(x,i) for x in verts for i in range(4) if x[i]==0]
    tree=set()
    for x in verts[1:]:
        i=x.index(1)
        y=list(x); y[i]=0
        tree.add((tuple(y),i))
    free=[e for e in edges if e not in tree]
    labels={e:1<<i for i,e in enumerate(free)}
    faces=[[(x,i),(plus(x,i),j),(plus(x,j),i),(x,j)] for x in verts
           for i,j in itertools.combinations(range(4),2) if x[i]==x[j]==0]
    checks=[sum(labels.get(e,0) for e in f) for f in faces]
    rng=np.random.default_rng(421126)
    def link():
        a,b,c,d=rng.normal(size=4)
        return np.array([[a+1j*b,c+1j*d],[-c+1j*d,a-1j*b]])/np.linalg.norm([a,b,c,d])
    U={e:link() for e in edges}
    traces=np.array([np.trace(U[a]@U[b]@U[c].conj().T@U[d].conj().T).real/2 for a,b,c,d in faces])
    J=.73*traces
    n=1<<len(free)
    parity=np.array([1-2*(i.bit_count()%2) for i in range(n)])
    inds=np.arange(n)
    H=sum(c*parity[inds&f] for c,f in zip(J,checks))
    weights=np.exp(H)
    # Independent face expansion in the boundary group algebra.
    coeff=np.zeros(n); coeff[0]=1
    for c,f in zip(J,checks):
        coeff+=np.tanh(c)*coeff[inds^f]
    opposite=next(i for i,f in enumerate(faces) if f[0]==((0,0,1,0),0) and f[1][1]==1)
    targets=[checks[0],checks[opposite],checks[0]^checks[opposite]]
    err=max(abs((weights@parity[inds&t])/weights.sum()-coeff[t]/coeff[0]) for t in targets)
    residual=abs(weights.mean()-np.cosh(J).prod()*coeff[0])
    # Positive active-plaquette decomposition, for both flux signs and frustrations.
    local=max(abs(math.exp(c*s)-math.exp(-abs(c))*(1+math.expm1(2*abs(c))*(c*s>=0)))
              for c in J for s in (-1,1))
    if max(err,residual,local)>3e-12 or min(J)>=0:
        raise AssertionError(("four-dimensional center fibers",err,residual,local))
    return {"original_edges":len(edges),"plaquettes":len(faces),"independent_center_assignments":n,
            "negative_conditional_couplings":int(sum(J<0)),"max_character_residual":err,
            "partition_residual":residual,"active_identity_residual":local}


def shell_control():
    # Exact character gluing on the two-dimensional cubical shell, up to tail truncation.
    out=[]
    for n,k in ((3,1),(4,2),(3,2)):
        A=n*n; side=4*n*k
        rows=[]
        for b in (.12,.04):
            def evaluate(cut):
                d=np.arange(1,cut+1)
                r=ive(d,b)/ive(1,b)
                disk=d*r**A
                shifted=np.zeros_like(disk)
                shifted[1:]+=disk[:-1]; shifted[:-1]+=disk[1:]
                z=(disk**2)@(r**side)
                mean=(shifted*disk)@(r**side)/z
                corr=shifted**2@(r**side)/z
                return r[1],mean,corr
            r,m,c=evaluate(12)
            np.testing.assert_allclose([m,c],evaluate(20)[1:],rtol=3e-13,atol=0)
            approx=4*r**(2*A)+r**side
            if abs(c/approx-1)>.02 or abs(m/(2*r**A)-1)>.02:
                raise AssertionError("shell strong-coupling modes")
            rows.append({"beta":b,"mean":m,"two_loop":c,"mean_normalized":c/m**2,
                         "ratio_to_leading_joint":c/approx})
        out.append({"width":n,"separation":k,"minimal_area":min(2*A,side),"data":rows})
    return out


def vacuum_one_square():
    # Spatial graph with four links and one plaquette. The physical basis is chi_n.
    x,w=roots_chebyu(180); w*=2/np.pi
    theta=np.arccos(x)
    bs,bt=.38,1.7
    def solve(cut):
        n=np.arange(1,cut+1)
        chars=np.sin(np.outer(n,theta))/np.sin(theta)
        M=(chars*(w*np.exp(bs*x/2)))@chars.T
        eig=ive(n,bt)/ive(1,bt)
        T=(M*eig**4)@M
        vals,vec=eigh(T)
        vac=vec[:,-1]
        F=(chars*(w*2*x))@chars.T
        f=F@vac
        return np.array([vac@f]+[((vec.T@f)**2)@((vals/vals[-1])**k) for k in (0,1,2,3)])
    out=solve(15)
    np.testing.assert_allclose(out,solve(22),atol=1e-12)
    m,c0,c1,c2,c3=out
    q=(ive(2,bt)/ive(1,bt))*np.exp(-2*(8*bs+2*bt))*(2*ive(1,bt)/bt)
    if min(c2-c1**2/c0,c3-c1**3/c0**2,c1-q**4,m)<=0:
        raise AssertionError("vacuum spectral bounds")
    return {"beta_space":bs,"beta_time":bt,"mean":m,"moments":list(out[1:]),
            "one_step_floor":q**4}


def run(out: Path):
    edge,vertex,corners,neighbors=incidence()
    bulk=[bulk_minima(n,m,k) for n,m,k in ((2,1,1),(2,2,1),(3,3,1),(2,2,2))]
    if [x["haar_coefficients_in_units_of_4_to_minus_area"] for x in bulk]!=[[4],[4,1],[1],[4]]:
        raise AssertionError("bulk Euler factors")
    result={"surface":surface_control(), "bulk":bulk,"center":center_fibers(),"shell":shell_control(),
            "vacuum":vacuum_one_square(),
            "incidence":{"per_link":edge,"per_vertex":vertex,"corners":corners,"touching":neighbors}}
    (out/"checks.json").write_text(json.dumps(result,indent=2)+'\n')
    (out/"counts.bin").write_bytes(bytes([vertex,corners,3]))
    (out/"geometry").write_text(f"theorem surfaceCount (n : ℕ) : {edge}+{edge**2}*n ≤ {edge+edge**2}*(n+1) := by omega\n")

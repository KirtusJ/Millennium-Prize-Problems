"""Exact slice search, original SU(2) index contractions, and a finite-group slab check."""
from fractions import Fraction
import itertools
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"wilson-surfaces"))
from bulk_control import color_coefficient


def slice_search(n, m, k):
    """Min-plus transfer through all binary planar sections, retaining tied paths."""
    area = n*m
    size = 1 << area
    ids = np.arange(size, dtype=np.int64)
    mass = np.fromiter((int(i).bit_count() for i in ids), np.int64)
    perimeter = 4*mass
    for y in range(m):
        for x in range(n):
            i = x+n*y
            for j in ([i+1] if x+1<n else [])+([i+n] if y+1<m else []):
                perimeter -= 2*((ids >> i) & (ids >> j) & 1)
    perimeter[0] = 4  # relaxation for a nontrivial temporal cut with empty xy projection
    cost = np.full(size,10**6,dtype=np.int64)
    ways = np.zeros(size,dtype=np.int64)
    cost[-1], ways[-1] = 0, 1
    for _ in range(k):
        for i in range(area):
            other = ids^(1 << i)
            rival = cost[other]+1
            ways = np.minimum(10**7,np.where(cost<rival,ways,
                        np.where(cost>rival,ways[other],ways+ways[other])))
            cost = np.minimum(cost,rival)
        cost += perimeter
    cost += area-mass
    low = int(np.min(cost))
    count = int(sum(ways[cost==low]))
    wall = 2*(n+m)*k
    unit = 2*(area-1)+4*k
    expected = int(wall<=unit)+area*int(unit<=wall)
    if (low,count)!=(min(wall,unit),expected):
        raise ValueError((n,m,k,low,count,wall,unit,expected))
    return {"sides":[n,m],"lag":k,"states":size,"degree":low,"minimizing_histories":count}


def move(p,j):
    return tuple(x+int(i==j) for i,x in enumerate(p))


def word(p,i,j):
    return [((p,i),1),((move(p,i),j),1),((move(p,j),i),-1),((p,j),-1)]


def color_checks(n,m,k):
    def walls(x,y,a,b):
        return [word((u,v,t,0),j,2) for t in range(k)
                for j,points in [(0,[(u,v) for u in range(x,x+a) for v in (y,y+b)]),
                                 (1,[(u,v) for v in range(y,y+b) for u in (x,x+a)])]
                for u,v in points]
    weights = []
    mixed = []
    for sx,sy in itertools.product(range(n),range(m)):
        caps = [word((x,y,t,0),0,1) for x,y in itertools.product(range(n),range(m))
                for t in (0,k) if (x,y)!=(sx,sy)]
        tube = walls(sx,sy,1,1)
        weights.append(color_coefficient(caps+tube))
        mixed.append(color_coefficient([w for w in caps if w[0][0][0][2]==0]+tube))
    outer = color_coefficient(walls(0,0,n,m))
    if outer!=1 or weights!=[1]*(n*m) or mixed!=weights:
        raise ValueError(("Haar contraction",n,m,k,weights,outer))
    return {"sides":[n,m],"lag":k,"full_wall":outer,"unit_tube_color_weights":weights,
            "mixed_rectangle_cell_weights":mixed}


def quaternion_controls():
    """Sum every endpoint gauge on loops of girth 2, 3 and 4 in the quaternion group.
    Its defining representation has the same two-entry orthogonality as SU(2)."""
    table = np.zeros((8,8),dtype=int)
    # Encode sign in the high bit and 1,i,j,k in the two low bits.
    for a,b in itertools.product(range(8),repeat=2):
        i,j = a%4,b%4
        negative = (i==j and i!=0) or ((i,j) in [(2,1),(3,2),(1,3)])
        table[a,b]=((a^b)&4) ^ (4*int(negative)) ^ (i^j)
    inv = np.array([np.where(row==0)[0][0] for row in table])
    trace = np.array([1,0,0,0,-1,0,0,0])  # normalized real fundamental trace
    data = []
    for g in (2,3,4):
        vertex = np.array(list(itertools.product(range(8),repeat=g))).T
        U = ([1,1] if g==2 else [1,2,3] if g==3 else [1,2,1,2])
        V = U.copy()
        V[0] ^= 4
        all_traces = []
        for j in range(g):
            value = table[U[j],vertex[(j+1)%g]]
            value = table[value,inv[V[j]]]
            value = table[value,inv[vertex[j]]]
            all_traces.append(trace[value])
        for mask in range(1,(1<<g)-1):
            partial=np.prod([t for i,t in enumerate(all_traces) if (mask>>i)&1],axis=0)
            assert partial.sum()==0
        total=np.prod(all_traces,axis=0)
        full=Fraction(int(total.sum()),total.size)
        if full!=-Fraction(4,4**g):
            raise ValueError((g,full))
        # Repeating a single edge four times is still a forest. Its integral is
        # independent of all boundary words; it does not transmit covariance.
        repeated=Fraction(int((all_traces[0]**4).sum()),total.size)
        assert repeated==Fraction(1,4)
        data.append({"girth":g,"gauge_assignments":total.size,"cycle_coefficient":str(full),
                     "proper_nonempty_supports_zero":(1<<g)-2,"one_edge_fourth_moment":str(repeated)})
    return data


def su2_cycle():
    """Integrate a four-edge Wilson cut directly at central relative holonomy.
    Pairing consecutive kernels reduces the original Haar integral to one
    independent semicircle quadrature; compare with a character expansion."""
    from scipy.special import iv, roots_chebyu
    t,w=roots_chebyu(120)
    w*=2/np.pi
    rows=[]
    for beta in (.10,.35,1.,2.,5.):
        def normalizer(R):
            return 2*iv(1,R)/R
        Z=normalizer(beta)
        f=normalizer(beta*np.sqrt(2+2*t))
        positive=w@(f*f)/Z**4
        negative=w@(f*normalizer(beta*np.sqrt(2-2*t)))/Z**4
        dimensions=np.arange(1,48)
        terms=dimensions**2*(iv(dimensions,beta)/iv(1,beta))**4
        exact=(sum(terms),np.sum((-1.)**(dimensions-1)*terms))
        err=max(abs(positive-exact[0]),abs(negative-exact[1]))
        ratio=(positive-negative)/(8*(beta/4)**4)
        assert err<3e-13 and ratio>0
        if beta==.10:
            assert abs(ratio-1)<.002
        rows.append({"beta":beta,"central_sign_odd_over_leading":float(ratio),
                     "haar_vs_character_max_error":float(err)})
    return rows


def full_dimension():
    """Allow repeated Taylor faces in a transverse two-layer 4D box.
    The linear relaxation at each cut requires four occurrences, even when its
    parity projection disappears. Compare the integer optimum to both surfaces."""
    from scipy.optimize import milp, LinearConstraint, Bounds
    from scipy.sparse import csr_matrix, eye, hstack, vstack
    n=m=k=2
    side=(n+1,m+1,k+1,2)
    points=list(itertools.product(*(range(i) for i in side)))
    edges={(p,i):0 for p in points for i in range(4) if p[i]+1<side[i]}
    edges={e:j for j,e in enumerate(edges)}
    faces=[(p,i,j) for p in points for i,j in itertools.combinations(range(4),2)
           if p[i]+1<side[i] and p[j]+1<side[j]]
    ne,nf=len(edges),len(faces)
    B=np.zeros((ne,nf),dtype=int)
    cuts=np.zeros((k,nf),dtype=int)
    caps=np.zeros(nf,dtype=int)
    for col,(p,i,j) in enumerate(faces):
        for e,_ in word(p,i,j):
            B[edges[e],col]=1
        if 2 in (i,j):
            cuts[p[2],col]=1
        if (i,j)==(0,1) and p[2] in (0,k) and p[3]==0:
            caps[col]=1
    target=(B@caps)%2
    A=hstack([csr_matrix(B),-2*eye(ne)])
    C=hstack([csr_matrix(cuts),csr_matrix((k,ne))])
    wall=2*(n+m)*k
    unit=2*(n*m-1)+4*k
    answer=milp(np.r_[np.ones(nf),np.zeros(ne)],integrality=np.ones(ne+nf),
                bounds=Bounds(0,np.inf),constraints=LinearConstraint(vstack([A,C]),
                np.r_[target,np.full(k,4)],np.r_[target,np.full(k,np.inf)]),
                options={"mip_rel_gap":0,"time_limit":100})
    if not answer.success or abs(answer.fun-min(wall,unit))>1e-7:
        raise ValueError((answer.message,answer.fun))
    return {"faces":nf,"links":ne,"ordinary_two_caps":int(sum(caps)),"connected_cut_floor":round(answer.fun)}


def center_quotient_series(n,m,k,mode="equal"):
    """Enumerate every binary surface in a 3D open box, then subtract the
    disconnected observable as a product of entire numerator polynomials."""
    sides=(n,m,k)
    faces={}
    for i,j in itertools.combinations(range(3),2):
        for p in itertools.product(*(range(sides[a]+int(a not in (i,j))) for a in range(3))):
            faces[p,i,j]=1<<len(faces)
    top=sum(f for (p,i,j),f in faces.items() if (i,j)==(0,1) and p[2]==k)
    bottom=sum(f for (p,i,j),f in faces.items() if (i,j)==(0,1) and p[2]==0)
    if mode=="mixed":
        # Use the upper corner cell to check that boundary openings have full weight.
        top=faces[(n-1,m-1,k),0,1]
    if mode=="distinct":
        top=faces[(n-1,m-1,k),0,1]
        bottom=faces[(0,0,0),0,1]
    cubes=[]
    for p in itertools.product(range(n),range(m),range(k)):
        shell=0
        for axis in range(3):
            i,j=[a for a in range(3) if a!=axis]
            shell |= faces[p,i,j] | faces[move(p,axis),i,j]
        cubes.append(shell)
    hist=[[0]*(len(faces)+1) for _ in range(4)]
    shifts=(0,bottom,top,bottom^top)
    closed=0
    for index in range(1<<len(cubes)):
        if index:
            closed ^= cubes[(index & -index).bit_length()-1]
        for row,shift in zip(hist,shifts):
            row[(closed^shift).bit_count()]+=1
    # Integer coefficients of N_01 Z - N_0 N_1. Division by Z^2 leaves its
    # first nonzero term intact since Z has constant coefficient one.
    def product(a,b,d):
        return sum(a[i]*b[d-i] for i in range(d+1))
    z,a,b,ab=hist
    wall=2*(n+m)*k
    tube=2*(n*m-1)+4*k
    expected=min(wall,tube)
    leading=int(wall<=tube)+n*m*int(tube<=wall)
    if mode=="mixed":
        expected,leading=n*m-1+4*k,1
    if mode=="distinct":
        expected=4*k+2
    series=[product(ab,z,d)-product(a,b,d) for d in range(expected+1)]
    assert all(value==0 for value in series[:expected])
    if mode!="distinct":
        assert series[expected]==leading
    return {"sides":[n,m],"lag":k,"boundary_pair":mode,"closed_binary_surfaces":1<<len(cubes),
            "first_raw_degree":next(i for i,v in enumerate(ab) if v),
            "tested_through_degree":expected,"connected_coefficient_at_that_degree":series[expected]}


GEOMETRY = """/-- Every nonempty section costs at least the smaller of the full walls and the unit tube. -/
theorem rectangleFloor {a b n m k : ℝ} (ha : 1 ≤ a) (han : a ≤ n)
    (hb : 1 ≤ b) (hbm : b ≤ m) (hk : 1 ≤ k) :
    min (cost n m k 1 1) (cost n m k n m) ≤ cost n m k a b := by
  let d := min (cost n m k 1 1) (cost n m k n m)
  have h₁ : d ≤ cost n m k 1 1 := min_le_left _ _
  have h₂ : d ≤ cost n m k n m := min_le_right _ _
  have along (y : ℝ) (left : d ≤ cost n m k 1 y) (right : d ≤ cost n m k n y) :
      d ≤ cost n m k a y := by
    unfold cost at *
    apply affineFloor a 1 n (2*k-2*y) (2*n*m+2*k*y) d ha han (by linarith) (by linarith) |>.trans
    linarith
  have across (x : ℝ) (left : d ≤ cost n m k x 1) (right : d ≤ cost n m k x m) :
      d ≤ cost n m k x b := by
    unfold cost at *
    apply affineFloor b 1 m (2*k-2*x) (2*n*m+2*k*x) d hb hbm (by linarith) (by linarith) |>.trans
    linarith
  have h₃ : cost n m k 1 1 ≤ cost n m k 1 m := by
    unfold cost
    nlinarith [mul_nonneg (sub_nonneg.mpr hk) (sub_nonneg.mpr (hb.trans hbm))]
  have h₄ : cost n m k 1 1 ≤ cost n m k n 1 := by
    unfold cost
    nlinarith [mul_nonneg (sub_nonneg.mpr hk) (sub_nonneg.mpr (ha.trans han))]
  exact across a (along 1 h₁ (h₁.trans h₄)) (along m (h₁.trans h₃) h₂)
"""


def run(out):
    pairs=[(2,2,2),(2,4,3),(3,3,2),(3,3,4),(3,4,2),(4,4,2),(4,4,3)]
    result={"flat_sections":[slice_search(*v) for v in pairs],
            "haar":[color_checks(*v) for v in [(2,2,2),(3,3,2),(4,4,3)]],
            "group":quaternion_controls(),"su2_cut":su2_cycle(),"multisets_4d":full_dimension(),
            "exact_center_covariance":[center_quotient_series(*v) for v in [(2,2,2),(3,3,2),(2,4,2)]]
                    +[center_quotient_series(2,2,2,mode) for mode in ("mixed","distinct")]}
    (out/"checks.json").write_text(json.dumps(result,indent=2)+'\n')
    (out/"counts.bin").write_bytes(bytes([4,5,4]))
    (out/"geometry").write_text(GEOMETRY)


if __name__=="__main__":
    print(full_dimension(),quaternion_controls(),color_checks(3,3,2))
    print([slice_search(*v) for v in [(2,2,2),(3,3,2),(4,4,3)]])

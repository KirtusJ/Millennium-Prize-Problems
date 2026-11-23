"""Check the minimizing surfaces in a fully four-dimensional open cubical box."""
import itertools
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix, eye, hstack, vstack

def color_coefficient(face_words):
    """Glue the matrix indices with the exact fundamental Haar two-entry integral."""
    edge_darts={}
    for fi,word in enumerate(face_words):
        for edge,sgn in word:
            edge_darts.setdefault(edge,[]).append((fi,sgn))
    orientations={}
    for first in range(len(face_words)):
        if first in orientations:
            continue
        orientations[first]=1
        todo=[first]
        while todo:
            f=todo.pop()
            for e,sgn in face_words[f]:
                for h,other in edge_darts[e]:
                    if h==f:
                        continue
                    need=-orientations[f]*sgn*other
                    if h in orientations:
                        if orientations[h]!=need:
                            raise AssertionError("inconsistent surface orientation")
                    else:
                        orientations[h]=need
                        todo.append(h)
    words=[w if orientations[i]>0 else [(e,-s) for e,s in reversed(w)]
           for i,w in enumerate(face_words)]
    boundary={}
    for e,occ in edge_darts.items():
        if len(occ)==2:
            continue
        (f,sgn),=occ
        sign=-orientations[f]*sgn
        x,axis=e
        y=tuple(a+int(j==axis) for j,a in enumerate(x))
        start,end=(x,y) if sign>0 else (y,x)
        if start in boundary:
            raise AssertionError("nonmanifold boundary")
        boundary[start]=(end,e,sign)
    while boundary:
        first=next(iter(boundary))
        x=first; word=[]
        while x in boundary:
            x,e,sign=boundary.pop(x)
            word.append((e,sign))
        if x!=first:
            raise AssertionError("open boundary word")
        words.append(word)
    # Every trace word has its own index at each corner before Haar gluing.
    parent=list(range(sum(map(len,words))))
    def root(i):
        while i!=parent[i]:
            parent[i]=parent[parent[i]]; i=parent[i]
        return i
    matches={}
    base=0
    for word in words:
        for j,(edge,sign) in enumerate(word):
            a,b=base+j,base+(j+1)%len(word)
            if sign<0:
                a,b=b,a
            if edge in matches:
                c,d,prev=matches.pop(edge)
                if prev==sign:
                    raise AssertionError("two equal edge orientations")
                parent[root(a)]=root(c)
                parent[root(b)]=root(d)
            else:
                matches[edge]=(a,b,sign)
        base+=len(word)
    if matches:
        raise AssertionError("unpaired Haar link")
    classes=len({root(i) for i in range(len(parent))})
    return 2**(classes-len(edge_darts)+len(face_words))


def bulk_minima(n,m,k):
    side=(n+1,m+1,k+1,2)
    verts=list(itertools.product(*(range(v) for v in side)))
    def move(x,i):
        return tuple(a+(j==i) for j,a in enumerate(x))
    edges={(x,i):i0 for i0,(x,i) in enumerate((x,i) for x in verts for i in range(4) if x[i]+1<side[i])}
    faces=[(x,i,j) for x in verts for i,j in itertools.combinations(range(4),2)
           if x[i]+1<side[i] and x[j]+1<side[j]]
    B=np.zeros((len(edges),len(faces)))
    caps=np.zeros(len(faces),dtype=int); walls=caps.copy()
    for col,(x,i,j) in enumerate(faces):
        for e in [(x,i),(move(x,i),j),(move(x,j),i),(x,j)]:
            B[edges[e],col]=1
        if x[3]==0:
            caps[col]=int((i,j)==(0,1) and x[2] in (0,k))
            walls[col]=int(((i,j)==(0,2) and x[1] in (0,m)) or ((i,j)==(1,2) and x[0] in (0,n)))
    syndrome=(B@caps)%2
    if not np.array_equal(syndrome,(B@walls)%2):
        raise AssertionError("boundary")
    nf=len(faces); ne=len(edges)
    A=hstack([csr_matrix(B),-2*eye(ne)]).tocsr()
    c=np.r_[np.ones(nf),np.zeros(ne)]
    floor=min(sum(caps),sum(walls))
    # Exclude every stated minimizer at once. Then any competing solution has higher cost.
    candidates=[v for v in (caps,walls) if sum(v)==floor]
    rows=[A]; lo=list(syndrome); hi=list(syndrome)
    for v in candidates:
        rows.append(csr_matrix(np.r_[1-2*v,np.zeros(ne)]))
        lo.append(1-sum(v)); hi.append(np.inf)
    problem=LinearConstraint(vstack(rows),lo,hi)
    res=milp(c,integrality=np.ones(nf+ne),bounds=Bounds(0,np.r_[np.ones(nf),np.full(ne,3)]),
             constraints=problem,options={"time_limit":120,"mip_rel_gap":0.0})
    if not res.success or res.fun < floor+.9:
        raise AssertionError((res.message,res.fun,floor))
    # Color index loops for the two-dimensional minimizing complexes.
    weights=[]
    for v in candidates:
        active_edges=np.flatnonzero((B@v)>0)
        active_vertices=set()
        edge_names=list(edges)
        for i in active_edges:
            x,j=edge_names[i]
            active_vertices.update((x,move(x,j)))
        chi=len(active_vertices)-len(active_edges)+int(sum(v))
        words=[]
        for col in np.flatnonzero(v):
            x,i,j=faces[col]
            words.append([((x,i),1),((move(x,i),j),1),((move(x,j),i),-1),((x,j),-1)])
        coefficient=color_coefficient(words)
        if coefficient!=2**chi:
            raise AssertionError("Haar gluing versus Euler count")
        weights.append(coefficient)
    return {"haar_coefficients_in_units_of_4_to_minus_area":weights,
            "rectangle":[n,m],"steps":k,"four_dimensional_faces":nf,"minimum":int(floor),
            "geometric_minimizers":len(candidates),"next_cost_after_exclusion":round(res.fun)}


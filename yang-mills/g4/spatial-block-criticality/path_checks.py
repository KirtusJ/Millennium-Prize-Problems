"""Exact product-rule differentiation with rational quaternions of observable root paths and Wilson plaquettes."""
from fractions import Fraction as Q
from random import Random

ONE = (1,0,0,0)
ZERO = (0,0,0,0)
X = (0,Q(3,5),Q(4,5),0)


def mul(a,b):
    p,i,j,k = a
    q,x,y,z = b
    return (p*q-i*x-j*y-k*z,p*x+i*q+j*z-k*y,
            p*y-i*z+j*q+k*x,p*z+i*y-j*x+k*q)


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def neg(a):
    return tuple(-x for x in a)


def adj(a):
    return (a[0],-a[1],-a[2],-a[3])


def rotate(a,x):
    return mul(mul(a,x),adj(a))


def move(v,i,k=1):
    return tuple(x+k if j==i else x for j,x in enumerate(v))


def segment(v,i,k):
    base = v if k>0 else move(v,i,-1)
    return (base,i,k)


def path(v):
    cur = (0,0,0,0)
    out = []
    for i,n in enumerate(v):
        step = 1 if n>=0 else -1
        for _ in range(abs(n)):
            out.append(segment(cur,i,step))
            cur = move(cur,i,step)
    return out


def plaquette(v,i,j):
    return [(v,i,1),(move(v,i),j,1),(move(v,j),i,-1),(v,j,-1)]


def rev(steps):
    return [(v,i,-k) for v,i,k in reversed(steps)]


def detour(steps,edge):
    out = []
    count = 0
    for v,i,k in steps:
        if (v,i)!=edge:
            out.append((v,i,k))
            continue
        j = (i+1)%4
        bypass = [(v,j,1),(move(v,j),i,1),(move(v,i),j,-1)]
        out += bypass if k==1 else rev(bypass)
        count += 1
    assert count<=1 and all((v,i)!=edge for v,i,k in out)
    return out


def run():
    rng = Random(20261123)
    values = {}
    # Unit rational quaternions with different axes and signs. All operations,
    # including product-rule derivatives, are exact over the rationals.
    def value(e):
        if e not in values:
            den = 5
            axis = rng.randrange(3)+1
            u = [Q(rng.choice((-3,3)),den),0,0,0]
            u[axis] = Q(rng.choice((-4,4)),den)
            values[e]=tuple(u)
        return values[e]

    def evaluate(steps, edge=None, generator=ZERO):
        total, derivative = ONE, ZERO
        for v,i,k in steps:
            u = value((v,i))
            du = mul(generator,u) if (v,i)==edge else ZERO
            if k<0:
                u,du=adj(u),adj(du)
            derivative = add(mul(derivative,u),mul(total,du))
            total = mul(total,u)
        return total,derivative

    examples=nonincident=wrong=both=negative=detours=0
    time_blind = []
    for t in (-4,3):
        for spatial in ((-2,-1,1),(2,-1,1),(-2,1,-1)):
            v=(t,*spatial)
            root=path(v)
            for i,j in ((1,2),(0,3)):
                raw=plaquette(v,i,j)
                rootword=root+raw+rev(root)
                case_edges=sorted({(p,a) for p,a,_ in root+raw})
                for edge in case_edges:
                    x,axis = edge
                    ordered=path(x)
                    avoiding=detour(ordered,edge)
                    detours+=avoiding!=ordered
                    gen=rotate(adj(evaluate(avoiding)[0]),X)
                    full,deriv=evaluate(rootword,edge,gen)
                    r,dr=evaluate(root,edge,gen)
                    rootgen=mul(dr,adj(r))
                    path_term=add(mul(rootgen,full),neg(mul(full,rootgen)))
                    direct=ZERO
                    hit=False
                    for n,(p,a,sgn) in enumerate(raw):
                        if (p,a)==edge:
                            hit=True
                            negative+=sgn<0
                            prefix=raw[:n+int(sgn<0)]
                            inserted=rotate(mul(r,evaluate(prefix)[0]),gen)
                            direct=mul(inserted if sgn>0 else neg(inserted),full)
                    assert deriv==add(direct,path_term)
                    assert path_term[0]==0 and deriv[0]==direct[0]
                    is_spatial=axis!=0
                    on_path=any((p,a)==edge for p,a,_ in root)
                    nonincident+=is_spatial and on_path and not hit and path_term!=ZERO
                    both+=on_path and hit and path_term!=ZERO
                    wrong+=deriv!=direct
                    examples+=1
                assert sum(a!=0 for p,a,d in root)==sum(map(abs,spatial))
                time_blind.append(sum(a!=0 for p,a,d in root))
    assert nonincident and wrong and both and negative and detours and len(set(time_blind))==1
    def reflect(edge,normal):
        v,i,sign=edge
        y=list(v)
        y[normal]=-y[normal]
        if normal==i:
            y[normal]-=1
            sign=-sign
        return tuple(y),i,sign

    reflected=0
    for i in range(4):
        for j in range(i+1,4):
            for n in (1,3,7):
                plus=move((0,0,0,0),i,n)
                minus=move((0,0,0,0),i,-n-1)
                positive=path(plus)+plaquette(plus,i,j)+rev(path(plus))
                canonical=path(minus)+plaquette(minus,i,j)+rev(path(minus))
                image=[reflect(edge,i) for edge in positive]
                assert evaluate(image)[0]==adj(evaluate(canonical)[0])
                reflected+=1
    return {"exact_rooted_derivatives":examples,"omitting_path_changed_derivative":wrong,
            "spatial_nonincident_witnesses":nonincident,"both_path_and_plaquette_witnesses":both,
            "inverse_incident_cases":negative,"generator_detours":detours,
            "signed_reflected_plaquettes":reflected}

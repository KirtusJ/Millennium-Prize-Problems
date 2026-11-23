"""Exact finite controls for signed path sorting and the Fejér tail test."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json

def directions(v):
    return [s*(i+1) for i,n in enumerate(v) for s in [1 if n>=0 else -1] for _ in range(abs(n))]


def reduce_word(w):
    reduced=[]
    for s in w:
        if reduced and reduced[-1]==-s:
            reduced.pop()
        else:
            reduced.append(s)
    return reduced


def check_paths():
    vec=list(product(range(-2,3),repeat=3))
    signed=Counter()
    total=0
    for z in vec:
        for v in vec:
            word=directions(z)+directions(v)
            swaps=0
            for i in range(1,len(word)):
                j=i
                while j and abs(word[j-1])>abs(word[j]):
                    a,b=word[j-1:j+1]
                    # Before and after trace the two sides of the same signed
                    # square. Its positively oriented base can differ on both axes.
                    signed[(abs(a),abs(b),a>0,b>0)]+=1
                    word[j-1],word[j]=b,a
                    j-=1
                    swaps+=1
            assert swaps==abs(z[1]*v[0])+abs(z[2]*v[0])+abs(z[2]*v[1])
            assert reduce_word(word)==directions(tuple(a+b for a,b in zip(z,v)))
            total+=swaps
    assert len(signed)==12 and all(t>0 for t in signed.values())
    return {"ordered_path_pairs":len(vec)**2,"perpendicular_swaps":total,
            "axis_and_sign_cases":len(signed)}


def convolution(a,b):
    c=Counter()
    for i,x in a.items():
        for j,y in b.items():
            c[i+j]+=x*y
    return {i:w for i,w in c.items() if w}


def cosines(x,order):
    vals=[Q(1),x]
    for _ in range(2,order+1):
        vals.append(2*x*vals[-1]-vals[-2])
    return vals


def check_fourier():
    cases=0
    separated=0
    for M in (1,2,3,5,8,15):
        f={j:Q(M-abs(j),M**2) for j in range(1-M,M)}
        d={j:int(j==0)-v for j,v in f.items()}
        poly={0:Q(1)}
        for _ in range(4):
            poly=convolution(poly,d)
        assert max(map(abs,poly),default=0)<=4*(M-1)
        assert sum(map(abs,poly.values()))<=16 and sum(poly.values())==0
        for x in (Q(-1),Q(-3,5),Q(-1,3),Q(0),Q(3,5),Q(99,101),Q(1)):
            c=cosines(x,4*M)
            F=sum(v*c[abs(j)] for j,v in f.items())
            K=sum(v*c[abs(j)] for j,v in poly.items())
            assert 0<=F<=1 and K==(1-F)**4
            assert 1-F<=Q(M*M-1,6)*(1-x)
            if M*M*(1-x)>=8:
                assert K>=Q(3,4)**4
                separated+=1
            cases+=1
    # R=4, P=0 versus P=2π (within the representative cube). The corresponding
    # k values have cosines 1 and 0. Their stride-R phases agree; F_4 separates.
    c0,c1=cosines(Q(1),4),cosines(Q(0),4)
    assert c0[4]==c1[4]==1
    def f4(c):
        return sum(Q(4-abs(j),16)*c[abs(j)] for j in range(-3,4))
    assert f4(c0)==1 and f4(c1)==0
    return {"exact_fourier_tests":cases,"far_angle_floor_tests":separated,"stride_alias_separated":True}


def check_pareto_and_wrapping():
    for A in map(Q,(1,2,3,8,31,128)):
        # For the law P(U>t)=min(1,t^-6), split the layer-cake integral at t=1.
        layer=8/A**8*(Q(1,8)+(A*A-1)/2)
        assert layer==4/A**6-3/A**8 and 1/A**6<=layer<=4/A**6
    def center(x,R):
        # Momentum in units of π, representative [-R,R).
        return (x+R)%(2*R)-R
    wrapped=0
    for R in (3,7):
        for legs in product(range(-R,R),repeat=3):
            wrapped+=1
            assert abs(center(sum(legs),R))<=sum(map(abs,legs))
            # For every positive threshold a large representative forces a large leg.
            h=abs(center(sum(legs),R))
            assert h<=3*max(map(abs,legs))
    return {"pareto_eighth_moment_cases":6,"wrapped_three_leg_cases":wrapped}

if __name__=="__main__":
    print(json.dumps({"paths":check_paths(),"fejer":check_fourier(),
                      "tails":check_pareto_and_wrapping()},indent=2))

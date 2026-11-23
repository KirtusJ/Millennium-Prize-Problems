"""Exact open-path geometry, finite SU(2)-subgroup strips, and a failed reflection control."""
from fractions import Fraction
from itertools import product
from math import cos, pi


def invert(word):
    return [(edge,-sign) for edge,sign in reversed(word)]


def path(start, steps):
    point = list(start)
    word = []
    for step in steps:
        axis, sign = abs(step)-1, 1 if step>0 else -1
        if sign<0:
            point[axis] -= 1
        word.append(((tuple(point),axis),sign))
        if sign>0:
            point[axis] += 1
    return word, tuple(point)


def reduced(word):
    out = []
    for edge, sign in word:
        if out and out[-1] == (edge,-sign):
            out.pop()
        else:
            out.append((edge,sign))
    return out


def trace_word(word):
    """Canonical unoriented cyclic word for a normalized SU(2) trace."""
    word = reduced(word)
    while len(word) >= 2 and word[0] == invert(word[-1:])[0]:
        word = word[1:-1]
    if not word:
        return ()
    return min(tuple(w[i:] + w[:i]) for w in (word, invert(word)) for i in range(len(w)))


def staple_checks():
    count = 0
    origin = (0, 0, 0, 0)
    for normal, width in product(range(1, 5), repeat=2):
        if normal == width:
            continue
        for s, t in product(range(7), repeat=2):
            lower, end_a = path(origin, [-normal]*s + [width] + [normal]*s)
            upper, end_b = path(origin, [normal]*t + [width] + [-normal]*t)
            assert end_a == end_b
            _, base = path(origin, [-normal]*s)
            boundary, end = path(base, [normal]*(s+t) + [width] + [-normal]*(s+t) + [-width])
            assert base == end
            assert trace_word(invert(lower) + upper) == trace_word(boundary)
            count += 1
    print(f"{count} reflected staple pairs equal the rectangle trace word")


def segments(x):
    return [[(i+1 if v>=0 else -i-1)]*abs(v) for i,v in enumerate(x)]


def path_checks():
    zero=(0,0,0,0)
    count=0
    for x in product((-2,0,1),repeat=4):
        blocks=segments(x)
        for edge in (1,-1,2,-2,3,-3,4,-4):
            axis=abs(edge)-1
            before=sum(blocks,[])+[edge]
            for j in range(3,axis,-1):
                prefix=sum(blocks[:j],[])
                after=prefix+[edge]+sum(blocks[j:],[])
                old_word,_=path(zero,before)
                new_word,_=path(zero,after)
                pref_word,base=path(zero,prefix)
                across=blocks[j]
                rhombus,end=path(base,across+[edge]+[-v for v in reversed(across)]+[-edge])
                assert end==base
                assert reduced(old_word+invert(new_word))==reduced(pref_word+rhombus+invert(pref_word))
                before=after
            final,target=path(zero,before)
            assert reduced(final)==path(zero,sum(segments(target),[]))[0]
            count+=1
    print(f"{count} signed edge insertions, including crossings of negative coordinate runs")


def qmul(a,b):
    # ±1, ±2, ±3, ±4 encode ±1, ±i, ±j, ±k.
    i,j=abs(a)-1,abs(b)-1
    sign=1 if a*b>0 else -1
    if not i or not j: return sign*(1+max(i,j))
    if i==j: return -sign
    return sign*(7-i-j)*(1 if (i,j) in [(1,2),(2,3),(3,1)] else -1)


def strip_law():
    # Open two-dimensional strips in axial gauge have independent plaquettes.
    # At beta=log k the Wilson weights multiplied by k are k², 1, and six k's.
    for k in (2,16,256,4096):
        weights={**{x:k for x in [-4,-3,-2,2,3,4]},1:k*k,-1:1}
        total=sum(weights.values())
        r=Fraction(k*k-1,total)
        previous={1:1}
        for n in range(1,25):
            counts={g:0 for g in weights}
            for a,ca in previous.items():
                for b,cb in weights.items():
                    counts[qmul(a,b)]+=ca*cb
            previous=counts
            reading=Fraction(counts[1]-counts[-1],total**n)
            assert reading==r**n and 1-reading<=n*(1-r)
        if k==4096:
            print(f"Length-24 deficit / linear ceiling, k={k}: {float((1-reading)/(24*(1-r))):.9f}")


def no_reflection():
    r=Fraction(3,5)
    two=2*r*r-1
    assert two-r*r==Fraction(-16,25)
    n=64
    assert 1-cos(n*pi/n)>n*(1-cos(pi/n))
    print("Coherent rotation violates the length bound and the 2-by-2 staple Gram test")


if __name__=="__main__":
    staple_checks()
    path_checks()
    strip_law()
    no_reflection()

"""Exact two-slice moment checks with no fitted spectral or contour parameters."""
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial


@lru_cache(None)
def one_color(a, b, v, k):
    if a+b==0:
        return F(1)
    if a:
        same=(a-1)*v*one_color(a-2,b,v,k) if a>1 else 0
        cross=b*k*one_color(a-1,b-1,v,k) if b else 0
        return same+cross
    return (b-1)*v*one_color(0,b-2,v,k) if b>1 else F(0)


@lru_cache(None)
def power_moment(colors, i, j, v, k):
    if colors==1:
        return one_color(2*i,2*j,v,k)/F(2**(i+j))
    return sum(comb(i,a)*comb(j,b)*power_moment(1,a,b,v,k)*
               power_moment(colors-1,i-a,j-b,v,k)
               for a in range(i+1) for b in range(j+1))


def winding_polynomials(n):
    # T_{m+1}(1-D)=2(1-D)T_m(1-D)-T_{m-1}(1-D).
    prev, curr = [1], [1,-1]
    result=[]
    for _ in range(n):
        result.append([1-curr[0]]+[-x for x in curr[1:]])
        nxt=[0]*(len(curr)+1)
        for i,x in enumerate(curr):
            nxt[i]+=2*x
            nxt[i+1]-=2*x
        for i,x in enumerate(prev):
            nxt[i]-=x
        prev,curr=curr,nxt
    return result


def determinant(rows):
    # Small exact determinants by cofactor expansion.
    if len(rows)==1:
        return rows[0][0]
    return sum((-1)**j*value*determinant([row[:j]+row[j+1:] for row in rows[1:]])
               for j,value in enumerate(rows[0]))


def controls():
    for v,k in ((F(5),F(1,3)),(F(91),F(-2)),(F(3,2),F(5,4))):
        def raw(i,j):
            return power_moment(3,i,j,v,k)
        def cov(i,j):
            return raw(i,j)-raw(i,0)*raw(0,j)
        def pair(p,q):
            return sum(a*b*cov(i,j) for i,a in enumerate(p) for j,b in enumerate(q) if a*b)
        words=winding_polynomials(4)
        gram=[[pair(x,y) for y in words] for x in words]
        assert (1-gram[1][0]/(4*gram[0][0]))/raw(1,0)==F(5,3)
        assert pair([0,-5*v,1], [0,-5*v,1])==F(15,2)*k**4
        amplitude=F(1)
        for n in range(1,5):
            amplitude*=F(factorial(2*n+1),4**n)
            order=n*(n+1)//2
            observed=determinant([row[:n] for row in gram[:n]])/gram[0][0]**order
            expected=2**(n*(n-1))*amplitude/F(3,2)**order
            assert observed==expected
            if n==2:
                assert observed==F(40,3)
        print(f"v={v}, K={k}: exact centered winding determinants through rank 4, 40/3 and 5/3 passed")


if __name__=="__main__":
    controls()

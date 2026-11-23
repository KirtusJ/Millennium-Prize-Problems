"""Test the residual gauge measure against twisted character integrals and independent frames."""
from fractions import Fraction as F
from itertools import combinations
import json
from math import prod,sqrt
from pathlib import Path
import sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import numpy as np
from scipy.special import ive,roots_legendre
from twisted import evaluate, evaluate_sources, geometry


def characters():
    for shape in [(1,1),(2,2),(3,2)]:
        for rev in (False,True):
            geo=geometry(shape,rev)
            n=len(geo[0])
            f=np.array([[((k+2*i)%5)-2 for k in range(n)] for i in range(3)])
            r=evaluate_sources(geo,f)
            assert r['A0']==F(n,8)
            assert r['V1']==[F(int(f[i]@f[j]),4) for i,j in combinations(range(3),2)]
            assert r['T1']['wilson']==F(3*int(np.sum(np.prod(f,axis=0))),4)
    x,w=roots_legendre(60)
    angles=(x+1)*np.pi/2
    s=np.sin(angles)**2
    # sin²(a) da and sin²(b) db under Haar, d cos(theta)/2 for their axes.
    measure=(w*s)[:,None,None]*(w*s)[None,:,None]*w[None,None,:]/2
    deficit=2*(1-s[:,None,None]*s[None,:,None]*(1-x**2)[None,None,:])
    for beta in (.5,2.,8.):
        integral=np.sum(measure*np.exp(-beta*deficit))
        expected=(ive(0,beta)-np.exp(-2*beta))/beta
        assert abs(integral-expected)<2e-13
    print('twisted one-face compact quadrature and six two-dimensional gauge-slice source tests passed')


def main():
    characters()
    origins=[(t,0,0,0) for t in (0,2,4)]
    for shape in [(6,1,1,1),(6,2,1,1)]:
        results=[]
        for dual in (False,True):
            a=evaluate(shape,origins,dual)
            b=evaluate(shape,origins,dual,True)
            assert a['A0']==b['A0'] and a['V1']==b['V1']
            assert a['pairs']==b['pairs'] and a['T0']==b['T0']
            for key in ('wilson','abelian'):assert a['T1'][key]==b['T1'][key]
            results.append(a)
        a,b=results
        assert a['T0']==-b['T0'] and a['pairs']==b['pairs']
        s=(a['T1']['wilson']+b['T1']['wilson'])/2
        print('exact two frames',shape,'paired Wilson R1',float(s)/sqrt(float(prod(a['pairs']))))
    from certify_twist import SKEW
    for label,points in [('',origins),('skew-',SKEW)]:
        verify_large(label,points)


def verify_large(label,points):
    from twisted import sources
    shape=(6,2,2,2)
    faces=geometry(shape)[0]
    for dual in (False,True):
        mask=sources(shape,faces,points,dual)
        links=[]
        for row in mask:
            marked=set()
            for (x,a,b),weight in zip(faces,row):
                if weight:
                    for along,other in [(a,b),(b,a)]:
                        y=tuple((z+int(i==other))%shape[i] for i,z in enumerate(x))
                        marked.update([(x,along),(y,along)])
            links.append(marked)
        overlaps=[len(x&y) for x,y in combinations(links,2)]
        if label or not dual:assert overlaps==[0,0,0]
        else:assert min(overlaps)>0
        print(label+('star' if dual else 'cube'),'pairwise shared links',overlaps)
    large=[]
    for name in ('cube','star'):
        ref=json.loads((HERE/'evidence'/('twisted-'+label+name+'.json')).read_text())
        # Independent chart, different spanning tree and a prime unused by the CRT.
        p=193
        r=evaluate((6,2,2,2),points,name=='star',True,p)
        def reduce(v):
            v=F(v);return v.numerator*pow(v.denominator,-1,p)%p
        assert [reduce(v) for v in ref['V0']]==r['pairs'] and reduce(ref['T0'])==r['T0']
        for key in ('wilson','abelian'):assert reduce(ref['T1'][key])==r['T1'][key]
        print(label+name,'opposite frame mod',p,r['T0'],r['T1']['wilson'],flush=True)
        large.append(ref)
    a,b=large
    assert F(a['T0'])==-F(b['T0'])!=0 and a['V0']==b['V0']
    for k in ('wilson','abelian'):
        s=(F(a['T1'][k])+F(b['T1'][k]))/2
        print('6 x 2 x 2 x 2 paired',label,k,'T1',s,'R1',float(s)/sqrt(float(prod(map(F,a['V0'])))))


if __name__=='__main__':main()

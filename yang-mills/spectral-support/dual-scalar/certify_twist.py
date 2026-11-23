"""Recover signed rational first coefficients for the nondegenerate twisted box by CRT."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import numpy as np
from sympy import prevprime
from twisted import covariances, evaluate_sources, expansion_terms, geometry, sources

SHAPE=(6,2,2,2)
ORIGINS=[(t,0,0,0) for t in (0,2,4)]
SKEW=[(0,0,0,0),(2,1,1,0),(4,1,0,1)]


def integer_bound(geo,f):
    faces,words,B,active,density=geo
    D,C,pairs,t=covariances(B,active,f,None)
    M=np.array([max(abs(x) for x in C[:,m].flat) for m in range(8)],dtype=object)
    w=np.zeros(8,dtype=object);w[0]=1
    for i in range(3):w[1<<i]=D*int(max(f[i]))
    fourth,triples=expansion_terms(words)
    # Upper bounds for the signed polynomial coefficients before dividing by 24 D^6.
    # V sums absolute cubic coefficients over all triples at each source mask.
    V=np.zeros(8,dtype=object)
    for edges,weights in triples.items():
        if all(active[a,i] for a,i in enumerate(edges)):
            V[0]+=abs(sum(weights.values()))
            for i in range(3):
                V[1<<i]+=D*abs(sum(int(f[i,p])*v for p,v in weights.items()))
    def mul(x,y):
        return np.array([sum(int(x[j])*int(y[m^j]) for j in range(8) if j&m==j)
                         for m in range(8)],dtype=object)
    haar=8*D**2*3*int(density.sum())*M[7]
    quart=15*D*sum(abs(row[1]) for row in fourth)*mul(w,mul(M,M))[7]
    cubic=12*mul(mul(V,V),mul(M,mul(M,M)))[7]
    abel=9*D*len(faces)*mul(w,mul(16*M,16*M))[7]
    return D,int(max(haar+quart+cubic,abel)),pairs,t


def certify(orientation,skew=False):
    geo=geometry(SHAPE)
    f=sources(SHAPE,geo[0],SKEW if skew else ORIGINS,orientation=='star')
    den,bound,pairs,t0=integer_bound(geo,f)
    denominator=24*den**6
    values=dict.fromkeys(('wilson','haar','quartic','cubic','abelian'),0)
    modulus=1
    rows=[]
    p=1000003
    while modulus<=2*bound:
        p=int(prevprime(p))
        if denominator%p==0:continue
        r=evaluate_sources(geo,f,p)
        assert all(int(v.numerator)*pow(int(v.denominator),-1,p)%p==u
                   for v,u in zip(pairs,r['pairs']))
        assert t0.numerator*pow(t0.denominator,-1,p)%p==r['T0']
        for key,z in values.items():
            target=r['T1'][key]*denominator%p
            values[key]=z+modulus*((target-z)*pow(modulus,-1,p)%p)
        modulus*=p
        rows.append(dict(p=p,**r['T1']))
        print(orientation,'prime',p,'certified modulus bits',modulus.bit_length(),flush=True)
    for key,z in values.items():
        if 2*z>modulus:z-=modulus
        assert abs(z)<=bound
        values[key]=F(z,denominator)
    assert values['wilson']==sum(values[k] for k in ('haar','quartic','cubic'))
    return dict(shape=SHAPE,orientation=orientation,chord_denominator=str(den),
                common_denominator=str(denominator),numerator_bound=str(bound),modulus=str(modulus),
                residues=rows,V0=list(map(str,pairs)),T0=str(t0),T1={k:str(v) for k,v in values.items()})


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('orientation',choices=['cube','star']);p.add_argument('--write',action='store_true')
    p.add_argument('--skew',action='store_true',help='use three link-disjoint star supports')
    args=p.parse_args()
    data=certify(args.orientation,args.skew)
    if args.skew:data['origins']=SKEW
    raw=json.dumps(data,indent=2,sort_keys=True)+'\n'
    path=HERE/'evidence'/('twisted-'+('skew-' if args.skew else '')+args.orientation+'.json')
    if args.write:path.write_text(raw)
    else:assert path.read_text()==raw
    print('exact',args.orientation,'T0',data['T0'],'T1',data['T1']['wilson'],flush=True)

if __name__=='__main__':main()

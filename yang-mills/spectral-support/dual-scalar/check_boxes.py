"""Verify Hodge complementation, reciprocal sources and compact response in exact arithmetic."""
import argparse
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
from sympy import Matrix
from dual_box import box, cube_sources, experiment, face_map, relative_box
from response import inverse_jets


def abelian_local(B,f):
    den,C,steps=inverse_jets(B,f)
    P=B@C[0]@B.T
    total=0
    for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:
        I,J,K=[np.flatnonzero(f[z]) for z in (i,j,k)]
        ij=P[np.ix_(I,J)]
        ik=P[np.ix_(I,K)]
        jk=P[np.ix_(J,K)]
        gj=(ij**2)@f[j,J]
        hk=(ik**2)@f[k,K]
        mixed=(((ij*f[j,J])@jk)*(ik*f[k,K])).sum(axis=1)
        total+=np.sum(f[i,I]*(2*gj*hk-2*(den-2*np.diag(P)[I])*mixed))
    return F(3*int(total),8*den**4)


def general_weights():
    shape=(2,1,1,1)
    p,_,B=box(shape);d,_,G=relative_box(shape)
    idx,signs=face_map(p,d)
    B=Matrix(B);G=Matrix(signs[:,None]*G[idx])
    weights=Matrix.diag(*[2+(3*i%7) for i in range(len(p))])
    H=B.T*weights*B
    D=G.T*weights.inv()*G
    # Normalized determinants remove the tree-basis covolumes.
    assert H.det(method='domain-ge')*(G.T*G).det()==weights.det()*D.det(method='domain-ge')*(B.T*B).det()
    K=B*H.inv()*B.T;J=G*D.inv()*G.T
    assert J==weights-weights*K*weights
    print('reciprocal nonconstant rational weights: full covariance and normalized determinant agree')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--write',action='store_true')
    args=p.parse_args()
    general_weights()
    data={}
    for shape,times in [((5,1,1,1),(0,2,4)),((7,1,1,1),(1,3,5)),
                        ((7,1,1,1),(0,2,6)),((5,2,1,1),(0,2,4))]:
        origins=[(t,0,0,0) for t in times]
        r,s=experiment(shape,origins)
        r2,s2=experiment(shape,origins,True)
        assert r['triangle']==-s['triangle']!=0 and r['pairs']==s['pairs']
        out=dict(shape=shape,times=times,V0=list(map(str,r['pairs'])),cube_T0=str(r['triangle']),
                 star_T0=str(s['triangle']),chords=[r['chords'],s['chords']])
        for model in ('wilson','abelian','matched'):
            assert r['A'][model]==r2['A'][model] and s['A'][model]==s2['A'][model]
            u,v=-r['A'][model][7],-s['A'][model][7]
            t1=(u+v)/2
            out[model]=dict(cube_T1=str(u),star_T1=str(v),paired_T1=str(t1),
                            normalized_squared=str(t1**2/prod(r['pairs'])))
        faces,_,B=box(shape)
        compact=F(out['abelian']['paired_T1'])
        assert abelian_local(B,cube_sources(faces,origins))==compact
        t=F(out['wilson']['paired_T1'])
        assert t>compact>0
        out['improved_T1']=str(t-compact)
        data['x'.join(map(str,shape))+'@'+','.join(map(str,times))]=out
        root=sqrt(float(prod(r['pairs'])))
        print(shape,times,'R1 Wilson, circle, improved',*[float(x)/root for x in (t,compact,t-compact)],flush=True)
    raw=json.dumps(data,sort_keys=True,indent=2)+'\n'
    path=HERE/'evidence/box-pairs.json'
    if args.write:path.write_text(raw)
    else:assert path.read_text()==raw

if __name__=='__main__':main()

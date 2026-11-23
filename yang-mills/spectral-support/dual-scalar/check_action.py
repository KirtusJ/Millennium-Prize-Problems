"""Exact effect of adding lambda times the squared plaquette deficit, in the twisted box."""
from fractions import Fraction as F
import json
from math import prod,sqrt
from pathlib import Path
import sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import numpy as np
from twisted import covariances,geometry,jets_mul,sources
from certify_twist import SHAPE,ORIGINS


def bilinear(x,y):
    return x.sum(axis=0)*y.sum(axis=0)+2*(x*y).sum(axis=0)


def compute(geo,f,local):
    faces,words,B,active,density=geo
    D,C,pairs,t=covariances(B,active,f,None)
    W=np.zeros((8,len(faces)),dtype=object);W[0]=1
    for i,row in enumerate(f):W[1<<i]=D*row.astype(object)
    var=np.stack([np.stack([np.sum((B[c]@cm)*B[c],axis=1) for cm in C[c]]) for c in range(3)])
    def mul(x,y):return jets_mul(x,y,None)
    trace=var.sum(axis=0)
    # Minus sign of the action cancels the third-derivative insertion sign.
    quartic=mul(W,mul(trace,trace)+2*sum(mul(v,v) for v in var)).sum(axis=1)
    direct=F(int(quartic[7]),4*D**5)
    if not local:return direct,None
    P=[B[c]@C[c,0]@B[c].T for c in range(3)]
    answer=0
    for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:
        I,J,K=[np.flatnonzero(f[z]) for z in (i,j,k)]
        gj=[];hk=[];loops=[];diagonal=[]
        for p in P:
            a,b,c=p[np.ix_(I,J)],p[np.ix_(J,K)],p[np.ix_(I,K)]
            gj.append((a**2)@f[j,J]);hk.append((c**2)@f[k,K])
            loops.append((((a*f[j,J])@b)*(c*f[k,K])).sum(axis=1))
            diagonal.append(D-2*np.diag(p)[I])
        contact=bilinear(np.stack(diagonal),np.stack(loops))
        product=bilinear(np.stack(gj),np.stack(hk))
        answer+=np.sum(f[i,I]*(contact-product))
    return direct,F(int(answer),2*D**4)


def main():
    geo=geometry(SHAPE)
    absolute,local=compute(geo,sources(SHAPE,geo[0],ORIGINS,False),True)
    relative,_=compute(geo,sources(SHAPE,geo[0],ORIGINS,True),False)
    assert (absolute+relative)/2==local
    rows=[json.loads((HERE/'evidence'/('twisted-'+name+'.json')).read_text()) for name in ['cube','star']]
    w=sum(F(r['T1']['wilson']) for r in rows)/2
    a=sum(F(r['T1']['abelian']) for r in rows)/2
    norm=sqrt(float(prod(map(F,rows[0]['V0']))))
    print('twisted action derivative per unit lambda',local,'normalized',float(local)/norm)
    print('finite-twist departure from -10 Abelian',float(local+10*a)/norm)
    print('normalized response for D+D^2/10',float(w+local/10)/norm)

if __name__=='__main__':main()

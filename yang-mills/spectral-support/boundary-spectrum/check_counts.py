"""Finite spatial spectra for the open cube and periodic zero-flux Gaussian control."""
from itertools import product
import numpy as np
from scipy.linalg import cho_factor, cho_solve, eigvalsh


def incidence(side, periodic):
    cells=list(product(range(side),repeat=3))
    index={p:i for i,p in enumerate(cells)}
    edges=[]
    for p,u in index.items():
        for k in range(3):
            if p[k]==0 and not periodic:
                edges.append((u,-1,k))
            q=list(p)
            q[k]+=1
            if periodic:
                q[k]%=side
            edges.append((u,index.get(tuple(q),-1),k))
    H=np.zeros((side**3,len(edges)))
    for j,(u,v,_) in enumerate(edges):
        H[u,j]=1
        if v>=0:
            H[v,j]-=1
    return H,edges


def main():
    for n in (2,3,5,8,10):
        H,e=incidence(n,False)
        P=np.eye(len(e))-H.T@cho_solve(cho_factor(H@H.T),H)
        K=6*P**2
        row=np.sum(K,axis=1)
        assert np.max(np.abs(row-6*np.diag(P)))<2e-13
        assert abs(np.sum(row-4)-6*n*n)<2e-9 and np.min(row)>4-1e-12
        spectrum=eigvalsh(K,driver='evr',subset_by_value=(4,6),check_finite=False)
        counts=[int(np.count_nonzero(spectrum>t)) for t in (4.0119,4.105,4.3929)]
        assert counts[0]>=6*((n-2)//8)**2 and counts[1]>=12*max(0,(n-6)//7)
        assert np.sum(spectrum-4)<=6*n*n+1e-9
        print('side',n,'three threshold counts',counts,'largest',float(max(spectrum)),flush=True)
    for n in (3,4):
        H,e=incidence(n,True)
        # Remove one redundant divergence row and all three harmonic fluxes.
        harmonic=np.array([[int(k==a) for _,_,k in e] for a in range(3)])/np.sqrt(n**3)
        H=np.vstack([H[1:],harmonic])
        P=np.eye(len(e))-H.T@cho_solve(cho_factor(H@H.T),H)
        K=6*P**2
        exact=4*(1-1/n**3)
        assert np.max(np.abs(K.sum(axis=1)-exact))<2e-13
        assert abs(eigvalsh(K,subset_by_index=(len(e)-1,len(e)-1))[0]-exact)<2e-13
        print('periodic Maxwell box',n,'exact norm 4(1-1/V)',exact)


if __name__=='__main__':
    main()

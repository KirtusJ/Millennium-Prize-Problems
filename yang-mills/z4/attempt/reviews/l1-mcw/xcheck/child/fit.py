"""Spectral analysis of data_v1.json (T=512 ~ T->inf). Predicates (fixed before run):
 F1 fit C(t)=sum_{m=1..3} w_m exp(-E_m t), E_m=4*asinh(sqrt(m)) (pair of photons, sinh^2(w/2)=m, phat^2=4m), t=1..8 exact LS:
    max rel residual < 1e-6 for each of S,A1,E (tolerance: P(tau)^2 roundoff 1e-32 vs e^{-3.5 t}... t<=8 gives rel 1e-12 noise; 1e-6 is generous)
 F2 same fit incl. t=0: report residual (contact term allowed to fail; informational)
 F3 E1 = 3.52549435 to 1e-8 (auditor value) ; w1/C(0) vs 0.046875
 F4 T-> inf: T=32,48,64,256,512 ratios C(t)/C(0) t=0..6 agree to 1e-10 abs
"""
import json,numpy as np
r=json.load(open('data_v1.json'))['out']
fails=[]
Ts=['32','48','64','256','512']
for X in ('S','A1','E'):
    ref=np.array(r['512'][X][:7]); ref=ref/ref[0]
    d=max(np.abs(np.array(r[T][X][:7])/r[T][X][0]-ref).max() for T in Ts)
    print(X,'F4 maxdiff',d, 'PASS' if d<1e-10 else 'FAIL')
Em=np.array([4*np.arcsinh(np.sqrt(m)) for m in (1,2,3)])
print('E_m',Em, 'auditor E1 diff',Em[0]-3.52549435)
for X in ('S','A1','E'):
    C=np.array(r['512'][X][:13])
    for t0,lab in ((1,'F1'),(0,'F2')):
        t=np.arange(t0,9); A=np.exp(-np.outer(t,Em))
        w,*_=np.linalg.lstsq(A,C[t0:9],rcond=None)
        res=np.abs(A@w-C[t0:9]).max()/C[t0:9].max()
        print(X,lab,'w=',w,'w/C0=',w/C[0],'rel res',res,'PASS' if (lab=='F2' or res<1e-6) else 'FAIL')
    # extrapolate beyond fit range check t=9..12
    t=np.arange(9,13);print('  pred t=9..12 rel err',np.abs(np.exp(-np.outer(t,Em))@w-C[9:13])/C[9:13])
    print('  C(t)/C(0)',C[:7]/C[0], 'ratio C(t+1)/C(t) t=4..7',C[5:9]/C[4:8],'e^-E1',np.exp(-Em[0]))

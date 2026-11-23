import numpy as np
out=open('results.txt','x')
def P(s):
    print(s); out.write(s+'\n')
def loop(links,G,L):
    # links: (base tuple, mu, sign)
    V=0.0
    for (x,m,s) in links:
        for (y,n,t) in links:
            if m==n:
                d=tuple((a-b)%L for a,b in zip(x,y))
                V+=s*t*G[d]
    return V
for L in (16,32):
    k=2*np.pi*np.fft.fftfreq(L)
    K=np.meshgrid(k,k,k,k,indexing='ij')
    K2=sum(2-2*np.cos(q) for q in K)
    K2[0,0,0,0]=1
    Gh=1/K2; Gh[0,0,0,0]=0
    G=np.fft.ifftn(Gh).real
    d=G[0,0,0,0]-G[1,0,0,0]
    P(f"L={L}: G(0)-G(e1)={d:.12f}  (1/8={0.125}); predicted (1/8)(1-1/L^4)={0.125*(1-1/L**4):.12f}")
    z=(0,0,0,0)
    def pt(a,b): return (a,b,0,0)
    plaq=[(pt(0,0),0,1),(pt(1,0),1,1),(pt(0,1),0,-1),(pt(0,0),1,-1)]
    rect=[(pt(0,0),0,1),(pt(1,0),0,1),(pt(2,0),1,1),(pt(1,1),0,-1),(pt(0,1),0,-1),(pt(0,0),1,-1)]
    # 1x2 : 2 links along dir 1, 1 along dir 2; fix: right side at x=2, top row at y=1
    rect=[(pt(0,0),0,1),(pt(1,0),0,1),(pt(2,0),1,1),(pt(1,1),0,-1),(pt(0,1),0,-1),(pt(0,0),1,-1)]
    P(f"L={L}: V(1x1 plaquette)={loop(plaq,G,L):.12f}  (expected 0.5)")
    P(f"L={L}: V(1x2 rectangle, (1,2)-plane)={loop(rect,G,L):.12f}")
out.close()

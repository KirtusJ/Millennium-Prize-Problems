"""Free theory, blocking factor 2: the rate at small coarse momentum in several directions, side 2^22.
Exploratory: the numbers were seen before this file was written, so it carries no predicate. It reports
(rate - limit) * N / |q| with limit = 0.674941363; equal values mean that the rate depends on a small momentum
through its length only. Output directions_result.txt (not overwritten). Command: python3 directions.py"""
import numpy as np, itertools
src=open('matrixbridge.py').read(); exec(src[src.index("def omega"):src.index("out=[];res={}")])
lim=0.674941363; N=2**22; out=[]
for q in ((1,0,0),(1,1,0),(1,1,1),(3,2,1),(8,5,3),(7,0,2)):
    g=blk(N,q)[0]; out.append("q=%s rate=%.12f (rate-limit)*N/|q| = %.6f"%(q,g,(g-lim)/np.linalg.norm(q)*N))
open('directions_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))

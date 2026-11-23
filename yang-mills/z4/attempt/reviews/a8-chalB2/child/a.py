"""Analysis of G_results.txt. Predicates as in g.py (P1..P4). Output to analysis.txt (mode x)."""
import numpy as np
d=np.loadtxt("G_results.txt"); g=d[:,3]; df=np.abs(d[:,3]-d[:,2])
n=np.arange(8,17); p,lc=np.polyfit(np.log(n),np.log(g[8:]),1)
loc=[-np.log(g[i+1]/g[i])/np.log((i+1)/i) for i in range(8,16)]
out=["G0 %.12f maxdiff256-128 %.2e"%(g[0],df.max()),"p %.4f c %.5f (continuum 1/pi^2=%.5f)"%(-p,np.exp(lc),1/np.pi**2),
"local p "+" ".join("%.3f"%x for x in loc),"P1 %s P2 %s P3 %s P4 %s"%(abs(g[0]-.5)<1e-3,df.max()<1e-4,(g[1:]>0).all(),3.7<-p<4.3),
"n^4 G: "+" ".join("%.4f"%(k**4*g[k]) for k in range(1,17))]
with open("analysis.txt","x") as f: f.write("\n".join(out)+"\n")
print("\n".join(out))

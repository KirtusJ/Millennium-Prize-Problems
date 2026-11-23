import numpy as np,json
def mul(a,b):
    w1,x1,y1,z1=a.T;w2,x2,y2,z2=b.T
    return np.stack([w1*w2-x1*x2-y1*y2-z1*z2,w1*x2+x1*w2+y1*z2-z1*y2,w1*y2-x1*z2+y1*w2+z1*x2,w1*z2+x1*y2-y1*x2+z1*w2],1)
cj=lambda a:a*np.array([1,-1,-1,-1])
r=np.random.default_rng(12345);N=2*10**6
def H():
    q=r.normal(size=(N,4));return q/np.linalg.norm(q,axis=1)[:,None]
u1,u2,u3=H(),H(),H()
P=lambda a,b:mul(mul(a,b),mul(cj(a),cj(b)))
t12=2*P(u1,u2)[:,0];t13=2*P(u1,u3)[:,0]
def st(x):return float(x.mean()),float(x.std(ddof=1)/np.sqrt(N))
a=st(t12);b=st(t12*t13)
res={"N":N,"seed":12345,"A(1/2,0)":{"mean":a[0],"se":a[1],"expected":0.5,"z":(a[0]-.5)/a[1],"compatible_4SE":abs(a[0]-.5)<4*a[1]},
"A(1/2,1/2)":{"mean":b[0],"se":b[1],"z_vs_0":b[0]/b[1],"sign":"positive" if b[0]>4*b[1] else "negative" if b[0]<-4*b[1] else "compatible with zero"}}
with open('results.json','x') as f:json.dump(res,f,indent=1)
with open('report.md','x') as f:f.write(f"""# SU(2) plaquette correlators (Haar MC, N={N}, seed 12345)
- A(1/2,0) = {a[0]:.5f} +/- {a[1]:.5f}; expected 0.5; z={res['A(1/2,0)']['z']:.2f}; compatible at 4SE: {res['A(1/2,0)']['compatible_4SE']}
- A(1/2,1/2) = {b[0]:.5f} +/- {b[1]:.5f}; z vs 0 = {res['A(1/2,1/2)']['z_vs_0']:.1f}; verdict: {res['A(1/2,1/2)']['sign']}
(Analytic cross-check: E[(trU)^4]/4 = 1/2.)
""")
print(open('report.md').read())

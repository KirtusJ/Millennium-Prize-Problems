import numpy as np, math
def ive1(z,N):
    t=2*np.pi*np.arange(N)/N
    return np.mean(np.exp(z*(np.cos(t)-1))*np.cos(t))
def series(z):
    s=0.0;term=z/2;k=0
    while k<200:
        s+=term; k+=1; term*=(z/2)**2/(k*(k+1))
    return s*math.exp(-z)
def rhs(z): return (1-1/(2*z))/math.sqrt(2*math.pi*z)-0.5*math.exp(-z)
zs=sorted(set(list(np.logspace(-6,math.log10(0.5),30))+list(np.linspace(0.5,100,50))+[100,200,300,500,700]+list(np.linspace(100,700,13))))
rows=[];maxconv=0;maxser=0
for z in zs:
    N=1024
    while True:
        a=ive1(z,N);b=ive1(z,2*N)
        if abs(a-b)<1e-15 or N>=65536: break
        N*=2
    maxconv=max(maxconv,abs(a-b))
    if z<=20: maxser=max(maxser,abs(b-series(z)))
    rows.append((z,b,rhs(z),b-rhs(z),2*N))
m=min(rows,key=lambda r:r[3])
with open('results.txt','x') as o:
    o.write("z ive1 rhs margin N\n")
    for r in rows:o.write("%.10g %.15e %.15e %.6e %d\n"%r)
    o.write("npoints %d\nmax |N vs 2N| %.3e\nmax |quad-series| (z<=20) %.3e\n"%(len(rows),maxconv,maxser))
    o.write("MIN margin %.6e at z=%.10g\nVERDICT %s (tol -1e-12)\n"%(m[3],m[0],"MET" if m[3]>=-1e-12 else "FAILED"))
print(len(rows),maxconv,maxser,m)
neg=[r for r in rows if r[3]<0];print(len(neg))
big=[r for r in rows if r[0]>=100];print(min(big,key=lambda r:r[3]))

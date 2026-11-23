import numpy as np
def simp(f,a,b,n):
    x=np.linspace(a,b,n+1);y=f(x);h=(b-a)/n
    return h/3*(y[0]+y[-1]+4*y[1:-1:2].sum()+2*y[2:-1:2].sum())
c=simp(np.sin,0,np.pi,2000)
with open('control.txt','x') as f: f.write("%.6f\n"%c)
print("%.6f"%c)
eps=lambda a:2*np.arcsinh(np.sin(a))
eta=0.05
def Sm(s):
    s=np.clip(s,0,1);return 3*s*s-2*s**3
def sq(e): return np.sqrt(np.maximum(e-eta,0))*Sm(((e-eta)/eta-0.5)/1.5)
T=np.sqrt(np.pi/2)
F1=lambda t:np.sqrt(2*eps(t*t))*2*t
F2=lambda t:np.sqrt(2)*sq(eps(t*t))*2*t
r={}
for n in (200000,400000,800000):
    r[n]=(2*simp(F1,0,T,n),2*simp(F2,0,T,n))
    print(n,"%.9f %.9f"%r[n])
cs,cr=r[800000]
ok=cs-np.pi*np.sqrt(6*eta)<=cr<=cs
print(cs,cr,cs-np.pi*np.sqrt(6*eta),ok)
with open('result.txt','x') as f: f.write("c*=%.9f c_rho=%.9f ineq=%s lower=%.6f\n"%(cs,cr,ok,cs-np.pi*np.sqrt(6*eta)))

import numpy as np
def gl(n,a,b):
    x,w=np.polynomial.legendre.leggauss(n); return (b-a)/2*x+(a+b)/2,(b-a)/2*w
t,w=gl(200,0,np.pi)
print("%.6f"%(2/np.pi*np.sum(w*np.exp(np.cos(t))*np.sin(t)**2)),file=open('control.txt','w'))
print(open('control.txt').read())
beta=64.;s=0.3;al=2*s*np.sqrt(1+s*s)
t,w=gl(400,0,np.pi)
logZ=beta+np.log(2/np.pi*np.sum(w*np.exp(beta*(np.cos(t)-1))*np.sin(t)**2))
def B(rho,ne,npq):
    u0=np.sqrt(1-rho**2);u1=rho
    e,we=gl(ne,0,np.pi/2)
    ph=2*np.pi*np.arange(npq)/npq; wp=2*np.pi/npq
    E,P,Q=np.meshgrid(e,ph,ph,indexing='ij')
    W=(we[:,None,None]*wp*wp*np.ones_like(E))*np.sin(E)*np.cos(E)/(2*np.pi**2)
    norm=W.sum()
    ip=u0*np.cos(E)*np.cos(P)+u1*np.sin(E)*np.cos(Q)
    L=beta*ip-beta*s*s*np.sin(E)**2-beta*al*np.sin(E)**2/2-logZ
    m=L.max()
    I=np.sum(W*np.exp(L-m))
    logB=-beta*s*s*rho**2+beta*al*rho**2/2+m+np.log(I)
    return np.exp(logB),norm
out=[]
for rho in (0,0.2):
    for ne,n in ((40,64),(80,128),(160,256)):
        b,nm=B(rho,ne,n); out.append("rho=%g ne=%d np=nq=%d B=%.10f norm=%.12f"%(rho,ne,n,b,nm)); print(out[-1])
open('report.txt','w').write("control Z(1)=%s\nbeta=64 s=0.3\n"%open('control.txt').read()+"\n".join(out)+"\n")

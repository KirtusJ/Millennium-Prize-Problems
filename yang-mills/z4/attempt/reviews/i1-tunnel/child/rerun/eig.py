import numpy as np, time
def lam(beta,s,h,L):
    n=int(round(2*L/h))+1
    x=np.linspace(-L,L,n); h=x[1]-x[0]
    w=np.exp(-beta*s*s*x*x)  # exp(-V/2), V=2 beta s^2 x^2
    G=np.sqrt(beta/(2*np.pi))*np.exp(-0.5*beta*(x[:,None]-x[None,:])**2)
    M=h*w[:,None]*G*w[None,:]
    return np.linalg.eigvalsh(M)[-1],n,h
cases=[(50,1.0,'beta=50 a=pi/2'),(50,np.sin(0.3),'beta=50 a=0.3'),(200,1.0,'beta=200 a=pi/2')]
out=open('result.txt','x')
def P(*a):
    t=' '.join(str(i) for i in a); print(t); out.write(t+'\n')
for beta,s,name in cases:
    h0=0.01/np.sqrt(beta); L=10/np.sqrt(beta)
    l1,n1,hh1=lam(beta,s,h0,L); l2,n2,hh2=lam(beta,s,h0/2,L)
    F=1/(s+np.sqrt(1+s*s))
    P(name,'s=%.12f'%s,'L=%.6f'%L)
    P('  h=%.8f N=%d lambda=%.10g'%(hh1,n1,l1))
    P('  h=%.8f N=%d lambda=%.10g'%(hh2,n2,l2))
    P('  convergence |diff|=%.3e'%abs(l1-l2))
    P('  formula=%.10g  rel diff (numeric-formula)/formula=%.6e'%(F,(l2-F)/F))

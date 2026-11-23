import numpy as np
beta=256.;h=1/np.sqrt(beta)
N=int(round(2*np.pi/h/4))*4;h=2*np.pi/N
x=-np.pi+np.arange(N)*h
d=x[:,None]-x[None,:]
K=sum(np.exp(-beta*(d+2*np.pi*k)**2/2) for k in(-1,0,1))*h*np.sqrt(beta/(2*np.pi))
e=2*np.arcsinh(np.abs(np.sin(x)));s=np.exp(-e/2)
T=s[:,None]*K*s[None,:]
H=N//2
A=T[:H,:H];B=T[:H,H:]
# sigma: i->i+H ; T commutes. even: A+B, odd: A-B
le=np.linalg.eigh((A+B+(A+B).T)/2)[0][-1]
lo=np.linalg.eigh((A-B+(A-B).T)/2)[0][-1]
m=np.log(le/lo)
out="N=%d h=%.8f\nlambda_e=%.12f\nlambda_o=%.12f\nm=%.10e\n-log(m)/sqrt(beta)=%.8f\n"%(N,h,le,lo,m,-np.log(m)/np.sqrt(beta))
open('result.txt','x').write(out);print(out)
open('answer.md','x').write("# Result\n\n```\n"+out+"```\nEven/odd sectors via T[:H,:H]+-T[:H,H:] (H=N/2).\n")

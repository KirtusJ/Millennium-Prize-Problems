import numpy as np
beta=64.0; N=40001
t=np.linspace(-1,1,N); h=t[1]-t[0]
w=np.ones(N); w[1:-1:2]=4; w[2:-1:2]=2; w*=h/3/2  # includes dt/2
def ls(J):
    r=np.zeros(3002); x=0.0   # r[n]=I_{n+1}/I_n, r[3000]=0
    for n in range(2999,-1,-1):
        r[n]=1/(2*(n+1)/beta+r[n+1])
    cp=np.concatenate([[1.0],np.cumprod(r[1:2*J+1])])  # cp[k]=prod_{n=1}^k r_n
    return cp[0:2*J+1:2]
def eps(J,a):
    P=np.zeros((J+1,N)); P[0]=1
    if J>=1: P[1]=t
    for n in range(1,J): P[n+1]=((2*n+1)*t*P[n]-n*P[n-1])/(n+1)
    P*=np.sqrt(2*np.arange(J+1)+1)[:,None]
    E=np.exp(-beta*np.sin(a)**2*(1-t))
    A=(P*(w*E))@P.T
    s=np.sqrt(ls(J)); M=s[:,None]*A*s[None,:]
    return -np.log(np.linalg.eigvalsh((M+M.T)/2)[-1])
with open('results.txt','x') as f:
    for name,a in (('pi/2',np.pi/2),('0.1',0.1)):
        for J in (60,120,200):
            l=f'a={name} beta=64 J={J} eps_eff={eps(J,a):.8f}'
            print(l); f.write(l+'\n')

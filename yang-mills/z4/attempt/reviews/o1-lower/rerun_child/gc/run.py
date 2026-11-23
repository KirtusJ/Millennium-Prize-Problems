import numpy as np
def buildT(N,beta):
    h=2*np.pi/N; i=np.arange(N); x=-np.pi+2*np.pi*i/N
    d=x[:,None]-x[None,:]
    K=h*sum(np.sqrt(beta/(2*np.pi))*np.exp(-beta*(d+2*np.pi*k)**2/2) for k in (-1,0,1))
    e=np.exp(-np.arcsinh(np.abs(np.sin(x)))) # exp(-eps/2)
    return e[:,None]*K*e[None,:]
out=[]
def P(s):
    print(s); out.append(s)
# control
N=8;T=buildT(8,1.0)
P("control symmetric max|T-T^T| = %.3e"%np.abs(T-T.T).max())
H=N//2; sg=(np.arange(N)+H)%N
Ts=T+T[:,sg]
E=Ts[:H,:H]
lt=np.linalg.eigvalsh(T)[-1]
le=np.max(np.linalg.eigvals(E).real)
P("control top eig T = %.15f, top eig even sector = %.15f, diff=%.3e"%(lt,le,abs(lt-le)))
P("control agree to 1e-12: %s"%(abs(lt-le)<1e-12))
# main
N=104;beta=16.0;H=N//2
T=buildT(N,beta); sg=(np.arange(N)+H)%N
P("main symmetric max|T-T^T| = %.3e"%np.abs(T-T.T).max())
w,V=np.linalg.eigh(T)
ev=[];od=[]
for k in range(N):
    v=V[:,k]; pe=np.linalg.norm(v-v[sg]); po=np.linalg.norm(v+v[sg])
    if pe<1e-8: ev.append(k)
    elif po<1e-8: od.append(k)
    else: P("unclassified eigvec %d w=%.6e pe=%.2e po=%.2e"%(k,w[k],pe,po))
ke=max(ev,key=lambda k:w[k]); ko=max(od,key=lambda k:w[k])
le,lo=w[ke],w[ko]
Da=le-lo
P("top overall index %d; ke=%d ko=%d"%(N-1,ke,ko))
P("lambda_e=%.17g lambda_o=%.17g"%(le,lo))
g=V[:,ke];f=V[:,ko]
A=np.zeros(N,bool);A[N//4:3*N//4]=True
B=~A
num=(T[np.ix_(A,B)]*(f[A][:,None]*g[B][None,:]-f[B][None,:]*g[A][:,None])).sum()
den=(f[A]*g[A]).sum()
if den<0: num,den=-num,-den
Db=num/den
P("Delta (a) = %.17g"%Da)
P("Delta (b) = %.17g"%Db)
P("rel diff = %.3e"%(abs(Da-Db)/abs(Da)))
open('result.txt','x').write("\n".join(out)+"\n")

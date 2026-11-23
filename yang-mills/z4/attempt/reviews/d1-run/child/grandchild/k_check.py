import numpy as np, itertools, json, math
R=4
def su2(phi):
    return np.diag([np.exp(1j*phi/4),np.exp(-1j*phi/4)])
def build(eta):
    phi=lambda x0: -eta-(math.pi-2*eta)*x0/4
    U={}
    for x in itertools.product(range(R+1),range(R),range(R),range(R)):
        U[(x,0)]=np.eye(2,dtype=complex)
        for mu in (1,2,3):
            U[(x,mu)]=su2(phi(x[0]))
    return U
def dyn(x,mu):
    if mu==0: return x[0]<=3
    return 1<=x[0]<=3
def shift(x,mu):
    y=list(x); y[mu]+=1
    if mu>0: y[mu]%=R
    return tuple(y)
def action(U):
    S=0.0
    for x in itertools.product(range(R+1),range(R),range(R),range(R)):
        for mu in range(4):
            for nu in range(mu+1,4):
                if mu==0 or nu==0:
                    pass
                # plaquette needs x+0 <= 4
                if (mu==0 or nu==0) and x[0]>=R: continue
                xm=shift(x,mu); xn=shift(x,nu)
                links=[(x,mu),(xm,nu),(xn,mu),(x,nu)]
                if not any(dyn(*l) for l in links): continue
                Up=U[(x,mu)]@U[(xm,nu)]@U[(xn,mu)].conj().T@U[(x,nu)].conj().T
                S+=1-0.5*np.trace(Up).real
    return S
def Sof(eta): return action(build(eta))
closed=lambda eta:3*R**4*(1-math.cos((math.pi-2*eta)/R**2))
e0=math.pi/4
def cd(h): return (Sof(e0+h)-Sof(e0-h))/(2*h)
d1=cd(1e-3); d2=cd(5e-4)
k1,k2=4*d1,4*d2
kr=(4*k2-k1)/3
kc=24*R**2*math.sin((math.pi-2*e0)/R**2)
S0=Sof(e0)
res=dict(S_V=S0,S_closed=closed(e0),S_diff=abs(S0-closed(e0)),k_h1em3=k1,k_h5em4=k2,k_richardson=kr,k_closed=kc,
 rel_err_richardson=abs(kr-kc)/kc,rel_err_h5e4=abs(k2-kc)/kc,
 pred_S=bool(abs(S0-closed(e0))<1e-9),pred_k=bool(abs(kr-kc)/kc<1e-6))
print(json.dumps(res,indent=1))
with open('result.json','x') as f: json.dump(res,f,indent=1)

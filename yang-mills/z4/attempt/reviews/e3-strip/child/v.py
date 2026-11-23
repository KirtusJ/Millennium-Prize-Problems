"""T59 free-field linearized Wilson loop norms. Predicates fixed BEFORE first run:
P1 |G(0)-0.154933|<5e-6 (quoted 6 digits)   P2 |G0-G(e1)-1/8|<1e-8 (quadrature tol)
P3 |V(1x1)-1/2|<1e-8   P4 V(1xw)<=w*V11+1e-8 for each of 7 w (count qualifying)
P5 V(wxw)<=w^2*V11+1e-8 for each of 7 w (count)   P6 slope(32->64) reported, no pass/fail
G(a,b,0,0)=int ive(a,2t)ive(b,2t)ive(0,2t)^2 dt on log-t Simpson grid [1e-9,T], plus analytic tail
int_T^inf (4 pi t)^-2 exp(-r^2/4t) dt. Result file opened mode 'x'."""
import numpy as np, sys, json
N=64
def ive_all(t):
    # exp(-x)I_n(x), x=2t, n=0..N, via periodic trapezoid of (1/pi) int_0^pi exp(x(cos th-1)) cos(n th)
    out=np.zeros((N+1,len(t)))
    ns=np.arange(N+1)[:,None]
    for k,tt in enumerate(t):
        x=2*tt
        Mth=int(max(256,12*np.sqrt(x)*np.pi/ 1.0))
        th=np.linspace(0,np.pi,Mth+1)
        e=np.exp(x*(np.cos(th)-1)); e[0]*=.5; e[-1]*=.5
        out[:,k]=(np.cos(ns*th)@e)/Mth
    return out
def Gtable(npts,T):
    u=np.linspace(np.log(1e-9),np.log(T),npts)  # npts odd
    t=np.exp(u); h=u[1]-u[0]
    w=np.ones(npts); w[1:-1:2]=4; w[2:-1:2]=2; w*=h/3; w*=t
    M=np.array([ivec(n_,t) for n_ in [0]]) if False else ive_all(t)
    M0=M[0]**2
    G=np.zeros((N+1,N+1))
    for a in range(N+1):
        G[a]=(M[a]*M0*w)@M.T
    a,b=np.meshgrid(range(N+1),range(N+1),indexing='ij')
    r2=a*a+b*b; c=r2/4.0
    with np.errstate(divide='ignore',invalid='ignore'):
        tail=np.where(r2>0,(1-np.exp(-c/T))/c,1.0/T)/(16*np.pi**2)
    return G+tail
def Gf(G,a,b): return G[abs(a),abs(b)]
def loop(m,n):  # m along dir0, n along dir1; links (mu,x,y,sign)
    L=[]
    for i in range(m): L.append((0,i,0,1)); L.append((0,i,n,-1))
    for j in range(n): L.append((1,m,j,1)); L.append((1,0,j,-1))
    return L
def V(G,L):
    s=0.0
    for (m1,x1,y1,s1) in L:
        for (m2,x2,y2,s2) in L:
            if m1==m2: s+=s1*s2*Gf(G,x1-x2,y1-y2)
    return s
if __name__=="__main__":
    npts=int(sys.argv[1]); T=float(sys.argv[2]); out=sys.argv[3]
    G=Gtable(npts,T)
    ws=[1,2,4,8,16,32,64]
    res={"npts":npts,"T":T,"G0":float(G[0,0]),"G0-Ge1":float(G[0,0]-G[1,0])}
    v11=V(G,loop(1,1)); res["V11"]=float(v11)
    res["V1w"]=[V(G,loop(1,w)) for w in ws]
    res["Vww"]=[V(G,loop(w,w)) for w in ws]
    res["ratio_lin"]=[v/(w*v11) for v,w in zip(res["V1w"],ws)]
    res["ratio_area"]=[v/(w*w*v11) for v,w in zip(res["Vww"],ws)]
    res["slope_1w"]=float(np.log(res["V1w"][6]/res["V1w"][5])/np.log(2))
    res["slope_ww"]=float(np.log(res["Vww"][6]/res["Vww"][5])/np.log(2))
    res["P1"]=bool(abs(res["G0"]-0.154933)<5e-6)
    res["P2"]=bool(abs(res["G0-Ge1"]-.125)<1e-8)
    res["P3"]=bool(abs(v11-.5)<1e-8)
    res["P4_count"]=int(sum(v<=w*v11+1e-8 for v,w in zip(res["V1w"],ws)))
    res["P5_count"]=int(sum(v<=w*w*v11+1e-8 for v,w in zip(res["Vww"],ws)))
    with open(out,"x") as f: json.dump(res,f,indent=1)
    print(json.dumps(res,indent=1))

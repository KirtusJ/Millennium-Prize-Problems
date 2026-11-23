"""prog2_model.py -- worker v1-chL (T180). Analytic steps of tun_lower.tex tested on the actual model (quaternions).
Predicates FIXED before the first run. Seeds fixed (numpy default_rng(20261123)). Tolerances: 1e-9 relative for
identities (double rounding after ~10 flops on O(1) numbers, with margin); inequalities strict up to 1e-12 absolute.
 M1 (Lemma exact (c),(d)) u' = u + R xi - (1-g0)u and |r_xi| <= 2 r_b^2|w| + (r_b+r_b^2)^2 on random x in X, xi in product ball, r_b in (0,1/2].
 M2 (Lemma exact (e),(f)) l l^T = S^2 I - u1u1^T - u2u2^T - 2ww^T ; singular values {S^2-2W, nu+, nu-}; l p = -kappa w.
 M3 (Lemma taylor) |F - Model| <= Err (stated form, with the stated Delta h bound) at random x in tube T, xi in product ball,
    eta in {0.4,0.1}, beta in {1e4,1e6}, r_b = L/sqrt(beta) <= s_-/8, with a concrete smooth chi (C^infty step).
    H_Psi, Lambda computed on a grid of 4e5 points (a numerical sup; slight underestimate possible -> report worst ratio).
 M4 (Lemma gauss) log J formula of the note == determinant formula (rel 1e-9); exact gap formula == direct gap (abs 1e-9);
    gap <= DG1' <= DG1 and -gap <= DG3' <= DG3 (DG1,DG3 only where sigma_w>0); random x in X (a_i arbitrary), random tilts.
    Also: Monte Carlo check of the determinant formula at one configuration (2e6 samples; |MC/J-1| < 5 standard errors).
 M5 (Lemma elem (infl)) sqrt(V(z)/2) <= sqrt(V(p)/2) + rho(s1+s2) + rho^2/sqrt(beta) for z within rho/sqrt(beta) per link.
 M6 (Lemma balls (II)) at the smallest beta meeting the four conditions (and 10x it), eta in {0.4,0.1}, M^2=MA2:
    for z in valley balls: G(z)-c1 >= e^{-1.5 rho_B^2}/2 and E(z)-c2 >= 1/2.
 M7 MEASURED ONLY: Monte Carlo of the true one-step defects at beta=1e4, eta=0.4, M^2=MA2 at 6 points of T:
    d1 = log A1 - log(true ratio for E1), d3 = log(true ratio for E3) - log A3 (Delta=0). Report vs margin m/2.
Result file mode 'x'.
"""
import numpy as np, math
from numpy import sqrt, log, exp, arcsinh as asinh, sin, cos, pi
rng=np.random.default_rng(20261123)
out=[]; fails=[]
def say(*a):
    s=' '.join(str(x) for x in a); print(s,flush=True); out.append(s)
def pred(name, ok, info=''):
    say(f'{name}: {"MET" if ok else "FAILED"} {info}')
    if not ok: fails.append(name)
def qmul(a,b):
    return np.concatenate([[a[0]*b[0]-a[1:]@b[1:]], a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:],b[1:])])
def unit(v): return v/np.linalg.norm(v)
def rand_unit(): return unit(rng.normal(size=3))
def cross_mat(u): return np.array([[0,-u[2],u[1]],[u[2],0,-u[0]],[-u[1],u[0],0]])
def ball_vec(r):  # uniform in 3-ball of radius r
    return rand_unit()*r*rng.random()**(1/3)
def ell_matrix(x01,u1,x02,u2):
    R1=x01*np.eye(3)+cross_mat(u1); R2=x02*np.eye(3)+cross_mat(u2)
    # l(xi) = R1 xi1 x u2 + u1 x R2 xi2 ;  a x u2 = -[u2]x a
    return np.hstack([-cross_mat(u2)@R1, cross_mat(u1)@R2])
hS=lambda S: 1+sqrt(1+S*S)/S
eS=lambda S: 2*asinh(S)
# ---------------- M1, M2
ok1=ok2=True; worst_r=0
for it in range(20000):
    a1,a2=rng.uniform(0,pi,2); n1,n2=rand_unit(),rand_unit()
    U1=np.concatenate([[cos(a1)],sin(a1)*n1]); U2=np.concatenate([[cos(a2)],sin(a2)*n2])
    rb=rng.uniform(1e-3,.5); xi1,xi2=ball_vec(rb),ball_vec(rb)
    g1=np.concatenate([[sqrt(1-xi1@xi1)],xi1]); g2=np.concatenate([[sqrt(1-xi2@xi2)],xi2])
    V1=qmul(U1,g1); V2=qmul(U2,g2)
    u1,u2=U1[1:],U2[1:]; w=np.cross(u1,u2)
    R1=U1[0]*np.eye(3)+cross_mat(u1)
    ok1&= np.allclose(V1[1:], u1+R1@xi1-(1-g1[0])*u1, atol=1e-12)
    l=ell_matrix(U1[0],u1,U2[0],u2); xi=np.concatenate([xi1,xi2])
    r=np.cross(V1[1:],V2[1:])-w-l@xi; bound=2*rb*rb*np.linalg.norm(w)+(rb+rb*rb)**2
    worst_r=max(worst_r,np.linalg.norm(r)/bound); ok1&= np.linalg.norm(r)<=bound+1e-12
    S2=u1@u1+u2@u2; W=w@w
    ok2&= np.allclose(l@l.T, S2*np.eye(3)-np.outer(u1,u1)-np.outer(u2,u2)-2*np.outer(w,w), atol=1e-12)
    sv=np.sort(np.linalg.svd(l,compute_uv=False)**2)
    G=np.outer(u1,u1)+np.outer(u2,u2); nu=np.linalg.eigvalsh(G)[1:]   # the two nonzero (span) eigenvalues
    ok2&= np.allclose(sv,np.sort(np.array([S2-2*W,nu[0],nu[1]])),atol=1e-10)
    P1,P2=rng.normal(size=2)
    p=-np.concatenate([P1*unit(u1),P2*unit(u2)])
    kap=P1*cos(a1)/sin(a1)+P2*cos(a2)/sin(a2)
    ok2&= np.allclose(l@p,-kap*w,atol=1e-9*(1+abs(kap)))
pred('M1',ok1,f'20000 cases, worst |r|/bound={worst_r:.3f}')
pred('M2',ok2,'20000 cases')
# ---------------- concrete ansatz
def smoothstep(x):
    x=np.clip(x,0,1); A=np.where(x>0,exp(-1/np.maximum(x,1e-300)),0.); B=np.where(x<1,exp(-1/np.maximum(1-x,1e-300)),0.)
    return A/(A+B)
def make(eta):
    am=math.asin(math.sinh(eta)); r0=math.sqrt(eta*math.sinh(eta)/4); ell=r0/3; th0=.5
    def chi(a):
        a=np.asarray(a,float)
        return np.where(a<=pi/2, smoothstep((a-am/2)/(am/2)), smoothstep((pi-am/4-a)/(am/4)))
    dPsi=lambda a: chi(a)*sqrt(2*(2*asinh(sin(a))+eta))
    GLx,GLw=np.polynomial.legendre.leggauss(60)
    def Psi_diff(a,b):   # Psi(b)-Psi(a)
        if a==b: return 0.
        return ((b-a)/2*GLw*dPsi((b-a)/2*GLx+(a+b)/2)).sum()
    grid=np.linspace(1e-6,pi-1e-6,400001); d=dPsi(grid); dd=np.gradient(d,grid)
    HPsi=max(np.abs(dd).max(), np.abs(d*cos(grid)/sin(grid)).max()); Lam=d.max()
    Theta=lambda a: th0*(sqrt(a*a+ell*ell)-ell); dTheta=lambda a: th0*a/sqrt(a*a+ell*ell)
    m0=(1-math.exp(-3*eta/4))/2; m1=(1-math.exp(-1/16))/2
    MA2=2*math.sqrt(2+r0**2)+max(math.log(1/m1)/math.tanh(eta), .75*eta/math.tanh(eta)+math.log(1/m0))
    return dict(am=am,r0=r0,ell=ell,th0=th0,dPsi=dPsi,Psi_diff=Psi_diff,HPsi=HPsi,Lam=Lam,Theta=Theta,dTheta=dTheta,
                MA2=MA2,m=min(m0,m1),eta=eta)
def sample_T(P,beta,M2):
    """random x in tube with a1 in [a_-,pi/2]; returns U1,U2"""
    while True:
        a1=rng.uniform(P['am'],pi/2); a2=rng.uniform(0,P['r0'])
        n1=rand_unit(); perp=unit(np.cross(n1,rand_unit()))
        bt=rng.uniform(0,math.sqrt(M2))   # target |b|
        s=bt/(math.sqrt(beta)*sin(a1)*sin(a2)+1e-300)
        if s>1: continue
        phi=math.asin(s); n2=cos(phi)*n1+sin(phi)*perp
        U1=np.concatenate([[cos(a1)],sin(a1)*n1]); U2=np.concatenate([[cos(a2)],sin(a2)*n2])
        S=math.sqrt(sin(a1)**2+sin(a2)**2); w=np.cross(U1[1:],U2[1:]); q=(w@w)/S**2
        if beta*2*S*math.sqrt(1+S*S)*q/2<M2: return a1,a2,U1,U2
# ---------------- M3 Taylor
ok3=True; worst3=0; n3=0
for eta in [0.4,0.1]:
    P=make(eta); M2=P['MA2']; sm=math.sinh(eta)
    say(f'  eta={eta}: a_-={P["am"]:.4f} r0={P["r0"]:.4f} H_Psi~{P["HPsi"]:.3f} Lambda~{P["Lam"]:.3f} MA2={M2:.3f}')
    for beta in [1e4,1e6]:
        rb=min(sm/8, 4/math.sqrt(beta)); rbp=math.asin(rb); sb=math.sqrt(beta)
        for it in range(1500):
            a1,a2,U1,U2=sample_T(P,beta,M2)
            u1,u2=U1[1:],U2[1:]; w=np.cross(u1,u2); S=math.sqrt(u1@u1+u2@u2); h=hS(S)
            xi1,xi2=(ball_vec(rb),ball_vec(rb)) if it%3 else (rand_unit()*rb,rand_unit()*rb)
            g1=np.concatenate([[sqrt(1-xi1@xi1)],xi1]); g2=np.concatenate([[sqrt(1-xi2@xi2)],xi2])
            V1=qmul(U1,g1); V2=qmul(U2,g2)
            a1p=math.acos(max(-1,min(1,V1[0]))); a2p=math.acos(max(-1,min(1,V2[0])))
            Sp=math.sqrt(V1[1:]@V1[1:]+V2[1:]@V2[1:]); wp=np.cross(V1[1:],V2[1:])
            F=-hS(Sp)*beta*(wp@wp)-sb*P['Psi_diff'](a1,a1p)-sb*(P['Theta'](a2p)-P['Theta'](a2))
            l=ell_matrix(U1[0],u1,U2[0],u2); xi=np.concatenate([xi1,xi2])
            pv=-np.concatenate([float(P['dPsi'](a1))*unit(u1), P['dTheta'](a2)*(unit(u2) if a2>0 else np.zeros(3))])
            Mod=-h*beta*np.sum((w+l@xi)**2)+sb*pv@xi
            nw=np.linalg.norm(w); m_=nw+math.sqrt(2)*S*rb; r_=2*rb*rb*nw+(rb+rb*rb)**2
            EW=beta*(2*m_*r_+r_*r_); BW=beta*(m_+r_)**2
            dS2=2*((sin(a1)+sin(a2))*rb+2*rb*rb); sgm=S*S-dS2
            dh=dS2/(2*sgm**2*math.sqrt(1+1/sgm))
            Err=h*EW+dh*BW+sb*(.5*P['HPsi']*rbp**2+abs(float(P['dPsi'](a1)))*(rbp-rb))+sb*(.5*P['th0']/P['ell']*rbp**2+P['dTheta'](a2)*(rbp-rb))
            n3+=1; ratio=abs(F-Mod)/Err; worst3=max(worst3,ratio); ok3&= abs(F-Mod)<=Err+1e-12
            # explicit Delta h bound (dh-explicit)
            ok3&= abs(hS(Sp)-h)<=dh+1e-12 and dh<=5*rb/S**2+1e-12
pred('M3',ok3,f'{n3} cases, worst |F-M|/Err={worst3:.3f}')
# ---------------- M4 Gauss
def logJ_det(h,l,b,p):
    Mt=np.eye(6)+2*h*l.T@l; v=p-2*h*l.T@b
    return -.5*np.linalg.slogdet(Mt)[1]+.5*v@np.linalg.solve(Mt,v)-h*(b@b)
ok4=True; nq=0; worst_f=0; worst_g=0
for it in range(20000):
    a1,a2=rng.uniform(0.02,pi-0.02,2); n1,n2=rand_unit(),rand_unit()
    if it%4==0: n2=unit(n1+rng.normal(size=3)*10**rng.uniform(-4,0))   # near-valley
    beta=10**rng.uniform(1,8)
    u1,u2=sin(a1)*n1,sin(a2)*n2; w=np.cross(u1,u2); S=math.sqrt(u1@u1+u2@u2); W=w@w
    h=hS(S); A=1+2*h*S*S; l=ell_matrix(cos(a1),u1,cos(a2),u2); b=math.sqrt(beta)*w
    P1,P2=rng.normal(size=2)*2
    p=-np.concatenate([P1*n1,P2*n2]); kap=P1/math.tan(a1)+P2/math.tan(a2)
    ld=logJ_det(h,l,b,p)
    sw2=S*S-2*W; nup=(S*S+math.sqrt(max(S**4-4*W,0)))/2; num=W/nup if nup>0 else 0
    sig2=[sw2,nup,num]; sw=math.sqrt(sw2); pw=-kap*math.sqrt(W)/sw; bw=math.sqrt(b@b)
    lf=(p@p)/2-.5*sum(math.log(1+2*h*s) for s in sig2)-(h*pw*pw*sw2+2*h*sw*pw*bw+h*bw*bw)/(1+2*h*sw2)
    worst_f=max(worst_f,abs(lf-ld)/max(1,abs(ld)))
    gap_direct=(-eS(S)+(p@p)/2)-((h-2)*(b@b)+ld)
    x=4*h*W/A; Dw=A*(1-x); B2=b@b
    gap_ex=.5*math.log(1-x)+.5*math.log(1+h*x)+h*x*B2/Dw+h*B2/Dw*(kap**2/beta-2*kap/math.sqrt(beta))
    worst_g=max(worst_g,abs(gap_ex-gap_direct)/max(1,abs(gap_direct)))
    DG1p=2*h*h*B2/(beta*A)+4*h*h*B2**2/(beta*A*Dw)+h*kap**2*B2/(beta*Dw)+2*h*abs(kap)*B2/(math.sqrt(beta)*Dw)
    DG3p=2*h*B2/(beta*Dw)+2*h*abs(kap)*B2/(math.sqrt(beta)*Dw)
    DG1=2*h*B2/(beta*S*S)+kap**2*B2/(2*beta*sw2)+abs(kap)*B2/(math.sqrt(beta)*sw2)+4*h*h*B2**2/beta
    DG3=h*(2+2/S**2)*B2/beta+abs(kap)*B2/(math.sqrt(beta)*sw2)
    t=1e-9*max(1,abs(gap_direct))
    ok4&= gap_direct<=DG1p+t and DG1p<=DG1+t and -gap_direct<=DG3p+t and DG3p<=DG3+t and abs(lf-ld)<=1e-9*max(1,abs(ld)) and abs(gap_ex-gap_direct)<=1e-9*max(1,abs(gap_direct))
    nq+=1
# MC check of determinant formula at one configuration
a1,a2=1.0,0.3; n1=unit(np.array([1.,.2,0])); n2=unit(np.array([.3,1.,.5])); beta=50.
u1,u2=sin(a1)*n1,sin(a2)*n2; w=np.cross(u1,u2); S=math.sqrt(u1@u1+u2@u2); h=hS(S)
l=ell_matrix(cos(a1),u1,cos(a2),u2); b=math.sqrt(beta)*w; p=-np.concatenate([.7*n1,.4*n2])
Z=rng.normal(size=(2000000,6)); vals=exp(-h*np.sum((b+Z@l.T)**2,axis=1)+Z@p)
mc=vals.mean(); se=vals.std()/math.sqrt(len(vals)); J=math.exp(logJ_det(h,l,b,p))
okmc=abs(mc-J)<=5*se
pred('M4',ok4 and okmc,f'{nq} cases; worst rel |formula-det|={worst_f:.2e}; worst |gap_exact-gap|={worst_g:.2e}; MC/J-1={mc/J-1:.2e} (se {se/J:.1e})')
# ---------------- M5 infl
ok5=True; w5=0
for it in range(20000):
    beta=10**rng.uniform(0,6); rho=rng.uniform(0,.5)*math.sqrt(beta) if it%2 else rng.uniform(0,.5)
    rho=min(rho,math.sqrt(beta)*pi)
    a1,a2=rng.uniform(0,pi,2); n1,n2=rand_unit(),rand_unit()
    U1=np.concatenate([[cos(a1)],sin(a1)*n1]); U2=np.concatenate([[cos(a2)],sin(a2)*n2])
    def mv(U):
        X=ball_vec(rho/math.sqrt(beta)); t=np.linalg.norm(X)
        return qmul(U,np.concatenate([[cos(t)],sin(t)*unit(X)]) if t>0 else np.array([1.,0,0,0]))
    Z1,Z2=mv(U1),mv(U2)
    lhs=math.sqrt(beta)*np.linalg.norm(np.cross(Z1[1:],Z2[1:]))
    rhs=math.sqrt(beta)*np.linalg.norm(np.cross(U1[1:],U2[1:]))+rho*(sin(a1)+sin(a2))+rho*rho/math.sqrt(beta)
    w5=max(w5,lhs/rhs if rhs>0 else 0); ok5&= lhs<=rhs+1e-12
pred('M5',ok5,f'20000 cases, worst lhs/rhs={w5:.4f}')
# ---------------- M6 valley balls
ok6=True; info6=''
for eta in [0.4,0.1]:
    P=make(eta); rB=.5; M2=P['MA2']
    sb0=max(2, rB/P['r0']*1.0000001, P['th0']*rB**2/(2*P['ell']*math.log(4/3)), math.log(4)/P['Theta'](P['r0']))
    for sb in [sb0, 10*sb0]:
        beta=sb*sb; c1=math.exp(-M2); c2=math.exp(-sb*P['Theta'](P['r0'])); worstG=9; worstE=9
        for it in range(5000):
            t=rng.uniform(-pi,pi); n=rand_unit(); C1=np.concatenate([[cos(t)],sin(t)*n]); C2=np.array([1.,0,0,0])
            def mv(U):
                X=ball_vec(rB/sb) if it%2 else rand_unit()*rB/sb; tt=np.linalg.norm(X)
                return qmul(U,np.concatenate([[cos(tt)],sin(tt)*unit(X)]))
            Z1,Z2=mv(C1),mv(C2); u1,u2=Z1[1:],Z2[1:]; w=np.cross(u1,u2); S=math.sqrt(u1@u1+u2@u2)
            q=(w@w)/S**2; G=math.exp(-beta*2*S*math.sqrt(1+S*S)*q/2); a2=math.acos(min(1,Z2[0]))
            E=math.exp(-sb*P['Theta'](a2))
            worstG=min(worstG,(G-c1)-math.exp(-1.5*rB**2)/2); worstE=min(worstE,(E-c2)-.5)
        ok6&= worstG>=-1e-12 and worstE>=-1e-12; info6+=f' eta={eta} sqrt(beta)={sb:.1f}: slackG={worstG:.4f} slackE={worstE:.4f};'
pred('M6',ok6,info6)
# ---------------- M7 measured only: MC defects at beta=1e4
beta=1e4; sb=100.; eta=0.4; P=make(eta); M2=P['MA2']
def I1s(bb):
    GLx,GLw=np.polynomial.legendre.leggauss(400); f=lambda t: exp(-2*bb*sin(t/2)**2)*cos(t)
    e=np.linspace(0,pi,81); return sum(((e[i+1]-e[i])/2*GLw*f((e[i+1]-e[i])/2*GLx+(e[i]+e[i+1])/2)).sum() for i in range(80))/pi
varrho=math.sqrt(2*pi*beta)*I1s(beta)
Nmc=400000
for j in range(6):
    a1,a2,U1,U2=sample_T(P,beta,M2)
    u1,u2=U1[1:],U2[1:]; S=math.sqrt(u1@u1+u2@u2); w=np.cross(u1,u2); h=hS(S); B2=beta*(w@w)
    xi=rng.normal(size=(Nmc,2,3))/sb; nr=np.linalg.norm(xi,axis=2); keep=np.all(nr<1,axis=1)
    g0=sqrt(np.clip(1-nr**2,0,1)); wt=np.prod(exp(-beta*(1-g0)+beta*nr**2/2)/g0,axis=1)/varrho**2*keep
    def mulv(U,g0,xi):  # vectorised quaternion product U*(g0,xi)
        x0=U[0]*g0-xi@U[1:]; v=U[0]*xi+g0[:,None]*U[1:]+np.cross(U[1:],xi); return x0,v
    x1,v1=mulv(U1,g0[:,0],xi[:,0]); x2,v2=mulv(U2,g0[:,1],xi[:,1])
    a1p=np.arccos(np.clip(x1,-1,1)); a2p=np.arccos(np.clip(x2,-1,1))
    Sp=sqrt(np.sum(v1**2,1)+np.sum(v2**2,1)); Wp=np.sum(np.cross(v1,v2)**2,1)
    # Psi differences: integrate dPsi with 20-pt GL per sample
    gx,gw=np.polynomial.legendre.leggauss(20)
    mid=(a1p+a1)/2; half=(a1p-a1)/2; dPs=(half[:,None]*gw*P['dPsi'](mid[:,None]+half[:,None]*gx)).sum(1)
    dTh=P['Theta'](a2p)-P['Theta'](a2)
    pre=(h-2)*B2
    r1=exp(pre)*np.mean(wt*exp(-hS(Sp)*beta*Wp-sb*dPs-sb*dTh))
    r3=exp(pre)*np.mean(wt*exp(-hS(Sp)*beta*Wp-sb*dPs))
    dP=float(P['dPsi'](a1)); dT=P['dTheta'](a2)
    logA1=-eS(S)+.5*(dP**2+dT**2); logA3=-eS(S)+.5*dP**2
    say(f'M7 (measured) x: a1={a1:.3f} a2={a2:.4f} |b|^2={B2:.2f}: d1=logA1-log r1={logA1-math.log(r1):+.4f}  d3=log r3-logA3={math.log(r3)-logA3:+.4f}  margin m/2={P["m"]/2:.4f}')
say('FAILED:',fails)
with open('result_prog2.txt','x') as f: f.write('\n'.join(out)+'\n')

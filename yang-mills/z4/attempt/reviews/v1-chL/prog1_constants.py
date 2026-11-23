"""prog1_constants.py -- worker v1-chL (T180). Explicit constants and scalar inequalities of tun_lower.tex.
Predicates FIXED before the first run (tolerance origin in brackets):
 C1  c* = int_0^pi sqrt(2*2asinh(sin a)) da agrees with 4.6054132 to 5e-8   [claim printed to 7 decimals]
 C2  c_ch(K0)/d at d=3.65, rho=0.265 <= 8.35 and c_ch(K1)/d <= 9.09        [as stated, lines 918-919]
 C3  min over d in [1,8], rho in (0,1/2] of c_ch(K0)/d lies in [8.34,8.35], argmin within 0.05 of (3.65,0.265) [claim 'minimum ... near']
 C4  8.35*(2a+r)+9.09a <= 35(a+r) for all a,r>=0 and 3*8.35+9.09 <= 35 [exact arithmetic]
 C5  max_{S^2<=1+1/16} S sqrt(1+S^2) <= 1.4804 (to 1e-4) and <=1.5           [line 1010, rounding 1e-4]
 C6  e^{-1.5/4}/2 - e^{-MA2(eta)} >= 0.3436 for eta in (0,0.4] (grid 4000) [line 1027]
 C7  MA2 is decreasing on (0,0.4] (grid 4000) and MA2 >= 1.5/4+log2         [line 952]
 C8  a_- = arcsin(sinh eta) <= pi/4 for eta <= 0.65; r0 <= 0.21 for eta<=0.4 [line 905; my need: r0+r_b'<pi/2]
 C9  D_beta <= rho(beta) <= 1 for beta in {10,1e2,1e3,1e4,1e6}               [Lemma exact (a); quadrature rel err ~1e-12]
 C10 (I1 up), (k_min) via I1 up, (vol) v(r)>=11r^3/(24pi) on r in (0,1/2]   [Lemma elem]
 C11 1-t/2-t^2/2 <= sqrt(1-t) <= 1-t/2 on t in [0,1/4]                       [Lemma exact (b)]
 C12 L_beta values 0.014,0.096,0.31,0.53,0.75 at beta=1e4,1e6,1e9,1e12,1e16 (to the printed 2 digits, abs 0.006)
 C13 S4 Step 4/5 bounds hold symbolically on grid: log R <= log m0 and P <= m1 for S in [s_-,s_+], eta grid
 C14 S4 full scalar inequality F <= 1-m/2 (strip) and <=1-m (a2>=ell) on a grid in (eta,S,xc,yc,t) with lambda=1, M^2=MA2
 C15 Lemma tails: P(chi3>r) formula equals 1-CDF by quadrature to 1e-10.
Result file opened with mode 'x'. No randomness except C14 grid (deterministic).
"""
import numpy as np, math
from numpy import sqrt, log, exp, arcsinh as asinh, sinh, sin, cos, pi, tanh
out=[]; fails=[]
def say(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
def pred(name, ok, info=''):
    say(f'{name}: {"MET" if ok else "FAILED"} {info}')
    if not ok: fails.append(name)
GLx,GLw=np.polynomial.legendre.leggauss(400)
def quad(f,a,b):
    return ((b-a)/2*GLw*f((b-a)/2*GLx+(a+b)/2)).sum()
def quadc(f,a,b,n=50):
    e=np.linspace(a,b,n+1); return sum(quad(f,e[i],e[i+1]) for i in range(n))
# C1 (substitution a=t^2 near 0 to remove sqrt singularity; symmetric)
cs=2*quadc(lambda t: 2*t*sqrt(4*asinh(sin(t*t))),0,sqrt(pi/2))
pred('C1', abs(cs-4.6054132)<5e-8, f'c*={cs:.10f}')
# C2-C4
def cch(K,d,rho): R=d+2*rho; return K+R*R+log(pi/2)+2*log(24*pi/(11*rho**3))
K0=lambda r:2*(2*r+r*r)**2; K1=lambda r:2*(sqrt(.5)+2*r+r*r)**2
v0=cch(K0(.265),3.65,.265)/3.65; v1=cch(K1(.265),3.65,.265)/3.65
pred('C2', v0<=8.35 and v1<=9.09, f'cK0/d={v0:.5f} cK1/d={v1:.5f}')
D,RH=np.meshgrid(np.linspace(1,8,1401),np.linspace(0.01,0.5,981))
val=cch(K0(RH),D,RH)/D; i=np.unravel_index(val.argmin(),val.shape)
pred('C3', 8.34<=val.min()<=8.35 and abs(D[i]-3.65)<0.05 and abs(RH[i]-.265)<0.05, f'min={val.min():.5f} at d={D[i]:.4f} rho={RH[i]:.4f}')
pred('C4', 2*8.35<=35 and 8.35+9.09<=35 and 3*8.35+9.09<=35, f'3*8.35+9.09={3*8.35+9.09}')
# C5,C6,C7,C8
S=np.linspace(1e-6,sqrt(1+1/16),200001); mx=(S*sqrt(1+S*S)).max()
pred('C5', mx<=1.4804+1e-4 and mx<=1.5, f'max={mx:.6f}')
eta=np.linspace(1e-4,0.4,4000); am=np.arcsin(sinh(eta)); r0=sqrt(eta*sinh(eta)/4)
m0=(1-exp(-3*eta/4))/2; m1=(1-exp(-1/16))/2
MA2=2*sqrt(2+r0**2)+np.maximum(log(1/m1)/tanh(eta), .75*eta/tanh(eta)+log(1/m0))
c6=(exp(-1.5/4)/2-exp(-MA2)).min()
pred('C6', c6>=0.3436, f'min={c6:.6f}')
pred('C7', np.all(np.diff(MA2)<0) and MA2.min()>=1.5/4+log(2), f'MA2(0.4)={MA2[-1]:.4f} min={MA2.min():.4f} need {1.5/4+log(2):.4f}')
pred('C8', math.asin(math.sinh(0.65))<=pi/4 and r0.max()<=0.21, f'a_-(0.65)={math.asin(math.sinh(.65)):.4f} r0max={r0.max():.4f}')
# C9 I1 scaled by quadrature: e^{-b} I1(b) = (1/pi) int_0^pi e^{-2b sin^2(t/2)} cos t dt
def I1s(b):
    f=lambda t: exp(-2*b*sin(t/2)**2)*cos(t)
    cut=min(pi,60/sqrt(b)); return (quadc(f,0,cut,40)+(quadc(f,cut,pi,40) if cut<pi else 0))/pi
ok=True; info=''
for b in [10,1e2,1e3,1e4,1e6]:
    rho=sqrt(2*pi*b)*I1s(b); Db=1-1/(2*b)-sqrt(2*pi*b)*exp(-b)/2
    ok&= (Db<=rho<=1); info+=f' b={b:g}:D={Db:.8f},rho={rho:.8f}'
pred('C9', ok, info)
# C10
ok=True; info=''
for b in [2.,10.,100.,1e4]:
    up=(pi/2)/sqrt(2*pi*b)  # scaled: e^{-b} * (pi/2)e^b/sqrt(2 pi b)
    ok&= I1s(b)<=up; info+=f' b={b:g}:{I1s(b):.5g}<={up:.5g}'
    R=3.0; th=R/sqrt(b)
    if th<=pi:
        k=exp(b*cos(th))*b/(2*I1s(b)*exp(b)); kmin=sqrt(2/pi)*b**1.5*exp(-R*R/2)
        ok&= k>=kmin; info+=f' kmin ok {k:.4g}>={kmin:.4g}'
r=np.linspace(1e-4,0.5,5000); x=2*r
vr=np.where(x>1e-2,(x-sin(x))/(2*pi),(x**3/6-x**5/120+x**7/5040)/(2*pi))
ok&= np.all(vr>=11*r**3/(24*pi)); pred('C10', ok, info+f' vol min ratio={np.min(vr/(11*r**3/(24*pi))):.4f}')
t=np.linspace(0,.25,10001)
pred('C11', np.all(1-t/2-t*t/2<=sqrt(1-t)+1e-15) and np.all(sqrt(1-t)<=1-t/2+1e-15))
# C12 L_beta
def vball(r): x=2*r; return (x**3/6-x**5/120+x**7/5040-x**9/362880)/(2*pi) if x<1e-2 else (x-math.sin(x))/(2*pi)
def Pk(b,tt):
    # density of theta ~ sin^2(th) e^{-2b sin^2(th/2)}; integrate in s=sqrt(b) th
    f=lambda s: sin(s/sqrt(b))**2*exp(-2*b*sin(s/(2*sqrt(b)))**2)
    top=min(pi*sqrt(b),80.); num=quadc(f,0,min(tt*sqrt(b),top),40); den=quadc(f,0,top,80)
    return num/den
claims={1e4:.014,1e6:.096,1e9:.31,1e12:.53,1e16:.75}; ok=True; info=''
for b,cl in claims.items():
    rr=b**(-1/3); tt=b**(-5/12)
    L=exp(-2*b*rr**4)*(vball(rr-tt)/vball(rr)*Pk(b,tt))**2
    ok&= abs(L-cl)<=0.006; info+=f' {b:g}:{L:.4f}'
pred('C12', ok, info)
# C13 and C14
ok13=True; worst14=1e9; worst14s=1e9; n14=0
for e in np.concatenate([np.logspace(-4,-1,25),np.linspace(.1,.4,25)]):
    am_=math.asin(math.sinh(e)); r0_=math.sqrt(e*math.sinh(e)/4); ell=r0_/3
    m0_=(1-math.exp(-3*e/4))/2; m_=min(m0_,m1)
    MA=2*math.sqrt(2+r0_**2)+max(math.log(1/m1)/math.tanh(e), .75*e/math.tanh(e)+math.log(1/m0_))
    for Sv in np.linspace(math.sinh(e),math.sqrt(1+r0_**2),40):
        k=math.sqrt(1+Sv*Sv)/Sv; gam=1-1/k; eS=2*math.asinh(Sv); P=math.exp(eS-MA/k)
        logR=-math.log(k)+k*eS-MA+(k-1)*.75*e
        ok13 &= (logR<=math.log(m0_)+1e-12) and (P<=m1+1e-15)
        for s1 in np.linspace(am_,pi/2,6):       # a1 with sin a1 <= S : require sin^2 a2 = S^2 - sin^2 a1 in [0, sin^2 r0]
            s2sq=Sv*Sv-math.sin(s1)**2
            if s2sq<0 or s2sq>math.sin(r0_)**2: continue
            a2=math.asin(math.sqrt(s2sq)); tp=(0.5*a2/math.sqrt(a2*a2+ell*ell))**2/2
            D_=eS-2*math.asinh(math.sin(s1)); a=math.exp(-e+D_-tp)   # lambda=1, Delta=0
            b_=math.exp(-tp)
            for xc in np.linspace(0,1,21):
                for yc in np.linspace(0,1,21):
                    F=a*(1-xc)*(1-yc)+P*xc**gam+b_*yc
                    n14+=1
                    if a2>=ell: worst14=min(worst14,(1-m_)-F)
                    else:
                        yb=yc  # on strip yc<=y_beta; test the bound with yc<=m/2
                        if yc<=m_/2: worst14s=min(worst14s,(1-m_/2)-F)
pred('C13', ok13)
pred('C14', worst14>=-1e-12 and worst14s>=-1e-12, f'cases={n14} min slack (a2>=ell)={worst14:.3e} strip={worst14s:.3e}')
from math import erfc
rr=np.linspace(0.1,8,50); fo=erfc  # chi3 tail
ok=True
for r_ in rr:
    form=erfc(r_/math.sqrt(2))+math.sqrt(2/pi)*r_*math.exp(-r_*r_/2)
    num=quad(lambda s: math.sqrt(2/pi)*s*s*exp(-s*s/2), r_, 40)
    ok&= abs(form-num)<1e-10
pred('C15', ok)
say('FAILED:',fails)
with open('result_prog1.txt','x') as f: f.write('\n'.join(out)+'\n')

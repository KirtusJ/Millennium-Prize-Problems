"""check_c4.py -- challenger checks of numbers printed by Director C4 (magnetic-smearing).

Predicates (fixed before first run). Tolerance sources in brackets.
P1 lattice temporal Green (spectrum.md): int dk4/2pi e^{i k4 n}/(Q^2+2-2cos k4)
   = e^{-w|n|}/(2 sinh w), w = 2 arsinh(Q/2); Q in {0.3,1,2.5}, n in {0,1,3}; rel err < 1e-10
   [periodic trapezoid, 4096 nodes, exponential convergence].
P2 point kernel: per colour <B3(t,x)B3(0)> = -(d1^2+d2^2) G, G = 1/(4 pi^2 (x^2+t^2)), equals Z4's
   (t^2+x3^2-x1^2-x2^2)/(pi^2 (x^2+t^2)^3) at 5 points; and at x=0 equals C4's |J|^2/(pi^2 t^4)
   (J=1); rel err < 1e-5 [central FD, h=1e-3, O(h^2) truncation].
P3 angular constants: int theta3^{2m}(theta1^2+theta2^2) dOmega = 8 pi/((2m+1)(2m+3)), m=0,1,2;
   rel err < 1e-12 [Gauss-Legendre exact for polynomials].
P4 Cov(|X0|^2/2, |Xt|^2/2) = 3 C_t^2/2 for 3 iid colours, C0=1, Ct=0.4; MC N=2e6 seed 1; |dev| < 5 SE.
P5 Cov(exp(-s|X0|^2), exp(-s|Xt|^2)) = [D^2-4 s^2 Ct^2]^{-3/2} - D^{-3}, D=1+2 s C0, s=0.7; MC; < 5 SE.
P6 internal consistency of execution.md: from printed C0(0),C0(1),C0(2) and s=1/(2C0(0)),
   8*B(t) (mean-normalized, D=2) equals printed 0.02029847 (t=1), 0.00180930 (t=2), ratio 0.0891348;
   rel err < 5e-4 [printed C values have 6 significant digits; B ~ C^2 doubles relative error].
P7 low-energy law: mu density J^2 E^3/(6 pi^2) => (3/2) mu*mu mass below eps = 3 J^4 eps^8/(2 pi^4 8!);
   rel err < 1e-8 [Gauss-Legendre on polynomial].
P8 lattice -> continuum: discrete covariance (spectrum.md formula, m=0, node-sampled Gaussian profile
   psi=exp(-|x|^2/2), g=r^{-1}psi(x/r)) at n = r t, t=1, approaches C0(1); error at r=16 below 2%
   and decreasing r=4->8->16 [expectation O(r^-2) lattice artifacts; 2% is my own margin].
M1 (measured only) reproduction attempt of C0(0)=0.01972957 with a GUESSED profile (standard bump
   exp(-1/(1-x^2)) normalized, fourfold self-convolution, tensor product). Mismatch = my guess.
"""
import numpy as np, math, os, sys
np.random.seed(1)
out = []
def rep(name, ok, msg):
    ok = None if ok is None else bool(ok)
    out.append(f"{name}: {'MET' if ok is True else ('FAILED' if ok is False else 'MEASURED')} | {msg}")
    print(out[-1])

# P1
N = 4096; k = 2*np.pi*np.arange(N)/N; worst = 0
for Q in (0.3, 1.0, 2.5):
    w = 2*np.arcsinh(Q/2)
    for n in (0, 1, 3):
        num = np.mean(np.cos(k*n)/(Q*Q+2-2*np.cos(k)))
        ex = np.exp(-w*n)/(2*np.sinh(w)); worst = max(worst, abs(num/ex-1))
rep("P1", worst < 1e-10, f"max rel err {worst:.2e}")

# P2
def G(x1, x2, x3, t): return 1/(4*np.pi**2*(x1*x1+x2*x2+x3*x3+t*t))
h = 1e-3; worst = 0
for (x1, x2, x3, t) in [(0,0,0,1),(0,0,0,2.5),(0.3,0.2,0.5,1),(1,0,0,0.7),(0.2,-0.4,1.3,0.9)]:
    lap = (G(x1+h,x2,x3,t)+G(x1-h,x2,x3,t)+G(x1,x2+h,x3,t)+G(x1,x2-h,x3,t)-4*G(x1,x2,x3,t))/h**2
    num = -lap; r2 = x1*x1+x2*x2+x3*x3
    z4 = (t*t+x3*x3-x1*x1-x2*x2)/(np.pi**2*(r2+t*t)**3)
    worst = max(worst, abs(num/z4-1))
    if r2 == 0: worst = max(worst, abs(z4*np.pi**2*t**4-1))
rep("P2", worst < 1e-5, f"max rel err {worst:.2e} (C4 C0~J^2/(pi^2 t^4) = Z4 kernel at x=0)")

# P3
xg, wg = np.polynomial.legendre.leggauss(40); worst = 0
for m in (0, 1, 2):
    val = 2*np.pi*np.sum(wg*xg**(2*m)*(1-xg**2))  # theta3=cos, theta1^2+theta2^2 = sin^2
    worst = max(worst, abs(val/(8*np.pi/((2*m+1)*(2*m+3)))-1))
rep("P3", worst < 1e-12, f"max rel err {worst:.2e}")

# P4, P5
Nmc = 2_000_000; C0, Ct = 1.0, 0.4
a = np.random.randn(Nmc, 3); b = np.random.randn(Nmc, 3)
X0 = a; Xt = Ct*a + math.sqrt(C0*C0-Ct*Ct)*b
q0 = (X0**2).sum(1)/2; qt = (Xt**2).sum(1)/2
prod = (q0-q0.mean())*(qt-qt.mean()); est = prod.mean(); se = prod.std()/math.sqrt(Nmc)
rep("P4", abs(est-1.5*Ct**2) < 5*se, f"MC {est:.5f} vs 3Ct^2/2={1.5*Ct**2:.5f}, SE {se:.1e}")
s = 0.7; o0 = np.exp(-s*(X0**2).sum(1)); ot = np.exp(-s*(Xt**2).sum(1)); D = 1+2*s*C0
prod = (o0-o0.mean())*(ot-ot.mean()); est = prod.mean(); se = prod.std()/math.sqrt(Nmc)
Bf = (D*D-4*s*s*Ct*Ct)**-1.5 - D**-3
rep("P5", abs(est-Bf) < 5*se, f"MC {est:.6f} vs formula {Bf:.6f}, SE {se:.1e}")

# P6
c0, c1, c2 = 0.01972957, 0.00455193, 0.00136940
def Bn(ct): s = 1/(2*c0); D = 2.0; return ((D*D-4*s*s*ct*ct)**-1.5 - D**-3)*D**3
b1, b2 = Bn(c1), Bn(c2)
e = max(abs(b1/0.02029847-1), abs(b2/0.00180930-1), abs((b2/b1)/0.0891348-1))
rep("P6", e < 5e-4, f"8B(1)={b1:.8f} 8B(2)={b2:.8f} ratio={b2/b1:.7f}; max rel err {e:.1e}")

# P7
J = 1.0; c = J**2/(6*np.pi**2); eps = 0.37
# (mu*mu)(E) = c^2 int_0^E x^3 (E-x)^3 dx = c^2 E^7 * 3!3!/7!; mass below eps:
xs, ws = np.polynomial.legendre.leggauss(30)
def conv(E):
    x = (xs+1)/2*E; return c*c*np.sum(ws*E/2*x**3*(E-x)**3)
E = (xs+1)/2*eps; mass = 1.5*np.sum(ws*eps/2*np.array([conv(e_) for e_ in E]))
claim = 3*J**4*eps**8/(2*np.pi**4*math.factorial(8))
rep("P7", abs(mass/claim-1) < 1e-8, f"mass {mass:.6e} vs claim {claim:.6e}")

# P8: continuum C0(1) for Gaussian profile: |psihat|^2=(2pi)^3 e^{-p^2}; radial form
def C0cont(t):
    p, wp = np.polynomial.legendre.leggauss(400); p = (p+1)/2*12; wp = wp*6
    return np.sum(wp*(2*np.pi)**3*np.exp(-p*p)*p**2/(8*np.pi**3)*(8*np.pi/3)*p/2*np.exp(-t*p))
def C0lat(r, t, M=96, P=7.0):
    n = round(r*t)
    g = np.linspace(-P, P, M, endpoint=False) + P/M  # p-grid (k = p/r), integrand negligible beyond P
    p1, p2, p3 = np.meshgrid(g, g, g, indexing="ij"); kk = [p1/r, p2/r, p3/r]
    q2 = [4*np.sin(ki/2)**2 for ki in kk]; Q = np.sqrt(q2[0]+q2[1]+q2[2]); w = 2*np.arcsinh(Q/2)
    # node-sampled Gaussian: ghat(k) = r^{-1} sum_x psi(x/r) e^{-ikx} = r^2 (2pi)^{3/2} sum_l e^{-|r(k+2pi l)|^2/2}; l=0 dominant
    gh2 = r**4*(2*np.pi)**3*np.exp(-(p1**2+p2**2+p3**2))
    integ = gh2*(q2[0]+q2[1])/(2*np.sinh(w))*np.exp(-n*w)
    dk3 = (2*P/M/r)**3
    return integ.sum()*dk3/(2*np.pi)**3
cc = C0cont(1.0); errs = []
for r in (4, 8, 16):
    errs.append(abs(C0lat(r, 1.0)/cc-1))
ok = errs[2] < 0.02 and errs[0] > errs[1] > errs[2]
rep("P8", ok, f"C0cont(1)={cc:.6e}; rel err r=4,8,16: {', '.join(f'{x:.2e}' for x in errs)}")

# M1 guessed profile
xx = np.linspace(-1, 1, 4001)[1:-1]; phi = np.exp(-1/(1-xx**2)); dx = xx[1]-xx[0]; phi /= phi.sum()*dx
pp = np.linspace(0, 40, 4001)
phihat = np.array([np.sum(phi*np.cos(p_*xx))*dx for p_ in pp])
f1 = lambda p: np.interp(np.abs(p), pp, phihat)**4  # fourfold convolution
M = 80; gp = np.linspace(-20, 20, M, endpoint=False)+20/M
p1, p2, p3 = np.meshgrid(gp, gp, gp, indexing="ij"); pn = np.sqrt(p1**2+p2**2+p3**2)
w2 = (f1(p1)*f1(p2)*f1(p3))**2*(p1**2+p2**2)/(2*pn); dp3 = (40/M)**3/(2*np.pi)**3
vals = [np.sum(w2*np.exp(-t*pn))*dp3 for t in (0, 1, 2)]
rep("M1", None, f"guessed-profile C0(0,1,2) = {vals[0]:.8f}, {vals[1]:.8f}, {vals[2]:.8f} vs printed 0.01972957, 0.00455193, 0.00136940")

fn = "results_check_c4_1.txt"
while os.path.exists(fn): fn = fn.replace(".txt", "_n.txt")
open(fn, "w", encoding="utf-8").write("\n".join(out)+"\n")
fails = sum(1 for l in out if ": FAILED" in l)
sys.exit(1 if fails else 0)

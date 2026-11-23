"""powers.py -- challenger check of Z4 S1, S2, S4 (free Maxwell, 3+1, continuum).

My own derivation (not taken from STATEMENT.md):
  Transverse A with <A_i A_j>(k) = (delta_ij - k_i k_j/k^2)/(2|k|), B = curl A, so
  <B_3 e^{-tH} B_3>(k) = G_t(k) = (k1^2+k2^2)/(2|k|) e^{-t|k|}.
  Real space (from S(t,x) = 1/(4 pi^2 (t^2+r^2)), D_33 = -(d1^2+d2^2) S):
      D_t(x) = (u - 2 rho^2)/(pi^2 u^3),  u = t^2 + r^2, rho^2 = x1^2+x2^2.
  Wick: C(t) = 2 int d^3r FF(r) D_t(r)^2, FF = f*f (autocorrelation).
  Sphere average of (u-2 r^2 sin^2)^2 = u^2 - (8/3) u r^2 + (32/15) r^4, so
      C(t) = (8/pi^3) int_0^inf r^2 FF(r) [u^2-(8/3)u r^2+(32/15)r^4]/u^6 dr.
  f(x) = exp(-r^2/(2w^2)):  FF(r) = pi^{3/2} w^3 exp(-r^2/(4w^2)), int f^2 = pi^{3/2} w^3,
  int f = (2 pi)^{3/2} w^3.
  Predictions: C_Lambda(0) ~ (2/(75 pi^2)) Lambda^5 int f^2 (sharp cutoff |k|<Lambda);
  C(t) ~ int f^2 /(50 pi^2 t^5) (t->0);  C(t) ~ 2 (int f)^2/(pi^4 t^8) (t->inf, infinite volume);
  point split |r|>a at t=0: C_a = c5 a^-5 + c3 a^-3 + c1 a^-1 + finite, c3 = (56/(15pi^3)) FF''(0)/6 < 0.

PREDICATES (fixed before first run; tolerance sources in brackets):
 P1 sharp-cutoff local exponent dlnC/dlnLambda between Lambda=16,32 (w=1) in [4.9,5.1]
    [subleading Lambda^-2 term ~ 1.5/(Lambda w)^2 ~ 0.6% plus k-grid counting noise]
 P2 C/(Lambda^5 int f^2) at Lambda=32 within 3% of 2/(75 pi^2) for w=1 and w=0.7, and the two
    ratios agree within 2%  [same subleading estimate, doubled for w=0.7]
 P3 Gaussian cutoff exp(-k^2/Lambda^2) local exponent Lambda=8->16 in [4.9,5.1]  [as P1]
 P4 momentum-grid C(0.5) agrees with real-space 1D integral within 1% [grid/box discretisation]
 P5 C(t) t^5 at t=1e-3 within 0.5% of int f^2/(50 pi^2); local exponent t=1e-3..2e-3 in 5+-0.01
    [relative correction O(t^2/w^2)=1e-6; quadrature]
 P6 C(t) t^8 at t=1e3 within 0.5% of 2 (int f)^2/pi^4; local exponent t=1e3..2e3 in 8+-0.01
    [correction O(w^2/t^2)=1e-6]
 P7 point split: (C_a - c5 a^-5) local exponent between a=0.01,0.02 in -3+-0.05 and within 1% of
    c3 a^-3; second remainder exponent in -1+-0.1  [Taylor remainder O(a^2/w^2)]
 P8 (S4, for all p with |n_p|_inf<=4): min over nonzero integer n,n' with n+n'=n_p of |n|+|n'| >= 2;
    count cases; and B_3 projector weight at k=(1,0,0),k'=-k is > 0.
 P9 (S4 lattice) lowest lattice two-photon energy 2 (2/b) sin(pi b/l) vs 2(2pi/l): prediction:
    strictly BELOW by relative pi^2 b^2/(6 l^2) (so "at or above 2(2pi/l)" holds only with the O(b^2)).
 M1 (measured only) lattice C_b(0) b^5 and C_b(0.5) vs continuum, l=12, N=24,48,96.
Exit code 0 iff all P pass, else 1.
"""
import numpy as np, mpmath as mp, json, os, sys, itertools
mp.mp.dps = 30
res = {}; ok = {}
pi = np.pi

def FF(r, w): return mp.pi**1.5 * w**3 * mp.e**(-r**2/(4*w**2))

def C_real(t, w):
    t = mp.mpf(t)
    def g(r):
        u = t**2 + r**2
        return r**2*FF(r, w)*(u**2 - mp.mpf(8)/3*u*r**2 + mp.mpf(32)/15*r**4)/u**6
    pts = [0, t/4, t, 4*t, 1, 4*w, 12*w, mp.inf] if t < 1 else [0, w, 4*w, t, 4*t, 20*t, mp.inf]
    pts = sorted(set(pts), key=lambda z: float(z) if z != mp.inf else 1e99)
    return 8/mp.pi**3 * mp.quad(g, pts)

# ---------- momentum grid (continuum box) ----------
L, M = 12.0, 160
h = L/M
n = np.fft.fftfreq(M, d=1.0/M)
k1d = 2*pi*n/L
K1, K2, K3 = np.meshgrid(k1d, k1d, k1d, indexing='ij')
KK = np.sqrt(K1**2+K2**2+K3**2); KK[0,0,0] = 1.0
x1d = h*np.where(n >= 0, n, n)  # positions with wrap
X1, X2, X3 = np.meshgrid(x1d, x1d, x1d, indexing='ij')
R2 = X1**2+X2**2+X3**2
Gbase = (K1**2+K2**2)/(2*KK); Gbase[0,0,0] = 0.0

def C_grid(w, mult):
    Dk = Gbase*mult
    D = np.real(np.fft.ifftn(Dk))*M**3/L**3
    ff = pi**1.5*w**3*np.exp(-R2/(4*w**2))
    return 2*h**3*np.sum(D**2*ff)

c5 = 2/(75*pi**2)
Cs = {}
for w in (1.0, 0.7):
    for Lam in (16.0, 32.0):
        Cs[(w, Lam)] = C_grid(w, (KK < Lam).astype(float))
s1 = np.log(Cs[(1.0,32.0)]/Cs[(1.0,16.0)])/np.log(2)
res['P1_exponent_sharp'] = s1; ok['P1'] = 4.9 <= s1 <= 5.1
r_w1 = Cs[(1.0,32.0)]/(32.0**5*pi**1.5*1.0)
r_w07 = Cs[(0.7,32.0)]/(32.0**5*pi**1.5*0.343)
res['P2_ratio_w1'] = r_w1/c5; res['P2_ratio_w07'] = r_w07/c5
ok['P2'] = abs(r_w1/c5-1) < 0.03 and abs(r_w07/c5-1) < 0.03 and abs(r_w1/r_w07-1) < 0.02
g8 = C_grid(1.0, np.exp(-KK**2/64.0)); g16 = C_grid(1.0, np.exp(-KK**2/256.0))
s3 = np.log(g16/g8)/np.log(2); res['P3_exponent_gauss'] = s3; ok['P3'] = 4.9 <= s3 <= 5.1
cg = C_grid(1.0, np.exp(-0.5*KK)); cr = float(C_real(0.5, 1))
res['P4_grid_C0.5'] = cg; res['P4_real_C0.5'] = cr; ok['P4'] = abs(cg/cr-1) < 0.01
print('grid done', res, flush=True)

# ---------- real-space asymptotics ----------
I2 = float(mp.pi**1.5); I1 = float((2*mp.pi)**1.5)
a1, a2 = float(C_real(1e-3,1)), float(C_real(2e-3,1))
res['P5_Ct5_over_pred'] = a1*1e-15/(I2/(50*pi**2)); res['P5_exp'] = -np.log(a2/a1)/np.log(2)
ok['P5'] = abs(res['P5_Ct5_over_pred']-1) < 0.005 and abs(res['P5_exp']-5) < 0.01
b1, b2 = float(C_real(1e3,1)), float(C_real(2e3,1))
res['P6_Ct8_over_pred'] = b1*1e24/(2*I1**2/pi**4); res['P6_exp'] = -np.log(b2/b1)/np.log(2)
ok['P6'] = abs(res['P6_Ct8_over_pred']-1) < 0.005 and abs(res['P6_exp']-8) < 0.01
# for the record: C(t) on a grid of t
res['Ct_table'] = {str(t): float(C_real(t,1)) for t in (0.01,0.1,0.5,1,2,5,10,100)}

# ---------- point split at t=0 ----------
K = 56/(15*mp.pi**3)
def C_split(a): return K*mp.quad(lambda r: FF(r,1)*r**-6, [a, 10*a, 1, 12, mp.inf])
F0 = FF(0,1); F2 = -F0/2  # FF''(0) for w=1: FF = F0 exp(-r^2/4) -> F'' = -F0/2
cc5 = K*F0/5; cc3 = K*F2/2/3
rem = {}
for a in (mp.mpf('0.01'), mp.mpf('0.02')):
    rem[a] = C_split(a) - cc5*a**-5
e7 = float(mp.log(rem[mp.mpf('0.02')]/rem[mp.mpf('0.01')])/mp.log(2))
res['P7_rem_exp'] = e7; res['P7_rem_over_c3'] = float(rem[mp.mpf('0.01')]/(cc3*mp.mpf('0.01')**-3))
F4 = F0*3/4  # 4th derivative at 0 of exp(-r^2/4): 3/4 * F0 ... coefficient r^4/24*F4
cc1 = K*(F4/24)/1
rem2 = {a: rem[a]-cc3*a**-3 for a in rem}
e7b = float(mp.log(rem2[mp.mpf('0.02')]/rem2[mp.mpf('0.01')])/mp.log(2))
res['P7_rem2_exp'] = e7b; res['P7_rem2_over_c1'] = float(rem2[mp.mpf('0.01')]/(cc1*100))
res['P7_c5,c3,c1'] = [float(cc5), float(cc3), float(cc1)]
ok['P7'] = abs(e7+3) < 0.05 and abs(res['P7_rem_over_c3']-1) < 0.01 and abs(e7b+1) < 0.1

# ---------- S4 box ----------
cases = 0; viol = 0; atmin = 0
rng = range(-6, 7)
vecs = [np.array(v) for v in itertools.product(rng, rng, rng) if any(v)]
for p in itertools.product(range(-4,5), repeat=3):
    p = np.array(p); cases += 1
    m = min(np.linalg.norm(k)+np.linalg.norm(p-k) for k in vecs if any(p-k) and np.max(np.abs(p-k)) <= 6)
    if m < 2-1e-12: viol += 1
    if abs(m-2) < 1e-12: atmin += 1
proj = (1.0**2+0.0)/1.0
res['P8_cases'] = cases; res['P8_violations'] = viol; res['P8_cases_reaching_2'] = atmin
ok['P8'] = viol == 0 and proj > 0
l = 12.0
p9 = {}
for N in (24, 48, 96):
    b = l/N; e = 2*(2/b)*np.sin(pi*b/l); p9[N] = [e/(2*2*pi/l)-1, -pi**2*b**2/(6*l**2)]
res['P9'] = p9; ok['P9'] = all(v[0] < 0 and abs(v[0]/v[1]-1) < 0.01 for v in p9.values())

# ---------- M1 lattice (measured only) ----------
m1 = {}
for N in (24, 48, 96):
    b = l/N; nn = np.fft.fftfreq(N, d=1.0/N); kk = 2*pi*nn/l
    Q1, Q2, Q3 = np.meshgrid(kk, kk, kk, indexing='ij')
    h1, h2, h3 = [(2/b)*np.sin(q*b/2) for q in (Q1, Q2, Q3)]
    kh = np.sqrt(h1**2+h2**2+h3**2); kh[0,0,0] = 1
    xs = b*np.where(nn >= 0, nn, nn)
    Y1, Y2, Y3 = np.meshgrid(xs, xs, xs, indexing='ij')
    f = np.exp(-(Y1**2+Y2**2+Y3**2)/2)
    acf = np.real(np.fft.ifftn(np.abs(np.fft.fftn(f))**2))  # sum_y f(y) f(y+r)
    out = []
    for t in (0.0, 0.5):
        Gk = (h1**2+h2**2)/(2*kh)*np.exp(-t*kh); Gk[0,0,0] = 0
        D = np.real(np.fft.ifftn(Gk))*N**3/l**3
        out.append(2*b**6*np.sum(D**2*acf))
    m1[N] = {'Cb0_b5': out[0]*b**5, 'Cb0.5': out[1], 'rel_err_vs_cont': out[1]/cr-1}
res['M1'] = m1

res['pass'] = ok
fn = 'result_powers.json'
if os.path.exists(fn):
    i = 1
    while os.path.exists(f'result_powers_{i}.json'): i += 1
    fn = f'result_powers_{i}.json'
with open(fn, 'w') as fh: json.dump(res, fh, indent=1, default=str)
print(json.dumps(res, indent=1, default=str)); print('written', fn)
sys.exit(0 if all(ok.values()) else 1)

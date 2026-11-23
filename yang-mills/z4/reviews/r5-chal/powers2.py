"""powers2.py -- follow-up to powers.py after P2 and P5 failed (own expectation errors).
PREDICATES (fixed before run):
 Q1 C(t) t^5 at t=1e-3 within 0.5% of int f^2/(10 pi^2)  [corrected arithmetic; O(t^2) correction]
 Q2 sharp cutoff: relative deviation dev(w,Lam) = C/(c5 Lam^5 int f^2) - 1 matches the derived nonlocal
    term -1.25 <|p|>/Lam, <|p|> = 2/(sqrt(pi) w), within 10% for (w,Lam) in {1,0.7}x{16,32}
    [remaining local Lam^-2 term estimated ~1%/(w^2)]
Exit 0 iff both pass.
"""
import numpy as np, mpmath as mp, json, os, sys
import importlib.util
pi = np.pi
mp.mp.dps = 30
def FF(r, w): return mp.pi**1.5*w**3*mp.e**(-r**2/(4*w**2))
t = mp.mpf('1e-3')
g = lambda r: r**2*FF(r,1)*((t**2+r**2)**2-mp.mpf(8)/3*(t**2+r**2)*r**2+mp.mpf(32)/15*r**4)/(t**2+r**2)**6
C = 8/mp.pi**3*mp.quad(g, [0, t/4, t, 4*t, 1, 12, mp.inf])
q1 = float(C*t**5/(mp.pi**1.5/(10*mp.pi**2)))
L, M = 12.0, 160; h = L/M
n = np.fft.fftfreq(M, d=1.0/M); k1d = 2*pi*n/L
K1, K2, K3 = np.meshgrid(k1d, k1d, k1d, indexing='ij')
KK = np.sqrt(K1**2+K2**2+K3**2); KK[0,0,0] = 1
X = h*n; X1, X2, X3 = np.meshgrid(X, X, X, indexing='ij'); R2 = X1**2+X2**2+X3**2
G = (K1**2+K2**2)/(2*KK); G[0,0,0] = 0
c5 = 2/(75*pi**2); q2 = {}
for w in (1.0, 0.7):
    ff = pi**1.5*w**3*np.exp(-R2/(4*w**2))
    for Lam in (16.0, 32.0):
        D = np.real(np.fft.ifftn(G*(KK < Lam)))*M**3/L**3
        dev = 2*h**3*np.sum(D**2*ff)/(c5*Lam**5*pi**1.5*w**3) - 1
        pred = -1.25*2/(np.sqrt(pi)*w)/Lam
        q2[f'{w},{Lam}'] = [dev, pred, dev/pred]
ok = {'Q1': abs(q1-1) < 0.005, 'Q2': all(abs(v[2]-1) < 0.1 for v in q2.values())}
res = {'Q1_ratio': q1, 'Q2_dev_pred_ratio': q2, 'pass': ok}
fn = 'result_powers2.json'
i = 1
while os.path.exists(fn): fn = f'result_powers2_{i}.json'; i += 1
json.dump(res, open(fn, 'w'), indent=1, default=str); print(json.dumps(res, indent=1, default=str))
sys.exit(0 if all(ok.values()) else 1)

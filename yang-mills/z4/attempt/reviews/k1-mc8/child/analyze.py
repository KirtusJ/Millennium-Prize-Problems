"""Analysis of run_data.npz per predicates P2,P3,P5 in mc.py docstring. Output report_numbers.txt (mode x)."""
import numpy as np
d = np.load('run_data.npz'); NS = int(d['NS']); Cs = d['Csum']/NS; Os = d['Osum']/NS; ser = d['ser']
Nc, T = Cs.shape[0], Cs.shape[2]; out = open('report_numbers.txt', 'x')
def w(s): print(s); out.write(s+'\n')
w(f"acc={float(d['acc']):.3f} NS={NS} chains={Nc}")
# P2
s = ser[:, :, 2]; h = NS//2; a, b = s[:h].mean(0), s[h:].mean(0); diff = a-b
z = diff.mean()/(diff.std(ddof=1)/np.sqrt(Nc)); w(f"P2 <s> first half {a.mean():.5f} second half {b.mean():.5f} z={z:.2f} -> {'PASS' if abs(z)<3 else 'FAIL'}")
# P3
def tau(x):
    x = x-x.mean(); n = len(x); f = np.fft.rfft(x, 2*n); ac = np.fft.irfft(f*f.conj())[:n]; ac /= ac[0]
    t = 0.5
    for M in range(1, n):
        t += ac[M]
        if M >= 6*t: break
    return t
for k, name in ((0, 'corr(tau=1)'), (2, '<s>')):
    ts = np.array([tau(ser[:, c, k]) for c in range(Nc)]); tm = np.mean([tau(ser[:, :, k].mean(1))])
    w(f"P3 tau_int[{name}] chain-mean={ts.mean():.1f} (median {np.median(ts):.1f}, max {ts.max():.1f}); need NS>=50 tau: {'PASS' if NS >= 50*ts.mean() else 'FAIL'}")
# correlator
def mass(idx):
    Cm = Cs[idx].mean(0) - (Os[idx].mean(0)**2)[:, None]   # (2,T) ; <O>^2 per channel
    Cm = Cm.mean(0); D = Cm[:-1]-Cm[1:]; return D
def meff(idx):
    D = mass(idx)
    with np.errstate(all='ignore'): return np.log(D[:-1]/D[1:])
full = meff(np.arange(Nc)); jk = np.array([meff(np.delete(np.arange(Nc), c)) for c in range(Nc)])
err = np.sqrt((Nc-1)/Nc*((jk-jk.mean(0))**2).sum(0))
Dfull = mass(np.arange(Nc))
w("t  D(t)  m_eff  err")
for t in range(0, 14): w(f"{t:2d} {Dfull[t]: .3e} {full[t]: .4f} {err[t]:.4f}")
res = None
for t0 in range(1, 12):
    sl = slice(t0, t0+3); m = full[sl]; e = err[sl]
    if not np.all(np.isfinite(m)) or not np.all(np.isfinite(e)) or np.any(e/np.abs(m) >= .25) or np.any(m <= 0): continue
    wt = 1/e**2; mu = (wt*m).sum()/wt.sum(); chi = (((m-mu)/e)**2).sum()/2
    if chi <= 2:
        def wm(mm, ee): ww = 1/ee**2; return (ww*mm).sum()/ww.sum()
        jm = np.array([wm(jk[c, sl], e) for c in range(Nc)])  # weights fixed at full-sample errors
        je = np.sqrt((Nc-1)/Nc*((jm-jm.mean())**2).sum()); res = (t0, mu, je, chi); break
if res is None: w("P5 plateau: FAIL (no window meets rule)")
else:
    t0, mu, je, chi = res; w(f"P5 plateau t0={t0}..{t0+2}: m={mu:.4f} +- {je:.4f} chi2/dof={chi:.2f}  m*beta^(1/3)={mu*64**(1/3):.4f} +- {je*64**(1/3):.4f}")

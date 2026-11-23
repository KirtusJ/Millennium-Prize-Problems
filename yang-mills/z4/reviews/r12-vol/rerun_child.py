"""Independent recomputation of the child's case with my vol.C_fft (own code, not the child's).
Predicate fixed before the run: |C_mine - 2.177968313057|/C <= 1e-10 and |P_mine - 0.01879479225576|/P <= 1e-10
(tolerance: both are double-precision FFT sums of ~1e5 terms; rounding ~1e-13)."""
import numpy as np, math, json, sys, vol
N, l, s = 48, 1.0, 0.005; b = l/N
x = np.arange(N)*b
g = sum(np.exp(-(x-0.3-m)**2/(2*0.15**2)) for m in range(-2,3))
f = g[:,None,None]*g[None,:,None]*g[None,None,:]
C = vol.C_fft(f,l,s); P = b**3*np.sum(f*f)
r = dict(C=C, P=P, ratio=C*s**2.5/P, relC=abs(C-2.177968313057)/C, relP=abs(P-0.01879479225576)/P)
r['pass'] = bool(r['relC'] <= 1e-10 and r['relP'] <= 1e-10)
print(json.dumps(r))
open(sys.argv[1],'x').write(json.dumps(r))
sys.exit(0 if r['pass'] else 1)

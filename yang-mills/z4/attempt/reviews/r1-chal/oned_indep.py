"""oned_indep.py -- independent double-precision check of the child's 1D splitting at beta=64.
Predicates (fixed before first run):
 OP1 Delta via ground-state identity E(h)=1/2 sum T g g (h_i-h_j)^2 (h=f/g, folded blocks, double eigh)
     agrees with the child's Decimal value diff=2.073096659556E-14 (beta=64, N=204) to 1e-6 relative
     (tolerance: g(saddle)~e^-18, double eigvec abs error ~1e-15 -> rel ~1e-7 at saddle).
 OP2 plain eigenvalue difference agrees to 1e-2 relative (double cancellation: 1e-16/2e-14 ~ 1e-2).
 OP3 -log m <= c* sqrt(beta) at beta=64 (c*=4.605413).
"""
import numpy as np, math, sys
out = open(sys.argv[1], 'x')
beta, N = 64, 204
h = math.pi/N; M = 2*N; X = np.arange(M)*h; E = 2*np.arcsinh(np.abs(np.sin(X)))
d = X[:,None]-X[None,:]
K = sum(np.sqrt(beta/2/math.pi)*np.exp(-beta*(d+2*math.pi*k)**2/2) for k in (-2,-1,0,1,2))
A = h*np.exp(-E/2)[:,None]*K*np.exp(-E/2)[None,:]
Ae = A[:N,:N]+A[:N,N:]; Ao = A[:N,:N]-A[:N,N:]
we, ve = np.linalg.eigh(Ae); wo, vo = np.linalg.eigh(Ao)
g = np.abs(ve[:,-1]); f = vo[:,-1]
if f[N//4] < 0: f = -f   # orientation irrelevant (squared differences) but keep h ~ +1 near 0
# full-circle vectors: g(x+pi)=g(x), f(x+pi)=-f(x); normalise to sum h*v^2 = 1 on the circle
G = np.concatenate([g,g]); F = np.concatenate([f,-f])
G /= math.sqrt(np.sum(G*G)); F /= math.sqrt(np.sum(F*F))
H = F/G
# with A including weight h and vectors normalised in counting measure: Delta = 1/2 sum A_ij G_i G_j (H_i-H_j)^2
Dl = 0.5*np.sum(A*G[:,None]*G[None,:]*(H[:,None]-H[None,:])**2)
plain = we[-1]-wo[-1]
ref = 2.073096659556E-14
m = math.log(1+Dl/wo[-1]) if False else math.log(we[-1]/(we[-1]-Dl))
s = []
s.append('Delta_identity %.12e plain %.6e child %.12e' % (Dl, plain, ref))
s.append('OP1 rel %.2e %s' % (abs(Dl/ref-1), 'MET' if abs(Dl/ref-1) < 1e-6 else 'FAILED'))
s.append('OP2 rel %.2e %s' % (abs(plain/ref-1), 'MET' if abs(plain/ref-1) < 1e-2 else 'FAILED'))
nlm = -math.log(m)
s.append('-log m %.6f  c* sqrt(beta) %.6f  OP3 %s' % (nlm, 4.605413*8, 'MET' if nlm <= 4.605413*8 else 'FAILED'))
for x in s: print(x); out.write(x+'\n')

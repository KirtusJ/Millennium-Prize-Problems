"""q2b: retest of failed Q4 with a finer unreduced 6-D rule, reusing q2.py functions (import-free: exec of q2 defs not needed; copied).
Predicate (fixed before run): full(Na=16,Nt=14,Np=28) agrees with red N=40 value within 1e-8 for A and B,
 and |A+1/12|<1e-10 (observation from q2, labelled as a numerical observation not a theorem).
Tolerance source: red N=10 vs N=40 differs 2.8e-6 for B; the full rule has ~16x14 resolution, expected error << 1e-8 if geometric convergence."""
import re
src=open("q2.py").read().split("out=[]; ok=")[0]
exec(src)
f=full(16,14,28); W,x1,x2,c=red(40)
A=np.sum(W*x1*x2*c.real); B=np.sum(W*np.exp(-4*(1-c.real)))
dA=abs(f['A']-A); dB=abs(f['B']-B)
s=f"full(16,14,28): A={f['A'].real:.12f} B={f['B']:.12f} sumW={f['w']:.15f}\n|dA|={dA:.2e} |dB|={dB:.2e} Q4b {'PASS' if dA<1e-8 and dB<1e-8 else 'FAIL'}\n|A+1/12|={abs(A.real+1/12):.2e} {'PASS' if abs(A.real+1/12)<1e-10 else 'FAIL'}\n"
with open("q2b_result.txt","x") as fh: fh.write(s)
print(s)

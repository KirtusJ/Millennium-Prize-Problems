# T157 result

beta=1024, a1=pi/2, c=0, y=0, n_pairs=200000, seed=987654321 (default_rng)
control: 1.000000

Predicates (stated in t157.py docstring before first run):
P0 control = 1.000000
P1 sampler vs I2/I1
P2 f1(x)=f3(x)=exp(-sqrt(beta)Psi(a1))
P3 |sqrt(beta)*delta|<=1

Sampler check: mean Re g (2n draws)=0.998538 +- 0.000002 ; I2/I1 by numeric quadrature=nan ; asymptotic 1-3/(2b)+3/(8b^2)=0.998536 ; z=nan
P1 FAIL
P2 checked analytically: U1=(0,0,0,1),U2=1 -> u2=0, V=0,G=1,a2=0,Theta(0)=0,E=1. PASS
Mean a1'-a1 range check: a1' in [1.4321,1.7095]

delta1 = -0.087337 +- 0.019611  (log mean ratio=0.162663, mean ratio=1.176640 +- 0.023075, predicted=0.250000); sqrt(beta)*delta1 = -2.7948 +- 0.6275 ; P3 FAIL
delta3 = 0.027736 +- 0.019319  (log mean ratio=0.277736, mean ratio=1.320138 +- 0.025503, predicted=0.250000); sqrt(beta)*delta3 = 0.8876 +- 0.6182 ; P3 PASS

Rerun: cd /home/user/z4-workers/q1-E13/child/grandchild && python3 t157.py main <fresh_outdir> (needs control.txt in outdir; run 'python3 t157.py control <fresh_outdir>' first; files opened with mode x)

# notes g2-three (T79)
step0 17:0x control.txt = 0.272341 (-ln tanh 1). Lean READY exists; not planned to be used.
step0 no scipy/mpmath/sympy: Bessel by power series, 6j by Racah formula (own code).
step1 child control question chosen: I_2(2)/I_1(2) = 0.433127 (series, computed before writing prompt).
step1 xquad.py (6-D tensor quadrature, check K1, exit 0): Z3(1)=0.176721305342 X3(1)=0.014826962750 Z3(2)=0.062822729209 X3(2)=0.019705126670 (M16 vs M24 diff <=4e-12). Q0,Q1,Q2 met.
step2 child admitted T83 under T79; launched recorded as child-run1 (background). Child Qs: V=0 kernel ratio I_{2j+1}/I_1 at beta=2; Haar MC of Z3,X3 at beta=1,2. Expected -ln(I3(2)/I1(2)) = 2.011835 (from I3/I1=0.133745147).
step3 child returned (79 s, exit 0). Control graded FIRST: child/control.txt = 0.433127, expected 0.433127: CORRECT.
step4 ang.py (Racah exact) spot checks vs known 6j/3j values ok; cont3.py dev runs (scratchpad, not recorded): ctrl N=8 C1,C2 met (C2 gap 1.974988 vs 1.974964); h3 N=12 w=1: E0=6.5524, first excitation 5-fold (E+T2 of O_h = J=2) at +3.1471, then 0++ at +3.8090 (not converged).
step5 cont3.py edited before recorded runs: representative sectors only, x3 multiplicity for images. Launched recorded run cont3_runs (run_cont3.sh: ctrl N=10; h3 N=12,16,20,24 w=2; N=24 w=1.5).
step6 child report read AFTER grading control. Child MC (N=4e6, seed 2024): Z(1)=0.176791+-0.000089 (mine 0.176721, z=+0.79); X(1)=0.014744+-0.000232 (mine 0.014827, z=-0.36); Z(2)=0.062870+-0.000061 (mine 0.062823, z=+0.78); X(2)=0.019672+-0.000160 (mine 0.019705, z=-0.21). Q1: -ln(k1/k0)(beta=2)=2.0118191813; my note in step2 said 2.011835: MY arithmetic slip (correct -ln 0.1337451466 = 2.0118192). Grandchild T84 (admitted by child under T83, released): Z(1)=0.176840+-0.000126 Euler angles; beta->0: Z ~ 1-2.25 beta, X->0. Child task T83 released.
step7 cont3_runs (K3, exit 0): ctrl C1 (trivial: H diagonal), C2 met: 2-dir reduction E0=3.3505330, gap 1.9749642 vs 1.974964.
 h3 w=2: N=12/16/20/24: E0=6.5351031/6.5349054/6.5348872/6.5348854; J=2 (5-fold, E+T2) gap 3.020472/3.013550/3.012667/3.012554; 0++ gap 3.620213/3.605728/3.603284/3.602897. w=1.5 N=24: 6.5348877, 3.012640, 3.603209. C3,C4 met (C4: 3 clusters below E0+4, all odd size 1,5,1).
 FROM MEMORY: E0 of -1/2 Lap + (g^2/2) sum_{i<j}|A_i x A_j|^2 at g=1 is ~4.1167 (Luscher-Munster/van Baal era); ours has g^2=4 -> x 4^{1/3}: 6.5349/1.5874 = 4.1167. Agreement, not relied on.
step8 lat3.py dev (scratch): dec beta=2 N=8: 1.6376208 (2-dir 1.63761996, 8e-7), 1.8823418 (1.88234137), free link 2.0118192 = -ln(I3/I1). full beta=4 N=8: m_e=0.96972 (doublet-ish 0.96992), 1.18522. Launched cont3_N28 recorded.
step9 lat3 N=12 dev too slow (python pairA loops, >2 min in first sector), stopped. Launched recorded lat3_runs: v0, dec(2,4), full beta=0.01,1,2,4,8 at N=6,8; MA 64 at beta=4 N=8; N=10 at beta=2,4,8.
step10 reran child q1.py,q2.py in scratch copy (python3 -I): output identical. Child q2 code read: explicit 2x2 matrices, V and chi_1 as defined.
step11 lat3_runs K4 exit 0; analyse3 -> results/analysis3.md. L1,L2,L3,L5 met; L4 met 5 failed 3 (beta=4 N6-8, beta=8 N6-8 and N8-10): truncation, own expectation that N<=10 suffices; not a target defect.
 Lattice m_e (N=10): beta=2 1.6215047, beta=4 0.9689303, beta=8 0.9447 (not converged, dN=1.5e-2). Lowest excitation is a 2-fold level in sector (000) (S3 'E'); its splitting at beta=8 (8e-4) is a truncation artefact of the product A=E12E13E23 (not S3-symmetric at finite N).
step12 report.md written; registers verified (both PASS lines quoted).

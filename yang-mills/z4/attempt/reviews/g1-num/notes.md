# g1-num notes
Step 0: control.txt = 0.272341 (-ln tanh 1). Lean READY exists (not used). numpy 2.5.3 only (no scipy/mpmath/sympy).
Step 1: register pcp initialised. Child admitted as T73 (parent T72). Reference numbers for the child computed first (ref_child.py -> ref_child.out):
  I1(1)/I0(1)=0.446390; A=-1/12=-0.0833333333; B=0.1982495197; -ln(I1/I0)(4)=0.146735196417, (16)=0.032287934847; -ln(I2/I0)(4)=0.565213711762,(16)=0.129002770250.
Child started in background (child-run1) at ~16:2x.

Step 2 (derivation, by hand; see report.md section D for the full text).
Wilson action S = beta sum_p (1 - 1/2 Re Tr U_p) on sites (0,0,t), t in Z, links U_1(t),U_2(t) (spatial), g(t)=U_0(t) (temporal).
Per site: plaquettes (1,2),(0,1),(0,2), one each. (1,2): U_1(x)U_2(x+1)U_1(x+2)^-1 U_2(x)^-1 with x+1=x on the 1x1 torus -> U1U2U1^-1U2^-1 : once per slice -> V = beta(1-1/2 Tr comm). Matches brief.
(0,i): g(t) U_i(t+1) g(t)^-1 U_i(t)^-1 ; Re Tr equals Re Tr(U_i(t) g W_i^-1 g^-1) (trace of inverse, SU(2) traces real) -> one per spatial link per step. Matches brief. Splitting e^{-V} symmetrically gives T = e^{-V/2}Ke^{-V/2}. No factor differs.
Coordinates: U=cos a + i sin a n.sigma, Haar = (2/pi) sin^2 a da dOmega/4pi. Invariants (a1,a2,gamma): measure (2/pi)^2 sin^2a1 sin^2a2 da1 da2 (1/2) sin g dg.
Commutator: 1/2 Tr(U1U2U1^-1U2^-1) = 1 - 2 sin^2a1 sin^2a2 sin^2 gamma (to be checked numerically from explicit matrices) -> V = 2 beta s1^2 s2^2 (1-t^2), t=cos gamma.
Basis: S^3 hyperspherical harmonics: degree n=2j, SO(3)(conjugation) spin L=0..n, radial sin^L a C^{L+1}_{n-L}(cos a). Invariant pair functions Phi_{n1 n2 L} = F_{n1 L}(a1) F_{n2 L}(a2) sqrt(2L+1) P_L(cos gamma), L<=min(n1,n2).
K diagonal: per link eigenvalue int e^{-beta(1-1/2TrU)} chi_j/d_j dU = e^{-beta}(2/beta) I_{n+1}(beta). Center parity (-1)^{n_i}; U2->U2^-1 parity (-1)^L; exchange c_{n1n2L}<->c_{n2n1L}.
Method: M = K^{1/2} E K^{1/2}, E_ab = <Phi_a|e^{-V}|Phi_b> by Gauss quadrature (uniform a-grid = Gauss-Chebyshev-U; Gauss-Legendre in t); same nonzero spectrum as T. Truncation n_i<=N is a compression -> top eigenvalues increase monotonically with N (Cauchy interlacing) if E exact.
Continuum: -log K ~ (1/2beta)(-Lap_S3), V ~ 2beta|A1 x A2|^2, A=beta^{-1/3}Y => H ~ beta^{-1/3}[ -1/2 Lap_Y + 2|Y1xY2|^2 ] so kappa=2 in the normalization U=exp(i Y.sigma) (vector cross product). Predicted: m_e beta^{1/3} -> E1(h).
Step 3: controls1 FAILED (exit 1, LinAlgError): own defect - trapezoid e^-b I_n underflows to negative at beta=0.01, n>=5 -> sqrt NaN. Fix: use Miller recurrence for kn (C1 still compares both). controls2 next.
Step 4: controls2 exit 1. Passed: C2 (orth 7e-14), C3 (commutator formula vs matrices 5.6e-16), C4 dense (U(1)^2 ratios to 4.8e-15 at b=4,16; |V| from matrices <= 5e-15), C5 (V=0 SU(2): 6e-15, dims 285=285), C6 strong coupling (b=0.01: m_e-pred=-0.0033, m_o-pred=-0.0025; b=0.001: -3.3e-4, -2.5e-4; linear in beta, within 10 beta).
 FAILED C1: OWN EXPECTATION. Trapezoid e^-b I_n has ABSOLUTE error ~1e-17, so relative error is large for tiny I_n (rel 1e83 at b=0.1,n=40). Miller agrees with the power series to 3e-16 (b=0.1, n<=7). Model uses Miller.
 FAILED C4@16 Lanczos sub-test: OWN TEST DESIGN. V from matrices is 5e-15 not 0, splits the exact degeneracies, so Lanczos legitimately returns two near-copies of 0.968; comparing with the list of DISTINCT values misaligns. Lanczos alone with V=0 returns [1,.96822776,.93746499,.87897153] = distinct exact. Amended predicates in controls_b.py.
Step 5: child T73 returned. Control graded FIRST: child/control.txt = 0.446390 = my value -> correct. Q1 values equal mine (ref_child.out) to all 12 printed digits. A=-0.0833333333 (= -1/12, mine -1/12), B=0.198249519694 (mine 0.1982495197). Child recorded its own failed Q4 (coarse-rule tolerance; own expectation). Grandchild T75 (Euler-angle recomputation of A,B) agrees. T73 released. I reran q1.py, q2.py, q2b.py and grandchild/run.py in scratchpad copy: outputs identical.
Step 6: dev timing (scratchpad, not results): beta=64 N=48 Nx=Nt=80 -> 5 s; N=64,Nx=100 identical to 10 digits. ee gaps beta=8: 0.5156 (Leven,ex-); beta=64: 0.4399 (Leven,ex-), 0.4557 (Lodd,ex+), 0.5185 (Leven,ex+).
Step 7: cont.py: first version had Golub-Welsch weights -> spurious negative eigenvalues (-1e5) at K=16: OWN DEFECT (tiny weights lose relative accuracy). Fixed with Christoffel weights; orthonormality 8e-15; moment check Gamma(11.5) ok.
 dev: (K,Lmax,w)=(20,28,1): E0=3.35053306; sectors lowest: (Le,ex-) 5.32549860, (Lo,ex+) 5.32549708 [degenerate: continuum has O(2) flavor rotation (Y1,Y2)->rotation, lattice breaks it to D4], (Le,ex+) 2nd 5.72541082.
 => continuum gap E1 = 1.97496 ; second invariant gap 2.37488.
Step 8: sweep running. Partial (dev analysis, scratch): m_e b^(1/3) = 1.636 (32), 1.760 (64), 1.837 (128); local exponents 0.07,0.23,0.27. Center-odd splitting at b=128 is 3e-16 = double-precision floor -> reported as below floor. analyse.py display adjusted for that (no predicate change).
Step 9: lat_sweep1 (beta 2..512, 27 runs) exit 0, 771 s. Dev analysis: all shown levels converged (dE(N) <= 3e-11, dE(grid) <= 1e-13 at beta=512).
 m_e b^(1/3): 2.063,1.212,1.031,1.364,1.636,1.760,1.837,1.887,1.919 (b=2..512); local exponents ... 0.228(32->64),0.271,0.295,0.309.
 Increments of m_e b^(1/3): 0.124,0.077,0.0496,0.032 -> ratios 0.62,0.64,0.645 ~ 2^(-2/3)=0.630 => leading correction ~ b^(-2/3); geometric extrapolation 1.973 vs continuum E1=1.975.
 Center-odd splittings: exp(-c sqrt b), -ln m_eo/sqrt(b) = 2.49 (32), 2.89 (64); below double precision floor from b=128 on.
 Launched cont_runs (K,L)=(16,24),(20,32),(24,40) w=1 and (24,40) w=1.5, and lat_sweep2 (beta=1024) on 1 core each.
Step 10: cont_runs exit 0. (24,40,w=1): E0=3.3505330 E1=5.3254972/5.3254970 ; (24,40,w=1.5): E0=3.3505330, E1=5.3254970 (doublet exact to 1e-7), E2=5.7254082. Gap E1-E0=1.974964, E2-E0=2.374875. Control P1 4e-16. Note: w=1 vs w=1.5 bases are not nested, so the RR-monotone part of A4 between them is not a valid variational test (my predicate design); K/L nesting at fixed w is (16,24)->(20,32)->(24,40): monotone decreasing in all printed levels.
Step 11: lat_sweep2 (1024) exit 0. analyse exit 0: m_e b^(1/3)=1.939100 at 1024, local exp 0.318; 3-term fit c0=1.9762 (c1=-0.052 ~ 0, c2=-3.27); E1=1.974964. Mislabel noticed: '2nd ee gap' column is the O(2)-doublet partner, compare with E1 (0.9866 at 1024), not E2.
Step 12: report.md written.

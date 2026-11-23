# notes.md — r5-bench (builder, free lattice Maxwell benchmark)

## Step 0 control
control.txt = 0.272341 ( -ln tanh 1 ).

## Step 1 delegation (rule 7), launched first so it runs in parallel
Question given to child (child/): continuum C(t) with D_t having k^ -> |k|, sum over (2pi)Z^3\{0},
same periodic Gaussian f (images n in {-1,0,1}^3, c=(.5,.5,.5), peak 1), R=0.1 and 0.05, t=0.05,0.1,0.2,
spherical cutoff |k|<=K with convergence shown, -d/dt log C at t=0.2. Control question: zeta(4) to 8 decimals.
Child was given only the formula and the definition of C, not my code.

## Step 2 (B0) derivation of D_t
Conventions: A_i(x) on link x -> x+e_i, x integer site, physical position bx. Fourier with link-midpoint
phase: A_i(x) = N^{-3/2} sum_k e^{i k.(x+e_i/2) b} a_i(k)  (unitary => a, e canonical, [a_i(k), e_j(k')^*] = i delta).
Then
 theta_12(k) = e^{ik_1b/2} a_1 (1 - e^{ik_2 b}) + e^{ik_2 b/2} a_2 (e^{ik_1 b} - 1)
             = e^{i(k_1+k_2)b/2} * i b (k^_1 a_2 - k^_2 a_1),     k^_i = (2/b) sin(k_i b/2).
The phase e^{i(k_1+k_2)b/2} is the plaquette centre x+(e_1+e_2)/2; it multiplies theta_12(k) and its conjugate
and CANCELS in <theta(k) theta(k)^*>. (Equivalently B_3 is located at plaquette centres; D_t(x-y) only depends on
the difference, both points carry the same offset.) Same for general theta_ij: theta_ij(k) = i b e^{..}(k^ x a)_l.
Gauss law: div E = 0  <=>  sum_i k^_i e_i(k) = 0 (midpoint variables) -> transverse w.r.t. the REAL vector k^.
Gauge directions a ∝ k^ drop out of theta. Zero mode k=0 (3 constant A_i, flat holonomies) removed.
 sum_{i<j} |theta_ij(k)|^2 = b^2 |k^ x a|^2 = b^2 k^2 |a_T|^2.
H = sum_k [ (g^2/2b) |e_T|^2 + (b k^2/(2 g^2)) |a_T|^2 ]  ->  oscillator with mass m = b/g^2, frequency omega:
 m omega^2 = b k^2/g^2 => omega = k^ (two transverse polarisations per k).
Ground state: <q q> = 1/(2 m omega) = g^2/(2 b k^); Euclidean <q e^{-tH} q> = g^2/(2 b k^) e^{-t k^}
(H normal-ordered, i.e. vacuum energy subtracted — implicit in the statement).
Polarisation sum: sum_pol (k^ x eps)_3 (k^ x eps)_3^* = k^2 - k^_3^2 = k^_1^2 + k^_2^2.
 <theta_12(x) e^{-tH} theta_12(y)> = N^{-3} sum_{k!=0} e^{ik.(x-y)b} b^2 (k^_1^2+k^_2^2) g^2/(2 b k^) e^{-t k^}.
B_3 = theta_12/(g b^2):
 D_t = N^{-3} b^{-3} sum e^{ik.(x-y)b} (k^_1^2+k^_2^2)/(2 k^) e^{-t k^}
     = ell^{-3} sum_{k!=0} e^{ik.(x-y)b} ((k^_1^2+k^_2^2)/k^2) (k^/2) e^{-t k^}.
AGREES with the statement (normalization k^/2, projector (k^_1^2+k^_2^2)/k^2 with lattice k^_i).
Only notational remark: the statement writes e^{ik.(x-y)} with x integer; it must be e^{ik.(x-y)b} (or x physical).
Not a defect of substance. Modes with k^_1=k^_2=0, k_3 != 0 contribute 0 (B_3 blind to them) — consistent.

## Step 3 (B0 hypothesis test) b0_check.py, N=4, run via PCP (exit 0)
Q1 ker K = 66 = 63 gauge + 3 zero modes, 126 physical modes: MET
Q2 physical frequencies = {k^, twice}: MET (7.7e-16)
Q3 direct position-space <B3 B3> vs formula, t=0 and t=0.3: MET (1.1e-13, 1.2e-14 abs; D(0)=203.119000903 at t=0)
Q4 translation invariance: MET
=> statement's D_t (normalization k^/2, lattice projector) confirmed. No defect.

## Step 4 (B1/B2) bench.py via PCP (exit 0), results_bench_1.txt/.json. Tally: met 46, failed 4, measured 9.
R=0.1: C_b(0) b^5 = 8.0086e-3, 8.0850e-3, 8.1052e-3, 8.1104e-3 (N=16..128); ratios 32.305, 32.080, 32.020; exponent fit -5.0023. P1 MET.
R=0.05: ratios 32.69, 32.31, 32.08. P1 MET. C0 b^5 ratio R.1/R.05 -> 8.005 (= int f^2 ratio 8): "constant times int f^2" supported.
P2: t=0.1, 0.2 MET (diff ratios 4.1-5.8). t=0.05 FAILED both R: first ratio 1.21 / 1.08 (N=16 is pre-asymptotic:
  C_b(0.05) is non-monotone 181 -> 266 -> 195 -> 178; t*k^max = 0.05*2N*sqrt3 = 2.8 at N=16, BZ edge not suppressed).
  Second ratio 4.08 / 4.14. => failure is MY expectation (range of N), not a defect of S2.
P3: all S5-derived bounds MET for every N, tau; ratios converge (<1.7% change 64->128). tau*M1/M0 ~ 2.6-3.2, tau^2 M2/M0 ~ 8-11.
P4: rate(3) -> 12.5694 vs Emin_lattice = 4N sin(pi/N) = 12.5651 (N=128): MET. rate(0.2) = 28.5 (2.27 x 4pi), far from asymptotic.
  P4c FAILED: lattice lowest two-photon atom 4N sin(pi/N) is strictly BELOW 4pi/ell by (pi b)^2/6 relative for every N.
  S4's "at or above 2(2pi/ell)(1+O(b^2))" is true only if O(b^2) is allowed negative; "at or above 2(2pi/ell)" is false.
  Wording defect of S4 (small); the no-gap conclusion is unaffected.
B2: C_{R=.05}(t/2)/C_{R=.1}(t) = 4.09 (t=0.1), 4.16 (t=0.2): near R^-2 Phi(t/R) dimensional scaling, deviation grows with t/ell
  (box effects); same-t ratios 8.7, 10.3, 14.9 — not a power law in R at fixed t.

## Step 5 (B3) leading-order map SU(2) plaquette -> B^2 (LEADING ORDER ONLY, not a result about interacting YM)
U_p = exp(i theta^a sigma^a/2), theta^a = plaquette angle of colour a (a=1,2,3 = dim SU(2)), theta^a_12 = g b^2 B^a_3.
Normalized character chi_{1/2}(U)/2 = (1/2) tr U = cos(|theta|/2) = 1 - (1/8) sum_a (theta^a)^2 + O(theta^4)
  = 1 - (1/8) g^2 b^4 sum_{a=1}^{3} (B^a)^2 + O(g^4 b^8 B^4).  const = 1/8 (1/4 for unnormalized tr U = 2 - ...).
Consistency: Kogut-Susskind magnetic term (4/(g^2 b)) sum_p (1 - (1/2)tr U_p) = (1/(2 g^2 b)) sum theta^a theta^a, i.e. the
statement's abelian term per colour. Hence O_YM = b^3 sum f (1/2 tr U - vac) ~ -(g^2 b^4/8) sum_a O^a, and at Gaussian order
C_YM = (g^2 b^4/8)^2 * 3 * C_b (colours independent). S6's Z(b) = const/(g^2 b^4) has const = 8 (sign -) at leading order.

## Step 6 delegation outcome + compare.py (PCP exit 0)
Child returned continuum C(t) (spherical cutoff, analytic |fhat|^2, exact FFT linear convolution); first child run failed its own
K-convergence predicate (its expectation), second passed. I read corr.py and reran it myself (results_3.txt, identical table).
P2-cont: 6/6 MET. C128/Ccont-1 = +2.5e-2, +6.6e-3, +2.1e-3 (R=.1; t=.05,.1,.2); Richardson brings to -8e-3, -3.5e-4, -2.8e-5.
Rate at t=0.2: lattice 28.5215 vs continuum 28.5063 (R=.1).

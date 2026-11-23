# r6-loop notes (worker of Z4)

## Step 0
control.txt = 0.272341 (= -ln tanh 1). PCP register `pcp` initialized (method not pinned, expected).
Sub-agent launched on L2 (continuum mode sum), child/, control question: sum n e^{-n} = e/(e-1)^2 = 0.920674.

## Step 1 — L0, W1 by algebra
Normalization: B_3 = theta_12/(g b^2), so Phi = b^2 sum_p B_3(p) = (1/g) sum_p theta_p and W = exp(i sum theta) = exp(i g Phi).
H has g^2 E^2 and theta^2/g^2, so <theta theta> ∝ g^2 and D_t (hence G_b) is g-independent. Consistent with W = e^{igPhi}.

Phi is linear in the oscillators: Phi = sum_k (c_k a_k + c_k^* a_k^†). Define Phi_E(t) = e^{-tH} Phi e^{tH} (not Hermitian; linear in a, a^†,
a_k -> a_k e^{+... } : a_k e^{t w}, a^† e^{-t w}; careful, e^{-tH} a^† e^{tH} = e^{-tw} a^†). Since H Omega = 0,
  <W* e^{-tH} W> = <Omega| e^{-igPhi} e^{-tH} e^{igPhi} |Omega> = <Omega| e^{X} e^{Y} |Omega>,  X = -ig Phi, Y = ig Phi_E(t).
X, Y linear in a, a^† with c-number commutator, so (BCH + Gaussian vacuum) <e^X e^Y> = exp(½<X^2> + ½<Y^2> + <XY>).
  <X^2> = -g^2 G_b(0); <Y^2> = -g^2 <Omega|e^{-tH} Phi^2 e^{tH}|Omega> = -g^2 G_b(0) (e^{±tH} Omega = Omega);
  <XY> = (-ig)(ig) <Phi e^{-tH} Phi> = + g^2 G_b(t).
=> <W* e^{-tH} W> = exp(-g^2 G_b(0) + g^2 G_b(t)). Sign as stated. W1 STANDS (algebra).
<W> = exp(½<(igPhi)^2>) = exp(-g^2 G_b(0)/2), real, so |<W>|^2 = exp(-g^2 G_b(0)).
Does the conjugate matter? Yes: without it, <W e^{-tH} W> = exp(-g^2 G_b(0) - g^2 G_b(t)) (cross term (ig)(ig) = -g^2). Only the
W* version is the inner product <W Omega, e^{-tH} W Omega>, i.e. the reflection-positive correlator; the + sign is what makes rho > 0.
Also: ||e^{-tau H}(W/<W> - 1)Omega||^2 = <W*e^{-2tauH}W>/<W>^2 - 1 - 1 + 1 = rho_b(2tau) (uses <W> real and e^{-H}Omega=Omega). Checked.
rho = exp(g^2 G) - 1 = sum_n g^{2n} G^n/n!, and each G(t)^n is a positive combination of exponentials (G has positive weights
per mode), so rho is a positive finite sum of exponentials in the box: S5 hypotheses hold (finite box, finite lattice).

## Step 2 — Stokes on the lattice (algebra)
For a planar M x M square of plaquettes in the 1-2 plane, sum_p theta_12(p) = sum_p [A1(x)+A2(x+e1)-A1(x+e2)-A2(x)]: each interior
link appears in two adjacent plaquettes with opposite signs and cancels; boundary links survive once with the orientation of the
counterclockwise boundary. So sum_p theta_p = oriented link sum around Gamma, exactly (no b correction). Numerically checked in the program (P0).
Centering: |F(k)|^2 is translation invariant, so "centered in the box" has no effect on G_b. R/b = R N must be an integer: R = 0.25 needs
4 | N, R = 0.125 needs 8 | N; N = 16..256 qualify (M = 4..64 and 2..32).

## Momentum form
G_b(t) = l^{-3} sum_{k!=0} |F(k)|^2 ((kh1^2+kh2^2)/kh^2)(kh/2) e^{-t kh},  F(k) = b^2 sum_{n1,n2=0}^{M-1} e^{ib(k1 n1 + k2 n2)},
|F|^2 = prod_{i=1,2} b^2 sin^2(k_i R/2)/sin^2(k_i b/2)  (= R^2 per factor at k_i = 0). Independent of k3.

## Step 3 — L1 program loop_bench.py (register K1, exit 1 expected: P5c predicted to fail)
Counts: met 40, failed 16, measured only 4. Output results_L1.txt.
- P0a Stokes exact (diff 4e-16); P0b momentum form = position form b^4 sum D_t(p-p') at N=16 to 12 digits.
- Q1/W2: c1 = 0.32140 (R=.25) vs 0.32116 (R=.125) on N=16..128 (0.08% apart); 0.32143 vs 0.32133 on 16..256. c2 = -0.199 / -0.190
  (log correction present, negative: corners). Residuals <= 1e-3. Local exponent 1.019 / 1.033. PERIMETER LAW; not area.
- Q2/W3: t >= 0.1 differences shrink at O(b^2) (ratios 4.2-5.0); t = 0.05 non-monotone at N=32 then ratio 3.3, 5.0; t = 0.02 not in
  regime by N=256 (d128/d256 ~ 2.1). P2c fails at t=0.1 by 1.04e-2 vs my 1e-2. All P2 failures: my expectation/my N range, not W3.
- Q3: log10 corr at N=256: -34.9 (R=.25,g=1), -9.35 (g=.5); strictly decreasing in N. W2 last sentence stands.
- Q4: rho/g^2 -> G with deviation within [x/2, x e^x/2] in all 6 cases. W4 arithmetic stands.
- Q5: lowest weighted energy = 2N sin(pi/N) exactly (mode |n|=1); rate(5->6) matches it to 9e-7; vs 2pi off by pi^2 b^2/6
  (4.0e-4 at N=64, 1.0e-4 at N=128): P5c fails as predicted (wording, like S4 defect 1). Form-factor zeros per axis at n = multiples of
  l/R (4, 8 for R=.25; 8 for R=.125): |n|=1 survives for every R < l, so 2pi/l is the rate for both sizes.
- Observation: d256(R=.125,t=.05) = d128(R=.25,t=.1) = -3.346e-3: scaling (R,t,b) -> 2x at fixed l holds to 4 digits, finite-l effects small.

## Step 4 — L2 delegated (sub-agent, child/). Control answer 0.920674 correct. Its check K1, K2 exit 0; its verify PASS.
It could not write child/report.md (harness blocked); report given in its message. I reread continuum.py (formula matches, octant
symmetry with multiplicity 2 per nonzero component, M doubling to rel 1e-6) and reran it in rerun/ via my register (K2): output
byte-identical (C0). compare.py (K3, exit 1 expected): C1 6/6 met (Richardson 128/256 vs continuum: 1e-6..1.9e-4), C3 6/6 met,
C2 (t=0.02) 0/2 as predicted (3.6e-3, 4.2e-3; lattice not yet in O(b^2) regime, but G256 within 1.3% and approaching).
Continuum rate at t=3: 6.28590 (R=.25), above 2pi by 4e-4 and decreasing: consistent with W5.

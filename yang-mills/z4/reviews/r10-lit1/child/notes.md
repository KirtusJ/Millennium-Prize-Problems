# Notes (Q3)

- Step 0: control = -ln(tanh 1) = 0.272341 (written to control.txt; computed with python -I, math.log/math.tanh).
- Step 1: PCP register initialised at child/pcp (method not pinned, as expected).
- Step 2: extract.py written with predicates P1-P4 in docstring before first run.
  Run via pcp check K1: exit 0. Outputs text/chatterjee_1602.01222.txt (49 pages),
  text/chatterjee_2401.10507.txt (50 pages). Printed page numbers coincide with PDF page
  numbers in both files (page 1 of each PDF carries printed number 1).

## 1602.01222 (free energy)
- p1 abstract: explicit leading term of free energy, 3D U(N) lattice gauge theory, any N,
  lattice spacing -> 0; 4D only in weak coupling limit.
- p2: Wilson action, phi(U)=Re Tr(I-U), measure exp(-S/g0^2) dHaar; F = log Z / |Lambda|.
- p3-4: Theorem 2.1 (main result): any d>=2, N>=1, K_d = lim K_{n,d} (from log det of axial-
  gauge-fixed quadratic form M^0_n) exists finite; limit as n->inf, g0->0 (independently)
  of F(B_n,g0) - (1/2)(d-1-d/n+1/n^d) N^2 log g0^2 equals (d-1) log(prod_{j<N} j!/(2pi)^{N/2}) + N^2 K_d.
- p4: Theorem 2.2: d=2,3, scaled lattice eps Z^d with coupling g^2 eps^{4-d}, n->inf, eps->0,
  n*eps bounded below, fixed g: log Z = n^d(...) + o(n^d).
- p5: Theorem 2.3: d=4, n->inf, eps->0, g->0 simultaneously, no relation required.
- p4 & p10: Gaussian behaviour appears only as proof heuristic (small-scale Gaussian process).
- p9: author says complete solution needs exact asymptotics of Z, not only the leading term
  of the exponent derived here; observables not well-behaved are cited as reason to study Z.
- No theorem about Wilson loops / correlations / Gaussian limit of observables (grep for
  "Wilson loop": no hits; "observable": only p9 discussion).

## 2401.10507 (Higgs)
- p1 abstract: any d>=2; SU(2) lattice YM + Higgs in fundamental rep, degenerate potential;
  unitary gauge fixing; eps->0, g->0, alpha->inf with alpha*g = c*eps, g = O(eps^{50d});
  stereographic projection of gauge field -> massive Gaussian field; also U(1).
  Last sentence of abstract: non-Gaussian scaling limit remains open.
- p4-5: degenerate potential = zero at 1, infinite elsewhere (Higgs length fixed to alpha).
- p11: Theorem 3.1 (U(1)): Z(x)=eps^{-(d-2)/2} Y(x/eps) -> Euclidean Proca field param c^2.
- p12: Theorem 3.2 (SU(2)): A_e = (sqrt2/g) sigma_3(tau(V_e)) in R^3; same scaling; Z -> 3
  independent Euclidean Proca fields with parameter c^2/2. Infinite-volume Gibbs measure =
  any periodic-b.c. weak limit (p10, p12).
- p9-10: Proca field param lambda has mass sqrt(lambda) (Lemma 2.6).
- p13: mass only in the scaling limit; nothing about lattice exponential decay.
- p15: three components decouple because non-Abelian couplings are lower-order; fast g->0
  suppresses non-Abelian interference.
- p16 Sec 3.5 Open questions: whether g=O(eps^{50d}) needed; for SU(2) slow decay of g may
  bring non-Abelian effects, "possibly leading to a different scaling limit"; extending to
  general Higgs potentials open. (Sec 3.5 does not use the words "non-Gaussian"; the explicit
  statement is in the abstract, p1.)
- p16: method does not extend to SU(3) (nontrivial stabilizer after gauge fixing).

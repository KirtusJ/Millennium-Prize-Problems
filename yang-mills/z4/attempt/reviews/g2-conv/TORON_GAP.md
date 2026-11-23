# TORON_GAP: lower-bound attempt on the center-even gap, single-site SU(2) cylinder (g1-toron, T71)

**Strongest target closed: NONE of T1, T2, T3, T4.**
Proved here:
- an exact reformulation of the gap problem that avoids the Golden–Thompson direction problem;
- a closed form for the potential in the two-direction model;
- a ground-state representation that reduces the zero-point (ground-energy) lower bound to ONE pointwise inequality;
- explicit kinetic bounds, conditional on one cited Bessel-ratio inequality.

The gap itself needs one further inequality, M1 below, which I did not prove. Numerics on the two-direction model were done by exact Galerkin in the spin-network basis (β ≤ 16). They are consistent with T4 but are not a proof.

Tags: PROVED (argument given here) / PROVED+LEAN (scalar step checked in scalar.lean) / CITED (locator; how read) / CLAIMED / MISSING.

## 0. Setting (k = 2; k = 3 differs only in V)

- **Hilbert space.** H = L²(SU(2)^k, Haar).
- **Potential.** V(U) = β Σ_{i<j} (1 − ½ Re Tr(U_i U_j U_i⁻¹ U_j⁻¹)).
  - Normalization: with one spatial site, the plaquette (i,j) at time t is U_i(x)U_j(x+e_i)U_i(x+e_j)⁻¹U_j(x)⁻¹ = U_iU_jU_i⁻¹U_j⁻¹, because x + e_i = x.
  - So the Wilson action β Σ_P (1 − ½ Re Tr U_P) splits as Σ_t V(U(t)) plus the temporal plaquettes.
- **Kinetic operator.** In temporal gauge U_0 = 1 the temporal plaquettes give β(1 − ½ Re Tr U_i(t+1)U_i(t)⁻¹).
  - Kernel: k(g) = e^{(β/2)Tr g}/Z, with Z = ∫ e^{(β/2)Tr g} dg = 2I_1(β)/β.
  - K = (gauge projector) ∘ (convolution by Π_i k(U_iW_i⁻¹)). The projector is the average over the temporal link W ↦ gWg⁻¹. It commutes with the convolution.
  - Overall constants e^{−β} drop out of λ1/λ0.
- **Transfer operator.** T = e^{−V/2} K e^{−V/2}.
- **Eigenvalues of K** (PROVED):
  - on spin j of each factor, the eigenvalue is κ_j = I_{2j+1}(β)/I_1(β);
  - computation: (1/(2j+1))∫ e^{β cos θ} χ_j (2/π) sin²θ dθ = (I_{2j} − I_{2j+2})/(2j+1) = (2/β) I_{2j+1}(β), then divide by the j = 0 value;
  - consequently K is positive, injective and of norm 1 (I_n(β) > 0).
- **Positivity of T** (PROVED, no citation needed): ⟨f,Tf⟩ = ⟨g,Kg⟩ ≥ 0 with g = e^{−V/2}f. T is trace class with a continuous, strictly positive kernel, so Perron–Frobenius (Jentzsch) gives a simple top eigenvalue λ0 with a positive eigenvector. That eigenvector is invariant under every symmetry, so it lies in the center-even gauge-invariant sector.
- **Symmetries.** Simultaneous conjugation; the center flips U_i → −U_i, each i separately; permutations of the directions.
  - In the spin basis the flip i acts by (−1)^{2j_i}.
  - The center-even gauge-invariant sector is the span of Ψ_{j1 j2 J} = Tr[(D^{j1}(U1) ⊗ D^{j2}(U2)) P_J] with j1, j2 integers and J ∈ j1 ⊗ j2. These functions are orthogonal, with ‖Ψ‖² = (2J+1)/((2j1+1)(2j2+1)) (Schur).
- **Gap.** m_e(β) = −ln(λ1/λ0), with λ1 the second eigenvalue of T on that sector.

## 1. Proved steps

**S1. Exact reformulation (PROVED).** Substitute f = e^{V/2} g (a bijection of H, since V is bounded) and let W := e^V − 1 ≥ V ≥ 0. Then
  R(f) = ⟨f,Tf⟩/⟨f,f⟩ = ⟨g,Kg⟩/⟨g,(1+W)g⟩, and 1 − R(f) = ⟨g,(1−K+W)g⟩/⟨g,(1+W)g⟩ =: Q(g).
- The min-max values satisfy μ_k = 1 − λ_k (the k-th eigenvalue of T in the sector). This is the generalized eigenproblem (1−K+W)g = μ(1+W)g.
- Both operators are sums of nonnegative pieces, so no Trotter, Golden–Thompson or Araki inequality is needed. (Araki–Lieb–Thirring goes the wrong way for an upper bound on λ1: e^{A+B} ≺_log e^{A/2}e^Be^{A/2}.)
- Also m_e ≥ (λ0−λ1)/λ0 ≥ μ1 − μ0.

**S2. Regime split (PROVED+LEAN, F5).** Let ν0 := inf spec(1−K+V) on the sector. Then μ0 ≥ min(½, ν0/2), i.e. λ0 ≤ 1 − min(½, ν0/2).
- Proof: write a0 = ⟨g,(1−K)g⟩ ≤ n = ‖g‖², v = ⟨g,Vg⟩ ≤ w = ⟨g,Wg⟩.
- If w ≥ n, then Q ≥ ½.
- Otherwise Q ≥ (a0+v)/(2n) ≥ ν0/2.

**S3. Closed form of the potential, k = 2 (PROVED, checked numerically to 8e−16, P1).**
- Coordinates: U1 = exp(iθ1σ3), U2 = cos θ2 + i sin θ2 n·σ, with the axis of U2 at angle φ to the axis of U1. Then ½Tr(U1U2U1⁻¹U2⁻¹) = a0² + a3² + (a1²+a2²)cos 2θ1, so
  **V = 2β sin²θ1 sin²θ2 sin²φ.**
- The zero set (commuting pairs) is {θ1 ∈ {0,π}} ∪ {θ2 ∈ {0,π}} ∪ {φ ∈ {0,π}}.
- Transversally to the torus of U1, the potential is 2β sin²θ1 · ρ², with ρ² = a1² + a2² the squared distance of U2 from that torus. This is the exact group analogue of x²y².

**S4. Product splitting (PROVED+LEAN, F1).** 1 − K1K2 ≥ ½(1−K1) + ½(1−K2), for commuting 0 ≤ K_i ≤ 1 (spectral calculus from 1−ab ≥ ((1−a)+(1−b))/2 on [0,1]²). The gauge projector commutes with all of these.

**S5. Kinetic upper bound for κ (CITED + PROVED derivation + numerically checked).**
- Amos's inequality I_{ν+1}(x)/I_ν(x) ≤ x/(ν+½+√((ν+½)²+x²)), for ν ≥ 0 and x > 0.
  - CITED: D. E. Amos, "Computation of modified Bessel functions and their ratios", Math. Comp. 28 (1974) 239–251.
  - Cited from memory; **not read in this session**.
  - Child T74 checked it on 2211 grid cases with no failure.
- Derivation from Amos:
  - r_ν ≤ 1/(1+(ν+½)/x);
  - ln(1+y) ≥ y/(1+y) (F3, LEAN);
  - (ν+½)/(x+ν+½) ≥ (ν+½)/(x+n+½) for ν ≤ n;
  - Σ_{ν=1}^{n}(ν+½) = n(n+2)/2 (F2, LEAN).
- Together these give, for n = 2j:
  **κ_j ≤ exp(−2j(j+1)/(β+2j+½)).**
  Child T74: 2200 grid cases, 0 failed; tightest case (n=1, β=512) has log-slack 1.1e−5.
- Consequences for β ≥ 8:
  - for 2j+½ ≤ β, κ_j ≤ e^{−j(j+1)/β};
  - for larger j, κ_j ≤ e^{−(β−½)/4};
  - hence 1 − K ≥ (1−e⁻¹)·min(−Δ/(4β), 1) on each factor, with −Δ the Laplacian of the unit S³ (eigenvalue 4j(j+1)).
- The Bessel-ratio bound is not attempted in Lean (no Mathlib Bessel-I theory available to me). Only the scalar steps F1–F5 are in Lean.

**S6. Ground-state representation for the transfer kernel (PROVED).** For any symmetric kernel P ≥ 0, any φ > 0 and g = φh:
  ⟨g,(1−P)g⟩ = ∫(1 − Pφ/φ)|g|² + ½∫∫ P(x,y)φ(x)φ(y)(h(x)−h(y))².
  Hence ν0 ≥ inf_U [1 − (Kφ)(U)/φ(U) + V(U)] for every positive, gauge-invariant, center-even φ. The zero-point bound therefore reduces to one pointwise inequality (M0).

**S7. Jacobi bound for the continuum fibre (PROVED+LEAN for the minimisation, F4).**
- On S³ in Hopf coordinates (ρ = sin χ), with φ = e^{−√λ sin²χ}:
  (−Δφ)/φ + 4λ sin²χ = 4√λ − 8√λu + 4λu², where u = sin²χ;
  this is ≥ 4√λ − 4.
- So −Δ + 4λρ² ≥ 4(√λ − 1) on L²(S³). This is the fibre form of Simon's −∂² + x²y² ≥ |y|.
- It is stated for the Laplacian. Transferring it to 1 − K needs M0 or a Laplacian comparison, and S5 gives that comparison only with a cap at 1.

## 2. What remains: the exact missing inequalities

**M0 (MISSING): zero-point bound, the first rung.** There exist β0, c > 0 and, for each β ≥ β0, a positive gauge-invariant, center-even φ_β on SU(2)² such that
  1 − (Kφ_β)(U)/φ_β(U) + 2β sin²θ1 sin²θ2 sin²φ ≥ c β^{−1/3} for all U.
- Via S6 and S2 this gives −ln λ0 ≥ c' β^{−1/3}.
- Natural trial function: φ_β = exp(−a β^{2/3}·|Y|²-type function along the valley), times a transverse Gaussian of width (β·sin²θ1)^{−1/4}. Then Kφ/φ must be computed with remainder, using the explicit kernel k.
- This would be the first weak-coupling statement in which SU(2) and U(1) differ with a sign. For U(1), −ln λ0 = 0 exactly. **But it is a bound on the vacuum energy, not on the gap.**

**M1 (MISSING): the gap.** On the center-even gauge-invariant sector, μ1 − μ0 ≥ c β^{−p}, where μ_k are the min-max values of Q in S1. Proving it needs either of the following.
- (a) Two-sided semiclassics of Q with relative error o(1) at the scale β^{−1/3}: an Agmon localization to within β^{−1/3+δ} of the valley, plus norm-resolvent convergence to the matrix Hamiltonian along the whole valley. These are the RUNG chain's steps 2 and 4, unchanged.
- (b) A Poincaré inequality for the Markov kernel P(U,dW) = T(U,W)ψ0(W)/(λ0ψ0(U)), for example a Doeblin minorization T^n(U,W) ≥ ε λ0^n ψ0(U)ψ0(W) with n ≈ β^{p}. That needs pointwise bounds on the unknown ψ0.
- Neither (a) nor (b) is supplied. Nothing in S1–S7 controls a second eigenvalue: S6 and the Jacobi/Schur-type bounds act only on the bottom of the spectrum.

**Honest status.**
- T4 (m_e β → ∞) is not proved.
- I see no soft route to it. Every route I found needs either μ1 > μ0 at relative precision o(1) on the scale β^{−1/3}, or mixing-time control of the ground-state Markov chain.

## 3. U(1) discriminator

- For U(1) on the same lattice, V ≡ 0, so W = 0 and Q = ⟨g,(1−K)g⟩/‖g‖². S1–S5 then give exactly the free gaps −ln κ, which are ≈ 2/β in the Z₂-even U(1) sector (−ln(I_2/I_0)).
- None of the proved steps can yield more than c/β.
- The commutator enters only through V = 2β sin²θ1 sin²θ2 sin²φ: in S3, and through it in M0 and M1. Concretely, it enters in the term 2β sin²θ1·ρ², whose fibre ground energy grows like |sin θ1| (S7).
- The same discriminator inside SU(2): with V switched off, my program reproduces the free SU(2) gap −ln(I_3/I_1) ≈ 4/β exactly (P3).

## 4. Center-odd sector

- K and V commute with each center flip, so T splits into the 2^k flip sectors.
- On SU(2)² the zero set of V connects the four center points (±1, ±1). For example, U1 = exp(iθσ3), U2 = 1 has V = 0 along the whole path from (1,1) to (−1,1). So V puts no barrier between the center copies.
- The suppression comes from the effective valley potential ≈ |sin θ1| (the transverse zero-point energy, S7) against the kinetic scale 1/β. A WKB estimate along the valley gives an action ∫√(β|a|) da ∼ √β, hence an odd–even splitting of about exp(−c√β) (CLAIMED; semiclassical, not proved).
- So the center-odd gap is beyond every power of β^{−1}. A power-law lower bound must exclude it, which is why the statement is restricted to center-even functions; the restriction is not removable. Center-odd states were not computed (they are the half-integer-j sectors of my basis).

## 5. Numerical check on the two-direction model (prog/su2x2.py; predicates fixed in the docstring first)

**Method.**
- Exact Galerkin compression of K^{1/2}e^{−V}K^{1/2}, which has the same nonzero spectrum as T, to spins j1, j2 ≤ jmax, center-even.
- 3-D reduced quadrature: trapezoid in θ1 and θ2, Gauss–Legendre in φ.
- Compression gives λ_k(trunc) ≤ λ_k(true) by Cauchy interlacing, so the gap is not bounded either way. Convergence was checked by comparing (jmax, n) = (5, 40) against (6, 48).

**Results** (jmax 6, n 48):

| β | λ0 | λ1 | m_e | m_e β^{1/3} | m_e β | free SU(2) gap −ln(I3/I1) | ν0 (Galerkin upper bound) |
|---|---|---|---|---|---|---|---|
| 2 | 0.36274 | 0.07053 | 1.6376 | 2.06 | 3.28 | 2.0118 | 0.761 |
| 4 | 0.26963 | 0.12569 | 0.7632 | 1.21 | 3.05 | 1.0731 | 0.883 |
| 8 | 0.26773 | 0.15988 | 0.5156 | 1.03 | 4.12 | 0.5270 | 0.875 |
| 16 | 0.31555 | 0.18362 | 0.5415 | 1.36 | 8.66 | 0.2574 | 0.811 |

**Reading.**
- At β = 16 the gap is already 2.1 times the free gap, and m_e·β grows: consistent with T4.
- At β ≤ 8 the potential lowers the gap below the free value (P5 failed there: my expectation was wrong at strong coupling).
- ν0 ≈ 0.8 is not yet small at β = 16, so the asymptotic regime starts only beyond β = 16.
- Larger β needs jmax ≳ β^{1/2}. Out of reach in this budget.

## 6. References

| Reference | Locator | How read |
|---|---|---|
| D. E. Amos, Math. Comp. 28 (1974) 239–251 | Ratio bounds, as stated in S5 | From memory, not read; supported numerically by child T74 |
| B. Simon, "Some quantum operators with discrete spectrum but classically continuous spectrum", Ann. Phys. 146 (1983) 209 | — | Not read; S7 does not rely on it |
| M. Lüscher, Commun. Math. Phys. 54 (1977) 283 | — | Not needed: positivity is proved directly in §0 |

No network was used in this run.

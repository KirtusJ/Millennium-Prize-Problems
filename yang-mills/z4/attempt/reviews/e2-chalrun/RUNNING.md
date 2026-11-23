**Summary.** PROVED here: the weak-coupling expansion g2(R,β) = g0² + c1(R;G) g0⁴ + O_R(g0⁶) of the Schrödinger-functional (SF) coupling. It holds at fixed box size R (β → ∞ first), for every compact connected G and R where the classical minimum is unique modulo symmetry and nondegenerate. Also PROVED: for compact U(1), 0 < c1(R;U(1)) ≤ 1/(2cos(π/(2R²))) for all R, so the coefficient stays bounded. CITED: uniqueness of the minimum for SU(2) at R ≥ 4 (LNWW Theorem 1), and the logarithmic growth of c1(R;SU(2)) beyond the computed R. COMPUTED (floating point, own program, agrees with LNWW Table 1 to 8 digits): c1(R;SU(2)) for R = 2..16, with c1(R) − c1(R/2) > 0 and close to 2b0 ln 2; c1(R;U(1)) → 1/4 with differences → 0. **This is perturbative at fixed box size and says nothing about fixed β as R grows.**

Worker d1-run (task T38) under Director Z4, 23 Nov 2026. Tags: PROVED / CITED (locator) / CLAIMED / MISSING / COMPUTED.

## 1. Definition

- **Lattice.** Sites x = (x0, x⃗), with x0 = 0..T (T = R, Dirichlet in time) and x⃗ ∈ Z_R^{d−1} periodic. Lattice spacing a = 1.
- **Dynamical links.** U(x,0) for x0 = 0..T−1, and U(x,k) for x0 = 1..T−1. The spatial links at x0 = 0 and x0 = T are fixed:
  W(k) = exp(i φ Q / R) and W′(k) = exp(i φ′ Q / R), with φ = −η and φ′ = −(π − η).
  The charge Q is σ3 for SU(2) and 1 for U(1).
  This is the LNWW SU(2) choice: hep-lat/9207009, eq. (5.10); the full text was read.
- **Action and coupling.** Wilson action S = Σ_p (1 − (1/N) Re tr U_p), summed over plaquettes with at least one dynamical link, with N = 2 or 1.
  The bare coupling is β = 4/g0² for SU(2) and β = 1/g0² for U(1). Both give (1/2g0²) Σ f_a² at quadratic order in an orthonormal basis of the Lie algebra (T_a = iσ_a/2 with ⟨X,Y⟩ = −2 tr XY; T = i for U(1)).
- **Free energy.** Z(η) = ∫ e^{−βS} ∏ dU_Haar and Γ = −log Z.
- **Coupling.** Let k := g0² β dS0/dη, where S0(η) is the minimum of the action. Define
  **1/g2(R,β) := Γ′(η)/k at η = π/4.**
  In closed form k = −2c (d−1) R^{d−2} sin((π−2η)/R²), with c = 4 (SU(2)) or 1 (U(1)); k is negative.
- **Required properties.**
  - (i) g2 is gauge invariant: Γ is.
  - (ii) It is defined for every compact connected G with a U(1) subgroup to carry the boundary field.
  - (iii) g2 = g0² at leading order (Theorem 1).
  - This is LNWW's coupling, eq. (2.43) as cited in their sect. 5.3. The identity c1 = m1 is checked numerically in §4.

## 2. Hypotheses and lemmas

- **Lemma 0 (critical point). PROVED + COMPUTED.** V(x,0) = 1 and V(x,k) = exp(i φ(x0) Q/R), with φ linear from φ to φ′.
  - V has the boundary values.
  - Its spatial plaquettes are 1.
  - All timelike plaquettes equal exp(−i(π−2η)Q/R²).
  - Hence S0 = (d−1) R^{d−1} T (1 − cos((π−2η)/R²)).
  - ∇S(V) = 0 is computed to below 2·10⁻¹⁶ (predicate P1). It is also LNWW's statement after eq. (5.6).
- **Hypothesis U (uniqueness).** S[U] ≥ S[V], with equality only on the orbit of V under the symmetry group 𝒢.
  - 𝒢 consists of gauge transformations Ω with Ω = 1 at x0 = 0, arbitrary at 1 ≤ x0 ≤ T−1, and at x0 = T a constant element of the centraliser of W′. That centraliser is the maximal torus exp(itσ3), resp. U(1).
  - The constant boundary transformation at x0 = T is an exact symmetry: it fixes W′ and right-multiplies the last time links. It must be included. Without it H has one extra zero mode at p = 0 (the time-like line of Q-charge). LNWW do not discuss zero modes (sect. 3.3).
  - **SU(2): CITED.** LNWW hep-lat/9207009, sect. 5.2, Theorem 1 (fundamental domain eq. (5.8), technical condition eq. (5.9)). For the SU(2) family (5.10) the premises hold when 0 < η < π and L/a ≥ 4 (eq. (5.11)). The proof is in their appendix B, which I did not read. **R = 2, 3 lie outside the cited theorem**, and for them only local strict minimality is computed.
  - **U(1): CLAIMED.** Only local strict minimality is COMPUTED (Lemma N). The global statement is not proved here. LNWW's theorem is stated for SU(N), and I did not check whether it covers N = 1.
- **Lemma F (freeness). PROVED.** If Ω ∈ 𝒢 fixes V, then:
  - Ω(1) = Ω(0)V(0,0) = 1 along the time links leaving x0 = 0.
  - Inductively Ω(x0) = 1 for every x0 ≤ T−1, and then Ω(T) = 1.
  - So 𝒢 acts freely at V, and by continuity freely near the orbit. The global constant torus element that also acts at x0 = 0 stabilises V; that is why it is quotiented out by setting Ω(0) = 1.
- **Lemma N (nondegeneracy). COMPUTED for each listed R, not proved for all R.**
  - Let H be the Hessian of S at V in the coordinates U = e^X V. These are normal coordinates of the bi-invariant metric centred at V; the Haar density is 1 + O(|X|²).
  - Let D be the orbit map ω ↦ X(x,μ) = ω(x) − Ad_{V(x,μ)} ω(x+μ̂). Gauge invariance gives HD = 0 (computed, ≤ 3·10⁻¹⁵).
  - If H + DD† > 0, then ker H = range D, i.e. the Hessian is nondegenerate on the normal slice.
  - Spatial translation invariance makes H and D block diagonal in the spatial momentum p (exact Fourier decomposition). The program checks min eig(H(p) + D(p)D(p)†) > 0 for every p.
  - The minimum eigenvalue over all p is 0.120 (R=4), 0.0341 (R=8), 0.00906 (R=16); it is the same for SU(2) and U(1).
  - Rigour: LAPACK's symmetric eigensolver is backward stable, so the error is about n·ε·‖A‖ ≲ 10⁻¹². That is far below the margins. This is floating point with an a priori error bound, not interval arithmetic.
- **Laplace's method with parameters. CITED (standard).**
  - Reference: Hörmander, *The Analysis of Linear Partial Differential Operators I*, Thm 7.7.5 (stationary phase / Laplace with smooth parameter dependence). Read from memory, not reopened in this session.
  - The Morse–Bott reduction over a free compact orbit uses a slice. It is standard and written out below. I read no source for it in this session.

## 3. Theorem 1 (PROVED, given Hypothesis U and Lemma N at the given R; both hold for SU(2), R ∈ {4,…,16} by citation + computation)

Fix G ∈ {SU(2), U(1)}, d, R, and η in a compact interval J around π/4 on which U and N hold. As β → ∞:

  Γ(η) = β S0(η) + Γ1(η) + log C_β + r(β,η), with sup_J |∂_η r| ≤ C(R) β⁻¹,
  Γ1(η) = ½ log det(H_η + D_η D_η†) − log det(D_η† D_η).

Here C_β is independent of η. Consequently

  **g2(R,β) = g0² + c1(R;G) g0⁴ + O(C′(R) g0⁶), with c1 = −Γ1′(π/4)/k.**

The momentum decomposition gives

  c1 = −(1/k) d/dη Σ_p [½ log det(H(p)+D(p)D(p)†) − log det(D(p)†D(p))].

This is a finite sum of finite-dimensional determinants: the gauge-fixed (Feynman, background) fluctuation operator and the Faddeev–Popov operator D†D (a covariant Laplacian with Dirichlet conditions), with the extra boundary torus generator at p = 0. The Haar-measure Jacobian 1 + O(X²) and the cubic and quartic terms of the action enter only through r, i.e. at order g0⁶ in g2.

**Proof.**
1. **Localisation.** By Hypothesis U, compactness of the configuration space, and continuity of S in (U,η): for each neighbourhood 𝒩 of the critical orbit 𝒪_η there is δ > 0 with S ≥ S0(η) + δ off 𝒩, uniformly for η ∈ J. Since V_η depends smoothly on η, 𝒩 can be taken as a smoothly moving tube. Hence the contribution from outside 𝒩 is O(e^{−βδ}) relative to the rest, together with its η-derivative. The derivative brings down β ∂_ηS, which is bounded, so the factor β e^{−βδ} is still negligible.
2. **Slice (PROVED).** By Lemma F the map 𝒢 × B → 𝒩, (Ω, ξ) ↦ Ω·exp(ξ)V is a diffeomorphism for a small ball B in N_V := (range D)^⊥. Here 𝒢 is a compact Lie group of dimension m. The Haar product measure pulls back to dΩ · J(ξ) dξ, with J smooth and J(0) = det(D†D)^{1/2} relative to the metric-normalised Haar measure on 𝒢. This holds because the differential at (1,0) is (D, ι_N), and the Riemannian volume of the frame (range D) ⊕ N_V is det(D†D)^{1/2}. S is 𝒢-invariant, so Z_𝒩 = vol(𝒢) ∫_B e^{−βS(e^ξ V)} J(ξ) dξ.
3. **Laplace (CITED).** On B the phase f(ξ) = S(e^ξV) − S0 has a nondegenerate minimum at 0 with Hessian H|_N (Lemma N), and the amplitude J is smooth. Hörmander Thm 7.7.5 (applied with real phase) gives
   ∫ e^{−βf} J = (2π/β)^{(n−m)/2} det(H|_N)^{−1/2} J(0) (1 + a1(η)β⁻¹ + R2),
   with |R2| ≤ C(R) β⁻². The constants are uniform and smooth in η ∈ J because all data depend smoothly on η.
   C(R) depends on the dimension n − m ~ R^d, on the smallest eigenvalue of H|_N (~R⁻²), and on C³ bounds. **No uniformity in R is claimed.**
4. **Determinant identity (PROVED).** H D = 0 and H is symmetric, so range H ⊥ range D. Then H + DD† = H|_N ⊕ (DD†)|_{range D}, and hence det(H + DD†) = det(H|_N) det(D†D). Inserting this into step 3:
   −log Z = βS0 + ½ log det H|_N − ½ log det(D†D) + (η-independent) + O(β⁻¹)
          = βS0 + ½ log det(H+DD†) − log det(D†D) + const + O(β⁻¹).
   This is LNWW's form ½ ln det Δ1 − ln det Δ0 (their eqs. (3.20), (6.22)).
5. **Differentiability.** Apply step 3 also to ∂_η Z = −β ∫ ∂_ηS e^{−βS}, whose amplitude is ∂_ηS · J. The two asymptotic expansions of the same smooth function of η agree term by term. So Γ′ = βS0′ + Γ1′ + O(C(R)β⁻¹).
6. **Coupling.** Γ′/k = 1/g0² + Γ1′/k + O(g0²). Invert: g2 = g0² − (Γ1′/k) g0⁴ + O(g0⁶). ∎

**Finite group (the expansion does not exist; PROVED).** A continuous family of group elements in a finite group is constant, so W cannot depend on η: g2 is not even defined. Even with a fixed boundary, Z is a finite sum. Then Γ = β S_min − log #(minimisers) + O(e^{−βΔ}), with no power series in 1/β. The proof fails at step 2/3: there is no tangent space and no Gaussian integral.

**Periodic torus (why not used; PROVED + CITED).** On a periodic box, every constant diagonal configuration U(x,μ) = exp(iθ_μ σ3) has zero action. Configurations with different θ have different Polyakov-loop traces 2cos(Rθ_μ), so they are not gauge equivalent. The minimum set is therefore a positive-dimensional manifold of gauge-inequivalent flat fields ("torons"), and Hypothesis U fails. Laplace's method in its nondegenerate form does not apply, and the zero modes need a separate non-Gaussian treatment. The name and references are from LNWW sect. 5.1 (p. 30): refs. [59] Gonzalez-Arroyo, Jurkiewicz, Korthals-Altes (Freiburg lectures 1981) and [60] Lüscher, Nucl. Phys. B219 (1983) 233. I did not read either reference; the citation is secondhand.

## 4. Theorem 2: U(1) carries no running (PROVED)

For compact U(1) with the action above, the orbit map D does not depend on η: Ad is trivial. The η-dependence of H comes only through the timelike plaquettes:

  H_η = cos θ · H_t + H_s, with θ = (π−2η)/R².

Here H_t and H_s are the (η-independent) Maxwell forms of the timelike and spatial plaquettes. Hence Γ1′ = ½ tr[A⁻¹ ∂_ηH], with A = H + DD† and ∂_ηH = −sin θ · θ′ H_t, and

  **c1(R;U(1)) = tr[A⁻¹ H_t] / (2 N_t),** with N_t = (d−1) R^{d−1} T timelike plaquettes.

Bounds:
- **Lower bound.** A > 0 and H_t ≥ 0, so tr[A⁻¹ H_t] > 0 (H_t ≠ 0).
- **Upper bound.** H_t ≤ H / cos θ, so tr[A⁻¹H_t] ≤ tr[A⁻¹H]/cos θ = rank H / cos θ = (n−m)/cos θ, because A⁻¹H is the projection onto range H.
- In d = 4: n − m = R³(3(T−1)+1) − 1. Therefore

  **0 < c1(R;U(1)) ≤ (n−m)/(2 N_t cos θ) < 1/(2 cos(π/(2R²))) for every R.**

So c1(R;U(1)) is bounded uniformly in R: there is no log R term. A bulk counting gives tr ≈ (2/d) N_t, i.e. c1 → 1/d = 1/4. That is the familiar tadpole renormalisation of the compact Wilson action, and the numbers below confirm it: CLAIMED limit, COMPUTED values.

For **non-compact** U(1), H does not depend on η at all and **c1 ≡ 0 exactly**.

## 5. Computed table (COMPUTED; d = 4, η = π/4; program `c1sf.py`, file `results/*.txt`, checks in `results/analysis.txt`)

See `results/analysis.txt` for the full table. All rows satisfy P1–P4: gradient ≤ 2·10⁻¹⁶, |HD| ≤ 3·10⁻¹⁵, Hermiticity, positivity. The derivative in η is a central difference (h = 10⁻³ and 5·10⁻⁴, Richardson); the error is ~10⁻⁸.

| R | c1(R;SU(2)) | c1(R;U(1)) | LNWW m1(R) | Δ_SU2(R)=c1(R)−c1(R/2) | Δ_U1(R) |
|---|---|---|---|---|---|
| 2 | 0.226403 | 0.228751 | – | – | – |
| 3 | 0.281797 | 0.229316 | – | – | – |
| 4 | 0.313012 | 0.233057 | – | 0.086609 | 0.004305 |
| 5 | 0.335656 | 0.236059 | – | – | – |
| 6 | 0.35422030 | 0.238253 | 0.35422030 | 0.072424 | 0.008937 |
| 8 | 0.38370429 | 0.241119 | 0.38370429 | 0.070692 | 0.008062 |
| 10 | 0.40644167 | 0.242876 | 0.40644167 | 0.070786 | 0.006817 |
| 12 | 0.42483107 | 0.244057 | 0.42483107 | 0.070611 | 0.005804 |
| 16 | 0.45347745 | 0.245539 | 0.45347745 | 0.069773 | 0.004420 |

Further rows and fits:
- 2b0 ln 2 = 0.064378. The ratios Δ_SU2/(2b0 ln 2) are 1.098, 1.100, 1.097 and 1.084 at R = 8, 10, 12, 16; the excess is the O(a/L) artefact (r1/L) of the unimproved c_t = 1 action.
- Fit of c1(R;SU(2)) to A ln R + B + C/R + E/R² on R = 4..16 gives A/(2b0) = 1.004.
- With A = 2b0 fixed, the fit gives B = 0.2028 and C = −0.121, against LNWW r0 = 0.202349(3) and r1 = −0.1084(11).
- U(1) rises towards 1/4 and stays below the proved bound 1/(2cos θ) ≈ 0.5.
- R = 2, 3: the stability theorem is not cited for these sizes (LNWW require L/a ≥ 4); only local minimality is computed.

**d = 3, SU(2)** (same formula, 2 spatial directions, COMPUTED): c1 = 0.6667, 0.9530, 1.2356, 1.7963, 2.3541, 3.4662 at R = 4, 6, 8, 12, 16, 24. c1/R = 0.1667 → 0.1444 and settles, so c1 grows linearly in R, as power counting R^{4−d} predicts (the coupling is dimensionful in d = 3).

**Comparison with LNWW Table 1** (hep-lat/9207009, p. 46, "One-loop coefficient m1(L) and remainder ε(L) at η = π/4"; full text read):
- m1(6) = 0.35422030, m1(8) = 0.38370429, m1(10) = 0.40644167, m1(12) = 0.42483107, m1(16) = 0.45347745.
- My c1 agrees in every printed digit at every listed R (R = 4 is not in their table).
- Their asymptotics (eqs. (7.37)–(7.41)): m1(L) ~ Σ_n (r_n + s_n ln L)/L^n, with s0 = 11/(12π²) = 2b0 for b0 = 11/(24π²), s1 = 0, r0 = 0.202349(3), r1 = −0.1084(11). They confirmed s0 numerically to four decimals.

**Independent route (child T40, dense full-lattice matrices, finite-difference Hessian, no Fourier decomposition):**
- c1(4) = 0.312997, with a Richardson error estimate of about 1.2·10⁻⁵. Mine is 0.313012, so the difference is 1.5·10⁻⁵, consistent.
- I reran the child's program under my register (`child-rerun-R4`) and it reproduced.
- R = 6 was not done by the child.

**Rigour of the table.**
- These are IEEE double evaluations of exact finite-dimensional formulas.
- Determinants use LU (slogdet), with condition numbers ≲ 10³ and an error of about 10⁻¹² per log det.
- The η-derivative is a finite difference with a measured h-dependence below 10⁻⁵ (A2).
- This is not interval arithmetic, and not a computer-assisted proof. The margins are large: Δ(R) ≈ 0.07 against errors of 10⁻⁵.

## 6. The signed statement (Theorem 1 + Theorem 2 + table)

For each R ∈ {4, 6, 8, 12, 16} with R/2 also computed:
- c1(R;SU(2)) − c1(R/2;SU(2)) > 0 (COMPUTED, floating point, margin about 10⁴ times the error), with values close to 2b0 ln 2 = 0.0644.
- c1(R;U(1)) − c1(R/2;U(1)) is small and decreasing (COMPUTED). For all R, c1(R;U(1)) ∈ (0, 0.5] (PROVED), so no logarithmic growth is possible.

Beyond the listed R, the growth 2b0 ln R is CITED (LNWW eq. (7.37)–(7.39), numerical extrapolation to L = 32, not a proof). **MISSING:** a proof of monotonicity or log-growth of c1(R;SU(2)) for all R (an asymptotic analysis of the lattice determinant). It is not attempted here.

Where the sign comes from: in the SU(2) σ3 background, the neutral component behaves like U(1) (bounded, → 1/4 as in Theorem 2). The charged components (T±) see the background through Ad_V in both H and D†D. Their η-response grows like log R, which is the b0 term: (11/3)N, with the −1/3 from the ghost and the "paramagnetic" +4 from the spin coupling. That decomposition is CLAIMED (textbook); here it is only the computed total.

## 7. Discriminators

| case | outcome |
|---|---|
| U(1) compact | c1 bounded for all R (Thm 2, PROVED); differences → 0 (COMPUTED) |
| U(1) non-compact | c1 ≡ 0 (PROVED) |
| finite group | no expansion: no tangent space, and g2 is undefined since η cannot vary (PROVED, §3) |
| SU(2), d = 3 | c1 grows ~linearly in R (power counting R^{4−d}); COMPUTED in table D3 |
| SU(2), d = 5 | not computed (time). Power counting gives bounded c1 + O(R⁻¹): NOT CHECKED |

## 8. What this gives the attempt, and what it does not

- **Order of limits.** Theorem 1 is lim_{β→∞} at fixed R. The remainder constant C′(R) is not controlled in R. Through the proof it grows at least with the number of degrees of freedom and with 1/λ_min(H|_N) ~ R², so **nothing follows at fixed β as R → ∞**. The statement "g2 runs" is proved only as a statement about the first Taylor coefficient in g0² at each fixed R.
- **What would be needed.** To conclude "g2(R,β) increases with R for R up to exp(cβ)", one would need:
  - |g2 − g0² − c1 g0⁴| ≤ K g0⁶ (1 + log R)² uniformly for R ≤ e^{cβ}, i.e. renormalised perturbation theory with remainders uniform in a/L, including the large-field region;
  - and then c1(2R) − c1(R) ≥ 2b0 ln 2 − O(1/R), which is itself still MISSING as a theorem for all R.
- **Known techniques.** Balaban's renormalisation-group programme (Commun. Math. Phys. 1984–89, "ultraviolet stability" of 4D lattice Yang–Mills in a finite periodic box of fixed physical size) controls effective actions with effective couplings following the perturbative flow, with bounds uniform in the number of RG steps.
  - That is CLAIMED from memory: not read in this session, and no locator.
  - As far as I know it is stated for the torus (toron issues are handled in its small/large-field split), and not for this SF observable.
  - It gives bounds on the partition function and effective action, not an asymptotic statement about Γ′(η) with an explicit c1.
  - Transferring it to "g2(R,β) increases for R ≤ e^{cβ}" is an open task, not a known theorem: MISSING.
- **Relation to the gap.** None. Asymptotic freedom here is a statement at β = ∞ first; the mass gap concerns R → ∞ at fixed β. The ledgers' obstruction ("asymptotic freedom used non-perturbatively") is untouched. What is new is only that the group enters c1 with a definite sign and log growth for SU(2), and boundedly for U(1).

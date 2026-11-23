**Proved range: β_W < 1/12, the same as published. Published range for the mass gap: β_W < 1/12 (Shen–Zhu–Zhu). Published range for the area law: β_W < 1/6 (Cao–Nissim–Sheffield 2025). The published ranges are larger or equal. The horizontal criterion adds nothing at the worst configuration. No pointwise (horizontal) Bakry–Émery argument can go past β_W = 1/8.**

# f1-strong (T63): an explicit lower bound on the gap at strong coupling, SU(2), d = 4

Conventions: V = −(β/2) Σ_p Re Tr Q_p, Q_p = U1U2U3⁻¹U4⁻¹. The metric is ⟨X,Y⟩ = −Tr XY, with e_a = iσ_a/√2. Variations are U_e → e^{s t_e}U_e. Ric = 1. Throughout, β means β_W.
Conversion (PROVED, arithmetic): SZZ use the weight exp(Nβ_SZZ Re Σ Tr Q_p). For SU(2) this is exp(2β_SZZ Re Tr), and ours is exp((β_W/2) Re Tr), so **β_W = 4β_SZZ**. For SU(N), with Wilson weight exp((β_W/N) Re Tr), the relation is β_W = N²β_SZZ.

## 1. Literature (sources read; fetched text is kept outside this directory)

| paper | how read | statement | range, their normalization | range in β_W (SU(2), d=4) | what is proved |
|---|---|---|---|---|---|
| Shen, Zhu, Zhu, "A stochastic analysis approach to lattice Yang–Mills at strong coupling", arXiv:2204.12737v1 (2022), CMP 2023 | full PDF via pdftotext: Ass. 1.1 (1.3), Lemma 4.1 (4.2), Thm 1.2, Thm 1.4, Cor 1.6 | K_S = (N+2)/4·2 − 1 − 8N\|β\|(d−1) > 0 for SU(N). (4.2) is \|Hess S(v,v)\| ≤ 8(d−1)N\|β\|\|v\|² on **all** tangent vectors v. The Bakry–Émery condition is imposed on the whole of T(SU(N)^E); I found no restriction to gauge-invariant observables in the curvature condition. | \|β\| < 1/(16(d−1)) = 1/48 | **β_W < 1/12** | Uniqueness of the infinite-volume measure (Thm 1.2); LSI with constant 2/K_S and Poincaré for cylinder functions (Thm 1.4); exponential decay of covariances of cylinder functions with disjoint supports (Cor 1.6, "mass gap"), with rate c_N depending on K_S, N, d and c1 depending on the support sizes. I saw no transfer-matrix statement. |
| Cao, Nissim, Sheffield, "Dynamical approach to area law for lattice Yang–Mills", arXiv:2509.04688v2 (2025) | full PDF via pdftotext: Def 1.4, Rem 1.5, Thm 1.6, Prop 3.2 | Bakry–Émery is applied to an auxiliary **vertex** σ-model, with a uniform mass gap in all fields A, B (Prop 3.2). Area law then follows via Durhuus–Fröhlich [DF80]. Rem 1.5 says the SZZ threshold is half of theirs. | β < β*_SU(N) = 1/(8(d−1)) = 1/24 | **β_W < 1/6** | **Area law** for U(N), SU(N), SO(2(N−1)), d ≥ 2 (Thm 1.6). It does **not** state an LSI or a mass gap for lattice YM itself; I read only the intro and §2–3 headers. |
| Cao, Nissim, Sheffield, "Expanded regimes of area law for lattice Yang–Mills theories", arXiv:2505.16585 (v3, 2025) | abstract only | Master loop equation treated as a linear inhomogeneous equation, with an a-priori bound; improves Osterwalder–Seiler, especially for large N | not read | NOT CHECKED | area law, U(N) |
| Nissim, arXiv:2510.22788 (2025) | abstract only | Mass gap and unique infinite-volume limit for U(N) in the 't Hooft regime, by random-environment reduction to SU(N) plus cluster expansion. Notes that Bakry–Émery fails for U(N). | not read | NOT CHECKED | mass gap, U(N) |
| Osterwalder–Seiler 1978 | not read | cluster expansion | not explicit | — | mass gap, area law (CITED via LIT_RIGOROUS) |

Where 8(d−1) comes from (CITED, SZZ Lemma 4.1, eq. (4.2)): it bounds \|Hess S\| on every tangent vector, plaquette by plaquette with Hölder. Each link lies in 2(d−1) plaquettes. Our computation in §2 reproduces the constant exactly as (per-plaquette maximum 4) × (β/2) × 2(d−1) = 12β_W.

## 2. The Hessian (PROVED)

**H1 (exact formula).** Move all exponentials to the left: Q_p(s) = e^{sX1}e^{sX2}e^{sX3}e^{sX4}Q_p, where X1 = t1, X2 = Ad(U1)t2, X3 = −Ad(U1U2U3⁻¹)t3 and X4 = −Ad(U1U2U3⁻¹U4⁻¹)t4 = −Ad(Q_p)t4. Let Y = ΣX_i and C = Σ_{i<j}[X_i,X_j]. Then
  d²/ds² V_p = −(β/2) Re Tr[(ΣX_i² + 2Σ_{i<j}X_iX_j)Q] = −(β/2) Re Tr[(Y² + C)Q].
For SU(2), Y² = −½\|Y\|²·1. Write A = (Q − Q†)/2 ∈ su(2), with Re Tr Q = 2cos θ and \|A\| = √2 sin θ. Then
  **Hess V_p(t,t) = (β/2)[cos θ_p \|Y_p\|² + ⟨C_p, A_p⟩]**, which is (β/4)\|Y\|² Re Tr Q plus the commutator term.
The curves s ↦ e^{st}U are geodesics of the bi-invariant metric, so this is the Riemannian Hessian. COMPUTED check: P1, finite differences, relative error 9.7e-6 ≤ 1e-5.

**H2 (exact per-plaquette constant).** Decompose X_i = z_i a + w_i, where a = A/\|A\| and w_i ⊥ a, identified with ℂ. Using \|[X,Y]\| = √2\|X×Y\|, the bracket in H1 becomes
  −cos θ(Σz_i)² + w*M(θ)w, with M = −cos θ J ± sin θ K,
where J is the all-ones matrix, K_jk = −i·sgn(k−j), and the sign depends on orientation. Then 4I − M = N(θ) + (3 + cos θ)I with N_jk = e^{iθ sgn(k−j)} and N_jj = 1. Take the ansatz v_j = z^j. It is an eigenvector iff z⁴ = e^{−2iθ}. The four roots give the full spectrum of N: {4cos²(θ/4), 4sin²(θ/4), +2sin(θ/2), −2sin(θ/2)}. Therefore
  λ_max(M) = 2s(1+s), with s = sin(θ/2).
The z-part is ≤ 4max(−cos θ, 0) = 4(2s²−1)₊ ≤ 2s(1+s), because (3s+2)(1−s) ≥ 0. Hence
  **−Hess V_p(t,t) ≤ (β/2) h(θ_p) Σ_{e∈p}\|t_e\|², with h(θ) = 2s(1+s) ≤ 4.** Equality h = 4 holds iff Q_p = −1, and h is sharp for every θ.
COMPUTED check: P2, \|λ_max − h(θ)\| ≤ 4.9e-15 on 200 random plaquettes.

**H3 (all directions).** Sum H2 over plaquettes; each link lies in 2(d−1) = 6 plaquettes. This gives
  Hess V(t,t) ≥ −(β/2) max_e Σ_{p∋e} h(θ_p) · \|t\|² ≥ **−12β\|t\|²**.
This is SZZ's constant, recovered with a configuration-dependent refinement. The worst local situation is a link whose 6 plaquettes are all −1.

**H4 (the truth is ≥ 8; PROVED).** Take the π-flux configuration: U_μ(x) = (−1)^{x_1+…+x_{μ−1}}·1, so Q_p = −1 for every p. It exists on Z⁴ and on every even periodic torus. Since Ad(−1) = id, the transports are trivial and C = 0, A = 0. So Hess V(t,t) = −(β/2)Σ_p\|curl t\|², with the flat curl tensored with su(2). In Fourier, Σ_p\|curl t\|² = Σ_k(\|k̂\|²\|t̂\|² − \|k̂·t̂\|²) with \|k̂\|² = Σ4sin²(k_μ/2) ≤ 16. The bound is attained at k = (π,π,π,π) by transverse t̂. Hence **λ_min = −8β**.
COMPUTED check: P3, −8.000000000000 on L = 2 and L = 4.

**H5 (horizontal gives nothing at the worst known configuration; PROVED).** Each plaquette term of V is critical at Q = ±1, since dV_p ∝ A_p = 0. So the π-flux configuration is a critical point. V is constant on its gauge orbit, which therefore consists of critical points, so Hess V(ω, ·) = 0 for every gauge direction ω. The eigenvectors with negative eigenvalues are therefore orthogonal to the orbit, and κ_H(π-flux) = 1 − 8β.
COMPUTED check: horizontal minimum −8.000000000000005 on L = 2.
The same argument applies at every center-valued (Z₂) configuration, including "one link −1". There κ_H equals the full minimum: −4.676 on L = 2 and −4.314 on L = 3 (M1, measured only). This agrees with the route's 4.31.

**Consequence.** Over all configurations, sup c(U) := sup −λ_min(Hess V)/β lies in [8, 12]. 8 is attained, and 12 is proved (H3). The horizontal restriction does not lower the supremum below 8 (H5).
- **(a) all t:** c = 12 PROVED. The truth is ≥ 8 (PROVED); the best found numerically is 8.000.
- **(b) horizontal t:** c_H = 12 PROVED, with the same proof; I have no better proof. The truth is ≥ 8 (PROVED by H5).
MISSING: a proof of any c < 12. Per-plaquette arguments cannot give one, because H2 is sharp per plaquette. One would need a global bound on the covariant curl, ‖curl_U‖² ≤ 16 + (correction in 1 − Ad Q_p), together with the commutator term. I did not prove one.

## 3. Theorem (PROVED modulo CITED Bakry–Émery)

For SU(2), d = 4 and β_W < β_1 := 1/12, in any finite box with any boundary condition (or on a torus), Ric + Hess V ≥ 1 − 12β_W > 0 on all directions. By Bakry–Émery (CITED: SZZ Thm 1.4, Cor 4.4/4.5 and the proof of (4.7)), μ satisfies LSI with constant 2/(1 − 12β_W) and Poincaré with constant 1/(1 − 12β_W). This holds for all functions, not only gauge-invariant ones, uniformly in volume and boundary condition.

Decay of correlations: CITED from SZZ Cor 1.6 (via Cor 4.11 and Lemma 4.9). It needs Ass. 1.1, which is exactly this range, for cylinder functions with disjoint supports. A transfer-matrix gap would follow by the spectral argument of CURVATURE_ROUTE S10 (CLAIMED there; not re-checked here). It also needs the decay rate to be uniform in the supports, which Cor 1.6 does not give explicitly (c1 depends on \|Λ_f\|, \|Λ_g\|).

**β_1 = 1/12 is not larger than the published value.** The horizontal restriction does not improve the worst case. The worst configuration found is π-flux, with κ_H = 1 − 8β. A link with all 6 plaquettes at −1 saturates the local bound, but the true λ_min there (one-link flip) is only −4.3 to −4.7. **Ceiling (PROVED by H4–H5): no pointwise Bakry–Émery criterion, full or horizontal, can give a range beyond β_W < 1/8.**

## 4. Numerical control (own program hess.py on L=2; child on L=2)
- Haar samples: max c = 4.54 (30 samples).
- Hill-climb from 6 Haar seeds: 5.48–5.93 after 300 steps each.
- From π-flux: stays at 8.000.
- No value above 8 was found, and none came near 12.
- The child's independent search is in report.md §5.

## 5. Honest comparison
- Mass gap: my range equals SZZ's, β_W < 1/12. That is not an improvement.
- Area law: CNS 2509.04688 has β_W < 1/6. This exceeds even the pointwise-BE ceiling of 1/8 that I proved, because CNS run Bakry–Émery on a vertex σ-model, not on the link measure.
- What the horizontal criterion adds here: nothing in the constant. What this work adds:
  - (i) the sharp per-plaquette constant h(θ) = 2 sin(θ/2)(1 + sin(θ/2)), which gives a configuration-dependent bound;
  - (ii) the proof that the method is capped at 1/8 for both the full and the horizontal criterion, so a gain of at most a factor 3/2 remains open, MISSING a global curl estimate.

## 6. Discriminators
- **U(1)** (Ric = 0): K = −c·β < 0 for every β > 0, so the criterion proves nothing. Correct as a discriminator. A strong-coupling gap for U(1) is nevertheless true (cluster expansion, Osterwalder–Seiler, CITED via LIT_RIGOROUS; not read by me). So curvature is not the only mechanism. CNS/Nissim's U(N) results also come from a different route.
- **SU(N)** (CITED from SZZ (1.3) plus the conversion above): β_SZZ < 1/(16(d−1)), so β_W < N²/(16(d−1)), with Ric = N/2. I did not redo H2 for N > 2; the identity Y² ∝ 1 is special to SU(2). NOT CHECKED.

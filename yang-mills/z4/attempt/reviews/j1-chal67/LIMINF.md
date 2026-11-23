PROVED here (K normalised, κ_0 = 1): for every k ≥ 0, liminf_{β→∞} β^{1/3} ν_k(β) ≥ E_k, where E_k is the k-th min-max value of h on rotation-invariant functions. Inputs: the Bessel-ratio bounds of Ruiz-Antolín–Segura Thm 2 (CITED, read), Rellich–Kondrachov and the min-max principle (standard, CITED), and L1–L4 of SCALING_LIMIT.md, which I rechecked and use in the forms restated below. L3 has a sign typo and L4 an arithmetic slip in a constant; neither changes the conclusion. The corollary liminf β^{1/3} m_e ≥ E_1 − E_0 is CONDITIONAL: it also needs the k = 0 upper bound of SCALING_LIMIT §2 (not rechecked here) and E_1 > E_0 (C2, cited there from memory).

# L6 and L7 in full: the lower half of the scaling limit (h1-liminf, T86)

Tags: **PROVED** (argument given here); **PROVED+LEAN** (scalar step in `lean/Liminf.lean`, lemma Gx, exit 0, axioms propext/Classical.choice/Quot.sound); **NUM** (`prog/scalars.py`, results/scalars_run1.json); **CITED** (locator, how read); **CLAIMED** / **MISSING**.
The director, the author of SCALING_LIMIT.md and I share a model family, so this is not independent review.

## 0. Notation (as in SCALING_LIMIT.md §0)
- G = SU(2), with normalised Haar measure dU. U = exp(iA·σ) = cos a + i sin a Â·σ, where a = |A| ∈ [0,π) is the geodesic distance to 1 on the unit S³.
- Peter–Weyl degree n = 2j. −Δ is the Laplacian of the unit S³, with eigenvalue n(n+2). On G², −Δ = −Δ_1 − Δ_2.
- K has eigenvalue κ_{n_1}κ_{n_2} on degree (n_1,n_2), where κ_n(β) = I_{n+1}(β)/I_1(β) = Π_{ν=1}^{n} r_ν(β) and r_ν = I_{ν+1}/I_ν.
- V = 2β sin²a_1 sin²a_2 sin²γ, where γ is the angle between the axes Â_1 and Â_2. Also V = 2β s_2²|x⃗_1 × n_2|², where x⃗_i = sin a_i Â_i, s_i = |sin a_i| and n_2 = Â_2.
- H = 1 − K + V. This is a bounded operator on L²(G²), so there are no domain questions at lattice level. S is the conjugation-invariant, center-even sector, and ν^H_k is the k-th min-max value of H on S.
- h = −½Δ + w on L²(R⁶) with w(Y) = 2|Y_1×Y_2|². It is the Friedrichs extension from C_c^∞, with form q_h and form domain Q(h).
  - L²_inv is the subspace of functions invariant under the diagonal action Y ↦ (OY_1, OY_2), O ∈ SO(3).
  - E_k := inf_{F ⊂ Q(h)∩L²_inv, dim F = k+1} max_{ψ∈F∖0} q_h(ψ)/‖ψ‖².
  - These are the eigenvalues of h|inv when h has compact resolvent (SCALING_LIMIT C1). Nothing below uses C1.
- Rescaling: Y = β^{1/3}A. For f on G² supported in the chart, the rescaled function is 𝓡f(Y) := (2π²)^{−1}β^{−1} f(U(β^{−1/3}Y)).
- J(Y) := Π_i (sin a_i/a_i)². By §3 below, ‖f‖²_{L²(G²)} = ∫|𝓡f|² J dY.

## 1. Scalar inputs

**B (Bessel ratios).** For integer ν ≥ 0 and x > 0:
 (A) r_ν(x) ≥ x/(ν+1+√((ν+1)²+x²)),  (B) r_ν(x) ≤ x/(ν+½+√((ν+½)²+x²)).
- CITED: D. Ruiz-Antolín, J. Segura, "A new type of sharp bounds for ratios of modified Bessel functions", arXiv:1606.02008 (2016; "to appear in J. Math. Anal. Appl."), **Theorem 2**: I_ν/I_{ν−1} < x/(ν−½+√((ν−½)²+x²)) for ν ≥ ½, and I_ν/I_{ν−1} > x/(ν+√(ν²+x²)) for ν ≥ 0.
- How read: a fetch sub-agent read the arXiv abstract page and the HTML v1 (first 40k of 73k characters, which includes Theorem 2 verbatim). I read its report, not the page. The fetched text is kept outside this directory.
- The substitution ν → ν+1 gives (A) for ν ≥ −1 and (B) for ν ≥ −½.
- The paper attributes the bounds to earlier works [8, 12]. That reference list was in the unread part, so the attribution is not confirmed. SCALING_LIMIT/TORON_GAP call (B) "Amos 1974", which I did not check.
- NUM Q1, Q2: 5614 + 5614 cases (ν = 0..400, 14 values of x in [0.5, 10⁴]), 0 failed. Smallest relative slack 9.7e−10 for Q1 at (ν, x) = (400, 0.5), against a tolerance of 1e−10. The child T90 checked the same independently (§7).

**K1 (two-sided κ bound).** For n ≥ 0 and β > 0:
  n(n+2)/(2(β+n+½)) ≤ −ln κ_n(β) ≤ n(n+3)/(2β).
- PROVED from B:
  - Upper bound: by (A), −ln r_ν ≤ ln(t+√(1+t²)) with t = (ν+1)/β, and this is ≤ t (**G1**, PROVED+LEAN). Summing, Σ_{ν=1}^n (ν+1) = n(n+3)/2 (**G6b**, PROVED+LEAN).
  - Lower bound: by (B), with c = ν+½, r_ν ≤ x/(c + x) = 1/(1+c/x). So −ln r_ν ≥ ln(1+c/β) ≥ c/(β+c) (**G2**, PROVED+LEAN) ≥ (ν+½)/(β+n+½) for ν ≤ n. Summing, Σ_{ν=1}^n (ν+½) = n(n+2)/2 (**G6a**, PROVED+LEAN).
- NUM Q3: 11228 cases, 0 failed. Tightest case: n = 1, β = 10⁴, relative slack 2.0e−4.
- κ_n is decreasing in n, since r_ν < 1 by (B).

**K2 (spin-cutoff bookkeeping; brief point (i)).** Fix m ∈ (0, ½] and put M = ⌊m√β⌋.
- Low set L = {n_1 ≤ M, n_2 ≤ M}. There
    1 − κ_{n_1}κ_{n_2} ≥ θ(m,β) · (n_1(n_1+2) + n_2(n_2+2))/(2β),
  with θ(m,β) := (β/(β+M+½)) · 1/(1+m²+3m/√β). Note θ → 1/(1+m²) as β → ∞, and θ → 1 as m → 0 afterwards.
- High set (complement of L). There
    1 − κ_{n_1}κ_{n_2} ≥ c(m,β) := 1 − exp(−(M+1)(M+3)/(2(β+M+3/2))),
  with c → 1 − e^{−m²/2} > 0.
- PROVED:
  - Low set: y = −ln κ_{n_1} − ln κ_{n_2} lies between y_lo = (λ_1+λ_2)/(2(β+M+½)) (K1, with n_i ≤ M) and y_hi = (M²+3M)/β ≤ m² + 3m/√β (K1). Then 1 − e^{−y} ≥ y/(1+y) (**G3**, PROVED+LEAN) ≥ y_lo/(1+y_hi).
  - High set: some n_i ≥ M+1. Since κ_{n_j} ≤ 1, 1 − κκ ≥ 1 − κ_{n_i} (**G7**, PROVED+LEAN) ≥ 1 − κ_{M+1} ≥ c(m,β) (K1 and monotonicity).
- NUM Q4 (2984 cases) and Q5 (4.4·10⁶ cases): 0 failed, for m ∈ {0.05, 0.1, 0.2, 0.3} and β ∈ [100, 10⁴].
- Consequence: since K is diagonal in (n_1,n_2), let P be the spectral projection onto L, with P^⊥ = 1 − P. For every f ∈ L²(G²):
    ⟨f,(1−K)f⟩ ≥ θ(m,β)⟨Pf,(−Δ/2β)Pf⟩ + c(m,β)‖P^⊥f‖².   (2.1)
  Here Pf is a finite Peter–Weyl sum, so it is smooth, and ⟨Pf,−ΔPf⟩ = ∫_{G²}|∇Pf|² dU.
- The cutoff m is **fixed** while β → ∞ and is sent to 0 only at the very end (§4, step 6). No rate m(β) is needed.

**Chart (brief point (iii)).** For 0 < a ≤ 1: a²(1−a²/2) ≤ sin²a, and sin a ≤ a (**G5**, PROVED+LEAN, from Mathlib's sin x > x − x³/4).

## 2. Rechecks of L1–L4 (in the forms used)

**L1 (used in the form): ν_k ≥ ν^H_k/(1+ν^H_k).** RECHECKED, STANDS. This covers the lower direction of brief point (iv).
- Put f = e^{V/2}g, a bijection of S onto itself (V is conjugation- and center-invariant), and W = e^V − 1 ≥ V ≥ 0. Then 1 − ⟨f,Tf⟩/‖f‖² = Q(g) = (a+w)/(n+w), with a = ⟨g,(1−K)g⟩ ∈ [0,n], n = ‖g‖², w = ⟨g,Wg⟩.
- d/dw[(a+w)/(n+w)] = (n−a)/(n+w)² ≥ 0, so Q ≥ (a+v)/(n+v) with v = ⟨g,Vg⟩ ≤ w.
- With t = (a+v)/n we have v/n ≤ t, so (a+v)/(n+v) = t/(1+v/n) ≥ t/(1+t).
- t ↦ t/(1+t) is increasing, so min-max gives 1 − λ_k = μ_k ≥ ν^H_k/(1+ν^H_k).
- Finally ν_k = −ln(1−μ_k) ≥ μ_k.
- So liminf β^{1/3}ν_k ≥ liminf β^{1/3}ν^H_k whenever the right side is finite, because then ν^H_k → 0 and the factor 1/(1+ν^H_k) → 1. The loss is O(β^{1/3}(ν^H_k)²) = O(β^{−1/3}), which is o(1) after rescaling.
- The upper direction (§2 of SCALING_LIMIT: ν_k ≤ μ_k/(1−μ_k), with W ≤ Ve^{V_max} on box-supported trial functions) is used only for the corollary and was NOT rechecked here.

**L2 (used: ∫k(h) d(h,1)² dh ≤ π²/β).** RECHECKED, STANDS.
- E[cos a] = d/dβ ln(I_1(β)/β) = I_2/I_1.
- By (A) with ν = 1: 1 − r_1 ≤ (2 + √(4+β²) − β)/(2+√(4+β²)) ≤ (2+2/β)/(2+β) ≤ 2/β.
- a² ≤ (π²/2)(1 − cos a) on [0,π], from sin(a/2) ≥ a/π.

**L3 (used: |⟨g,(1−K)g⟩ − Σ_α⟨χ_αg,(1−K)χ_αg⟩| ≤ ½ sup_U ∫k_2(U,W)D(U,W)dW · ‖g‖², with D = Σ_α(χ_α(U)−χ_α(W))²).** RECHECKED. It STANDS in absolute value, with a **sign typo**.
- From Σ_αχ_α(U)χ_α(W) = 1 − ½D one gets Σ_α⟨χ_αg,(1−K)χ_αg⟩ = ⟨g,(1−K)g⟩ **+** ½∫∫k_2 ḡ(U)g(W)D. SCALING_LIMIT writes this term with the opposite sign on the other side.
- The term is bounded by the Schur test, because k_2D ≥ 0 is symmetric. Only its absolute value is used, so nothing changes.
- The V-part localises exactly.

**L4 (used: for β ≥ β_0, 0 < σ ≤ s_* = 0.002, any unit n, on L²(G): (1−K_1) + 2βσ²|x⃗×n|² ≥ σ − 1/β).** RECHECKED, STANDS. The constant of its IMS error is corrected.
- B = 2βσ²|x⃗×n|² is an even polynomial of degree 2 on S³ ⊂ R⁴. So B maps degree n into degrees n−2, n, n+2 (parity is preserved), and ‖B‖ ≤ 2βσ².
- Decompose B = B_{−2} + B_0 + B_2 by degree shift. Each B_d is a Fourier average of e^{iθN}Be^{−iθN}, so ‖B_d‖ ≤ ‖B‖.
- [χ,[χ,B_d]] = B_d·diag(w_d(n)) with w_d(n) = (χ(n+d)−χ(n))² ≤ (π|d|/2M)².
- So ‖½Σ_{i∈{lo,hi}}[χ_i,[χ_i,B]]‖ ≤ ½·2·2·‖B‖(π/M)² = 2π²‖B‖/M² ≤ 8π²σ² ≈ 79σ², using M² = β/2.
- SCALING_LIMIT writes "5π²σ²/m² ≈ 98.7σ²". Its own formula 5π²‖B‖/M² actually gives 20π²σ² ≈ 197σ², so the factor ‖B‖ = 2βσ² was dropped (arithmetic slip). Both 79σ² and 197σ² still close the bound:
  - √2 − 79·0.002 = 1.256 > 1;
  - √2 − 197·0.002 = 1.019 > 1.
- High part (n > M): 1 − κ_n ≥ 1 − exp(−M(M+2)/(2(β+M+½))) → 1 − e^{−1/4} = 0.221 (K1). This is ≥ √2σ, and B ≥ 0.
- Low part (n < 2M): y ≤ 2m² + 3m/√β = 1 + o(1), so 1 − κ_n ≥ y/(1+y) ≥ ½(1−o(1))·n(n+2)/(2β) (K1, G3).
- S7 (TORON_GAP), RECHECKED: for φ = e^{−k sin²χ}, (−Δφ)/φ + 4k²u = 4k − 8ku + 4k²u² with u = sin²χ. I recomputed this from Δf = (sc)^{−1}(sc f′)′. The right side is ≥ 4k − 4 (**G4**, PROVED+LEAN, as 4(ku−1)² ≥ 0).
- With λ = 2β²σ²/(1−o(1)), the low part is ≥ √2σ(1−o(1)) − 1/β.
- Total: ≥ (√2(1−o(1)) − 79σ)σ − 1/β ≥ σ − 1/β. Here o(1) → 0 as β → ∞, uniformly in σ ≤ s_*. So β_0 depends on nothing else.

## 3. The chart (brief point (iii)), PROVED

Put a_max ≤ 1 and Ω = {a_1, a_2 < a_max}.
- In geodesic polar coordinates the metric of the unit S³ is da² + sin²a g_{S²}, and the normalised Haar measure is (2π²)^{−1} sin²a da dω = (2π²)^{−1}(sin a/a)² d³A.
- For u smooth on Ω, |∇u|²_g = Σ_i[(∂_{a_i}u)² + |∇_{ω_i}u|²/sin²a_i]. Multiplying by the volume element:
  - the radial term i carries the weight (sin a_i/a_i)²(sin a_j/a_j)² relative to the flat density;
  - the angular term i carries (sin a_j/a_j)².
- With j := 1 − a_max²/2 ≤ (sin a/a)² ≤ 1 (G5):
    ∫_Ω|∇u|² dU ≥ j²(2π²)^{−2}∫_Ω|∇_A u|² d⁶A,   ‖u‖²_{L²(Ω,dU)} = (2π²)^{−2}∫_Ω |u|² Π(sin a_i/a_i)² d⁶A.
- Rescaling: d⁶A = β^{−2}d⁶Y and ∇_A = β^{1/3}∇_Y. Then
    (2β)^{−1}∫_Ω|∇u|²dU ≥ ½ j² β^{−1/3}‖∇_Y 𝓡u‖²_{L²(Ω̂)},   ‖u‖² = ∫|𝓡u|²J,  j² ≤ J ≤ 1,   (3.1)
  where Ω̂ = β^{1/3}Ω.
- Potential: sin²a_i ≥ j a_i², and γ is the same angle in the A-coordinates. So V ≥ 2βj²|A_1×A_2|² = j²β^{−1/3}w(Y), and β^{1/3}⟨f,Vf⟩ ≥ j⁴∫w|𝓡f|².   (3.2)

## 4. L6 (Γ-liminf in one box): PROVED

**Statement.**
- Hypotheses: R ≥ 1 is fixed. B_β := {a_1, a_2 ≤ α_β} with α_β := arcsin(2Rβ^{−1/3}). Let β_l → ∞, and let f_l ∈ L²(G²) be supported in B_{β_l}, with ‖f_l‖ ≤ 1 and β_l^{1/3}⟨f_l,Hf_l⟩ ≤ C.
- Conclusion: there are a subsequence and ψ ∈ Q(h) ∩ L²(R⁶) with
  - supp ψ ⊂ □ := {|Y_1|, |Y_2| ≤ 3R};
  - 𝓡f_l → ψ in L²(R⁶), and ‖ψ‖ = lim‖f_l‖;
  - liminf β_l^{1/3}⟨f_l,Hf_l⟩ ≥ q_h(ψ).
- If moreover each f_l is conjugation-invariant, then ψ ∈ L²_inv.

**Proof.**
1. *Geometry.* β^{1/3}α_β → 2R, so for β ≥ β_1(R), 𝓡f is supported in □. Put Ω := {a_i < 4Rβ^{−1/3}}, so Ω̂ = □' := {|Y_i| < 4R} is fixed. For β ≥ (4R)³ we have a_max = 4Rβ^{−1/3} ≤ 1, so §3 applies with j_β = 1 − 8R²β^{−2/3} → 1.
2. *Spin split (point (i)).* Fix m ∈ (0, ½]. By (2.1), V ≥ 0, and the fact that the Dirichlet integral over G² dominates the one over Ω:
     β^{1/3}⟨f,Hf⟩ ≥ θ β^{1/3}(2β)^{−1}∫_Ω|∇Pf|²dU + β^{1/3}c‖P^⊥f‖² + β^{1/3}⟨f,Vf⟩
                  ≥ ½θj²‖∇_Y φ̃‖²_{L²(□')} + β^{1/3}c‖P^⊥f‖² + j⁴∫w|φ|²,   (4.1)
   using (3.1) and (3.2), with φ := 𝓡f and φ̃ := 𝓡(Pf)|_{□'}.
   - Hence ‖P^⊥f_l‖² ≤ Cβ_l^{−1/3}/c(m,β_l) → 0, since c → 1 − e^{−m²/2} > 0.
   - Also ‖∇φ̃_l‖²_{□'} ≤ 2C/(θj²), bounded.
   - And ‖φ̃_l‖²_{L²(□')} ≤ j^{−2}‖Pf_l‖² ≤ j^{−2}.
3. *Leaving the box (point (ii)).* Pf is not supported in B_β. We never need a compactly supported version of it, so **no commutator [ζ,Δ] appears**: the second spatial cutoff is the restriction to □', which is legitimate because the Dirichlet integral is monotone in the domain (step 2). The only interaction between the cutoff and P is the L² leakage. Since f = 0 off B_β, φ̃ − φ = 𝓡(Pf − f) = −𝓡(P^⊥f) on □', so ‖φ̃_l − φ_l‖_{L²(□')} ≤ j^{−1}‖P^⊥f_l‖ → 0.
   - If one prefers a smooth cutoff ζ (ζ = 1 on B_β, supp ζ ⊂ Ω), then ζPf = f − ζP^⊥f, and the same leakage bound is all that is used. The gradient of ζPf is never needed.
4. *Compactness.* □' is a bounded Lipschitz domain and (φ̃_l) is bounded in H¹(□'). By Rellich–Kondrachov (CITED, standard; e.g. Evans, PDE, §5.7 Thm 1, from memory) and weak compactness, a subsequence has φ̃_l → ψ strongly in L²(□') and weakly in H¹(□').
   - By step 3, φ_l → ψ in L²(□'). Since φ_l = 0 on □'∖□, ψ = 0 a.e. on □'∖□.
   - Take η ∈ C_c^∞(□') with η = 1 on a neighbourhood of □. Then ψ = ηψ ∈ H¹_0(□'), and its extension by 0 lies in H¹(R⁶), with supp ⊂ □.
   - ‖ψ‖² = lim‖φ_l‖² = lim∫|φ_l|²J_l = lim‖f_l‖², because J_l → 1 uniformly on □.
5. *Form domain (point (v)).* Put ψ_ε = ψ * ρ_ε, a mollification. Then ψ_ε ∈ C_c^∞ is supported in a fixed compact set, and ψ_ε → ψ in H¹. Since w ≤ 2(4R)⁴ there, ∫w|ψ_ε−ψ|² → 0. So ψ_ε is q_h-Cauchy, ψ lies in the form closure Q(h), and q_h(ψ) = ½‖∇ψ‖² + ∫w|ψ|².
   - The general principle used: a compactly supported H¹ function automatically has finite potential energy, because w is locally bounded, and it is the H¹+w limit of its mollifications.
6. *Lower semicontinuity.* Weak lsc on H¹(□') gives liminf‖∇φ̃_l‖²_{□'} ≥ ‖∇ψ‖²_{□'} = ‖∇ψ‖²_{R⁶}. Since w is bounded on □ and φ_l → ψ in L², ∫w|φ_l|² → ∫w|ψ|².
   - With θ(m,β) → 1/(1+m²) and j → 1, (4.1) gives liminf β_l^{1/3}⟨f_l,Hf_l⟩ ≥ (1+m²)^{−1}·½‖∇ψ‖² + ∫w|ψ|².
   - ψ is the L² limit of φ_l = 𝓡f_l, so it does not depend on m. Given any sub-subsequence that realises the liminf, extract further for step 4: the limit is the same ψ. So the bound holds for every m ∈ (0, ½].
   - Letting m → 0 gives liminf ≥ q_h(ψ). ∎
7. *Invariance.* Conjugation by h ∈ SU(2) acts on A by R_h ∈ SO(3) on both factors at once. B_β is invariant, so 𝓡f(R_hY_1, R_hY_2) = 𝓡f(Y). L² limits keep this.

## 5. L7 (conclusion): PROVED

**Theorem.** For every k ≥ 0: liminf_{β→∞} β^{1/3}ν^H_k(β) ≥ E_k. By L1, the same holds for ν_k.

**Proof.** Fix k. Put Λ := liminf β^{1/3}ν^H_k. If Λ = ∞ there is nothing to prove. Otherwise choose β_l → ∞ with β_l^{1/3}ν^H_k(β_l) → Λ, and fix R ≥ R_0 (chosen in step 3). Write β for β_l.

1. *Eigenvectors.*
   - K has a continuous kernel on a compact space, so it is Hilbert–Schmidt and compact. By Weyl's theorem, σ_ess(H|_S) ⊂ σ(1+V) ⊂ [1, 1+2β].
   - For large l, ν^H_k ≤ (Λ+1)β^{−1/3} < 1. So ν^H_0..ν^H_k are eigenvalues of H on S, with orthonormal eigenvectors g_0..g_k ∈ S.
   - For every unit g ∈ 𝒢 := span{g_j}: ⟨g,Hg⟩ ≤ ν^H_k.
2. *Partition.*
   - Let ρ(t) = clip(t−1, 0, 1), ϑ_i = (π/2)ρ(s_i/σ_R) with σ_R = Rβ^{−1/3}, and
     χ_0 = cos ϑ_1 cos ϑ_2,  χ_1 = sin ϑ_1 cos ϑ_2,  χ_2 = sin ϑ_2.
   - Then Σχ_α² = 1 (**G8**, PROVED+LEAN, as an identity). Each χ_α is real and invariant under conjugation and both center flips.
   - Repair to L5: L5 writes χ_1 = η_1(1−η_2²)^{1/2}, which is not Lipschitz for a general smooth step θ. The sin/cos form fixes this.
   - (χ_0, χ_1, χ_2) is the standard embedding of (ϑ_1, ϑ_2) into S², whose metric is cos²ϑ_2 dϑ_1² + dϑ_2². So D ≤ |Δϑ_1|² + |Δϑ_2|² ≤ (π/2σ_R)²(d_1² + d_2²), because s_i = |sin d(U_i,1)| is 1-Lipschitz.
   - By L3 and L2, the IMS error is ≤ ½(π/2σ_R)²·2π²/β = (π⁴/4R²)β^{−1/3}. The constant is explicit, independent of k and β, and of order R^{−2}.
   - So Σ_α⟨χ_αg,Hχ_αg⟩ ≤ ν^H_k + (π⁴/4R²)β^{−1/3} for unit g ∈ 𝒢.   (5.1)
3. *Arms (L5, rechecked).*
   - On supp χ_2 we have s_2 ≥ σ_R, so V ≥ 2βσ_R²|x⃗_1×n_2|². Also 1 − K_1⊗K_2 ≥ (1−K_1)⊗1, since 0 ≤ K_2 ≤ 1.
   - L4 applied in each fibre U_2 (σ = σ_R ≤ s_* once β ≥ (R/s_*)³ and β ≥ β_0) gives ⟨χ_2g,Hχ_2g⟩ ≥ (σ_R − 1/β)‖χ_2g‖². The same holds for χ_1, with the factors exchanged.
   - With ⟨χ_0g,Hχ_0g⟩ ≥ 0, (5.1) gives (R − β^{−2/3})(1 − ‖χ_0g‖²) ≤ Λ + 1 + π⁴/(4R²).
   - So 1 − ‖χ_0g‖² ≤ τ_R := (Λ + 1 + π⁴/4)/(R − 1) for large l. R_0 is chosen so that τ_{R_0} < ½.
   - The arms are ≥ 0, so (5.1) also gives ⟨χ_0g,Hχ_0g⟩ ≤ ν^H_k + (π⁴/4R²)β^{−1/3}.
4. *Four boxes (center-evenness; point (v)).*
   - supp χ_0 ⊂ {s_1, s_2 ≤ 2σ_R} = ⊔_{z∈{±1}²} zB_β. The union is disjoint for α_β < π/2.
   - Put F[g] := 1_{B_β}χ_0g. Since g is center-even and χ_0 and V are center-invariant, the piece in zB_β is F[g](z·), and K commutes with central translations. Hence:
     - ‖χ_0g‖² = 4‖F‖²;
     - ⟨χ_0g,Vχ_0g⟩ = 4⟨F,VF⟩;
     - ⟨χ_0g,(1−K)χ_0g⟩ = 4⟨F,(1−K)F⟩ − X.
   - X is the sum of 12 cross terms with z ≠ z′. In some factor, U_iW_i^{−1} is at distance ≥ π − 2α_β from 1. With the elementary bound Z ≥ (2/3π)β^{−3/2}(1 − 1/(3β))e^{β−1/2} (restrict to a ≤ β^{−1/2} as in U4), this gives
       |X| ≤ 12 e^{β(1−cos 2α_β)}Z^{−2}‖F‖_1² ≤ C β³ e^{1−2β+16R²β^{1/3}}‖F‖² =: ε_X(β,R)‖F‖².
     Here ‖F‖_1 ≤ ‖F‖_2 because Haar measure is a probability measure. β^{1/3}ε_X → 0 for each R.
   - Therefore, for unit g ∈ 𝒢: β^{1/3}⟨2F[g],H 2F[g]⟩ ≤ β^{1/3}ν^H_k + π⁴/(4R²) + β^{1/3}ε_X, and ‖2F[g]‖² = ‖χ_0g‖² ∈ [1−τ_R, 1].
5. *Limits and Gram matrix (point (vi)).*
   - g ↦ 2F[g] is linear. Apply L6 to f_l = 2F[g_j] for j = 0..k in turn, extracting subsequences. This gives 𝓡(2F[g_j]) → ψ_j in L², with ψ_j ∈ Q(h) ∩ L²_inv supported in □.
   - For every unit c ∈ C^{k+1}, 𝓡(2F[g_c]) → ψ_c := Σc_jψ_j in L², where g_c = Σc_jg_j. L6 applied to f_l = 2F[g_c] along the same subsequence gives:
     - ‖ψ_c‖² = lim‖χ_0g_c‖² ∈ [1−τ_R, 1];
     - q_h(ψ_c) ≤ Λ + π⁴/(4R²).
   - So the Gram matrix Γ_{ij} = ⟨ψ_i,ψ_j⟩ satisfies Γ ≥ (1−τ_R)I > 0. The ψ_j are linearly independent and span a (k+1)-dimensional subspace of Q(h) ∩ L²_inv.
6. *Min-max and order of limits (point (vii)).*
   - By the definition of E_k (min-max; CITED, Reed–Simon IV Thm XIII.1/XIII.2, from memory):
       E_k ≤ max_c q_h(ψ_c)/‖ψ_c‖² ≤ (Λ + π⁴/(4R²))/(1 − τ_R).
   - The limits are taken in this order: β → ∞ along β_l first, at fixed R and m. Then m → 0, inside L6. Then R → ∞.
   - Every R-dependent quantity (β_1(R), (4R)³, (R/s_*)³, ε_X) affects only how large β must be. The surviving constants π⁴/(4R²) and τ_R depend only on R and Λ, and both → 0.
   - Constants that depend on k enter only through Λ = Λ(k), which is finite in this case.
   - So R → ∞ gives Λ ≥ E_k. ∎

**What is proved, exactly.**
- For every k ≥ 0, liminf β^{1/3}ν_k ≥ E_k (min-max values).
- E_k equals the k-th eigenvalue of h|inv once h has compact resolvent (SCALING_LIMIT C1, CITED there; not needed for the inequality).
- Inputs: B (CITED and read; NUM), Rellich–Kondrachov, the min-max principle and Weyl's theorem (standard, from memory), and the rechecked L1–L4 forms above.
- **Corollary** (CONDITIONAL): β^{1/3}m_e = β^{1/3}(ν_1 − ν_0). So liminf β^{1/3}m_e ≥ liminf β^{1/3}ν_1 − limsup β^{1/3}ν_0 ≥ E_1 − E_0, provided limsup β^{1/3}ν_0 ≤ E_0 (SCALING_LIMIT §2, PROVED there, **not rechecked here**). Positivity of E_1 − E_0 needs C2 (Reed–Simon XIII.47, cited from memory there).

## 6. Step tags (summary)
| step | tag |
|---|---|
| B (A),(B) | CITED (RS 2016 Thm 2, read via fetch agent from the HTML) + NUM (mine and child T90) |
| K1, K2, (2.1) | PROVED; scalar steps G1, G2, G3, G6a, G6b, G7 PROVED+LEAN; NUM Q3–Q5 |
| chart (3.1), (3.2) | PROVED; G5 PROVED+LEAN; NUM Q7 |
| L1, L2 | rechecked, PROVED |
| L3 | rechecked, PROVED; sign typo noted |
| L4 | rechecked, PROVED; constant corrected (79σ², not "98.7σ²") |
| S7 | rechecked, PROVED; G4 PROVED+LEAN; NUM Q6 |
| L5 | rechecked, PROVED with the sin/cos partition (repair) |
| L6 | PROVED (Rellich–Kondrachov CITED, from memory) |
| L7 | PROVED (min-max and Weyl CITED, from memory) |
| corollary | CONDITIONAL on SCALING_LIMIT §2 (k = 0) and C2 |
| MISSING | none inside L6/L7 |

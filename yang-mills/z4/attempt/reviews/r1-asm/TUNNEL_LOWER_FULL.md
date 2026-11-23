**What the assembly proves: the parts fit together into one linear proof of limsup_{β→∞} (−log m_eo)/√β ≤ c* = 4.6054132 after seven stated changes (C1–C7). No interface DOES NOT FIT. Two of the changes add steps that were not written anywhere: Lemma L4 (λ_ee, λ_eo → 1, which until now was a sketch) and the chain from x to σx (§4). The other five are re-parametrisations or smoothings that do not change any proof's mechanism. What remains: the result is only as good as the unreviewed proofs it rests on. All of them were written by workers in the same model family as me: Lemma F (LEMMA_F.md), (E1)/(E3) (E13.md), H4 (HARNACK.md), P'c/Corollary B (PATHS.md), Lemma K and (B) (TUNNEL_THEOREM.md), and S4-alg (TUNNEL_LOWER2.md). I re-derived the interfaces between them, not the inside of E13 §2–§4 or LEMMA_F §2. So the status is: PROVED IN WRITING, CONDITIONAL ON THOSE PARTS, NOT INDEPENDENTLY REVIEWED. Together with TUNNEL_THEOREM (liminf ≥ c*, now unconditional because Lemma F is proved in LEMMA_F.md), this would give lim (−log m_eo)/√β = c*.**

Worker r1-asm (task T158). I share a model family with the director and with every author of the parts, so my agreement is not independent review. No network was used. Numerical sanity checks: asm_check.py (asm_check_results.json) and onedflux.py (onedflux_beta64/256.json). The child T160 ran a 1D factor check, and grandchild T161 ran under it.

## 0. Model and fixed choices

- X = SU(2)² with Haar probability measure, and T = e^{−V/2}K₁K₂e^{−V/2}, where V = 2β|u₁×u₂|². The flips are σ = σ₁: U₁ → −U₁ (a₁ → π − a₁) and σ₂: U₂ → −U₂.
- g is the top eigenvector (sector ee), with ‖g‖ = 1 and eigenvalue λ := λ_ee ≤ 1.
- f is the top eigenvector of the sector odd under σ₁ and even under σ₂ (gauge invariant), with ‖f‖ = 1 and eigenvalue λ_eo. Δ := λ − λ_eo.
- m_eo = log(λ/λ_eo) ≥ 1 − λ_eo/λ = Δ/λ ≥ Δ, using log x ≥ 1 − 1/x and λ ≤ 1. This settles interface (6): FITS.
- f is also an eigenfunction of T on all of L²(X), because T commutes with gauge transformations. So PATHS (H1)–(H4) hold with σ = σ₁.

**Order of choices.** First fix η ∈ (0, 0.4]. Then fix, in this order:
- a₋ := arcsin(sinh η), so that ε(sin a₋) = 2η;
- r₀ := √(η sin a₋/4);
- ℓ := r₀/3 and θ₀ := 1/2;
- K := 1;
- ρ := 0.265 and d := 3.65 (HARNACK);
- the ball radius ρ_B := 1/2 for the path balls of §4;
- M = M(η), large enough for S4-alg (the c₁ condition) and with M² ≥ 2ρ_B²;
- η' := a₋ (change C1).

Then let β → ∞, and only at the end let η → 0. All o(1) terms below are as β → ∞ with these quantities fixed.

## 1. Interface (1): the sets

| set | definition (where) | form used here |
|---|---|---|
| supp φ_L | {G > c₁ = e^{−M²}} ∩ {E > c₂ = e^{−√βΘ(r₀)}} = {βα(S)q/2 < M²} ∩ {a₂ < r₀} (TUNNEL_LOWER2 §2) | same |
| Ω | supp φ ∩ {a₁ ∈ [a₋, π − a₋]} (TUNNEL_LOWER2 §2) | same; φ_L, φ_R have the same support because q, S, a₂ are σ₁-invariant |
| tube K | {a₁ ∈ [η', π−η'], a₂ ∈ [0, r₀], βαq/2 < M²} (E13 §0, numbers η' = 0.5) | with η' = a₋, K ⊇ Ω ∩ {a₁ ≤ π/2} (closure) |
| R_well | supp φ ∩ {a₁ < a₋ or a₁ > π − a₋} (TUNNEL_LOWER2 §2) | ⊂ D_M ∪ σ₁D_M |
| D_M | {a₁, a₂ ≤ π/2, V ≤ 2M²} (HARNACK §3) | same |
| S | C_η ∩ {V ≤ K}, the four corners {a_i < a₋ or > π − a₋} (PATHS §4) | same; it is σ₁-invariant because ε(sin a₁) and V are |

**Check.**
- On supp φ_L, V = 2βS²q < 4S²M²/α(S) = 2M²S/√(1+S²) < 2M², and a₂ < r₀ ≤ π/2. So R_well ∩ {a₁ < a₋} ⊂ D_M, and the other half is ⊂ σ₁D_M. FITS.
- **C1 (FITS AFTER STATED CHANGE).** E13's numerical parameter set (η = 0.25, η' = 0.5) has η' > a₋ = 0.2554 (asm_check P6 FAILED, as expected). With that set, (E1)/(E3) are not proved on the strip a₁ ∈ [a₋, η'), which Lemma C needs. The change is η' := a₋.
  - E13's proof takes any η' > 0. Its constants depend on η' only through sin²η' (in the Δh bound) and on H_Ψ, Λ, and all of these are fixed before β → ∞.
  - E13's hypothesis (H1), "C² near [η' − 0.1, π − η' + 0.1]", becomes "C² on a neighbourhood of [η'/2, π/2 + η'/2]". The 0.1 is only a margin for steps of length L/√β → 0.
  - With Ψ ≡ 0 on [0, a₋/2], Ψ∘a₁ is smooth near U₁ = 1 anyway.
  - An equivalent alternative: keep η' > a₋, start Ω at η', and let HARNACK cover a₁ ∈ [a₋, η'), since that strip lies in D_M. This costs 8.35·2η'/d per unit of √β, so η' must → 0 with η.
- **σ.** S, Ω and supp φ are invariant under σ₁. The odd flip of m_eo is σ₁ (TUNNEL_THEOREM §0). The tube of TUNNEL_LOWER2 §4 "and its U₂ → −U₂ image" is not needed when S is the corner set. FITS.

## 2. Interface (2): Lemma C on Ω

**Form needed (TUNNEL_LOWER §1, rechecked in the continuum by PATHS §3(C)).**
- φ ≥ 0, φ ∈ L².
- ‖T_ΩΩ‖ < λ.
- (Tφ)(x) ≥ λφ(x) for x ∈ Ω.
- φ ≤ g a.e. on Ω^c.
- Conclusion: φ ≤ g on Ω, and everywhere by continuity of g and φ.
- Ω^c = {φ = 0} ∪ R_well. On {φ = 0} the inequality φ ≤ g is trivial. On R_well, φ ≤ μ, so g ≥ μ is needed there (§3).

**Form proved.**

(a) *‖T_ΩΩ‖ < λ.*
- TUNNEL_LOWER2 §2 gives ‖1_Ω B*B 1_Ω‖ ≤ sup_{a₁ ∈ [a₋, π−a₋]} ‖F_{a₁}‖, using 1_Ω = 1_Ω 1_{a₁-range}.
- Lemma F (LEMMA_F §3, PROVED there), applied with η/2, gives ‖F_{a₁}‖ ≤ e^{−2η + η/2} for β ≥ β₀(η).
- λ > e^{−3η/2} by Lemma L4 (§5). FITS.

(b) *Tφ ≥ λφ on Ω.*
- φ = max(φ_L, φ_R), with φ_R = φ_L∘σ₁. Because q, S, a₂ are σ₁-invariant and Ψ is strictly increasing on [a₋, π − a₋/2], we have φ_L ≥ φ_R exactly when a₁ ≤ π/2. Then Tφ ≥ Tφ_L ≥ λφ_L = λφ. So S4-alg is needed only at x ∈ supp φ_L with a₁ ∈ [a₋, π/2], and symmetrically for φ_R.
- S4-alg needs (E1), (E2), (E3) at those x, with errors o(1).
- (E1) and (E3) come from E13 on K, which covers these x after C1, with sup_K Δ₁, Δ₃ = O((log β)^{3/2}β^{−1/2}).
- (E2) comes from Lemma K (TUNNEL_THEOREM §3).

**Changes.**
- **C2 (FITS AFTER STATED CHANGE).** TUNNEL_LOWER2 defines Ψ as "Ψ' = √(2(ε+η)) on [a₋, π − a₋/2], flat after". This gives a kink at π − a₋/2, where E13 (§0 remark) shows (E3) fails, and it breaks the global C² that Lemma K needs for (E2).
  - Change: Ψ' = χ(a)√(2(ε(sin a)+η)), where χ ∈ C^∞ with 0 ≤ χ ≤ 1, χ = 0 on [0, a₋/2] ∪ [π − a₋/4, π], and χ = 1 on [a₋, π − a₋/2].
  - Then Ψ∘a₁ is C^∞ on SU(2), and H_Ψ = sup max(|Ψ''|, |Ψ' cot a|) < ∞ (Ψ' = 0 near 0 and π). Also 0 ≤ Ψ' ≤ √(2(ε+η)) everywhere. That bound is used in §4 and was not stated in TUNNEL_LOWER2.
  - Nothing in S4-alg changes, because the inequality is used only for a₁ ≤ π/2 < π − a₋/2.
- **C3 (FITS AFTER STATED CHANGE).** Θ(a) = θ₀(√(a² + ℓ²) − ℓ) has Θ'(π) ≠ 0, so Θ∘a₂ has a cone point at U₂ = −1 and is not C² there. Lemma K, used for (E2), asks for a global Hessian bound.
  - Change: replace Θ by a C^∞ Θ̃ with Θ̃ = Θ on [0, π/2] and Θ̃' = 0 near π, keeping 0 ≤ Θ̃' ≤ θ₀ and Θ̃ nondecreasing.
  - E13 uses Θ only on a₂ ≤ r₀ + o(1) (its (H2) is stated for a ≤ π/2), and S4-alg uses only the values of E and |∇Θ| on supp φ. So nothing else changes.
- **Absorption of Δ₁, Δ₃ (re-proved in the form used).** On supp φ_L ∩ {a₁ ∈ [a₋, π/2]}:
  - A₁ − λ ≥ e^{η − D − Δ₁} − 1, with D = ε(S) − ε(sin a₁) ≤ 2(S − sin a₁) ≤ sin²a₂/sin a₁ ≤ r₀²/sin a₋ = η/4.
  - So A₁ − λ ≥ e^{3η/4 − Δ₁} − 1 ≥ e^{η/2} − 1 once Δ₁ ≤ η/4. This is where the order of limits (β → ∞ first, η fixed) is used.
  - The remaining absorptions in S4-alg need c₁ = e^{−M²} ≤ G_min(e^{η/2} − 1)e^{−C}/4. Here G_min = exp(−(√(1+S²)/S)(ε(S)+1)) ≥ exp(−(√2/sin a₋)(ε(√2)+1)) and C = ε(√2) + η + θ₀²/2 + 1.
  - So M² ≈ 3.4/η suffices (asm_check P5: M² required = 14.8, 23.4, 40.4, 73.9, 174, 339 at η = 0.4 … 0.01).
- **Verdict on (2): FITS AFTER STATED CHANGES C1–C3.**

## 3. Interface (3): normalisation μ

- **Form used.** φ_L = μ e^{−√βΨ(a₁)}(G − c₁)₊(E − c₂)₊ with μ ≤ inf_{R_well} g. This is not "g ≥ c₀φ with c₀ = inf g/φ": μ is placed inside φ, so Lemma C gives g ≥ φ directly.
- **Form proved (HARNACK Theorem H4 and Corollary).** For x ∈ D_M,
 −log g(x) ≤ 35(a₋ + r₀)√β + O(M^{5/2}β^{1/4}) + O(log β) − log(4m_B).
 Here m_B = ∫_{a₁,a₂<a₋, V≤1} g² ≥ ¼ − o(1) by Lemma M4.
- **Checks.**
  - M is fixed (M = M(η)) before β → ∞, so the β^{1/4} term is o(√β).
  - The tube entrance is in HARNACK's region: R_well ⊂ D_M ∪ σ₁D_M (§1). By σ₁-evenness of g the bound holds on σ₁D_M.
  - The relation η' = a₋ comes from C1.
- So μ := exp(−35(a₋ + r₀)√β − C_M β^{1/4} − C log β). FITS.
- **DEFECT (harmless) in HARNACK §3.** "M² = O(log(1/η))" is wrong: G_min ~ e^{−1/sin a₋}, so M² ~ 1/sin a₋ ~ 1/η (asm_check P5). M enters only the β^{1/4} term, so the conclusion is unaffected.

## 4. Interface (4): the chain and the factor c* versus 2c*

**Factor.**
- TUNNEL_LOWER2's Ψ is monotone through π/2, but φ = max(φ_L, φ_R) = μ e^{−√β min(Ψ(a₁), Ψ(π−a₁))} × (transverse factors). This is the tent.
- The tent's kink at a₁ = π/2 is a minimum of φ, and the subsolution inequality there is proved by the max argument of §2(b). This is the same device as in 1D: TUNNEL_LOWER Lemma S ("reflected branch lies below the monotone extension") and PATHS §3(S) (Ψ = min(Ψ₀(y), Ψ₀(π−y))).
- Hence sup over the chain of −log g ≤ √β Ψ(π/2) + (−log μ) + O(1), and 2Ψ(π/2) ≤ ∫₀^π √(2(ε+η)) = c*(η) (using C2: Ψ' ≤ √(2(ε+η))).
- Under the monotone reading, 2Ψ(π − a₋) ≈ 9.3 ≈ 2c* (asm_check P4, measured), which would be too weak by a factor 2. That reading is not the one proved.
- **Wording defect in TUNNEL_LOWER2 §4.** It says "g ≥ μ(1−c₁)(1−c₂)e^{−√βΨ(a₁)} on the tube core". It should say e^{−√β min(Ψ(a₁), Ψ(π−a₁))}. Its §5 uses 2Ψ(π/2), which is the correct value.
- **Independent 1D check (child T160, rerun by me).** −log m/√β = 3.936, 4.182, 4.335, 4.432 at β = 64, 256, 1024, 4096, rising towards c* and not towards 2c*. (−log g(π/2) + log g(0))/√β → c*/2, with 2q/r = 0.989 → 0.996.
  - My own independent code (onedflux.py: matrix squaring plus the flux identity (I0), not eigenvalue subtraction) reproduces r at β = 64 and 256 to all printed digits.
- Verdict: FITS (c*).

**Chain x → σx (C4, FITS AFTER STATED CHANGE; written here, not in any part).** Corollary B (PATHS §2.1) needs, for every x ∈ S, centres c₁(x), …, c_{n−1}(x) with consecutive distance ≤ d/√β in each link, and a lower bound on g and on T on the balls B(c_k, ρ_B/√β). HARNACK §2 proves chains from x to points of a corner, not to σx. PATHS §4 tags the x → σx geometry CLAIMED. The construction, for x in the corner (0, 0) (the other corners by σ₁, σ₂):
1. HARNACK phases 0 and 1 run from x to (U₁⁰, 1), where U₁⁰ = e^{a n̂} with a = a₁(x) < a₋.
   - Phase 0: V is nonincreasing from V(x) ≤ 1, in O(β^{1/4}) steps.
   - Phase 1: V ≡ 0, in ≤ a₋√β/d + 1 steps.
2. The valley segment, with U₂ = 1 and U₁(t) = e^{t n̂} for t from a down to a − π. Its end point is e^{(a−π)n̂} = −U₁⁰.
   - The class angle runs a → 0 → π − a, monotonically after 0.
   - V ≡ 0 and the length is π, so ≤ π√β/d + 1 steps.
3. σ₁ applied to the reverse of step 1, which runs from (−U₁⁰, 1) to σ₁x.
- **Steps:** n ≤ (π + 2a₋)√β/d + O(β^{1/4}) = O(√β). Centres depend measurably on x, since the phase-0 rotation is an explicit function of (U₁, U₂).

**Lower bounds on the balls.**
- *Balls around step 1 and step 3 points, and around valley points with a₁ ∉ [a₋, π − a₋].* By HARNACK's (infl), V ≤ 2(1 + 2ρ_B + ρ_B²)² on these balls, and a_i ≤ π/2, after σ₁ where needed. So they lie in D_{M'} ∪ σ₁D_{M'} with M' fixed, and HARNACK gives g ≥ μ' with −log μ' ≤ 35(a₋ + r₀)√β + O(β^{1/4}).
- *Balls around valley points with a₁ ∈ [a₋, π − a₋].* For z in the ball:
  - q ≤ |u₂|² ≤ ρ_B²/β, so βα(S)q/2 ≤ √2(1 + ρ_B²/β)ρ_B² ≤ 1.5ρ_B². asm_check P3: the maximum ratio is 1.398 over 3 × 20000 samples, met 3/3.
  - a₂(z) ≤ ρ_B/√β < r₀.
  - So z ∈ supp φ, and G − c₁ ≥ e^{−1.5ρ_B²} − e^{−M²} ≥ e^{−1.5ρ_B²}/2 (since M² ≥ 2ρ_B²). Also E − c₂ ≥ e^{−θ₀ρ_B²/(2ℓ√β)} − c₂ ≥ ½.
  - Hence, by §2 and §3, g(z) ≥ φ(z) ≥ (μ/4)e^{−1.5ρ_B²} e^{−√β min(Ψ(a₁), Ψ(π−a₁))} ≥ (μ/4)e^{−1.5ρ_B²}e^{−√βΨ(π/2)}.
  - Points of such a ball with a₁ just outside [a₋, π − a₋] are covered by the previous bullet.
- *T_min.* For consecutive ball points the link distance is ≤ (d + 2ρ_B)/√β and V ≤ V_max (bounded). HARNACK (k_min) gives T ≥ e^{−V_max}(√(2/π)β^{3/2}e^{−(d+2ρ_B)²/2})², which is polynomial.
- *Other Corollary B inputs.* sup g ≤ k_sup²/λ = O(β³) (HARNACK (sup)). v ≍ β^{−3}. n = O(√β).

**Conclusion of (4) via Corollary B.**
 −log Δ ≤ 2 sup_{balls}(−log g) + O(log β) − log(2∫_S f²) ≤ √β·2Ψ(π/2) + 70(a₋ + r₀)√β + O(β^{1/4}) − log(2∫_S f²).

## 5. Interface (5): ∫_S f², and Lemma L4 (new; replaces the sketches)

- **Form used.** ∫_S f² ≥ ½ for β ≥ β₀(η).
- **Form proved.** Lemma M4 (TUNNEL_LOWER2 §3) gives
 ∫_{C_η∩{V≤1}} f² ≥ 1 − (1 − λ_eo)/(1 − e^{−1}) − 2C(η)e^{−2√βφ_min(η)}.
 It needs (B) for f, and (B) needs Lemma F (PROVED) and λ_eo ≥ e^{−η/4}. Until now λ_eo ≥ e^{−η/4} and λ_ee ≥ e^{−η/4} were sketches (TUNNEL_THEOREM §4, TUNNEL_LOWER2 §3; HARNACK says "not rechecked").

**Lemma L4 (PROVED here).** λ_ee ≥ L_β and λ_eo ≥ L_β − ε_β, where
 L_β := e^{−2βr⁴}[(v(r−t)/v(r)) P_k(θ ≤ t)]², ε_β := 2v(r)² k(π − 2r) k_sup,
with r = β^{−1/3}, t = β^{−5/12} and v(r) = (2r − sin 2r)/(2π). Here L_β → 1 and ε_β ≤ e^{−β(1 − o(1))}.

*Proof.*
- Let B_r be the geodesic ball about 1 in SU(2), and b_c = 1_{B_r}(±U₁)1_{B_r}(±U₂) for the four corners c. Each b_c is gauge invariant.
- On B_r × B_r, V ≤ 2β sin²a₁ sin²a₂ ≤ 2βr⁴.
- ⟨b, Tb⟩ ≥ e^{−2βr⁴}⟨b, K₁K₂b⟩ = e^{−2βr⁴}Π_i ⟨1_{B_r}, K_i1_{B_r}⟩.
- For each link, by the triangle inequality d(Ug, 1) ≤ d(U, 1) + θ(g): ⟨1_{B_r}, K1_{B_r}⟩ ≥ ∫_{B_{r−t}}P(θ ≤ t) = v(r−t)P(θ ≤ t).
- Dividing by ‖b‖² = v(r)² gives λ_ee ≥ ⟨b, Tb⟩/‖b‖² ≥ L_β.
- For λ_eo take u = b₀₀ + b₀π − b_π0 − b_ππ, which is σ₁-odd and σ₂-even, with ‖u‖² = 4v(r)².
  - Cross terms between corners with the same U₁-corner carry sign + and are ≥ 0.
  - The 8 ordered cross terms between different U₁-corners are each ≤ v(r)²·sup T ≤ v(r)⁴k(π−2r)k_sup, because U₁ and U₁' are at distance ≥ π − 2r.
  - Hence λ_eo ≥ L_β − 2v(r)²k(π−2r)k_sup.
- L_β → 1 because βr⁴ = β^{−1/3} → 0, t/r = β^{−1/12} → 0, and t√β = β^{1/12} → ∞, so P_k(θ ≤ t) → 1 (θ√β is asymptotically χ₃). ∎

*Numerics (asm_check).*
- P1 met 3/3: the single-link inequality against Monte Carlo at β = 256, 4096, 65536.
- **P2 FAILED (my expectation, not a defect).** I predicted 1 − L_β < 0.05 at β = 10¹⁶. Measured: L_β = 0.014, 0.096, 0.31, 0.53, 0.75 at β = 10⁴, 10⁶, 10⁹, 10¹², 10¹⁶. The rate is about β^{−1/12}, so L4 is a pure o(1) statement and gives no usable β₀. That is enough for the limit, but no numerical β₀ follows from it.

With L4, M4 gives ∫_S f² ≥ 1 − o(1) ≥ ½, and m_B ≥ ¼ − o(1) for g. FITS (C5: L4 replaces the sketches).

## 6. Interface (7): parameters and the order of limits

| parameter | constraint (source) | choice |
|---|---|---|
| η | 0 < η, Lemma F η/2-form (LEMMA_F), (B) η/4-form | free; → 0 last |
| a₋ | ε(sin a₋) = 2η (TUNNEL_LOWER2); a₋ ≤ π/4 (HARNACK) | arcsin(sinh η); a₋ ≤ π/4 for η ≤ 0.65 |
| η' | η' ≤ a₋ (this file, C1); η' > 0 (E13) | η' = a₋ |
| r₀ | r₀²/sin a₋ ≤ η/4 (S4-alg); r₀ + 0.1 ≤ π/2 (E13) | √(η sin a₋/4) |
| ℓ, θ₀ | 0 < ℓ < r₀/2 (TUNNEL_LOWER2) | r₀/3, ½ |
| M | c₁ = e^{−M²} ≤ G_min(e^{η/2}−1)e^{−C}/4 (S4-alg); M² ≥ 2ρ_B² (§4) | M² ≈ 3.4/η + O(1) |
| K | M4, HARNACK m_B | 1 |
| d, ρ | HARNACK | 3.65, 0.265 |
| Lemma K's η, E13's L | β-dependent (β^{−1/8}, √(C log β)) | as in sources |
| β | β ≥ β₀(η, all above): Δ₁, Δ₃ ≤ η/4; λ ≥ e^{−η/4}; Lemma F | → ∞ first |

asm_check P5 (met 6/6 and monotone) confirms that the constraints are consistent for η ∈ {0.4, …, 0.01}. Consistent choice: YES.

## 7. The linear proof

1. Fix η. Choose the parameters of §6.
2. Lemma L4 gives λ, λ_eo ≥ e^{−η/4}. Then (B) (TUNNEL_THEOREM §4, and for f by TUNNEL_LOWER2 §3) and M4 give ∫_S f² ≥ ½ and m_B ≥ 1/8.
3. HARNACK H4 gives g ≥ μ on D_M ∪ σ₁D_M, with −log μ ≤ 35(a₋ + r₀)√β + o(√β).
4. Lemma F gives ‖T_ΩΩ‖ < λ. (E1) and (E3) (E13, with C1) and (E2) (Lemma K, with C2 and C3) feed S4-alg, which gives Tφ ≥ λφ on Ω for φ = max(φ_L, φ_R).
5. Lemma C gives g ≥ φ on X.
6. The chain of §4 (C4) and Corollary B (PATHS) give −log Δ ≤ √β c*(η) + 70(a₋ + r₀)√β + o(√β).
7. m_eo ≥ Δ, and c*(η) ≤ c* + π√(2η) (L3, Lean in TUNNEL_LOWER). So limsup (−log m_eo)/√β ≤ c* + π√(2η) + 70(a₋ + r₀) for every η. Since a₋, r₀ → 0 as η → 0, **limsup ≤ c***. ∎ (conditional as stated in the first line)

## 8. Interface verdicts

| interface | verdict |
|---|---|
| (1) sets K / Ω / S / D_M | FITS AFTER C1 (η' ≤ a₋) |
| (2) Lemma C from S4-alg + E13 + Lemma K | FITS AFTER C1–C3 |
| (3) μ from HARNACK | FITS (M fixed = M(η); HARNACK's M² = O(log 1/η) is wrong, harmless) |
| (4) chain x → σx; factor c* | FITS AFTER C4 (chain written here); the factor is c* via the tent (max). Fix the wording of TUNNEL_LOWER2 §4 |
| (5) ∫_S f² | FITS AFTER C5 (Lemma L4 proved here) |
| (6) m ≥ Δ/λ | FITS |
| (7) parameters and order of limits | FITS |

Two further changes, C6 and C7:
- **C6 (wording).** Replace "e^{−√βΨ(a₁)}" by "e^{−√β min(Ψ(a₁), Ψ(π−a₁))}" in TUNNEL_LOWER2 §4.
- **C7 (statement).** Add 0 ≤ Ψ' ≤ √(2(ε+η)) on the transition [a₋/2, a₋] to TUNNEL_LOWER2's ansatz. It is needed for 2Ψ(π/2) ≤ c*(η).

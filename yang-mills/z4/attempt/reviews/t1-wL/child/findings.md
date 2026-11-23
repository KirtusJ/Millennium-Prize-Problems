# Fidelity check of tun_lower.tex against parts/ (task T169, worker t1-wL child)

**Verdict: I found no WRONG item.** I checked every lemma, proposition, theorem and corollary of tun_lower.tex, and every numerical constant I could find. Every statement and constant either MATCHES the parts or is CHANGED. Each change is either justified by C1–C7 or a CHAL correction, or it is an unlisted change that I judge harmless. The unlisted changes are in the "Unlisted changes" section below, and the table marks them.

I share a model family with the authors, so this is not independent review. No Lean file was compiled. No network was used.

- **Control:** `control.txt` = 1.570796 (π/2).
- **Not checkable here:** `parts/` contains no TUNNEL_THEOREM.md and no LEMMA_F.md. The statements tex cites from the first half (Lemmas U-kernel, U-K, U-R, U-F, Proposition U-B, Theorem U-main) are therefore **not compared**. The (B) form in §6, the e^{−3η/2} Lemma F step, and "liminf ≥ c*" are compared only through how TUNNEL_LOWER2, CHAL_assembly and CHAL_conditional restate them.
- **Source key:** FULL = TUNNEL_LOWER_FULL.md. L1 = TUNNEL_LOWER.md. L2 = TUNNEL_LOWER2.md. E13, HARN = HARNACK.md, PATHS. CP = CHAL_parts.md, CA = CHAL_assembly.md, CC = CHAL_conditional.md.

## 1. Table

| # | item (tex line) | source | verdict | evidence |
|---|---|---|---|---|
| 1 | Lemma L-flux (I0), l.18–21 | L1 §1 (I0) | MATCHES | Both read Δ⟨f1_A,g⟩ = ∫_{A×A^c}T[f(x)g(y)−f(y)g(x)]. Tex adds the hypothesis X = A⊔σA, which is harmless. |
| 2 | (I1), l.22 | L1 §1 (I1) | MATCHES | Both read Δ ≥ 2∬_{ff<0}T\|f\|\|f\|. Both use λ = sup spec. |
| 3 | (I2), l.23–27 | TUNNEL_THEOREM §5 (not in parts), L1 l.113, CC item 10 | **CHANGED, justified by CC #10** | Prefactor 2 → **4**. Tex proves it: ½∬(s−s′)²gTg, with 1−ss′ = 2 on both cross blocks, gives 4⟨g1_A,Tg1_{A^c}⟩. L1 reports the factor-2 version failing at ratio 0.655–0.699. Tex adds the assumption s∘σ = −s, which is not needed. |
| 4 | Lemma L-GS, E(h) = Δ, l.57 | L1 (GS), PATHS §0 | MATCHES | Same E(h) = ½∬Tgg(h−h′)². |
| 5 | Lemma L-C (Comparison), l.70 | L1 Lemma C, FULL §2 | MATCHES | The hypotheses (i)–(iii) are the same. The conclusion is "a.e. on Ω, everywhere by continuity", as in FULL §2. The Neumann-series proof is the same. |
| 6 | Lemma L-Pc (P′c), l.89 | PATHS §1 | MATCHES | Both read Δ ≥ 2∫_S f²/(nρ). Both use off-diagonal domination. Both use 4h(x)² ≤ nΣ(Δh)², with 2nρE(h) at the end. |
| 7 | Corollary L-B (Cor B), l.118 | PATHS §2.1 | MATCHES | ρ ≤ n·sup_S g²·max(1/v,\|S\|/v²)/Q_min. Same Δ-bound and log form. Tex states that the inf g is taken over the balls and over S (the end points). PATHS has Q_min ≥ T_min(inf_balls g)² and says "balls" only. That is a clarification, not a change. |
| 8 | Scalar facts (L2), (L3), l.156–159 | L1 l.46–47 | MATCHES | c*(η) ≤ c* + π√(2η). |
| 9 | Lemma L-L4 (L4), l.181 | FULL §5 (C5) | MATCHES | L_β = e^{−2βr⁴}[v(r−t)/v(r)·P_k(θ≤t)]², ε_β = 2v(r)²k(π−2r)k_sup, r = β^{−1/3}, t = β^{−5/12}. Both have 8 ordered cross terms and ‖u‖² = 4v². My program P6 reproduces the printed L_β = 0.0138, 0.0965, 0.308, 0.531, 0.752 against the tex's 0.014, 0.096, 0.31, 0.53, 0.75. |
| 10 | Lemma L-M4, l.238 | L2 §3 | **CHANGED, unlisted, notation only** | The bound 1 − (1−λ)/(1−e^{−K}) − 2C(η)e^{−2√βφ_min} is the same. L2 bounds ‖e^{√βΦ}u‖ ≤ C(η). Tex bounds the square, ‖e^{√βΦ}u‖² ≤ C(η), and says so at l.258–259. If C bounded the norm, the error term would be 2C². Harmless. K is renamed ϰ. |
| 11 | Lemma L-tangent, l.266 | L2 §1 | MATCHES | δa_i = X_i^∥, δ_i = R(a_i)X_i^⊥, the 2+2+2 split, and the co-isometry. |
| 12 | Ansatz Ψ with χ, l.300–302 | FULL §2 C2 | MATCHES (C2 applied) | Ψ′ = χ√(2(ε+η)), with χ = 0 on [0,a₋/2]∪[π−a₋/4,π] and χ = 1 on [a₋,π−a₋/2]. L2 had "Ψ′ = √(2(ε+η)) on [a₋,π−a₋/2], flat after". |
| 13 | Ansatz Θ̃, l.303–305 | FULL §2 C3 | MATCHES (C3 applied) | Θ̃ = Θ on [0,π/2], Θ̃′ = 0 near π, 0 ≤ Θ̃′ ≤ θ₀. |
| 14 | Lemma L-ansatz-props (i)–(v), l.314 | FULL §2 C2/C3/C6/C7, L2 §2 | CHANGED, justified by C2, C3, C6, C7 | (i) adds 0 ≤ Ψ′ ≤ √(2(ε+η)) everywhere (C7). (iv) is the tent min(Ψ(a₁),Ψ(π−a₁)) (C6). (iv) also says "φ ≤ μ everywhere", where L2 says "off Ω". This is true because every factor is ≤ 1, so it is harmless. (v) is 2Ψ(π/2) ≤ c*(η) ≤ c* + π√(2η). |
| 15 | Tube 𝒯 with η′ = a₋, l.355–359 | FULL §1 C1, E13 §0 | MATCHES (C1 applied) | E13 had K with a₁∈[η′,π−η′] and η′ = 0.5. Tex takes η′ = a₋. Then 𝒯 ⊇ Ω∩{a₁≤π/2}. |
| 16 | (E1), (E2), (E3), l.363–372 | L2 §2 | MATCHES | A₁ = exp(−e(S) + ½(Ψ′²+Θ′²) − Δ₁), A₂ = exp(−V/2 + ½(Ψ′²+Θ′²) + Δ₂), A₃ = exp(−e(S) + ½Ψ′² + Δ₃). Tex says (E2) holds on all of X. That is correct, because the proof only drops e^{−V′/2} ≤ 1 and Lemma K applies globally after C2 and C3. |
| 17 | Lemma L-exact (a)–(f), l.376 | E13 §1 | MATCHES | D_β, the ball density bounds, \|ρ_ξ\| ≤ 2r_b²\|w\| + (r_b+r_b²)², and G1, G2. ϱ replaces ρ. My program P7: G1 = 3e−16, G2 = 1e−16, flat identity = 3e−15. |
| 18 | Lemma L-taylor (Err), l.431 | E13 §2 | MATCHES | m, r, E_W, B_W, ΔS², Δh ≤ ΔS²/(2σ₋²√(1+1/σ₋)) are all identical. |
| 19 | Lemma L-gauss, l.460 | E13 §3 | MATCHES | The log J formula, DG1 and DG3 are the corrected version, with 1/σ_w² in the cross term. My program P7: the closed form agrees with the direct determinant completion to 6.4e−14 on 200 random points. |
| 20 | Lemma L-tails, l.500 | E13 §4 | MATCHES | Tail ≤ e^{\|p\|²/2}ΣP(χ₃>L−\|p_i\|), and the same Q bound. |
| 21 | Proposition L-E13, l.525 | E13 §5, FULL §1 C1 | CHANGED, justified by C1/C2 | Δ₁ and Δ₃ and the rate (log β)^{3/2}β^{−1/2} are as in E13. The hypothesis (H1) "C² near [η′−0.1, π−η′+0.1]" is replaced by global smoothness (ansatz-props (i),(ii)). FULL says "C² on a neighbourhood of [η′/2, π/2+η′/2]". Tex is stronger as a hypothesis and is satisfied by the ansatz. Tex adds the CA wording fix: s₋⁻⁴ and h(s₋) also enter. |
| 22 | Lemma L-E2, l.566 | L2 §2 (E2), CC item 7 | MATCHES (CC #7 applied) | Δ₂ = O(β^{−1/4}) by Lemma K at parameter β^{−1/8}. The Taylor line cosh(√β(p·X+R)) ≤ cosh(√β p·X)e^{√βHθ²/2} is the line that CC #7 lists as missing. |
| 23 | Lemma L-S4 (S4-alg), l.592 | L2 §2, FULL §2 | CHANGED, justified by FULL §2 "absorption re-proved" | Eq. (cutoff) and the ring identity are the same. L2 has A₁−λ ≥ e^{3η/4−o(1)}−1 and c₁ ≤ G_min(e^{3η/4}−1)e^{−C}/4. Tex and FULL have A₁−λ ≥ e^{η/2}−1 and c₁ ≤ G_min(e^{η/2}−1)e^{−C}/4. This needs Δ₁ ≤ η/4 (tex: Δ₁+Δ₃ ≤ η/4, Δ₂ ≤ 1, a stricter hypothesis). G_min = exp(−(√2/sin a₋)(e(√2)+1)) and C = e(√2)+η+θ₀²/2+1 match FULL. The "3/4" is kept in A₁−λ ≥ e^{3η/4−Δ₁}−1. My program P9 reproduces the slacks: min slack 0.1088, 0.1077, 0.0952, 0.0488, 0.0100 at η = 0.4, 0.2, 0.1, 0.05, 0.01, against the tex's claimed 0.107, 0.107, 0.095, 0.049, 0.0100. The slack is ≥ 0 everywhere on my grid. The last two absorption bullets stay qualitative, as in L2 and as the tex status says. |
| 24 | Lemma L-norm, l.655 | L2 §2, FULL §2, CA | MATCHES | ‖T_ΩΩ‖ ≤ sup‖F_{a₁}‖ ≤ e^{−2η+η/2} = e^{−3η/2} < λ. λ > e^{−3η/2} comes from L4 (C5), which replaces the sketch λ ≥ 1−O(β^{−1/3}). |
| 25 | Proposition L-sub, l.673 | FULL §2, L2 §2 | MATCHES | The proof by Lemma C, the tent via max(φ_L,φ_R), and μ ≤ inf_{R_well} g. |
| 26 | Lemma L-elem, l.697 | HARN §0 | MATCHES | (sup), (I₁ up) with ratio ≤ 2/π, (k_min) with √(2/π)β^{3/2}e^{−R²/2}, (vol) v(r) ≥ 11r³/(24π), (infl). My program P8: min v(r)/(11r³/24π) = 1.384 on (0,½], and I₁/bound = 0.332 … 0.6366 for z = 1 … 10⁴. |
| 27 | Lemma L-chain, l.720 | HARN §1 Lemma Ch | MATCHES | c_ch(K′) = K′ + R² + log(π/2) + 2log(24π/(11ρ³)), R = d+2ρ. |
| 28 | Lemma L-geom, l.740 | HARN §2 | MATCHES | Phases 0–3 with step counts n₀ = ⌈(π/2)√M β^{1/4}/d⌉, ⌈a₂√β/d⌉, ⌈(a₁+a_*)√β/d⌉, ⌈a_*√β/d⌉. K_M = 2(M+2ρ+ρ²)², K₀ = 2(2ρ+ρ²)², K_ϰ = 2(√(ϰ/2)+2ρ+ρ²)². |
| 29 | Theorem L-H4, l.769 | HARN §3 | MATCHES | g(x) ≥ (λm_B/k_sup²)k_min²e^{−M²−ϰ/2}exp(−n₀c(K_M)−n₁₂c(K₀)−n₃c(K_ϰ)). β ≥ max(1,4ρ²), ρ ≤ ½. |
| 30 | Corollary L-H4cor, l.787: constants 35, 8.35, 9.09, d = 3.65, ρ = 0.265 | HARN corollary, FULL §3 | MATCHES (constants), CHANGED (M² remark) | The grandchild T171 and I both recomputed: min l(K₀)/d = **8.345845** at d = 3.645066, ρ = 0.263929 (interior of [1,5]×(0,½]). At (3.65, 0.265): l(K₀)/d = 8.345877 and l(K_ϰ)/d = **9.084971**. Tex's 8.35 and 9.09 are upper roundings, so they are valid. 9.09 is the value at the (3.65, 0.265) point and is **not** the minimum of l(K_ϰ)/d: that minimum is 8.9846 at d = 4.08, ρ = 0.206. Tex says "program values" and takes d = 3.65 and ρ = 0.265, so it does not claim a minimum. 8.35·(2a₋+r₀) + 9.09a₋ = 25.79a₋ + 8.35r₀ ≤ 35(a₋+r₀), and 8.35·3 + 9.09 = 34.14 ≤ 35 (my program P3). The "M² = O(log 1/η) is wrong, M² ~ 1/η" correction is FULL §3's DEFECT note, not one of C1–C7. |
| 31 | m_B ≥ 1/8, m_B ≥ ¼ − o(1) | FULL §3, §7 | MATCHES | Same values. |
| 32 | Parameter list, l.814–825, and the order of limits | FULL §0, §6 | MATCHES | a₋ = arcsin(sinh η), r₀ = √(η sin a₋/4), ℓ = r₀/3, θ₀ = ½, ϰ = 1 (FULL "K := 1"), ρ = 0.265, d = 3.65, ρ_B = ½, η′ = a₋. My program P2 and P4: r₀²/sin a₋ = η/4 to 1e−12; a₋ ≤ π/4 for η ≤ 0.4. The threshold "a₋ ≤ π/4 for η ≤ 0.65" is true: arcsin(sinh 0.65) = 0.7709 < π/4, and arcsin(sinh 0.66) = 0.7880 > π/4. FULL's "M ≈ 3.4/η" is dropped from tex. |
| 33 | Remark on M, l.833–836 | FULL §4 ("since M² ≥ 2ρ_B²") | **CHANGED, unlisted, repair** | FULL infers e^{−1.5ρ_B²} − e^{−M²} ≥ e^{−1.5ρ_B²}/2 from M² ≥ 2ρ_B², which is false: 0.081 against 0.344 at M² = ½. I confirmed both numbers. Tex repairs the argument by using the c₁ condition. My program P5 gives M² = **18.05** at η = 0.4 (tex says 18.0). FULL's own table (14.8, 23.4, …, 339) does not match my recomputation: η·M² = 7.2, 6.7, 6.1, 5.4, 5.1, 4.8, 4.8, 4.7 at η = 0.4 … 0.005. FULL's "3.4/η" is not what the c₁ condition gives. Tex dropped it. The statement is the same. |
| 34 | Chain x → σx, l.846–858 | FULL §4 (C4) | MATCHES (C4) | Steps 1–3, n ≤ (π+2a₋)√β/d + O(β^{1/4}). |
| 35 | Lemma L-balls, l.860 | FULL §4 | MATCHES | Same bound min(μ′, (μ/4)e^{−1.5ρ_B²}e^{−√βΨ(π/2)}), and the same 1.5. Tex's own status adds that the step "a₁ just outside [a₋,π−a₋] is covered by the first case" is not written out. FULL and CA state it as covered, and CA marks STANDS. Tex's "Proved" status line is therefore stronger than its text for that step. |
| 36 | T_min and other inputs, l.887 | FULL §4 | MATCHES | The T_min formula, sup g ≤ k_sup²/λ, v ≍ β^{−3}. |
| 37 | Theorem L-main, l.893 | FULL §7 | MATCHES | limsup ≤ c* + π√(2η) + 70(a₋+r₀). −log Δ ≤ √β·2Ψ(π/2) + 70(a₋+r₀)√β + O(β^{1/4}) + O(log β). |
| 38 | Corollary L-limit, l.918 | FULL line 1 | MATCHES | Conditional on liminf ≥ c* from TUNNEL_THEOREM (not in parts). Tex says "as for the two theorems it combines". |

## 2. Constants

| constant | tex | source | verdict |
|---|---|---|---|
| c* | 4.6054132 | task text | MATCHES. My P1: 4.605413245. |
| 35 | l.792 | HARN, FULL | MATCHES. |
| 70 | l.902 | FULL §7 (2×35) | MATCHES. |
| 8.35 | l.802 | HARN | MATCHES. Grandchild and I: 8.3458. |
| 9.09 | l.802 | HARN | MATCHES, as an upper rounding. The value is 9.0850 at (3.65, 0.265), 9.0838 at the argmin of (a), and 9.085 per HARN's own recomputation. |
| 1.5 (in 1.5ρ_B²) | l.871 | FULL §4 | MATCHES. √2 ≤ 1.5. |
| 3/4 (in e^{3η/4−Δ₁}) | l.622 | FULL §2 | MATCHES. |
| η/4 (r₀²/sin a₋ and D, Δ₁+Δ₃, λ ≥ e^{−η/4}) | various | FULL §0, §2 | MATCHES. Tex uses Δ₁+Δ₃ ≤ η/4 where FULL uses Δ₁ ≤ η/4. This is a stricter hypothesis, and the tex discloses it. |
| e^{η/2}−1 in the c₁ condition | l.602 | FULL §2 | CHANGED from L2's e^{3η/4}−1, justified by FULL §2. |
| e^{−3η/2} | l.656 | FULL §2 | MATCHES. |
| L_β exponents (β^{−1/3}, β^{−5/12}, 2βr⁴) | l.182–186 | FULL §5 | MATCHES. P6 reproduces the printed numerics. |
| r₀, ℓ, θ₀, M, ρ, d, ρ_B | l.814–825 | FULL §0 | MATCHES (ρ_B = ½ and M² ≥ 2ρ_B² as in FULL; see row 33 for M). |
| P1 ratio 0.655–0.699 | l.51 | L1 l.113 | MATCHES. I cannot recompute it here. |
| slack 0.107, 0.107, 0.095, 0.049, 0.0100 | l.647 | not in parts (asm_check results) | Reproduced as ≥ by my P9. |
| sup Δ₁ = 13.8 at β = 16384, 0.17 at 2.7·10⁸ | l.555 | E13 §6 | MATCHES. |

## 3. Unlisted changes (not in C1–C7 or the CHAL files)

All of these are harmless, and the tex discloses most of them.

1. M4 convention: C(η) bounds the squared norm (row 10).
2. Remark on M: the c₁ condition replaces the false inference from M² ≥ 2ρ_B² (row 33).
3. S4-alg hypothesis Δ₁+Δ₃ ≤ η/4 with Δ₂ ≤ 1, in place of FULL's Δ₁ ≤ η/4 (row 23).
4. "φ ≤ μ everywhere" in place of "off Ω" (row 14). It is true because every factor is ≤ 1.
5. Prop L-E13 takes global smoothness as its hypothesis in place of (H1) (row 21).

Status wording to watch: Lemma L-balls and Lemma L-tangent are marked "Proved", but the tex status text for L-balls admits one unwritten step. The tex also marks S4-alg's last two absorption bullets as qualitative only. FULL and the CHAL files record both as stated but not written out.

## 4. Programs, predicates and failures

`fid_check.py` has its predicates fixed in the docstring before the first run. It has fixed seed 12345 and its result file is opened with mode "x".

- **run1:** exit 1 with `ValueError: math domain error`. G_min underflowed at η = 0.005 in the P5 computation. This was a defect in my program, not in the target. I fixed it with a log-domain formula and left the predicates unchanged.
- **run2** (`results_fid_run2.txt`): P1, P2/P4, P2b, P3, P5, P6, P7, P8 and P9 all MET.
- **Tolerances:**
  - P1: 5e−8, from the 7 printed decimals.
  - P6: the rounding of the printed digits.
  - P7: double precision.
- **P5 and P9 notes:**
  - P5's predicate was only M² ≥ 1.5ρ_B² + log 2. The comparison to the tex's 18.0 is reported, not a predicate.
  - P9's comparison to the claimed slack numbers is reported, not a predicate. The grid is not specified in the tex.
- **P9 not checked:** the corner claim "A₂/A₁ ≤ 0.006".
- **"For all" predicates (hypothesis tested per case first):** P2 ran 5 η values. P3 ran 3 inequalities. P5 ran 8 η values. P7 ran 200 random points. P8 ran 2000 radii and 5 z values. P9 ran 5 η values × 60 a₁ × 25 a₂ × 400 t × up to 12 y points. All cases qualified, because the formulas have no domain exclusions (σ_w² > 0 held on all sampled points).

## 5. Sub-agent

- **Grandchild T171.** Admitted with `task-admit … --label t1-wL-grandchild --parent T169`. Released with `task-release … --id T171` (event 342 in the graph).
- **Question:** min over d∈[1,5], ρ∈(0,½] of l(K₀)/d, and the K_ϰ value. This is the 8.35 and 9.09 check.
- **Control:** ∫₀¹x² = 0.333333, correct.
- **Predicates fixed in its docstring:** P1 control, P2 |min − 8.35| < 0.005, P3 |value − 9.09| < 0.005, P4 interior.
- **Outcome:**
  - It reported 8.345845 at (3.645066, 0.263929). P1, P2 and P4 passed.
  - **P3 failed.** The value at the argmin is 9.083837, and the failure is 0.0062. The cause is the grandchild's own 2-decimal expectation, not a defect in the target. HARN states 9.085, and the value at (3.65, 0.265) is 9.084971.
  - The grandchild also found the separate minimum of l(K_ϰ)/d, 8.984572 at (4.08, 0.206).
- **Reread and rerun:** I read `check.py` and `result.md`. I copied `check.py` into `rerun_gc/` and reran it under `pcp check` (K1, exit 0). Its `result.md` is identical to the grandchild's.

## 6. PCP OS record

- Register `pcp` was created with `$P init pcp --principal principal --principal-name "Kirtus Justus"`. It reported the method as not found, as expected.
- Checks:
  - K1 `gc-rerun`: exit 0.
  - K2 `fid-check-run1`: exit 1 (my defect, above; the expected exit was 0).
  - K3 `fid-check-run2`: exit 0.
- Last line of `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Last line of `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## 7. Rerun

```
cd /home/user/z4-workers/t1-wL/child
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
# fid_check.py writes results_fid_run2.txt with mode "x"; change the name to rerun
$P check --ws pcp --name fid-check-rerun --expect-exit 0 -- python3 fid_check.py
```

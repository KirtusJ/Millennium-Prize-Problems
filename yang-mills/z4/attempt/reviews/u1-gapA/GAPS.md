CLOSED: (1) W1 rho_eta, (2) W3 ftilde + constants, (3) Delta h in tu:L-taylor (+ propagation into tu:L-E13), (4) DG1/DG3 in tu:L-gauss. NOT CLOSED: none of the four assigned. All four tagged PROVED. W1 is stated in a weaker form (C^1 instead of smooth), which is all that is used.

# Gap closures, worker u1-gapA (task T173)

Patched files: `note/tun_upper_patched.tex` (gaps 1, 2) and `note/tun_lower_patched.tex` (gaps 3, 4).
Both compile together with `note/preamble.tex` through `build/wrap_patched.tex`: pdflatex exit 0, 29 pages, no undefined references.
The patch scripts `patch_upper.py` and `patch_lower.py` contain every old→new text pair. Each old string occurs exactly once.

## (1) W1: construction of ρ_η — PROVED

- **Label.** The item (W1) in §tu:U-sec-weight, plus a new Lemma `tu:U-W13`.
- **Old (W1).** √ρ_η smooth, ρ_η ≤ (ε−η)₊, ρ_η ≥ ε−2η for ε ≥ 3η.
- **New (W1).** √ρ_η ∈ C¹([0,∞)), ρ_η ≤ (ε−η)₊, ρ_η = 0 on [0, 3η/2], ρ_η ≥ ε−2η for ε ≥ 3η.
  - This is weaker in smoothness. Only C¹ is used: it makes f C² off π/2, which gives Φ ∈ C² and H < ∞ in Lemma tu:U-weight(2).
  - The new vanishing on [0, 3η/2] is a property of the construction, not an extra demand.
  - Symmetry under a → π−a is automatic, because ρ_η(ε(a)) depends on a only through ε.
- **Construction.**
  - Sm(s) = 3s² − 2s³ on [0,1], clamped to 0 below and 1 above (C¹).
  - ψ(t) = Sm(2(t − 1/2)/3).
  - g_η(ε) = √((ε−η)₊) · ψ((ε−η)/η), and ρ_η = g_η².
- **Bound.** |g_η'| ≤ 3/√(2η).
- **What changes downstream.** Lemma tu:U-weight(3) is unchanged and still goes through: it uses only the two inequalities. The second half's φ_min(η) > 0 holds because f̃ > 0 where ε > 3η/2.

## (2) W3: C² smoothing f̃ of the tent — PROVED

- **Construction.**
  - χ(a) = Sm((π/2 − a)/(τ/2)).
  - f̃(a) = ∫₀ᵃ f'·χ on [0, π/2], reflected to f̃(π−a) = f̃(a).
- **C² at π/2.** f̃'(π/2) = f̃''(π/2⁻) = 0, so the even reflection is C².
- **Properties.**
  - f̃ = f outside the τ-window.
  - 0 ≤ f̃' ≤ f'.
  - f − Lτ/2 ≤ f̃ ≤ f. This is better than the f − Lτ used in the note; the note's version is kept.
- **Constants.**
  - |f̃''| ≤ 6/√η + 3L/τ.
  - |f̃' cot a| ≤ L / sinh(3η/4).
  - Hence H ≤ (1−δ)·max(6/√η + 3L/τ, L/sinh(3η/4)) and |Φ'| ≤ L.
  - These are the constants that Lemma tu:U-weight(2) and the Schur step (P = L, H₀ = H) use. Only their finiteness matters downstream.

## (3) Δh in Lemma tu:L-taylor — PROVED; the stated bound is correct

- **What h is.** h(S) = 1 + √(1+S²)/S = 1 + √(1 + 1/σ) with σ = S².
- **The suspicion of a dimensional error is unfounded.** σ₋ = S² − ΔS² is a lower bound for S'², a value of S², not of S. The bound is the derivative bound |dh/dσ| = 1/(2σ²√(1 + 1/σ)), evaluated at σ₋. This is legitimate because that quantity decreases in σ.
- **Derivation.**
  1. ΔS² comes from x0' = x0·g0 − u·ξ.
  2. Then an elementary inequality without the mean value theorem: for 0 < σ₀ ≤ σ₁, √(1+1/σ₀) − √(1+1/σ₁) ≤ (σ₁−σ₀) / (2σ₀²√(1+1/σ₀)). This is Lean-checked as `delta_h`.
- **Explicit form, new equation `tu:L-dh-explicit`.** If r_b ≤ S/8, then Δh ≤ 4r_b/S² + 4√2·r_b²/S³ ≤ 5r_b/S². On 𝒯 this gives Δh ≤ 5r_b/s₋².
- **Propagated into Prop tu:L-E13.** The new equation `tu:L-err-explicit`, valid for L/√β ≤ s₋/8, is
  Err ≤ β^{-1/2} [ L(M+2L)²(2.2·h(s₋) + 6.4/s₋²) + L²(0.51(H_Ψ + H_Θ) + 0.03(Λ + θ₀)) ].
  - The old rate had s₋⁻⁴; it is now s₋⁻².
  - The "wording fix" status remark is updated to match.

## (4) DG1/DG3 in Lemma tu:L-gauss — PROVED, via an exact formula

- **Exact formula, new equation `tu:L-gap-exact`.** With A = 1 + 2hS², x = 4hW/A and D_w = 1 + 2hσ_w² = A(1−x) ≥ 1:
  gap = ½·log(1−x) + ½·log(1+hx) + hx|b|²/D_w + h|b|²(κ²/β − 2κ/√β)/D_w.
- **Derived bounds.** From the formula, gap ≤ DG1' ≤ DG1 and −gap ≤ DG3'(κ) ≤ DG3(κ).
  - DG3 holds for gap₃ with κ₃. The original text wrote "−gap ≤ DG3 with κ₃", which is right only for gap₃; this is now made precise.
- **Uniform bound on 𝒯, new equation `tu:L-gap-unif`.**
  |gap|, |gap₃| ≤ 2h₋κ̄M²/√β + h₋M²(2h₋ + 4h₋M² + κ̄² + 2)/β.
- **Lower bound on σ_w no longer needed.** σ_w² ≥ 0 always holds, since W ≤ S⁴/4 ≤ S²/2.

## Checks

| check | file | result |
|---|---|---|
| W1/W3 numerics (P1–P12) | `results/w1w3.txt` | all met. P4 failed against the docstring tolerance 1e-12 (own expectation; see report.md) |
| Δh, exact gap, DG bounds (Q1–Q8, H1–H3) | `results/gap_dh.txt` | all met, 0 failed, 2·10⁵ samples each |
| explicit Err constant (E1–E6) | `results/err_const.txt` | all met, 0 failed, 10⁶ samples |
| Lean scalar lemmas | `lean/GapA.lean` | exit 0; axioms: propext, Classical.choice, Quot.sound; no sorry |
| child grid check (A1–D2) | `child/report.md` | all met; I reran it and got byte-identical results |

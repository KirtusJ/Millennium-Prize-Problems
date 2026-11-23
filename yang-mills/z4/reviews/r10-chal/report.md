# r10-chal report: challenge of PROOF_FREE_BOUNDS.md (two-sided bound on C_b in free lattice Maxwell)

Control: control.txt = 0.272341 (−ln tanh 1).
Counts (met, failed, measured only): my program chal.py 13, 0, 1; Lean recompile 1, 0, 0; sub-agent (rerun by me) 3, 0, 0.
Overall: 17 items STAND, 1 DEFECT (wording of the Brillouin zone), 2 NOT CHECKED. **No wrong constant was found.** Every constant (2/ℓ⁶, D₄/|p|⁴, π|m|/b, 4π(6/a⁴+√3/a³), π/ℓ, a = 4t/ℓ, κ₃ = 3√3/ℓ, b₀, and the ℓ-powers in V and v) was rederived and passed.

## 1. Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| Sec. 0, "BZ = representatives with \|k_i b\| ≤ π" | **DEFECT** (wording) | For even N, read literally this counts k_i b = +π and −π (the same mode) twice. Doing that at t = 0.1 gives C_b off by +170 % (N = 6) and +95 % (N = 8) (Q1b). The text should say "each mode once, e.g. −π < k_i b ≤ π". The proof's own numerics (agreement 5·10⁻¹⁵) must have counted each mode once. No bound is affected: w and k̂ do not depend on which representative is used, and step 3c holds either way. |
| A1: momentum representation, factor 2/ℓ⁶, k+k′ mod BZ | STANDS | Rederived by hand: b⁶Σf f e^{iq·b(x−y)} = conj(f̂_b(q)) f̂_b(q) for real f, and f̂_b is (2π/b)-periodic. Numerically (Q1): N = 6, 8, 9, ℓ = 1 and 0.7, three values of t, plus two direct sums with no FFT (N = 6, 9). Worst relative error is 1.9·10⁻¹⁵ over 20 cases, with a non-symmetric f (max\|Im f̂\|/max\|f̂\| = 0.43, Q0). |
| A2: decay \|f̃(p)\| ≤ ‖Δ²f‖₁/\|p\|⁴ | STANDS | Δ²e^{−ip·y} = \|p\|⁴e^{−ip·y}, so the constant is 1 and the norm is L¹. On a 96³ grid the largest ratio \|f̃\|\|p\|⁴/D₄ is 0.68 (Q3). |
| A2: aliasing lemma, absolute convergence | STANDS | Σ\|p\|⁻⁴ converges in 3D, so the Fourier series converges absolutely and uniformly to the continuous f, and evaluating it at lattice points is legitimate. Numerically exact to 1.6·10⁻¹⁶ (Q2). |
| A2: (2a) \|q+2πm/b\| ≥ π\|m\|/b, including q_i b = ±π | STANDS | Per component: 2π\|m_i\|/b − π/b ≥ π\|m_i\|/b for m_i ≠ 0. At the boundary it reads π\|2m_i+1\|/b ≥ π\|m_i\|/b, so either representative works. Checked for m ∈ [−6,6]³, N = 4, 6, 8, 10 and both representatives; the minimum ratio is exactly 1.0, reached at m_i = −1 (Q5). |
| A2: (2a) F_b bound and (2b) \|f̂_b(0)\| bound | STANDS | Holds for N = 3…16 (Q4). For N = 3 the (2b) lower bound is negative (vacuous), which is consistent with b₀ < ℓ/3 for this f. |
| A3 (3a): Jordan, (2/π)\|k\| ≤ k̂ ≤ \|k\| | STANDS | Lean `jordan_khat` is 1-D; the lift to the 3-D norm is a one-line text step and is correct. |
| A3 (3c): directions of the inequalities, P₃₃ ≤ 1, BZ sum → ℤ³ sum | STANDS | w = P₃₃k̂/2 ≤ k̂/2 ≤ \|k\|/2, and e^{−tk̂} ≤ e^{−(2t/π)\|k\|} because k̂ ≥ (2/π)\|k\|. The map k ↦ n = ℓk/2π is injective into ℤ³∖0 and the added terms are ≥ 0. S_b ≤ (π/ℓ)Σ\|n\|e^{−4t\|n\|/ℓ} holds in 12 of 12 cases (Q8). |
| A3 (3d): lattice-sum lemma and the integral | STANDS | 4π∫r²(r+√3/2)e^{−ar}dr = 4π(6/a⁴ + √3/a³). The second term is (√3/2)·8π/a³ = 4π√3/a³ (my hand derivation; quadrature agrees to all printed digits, Q6). The lattice sum is ≤ G(a) for a = 0.2…10. G/sum runs from 1.26 to 5.9·10⁵ (Q7): it is very loose for large a, because e^{√3a/2} grows while the true sum decays like 6e^{−a}. |
| A3: factor_upper step, C_b ≤ (2/ℓ⁶)F_b²S_b² | STANDS | 12 of 12 cases (Q8). |
| A3: final V, including every power of ℓ | STANDS | 30 of 30 cases qualify (b ≤ b₀) and C_b(τ) ≤ V holds in all of them (Q9, ℓ = 1 and 0.7). Sub-agent, rerun by me: 27 of 27 qualify for ℓ = 0.5, 1, 2, and C_b, V and v all scale exactly as λ⁻², b₀ as λ (P1–P3). Dimensional check by hand: V ∝ ℓ⁻⁶·L⁶·ℓ⁻²·G(τ/ℓ)². |
| A4: the four kept pairs, P₃₃ = 1, weight κ²/4, count | STANDS | (k,−k) and (−k,k) are both in the ordered double sum, so the four ordered pairs are k ∈ {±e₁, ±e₂}·2π/ℓ and give 4·κ²/4 = κ². P₃₃ = 1 to 1e-15 along e₁ and e₂, and P₃₃ = 0 along e₃ (Q11). N ≥ 3 is needed: at N = 2, e₁ ≡ −e₁. |
| A4 (4b): κ_N increasing, endpoint minimum | STANDS | κ_N is strictly increasing for N = 3…400 and κ₃ = 3√3/ℓ (Q11). min_N κ_N²e^{−2tκ_N} ≥ m(t) for t = 0.05…2 (Q12). The concavity argument is correct. |
| A4 (4c): b₀ | STANDS | S₄(b/2π)⁴D₄ ≤ \|∫f\|/2 ⇔ b ≤ 2π(\|∫f\|/(2S₄D₄))^{1/4}. v ≤ C_b(2τ) in all 30 + 27 qualifying cases. |
| A5: spectral identification | STANDS (argument only), with an unstated hypothesis | B₃ is linear in a, a†, so (B₃² − ⟨B₃²⟩)Ω = (a†a† terms)Ω: pure two-photon, no vacuum part. The sector is finite-dimensional and O_bΩ lies in it, so it is in the domain. Two finite atomic measures with the same Laplace transform for all t > 0 are equal. Degenerate energies only add weights (at N = 6: 46225 ordered pairs, 77 distinct energies, M1). This is harmless because S5e's window filters by energy. **Unstated:** e^{−tH} must have HΩ = 0, i.e. the zero-point energy subtracted. STATEMENT's H as written has a positive zero-point energy, and H1's e^{−tk̂} already assumes the subtraction. The zero modes (k = 0) are removed by hand in the setting; k̂ = 0 only at k ≡ 0, so no other zero modes exist. The identification is not needed to apply S5e to the index set (k,k′); it is needed only to call the result the spectral measure. |
| A6: Lean file | STANDS | Recompiled (copy R9Bounds_copy.lean, check K3): exit 0. `#print axioms` shows only propext, Classical.choice, Quot.sound for all 5 declarations. "sorry" appears only in the header comment. See note 1 below the table. |
| A6: "S5 copied verbatim from HeatRegularized.lean" | NOT CHECKED | The original was not supplied. This does not affect validity, because the copied S5 compiles and is proved inside this file. |
| A7: theorem statement | STANDS, with a rewording | See note 2 below the table. |
| S₄ ∈ [16.3597, 16.5791] | NOT CHECKED | I used 16.5791 as given. |

Note 1, what `window_from_two_sided` states. It takes a finite index set, w ≥ 0, E ≥ 0, τ > 0, v > 0 and a sub-finset K with v ≤ Σ_K w_i e^{−2τE_i} and C(τ) ≤ V, and concludes v/2 ≤ Σ_{E_i ≤ log(2V/v)/τ} w_i e^{−2τE_i}. Sections 4 and 3 deliver exactly hK (K = the four pairs at time 2τ) and hV. What is NOT formalized: that w and E are the step-1 atoms, the inequalities of sections 2–4 themselves (beyond `jordan_khat` and `factor_upper`), and the spectral identification.

Note 2, the theorem statement (A7).
- "For all b ≤ b₀" should read: for every integer N ≥ max(3, ⌈ℓ/b₀⌉), with b = ℓ/N. b₀ ≤ ℓ/3 already forces N ≥ 3.
- v and V do not depend on b or N. F depends only on b₀, ‖f‖₁ and D₄.
- As τ → 0: v → (∫f)²κ₃²/(2ℓ⁶) and V ~ τ⁻⁸.
- As τ → ∞: v ~ (2π/ℓ)²e^{−8πτ/ℓ}, while V grows like e^{4√3τ/ℓ} even though C decays. So E₀ → (8π + 4√3)/ℓ, which is bounded but loose.
- f enters only through ‖f‖₁, ∫f and D₄, plus the hypotheses that f is real, periodic and C⁴. The width R has no hidden role in the general theorem. Section 6 uses a different, Gaussian-specific route: all aliases are positive, so f̂_b(0) ≥ A with no b₀ at all, and its b₀ = 1/8 serves only the F bound. The section-4c b₀ for R = 0.1 would be far smaller. These are two different sets of constants, and the text should say so.

## 2. Hypotheses used, and where each is stated

- H1 (D_t with normalization k̂/2, ℓ⁻³): from STATEMENT.md, taken as reviewed there; not rederived here (proof Sec. 0 and Sec. 7).
- H2 (Wick, 2b⁶ΣΣ f f D²): STATEMENT.md.
- H3 (f real, C⁴, periodic, ∫f ≠ 0): proof Sec. 0. Reality is used in step 1, C⁴ in the decay estimate, ∫f ≠ 0 in 4c.
- H4 (N ≥ 3): proof Sec. 0 and 4a.
- BZ with each mode counted once: implicit; the stated form is defective (table).
- HΩ = 0 (zero-point energy subtracted) and zero modes removed: implicit in H1 and STATEMENT ("zero modes removed"); not stated in the proof.
- S₄ upper bound: proof Sec. 0, from the earlier worker's program.
- b ≤ b₀: Theorem, Sec. 5.

## 3. Failed predicates

- Mine: none. Q1b was my expectation that the literal BZ reading disagrees with position space; it was met, and that is the wording defect above.
- Sub-agent: its first run (child K1) exited 1 against an expected 0. Numpy booleans could not be written to JSON. This was the sub-agent's own coding defect, not a defect of the target. The truncated files results_run1.json and results_run2.json are kept, and the run was repeated without changing any predicate (child K2).

## 4. What I did not check

- H1 itself (oscillator normalization of D_t).
- The S₄ enclosure.
- Byte-identity of the S5 copy with HeatRegularized.lean.
- A Fock-space computation of the spectral measure of O_bΩ (A5 is checked by argument only).
- N > 16 for the final bracket, and τ outside [0.05ℓ, 0.6ℓ].
- The Section 6 Gaussian table, apart from two hand spot checks (v(0.05) = 4.738·10⁻³ and V(0.05) = 1.720·10⁷, both reproduced).
- D₄ is taken as 1.01 × its 96³-grid value. The grid difference between 48³ and 96³ is 1.0·10⁻⁴ relative (Q10), which is where the 1 % margin comes from.

## 5. Delegated question and outcome

- **Question (child/):** the ℓ-scaling test of A3. For ℓ ∈ {0.5, 1, 2}, N ∈ {6, 9, 12} and τ ∈ {0.05, 0.1, 0.3}·ℓ, test C_b ∝ λ⁻², V and v ∝ λ⁻², b₀ ∝ λ, and the bracket v ≤ C_b(2τ), C_b(τ) ≤ V when b ≤ b₀.
- **Control question:** Σ1/n⁴ = π⁴/90; it answered 1.082323, which is correct.
- **What came back:** 3 met, 0 failed, 0 measured only. All 27 cases qualify (b₀ = 0.2197ℓ). The scaling errors are exactly 0, because λ is a power of 2. V/C_b ranges from 3.3·10⁶ to 1.3·10⁹ and C_b(2τ)/v from 5.9 to 563. Its PCP verify line: "result: PASS (…)".
- **My checks on it:**
  - I reread scaling.py and reran it (my check K2). The output, written to ./results_run1.json, is identical as JSON to child/results_run3.json.
  - Its C_b values agree with my independent code, e.g. N = 6, τ = 0.05: 8786.47 and 2116.93.
  - It shares my model family, so this is not independent review.

## 6. Commands to rerun

From C:/Users/donke/z4-workers/r10-chal, with PYTHONUTF8=1:

```
python -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name chal_run2 --expect-exit 0 -- python chal.py results_chal_run2.json
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name child_rerun2 --expect-exit 0 -- python child/scaling.py
cd C:/Users/donke/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean C:/Users/donke/z4-workers/r10-chal/R9Bounds_copy.lean
cd C:/Users/donke/z4-workers/r10-chal && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```

chal.py refuses to overwrite an existing result file. scaling.py picks the next free results_runK.json in the current directory.

PCP register (pcp): K1 chal_run1, K2 child_scaling_rerun, K3 lean_R9_recompile. The last line of verify:
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

Three controls of fixed form do not measure the instrument's sensitivity in general.

## Lean itself (run separately, on the deposited files)

Command: `export PATH=$HOME/.elan/bin:$PATH; cd /home/user/z4-lean && lake env lean <deposited path>`.
Toolchain `leanprover/lean4:v4.19.0` (Lean 4.19.0, commit 6caaee842e94), Mathlib `inputRev v4.19.0`
(rev `c44e0c8ee63ca166450922a373c7409c5d26b00b`). Outputs: `lean/Inheritance.out`, `lean/haar.out`,
`lean/*.err`, `lean/*.exit`.

| File | Exit code | `sorry` / `admit` / `axiom` / `native_decide` in the text | Errors | Warnings | `#print axioms` |
|---|---|---|---|---|---|
| `f2-lean/Inheritance.lean` | 0 (14 s) | none | none | none | 18 theorems, each `[propext, Classical.choice, Quot.sound]` |
| `b2-haar/haar.lean` | 0 (8 s) | none | none | 1: `haar.lean:29:44: unused variable hp` (in `b_at_zero`) | 12 theorems, each `[propext, Classical.choice, Quot.sound]` |

## What is pinned and what is not

- Pinned: 6 of the 18 theorems of `Inheritance.lean` and 5 of the 12 of `haar.lean`, the ones cited in the
  paper's section "Machine-checked parts". Not pinned: `scalar_step`, `exp_rpow_ratio`, `M_pos`, `accum_mul`,
  `S_quad`, `S_lower`, `S_eig_quad`, `S_norm_le`, `S_eig`, `B_step`, `P_step`, `pyth`, `reset_example` (the
  example of Remark 5.4, formalised but not mentioned in the paper); `c_w_lt`, `c_formulas_equal`,
  `c_second_at_zero`, `s_root`, `riccati_gives`, `B_crossing`, `B_sprime_lt`.
- The definitions `M` and `S` used by the pinned statements are not covered by a statement digest: a change to
  `def S` would leave the digest of `gated_main` unchanged. The file digests above do cover them, so a pin
  should be read together with the file digest.
- `gated_main` and `gated_main_norm` formalise the continuous form of Theorem 1.2 (as in the third draft:
  `S e lam (2*a)`, real `t`, `tau <= t`, a finite-dimensional real space with an eigenbasis). The fourth draft
  states Theorem 1.2 for a discrete step `A` with integers `m >= j >= 1`, and says the Lean statement is the
  special case `A = e^{-aH}` injective. The discrete proof of the fourth draft (the case `q = 0`, the spectral
  projection `E`) is not formalised.
- `b_at_zero` carries an unused hypothesis `hp : 0 < p` (Lean's linter warning). Nothing is wrong; the
  hypothesis can be dropped.
- `c_second_pos` assumes `w < 2`; the paper's proof supplies `w < 3/2` (`c_w_lt`). Consistent.
- This rerun is internal checking within one model family and one toolchain. It shows that the files compile
  and that the statements are the pinned ones. It does not show that the paper's proofs are correct.

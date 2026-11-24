# Pinned Lean statements (rerun of 24 November 2026)

This table replaces an earlier one whose last column held the instrument's name instead of its result. Every row below was re-run with
`/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos instrument mathematics.statement '<JSON>'`
(keys `source`, `theorem`, `pinned`). Binary SHA-256 `d7c33c865d7cf4dea569b6eadaca726455ef4aa997718ab97869259ffc07c388`;
`pcp-os` checkout at `92623fa`. Driver: `../attempt/reviews/mod-qa/scripts/run_pins.py`; full instrument output for every call:
`../attempt/reviews/mod-qa/lean/pins_run1.jsonl`.

What the instrument establishes: the text of the named theorem's statement, comments removed and white space
collapsed, has the pinned SHA-256, and three textual probes are clear (no `sorry`/`admit` before the next
declaration; the conclusion is not true by its form; no hypothesis is `False`). It reads text. It does not run
Lean, and it does not say that the statement means what the paper says.

## Sources

| File | Deposited path (under `yang-mills/z4/attempt/reviews/`) | SHA-256 of the file | Byte-identical to worker copy |
|---|---|---|---|
| `Inheritance.lean` | `refinement-inequality/Inheritance.lean` | `74e9337dd18a9095754967635c18817780679eed46c3d1e8f8ea5634114ddf2b` | yes (`/home/user/z4-workers/f2-lean/Inheritance.lean`; also `g2-fid/lean/Inheritance.lean`) |
| `haar.lean` | `haar.lean` | `47ff4a24b0fb9dae1d84b6592eb658113c9fd763ae4e7ce2a744586d3d0f2eec` | yes (`/home/user/z4-workers/b2-haar/haar.lean`; also `g2-fid/lean/haar.lean`) |

## Instrument results

| File | Theorem (qualified name) | SHA-256 of the statement (pinned) | Instrument against the pin | Exit | Probes (a) open proof, (b) trivial conclusion, (c) False hypothesis |
|---|---|---|---|---|---|
| `Inheritance.lean` | `F2Lean.xr_le` | `0fdb052bf308596533b146fa491ae971daa02e037164f97e1e483e47a554f689` | HOLDS: statement digest equals the pin | 0 | all three clear |
| `Inheritance.lean` | `F2Lean.scalar_step_pos` | `e5cfed59c66ec4c77d15ddb740ed16d8b925f7a744477334e61df79c889a7bf1` | HOLDS: statement digest equals the pin | 0 | all three clear |
| `Inheritance.lean` | `F2Lean.accum` | `82e3aec468ff1f9c3e627decfc5639310b05b5608892309a79bd28f80d3ad97e` | HOLDS: statement digest equals the pin | 0 | all three clear |
| `Inheritance.lean` | `F2Lean.accum_pos` | `48a390e90a72823659bca00a62aa500875bff64178e539b1646c35a7bf605d4d` | HOLDS: statement digest equals the pin | 0 | all three clear |
| `Inheritance.lean` | `F2Lean.gated_main` | `c4de12b0e8f8916ae29a8fefd8018af890603eafc526c1274bcc3958d4e39ad0` | HOLDS: statement digest equals the pin | 0 | all three clear |
| `Inheritance.lean` | `F2Lean.gated_main_norm` | `55ba27a55ad87f5f031a4744f3659d82a8e0c2eda6e57caedc0bc0e926ea59dd` | HOLDS: statement digest equals the pin | 0 | all three clear |
| `haar.lean` | `B2Haar.a_at_zero` | `7efdc3ccdd034f0663871ef3f39dc0c9ec235959da60ba5fdfd82932ea321d19` | HOLDS: statement digest equals the pin | 0 | all three clear |
| `haar.lean` | `B2Haar.b_at_zero` | `51529c746902205b1144bdf7276c8b0a1ab3f6ecda96d7be98d7cca321e3fee8` | HOLDS: statement digest equals the pin | 0 | all three clear |
| `haar.lean` | `B2Haar.c_second_pos` | `86778a4b73af427371e59ff0c89bbc235dcf1c5c0ea60d3f16c8de69b82a9dd9` | HOLDS: statement digest equals the pin | 0 | all three clear |
| `haar.lean` | `B2Haar.d_reduction` | `8e15b204073e6ece6bfd439688b430eb0fa8ad294153393b214ea79c84194fb9` | HOLDS: statement digest equals the pin | 0 | all three clear |
| `haar.lean` | `B2Haar.first_zero` | `b12b436494c538ba834cfcb9a2ffdd813feb611a2090022c4883b2897df4a3b5` | HOLDS: statement digest equals the pin | 0 | all three clear |

All 11 rows: hold, all probes clear.

## Controls on the instrument (expected outcome stated first)

| Control | Expected | Observed on all 11 rows |
|---|---|---|
| correct pin (justified acceptance) | exit 0, "THE PINNED STATEMENT" | 11 of 11 exit 0 |
| no pin (must not count as holding) | exit 1, "NOT PINNED ... this result does not hold", prints the digest | 11 of 11 exit 1; printed digest equals the pinned digest in 11 of 11 |
| wrong pin `000...0` (fault detection) | exit 1, rejection | 11 of 11 exit 1 |

Three controls of fixed form do not measure the instrument's sensitivity in general.

## Lean itself (run separately, on the deposited files)

Command: `export PATH=$HOME/.elan/bin:$PATH; cd /home/user/z4-lean && lake env lean <deposited path>`.
Toolchain `leanprover/lean4:v4.19.0` (Lean 4.19.0, commit 6caaee842e94), Mathlib `inputRev v4.19.0`
(rev `c44e0c8ee63ca166450922a373c7409c5d26b00b`). Outputs: `lean/Inheritance.out`, `lean/haar.out`,
`lean/*.err`, `lean/*.exit`.

| File | Exit code | `sorry` / `admit` / `axiom` / `native_decide` in the text | Errors | Warnings | `#print axioms` |
|---|---|---|---|---|---|
| `refinement-inequality/Inheritance.lean` | 0 (14 s) | none | none | none | 18 theorems, each `[propext, Classical.choice, Quot.sound]` |
| `haar.lean` | 0 (8 s) | none | none | 1: `haar.lean:29:44: unused variable hp` (in `b_at_zero`) | 12 theorems, each `[propext, Classical.choice, Quot.sound]` |

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

## Added 24 November 2026: `Discrete.lean`

The refinement theorem in its discrete form, for an arbitrary symmetric contraction on a finite-dimensional real inner product space (kernel allowed, general lag `2k`). File SHA-256 `8706286bd607ea69005a8e3859726c190078fa4033a2ed72ae760c035d7e9c78`. Compiled with Lean 4.19.0 and Mathlib v4.19.0: exit 0, no `sorry`, no warning, `#print axioms` gives `[propext, Classical.choice, Quot.sound]` for all five declarations printed. Each statement below was run through the same instrument with its pin (exit 0, digest equals the pin, three probes clear) and with a wrong pin (exit 1). Written and run by the same model family that wrote the paper's proof; this is a machine check of the stated formal statement, not a review of whether that statement is the right one.

| File | Theorem | SHA-256 of the statement (pinned) | With pin | Wrong pin |
|---|---|---|---|---|
| `Discrete.lean` | `Discrete.refinement_fin` | `5af97e33c656ad19f48e05ab409eab58d49d5bb02bcefddacf2b455b589faefe` | exit 0 | exit 1 |
| `Discrete.lean` | `Discrete.refinement_norm` | `1b9e104c16cc89e3fdde0c79ec8f85f7c84d03dd2e4469e148c03bc7b5e795b6` | exit 0 | exit 1 |
| `Discrete.lean` | `Discrete.refinement_main` | `b8e952df34480c2fb532cd5f0e07e4080e5ad239e4bcc510ca53b88d4b1fcb9f` | exit 0 | exit 1 |
| `Discrete.lean` | `Discrete.pow_eq_Apow` | `d57faeeaa57896d810bbecbe01842c6a667305f272d5929376a711e2dd3bbaed` | exit 0 | exit 1 |
| `Discrete.lean` | `Discrete.Apow_norm_le` | `9e875e716958dc411048719d481debf1c2d7a926ba1380ea2413b8a571696c56` | exit 0 | exit 1 |

## Added 24 November 2026: `Hilbert.lean`

The refinement theorem (general lag `2k`) on every non-zero real inner product space, for a bounded symmetric positive operator of norm at most one. No spectral projection, no completeness, no dimension restriction; the proof uses approximate eigenvectors at the top of the spectrum and a Cauchy–Schwarz inequality for the forms of the powers. File SHA-256 `4cf810d6cbb7e359bf3a20672de899794c99d63b9f776c8aebb954e72d111472`. Lean 4.19.0, Mathlib v4.19.0: exit 0, no `sorry`, no warning; axioms printed in `Hilbert.axioms.txt` are `[propext, Classical.choice, Quot.sound]`. Each statement below: with its pin exit 0 and three probes clear; with a wrong pin exit 1. Written and run by the same model family that wrote the paper; a machine check of the formal statement, not a review of whether that statement is the right one. Complex scalars are not formalised.

| File | Theorem | SHA-256 of the statement (pinned) | With pin | Wrong pin |
|---|---|---|---|---|
| `Hilbert.lean` | `RefinementHilbert.refinement_hilbert` | `0f6e3b8ec02f629b977e62f60d5c3cbd88fe0b15a8ca629676a58c6fa621b11b` | exit 0 | exit 1 |
| `Hilbert.lean` | `RefinementHilbert.refinement_hilbert_norm` | `cdaf5b6ab399fb64c467e000515ff6d054c74eeeb1a3ae81ebda17c215e6f50e` | exit 0 | exit 1 |
| `Hilbert.lean` | `RefinementHilbert.exists_approx_eig` | `34d8c789672c0a7f8785f4d7a95756260fc966ace15a7a1b63d0c712e17039d8` | exit 0 | exit 1 |
| `Hilbert.lean` | `RefinementHilbert.proj_step` | `f14eaa8a4ffc4e0a753b73373e86708dfb1673016f317642aaff37b1dcd657bd` | exit 0 | exit 1 |
| `Hilbert.lean` | `RefinementHilbert.cs_form` | `dcc25a22971ae8070b4bb57e55240db1df593e9bb37de5aea8dce566d9cdecef` | exit 0 | exit 1 |
| `Hilbert.lean` | `RefinementHilbert.approx_pow` | `bff576fdf2c4630a93ec80e2fbf370db42b9b08b63b8d1ea0c19f8bb4d76e338` | exit 0 | exit 1 |

## Added 24 November 2026: `Gates.lean` and `Prediction.lean`

The algebra of the exceptional projection built from a gate (last sentence of the corollary on the return bound in the vacuum representation), and the Hilbert-space core of the conditional-prediction proposition. Both on real inner product spaces of any dimension. Lean 4.19.0, Mathlib v4.19.0: exit 0, no `sorry`, no warning, standard axioms (`*.axioms.txt`). With pin exit 0 and probes clear; wrong pin exit 1. The statement instrument does not read a `let` in a statement, so the projection is a definition (`Gates.gateB`), which the statement digest does not cover. Same-family work; the measure-theoretic identifications are not formalised.

| File | File SHA-256 | Theorem | SHA-256 of the statement (pinned) | With pin | Wrong pin |
|---|---|---|---|---|---|
| `Gates.lean` | `f858942e5f13c796c47e1e6760a00939c2fcde47162d92cd8d1b49b313176916` | `Gates.gate_projection` | `6048a80557cb70635ab7b418ac952747d3439c2345319d4d156a0dcdde8352cd` | exit 0 | exit 1 |
| `Prediction.lean` | `65abf6bce4e8028dc6faa5ffc1bcf7bb4c132577f276e635ab06580e072beec6` | `Prediction.conditional_prediction` | `8a1bc3c39afea200c2b3a90770243e8968d31068a0ad1b7283f8b985fae1a252` | exit 0 | exit 1 |

## Added 24 November 2026: `OneSeparation.lean`

The test at one time separation on finite-dimensional real spaces (symmetric `S`, `r ≤ 1`): no eigenvalue in `(r,1)` if and only if the quadratic inequality holds for every vector. File SHA-256 `a00fd234d6d26f650d1358005d2eee7b41b7492c919e0e881e953e2eca9d0af5`. Lean 4.19.0: exit 0, no `sorry`, no warning, standard axioms. Statement `OneSeparation.one_separation` pinned at `2f31cae1cfa1eedf47d806a0460f328953a508fb2d69457d590674d628a08e64`: with pin exit 0, wrong pin exit 1.

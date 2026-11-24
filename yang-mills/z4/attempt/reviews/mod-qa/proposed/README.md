# Spectral criteria and conditional infrared estimates (manuscript)

## Current status (fourth draft, 24 November 2026)

`main.tex` / `main.pdf`: fourth draft, 16 pages, repository commit `c7c2a16`. `preamble.tex` is its preamble.
Earlier drafts: `main_draft1.tex`, `main_draft2.tex`, `main_draft3.tex`. `LEAN_PINS.md` pins the Lean statements
cited in Section 9.

This is a separate manuscript from the upper-bound paper in `../attempt/paper/`, which is unchanged. It says
what is proved, what is conditional and what is open. It does not claim a mass gap.

In one sentence: Theorem 1.2 reduces one refinement step to three estimates; one of them, the return bound, is
proved for SU(2) (Theorem 1.3, Corollary 6.4); the other two are open (Hypotheses 3.1 and 3.2); chaining the
steps needs a third open condition, the budget (Hypothesis 3.3).

### Statement-to-proof ledger

Numbers are those of the fourth draft. Paths are relative to this folder unless they start with `yang-mills/`.

| Statement | Quantifiers and domain | Proof | Origin | Checks on record |
|---|---|---|---|---|
| Thm 1.1 spectral criterion; Remark 4.1 | any self-adjoint H ≥ 0, any τ > 0, any set with dense span | §4 | proposed by a GPT auditor session (issue comments 7119587014, 7119986944) | none formal |
| Prop 4.2 test at one time separation; Remark 4.3 | same H, τ; a dense linear subspace | §4 | added in the fourth draft; origin **[author to confirm]** | none on record |
| Thm 1.2 refinement inequality; Lemma 5.1 | self-adjoint 0 ≤ A ≤ I on a Hilbert space; integers m ≥ j ≥ 1; three operator hypotheses | §5 | `yang-mills/joint-refinement/rare-coarse-fields/inheritance.md` (Codex session), there for a semigroup e^{-sH}; the discrete form and its proof are of the fourth draft | source derivation attacked: `../attempt/reviews/y1-g4ret`. Lean, special case A = e^{-aH} on a finite-dimensional real space, and Lemma 5.1: `../attempt/reviews/f2-lean/Inheritance.lean`. The fourth-draft proof itself: none on record |
| Cor 5.2 accumulation; Remarks 5.3, 5.4 | real sequences | §5 | as Thm 1.2; Remark 5.3 is GPTAuditor2's counterexample | Lean (the inequality only): `../attempt/reviews/f2-lean/Inheritance.lean`, `accum`, `accum_pos` |
| Thm 1.3 return bound; Lemma 6.1 | SU(2), Wilson action, periodic lattice, even N ≥ 6, T ≥ 2, two slices distinct modulo T | §6, for periodic time | `yang-mills/joint-refinement/rare-coarse-fields/return.md` (Codex session) | attacked: `../attempt/reviews/y1-g4ret` (14 items stand, 3 not checked for want of archives) |
| Lemma 6.2 trace formula; Prop 6.3 vacuum limit; Cor 6.4 return bound in the vacuum representation | finite spatial lattice, β > 0; gauge-invariant functions | §6.1; injectivity of the temporal-gauge transfer operator is cited from Lüscher (1977) | written for the second draft; Lemma 6.2 stated and proved in the fourth | second-draft form reviewed: `../attempt/reviews/ref2-math/report.md` (found the gauge-averaging defect, since repaired). The proof of Lemma 6.2: none on record |
| Prop 7.1 one-link covariance; Remark 7.2 | tilted law on S³, all k > 0 | §7 | GPT auditor sessions (issue comments 7117411812, 7117416203) | attacked and partly formalised: `../attempt/reviews/b2-haar` (`haar.lean`, `enclosure.py`) |
| Remark 6.5(b) values | β = 3.399810242 | closed form | `return.md` | `../attempt/reviews/y1-g4ret/report.md`, `../attempt/reviews/g2-fid/report.md` |
| Hyp 3.1, Hyp 3.2, Hyp 3.3 | — | open | — | none. Hyp 3.1 is not measured. One trial for Hyp 3.2: §8.3 |
| Auxiliary local mixing statement (§3) | — | open | — | trials only: §8.1 |

### Measurements and their records

| Where in the paper | Record (under `../attempt/reviews/`) | Data in the deposit |
|---|---|---|
| Table 2, §8.1 (i), (ii) | `c2-grow` (`report.md`; `results_summaries.tgz`: `results/G-d0/an4.txt`, `results/G-clear0/an4.txt`); comparison values in the caption: `b2-matrix` | analysis outputs and weights; the per-stream matrices are not deposited, so a rerun starts from the seeds in `c2-grow/REPLAY.md` |
| §8.1 (iii) displaced holonomy | `e2-repair` (`report.md`, `results.tgz`); earlier single-mark runs `z1-mix6`, `z1-mix8` | per-stream files |
| §8.2 carry-over in time | `d2-time` (`report.md`, `REPLAY.md`, `weights/`) | none; a rerun starts from the seeds |
| §8.3 item 1 | `e2-cross` (`report.md`, `results.tgz`) | per-chain sums |
| §8.3 item 2 | `f2-cross2` (`report.md`, `results.tgz`, `src/analysis2.py`, `src/cross_eval2.py`) | per-chain sums; the two numbers were regenerated from them byte for byte, and the frozen vector of the test is written out **[path of the deposited copies of `frozen_vector_Z_ratio_opt.json` and `REPRODUCE.md`, once deposited]** |
| samplers | `sampler-sources` (`SHA256SUMS` verifies) | sources |
| couplings | `yang-mills/g4/full-attempt/physical-refinement/` | not recalibrated |

### Machine-checked parts

`LEAN_PINS.md`: eleven statements of `f2-lean/Inheritance.lean` and `b2-haar/haar.lean`, each with the SHA-256
of its statement and the result of the PCP OS instrument `mathematics.statement` against that digest (it reads
the statement text; it does not run Lean). Lean was run separately on both files: exit 0, no `sorry`, axioms
`propext`, `Classical.choice`, `Quot.sound` (Lean 4.19.0, Mathlib v4.19.0).

### Not done

- No reader outside the two model families; no person other than the author.
- The fourth draft has not been reviewed as a whole **[author to confirm; replace by the review's path when
  it exists]**. In particular the discrete proof of Theorem 1.2, Proposition 4.2 and the proof of Lemma 6.2
  have no review on record.
- Not formalised: Theorems 1.1 and 1.3, Propositions 4.2 and 6.3, Lemma 6.2, Corollary 6.4, the general case of
  Theorem 1.2, the Bessel identities of Proposition 7.1.
- The fidelity review of the second draft (105 items) was applied in commit `82357b4`, but its report was not
  deposited: `../attempt/reviews/ref2-fid/` is empty.
- From the readability report (`../attempt/reviews/ref2-read/report.md`): its table of about 35 terms (Table 1
  of the paper has twelve symbols), the symbol collisions (R, p, q, M, L, G, T, C, A, E each carry more than
  one meaning) and the repeated disclaimers.
- Raw data of `d2-time`, and the per-stream matrices of `c2-grow` and `b2-matrix`, are not deposited.

### External grounding

- Jaffe–Witten, *Quantum Yang–Mills Theory*, §§4–5: read (text extracted locally, not stored here).
- Yang–Mills group, *Validation of the OpenAI Yang–Mills construction*, 10 November 2026: first page and
  contents read; it states that the assessed construction proves a Wightman theory as a scaling limit of Wilson
  lattice gauge theory for any simple compact group and does not prove a mass gap or uniqueness of the
  infinite-volume limit. The construction itself was not read. Nothing in this manuscript is shown to belong
  to it.
- OpenAI, *Finite Time Blowup for Navier–Stokes*: first pages, contents, figure captions and the proof-outline
  section read for organisation only.

---

## History (earlier drafts; statement numbers and page counts are those of the draft named)

Everything below is a record of what was true when it was written. Where it differs from "Current status",
the current status holds.

### Fourth draft (24 November, commit `c7c2a16`; previous draft kept as `main_draft3.tex`)

- **Theorem 1.2** restated for a discrete step: a self-adjoint `A` with `0 ≤ A ≤ I` and integers `m ≥ j ≥ 1`
  in place of a semigroup `e^{-sH}` and real times. No logarithm of `A` is needed and `A` may have a kernel.
  New proof (spectral projection of `A` near its norm; the case `‖A‖ = 0` separately).
- **Lemma 6.2 (trace formula)** stated and proved for the gauge-averaged operator `L = T_0 Π`. Proposition 6.3
  and Corollary 6.4 were 6.2 and 6.3; Remark 6.5 was 6.4. (The one-link proposition and its remark became
  Proposition 7.1 and Remark 7.2 in the third draft.)
- **Proposition 4.2 and Remark 4.3** added: a test of the gap at one time separation.
- Auditors' wording points **[author to confirm the list]**.
- Deposited: `../attempt/reviews/f2-cross2/results.tgz`; `LEAN_PINS.md`.

### Third draft (24 November; 15 pages; `main_draft3.tex`)

Three subagent reviews of the second draft were applied:

- **Mathematics** (`../attempt/reviews/ref2-math/report.md`): one real defect in the vacuum bridge I had added.
  The operator for which the trace formula holds is the gauge-averaged transfer operator; it vanishes on
  functions that are not gauge invariant, so the Hamiltonian exists only on the gauge-invariant subspace. The
  setting, the application of the refinement inequality and the corollary are now stated there. The referee
  established this by its own argument and a toy computation (a Z_3 theory in 1+1 dimensions), not by
  rereading the cited papers. Four smaller gaps repaired (a missing line in the accumulation proof; the
  one-slice limit; two wordings).
- **Fidelity** (report not deposited; see "Not done"): 105 items against the records; 1 wrong reference,
  4 overstatements, 1 unsupported clause, all changed.
- **Readability** (`../attempt/reviews/ref2-read/report.md`): a plain-words subsection before the results; an
  "in words" paragraph after each of Theorems 1.2 and 1.3; the outline section rewritten to be read from the
  top of the figure; Question / Setup form for the three measurements, with "stream", "mark", "frozen
  background", "gate" and the two-time energy defined at first use; the one-link proposition's statement moved
  to its own section; sources and the external construction moved toward the end; the figure's arrows made
  consistent with its caption; the count of open items made consistent (two for one refinement step, a third
  for chaining them).

### Second draft (24 November; 13 pages; `main_draft2.tex`)

Two reviews of the first draft, a same-family referee (`../attempt/reviews/g2-fid/report.md`) and GPTAuditor2's
adversarial review (relayed by the Principal), agreed that the four proofs stand and that the surrounding
sentences said too much. Changes (numbers of the second draft):

- **Opening.** The introduction starts from the two questions the paper is about, before any statement.
- **Vacuum bridge.** The return bound was proved for periodic time, while the refinement inequality needs the
  vacuum semigroup. Added Proposition 6.2 (vacuum limit of two-slice expectations) and Corollary 6.3 (the
  return bound in the vacuum representation, and for B = R(I - P)). The transfer-matrix representation is
  cited (Luescher; Osterwalder-Seiler), not rederived.
- **Budget.** The accumulation needs the weighted sum of losses to stay below the initial deficit, not only
  summability. Now Hypothesis 3.3, with GPTAuditor2's exact counterexample as Remark 5.3.
- **Two kinds of mixing.** Hypothesis 3.1 (decay under the transfer semigroup) is separated from the auxiliary
  local mixing statement (relaxation under artificial local updates). The measured local quotients concern
  only the latter.
- **Theorem 1.3.** Complex test functions with absolute squares; slices of spatial links, distinct modulo the
  period.
- **Remark 4.1(a)** corrected: matrix elements do not decay; the vacuum must be projected out.
- **Remark 7.1.** The "three to four orders" comparison removed; the one-link floors are given with their scope.
- **Measurements.** The frozen background has three plaquettes at -I; "81 per cent" is a share of standardised
  squared coefficients; the paired decreases are kept; the time test is reported as limited carry-over in the
  observables tried; the cross-lattice result is stated as correlation retained (about 1 per cent against about
  7 per cent), with the rejection threshold 0.951 and the statement that one test does not measure the loss in
  Hypothesis 3.2.
- **Scope.** Finite mass; local fields and short-distance behaviour; the limit of the assessors' independent
  check; a crude return bound for general groups (Remark 6.4(d)).
- **References** pinned to files; Luescher and Osterwalder-Seiler added.

### First draft (24 November; 11 pages; `main_draft1.tex`)

Written after GPTAuditor2's final handoff (rendezvous issue, comment 7120159737) and the Principal's
instruction to state only what we have, with the organisation (not the claims) of OpenAI's Navier–Stokes
paper: short abstract, theorems stated on the first page with their domain, an architecture figure whose boxes
are numbered statements, proofs in dependency order, a status table at the end.

Not done at the first draft (superseded; see "Current status"): Theorem 1.3 was not carried to the infinite
time axis (done in the second draft). Theorems 1.1 and 1.3 were not formalised (still so). The figure prepared
with the PCP OS plot instrument for Table 2 was left out: the table carries the four numbers per row more
clearly.

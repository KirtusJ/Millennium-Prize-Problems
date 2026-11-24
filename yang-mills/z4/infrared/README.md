# Spectral criteria and conditional infrared estimates (manuscript)

**Current state: seventh version, 24 November 2026, 22 pages.** The paper, its source and its supplementary material are now in [`../../papers/spectral-criteria/`](../../papers/spectral-criteria/); this folder keeps the earlier versions and the change record. Earlier versions are `main_draft1.tex` to `main_draft6.tex`. The reading copy and the catalogue of supplementary material are in [`../../papers/spectral-criteria/`](../../papers/spectral-criteria/). This is a rough draft under revision. It states what is proved, what is conditional and what is open. It does not claim a mass gap, and no reader outside the two model families, and no person other than the author, has checked it.

It is a separate manuscript from the upper-bound paper in `../attempt/paper/`, which is unchanged.

## Statement-to-proof ledger (seventh version)

| Statement | Domain | Proof | Origin | Checks (none is independent review) |
|---|---|---|---|---|
| Thm 1.1 spectral criterion; Prop 4.2 test at one separation | any self-adjoint H ≥ 0, τ > 0; a set with dense span (1.1), a dense linear subspace (4.2) | §4 | GPT auditor sessions (issue comments 7119587014, 7119986944) | `../../papers/spectral-criteria/supplement/S10-review-records/mathematics-review` |
| Thm 1.2 refinement inequality; Cor 5.2 | positive self-adjoint contraction A on a Hilbert space, integers m ≥ j ≥ 1, three operator hypotheses | §5 | `yang-mills/joint-refinement/rare-coarse-fields/inheritance.md` (Codex session); discrete form suggested by a GPT auditor session | `y1-g4ret`, `mod-math` (265,000 random instances); Lean for the finite-dimensional semigroup case only: `f2-lean/Inheritance.lean` |
| Thm 1.3 return bound | SU(2), Wilson action, periodic lattice, even N ≥ 6, two slices distinct modulo T | §6 | `rare-coarse-fields/return.md` (Codex session) | `y1-g4ret`, `mod-math` |
| Lemma 6.2 trace formula; Prop 6.3; Cor 6.4 (return bound in the vacuum) | SU(2), β > 0, gauge-averaged transfer operator | §6.1, self-contained (Peter–Weyl and positive character coefficients; Lüscher's paper is referred to, not relied on, and was not reread) | this side | `ref2-math`, `mod-math` (full enumeration on Z₂ and Z₃ toy lattices) |
| Prop 3.2 conditional prediction; Remark 5.5 longer lag | reversible stationary one-step operator; any measurable set of coarse fields | §3, §5 | a GPT auditor session (pass 2, relayed) | `aud5-check` (finite-state program) |
| Prop 7.1 one-link covariance | tilted law on S³, all k > 0 | §7 | GPT auditor sessions (issue comments 7117411812, 7117416203) | `b2-haar` (partly formalised) |
| Hypotheses 3.1 (short-time decay), 3.3 (coarse comparison), 3.4 (budget); auxiliary local mixing | — | open | — | not measured; trial estimates only: `b2-matrix`, `c2-grow`, `d2-time`, `e2-repair`, `e2-cross`, `f2-cross2`; their statistics reviewed in `mod-sci` |

The records named in the last column are now under `../../papers/spectral-criteria/supplement/` (see `SUPPLEMENT.md` there for the present names; the Lean digests are in `S7-lean/LEAN_PINS.md`).

## External grounding

- Jaffe–Witten, *Quantum Yang–Mills Theory*, §§4–5: read (text extracted locally, not stored here).
- Yang–Mills group, *Validation of the OpenAI Yang–Mills construction*, 10 November 2026: first page and contents read; it states that the assessed construction proves a Wightman theory as a scaling limit of Wilson lattice gauge theory for any simple compact group and does not prove a mass gap or uniqueness of the infinite-volume limit. The construction itself was not read. Nothing in this manuscript is shown to belong to it.
- OpenAI, *Finite Time Blowup for Navier–Stokes*: first pages, contents, figure captions and the proof-outline section read for organisation only.

## Known gaps in the record

- The time-carry-over run (`d2-time`) left no result file in the deposit; its numbers are those of its report.
- Per-stream data of the local-quotient run (`c2-grow`) are not deposited (regenerated from seeds; across rebuilds of the sampler this is statistical, not byte for byte).
- Theorems 1.1 and 1.3, Lemma 6.2, Propositions 4.2 and 6.3 and Corollary 6.4 are not formalised.

# History of the drafts

## Seventh version (24 November): finalisation

On the Principal's instruction the worker tests were stopped (two background checks cancelled without result) and the paper was put into final form.

- **Label.** The title page states that the paper belongs to the research program *From Prephysical Hypotheses to Physical Models*, with subject classification and keywords; the draft label is removed.
- **References.** External literature first. Self-citations are two entries under an explicit heading: the research program, and one entry for the supplementary material. The five path-by-path repository entries are gone; the text cites "Supplement S1" to "S10", catalogued in Appendix B, with locations and digests in `papers/spectral-criteria/SUPPLEMENT.md`. No program paper is cited individually because none is used in a proof.
- **Internal names.** No project alias, folder name or process word appears in the paper. Contributions are attributed to Claude (Anthropic), OpenAI Codex and OpenAI GPT models in a statement "Use of artificial-intelligence systems", which says they are not authors. This follows common publisher practice (AI systems are not authors; their use is disclosed in a dedicated statement, methods or acknowledgments), checked against a web search of current policies rather than taken on instruction.
- **Appendices.** A: machine-checked parts (moved from the body; now says 11 of 30 theorems are pinned and that a statement digest does not cover dependencies). B: catalogue of supplementary material. A "Data and code availability" statement names the two things not stored.
- **GPTAuditor5's closing corrections** (issue comment 7121386048): the time test concerns the periodic analogue of the conditional correlation, not the vacuum quantity, and an estimate at one coarse field is not a certified bound; three of the 25 cross-lattice tests have point estimates below one and only one meets the criterion fixed in advance; the -0.017 offset is an idealised benchmark; "no measurement is evidence for or against" replaced by a statement of what trial estimates are evidence about.

- **Tidying (same day).** The source, the reading copy and every record the paper cites were moved into `yang-mills/papers/spectral-criteria/` under neutral names (S1 to S10), so that the paper and its catalogue point to no working label. Items S6, S8 and S9 are copies of notes maintained by the other side of the project, whose originals were not moved. Links in the working notes were updated; records keep the path names of their day inside their own text.

## Sixth draft (24 November)

A first-time-reader review of the fifth draft (`../../papers/spectral-criteria/supplement/S10-review-records/first-reader/report.md`, sub-agent of the same family) supplied a replacement abstract, introduction and Measurements section; the director read them, adjusted them and spliced them in. No theorem, number or claim was added or removed in the Measurements section (its 162 numerals were compared by script before and after; the later edits only add two clarifying values, 1.14 and the unrounded 0.93574 + 2 x 0.00271).

- **Opening.** The paper starts from a supposition and two numbered questions, defines "mass gap" in one sentence, and says in its own paragraph that no gap is proved. The refinement idea is told once, as suppositions (a), (b), (c), and the theorem's hypotheses are mapped to them.
- **Measurements.** A table of runs carries the designs; each subsection runs Question, What we found, Setup, results, failed checks, what this does not show. The two forms of the time test are now named with each value.
- **Wording that could be read as a claim** (17 places listed by the reader) qualified: "one of the three is proved" now says for exceptional sets of a particular kind; estimates are marked as estimates; the status table says what "proved" means here.
- **Layout.** Caption spacing, ragged-right status table, wider figure boxes.

A challenger on the new statements (`../../papers/spectral-criteria/supplement/S10-review-records/challenge-2/report.md`) found the conditional-prediction proposition and the longer-lag remark to stand (20000 and 40000 qualifying instances, no failure; the attacks that should fail do). Repaired after it: the correlation in the proposition is centred under the conditional law; the good set is gauge invariant; the last clause of the lag remark had stated a necessary condition as sufficient; the definition of mass gap now includes the vacuum; one convention for the Hamiltonian; "is a gap of that lattice" replaced. Its program was rerun by the director in a fresh directory with the same result.

Remarks 4.1 and 6.5 are now lists. Not done from that report: several undefined-at-first-use terms outside the introduction (colour classes, slabs, tilt); remaining letter clashes (A as operator and as background, r, C, E).

## Fifth draft (24 November)

Reviews of the fourth draft under the PCP mathematics, science and statistics modules (`../../papers/spectral-criteria/supplement/S10-review-records/mathematics-review/report.md`, `../../papers/spectral-criteria/supplement/S10-review-records/statistics-review/report.md`; both by sub-agents of the same model family). Their programs were rerun by the director in fresh directories and all result files reproduce byte for byte (statistics: 30 predicates met, 0 failed).

- **Mathematics: no error found in a statement.** Repaired: a letter used for two things in the proof of Corollary 6.4; a wrong description of the character coefficients in Lemma 6.2 (the convolution eigenvalue on spin n/2 is 2 I_{n+1}(β)/β), after which the lemma no longer leans on the cited paper; undefined P_i, M_0 and lag of κ_i in the hypotheses; two wrong reasons in the proof of Theorem 1.2; the sign in Remark 4.3; "centred" in Remark 6.5(c).
- **Measurements section rewritten.** No number was wrong in value. Four passages said more than the design supports, and the section omitted failed checks and rules. Now stated: the rule fixed in advance for "stopped falling" was met on the −I background (the paired comparison was not the rule); the time test's rule had three outcomes, and the formally met one is uninformative because of an over-fitting offset; the sentence that the time test "shows" two kinds of slowness differ is withdrawn; the failed hot/cold check behind 1.016(11); the further displacement 4/β; the number of streams behind every error; the 25 tests examined before the reported cross-lattice one; an unexplained 3.4-standard-error disagreement with an earlier run; that 0.951 is not a confidence limit at a stated level.
- **Quality assurance** (`../../papers/spectral-criteria/supplement/S10-review-records/quality-review/report.md`). The headline cross-lattice numbers reproduce exactly from the deposited per-chain files with no new sampling; the director reran this and obtained the same bytes. The full coefficient vector of the reported test is now deposited (`../../papers/spectral-criteria/supplement/S5-cross-lattice/second-study/frozen_vector_Z_ratio_opt.json`, with `../../papers/spectral-criteria/supplement/S10-review-records/quality-review/f2/REPRODUCE.md`). `LEAN_PINS.md` replaced: all eleven pins hold, and wrong or missing pins are refused. The count of open items is now the same everywhere (two for one step, a third for chaining). Terms defined at first use; six repeated disclaimers cut. One sentence removed because no record supports it (the sign pattern of the 15-mark combination). The fidelity report of the second draft (`ref2-fid`) was never committed and is lost; the link to it below is dead.
- **Auditors' closing points on the fourth draft** (issue comments 7120868145, 7121040887, 7121050934) applied: the all-vector reading of the first hypothesis and the two separate small quantities; the simple eigenvalue belongs to the constants; generating families in Remark 4.1(d); the θ³ scaling is at fixed coupling; three of the four plaquettes through the altered link; ε_i is an allowed loss; spectrum in [Δ, ∞).
- **Challenger on the changed proofs** (`../../papers/spectral-criteria/supplement/S10-review-records/challenge-1/report.md`): no proof broken. One sentence of the introduction was false as worded (it put the decay on the remainder alone; a rank-one example defeats that reading) and is replaced; quantifiers of Hypotheses 3.2 and 3.3 and of Corollary 5.2 made explicit.
- **GPTAuditor5, pass 2** (relayed by the Principal): its conditional-prediction reduction (now Proposition 3.2) and longer mixing lag (Remark 5.5) were checked by the director's own finite-state program before use (`../../papers/spectral-criteria/supplement/S10-review-records/conditional-prediction-check/`: 5244 and 20000 qualifying instances, no violation; the control with the old denominator fails, as it should). Both are reductions between open estimates. Its scope point (centred gauge-invariant against centre-neutral functions) is item 6 of "What is not claimed". Its other routes and countermodel were not added.
- **Symbols.** Gate Γ_θ (was A_θ); multiplication operator χ (was R); λ_∥, λ_⊥, λ_min, ℓ in Proposition 7.1 (were p, q, m, L); S in Proposition 4.2 (was T); n_g gates (was M).

## Fourth draft (24 November)

Theorem 1.2 restated for one transfer step and whole numbers of steps; Lemma 6.2 proved rather than cited; Proposition 4.2 added; wording reduced after the auditors' reviews of the second draft (issue comment 7120815551 lists every change).

## Second draft (24 November): what changed and why

`main.tex` / `main.pdf` are now the second draft (13 pages); `main_draft1.tex` is the first.

Two reviews of the first draft, a same-family referee ([`../../papers/spectral-criteria/supplement/S10-review-records/version-1-referee/report.md`](../../papers/spectral-criteria/supplement/S10-review-records/version-1-referee/report.md)) and GPTAuditor2's adversarial review (relayed by the Principal), agreed that the four proofs stand and that the surrounding sentences said too much. Changes:

- **Opening.** The introduction starts from the two questions the paper is about, before any statement.
- **Vacuum bridge.** The return bound was proved for periodic time, while the refinement inequality needs the vacuum semigroup. Added Proposition 6.2 (vacuum limit of two-slice expectations, from the cited transfer-matrix representation) and Corollary 6.3 (the return bound in the vacuum representation, and for B = R(I - P)). The figure's arrow is solid only because of this; the transfer-matrix representation is cited (Luescher; Osterwalder-Seiler), not rederived.
- **Budget.** The accumulation needs the weighted sum of losses to stay below the initial deficit, not only summability. Now Hypothesis 3.3, with GPTAuditor2's exact counterexample as Remark 5.3.
- **Two kinds of mixing.** Hypothesis 3.1 (decay under the transfer semigroup) is separated from the auxiliary local mixing statement (relaxation under artificial local updates). The measured local quotients concern only the latter and are no longer described as bounds on the rate in Hypothesis 3.1.
- **Theorem 1.3.** Complex test functions with absolute squares; slices of spatial links, distinct modulo the period.
- **Remark 4.1(a)** corrected: matrix elements do not decay; the vacuum must be projected out.
- **Remark 7.1.** The "three to four orders" comparison removed; the one-link floors are given with their scope.
- **Measurements.** The frozen background has three plaquettes at -I; "81 per cent" is a share of standardised squared coefficients; the paired decreases are kept; the time test is reported as limited carry-over in the observables tried, with the long-lag control named as such; the cross-lattice result is stated as correlation retained (about 1 per cent against about 7 per cent), with the rejection threshold 0.951 and the statement that one test does not measure the loss in Hypothesis 3.2.
- **Scope.** Finite mass; local fields and short-distance behaviour; the limit of the assessors' independent check; a crude return bound for general groups (Remark 6.4(d)).
- **References** pinned to files; Luescher and Osterwalder-Seiler added.

## Third draft (24 November)

`main.tex` / `main.pdf` are now the third draft (15 pages); `main_draft2.tex` is the second. Three subagent reviews of the second draft were applied:

- **Mathematics** ([`../../papers/spectral-criteria/supplement/S10-review-records/version-2-mathematics/report.md`](../../papers/spectral-criteria/supplement/S10-review-records/version-2-mathematics/report.md)): one real defect in the vacuum bridge I had added. The operator for which the trace formula holds is the gauge-averaged transfer operator; it vanishes on functions that are not gauge invariant, so the Hamiltonian exists only on the gauge-invariant subspace. The setting, the application of the refinement inequality and the corollary are now stated there. The referee established this by its own argument and a toy computation (a Z_3 theory in 1+1 dimensions), not by rereading the cited papers. Four smaller gaps repaired (a missing line in the accumulation proof; the one-slice limit; two wordings).
- **Fidelity** ([`../attempt/reviews/ref2-fid/report.md`](../attempt/reviews/ref2-fid/report.md)): 105 items against the records; 1 wrong reference, 4 overstatements, 1 unsupported clause, all changed.
- **Readability** ([`../../papers/spectral-criteria/supplement/S10-review-records/version-2-readability/report.md`](../../papers/spectral-criteria/supplement/S10-review-records/version-2-readability/report.md)): a plain-words subsection before the results; an "in words" paragraph after each of Theorems 1.2 and 1.3; the outline section rewritten to be read from the top of the figure; Question / Setup form for the three measurements, with "stream", "mark", "frozen background", "gate" and the two-time energy defined at first use; the one-link proposition's statement moved to its own section; sources and the external construction moved toward the end; the figure's arrows made consistent with its caption; the count of open items made consistent (two for one refinement step, a third for chaining them).

Not yet done from the readability report: its full table of about 35 terms, the symbol collisions it lists (R, p, M, L and G each carry more than one meaning), and its inventory of repeated disclaimers.

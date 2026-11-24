# Spectral criteria and conditional infrared estimates (manuscript)

`main.tex` / `main.pdf` (11 pages, 24 November 2026). A separate manuscript from the upper-bound paper in `../attempt/paper/`, which is unchanged. It says what is proved, what is conditional and what is open; it does not claim a mass gap.

Written after GPTAuditor2's final handoff (rendezvous issue, comment 7120159737) and the Principal's instruction to state only what we have, with the organisation (not the claims) of OpenAI's Navier–Stokes paper: short abstract, theorems stated on the first page with their domain, an architecture figure whose boxes are numbered statements, proofs in dependency order, a status table at the end.

## Statement-to-proof ledger

| Statement | Quantifiers and domain | Proof | Origin | Checks |
|---|---|---|---|---|
| Thm 1.1 spectral criterion | any self-adjoint H ≥ 0, any τ > 0, any set with dense span | §4, complete | proposed by a GPT auditor session (issue comments 7119587014, 7119986944) | none formal |
| Thm 1.2 refinement inequality; Cor 5.2 | abstract Hilbert space; three operator hypotheses | §5, complete | `yang-mills/joint-refinement/rare-coarse-fields/inheritance.md` (Codex session) | attacked `../attempt/reviews/y1-g4ret`; Lean, finite dimension: `../attempt/reviews/f2-lean/Inheritance.lean` |
| Thm 1.3 return bound | SU(2), Wilson action, periodic lattice, even N ≥ 6, two distinct slices | §6, complete for periodic time | `rare-coarse-fields/return.md` (Codex session) | attacked `../attempt/reviews/y1-g4ret` |
| Prop 1.4 one-link covariance | tilted law on S³, all k > 0 | §7, complete | GPT auditor sessions (issue comments 7117411812, 7117416203) | attacked and partly formalised: `../attempt/reviews/b2-haar` |
| Hyp 3.1, Hyp 3.2 | — | open | — | measurements only: `../attempt/reviews/{b2-matrix,c2-grow,d2-time,e2-repair,e2-cross,f2-cross2}` |

## External grounding

- Jaffe–Witten, *Quantum Yang–Mills Theory*, §§4–5: read (text extracted locally, not stored here).
- Yang–Mills group, *Validation of the OpenAI Yang–Mills construction*, 10 November 2026: first page and contents read; it states that the assessed construction proves a Wightman theory as a scaling limit of Wilson lattice gauge theory for any simple compact group and does not prove a mass gap or uniqueness of the infinite-volume limit. The construction itself was not read. Nothing in this manuscript is shown to belong to it.
- OpenAI, *Finite Time Blowup for Navier–Stokes*: first pages, contents, figure captions and the proof-outline section read for organisation only.

## Not done

No reader outside the two model families; no person other than the author. Theorem 1.3 is not carried to the infinite time axis. Theorems 1.1 and 1.3 are not formalised. The figure prepared with the PCP OS plot instrument for Table 2 was left out: the table carries the four numbers per row more clearly.

## Second draft (24 November): what changed and why

`main.tex` / `main.pdf` are now the second draft (13 pages); `main_draft1.tex` is the first.

Two reviews of the first draft, a same-family referee ([`../attempt/reviews/g2-fid/report.md`](../attempt/reviews/g2-fid/report.md)) and GPTAuditor2's adversarial review (relayed by the Principal), agreed that the four proofs stand and that the surrounding sentences said too much. Changes:

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

- **Mathematics** ([`../attempt/reviews/ref2-math/report.md`](../attempt/reviews/ref2-math/report.md)): one real defect in the vacuum bridge I had added. The operator for which the trace formula holds is the gauge-averaged transfer operator; it vanishes on functions that are not gauge invariant, so the Hamiltonian exists only on the gauge-invariant subspace. The setting, the application of the refinement inequality and the corollary are now stated there. The referee established this by its own argument and a toy computation (a Z_3 theory in 1+1 dimensions), not by rereading the cited papers. Four smaller gaps repaired (a missing line in the accumulation proof; the one-slice limit; two wordings).
- **Fidelity** ([`../attempt/reviews/ref2-fid/report.md`](../attempt/reviews/ref2-fid/report.md)): 105 items against the records; 1 wrong reference, 4 overstatements, 1 unsupported clause, all changed.
- **Readability** ([`../attempt/reviews/ref2-read/report.md`](../attempt/reviews/ref2-read/report.md)): a plain-words subsection before the results; an "in words" paragraph after each of Theorems 1.2 and 1.3; the outline section rewritten to be read from the top of the figure; Question / Setup form for the three measurements, with "stream", "mark", "frozen background", "gate" and the two-time energy defined at first use; the one-link proposition's statement moved to its own section; sources and the external construction moved toward the end; the figure's arrows made consistent with its caption; the count of open items made consistent (two for one refinement step, a third for chaining them).

Not yet done from the readability report: its full table of about 35 terms, the symbol collisions it lists (R, p, M, L and G each carry more than one meaning), and its inventory of repeated disclaimers.

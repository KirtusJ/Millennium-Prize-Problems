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

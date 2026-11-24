Report of a review sub-agent (same model family as the director; not independent review), as handed back; saved by the director. Line numbers are those of the fourth draft (commit c7c2a16).

# mod-qa handback: QA of the infrared manuscript and its deposit

## Two things you need to know first

1. **`report.md` was not written.** The Write tool refused it ("Subagents should return findings as text, not write report files"). I did not work around the refusal. The findings and the traceability table are below instead. The exact replacement texts are in two files it did allow: `proposed/README.md` and `proposed/main.tex.c7c2a16.patch`.
2. **`main.tex` changed while I worked.** I reviewed the committed fourth draft (`c7c2a16`, SHA-256 `aaec6bca…83f9`, now also `main_draft4.tex`). The working copy is now `d2fe6013…` (377 lines changed, uncommitted). All line numbers below are for `c7c2a16`. Of my 34 replacements, 27 still match the working copy verbatim; 7 do not, because that text was rewritten (holonomy in Thm 1.3, "not claimed" item 5, the raw-data sentence, Table 2 row label, l.647, "span of 54", "What remains").

Nothing found changes a mathematical statement or a reported number. This is same-family internal checking, not independent review.

## Results by task

**Task 2, LEAN_PINS.** All 11 rows hold against their pins (exit 0, three probes clear). Controls: no pin and a wrong pin both give exit 1, 11 of 11. Deposited Lean files are byte-identical to the worker copies. Lean 4.19.0 / Mathlib v4.19.0 on the deposited files: exit 0 for both, no `sorry`, 30 `#print axioms` lines all `[propext, Classical.choice, Quot.sound]`, one linter warning (`haar.lean:29:44`, unused `hp`). Only 11 of 30 theorems are pinned, and a statement digest does not cover `def S` or `def M`.

**Task 3, headline number.** It reproduces exactly from the deposited per-chain files, with no Monte Carlo:

| | Paper | Reproduced |
|---|---|---|
| R_5 held-out, 2l | 0.990(3) | 0.99027(0.00297) |
| R_10 held-out, 2l | 0.932(4) | 0.93177(0.00396) |
| ratio, 2l | 0.941(5) | 0.94092(0.00490) |
| ratio, 4l | 0.936(3) | 0.93574(0.00271) |
| threshold | 0.951 | 0.95071 |

The three regenerated result files are byte-identical to the deposited ones, and two fresh runs are byte-identical to each other. The full 54-coefficient vector is written out with names. `results.tgz` SHA-256: `914fc35fa496bb433362b1378b972032c40ed1e67c4732c45e823d7d811b5795`.
- The deposited programs do not run from the deposit unmodified: `analysis2.py` and `cross_eval2.py` hard-code `/home/user/z4-workers/f2-cross2/…`. My driver substitutes those two lines in memory.
- The vector depends on class order (class Z is optimised after class L has drawn from the seed-239 generator).
- The class-Z span has dimension 48, not 54.

**Task 4, build.** Three `pdflatex` passes, exit 0, 16 pages, no undefined reference, no overfull box, no duplicate label. No sentence points the wrong way. Two imprecise targets: l.273 "as in Theorem 1.3" (B is built in Corollary 6.4) and the figure's auxiliary box pointing to §8.1 instead of §3. Table 1 and Remarks 4.1, 4.3, 5.4, 7.2 are never cited. The patched fourth draft also compiles clean.

Terms not defined at or before first use:
- holonomy and round distance: used l.116, defined l.129-130
- centred: l.182, never defined
- staple: l.438, never defined
- trajectory: l.148, never defined
- matched coupling: l.148, explained only at l.674
- fixed physical box: l.22, never defined
- background: l.47, never defined
- "good background" does not occur in the paper.

**Task 1, README and paths.**
- README has 14 stale statements: page count, "Prop 1.4", missing Hyp 3.3, "not carried to the infinite time axis", old numbers 6.2/6.3/6.4(d)/7.1, no fourth-draft record, eight statements with no ledger row.
- `ref2-fid/report.md` is a broken link: the directory is empty, untracked, and no copy exists under `z4-workers`.
- `[Repo]` says "commit `db2edcb` or later", but `f2-cross2/results.tgz`, `ref2-math`, `ref2-read` and `LEAN_PINS.md` are absent at `db2edcb`.
- `[RepoInh]` reads as `rare-coarse-fields/full-complement/`, which does not exist; the folder is `joint-refinement/full-complement/`.
- l.598-599 claims raw data are deposited. `d2-time` has none; `c2-grow` and `b2-matrix` have summaries only.
- Fourth-draft additions (discrete proof of Thm 1.2, Prop 4.2, proof of Lemma 6.2) have no review record, and Prop 4.2 has no stated origin.

**Task 5, consistency.** Eleven disagreements. The main one is the count: the abstract (l.12-13) and introduction (l.51-53) say two open; "not claimed" (l.147-150), the outline (l.225) and Table 3 say three. Proposed single wording: one step needs three estimates, one proved for SU(2), two open (Hyp 3.1, 3.2), and chaining needs a third open condition (Hyp 3.3).
- "A fourth result" (l.135) omits Prop 4.2.
- Table 3 claims "every statement" but omits Lemmas 5.1 and 6.1, and "finite mass" and "all groups" from "What remains".
- Corollary 5.2 sits in both a solid and a dashed figure box.
- Table 3 says "two frozen backgrounds" where Table 2 says "sampled".

Repeated disclaimers, with deletions:

| Content | Occurrences | Delete or shorten |
|---|---|---|
| No mass gap | l.13, 30, 141, 304, Table 3 | l.304 |
| [OAI] not examined | l.29, 144, 726, 743, 768, bib | l.768 clause |
| Measurements are trials | l.154, 595, 647, 664, 692 | shorten l.154, l.647 |
| Local is not time | l.47, 195, 282, 603, 666 | l.47 clause, l.603 |
| Prop 7.1 scope | l.135, caption l.267, Remark 7.2 | caption |
| Lean scope | §9, l.758, Table 3 | l.758 |

## Traceability (condensed)

| Item | Record (under `attempt/reviews/`) | Exists | From deposit |
|---|---|---|---|
| Thm 1.1, Remark 4.1 | text only | — | — |
| Prop 4.2, Remark 4.3 | none | no | — |
| Thm 1.2 | `y1-g4ret`; `f2-lean/Inheritance.lean` (continuous special case) | yes | Lean rerun, exit 0 |
| Lemma 5.1, Cor 5.2 inequality, Remark 5.4 | `f2-lean` (`xr_le`, `accum`, `reset_example`) | yes | rerun |
| Thm 1.3, Lemma 6.1 | `y1-g4ret/report.md` (14 stand, 3 not checked) | yes | not rerun |
| Lemma 6.2 | none for this proof | no | — |
| Prop 6.3, Cor 6.4 | `ref2-math` | yes | not rerun |
| Remark 6.5(b) | `y1-g4ret`, `g2-fid` | yes | recomputed |
| Remark 6.5(a) constant; Remark 7.2 values | none | no | recomputed (1.5255; 0.003437, 0.003191) |
| Prop 7.1, R'(6) | `b2-haar` | yes | Lean rerun; enclosure not rerun |
| Table 2, (i), (ii) | `c2-grow/report.md` l.38, 51-58, 74; caption values also `b2-matrix` | yes | needs regeneration from seeds |
| (iii) 1.004(11), 1.034(13) | `e2-repair/report.md` l.19-20, 64-67 | yes | data deposited, not rerun |
| §8.2, all seven numbers | `d2-time/report.md` l.6-8, 25 | yes | needs regeneration, no data |
| §8.3 item 1 | `e2-cross/report.md` l.11, `notes.md` l.52 | yes | data deposited, not rerun |
| §8.3 item 2 | `f2-cross2` | yes | rerun, byte-identical |
| Fidelity review | `ref2-fid` | **empty** | no |

One item is not established: "(i) opposite sign in the 15-mark span" (l.632). `g2-fid` found it supported only for an 11-mark optimum, and the later check sits in the missing `ref2-fid`.

## Method clauses

- **Applied:** 1.2, 1.3, 2.1-2.3, 3.1, 3.2, 3.4, 3.6, 3.7, 4.2, 4.3, 5.3, 5.4, 6.1, 7.1, 7.2, 8.4, 8.5, Appendix A.
- **Not applied:** Core was not read, and no Review exists, so `quality.coverage` (§10) was not run. Also not applied: 2.4 beyond the brief, 3.5, 4.1, 4.4, 5.2 (needs an outside reader), 6.2-6.3 (corrections proposed, not applied), 9.
- No network was used, so external URLs and issue-comment numbers are unchecked.

## Files are in `/home/user/z4-workers/mod-qa/`

- `LEAN_PINS.md`
- `proposed/README.md`
- `proposed/main.tex.c7c2a16.patch`
- `f2/frozen_vector_Z_ratio_opt.json`
- `f2/REPRODUCE.md`
- `f2/rerun1/`, `f2/rerun2/`
- `lean/`
- `scripts/` (`apply_proposed.py` holds each replacement, tagged D1-D11 etc.)
- `chk/`
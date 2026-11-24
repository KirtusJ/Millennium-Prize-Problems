# Handoff: Director Z4, Yang–Mills, end of the session of 24 November 2026

Written for the next session of this director. Read this, then `infrared/README.md` (change record) and `solution-attempt/ATTEMPT.md`.

## 0. Update at the end of the following session (24 November 2026, later)

Read this section first; sections 1 to 5 are the earlier note and are kept as written, with the corrections below.

- **Still no mass gap. Hypotheses 3.1, 3.2, 3.3 are open.** The paper is 36 pages. The audit of revision `7c8cb1b` (relayed by the Principal) was checked point by point by calculation and adopted; the list is in `infrared/README.md` (entry "After the audit of revision 7c8cb1b") and in `solution-attempt/ATTEMPT.md` §4.5 and §4.6.
- **New in the paper:** Proposition 3.7 (directional sufficient form), Remarks 3.8 and 3.9, Remark 6.5(g), additions to 3.6(b), 6.5(f), Section 8 and Appendix E. Nothing was renumbered.
- **Compact toy (Supplement S12, last paragraph of Appendix E):** compact U(1) in 2+1 dimensions on a 2 × 2 torus blocked to one site; the lattice gap closes like 1/(2β) and `γ_opt` stays above 0.83; two programs agree to seven figures. The weight of the slow state in the fine detail divided by its energy has a closed form (`1/√8` there; `1/√2 + 1/(2√6)` for the free soft photon in three dimensions, derived in Remark 3.9), and the rate extrapolates to `2(√2 − 1)`. It is a toy. A natural next size (4 × 4 to 2 × 2) has 17 angles and cannot be done on a grid; an SU(2) version needs a spin-network basis and was not attempted.
- **Proposition 5.7 (new):** Hypothesis 3.1 can be replaced by the linear weight bound `‖G E((0,u]) G‖ ≤ c·a·u` for `u ≤ 1/a` with one constant; the refinement step then needs no rate and no a priori gap. This is now the sharpest form of the first open estimate: low-energy states are determined by the coarse field up to a fraction `c·a·u`. Proved for the whole Fock space of the free theory (Proposition E.4, `I − P ≤ c·a·H`, c < 15.94, computed 1.45). Equivalent form of Hypothesis 3.1: `G_i ≤ κ_i H_i` with `Σκ_i < ∞`. Next: the compact toy over all low states; any interacting model where `I − P ≤ κH` can be attacked directly (it is a Poincaré-type inequality: conditional variance given the coarse field bounded by the energy form).
- **Correction to item 4 of section 4 below:** "P_c of order 1/β" is impossible for all functions on the fibre (the constant is at least 1/3, Remark 3.8); it can only be meant for gauge-invariant functions, and bounded constants would already suffice. The target is now the weighted inequality of Proposition 3.7.
- **Tools in a new container.** LaTeX: `apt-get update && apt-get install -y texlive-latex-extra texlive-fonts-recommended texlive-science texlive-pictures cm-super` (without `cm-super` the PDF gets bitmap fonts). Python: `pip install numpy scipy`. Lean: elan with toolchain `leanprover/lean4:v4.19.0`; a project with `lakefile.toml` requiring `mathlib` at `rev = "v4.19.0"`, then `lake update` and `lake exe cache get` (about ten minutes); `lake env lean <file>`. The `pcpos` binary is not available; statement pins are computed with `papers/spectral-criteria/supplement/S7-lean/statement_digest.py` (same convention, seven recorded pins reproduced).
- **External sources.** `git clone --filter=blob:none --no-checkout https://github.com/yang-mills-group/OpenAI-YM-20261028.git`, then `git checkout 3456e5e75cf8d4cd558955a5c7638fba2d68f464 -- README.md YM/EveryPhase/Light.lean YM/EveryPhase/Decay.lean YM/EveryPhase/Extension.lean` fetches only those files. Read and remove; store nothing.
- **Paths and external grounding:** `PATHS.md` in this folder lists five stipulated paths with tests and the outcome that would count against each, and the literature found by search (abstracts only). Start there.
- **Open, in the order I would take them:** (1) any bound, even numerical and for one small lattice, on the quantity `‖Σ^{1/2} M Σ^{1/2}‖` of Proposition 3.7 for gauge-invariant functions of SU(2); (2) an estimate of the low-energy weight `F_i(u)` of Remark 3.9 beyond the free theory; (3) the relation between the external construction's blocking kernel and the coarse field used here; (4) "sum of influences is 2" in `ATTEMPT.md` §4 is still unchecked; (5) items 5 to 7 of section 4 below are unchanged.
- **A mistake of this session:** a convergence predicate compared grid maxima, which do not converge geometrically, with a tolerance meant for integrals. The failed result is kept (`weightedtoy_result.txt`) with a follow-up. Fix the basis of a tolerance per quantity.

## 1. Where things stand

**No mass gap is proved. Never say otherwise.** The interacting hypotheses 3.1, 3.2, 3.3 are open for SU(2); volume uniformity, identification with a continuum theory and all other groups are untouched. Rendezvous issue: `KirtusJ/Millennium-Prize-Problems#1` (keep open). Last comment of mine: 7122902283.

**The paper** (30 pages at commit `7c8cb1b`): `yang-mills/papers/spectral-criteria/`
- reading copy: the PDF with the full title as file name
- source: `source/main.tex`, `source/preamble.tex` (three passes of `pdflatex`; must give no undefined reference and no overfull box)
- supplement: `supplement/S1…S11`, catalogued in `SUPPLEMENT.md` (digests) and in Appendix D of the paper
- change record of every version: `yang-mills/z4/infrared/README.md` (drafts 1 to 6 are there as `main_draft*.tex`)

Structure of the paper: 1 Introduction (two questions; Theorems 1.1 spectral criterion, 1.2 refinement inequality, 1.3 return bound; what is not claimed) · 2 Setting · 3 Outline and open hypotheses (Hyp 3.1 mixing, 3.2 coarse comparison, 3.3 budget; Prop 3.4 conditional prediction; Remark 3.5 how weak the rate may be; Remark 3.6 exact and sufficient forms) · 4–6 proofs (Remark 5.6 second proof; Cor 6.4 vacuum return; Remark 6.5(a)–(f); Remark 6.6 Doob form) · 7 Measurements summary · 8 External construction · 9 What remains (status table) · 10 Provenance, AI use, availability · App A measurements in full · B one-link covariance · C machine-checked parts · D catalogue · E free theory (Props E.1, E.2, E.3).

**Machine-checked (Lean 4.19.0 + Mathlib v4.19.0; files in `supplement/S7-lean/`, pins in `LEAN_PINS.md`):** Theorem 1.1 in bounded-operator rate form (`Criterion.lean`), Proposition 4.2 (`SeparationHilbert.lean`), Theorem 1.2 with longer lag on all non-zero real or complex inner product spaces (`Hilbert.lean`; second proof `Discrete.lean`), algebra of the gate projection (`Gates.lean`), Hilbert-space core of Prop 3.4 (`Prediction.lean`). Not formalised: Theorem 1.3, Lemmas 6.1, 6.2, Prop 6.3, measure theory, Bessel identities, the limsup form and the passage H → e^{−τH}, Remark 3.6, Appendix E.

**Solution attempt:** failed; record with two rounds of outside corrections in `solution-attempt/ATTEMPT.md`. What survived: the rate may be as weak as e^{−cβ}, c < 1/s, if β ≤ s·log(1/a) + const; Hyp 3.1 ⇔ Σ‖G_i H_i⁻¹ G_i‖ < ∞; sufficient form γ ≥ 1/(1 + β² P L) (fibre Poincaré constant × next-slice covariance); in the free theory everything closes (γ ≥ 0.195 proved, 0.675 observed limit; βP → 0.617, βL → 1) and the free theory has no gap, so the refinement architecture cannot by itself give a gap in infinite volume.

**External construction** (cloned read-only this session at `/home/user/yang-mills-group/openai-ym-20261028`, revision `3456e5e`; the clone will be gone): low-energy statements are polynomial (`YM/EveryPhase/Light.lean` `light_bound`, `Decay.lean` `inverse_square`); meshes 1/D_n with odd factors ≥ 3 (not dyadic); mesh limit on a four-torus before volume; coupling slope 11·C_g/(24π²), which is 11/(3π²) for SU(2) in our normalisation. Assessment: `alexisdpc.github.io/yang-mills/references/assessment-1-2026-11-10.pdf`. Never store fetched papers or their text in the repository.

## 2. Standing rules (Principal, as of this session)

- Reports to the Principal: outcomes and blocks only; little chat text; no waiting on background tasks; the paper says only what we have and starts from a consideration, not an assertion.
- **No more PCP worker test rounds** unless asked. Subagents are allowed but were stopped on instruction; do calculations directly.
- No need to push after every small change; batch. (A stop hook still requires a clean tree at the end of a turn.)
- Paper: author line "Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada"; labelled as part of *From Prephysical Hypotheses to Physical Models*; self-citations only when necessary and under their explicit heading; **no working labels (Z4, G4, auditor, session, draft, worker) and no internal folder names in the paper or its PDF**; systems are named (Claude (Anthropic), OpenAI Codex, OpenAI GPT) and are not authors.
- G4 (Codex) is out; A4/B4/C4 inactive; the GPT auditors post on #1 or are relayed by the Principal. Check their points by calculation before adopting, credit them in the paper as "an OpenAI GPT model used as reviewer", and read back on #1.
- Do not touch other directors' folders (`yang-mills/g4/`, `joint-refinement/`) except path strings; S6, S8, S9 in the supplement are copies.
- Git: repository `/home/user/Millennium-Prize-Problems`, default branch `main`; commit with the identity used throughout `git log`; messages end with the Co-Authored-By and Claude-Session lines of the current session; then `git fetch -q origin main && git merge -q --no-edit origin/main && git push -q origin HEAD:main && git push -q origin HEAD:<session branch>`. No model identifier in repository artefacts. GitHub comments through the MCP tools, ending with the "Generated by Claude Code" footer.

## 3. How to do the routine things

**Rebuild and release the paper** (what `fin.sh` did this session; the script was in the scratchpad and is gone):
1. in `papers/spectral-criteria/source`: `pdflatex -interaction=nonstopmode main.tex` three times plus once to read the log; grep for `undefined`, `overfull`, `^!`;
2. `pdftotext main.pdf - | grep -i 'g4\|z4\|auditor\|session\|draft'` must be empty apart from ordinary words;
3. copy `main.pdf` over the reading copy; delete `main.pdf`, `*.aux`, `*.log`, `*.out`, `*.toc` from `source/`;
4. in `SUPPLEMENT.md` replace the two SHA-256 values on the "Reading copy" and "Source" lines;
5. add a line to `z4/infrared/README.md` (new entries go just above "## Sixth draft");
6. commit, merge, push.

**Lean:** the project was at `/home/user/z4-lean` (Lean 4.19.0 via elan, Mathlib v4.19.0 with cache); `export PATH=$HOME/.elan/bin:$PATH; cd /home/user/z4-lean && lake env lean <file>`. If the container is new, recreate: `lake new`-style project with `require mathlib` pinned to `v4.19.0`, `lake exe cache get`. A pass is exit 0, no `sorry`, no warning, axioms `propext`, `Classical.choice`, `Quot.sound`. Lessons: `by_contra h` misbehaved (use `by_contra!` or `rcases eq_or_ne`); `Π` is reserved; use `obtain ⟨x, hx⟩ : ∃ x, x = … := ⟨_, rfl⟩` instead of `set` when later rewrites must not unfold; real parts of complex casts need `rw [← Complex.ofReal_pow]` then `Complex.ofReal_re`.

**Statement pins:** `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos instrument mathematics.statement '{"source":…,"theorem":…,"pinned":…}'` (exit 0 with the right pin, 1 with a wrong one; it cannot read a `let` in a statement). Append to `S7-lean/LEAN_PINS.md` and update the file digest in `SUPPLEMENT.md`.

**Free-theory programs:** `supplement/S11-free-theory/` (`maxwell.py N…`, `worstq.py`, `poscheck.py`, `resolvent_check.py`, `blockr.py`, `bridge.py`); each refuses to overwrite its result file, so run in a fresh directory.

## 4. Open items, in the order I would take them

1. **Nothing is owed on the paper right now.** If it is frozen, the title page has no version label; the date is 24 November 2026.
2. Unverified in `ATTEMPT.md` §4: the hand claims "Bakry–Émery works only at strong coupling" and "sum of influences is 2".
3. The reviewers' suggested next step: look in the external sources for any estimate on the fine-detail inverse energy `G H⁻¹ G` or on blocked-field fluctuations (a name search for "transfer" found nothing relevant; that is not proof of absence).
4. Natural targets for SU(2), none attempted: bounds on the fibre Poincaré constant `P_c` and on `L_c = ‖Cov(next slice | present)‖`, both expected of order 1/β; numerical lower bounds for them would need a sampler with a whole slice frozen.
5. Known gaps in the record: the time carry-over run kept no result file; the second draft's fidelity report was never committed; per-stream data of Table 3 are regenerated from seeds.
6. The two sibling manuscripts (`z4/attempt/paper/`, 57 pages; `z4/attempt/tunnel-note/`, 33 pages) still use process words ("sessions", "workers") and repository-path references. The Principal has not asked for them to be brought to the paper's form.
7. Appendix E is not formalised; Proposition E.2's minimiser is "observed", not proved. (Later: the small-momentum limit is shown to be the same in every direction; what is missing is that the rate at every momentum is at least that limit.)

## 5. Mistakes of mine this session, so they are not repeated

- Reported an archive as deposited when it was never committed; wrote a commit message naming a fix that had not applied (a failed assertion followed by a script that committed anyway). Check exit codes before committing.
- Summaries overstated repeatedly (measurements "show", "has to hold", "cannot work"). Reviewers caught them. State estimates as estimates and heuristics as heuristics.
- A docstring claimed a test (whole subspace) that the code did not do (random vectors).
- Renumbered the paper several times while reviewers were citing numbers; add new items at the end of a section instead.

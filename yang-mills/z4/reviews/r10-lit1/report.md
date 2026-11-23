# Report r10-lit1: literature reader (primary sources opened)

Worker of Director Z4; principal Kirtus Justus. Control: `control.txt` = 0.272341 (−ln tanh 1). The worker, the director and the sub-agent are one model family, so this report is not independent review. Page numbers are PDF page numbers. Where a journal page differs, both are given (Driver: journal p. 479 = PDF p. 1).

## 0. Hypothesis first: the fetched files

| File (ref/) | Source | Bytes | Pages | Text extraction |
|---|---|---|---|---|
| jaffe_witten.pdf | Jaffe and Witten, Clay problem description | 195 976 | 14 | worked (14/14 pages) |
| chatterjee_1803.01950.pdf | Chatterjee, Yang–Mills for probabilists | 205 873 | 17 | worked (17/17) |
| chatterjee_1602.01222.pdf | Chatterjee, leading term of the YM free energy | 477 830 | 49 | worked (49/49) |
| chatterjee_2401.10507.pdf | Chatterjee, SU(2) YM–Higgs scaling limit | 615 120 | 50 | worked (50/50) |
| driver_1987.pdf | Driver, CMP 110 (1987) 479–501 | 2 127 595 | 23 | worked (23/23). The file carries an OCR text layer, so it is not a bare scan. Symbols are damaged (for example "U(1)" comes out as "ί/(l)"), but the statements can be read. |
| dimock_1304.0705.pdf | Dimock, RG according to Balaban III | 424 487 | 37 | worked (37/37) |

All six fetches succeeded (`fetch_log.txt`, K1). Extraction ran as K2 (`extract_summary.txt`; text in `text/`).

## 1. Verdict table

| Item | Verdict | Evidence (one line) |
|---|---|---|
| Q1a Axioms required | STANDS (with a correction to LITERATURE.md) | JW p.6 §4: "at least as strong as those cited in [45, 35]". [45] is Streater–Wightman and [35] is Osterwalder–Schrader. Both are cited, so the official text names OS as well as Wightman, not Wightman only. |
| Q1b What existence includes | STANDS (Z4 omits part of it) | JW p.6 §4: local operators matching gauge-invariant local polynomials in F; short-distance agreement with asymptotic freedom; stress tensor and OPE. JW p.11: a quantum-mechanical Hilbert space. JW fn. 2 p.12: compactness alone excluded. |
| Q1c Mass gap definition | STANDS | JW p.6: H has no spectrum in (0, Δ) for some Δ > 0, and the mass m = sup Δ must be finite. A vacuum unique up to phase is part of the axiom scheme (p.5 §3). |
| Q1d Groups | STANDS | JW p.6: any compact simple G. |
| Q1e Required vs comments | STANDS | §5 pp.6–7 are comments: clustering is a consequence; a uniform finite-volume gap "may play a fundamental role"; the upper gap, confinement, matter theories and 4-manifolds are extensions. None is required. |
| Q1f Z4's requirement list (a)–(f) | DEFECT (omissions) | Z4 omits: the local operator content and short-distance (asymptotic freedom / OPE / stress tensor) agreement; Wightman as an allowed form; finiteness of m; a unique vacuum; the Hilbert space; the compactness exclusion. Details in §3. |
| Q2 Survey: open problems | STANDS | Problems 4.1 (area law, p.8), 5.1 (lattice mass gap with ξ(β) → ∞, p.9), 5.2 (continuum limit of rectangular Wilson loops, p.10). |
| Q2 Osterwalder–Seiler as cited in LITERATURE.md ("reflection positive, mass gap at strong coupling") | PARTLY CONFIRMED | The survey (p.8, p.11) credits O–S with the small-β area law, confinement and a positive self-adjoint transfer matrix. It does not say "mass gap". JW p.11 credits [36] = O–S with reflection positivity of the Wilson approximation. No source read here states the O–S strong-coupling mass gap. |
| Q2 Gross 3D U(1), Driver 4D U(1) | CONFIRMED | Survey p.12. Driver read directly (Q4). |
| Q2 Bałaban 4D UV stability | CONFIRMED, with a scope correction | Survey p.12 and JW p.11 agree. The survey defines UV stability as subsequential convergence (compactness, p.12). JW p.11: the estimates still need extending to expectations of gauge-invariant functions. |
| Q3 Free-energy paper | STANDS (free energy only) | Thm 2.3 p.5: d = 4, n → ∞, ε → 0, g → 0 jointly; computes the leading term of log Z only. No local-observable Gaussian limit (sub-agent; checked by me). |
| Q3 Higgs paper | STANDS | Thm 3.2 p.12: SU(2)+Higgs, αg = cε, g = O(ε^{50d}) → independent Proca fields (Gaussian). Non-Gaussian limit stated open, p.1 (checked by me). |
| Q4 Driver 1987 | STANDS, with a correction to LITERATURE.md | 4D compact U(1): the lattice current converges to a free field with g² renormalized by α (Thm 4.2 p.484). In d = 4 the Gibbs state does not depend on the spacing (p.484), so this is a long-distance scaling limit at fixed coupling, on the current sector only. Unique-Gibbs case: large g² (Lemma 4.1 p.485). |
| Q4 Dimock III | STANDS: φ⁴₃ only, nothing on Yang–Mills | Abstract p.1: scalar φ⁴, d = 3. Theorem 2 / Cor. 1 p.33: a stability bound uniform in the UV cutoff. The words "gauge" and "Yang" do not occur in the text, and no Bałaban YM paper is cited. |
| LITERATURE.md row "Dimock … explains the method" as a source for the 4D YM claim | DEFECT (of the citation, not of the claim) | Dimock III cannot ground any statement about Bałaban's YM results. Grounding for 4D YM UV stability comes from JW p.11 and the survey p.12. |

Counts (met, failed, measured only): script predicates P1 6 met, 0 failed; E1 6 met, 0 failed; E2 6 met, 0 failed. Reading verdicts across the 15 rows: STANDS / CONFIRMED / PARTLY 13, DEFECT 2 (Z4's requirement list omits items; the Dimock citation), NOT CHECKED 0. The sub-items not checked are listed in §9. Sub-agent statements: 3 checked and met (Thm 2.3 p.5, Thm 3.2 p.12, abstract p.1), 0 failed, the rest taken as reported. Final register: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`.

## 2. Hypotheses each statement uses, and where they are stated

- **JW problem** (p.6): G compact simple; space-time ℝ⁴; axioms at least as strong as Wightman [45] / OS [35]; nontriviality; Δ > 0 with m < ∞. Axiom content (p.5): Poincaré representation, positive energy 0 ≤ H, vacuum unique up to phase, locality.
- **Osterwalder–Seiler** (as reported, survey p.11 and p.8; JW p.11): small β (strong coupling), any dimension, any compact group. The paper itself was not opened.
- **Driver Thm 4.2** (p.484): d = 4; compact U(1) with a C² even periodic energy function h; uniqueness of the Gibbs state for g⁻²h; closed test 2-forms. That is, the current sector J = d*F. Lemma 4.1 (p.485) gives uniqueness when sup h − inf h < 2g²/9. Thm 4.3: any extreme, translation- and 90°-rotation-invariant Gibbs state. Thm 4.5: Wilson-like h, all but countably many g.
- **Dimock Thm 2** (p.33): scalar φ⁴ on the torus (L^{−N}ℤ/L^Mℤ)³; μ̄ = 1; λ small; counterterms ε, μ chosen; L and M large (Theorem 1, p.3).
- **Bałaban UV stability** (survey p.12; JW p.11): 3D on a periodic lattice, and its extension to 4D. As the survey describes it, the result is compactness of the effective theories (subsequential convergence), not convergence of correlation functions.

## 3. Q1 in detail: Jaffe–Witten against OVERALL_DISPOSITION.md §2 "Against the requirements"

What the text requires (p.6 §4 unless stated otherwise):
1. G is any compact simple group, and the theory is on ℝ⁴.
2. A quantum field theory in the sense of §3 (p.5): a Hilbert space with a positive-energy Poincaré representation, a vacuum unique up to phase, and locality. Axioms "at least as strong as" Streater–Wightman [45] and Osterwalder–Schrader [35]. Both are cited, and either a Wightman or a Euclidean OS construction is evidently acceptable, since §3 p.5 presents them as equivalent schemes.
3. Local quantum field operators that correspond to the gauge-invariant local polynomials in F and its covariant derivatives (with footnote 1 on renormalization subtleties, p.6).
4. Correlation functions that agree at short distances with asymptotic freedom and perturbative renormalization theory, including a stress tensor and an OPE with the predicted singularities.
5. Nontriviality.
6. A mass gap: no spectrum of H in (0, Δ) for some Δ > 0, and m = sup Δ < ∞.
7. Footnote 2 p.12: weak existence (compactness) does not count unless the properties of the limit are established by other means.
8. p.11: establishing a quantum-mechanical Hilbert space is part of the solution.

Comments, not requirements (§5 pp.6–7): clustering (a consequence of the gap); a uniform finite-volume gap (a possible route); the upper gap / isolated one-particle state, confinement, other gauge theories, and arbitrary 4-manifolds ("natural extensions").

Known results as JW state them: no nontrivial 4D QFT satisfies the Wightman or any reasonable axioms (p.7). There are partial results for YM on T⁴, and present ideas give no route to a volume-uniform gap or to T⁴ → ℝ⁴ (p.7, p.12). P(φ)₂ and φ⁴₃ have been constructed (pp.8–9). BFS 2D abelian Higgs satisfies the OS axioms and is "the only complete example of an interacting gauge theory satisfying the axioms" (p.11); a mass gap there is [4]. Wilson lattice: reflection positivity holds [36] (p.11). Bałaban: 3D UV stability uniform in the spacing (p.11), extended to 4D [3] (p.11), still to be extended to expectations of gauge-invariant functions (p.11). Magnen–Rivasseau–Sénéor: continuum regularization (p.12, ref. [29]: YM₄ with an infrared cutoff).

Differences between Z4's list (a)–(f) and the text:

| # | Difference | Direction | Page |
|---|---|---|---|
| D1 | (b) names only "Reflection positivity, Osterwalder–Schrader axioms". The text cites both Wightman [45] and OS [35], "at least as strong as". | Z4 narrower (not wrong, incomplete) | p.6 |
| D2 | Z4 omits that the local operators must correspond to the gauge-invariant polynomials in F and covariant derivatives. | text requires, Z4 omits | p.6 |
| D3 | Z4 omits short-distance agreement with asymptotic freedom / perturbative renormalization, including a stress tensor and OPE. This is the requirement that ties the construction to Yang–Mills and not merely to some theory. | text requires, Z4 omits | p.6 |
| D4 | (e) "Mass gap > 0 in physical units": the text also requires m = sup Δ < ∞. | text requires, Z4 omits | p.6 |
| D5 | Uniqueness of the vacuum (up to phase) is part of the axioms the text refers to. Z4 does not list it. | text (via axioms), Z4 omits | p.5 |
| D6 | Footnote 2: compactness/weak existence is excluded unless the gap and axioms are established for the limit. Z4's (a) "Continuum limit on ℝ⁴" does not state this. | text requires, Z4 omits | p.12 |
| D7 | "Establishing a quantum mechanical Hilbert space is part of the solution." Z4's (b) covers it only implicitly through OS. | text, implicit in Z4 | p.11 |
| D8 | (c) Euclidean invariance and (d) nontriviality are in the text: Euclidean/Poincaré invariance through the axioms (p.5), and nontriviality at p.6. | agree | p.5, p.6 |
| D9 | (f) "All compact simple groups": the text says "for any compact simple gauge group G", the same. Note that Z4's state column cites results for "compact connected groups". Those include U(1) and non-simple groups and are a different class, which is harmless. | agree | p.6 |
| D10 | Z4 lists no requirement that the text does not make. Nothing in (a)–(f) goes beyond JW. Z4 says nothing that implies a uniform finite-volume gap is required (JW p.6 calls it a possible route). | none | — |

LITERATURE.md row 1 says secondary sources name "Wightman" and that the OS form "should be checked against the official text". Result: the official text cites OS [35] alongside Streater–Wightman [45] (p.6) and explains the Euclidean–Lorentzian equivalence (p.5). Using OS is consistent with the text.

## 4. Q2 in detail: Chatterjee, "Yang–Mills for probabilists" (17 pp, 2018)

Open problems as he numbers them:
- **Problem 4.1 (Area law)**, p.8: compact non-abelian G ⊆ U(N), N ≥ 2; 4D lattice, any infinite-volume limit, any β; |⟨W_{R,T}⟩| ≤ C(β)e^{−c(β)RT}.
- **Problem 5.1 (Mass gap)**, p.9: same setting; the plaquette–plaquette correlation decays with a finite correlation length ξ(β) ∈ (0, ∞) for every β > 0, and ξ(β) → ∞ as β → ∞. This is a lattice problem and is not the Clay problem.
- **Problem 5.2 (Continuum limit)**, p.10: as β → ∞ there exist ε(β) → 0, c(β) → ∞ and d ≠ 0 with log⟨W_{R/ε,T/ε}⟩ = −c(R+T) − dRT + o(1).
- Also stated as open in the text: how β must scale with ε in 4D (believed log(1/ε); "an open mathematical problem", p.6); uniqueness of the infinite-volume limit at large β for d > 2 (p.4); no continuum limit in any d > 2 with nontrivial Wilson-loop behaviour (p.12).

Known results reviewed (one line each, as he states them):
- Osterwalder–Seiler [72]: area law at small β for any lattice gauge theory (p.8); at strong coupling in any dimension, confinement and a positive self-adjoint transfer matrix (p.11).
- Guth [53]; Fröhlich–Spencer [44]: 4D U(1) has no area law at large β (Guth physics-level, F–S fully rigorous) (p.8).
- Göpfert–Mack [47]: 3D U(1) area law at every β (p.8). Non-abelian area law at large β is known only in 2D (p.8).
- Borgs [17]: confinement/deconfinement at weak coupling, 3D/4D (p.11).
- Brydges–Fröhlich–Seiler [20–22]: 2D U(1) Higgs model constructed (p.11). Borgs–Seiler developed it further.
- Gross–King–Sengupta, Driver (lassos), Klimek–Kondracki, Fine, Witten, Sengupta, Lévy: 2D Yang–Mills, general compact groups (p.11). Nguyen: 2D perturbative vs exact. Lévy; Driver–Hall–Kemp; Driver–Gabriel–Hall–Kemp; Driver: Makeenko–Migdal equations in 2D (p.11).
- 't Hooft-type expansions at strong coupling: Chatterjee, Chatterjee–Jafarov, Basu–Ganguly, Jafarov (p.11).
- King [56, 57]: continuum limit (and infinite-volume limit) of the 3D (U(1)) Higgs model by phase-cell renormalization (p.12).
- Gross [49]: continuum limit of pure U(1) in 3D, "with a different notion of convergence" (p.12).
- Driver [29]: continuum limit of 4D U(1) lattice gauge theory, by Gross's approach (p.12).
- Bałaban [1–14]: UV stability of 3D and 4D non-abelian lattice gauge theories by phase-cell RG (p.12). UV stability is defined as existence of a convergent subsequence (p.12).
- Federbush; Federbush–Williamson: phase-cell approach (p.12).
- Magnen–Rivasseau–Sénéor [67]: a direct continuum program for YM₄. Gauge invariance is broken by a quadratic regulator and restored in a limit; the reference title says "with an infrared cutoff" (p.12).
- Charalambous–Gross, Gross: Yang–Mills heat-flow regularization in ℝ³, with Lüscher's flow as a similar idea (p.13). This is a proposal, not a result.
- Summary sentence, p.12: there is no continuum limit in any dimension above two in which Wilson loops have been shown to behave nontrivially.

Survey against the repository texts:

| Repository statement | Survey says | Verdict |
|---|---|---|
| OVERALL_DISPOSITION §2 "common wall": what is proved needs strong coupling or a fixed mesh; this is the known central difficulty | p.12: no continuum limit in d > 2 with nontrivial Wilson loops; Problems 5.1/5.2 open | CONFIRMED |
| OVERALL_DISPOSITION §5.1: "the literature has none [no weak-coupling estimate for a fixed-size observable] in four dimensions" | p.12: Bałaban's 4D UV stability is a weak-coupling RG result, but for effective actions and subsequential convergence | LITERATURE.md's scoping is CONFIRMED. The original sentence is too strong if "estimate" includes effective-action bounds, and correct if it means control of a fixed-size observable's correlations. |
| LITERATURE.md: O–S 1978, "reflection positive, mass gap at strong coupling, SU(N) confines" | p.8, p.11: area law / confinement and a positive self-adjoint transfer matrix at small β. No "mass gap" wording | PARTLY CONFIRMED. The mass-gap part was NOT FOUND in the survey. The transfer matrix is consistent with RP (RP itself: JW p.11). |
| LITERATURE.md: Gross (U(1), 3D) and Driver (U(1), 4D) continuum limits | p.12 | CONFIRMED |
| LITERATURE.md: Bałaban gives "ultraviolet stability bounds for 4D lattice YM in a small-field regime" | p.12: UV stability, 3D and 4D, phase-cell RG. "Small field" is not in the survey (it is in JW's ref. [3] title, p.13) | CONFIRMED at survey level |
| LITERATURE.md: survey "all central questions open" | Problems 4.1, 5.1, 5.2 open (pp.8–10, 12) | CONFIRMED |
| LITERATURE.md: gradient flow is the "established" fixed-size observable | p.13 mentions YM heat flow (Gross, Charalambous–Gross) and Lüscher only as a promising regularization in 3D | NOT CONTRADICTED. The survey presents it as a hope, not as established mathematics; "established" holds in lattice physics, not in rigorous work. |
| OVERALL_DISPOSITION (b): reflection positivity at fixed regulator is in the territory of O–S | The survey does not say "reflection positivity". JW p.11 does ([36] = O–S) | CONFIRMED via JW |

## 5. Q3 (delegated) and Q4

Q3 is filled in from the sub-agent's report after rereading (see §7).

**Driver 1987 (CMP 110, 479–501).** Setting: compact U(1) lattice gauge theory on ℤ⁴, with a general C² even 2π-periodic energy function h (Wilson, Villain, Wilson-like; §3, p.482). The lattice approximation at spacing a with coupling g is a Gibbs state for g⁻²a^{d−4}h (Def. 3.2, p.483). In d = 4 this does not depend on a, and only the test forms φ_a are scaled (p.484). Main theorem (Thm 4.2, p.484): if the Gibbs state for g⁻²h is unique, then for every closed test 2-form φ, the Laplace transform of (F, φ_a), where F = h′(dω), converges as a → 0 to that of the free Euclidean electromagnetic field with g² renormalized by α = μ(h″) > 0 (α = 0 only for constant h). Uniqueness holds by Dobrushin when sup h − inf h < 2g²/9, that is, at large coupling (Lemma 4.1, p.485). Thm 4.3 gives the same limit for any extreme translation- and 90°-rotation-invariant state, and such a state exists for Wilson-like h at every coupling (Thm 4.4, Messager et al.). Thm 4.5 gives independence of the state for all but countably many g. In d > 4 the current-sector limit is trivial, a δ at 0 (Thm 4.1, p.484). Only the current J = d*F is treated, which avoids lattice monopoles (p.480). The limit is Gaussian.

**Dimock III (arXiv 1304.0705).** This is plainly scalar φ⁴ in three dimensions on a toroidal lattice (abstract, p.1), not a gauge theory. Main result (Thm 2, p.33): for λ small and μ̄ = 1, with suitably chosen counterterms, the partition function is Z_{M,N} = Z_{M,N}(0)·exp(ΣH(X)) with polymer bounds |H(X)| ≤ O(1)λ^{β/2}e^{−κ₀d_M(X)}. Corollary 1 (p.33) is the stability bound exp(±λ^η Vol), uniform in the UV cutoff N and the volume parameter M. The author says these bounds are not new and that the aim is to illustrate Bałaban's method (p.2). Correlation functions get only a remark (p.33). On Bałaban's Yang–Mills results it says nothing: no occurrence of "gauge" or "Yang", and none of Bałaban's YM papers is in its bibliography, whose Bałaban items are Higgs₂,₃, Green's functions and N-vector models (pp.35–36).

## 6. Q5: claim in the repository → what the literature read here says

| Claim | What the sources read here state | Mark |
|---|---|---|
| (i) Reflection positivity and a strong-coupling gap on the lattice (G4 slab RP; B4 strong-coupling transfer bounds) | RP of the Wilson approximation: JW p.11, citing Osterwalder–Seiler 1978. Strong coupling: O–S prove confinement and a positive self-adjoint transfer matrix (survey p.11) and the small-β area law (survey p.8). A strong-coupling *mass gap* attributed to O–S is not stated in either source read. | READ (RP JW p.11; transfer matrix survey p.11). The gap part: NOT FOUND |
| (ii) Gaussian weak-coupling limits at fixed lattice scale | Free-energy paper and Higgs paper: see §7 (sub-agent and my checks). Driver: a Gaussian limit, but at *fixed* coupling as a long-distance scaling of U(1)₄ (p.484), not a weak-coupling limit. | READ (Driver p.484). Chatterjee: see §7 |
| (iii) Continuum limit of abelian lattice gauge theory | Gross 3D U(1) (survey p.12; Driver p.480). Driver 4D U(1), current sector, free renormalized limit (Thm 4.2, p.484). King 3D U(1) Higgs, non-compact approximation (survey p.12; Driver p.480). BFS 2D abelian Higgs with OS axioms (JW p.11; survey p.11). | READ |
| (iv) Ultraviolet stability in 4D | Bałaban 4D (JW p.11; survey p.12), meaning compactness / effective actions, still to be extended to gauge-invariant expectations (JW p.11). MRS YM₄ with infrared cutoff (JW p.12; survey p.12). Dimock III covers only φ⁴₃ (p.1, p.33). | READ (JW p.11, survey p.12). Bałaban's papers themselves were not read. |
| (v) What is open | JW: the whole problem; volume-uniform gap and T⁴ → ℝ⁴ need new ideas (p.7, p.12); no nontrivial 4D QFT known (p.7). Survey: Problems 4.1, 5.1, 5.2 (pp.8–10); β(ε) scaling (p.6); no nontrivial continuum limit in d > 2 (p.12). Higgs paper: non-Gaussian limit (see §7). | READ |

## 7. Delegated question and outcome

**Question delegated.** Q3, with the two PDFs copied into child/ref. The sub-agent was asked to answer the control −ln tanh 1 first, keep its own register child/pcp, and state each main theorem with pages and the author's words on non-Gaussian limits.

**What came back.** The control was 0.272341, which is correct. The harness refused child/report.md for the sub-agent, so its content is in child/notes.md. Its register replays: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`. Its answers were:
- **Free energy (1602.01222).** Theorem 2.1 (pp.3–4) is for U(N) Wilson lattice gauge theory, any N ≥ 1 and d ≥ 2, with box size n → ∞ and coupling g → 0. It gives the leading term of log Z: an explicit N² log g² term plus constants, including K_d from an axial-gauge log-determinant. Theorem 2.2 (p.4) covers d = 2, 3 for the continuum-scaled lattice at fixed g. Theorem 2.3 (p.5) covers d = 4 only with g → 0 as well. **Only the free energy is computed.** There is no result on Wilson loops or local correlations, and "Wilson loop" does not occur in the text. Gaussian behaviour appears only as the mechanism of the proof.
- **Higgs (2401.10507).** Theorem 3.2 (p.12), any d ≥ 2: SU(2) lattice YM with a Higgs field, unitary gauge, ε → 0, αg = cε, g = O(ε^{50d}). The rescaled gauge field converges in law to three independent Euclidean Proca fields, a massive Gaussian field. Theorem 3.1 is the U(1) analogue. Abstract p.1: "The question of constructing a non-Gaussian scaling limit remains open." §3.5 (p.16): more slowly decaying g might show non-abelian effects.

**My checks (two statements, against the text).**
1. Free-energy Theorem 2.3, PDF p.5. Confirmed: d = 4; n → ∞, ε → 0 and g → 0 simultaneously, with no restriction on how they are related; the conclusion is a formula for log Z(n, ε, g) up to o(n⁴). My grep for "wilson loop" in the extracted text gives 0 hits, which agrees with "free energy only".
2. Higgs Theorem 3.2, PDF p.12. Confirmed: any d ≥ 2, αg = cε, g = O(ε^{50d}), convergence in law to independent Euclidean Proca fields. The abstract sentence on the non-Gaussian limit is on p.1 (text line 21).
I did not check the sub-agent's p.16 statement or its constants (K_d, the mass c/√2).

**Bearing on the repository.** LITERATURE.md row "Leading weak-coupling free energy" is CONFIRMED, with a sharpening: the paper gives no Gaussian limit for local observables, so it supports the repository's Gaussian structures only at the level of log Z. The row "A non-Gaussian limit is open" is CONFIRMED (p.1). The trajectory g = O(ε^{50d}) (p.12) is concrete support for LITERATURE.md's reading that the coupling "vanishes too fast for anything else". Q5 row (ii): READ (free energy p.5; Higgs p.12, p.1).

## 8. Failed predicates

None of the script predicates failed (P1, E1, E2 all met). My own expectation that Driver 1987 might be a scan without text was wrong: the file has an OCR layer. The expectation failed, the target did not. Reading expectations that failed:
- LITERATURE.md's attribution of a strong-coupling mass gap to O–S was not found in the two sources that discuss O–S. This is a defect of the earlier summary, or at least it is unsupported here.
- LITERATURE.md's description of Driver ("converges to a renormalized (free) continuum theory") is accurate, but it leaves out that in d = 4 the coupling stays fixed and only the test functions scale, and that only the current sector is treated.
- LITERATURE.md uses Dimock as an exposition relevant to 4D YM UV stability. Dimock III contains nothing on gauge theories.

## 9. What I did not check

- Osterwalder–Seiler 1978, Bałaban's papers, Magnen–Rivasseau–Sénéor, Gross 1983, King, BFS and Faria da Veiga–O'Carroll were not opened (not in the permitted list). Every statement about them is second-hand, from JW or the survey.
- The Driver OCR text was read for the statements in §3–4 of that paper. The proofs (§§5–8) were not read.
- Dimock: only the theorem statements (pp.1–4, 33), plus a grep of the whole text for gauge/Yang/Bałaban.
- Free-energy and Higgs papers: only through the sub-agent, plus the two statements I checked (§7).
- LITERATURE.md §2–4 rows on the Wilson-loop perimeter law, gradient flow, the Mihajlovic preprint and string tensions: no permitted source covers them.

## 10. Commands to rerun

From `C:/Users/donke/z4-workers/r10-lit1`, with `PYTHONUTF8=1`:
```
python -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py init pcp --principal principal --principal-name "Kirtus Justus"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name fetch --expect-exit 0 -- sh tools/fetch.sh
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name extract --expect-exit 0 -- python -I tools/extract.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```
(fetch.sh skips files already present, and extract.py writes text/<name>.N.txt when an output exists, so reruns overwrite nothing.) For the sub-agent, see child/report.md.

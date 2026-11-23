# r11-lit report (literature reader, Director Z4)

Control: `control.txt` = 0.272341 (= −ln tanh 1).
"FULL TEXT" below means: arXiv PDF downloaded to the session scratchpad (not this directory), converted with pdftotext, and the stated locator read there. Short quotations are at most two sentences.

## 1. Verdict table

| # | Item (claim relevant to Z4) | Verdict | One line of evidence |
|---|---|---|---|
| 1 | Lattice work uses a spatial-only (3D) gradient flow | STANDS | Sakai & Sasaki, PRD 107, 034510 (arXiv:2211.15176), Sec. II.B, eqs. (3)–(4): the "spatial gradient flow" evolves only the spatial links under the spatial Wilson plaquette action, with R_d = √(6τ). |
| 2 | 4D flow distorts the correlator at t < R_d; spatial flow does not | STANDS (numerical only) | Same paper, Sec. V, eq. (13) and Figs. 4–5: with 4D flow the effective mass rises linearly from 0 for t < R_d. Their reading: the two smeared operators overlap. They make no statement on positivity ("positiv"/"reflection": 0 hits). |
| 3 | A published statement that flowed observables are (or are not) reflection positive | NOT CHECKED (NOT FOUND) | 0 hits for "reflection", "transfer matrix" or "positiv[ity]" in Lüscher 1006.4518, Lüscher–Weisz 1101.0963 and Lüscher 1302.5246. Sakai–Sasaki eq. (17) only says the GEVP eigenvalue "corresponds to the eigenvalue of the transfer matrix". |
| 4 | Rigorous side: the 3D YM heat flow used as a gauge-invariant regulariser of observables | STANDS (as a programme; proved on 3D manifolds and tori only, not on time slices of a 4D theory) | Charalambous–Gross 1004.1639, Sec. 1: they propose it. Cao–Chatterjee 2111.12813, Thm 1.6 and 1.16, plus 2111.10652, Thm 1.19 and Cor. 1.22. CCHS 2201.03487, Thm 1.2 and Remark 1.3. |
| 5 | t²⟨E⟩ = 3(N²−1)g²/(128π²) at leading order | STANDS | Lüscher 1006.4518v3, eq. (2.32) (MS-bar, dimensional regularisation, one loop). |
| 6 | Flowed fields are finite to all orders | STANDS for the 4D flow only | Lüscher–Weisz 1101.0963: abstract, Sec. 7 and Sec. 8.2. The proof is all loop orders, dimensional regularisation, pure SU(N), and uses a local (4+1)-dimensional field theory. It says nothing about a 3D flow. |
| 7 | SU(2) Wilson action: a√σ at β = 2.3, 2.4, 2.5 | STANDS | 0.3690(30), 0.2660(20), 0.1905(8): Fingberg–Heller–Karsch, hep-lat/9208012, Table 3 (this table compiles other groups' data). Found by the child; I re-read it myself. |
| 8 | Average plaquette at exactly β = 2.3, 2.4, 2.5 | NOT CHECKED (NOT FOUND at these β) | The same paper's Table 8 gives 1−⟨U_p⟩ only at β = 2.2986 (0.39746), 2.4265 (0.36352) and 2.5115 (0.34564). |
| 9 | Continuum m(0++)/√σ for SU(2) | STANDS | 3.78(7): Lucini–Teper–Wenger, hep-lat/0404008, Table 14. Found by the child and the grandchild; I re-read it myself. |
| 10 | The spatially flowed density has a continuum-finite correlator at zero time separation | NOT CHECKED (NOT FOUND; open) | No source found. The Lüscher–Weisz finiteness argument does not carry over as stated (see Section 7). |
| 11 | In d = 4, time-zero fields smeared only in space are well defined (free field yes; Wick square at sharp time?) | NOT CHECKED (no locator read) | Glimm–Jaffe was not available online. Jäkel–Wreszinski 2002.09312, abstract only: "the interacting fields cannot in general be restricted to sharp times, as is known from model studies". |

Verdict counts: **STANDS 6, DEFECT 0, NOT CHECKED 5.**

## 2. Tables per question

### Q1. Spatial-only flow in the lattice literature

| Statement | Source | Locator | How read |
|---|---|---|---|
| A "spatial gradient flow" evolves only the spatial links V_i under the spatial part of the Wilson plaquette action; the diffusion radius is R_d = √(6τ). | https://arxiv.org/abs/2211.15176 — K. Sakai, S. Sasaki, "Glueball spectroscopy in lattice QCD using gradient flow", Phys. Rev. D 107, 034510 (2023). The journal reference was confirmed through the inspirehep API. | Sec. II.B, eqs. (3) and (4) | FULL TEXT |
| They use both flows: the original 4D flow (eq. (2), R_d = √(8τ)) and the spatial flow, and they adopt the spatial flow. | same | Sec. II.A, eq. (2); Secs. V and VI | FULL TEXT |
| With the 4D flow, the correlator at t < R_d suffers from the overlap of the two space-time-smeared operators. A Gaussian C(t) gives M_eff ≈ t′/R_d² (eq. (13)). With the spatial flow, the plateau starts earlier and does not depend on the flow time once R_d/a > 6.71. | same | Sec. V, eq. (13), Figs. 4 and 5 | FULL TEXT |
| The GEVP eigenvalue λ_n = e^{−(t−t0)M_n} "corresponds to the eigenvalue of the transfer matrix between two time slices". This is the only transfer-matrix statement; reflection positivity is not mentioned. | same | Sec. III, eq. (17) | FULL TEXT (grep: 0 hits for "positiv" or "reflection") |
| The spatial flow is numerically equivalent to 3D stout smearing at matched diffusion radius. | same | Sec. V, the paragraph after Fig. 6 | FULL TEXT (read in part) |
| Earlier proceedings by the same authors: PoS LATTICE2021, 333. Prior 4D-flow glueball work with over-smearing: Chowdhury, Harindranath, Maiti, JHEP 02 (2016) 134. | same | reference list [11], [12] | FULL TEXT (reference list only; neither paper was read) |

I found no other paper stating that APE or stout smearing in time spoils the spectral decomposition. The usual lattice practice is to smear only spatial links (APE, stout, and the spatial-link Wilson loops in Sakai–Sasaki Sec. IV). That last point is FROM MEMORY apart from Sakai–Sasaki Sec. IV.

### Q2. Rigorous constructions

| Statement | Source | Locator | How read |
|---|---|---|---|
| **Dimension and space:** 3D unit torus. **Group:** compact Lie group (g-valued). **Object:** a state space X of "random distributional gauge orbits", defined by the YM heat flow (following Charalambous and Gross). **Thm 1.6:** if S_YM(X_n(t)) is tight for every t > 0, a subsequence converges weakly to a probability measure on X. **Thm 1.16:** existence of a "gauge invariant free field". **Abstract:** regularised Wilson loops exist under the GFF assumption. | https://arxiv.org/abs/2111.12813 — S. Cao, S. Chatterjee, "A state space for 3D Euclidean Yang–Mills theories", 2021 (v4 2023) | Abstract; Thm 1.6; Remark 1.7; Thm 1.16; Sec. 1.9 | FULL TEXT (theorem statements read) |
| Local solutions of the YM heat flow in DeTurck gauge. **Thm 1.2:** smooth data. **Thm 1.19:** random distributional data under Assumptions (A)–(…). **Cor. 1.22:** this covers the 3D g-valued GFF on T³. | https://arxiv.org/abs/2111.10652 — S. Cao, S. Chatterjee, "The Yang–Mills heat flow with random distributional initial data", 2021 (v4 2022) | Abstract; Thm 1.2; Thm 1.19; Cor. 1.22 | FULL TEXT (statements located; Thm 1.19 hypotheses not read in full) |
| YM heat equation on a compact 3-manifold with boundary; existence and uniqueness for H¹ data. **Thm 2.7:** Dirichlet boundary conditions. **Thm 2.12:** Marini boundary conditions. **Thm 2.14:** Neumann boundary conditions. **Sec. 1:** the YM heat equation "provides a gauge invariant regularization procedure for a connection form A0" even for distributional A0. Infinite propagation speed makes A0 ↦ W_γ(A(t)) non-local, so local observables come from solving on a bounded set O ⊂ R³. | https://arxiv.org/abs/1004.1639 — N. Charalambous, L. Gross, "The Yang–Mills heat semigroup on three-manifolds with boundary", Comm. Math. Phys. 317 (2013) 727 (journal data SUMMARY ONLY, from search) | Sec. 1 (introduction); Thm 2.7, 2.12, 2.14 | FULL TEXT (intro and theorem headers) |
| Existence and uniqueness over R³ or a bounded convex set, for H^{1/2} (critical) initial data. **Thm 2.10:** a > 1/2. **Thm 2.11:** a = 1/2. **Sec. 1:** the aim is gauge-invariant functions of distributional initial data for QFT. "Finite action" is motivated because A0 then extends to a time interval in Minkowski space, so R³ is a spatial slice. | https://arxiv.org/abs/1606.04151 — L. Gross, "The Yang–Mills heat equation with finite action in three dimensions", 2016 (v2 2017; Memoirs AMS per arXiv) | Abstract; Sec. 1, the text around (1.9); Thm 2.10, 2.11 | FULL TEXT (intro and theorem headers) |
| YMH on T³ (3D Euclidean space-time). **Thm 1.2:** a state space S on which the DeTurck–YMH heat flow F_t extends continuously. **Remark 1.3:** gauge-invariant observables (Wilson loops etc.) have "smoothened" versions obtained by precomposing with the flow F̃_t; these separate gauge orbits (Sec. 2.8). **Thm 1.7:** local existence. **Thm 1.9:** gauge covariance of the SPDE. | https://arxiv.org/abs/2201.03487 — A. Chandra, I. Chevyrev, M. Hairer, H. Shen, "Stochastic quantisation of Yang–Mills–Higgs in 3D", 2022 (v2 2024) | Thm 1.2, Remark 1.3, Thm 1.7, Thm 1.9, Sec. 2.8 | FULL TEXT (statements) |
| 2D: a Banach space Ω¹_α of distributional 1-forms on which holonomies and Wilson loops are defined directly. In 2D no regularising flow is needed for observables. | https://arxiv.org/abs/2006.04987 — Chandra, Chevyrev, Hairer, Shen, "Langevin dynamic for the 2D Yang–Mills measure", 2020 (v3 2022) | Abstract; Thm 2.1; line about Wilson loops "well-defined" after Thm 2.4 | FULL TEXT (Thm 2.1 read in part) |

Answer: yes. The heat flow of a 3D connection as a gauge-invariant regulariser is exactly the Charalambous–Gross programme, carried out by Cao–Chatterjee and CCHS. All of these results are for 3D Euclidean space(-time) or spatial initial data. None of them treats the time-zero slice of the 4D Yang–Mills measure.

### Q3. Lüscher; Lüscher–Weisz

| Statement | Source | Locator | How read |
|---|---|---|---|
| ⟨E⟩ = 3(N²−1)g²/(128π²t²)·(1 + c̄1 g² + O(g⁴)), in MS-bar with dimensional regularisation (eq. (2.30)). To this order ⟨E⟩ needs no renormalisation. In terms of α: eq. (2.34). | https://arxiv.org/abs/1006.4518 — M. Lüscher, "Properties and uses of the Wilson flow in lattice QCD", JHEP 08 (2010) 071 [erratum 03 (2014) 092] | Sec. 2.6, eqs. (2.32), (2.33), (2.34) | FULL TEXT |
| That positive-flow-time fields are smooth renormalised fields is a *conjecture* there, supported numerically. An all-order analysis "will probably be required". | same | Sec. 3.5(a); concluding section | FULL TEXT |
| To all loop orders, for any matter multiplet, correlation functions of the flowed field are finite after the usual 4D renormalisation. The proof uses pure SU(N), dimensional regularisation and a local field theory on R⁴×[0,∞) with BRS symmetry; the general case is said to be "straightforward" (Sec. 8). | https://arxiv.org/abs/1101.0963 — M. Lüscher, P. Weisz, "Perturbative analysis of the gradient flow in non-abelian gauge theories", JHEP 02 (2011) 051 (journal data FROM MEMORY; arXiv id read) | Abstract; Sec. 7 (7.1–7.4); Sec. 8.2 | FULL TEXT |
| Gauge-invariant local fields need no renormalisation at positive flow time (Sec. 8.2, eqs. (8.5)–(8.6)). | same | Sec. 8.2 | FULL TEXT |
| Reflection positivity or the transfer matrix of flowed observables | 1006.4518, 1101.0963, 1302.5246 | — | FULL TEXT grep: **not mentioned** |

### Q4. SU(2) Wilson action (child result, re-read by me)

| Statement | Source | Locator | How read |
|---|---|---|---|
| a√σ = 0.3690(30) at β = 2.30 (10⁴ lattice), 0.2660(20) at β = 2.40 (16⁴), 0.1905(8) at β = 2.50 (32⁴) | https://arxiv.org/abs/hep-lat/9208012 — J. Fingberg, U. Heller, F. Karsch, "Scaling and asymptotic scaling in the SU(2) gauge theory", Nucl. Phys. B392 (1993) 493 (journal page FROM MEMORY) | Table 3. This is a compilation; the original measurements are in that paper's references, which I did not read. | FULL TEXT (child and me) |
| Average plaquette: not tabulated at 2.3, 2.4, 2.5. Table 8 lists 1−⟨U_p⟩ (U_p = N⁻¹ Tr): 0.39746(1) at 2.2986, 0.36352(1) at 2.4265, 0.34564(1) at 2.5115. | same | Table 8 (App. B) | FULL TEXT |
| Continuum m(0++)/√σ for SU(2) = 3.78(7); at fixed a ≈ 0.2/√σ it is 3.493(56) (Table 15, not the continuum value). | https://arxiv.org/abs/hep-lat/0404008 — B. Lucini, M. Teper, U. Wenger, "Glueballs and k-strings in SU(N) gauge theories: calculations with improved operators", JHEP 06 (2004) 012 (journal data FROM MEMORY) | Table 14 (O(a²) extrapolation, Sec. 5.1) | FULL TEXT |

### Q5. Continuum finiteness of the spatially flowed density at zero time separation

| Statement | Source | Locator | How read |
|---|---|---|---|
| NOT FOUND. Searched the web for: "spatial gradient flow" / "three-dimensional gradient flow" with renormalization, composite operator, time direction. Only 4D-flow renormalisation papers came up (e.g. Monahan et al., 2201.09740; Carosso–Hasenfratz–Neil, 1806.01385). | — | — | SUMMARY ONLY |
| Finiteness at coinciding points is proved only for the 4D flow, by power counting in the 4+1-dimensional theory. | Lüscher–Weisz 1101.0963 | Sec. 7; Sec. 8.2 | FULL TEXT |
| At positive flow time, the absence of short-distance singularities "derives from the smoothing property of the flow equations". | Lüscher 1302.5246, "Chiral symmetry and the Yang–Mills gradient flow" | Sec. 2, after eq. (2.14) | FULL TEXT |

### Q6. Time-zero fields smeared only in space

| Statement | Source | Locator | How read |
|---|---|---|---|
| "the interacting fields cannot in general be restricted to sharp times, as is known from model studies". This is a statement about interacting fields; no model is named in the abstract. | https://arxiv.org/abs/2002.09312 — C. D. Jäkel, W. F. Wreszinski, "A criterion to characterize interacting theories in the Wightman framework", 2020 | Abstract. Sec. 3.1 / Prop. 3.2 give the Källén–Lehmann decomposition dρ = Zδ + dσ. | ABSTRACT ONLY for the sharp-time claim; Prop. 3.2 FULL TEXT |
| Glimm–Jaffe, *Quantum Physics*: statement on time-zero free fields and Wick powers | — | not read | FROM MEMORY — not used |

## 3. Hypotheses each statement uses, and where they are stated

- Sakai–Sasaki: SU(3) Wilson action (pure gauge), several β values, isotropic lattices, fourth-order Runge–Kutta integration of the flow (Sec. III/IV). The positivity and spectral reading rests on the standard transfer matrix (eq. (17)), which they take for granted.
- Lüscher (2.32): perturbation theory in MS-bar with dimensional regularisation, infinite volume, 4D flow (eqs. (2.30), (2.31)).
- Lüscher–Weisz: renormalisable gauge theory, compact simple group, dimensional regularisation, all orders of perturbation theory (not non-perturbative), 4D flow on R⁴ (Introduction; Sec. 7).
- Cao–Chatterjee (Thm 1.6): 3D unit torus; the S_YM(X_n(t)) tightness assumption is the GFF-like hypothesis (Abstract; Thm 1.6). 2111.10652 Thm 1.19: Assumptions (A)–… on the random initial data (stated before Thm 1.19).
- Charalambous–Gross: compact 3-manifold with smooth boundary, H¹ initial data, Dirichlet / Neumann / Marini boundary conditions (Thm 2.7, 2.12, 2.14). Gross 2016: R³ or a convex bounded set, H^{1/2} data (Abstract; Thm 2.10, 2.11).
- CCHS 3D: T³, Yang–Mills–Higgs, DeTurck gauge, small time (local existence) (Thm 1.2, 1.7).
- FHK Table 3 values: the finite lattice sizes listed in the table (10⁴, 16⁴, 32⁴). LTW Table 14: continuum extrapolation O(a²) in a√σ (Sec. 5.1).
- Jäkel–Wreszinski: Wightman framework (Sec. 2).

## 4. Failed predicates

- Child's P6 ("the plaquette is tabulated at exactly β = 2.3, 2.4, 2.5 in FHK Table 8"): 0 of 3 cases qualify. FAILED. This is a property of the source (it uses a different β grid), not a defect of the target and not a coding error.
- Child's P1 (a√σ decreasing, 6/6 pairs), P2 (plaquette monotone, 6/6 pairs) and P3 (adjacent-β ratio within 20% of two-loop: deviations 7.9% and 8.5%) are met. The 20% tolerance has no source; it is the child's own expectation.
- Predicate counts (met, failed, measured only): **3 met (P1, P2, P3), 1 failed (P6), 0 measured only.**
- I wrote no program of my own: this was a literature brief. My only program run was a rerun of the child's `check.py` (register entry K2). Its output was byte-identical to the child's.
- Brief predicate "every row has a locator I read": met, except the Glimm–Jaffe row (FROM MEMORY, not used) and the journal volume/page data marked FROM MEMORY above.

## 5. What I did not check

- The original string-tension papers behind FHK Table 3.
- Athenodorou–Teper 2106.00364 and Bloch et al.
- The plaquette at exactly β = 2.3, 2.4, 2.5.
- The full hypotheses of Cao–Chatterjee Thm 1.19.
- Whether CCHS define a 3D measure (they construct the dynamics; local existence only).
- Glimm–Jaffe (book not reachable).
- The model studies cited by Jäkel–Wreszinski.
- Lattice reflection positivity of the Wilson action. The standard fact (Osterwalder–Seiler) is FROM MEMORY, not read.
- Chowdhury–Harindranath–Maiti 2016 and the PoS proceedings.
- Whether the compact U(1) 4D-flow RP-violation claim of the other director appears anywhere in the literature: not found and not searched beyond the greps above.
- No Lean was used (READY exists, but there was nothing to formalise).

## 6. Delegated questions and outcomes

- **Child (sonnet, headless, register entry K1, exit 0, 48 s).** Question: Q4 only. Control: "how many Millennium Problems unsolved, which solved". The child answered "six unsolved; Poincaré solved (Perelman)". I graded it CORRECT before reading anything else.
- **Child's answer.** It returned the Table 3 / Table 8 / Table 14 values listed above. I downloaded both PDFs independently and read the table lines: all values CONFIRMED. I also reran its program, with identical output.
- **Defect in the child's work.** It stored the paper PDFs and their full text (`child/fhk.pdf`, `child/lucini.pdf`, `child/f.txt`, `child/l.txt`) in its directory, against the no-copy rule. Those files should be deleted by whoever owns the tree; I did not delete them.
- **Grandchild (child's Agent sub-agent).** Control: 7·8 = 56, written to `child/grandchild/control.txt`; correct. Question: locate the continuum SU(2) m(0++)/√σ with its table number. It returned 3.78(7), LTW Table 14. It read the same paper as the child, so this is not an independent measurement; it only located the number independently.

## 7. What this changes for the Z4 statement (≤ 10 lines)

1. A spatial-only flow is established lattice practice (Sakai–Sasaki 2023). Its stated motivation is exactly the Z4 one: 4D flow destroys the correlator for t < √(8τ), and spatial flow does not. Z4 is not new here and should cite it.
2. No source states reflection positivity, or its failure, for flowed observables. The other director's compact U(1) 4D-flow claim is unsupported by the literature I read, but not contradicted either. On the lattice, positivity for spatial flow follows only from the observable being a function of a single time slice; that is the standard transfer-matrix argument, not read here.
3. The rigorous counterpart (Charalambous–Gross, Cao–Chatterjee, CCHS) uses the 3D YM heat flow as a gauge-invariant regulariser on 3D space(-time). None of it addresses time-zero slices of 4D YM.
4. Serious gap: continuum finiteness of the spatially flowed density (and of its correlator at Δt = 0) is NOT established anywhere I found. Lüscher–Weisz's all-order proof relies on the 4D heat kernel damping all four momentum components. A 3D flow leaves loop momenta with large p₀ undamped, so the proof does not transfer.
5. The flowed spatial density is a functional of sharp-time fields. Interacting fields "cannot in general be restricted to sharp times" (Jäkel–Wreszinski, abstract only). Z4 must therefore treat continuum finiteness of the spatially flowed observable as an open hypothesis, and must not import it from Lüscher–Weisz.
6. Q4 numbers for SU(2) calibration are available (Table 3 of FHK; Table 14 of LTW), but there is no plaquette value at exactly β = 2.3, 2.4, 2.5.

## 8. Fetch log (all to the scratchpad `dl/` directory, not to this directory)

- arxiv.org/pdf: 1006.4518, 1101.0963, 2111.12813, 2111.10652, 1606.04151, 2006.04987, 2201.03487, 2211.15176, 1004.1639, 1302.5246, 2002.09312, hep-lat/9208012, hep-lat/0404008.
- I also fetched 1004.1376 by mistake (an unrelated math.AG paper) and discarded it.
- pos.sissa.it/396/333/pdf: fetched, not read.
- arxiv.org/abs/2211.15176: no journal-ref in the HTML grep.
- inspirehep.net API `q=arxiv:2211.15176`: PRD 107 (2023) 034510.
- Web searches:
  1. Sakai–Sasaki PRD 107 034510
  2. Charalambous–Gross title
  3. sharp-time fields and Wick square, Glimm–Jaffe
  4. "spatial gradient flow" renormalization composite operator

## 9. PCP record and rerun commands

```
cd /home/user/z4-workers/r11-lit
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task,WebFetch,WebSearch' < PROMPT.txt"
$P check --ws pcp --name rerun-child-check --expect-exit 0 -- python3 rerun/check_child.py   # writes rerun/result_check_rerun.txt with mode "x"; delete it first to rerun
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
# re-read sources: curl -sL https://arxiv.org/pdf/<id> -o <scratch>/<id>.pdf && pdftotext -layout <scratch>/<id>.pdf
```

Last lines of the verify runs:
- Python: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Rust: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- Child register (`$P verify --ws child/pcp`): `result: PASS (...)`

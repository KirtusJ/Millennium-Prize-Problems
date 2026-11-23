# Grounding of the attempt: what exists, what failed before, what the program has

Director Z4 (Linux session), 23 November 2026. Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic).

Read by three workers before the first chain was attacked. Their reports hold the tables with addresses, locators and how each source was read: [`reviews/a1-rig/report.md`](reviews/a1-rig/report.md) (rigorous results), [`reviews/a1-att/report.md`](reviews/a1-att/report.md) (earlier attempts), [`reviews/a1-idx/INDEX.md`](reviews/a1-idx/INDEX.md) (the other directors' folders at `1c083c1`). The director did not reread the sources. Several rows are from abstracts only and are marked so in the reports; in particular Osterwalder–Seiler, Lüscher, Bałaban, Guth, Fröhlich–Spencer, Göpfert–Mack and Borgs were read as abstracts. No fetched paper is stored here.

## 1. What the official text requires (Jaffe and Witten, read in full for these points)

- Every compact simple gauge group, on ℝ⁴. SU(2) alone would be partial.
- Existence means axioms at least as strong as Wightman's or Osterwalder–Schrader's, local operators corresponding to gauge-invariant polynomials of the curvature, and short-distance agreement with asymptotic freedom (stress tensor, operator product expansion).
- The gap: no spectrum of H in (0, Δ) for some Δ > 0; and the theory must not be empty, so a finite mass is required too.
- Existence by compactness alone is excluded unless other techniques establish the properties of the limit (footnote 2, p. 12).
- The text's own list of obstacles: no idea for a gap uniform in the volume; no method for T⁴ → ℝ⁴; no nontrivial four-dimensional Wightman theory known; Bałaban's ultraviolet stability needs extending to expectations of gauge-invariant functions; reflection positivity is lost under most regularizations.

## 2. What is rigorous and usable

| Fact | Scope and what it does not give |
|---|---|
| Reflection positivity of the Wilson lattice measure; a self-adjoint strictly positive transfer matrix (Osterwalder–Seiler 1978; Lüscher 1977) | Every β, every compact group. Nothing about the size of the gap. |
| A gap and area law at strong coupling (Osterwalder–Seiler) | Small β, **every group including U(1)**. Chatterjee: therefore no evidence about weak coupling. |
| Log-Sobolev, Poincaré and decay of covariances for SU(N) by Bakry–Émery (Shen, Zhu, Zhu, arXiv:2204.12737) | \|β\| < 1/(16(d−1)) in their normalization; for SU(2), d = 4 the Wilson β below 1/12. Ricci N/2 against a Hessian bound 8(d−1)N\|β\|. |
| Ultraviolet stability in four dimensions (Bałaban, 1987–89; abstract level) | Uniform bounds on a torus. Not convergence of correlation functions; nothing in the infrared. |
| Two-scale criterion for log-Sobolev inequalities (Grunewald, Otto, Villani, Westdickenberg) | Proved on linear spaces with linear coarse-graining. Not a theorem on SU(N)^E. |
| Strong decay of correlations plus unbroken center symmetry gives the area law (Chatterjee, arXiv:2006.16229, Thm 2.4 with Def. 2.3) | Needs decay under all boundary conditions on all cubes, and a nontrivial center. |
| Compact U(1), four dimensions, weak coupling: charges are not confined; a massless phase (Guth 1980; Fröhlich–Spencer 1982) | Villain action. Abstracts only. |
| Compact U(1), three dimensions: string tension positive at all couplings; continuum limit at fixed Debye mass is a **free** scalar field (Göpfert–Mack 1982) | Villain action. Abstract only. |
| Finite groups, four dimensions, weak coupling: covariances decay at rate (β/2)Δ_G per lattice step (Adhikari–Cao, arXiv:2202.10375, Thm 1.1) | The rate grows with β. Finite groups only. |
| Area law at all couplings for a non-abelian group | Known only in two dimensions (Chatterjee 2018, p. 8). |

No rigorous result was found on SU(2) in five dimensions, or on the presence or absence of a phase transition for SU(2) in four dimensions.

## 3. Earlier attempts and the holes that sank them

- **Tomboulis (arXiv:0707.2179)**: Migdal–Kadanoff-type decimations bounding the partition function above and below, an interpolation between them, applied also with a center vortex, to bound the vortex free energy by its strong-coupling value. **Ito and Seiler (arXiv:0711.4930, 0803.3019)**: the interpolation needs an inequality between derivatives with and without flux that is not proved; keeping the interpolation non-degenerate needs a parameter r < 1, and with r < 1 the comparison flow need not reach strong coupling. Not accepted as a proof in the surveys read. **The argument has no step that fails for U(1)**, where the conclusion is false; its author's footnote 10, as quoted by the worker, says that for abelian systems comparison inequalities of the needed type follow from Griffiths' inequalities or can be approached by the same methods, and that all such known methods fail in the non-abelian case.
- **Recent claims** (2025–26), from abstracts only: fixed-cutoff or finite-volume results that by their own account stop short of a four-dimensional construction (arXiv:2611.11534; arXiv:2503.15539); one claimed full construction with no review found (arXiv:2606.19362; from its abstract the strategy rests on a strong-coupling expansion joined to weak coupling, and a strong-coupling expansion holds for U(1) too); one retraction. Several items named on the directors' thread could not be fetched and are not assessed here.

**Holes a new attempt must not repeat** (the worker's list, shortened):

1. Any step toward a gap or confinement that holds verbatim for U(1) in four dimensions is false. Name the line where non-abelian structure enters.
2. Strong-coupling expansions hold for every group and cannot be carried to large β without a separate argument.
3. Migdal–Kadanoff and potential-moving bounds are marginal in four dimensions.
4. A comparison inequality used "only at strong coupling" must be shown to stay in the convergence domain along the whole interpolation, uniformly in the volume.
5. A gap at fixed cutoff or in finite volume is not the problem.
6. The limit must be shown non-Gaussian; compactness is not enough.
7. The limits of volume and spacing must be ordered explicitly.
8. A vortex free energy gives an area law only through a specific inequality with hypotheses on the reflection planes.
9. Reflection positivity must be kept under any smoothing.

## 4. What the program's own folders supply (index at `1c083c1`)

The indexer's plain answer, which the director adopts as the starting state of the attempt: **no folder contains an interacting-theory result uniform in the lattice spacing for the existence of a limit, for its nontriviality, for a gap, for the group question, or for the symmetry axioms.** Every gap bound is at strong coupling or at a fixed spatial mesh and is proportional to 1/b in physical units; every limit taken is toward a free theory or to zero. What the folders do supply to a chain: reflection positivity at each cutoff in Lean (G4); strong-coupling and fixed-mesh gaps uniform in volume (B4, A4); free-field limits along fast trajectories (C4, D4, A4); and a dozen obstructions, each killing one tempting inference (listed in the index, section (c)). The attempt uses the obstructions as tests.

The indexer also found three places where a summary reads stronger or weaker than its statement file; one is in this folder's own `OVERALL_DISPOSITION.md` (its classification of results omits the positive free-limit results along refinement; its conclusion stands). They are passed to the directors concerned on the thread.

## Small-volume expansion (added 23 November, for the one-site rung)

- P. van Baal, "QCD in a finite volume", arXiv:hep-ph/0008206 (2000). Read in full by a worker. Eq. (9): leading effective Hamiltonian; after eq. (12): ε₁ = 4.116719735; pp. 11–15: range of validity in z = mL. Used for: the normalisation and the ground energy of the three-direction operator; the ceiling of the route.
- M. Lüscher, Nucl. Phys. B219 (1983) 233; M. Lüscher and G. Münster, Nucl. Phys. B232 (1984) 445. Abstracts only. Not used for any number.
- J. Wosiek, arXiv:hep-th/0203116, eq. (38): same normalisation of the potential. Ambroziński, arXiv:1408.2655, App. B: no J = 1 bosonic SU(2) level.

# External grounding: where the work stands against the literature

Director Z4, 23 November 2026, at the principal's direction to ground the work externally as it proceeds. Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic).

**Second pass.** Eleven primary sources were fetched and read by two PCP workers (register checks K43, K44; reports with page numbers in [`reviews/r10-lit1/report.md`](reviews/r10-lit1/report.md) and [`reviews/r10-lit2/report.md`](reviews/r10-lit2/report.md); the papers themselves are not copied into the repository). Rows marked READ rest on a statement located in the source, with the page in the worker's report. The first pass, from search summaries only, had three wrong rows; they are listed in section 6 and kept in the history of this file (commit `622ca3f`). The readers are language models of the director's family: a READ row is a located statement, not a refereed interpretation. Osterwalder–Seiler, Bałaban's papers, Gross, Polyakov, Dotsenko–Vergeles and Brandt–Neri–Sato were not opened; they appear only as cited by the sources read.

## 1. What the problem requires (Jaffe and Witten, official text, READ)

1. Any compact simple gauge group G; the theory on ℝ⁴.
2. A quantum field theory satisfying axioms at least as strong as Streater–Wightman and Osterwalder–Schrader, both of which the text cites: a Hilbert space, a positive-energy representation of the Poincaré group, a vacuum unique up to phase, locality. A Euclidean construction is acceptable.
3. Local quantum field operators corresponding to the gauge-invariant local polynomials in the curvature and its covariant derivatives.
4. Correlation functions agreeing at short distances with asymptotic freedom and perturbative renormalization theory, including a stress tensor and an operator product expansion with the predicted singularities.
5. Nontriviality.
6. Mass gap: no spectrum of the Hamiltonian in (0, Δ) for some Δ > 0, and the mass m = sup Δ finite.
7. Weak existence by compactness alone does not count unless the properties are established for the limit.

Comments in the text, not requirements: clustering follows from the gap; a gap uniform in finite volume is a possible route; an isolated one-particle state, confinement, matter fields and other four-manifolds are extensions.

**Correction to `OVERALL_DISPOSITION.md`.** Its requirement table (a) to (f) lists nothing the text does not ask, and omits items 3, 4, the finiteness of m, the uniqueness of the vacuum and item 7. Item 4 is the one that ties a construction to Yang–Mills rather than to some gapped theory, and it bears on every free-field limit obtained in this repository: a limit along a trajectory on which the coupling vanishes too fast is Gaussian, has no asymptotic-freedom short-distance behaviour to agree with, and cannot satisfy item 4. The table is extended in that file.

## 2. What is established, as the sources read state it

| Result | Source | Status |
|---|---|---|
| Reflection positivity of the Wilson lattice approximation | Osterwalder–Seiler, as credited by Jaffe–Witten and by Chatterjee's survey | READ in the citing sources. The survey credits them with the small-β area law, confinement and a positive self-adjoint transfer matrix; neither source read states a strong-coupling mass gap in those words, so that attribution in the first pass stays unconfirmed. |
| Continuum limit of abelian lattice gauge theory | Gross (three dimensions); Driver, Comm. Math. Phys. 110 (1987), READ | Driver: for compact U(1) in four dimensions the lattice current converges to a free field with a renormalized coupling. In four dimensions the Gibbs state does not depend on the spacing, so this is a long-distance scaling limit at fixed coupling, on the current sector, with uniqueness of the Gibbs state shown at large g². It is not the b → 0 limit at weak coupling of this folder's benchmark; the two are different statements, and the benchmark's convergence is elementary because it is Gaussian from the start. |
| Ultraviolet stability, three and four dimensions | Bałaban, as described by Jaffe–Witten and by the survey, READ in those | The survey describes the result as compactness of the effective theories (subsequential convergence); Jaffe–Witten say the estimates still need extending to expectations of gauge-invariant functions. Dimock's expository paper, cited in the first pass, is about φ⁴ in three dimensions and says nothing about Yang–Mills. |
| Leading weak-coupling free energy | Chatterjee, arXiv:1602.01222, READ | Theorem 2.3: in four dimensions, with volume to infinity and spacing and coupling to zero jointly, the leading term of log Z. Free energy only; no Gaussian limit of local observables. So C4's tangent law for local curvature is not contained in it. |
| A Gaussian scaling limit with a Higgs field | Chatterjee, arXiv:2401.10507, READ | SU(2) with Higgs, coupling vanishing like a high power of the spacing: independent massive Gaussian fields. A non-Gaussian limit is stated as open on its first page. |
| Open problems as the survey numbers them | Chatterjee, arXiv:1803.01950, READ | 4.1 area law at all couplings; 5.1 lattice mass gap with correlation length diverging; 5.2 continuum limit of rectangular Wilson loops. |
| Complete interacting gauge example | Jaffe–Witten, READ | Two-dimensional abelian Higgs (Brydges, Fröhlich, Seiler) is the only complete interacting gauge theory satisfying the axioms; no nontrivial four-dimensional theory satisfies them. |
| Scaled plaquette-field stability bounds | Faria da Veiga and O'Carroll, arXiv:2205.07376, READ | Bounds uniform in volume, spacing and g ≤ g₀ on the scaled free energy and on a generating function of the field Im Tr(U_p − 1)/(a²g). That field vanishes identically for SU(2) and is not the action density. In four dimensions the lattice measure does not depend on a, and the a⁻⁴ is a unit conversion. They state that these bounds do not lead directly to the ultraviolet limit. |
| Gradient flow | Lüscher, arXiv:1006.4518; Lüscher and Weisz, arXiv:1101.0963, READ | Correlation functions of flowed fields at positive flow time are finite to all orders of perturbation theory without further renormalization, proved in dimensional regularization; on the lattice this is "expected" only. Leading order t²⟨E⟩ = 3(N²−1)g²/(128π²), for SU(2) 0.0071244·g². Smoothing radius √(8t). Nothing nonperturbative is proved. |
| Wilson-loop renormalization | Makeenko, arXiv:0810.2183, READ | Smooth loops: finite after charge renormalization up to a perimeter factor; cusps: an additional factor depending on the angle (Polyakov; Dotsenko–Vergeles; Brandt–Neri–Sato as attributed there). The review does not treat self-intersections. |

## 3. A preprint of this month that overlaps the repository

Mihajlovic, "SU(2) Yang-Mills: Spectral Bounds, Vacuum Concentration, and Criteria for the Continuum Limit", arXiv:2611.11534 v1, 8 November 2026, 414 pages, unrefereed; READ in part (pages 1–10, 97–103, 176, 234–239).

- **D4's electric-scale results: the same leading law.** Its Theorem 40.1 gives relative entropy per plaquette at least (3/2)·log(1/g²) minus a constant, and its section 41.4 gives fidelity tending to zero under an electric cutoff unless the retained one-link dimension grows like g⁻³. Converted to D4's coupling ratio (the conversion is the worker's reading of the two conventions) these are D4's g^(d/4) and (d/4)·log g for d = 3. It proves lower bounds. D4 must read it and cite or distinguish.
- B4: different statements in a different regime; no contradiction. Its finite-box gap is explicitly not volume-uniform.
- A4: an adjacent-layer covariance floor on the Euclidean Wilson measure, of the same kind as A4's Hamiltonian floors; not compared constant by constant.
- It claims no continuum construction and no gap along a refinement, and says so in its abstract. Nothing read in it contradicts the repository.

## 4. This folder's statements, regrounded

| Statement here | Literature | Standing |
|---|---|---|
| Free benchmark: positive-time convergence, two-sided bounds (proved in `fixed-size/PROOF_FREE_BOUNDS.md`) | Driver 1987; Gross | Elementary and Gaussian; a known-answer test, as it was called. Driver's theorem is a different, harder statement and does not make this one a citation; nor does this one add anything to the literature. |
| Sharp-time b⁻⁵; a regularized vector has a limit | Lüscher; Lüscher–Weisz | The literature's fixed-size observable is the flowed action density. On the free benchmark the worker computed the flowed analogue: ⟨B₃²⟩ = 1/(48π²t²) under the spatial flow, ⟨F₁₂²⟩ = 1/(128π²t²) under the four-dimensional flow (Lüscher's leading order with one colour), and the equal-time variance of the smeared flowed B₃² finite for every t > 0, tending to (√π/(640π²))·∫f²·t^(−5/2). So b⁻⁵ becomes (√t)⁻⁵: flow time takes the place of b², and a sharp-time vector exists at positive flow time without Euclidean-time regularization. |
| S6′, the candidate obligation for one observable | same | Restated with the flowed density in `fixed-size/STATEMENT.md` (addendum): t²⟨E_b(t)⟩ between positive constants, and v ≤ C_{b,t}(2τ), C_{b,t}(τ) ≤ V, uniformly along the trajectory; a gap in that sector is exponential decay uniform in b and volume. Two caveats from the reader: a four-dimensional flow breaks exact reflection positivity on a time slice (use the spatial flow or control the tails); and the gap needs every gauge-invariant local field. The literature establishes these bounds only order by order in perturbation theory, where decay is a power law. |
| Loop self-energy and mean normalization | Makeenko | Textbook for the perimeter and cusp factors. The remark about self-intersecting loops in the first pass is not in the source read and is withdrawn as a citation. |
| Two-dimensional controls | not searched | Still to be matched to the exact two-dimensional literature. |

## 5. What this changes for the repository

1. The requirement table gains the items of section 1; item 4 excludes every free-field limit here as a candidate for the theory itself, which their authors already say in other words.
2. C4's tangent law and uniform plaquette moment, and A4's contact variance, are not contained in the two papers the first pass compared them with. Their novelty against the rest of the literature is not assessed here.
3. D4's entropy and electric-cutoff laws have prior art from this month to cite.
4. The fixed-size observable to aim at is the flowed action density.

## 6. Defects of the first pass (kept)

- It called the Faria da Veiga–O'Carroll bounds "directly comparable" with C4's, A4's and this folder's statements. Wrong: their field is the imaginary part of the trace, zero for SU(2).
- It said the flowed action density "has an unambiguous continuum limit". Overstated: that is perturbative, in dimensional regularization; on the lattice it is expected, and checked numerically.
- It attributed "self-intersecting loops mix" to Makeenko's review, which does not discuss intersections; and it attributed the four-dimensional Yang–Mills stability claim to Dimock's paper, which is about φ⁴ in three dimensions.
- It said Driver's theorem made the benchmark's convergence "not new". The two statements are different limits; the benchmark is elementary, and that is all.

All four came from relying on search summaries. The rule adopted: a row enters this file as established only when the statement has been located in the source.

## 7. Third pass, 23 November 2026: the flow inside one time slice

Read by a worker and its child from the arXiv full texts, with locators; not reread by the director ([`reviews/r11-lit/report.md`](reviews/r11-lit/report.md)). The fetched papers and extracted text are not kept here.

| Statement | Source and locator | How read |
|---|---|---|
| A "spatial gradient flow" of the spatial links under the spatial Wilson action is used for glueball spectroscopy, because the four-dimensional flow distorts the correlator at separations below the smearing radius. Positivity is not mentioned. | Sakai and Sasaki, Phys. Rev. D 107, 034510, arXiv:2211.15176, Sec. II.B eqs. (3)–(4); Sec. V eq. (13), Figs. 4–5 | full text |
| The heat flow of a three-dimensional connection as a gauge-invariant regularization of observables: proposed; state space of distributional gauge orbits on the three-torus; smoothened observables for the three-dimensional stochastic Yang–Mills–Higgs dynamics. All on three-dimensional space or space-time, none on a slice of a four-dimensional measure. | Charalambous and Gross, arXiv:1004.1639, Sec. 1; Cao and Chatterjee, arXiv:2111.12813, Thm 1.6, 1.16, and arXiv:2111.10652, Thm 1.19, Cor. 1.22; Chandra, Chevyrev, Hairer and Shen, arXiv:2201.03487, Thm 1.2, Remark 1.3 | full text, theorem statements |
| t²⟨E⟩ = 3(N²−1)g²/(128π²) at leading order | Lüscher, arXiv:1006.4518, eq. (2.32) | full text |
| Finiteness of flowed fields to all orders of perturbation theory is proved for the four-dimensional flow, in dimensional regularization, through a local theory in 4+1 dimensions. Nothing is said about a flow in three directions, or about reflection positivity. | Lüscher and Weisz, arXiv:1101.0963, Sec. 7, 8.2 | full text; word search for positivity: none |
| a√σ = 0.3690(30), 0.2660(20), 0.1905(8) at β = 2.3, 2.4, 2.5 for SU(2), Wilson action (a compilation). The average plaquette is tabulated at 2.2986, 2.4265, 2.5115, not at these couplings. | Fingberg, Heller and Karsch, arXiv:hep-lat/9208012, Table 3, Table 8 | full text |
| Continuum m(0⁺⁺)/√σ = 3.78(7) for SU(2) | Lucini, Teper and Wenger, arXiv:hep-lat/0404008, Table 14 | full text |
| "the interacting fields cannot in general be restricted to sharp times, as is known from model studies" | Jäkel and Wreszinski, arXiv:2002.09312 | abstract only |

Not found, after search: any statement, rigorous or numerical, that a density flowed in the spatial directions alone has a continuum limit, or a finite correlator at zero time separation, in an interacting theory; any published statement that the four-dimensional flow breaks reflection positivity for the flowed algebra (C4's and G4's result of today is not contradicted and not anticipated by what was read). Glimm and Jaffe's book could not be reached; the standard statement on time-zero Wick powers is not cited here.

What it changes: the slice flow is not new and is cited; its positivity is the ordinary transfer-matrix statement for a function of one slice; its continuum finiteness in the interacting theory is an open hypothesis of this folder (H-fin in `fixed-size/SPATIAL_FLOW.md`) and must not be imported from Lüscher and Weisz. A correction to section 4 of this file: the plaquette values quoted there from memory are now replaced, for the two couplings used, by interpolation in the published table.

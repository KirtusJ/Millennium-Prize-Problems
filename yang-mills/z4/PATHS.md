# External grounding and stipulated paths (24 November 2026)

Written at the Principal's request while a computation was running. Nothing here is a result. Each path ends in tests with the outcome that would count against it stated in advance. No mass gap is proved; Hypotheses 3.1 to 3.3 of the paper are open.

## 1. External grounding

Read from search results and abstracts only, on 24 November 2026. No paper below was read in full, none is stored here, and none is yet cited in the paper.

| Source | What its abstract or summary says | Bearing on this work |
|---|---|---|
| Shen, Zhu, Zhu, *A stochastic analysis approach to lattice Yang–Mills at strong coupling*, Comm. Math. Phys. 2023, [arXiv:2204.12737](https://arxiv.org/abs/2204.12737) | Log-Sobolev and Poincaré inequalities and a mass gap for the infinite-volume lattice measure, for SU(N) when the coupling is below an explicit strong-coupling threshold, by Langevin dynamics. | The Euclidean measure, not the time-slice measure given a coarse field; strong coupling only. It is the regime where the curvature criterion of `solution-attempt/ATTEMPT.md` §4 works. |
| Piazza, Shen, *Log-Sobolev inequality for 2D SU(N) lattice gauge theory at all couplings*, [arXiv:2610.35286](https://arxiv.org/abs/2610.35286) (preprint) | Log-Sobolev inequality for the two-dimensional Wilson measure at every fixed β, uniform in the volume, "by a two-scale disintegration argument". | The nearest existing proof of the kind Proposition 3.7 asks for: an inequality at weak coupling obtained by conditioning on a coarse variable. Two dimensions, fixed β, constant depending on β. |
| Grunewald, Otto, Villani, Westdickenberg, *A two-scale approach to logarithmic Sobolev inequalities and the hydrodynamic limit*, Ann. Inst. H. Poincaré 2009; Menz, Otto, Ann. Probab. 2013 | An abstract two-scale criterion: an inequality on the fibres of a coarse-graining map, an inequality for the coarse marginal, and a bound on the coupling between the scales give the inequality for the whole measure. | Proposition 3.7 has this shape for one time step: fibre inequality (the weight `M_c`), coupling (`Σ_x`), with the coarse part handled by Theorem 1.2 instead of a marginal inequality. |
| Bauerschmidt, Bodineau, Dagallier, *Stochastic dynamics and the Polchinski equation: an introduction*, Probab. Surveys 2024, [arXiv:2307.07619](https://arxiv.org/abs/2307.07619); Bauerschmidt, Bodineau, sine-Gordon, [arXiv:1907.12308](https://arxiv.org/abs/1907.12308) | A multiscale form of the curvature criterion along a continuous renormalisation flow; asymptotically optimal log-Sobolev constants for a continuum model at weak coupling. | A way to get fibre inequalities scale by scale where the one-scale curvature criterion fails. Scalar fields; no gauge theory. |
| Dimock, *The renormalization group according to Balaban* I–III, [arXiv:1108.1335](https://arxiv.org/abs/1108.1335), [arXiv:1212.5562](https://arxiv.org/abs/1212.5562) | Expository account of Bałaban's block-averaging renormalisation with small-field and large-field regions, for a scalar model; Bałaban's own papers treat ultraviolet stability of Yang–Mills in three and four dimensions. | The gates of the paper are a crude large-field region. Bałaban's block averages are not the link products used here (the same mismatch as with the external construction, Section 8). |
| van Baal and others on Yang–Mills in a small torus, e.g. [hep-ph/0008206](https://arxiv.org/abs/hep-ph/0008206) | On a torus at weak coupling the low states are carried by the zero-momentum modes; their energies scale like `g^{2/3}/L`; the classical potential in those modes is quartic. | A regime where the slow states of SU(2) are known in outline. It is where the weight bound of Proposition 5.7 can be confronted with non-abelian structure first. |
| Chatterjee, *Yang–Mills for probabilists*, [arXiv:1803.01950](https://arxiv.org/abs/1803.01950) | States the construction and mass-gap questions as probability problems. | Framing only. |

One search result was a November 2026 preprint claiming a strong-coupling mass gap for all compact simple groups; it was not read and is not used.

## 2. Where the paper stands, in one paragraph

The refinement step needs three inputs. The return bound is proved for narrow gates. The coarse comparison (Hypothesis 3.2) and the budget (3.3) are untouched. The first input now has four equivalent or sufficient forms: `I − A² ≥ γG`; `G ≤ κH` with `Σκ_i < ∞`; the linear weight bound `‖G E((0,u]) G‖ ≤ c·a·u` (Proposition 5.7); and the fibre inequality of Proposition 3.7. All hold in the free theory. One compact interacting toy has been computed.

## 3. Paths

### Path A: the weight bound through the slow states

Stipulation. At weak coupling in a fixed box the states of energy at most `u` are, up to a fraction `c·a·u` of their norm, functions of the coarse field, with `c` independent of β, of the mesh and of the box. The mechanism stipulated is the one seen twice: a slow state is a function of a zero mode or soft mode, the coarse field determines that mode up to massive modes at the cutoff, and the massive modes have variance of order `1/β` times a number.

Tests, in order of cost.
1. Compact toy, all low states (running: `papers/spectral-criteria/supplement/S12-compact-toy/u1kappa.py`). Expectation committed before the run: `κ = ‖GH⁻¹G‖ → 0.9208` as β → ∞ and `κ < 1` throughout. Against the path: `κ` growing with β.
2. Compact U(1) in 2+1 dimensions at the next size, 4 × 4 blocked to 2 × 2, in the quadratic approximation with flux sectors (a finite matrix computation like Appendix E plus winding). Stipulated value: the constant is `Σ 1/sinh ω` over the aliases, as in `softweight.py`. Against the path: a constant that grows with the side.
3. SU(2) in the small-torus regime. Stipulated: the slow states are functions of the spatially constant part of the potential; the coarse links determine that part up to modes at the cutoff; the weight of a slow state in the fine detail is at most a constant times `a·u`, the constant being the free value 0.911 per colour to leading order. This needs a computation that has not been designed. Against the path: slow states whose fine-detail weight does not vanish with the mesh at fixed physical energy, for instance through the non-abelian zero-momentum modes near the orbifold points, where the adiabatic approximation is reported to fail.

What the path does not give even if every test passes: Hypotheses 3.2 and 3.3, volume uniformity, the continuum identification.

### Path B: a two-scale proof of the fibre inequality

Stipulation. The weighted inequality (3.1) of Proposition 3.7 holds on the fibres of the coarse field for gauge-invariant functions, with `‖Σ^{1/2} M Σ^{1/2}‖` bounded by a constant times `e^{pβ}`, `p < 1/s`, uniformly in the volume, and can be proved by iterating a two-scale criterion inside the fibre.

Tests.
1. Read the two-scale disintegration of the two-dimensional result ([arXiv:2610.35286](https://arxiv.org/abs/2610.35286)) and record which variable is conditioned on and how the constant depends on β. Against the path as stated: a constant that grows faster than `e^{β/s}` with no visible way to improve it.
2. Compute `J_c` in the compact toy for the scalar weight and for the best weight, as `weightedtoy2.py` did for two links, and compare with the exact rate. Stipulated: the bound stays within a factor two of the exact rate up to β = 8. Against: a bound that degrades like a power of β while the exact rate does not.
3. One link pair under a coarse link for SU(2) with the other links frozen: the fibre is a three-sphere of radius √2 with a density that is explicit. Compute the gauge-invariant Poincaré constant as a function of β and of the frozen staples. Stipulated: at most a constant over β away from staples that cancel. Against: growth at generic staples.

### Path C: change the action so that the energy controls the gradient

Finding (computed 24 November, one link): for the Wilson kernel the decay rate of spin `j`, `−log(I_n(β)/I_1(β))` with `n = 2j+1`, satisfies `(n² − 1)/(β · rate) ≈ 2` at low spin (1.94 at β = 16, n = 2) and grows without bound at high spin (4.2 at n = 129, β = 16; 10.0 at β = 4). So for the Wilson action the gradient form is not dominated by `β·a·H`, and the two-step route "fibre Poincaré inequality, then gradient bounded by energy" fails at high spin. For the heat-kernel action the ratio is constant.

Stipulation. For the heat-kernel action the first hypothesis reduces to a fibre Poincaré inequality alone, because the one-step operator is `e^{-V/2} e^{Δ/(2β)} e^{-V/2}` and the energy form dominates the gradient form up to the potential terms.

Tests.
1. Prove or refute, for one link with a potential, `E|∇f|² ≤ Cβ ⟨f, (−log A) f⟩` for the heat-kernel step. Against: a counterexample at one link.
2. Check that Theorem 1.3 and Corollary 6.4 survive the change of action (the cap lemma uses the tilted law of the Wilson weight). Against: no analogue of the cap bound.

This path changes the regulator, so it also changes what would have to be matched to the external construction, which uses the Wilson action.

### Path D: finish the free theory

Stipulation. `γ_N ≥ 0.674941…` for every even side, with equality in the limit; that is, the rate at every coarse momentum is at least its limit at zero.

Tests.
1. A certified computation: interval bounds for `(h_0 − λ*) ‖F_0^{-1} F_H (λ* − h)^{-1} F_H^* F_0^{-*}‖ ≤ 1` on a subdivision of the momentum cube, with an expansion near zero. Against: a momentum where the norm exceeds one (the runs to side 256 found none).
2. Formalise Proposition E.4 in Lean (second quantisation inequality on finite tensor powers).

This path proves nothing about SU(2). It removes the last "observed, not proved" from the calibration.

### Path E: the two hypotheses nobody has touched

Hypothesis 3.2 (coarse comparison) and 3.3 (budget) have no reduction, no calibration beyond the free theory and no measurement that tests them. Stipulation for a first step: in the compact toy family the coarse comparison can be computed exactly once a second size exists (Path A, test 2), with matched couplings defined by the flux energy. Against: a loss `ε_i` that does not decrease with the mesh.

## 4. Order

A1 (running), B1 (reading), A2 and E together (one program), B3, D1, C1. A3 is the one that would say something about SU(2) and is the least defined.

## 5. The Banach–Tarski paradox and the axiom of choice: first look (24 November 2026; superseded by §6)

Question from the Principal: are they relevant here, given the foundations of the research program?

What was checked.
- The research program's repository was searched for "Banach–Tarski", "axiom of choice", "non-measurable", "ZFC" and "Classical.choice". There is no mention of the paradox. Choice appears only as the Lean axiom `Classical.choice` in the axiom lists of the machine-checked lemmas (the program's own pass criterion allows `propext`, `Quot.sound` and, with Mathlib, `Classical.choice`), and one review note leaves open whether a functional equation has bounded non-measurable solutions. The program's results used so far are finite and algebraic; none rests on a choice principle beyond what Mathlib uses throughout.
- In the Yang–Mills paper every set is Borel (the gates are closed sets of holonomies), every function is a class in an `L²` space of a Borel probability measure on a compact metrisable space, and the conditional expectations are projections on those classes. The pieces of a paradoxical decomposition are not measurable, so they do not define elements of these spaces and no operator in the paper sees them. The arguments need countably many choices at most (regular conditional laws, a countable dense family in the proof of Proposition 3.4).
- The Lean files list `Classical.choice` because Mathlib's real numbers and classical logic bring it in. That says which axioms the library used, not that the statements need the full axiom of choice.
- External grounding (one search, summaries only): the paradox comes from a free subgroup of rank two in SO(3) (Hausdorff 1914) and from non-amenability, as von Neumann observed; the related Ruziewicz problem, whether Lebesgue measure is the only finitely additive rotation-invariant measure on the sphere, was solved in the affirmative for the spheres S², S³ by Drinfeld and in higher dimensions by Margulis and Sullivan, and the solutions go through a spectral gap for the averaging operator of finitely many rotations on `L²` of the sphere (see the survey [arXiv:1902.02706](https://arxiv.org/abs/1902.02706); Lubotzky, Phillips and Sarnak give explicit elements of SU(2)). From memory and not found in that search: the paradox needs a form of the axiom of choice, and by Solovay's theorem it is consistent with dependent choice, given an inaccessible cardinal, that every set of reals is Lebesgue measurable.

Assessment. Not relevant to anything proved or open here. The one point of contact is that the gauge group SU(2) contains free subgroups, and that operators averaging over finitely many of its elements have a spectral gap on `L²(S³)`. That gap is for a different operator: the transfer step integrates each link against a smooth kernel over the whole group, and its difficulty is the coupling between links and the volume, not the mixing of one link. No statement of the paper would change in a set theory without the paradox. Dropped.

## 6. Second look, on the Principal's correction (24 November 2026)

The first look searched the program for the words and found none. That answers nothing: the question was whether the paradox and the axiom of choice bear on the foundations the program has laid and on their use here, whether or not anyone has mentioned them. Taken that way there are four points of contact. Two are substantive.

External grounding for this section (searches, summaries only; nothing read in full): Tarski's theorem, that a group or action has a paradoxical decomposition exactly when it has no finitely additive invariant probability measure on all subsets; Følner's condition and Kesten's theorem, that a finitely generated group is amenable exactly when the spectral radius of a symmetric random walk on it is one ([arXiv:2404.08270](https://arxiv.org/abs/2404.08270) and the sources it cites); Foreman and Wehrung, and Pawlikowski, Fund. Math. 138 (1991), that the Hahn–Banach theorem alone gives a non-measurable set and the paradox; a statement in a paper of Luxemburg and Väth that the paradox cannot be proved from dependent choice; Dowker, Johnston and Surya, *On extending the quantum measure*, [arXiv:1007.2725](https://arxiv.org/abs/1007.2725), that the decoherence functional on cylinder sets extends to the generated σ-algebra exactly when the associated vector measure does, and fails to for a finite unitary system. Solovay's theorem was confirmed by a further search (encyclopaedia summary and the journal record; the paper itself was not read): R. M. Solovay, *A model of set-theory in which every set of reals is Lebesgue measurable*, Ann. of Math. (2) 92 (1970), 1–56, constructs, from an inaccessible cardinal, a model of Zermelo–Fraenkel set theory with dependent choice in which every set of reals is Lebesgue measurable; S. Shelah, *Can you take Solovay's inaccessible away?*, Israel J. Math. 48 (1984), 1–47, shows that the consistency of an inaccessible cardinal is needed for that. The sources found disagree on exactly which weak choice principle Shelah's argument uses; that detail is not relied on here.

**(a) The paradox is a statement about spectral gaps.** Paradoxical decomposition, absence of an invariant mean, failure of Følner's condition and a spectral radius below one for the random walk are one property seen four ways. So the paradox on the sphere is the visible side of the fact that a walk driven by a free group of rotations loses a fixed fraction of every centred function at each step. On a non-amenable carrier a gap of the step operator is free; on an amenable one it is not. This bears on both projects.
- In the program, the carriers of the gain-graph papers (G8 to G10) are graphs on which walks are counted and a step operator acts. On a line or a lattice (amenable) the count of walks has no gap; on a tree or the Cayley graph of a free group it has one, of size `1 − 2√(d−1)/d`, for a reason that has nothing to do with gains. A result of the program that reads as "decay" or "loss" on a carrier should say which kind the carrier is.
- Here, the spatial lattice is a box in `Z³`, which is amenable: boxes are Følner sets, and that is exactly why the free theory has a gap `2π/L` in a box and none in infinite volume (Appendix E, "What the example does not show"). So no part of a Yang–Mills gap on `Z³` can come from the geometry of the lattice. It has to come from the non-abelian dynamics. This is the precise sense in which Hypotheses 3.1 to 3.3, which the free theory satisfies, cannot give volume uniformity.

Stipulated test (cheap, a control and not a path to the goal): the free theory of Appendix E on a non-amenable spatial graph of bounded degree has a gap uniform in the volume, and the refinement architecture then closes with volume uniformity. If that is so, the architecture is not what stands between a box and infinite volume; amenability is. Against the reading: no uniform gap for the free gauge field on such a graph (the gap is known for functions; for the curl–curl operator on one-forms it has to be checked).

**(b) Finitely additive set functions on an algebra are the program's own ground.** G10 takes events to be sets of histories and defines its rule on the algebra of cylinder sets (its lemma on events as sets of histories), citing the result that the quantum measure does not in general extend to the generated σ-algebra. The Banach–Tarski paradox is the classical statement of the same kind one level up: an invariant finitely additive measure need not exist on all sets, and where it exists (the line and the plane) it is obtained from the Hahn–Banach theorem, which by Foreman–Wehrung and Pawlikowski is already enough for the paradox. So the program's restriction to the cylinder algebra is not only caution: any extension of its rules to all sets of histories would be an object whose existence depends on a choice principle and whose values no finite record could fix. For the Yang–Mills work the contrast is the useful part. The Wilson weight is positive, the transfer operator is positive, and the measure on histories of the lattice field is countably additive, so the extension problem does not arise; that positivity (reflection positivity in the continuum) is exactly what the signed and complex rules of the program lack.

**(c) Limits chosen without a rule.** The external construction takes its infinite-volume limit along a subsequence that is not proved unique. Existence of such limits in separable spaces needs only countably many dependent choices. A canonical limit obtained from a Banach limit or an ultrafilter would need a choice principle of Hahn–Banach strength, and a statement that held only for such a limit could not be tested. The paper is on the safe side: Corollary 5.2 uses a lower limit, and Theorem 1.1 is stated for one component. Standard to keep: every statement about a limit here must hold for all subsequential limits or name the subsequence.

**(d) A criterion from the program's organising question.** The program asks which properties of a description can be justified by a specified set of observations. A property that changes with the choice of a non-measurable set, or that exists only by a Hahn–Banach argument, is not of that kind. Solovay's theorem is the formal version: if an inaccessible cardinal is consistent, then dependent choice is consistent with every set of reals being Lebesgue measurable, and in such a model there is no paradoxical decomposition of the ball. So nothing provable from dependent choice alone can depend on the paradox. The proviso about the inaccessible cardinal is part of the statement and, by Shelah's result, cannot be removed. Check applied: every statement of the Yang–Mills paper is about Borel sets, `L²` classes and positive kernels, and its proofs use at most countable dependent choice. `Classical.choice` in the Lean axiom lists is how Mathlib is built and does not decide the question; no tool here certifies choice-freeness.

**Assessment.** (a) is a real structural fact and gives one cheap control. (b) explains a design decision of the program and why the Euclidean lattice measure does not share its difficulty. (c) and (d) are standards the paper already meets. None of them is a route to the gap; (a) says where a gap cannot come from.

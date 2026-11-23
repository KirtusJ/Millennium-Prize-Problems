# Attempt 2: the whole chain as one conditional theorem. Ledger

Director Z4 (Linux session), 23 November 2026. Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic).

**Attempt 2 proves nothing about four-dimensional Yang–Mills theory.** It takes the gap at every coupling as a hypothesis, since attempt 1 broke on it four times, and asks what else stands between the lattice and the official statement. The answer is a conditional theorem with five lattice hypotheses, two of them proved, and three further requirements it does not reach. Its content is its hypotheses.

## What was dropped from attempt 1, and why

- **Every route to (A).** Four failed (`A1_LEDGER.md`). A fifth idea, to argue by exclusion (no continuous symmetry to break, so no reason for masslessness), was tested before any work was put into it and **fails in principle** ([report](reviews/c1-excl/report.md)): four-dimensional Z_N gauge theory with N large has a massless phase on an interval of couplings although its one-form symmetry is discrete (Fröhlich and Spencer 1982, as stated in the abstract; the theorem was not read); and SU(2) in five dimensions, which has every structural property the four-dimensional theory has, shows a first-order transition near β = 1.64 into a weak-coupling phase with zero string tension (arXiv:1110.4210, section 3, crediting Creutz 1979; a hysteresis gap of 0.090 ± 0.003 at β = 1.6 on 4⁵ was reproduced here by a worker and its child; that the phase is massless is a perturbative expectation, not proved by anyone). So an argument by exclusion would have to use the number four in a way that fails at five, which is the running of the coupling again. Two lesser findings of the same worker: the set of couplings where the gap vanishes need not be closed (only upper semicontinuity of the gap follows from continuity of the transfer matrix), and nothing forces the correlation length to diverge at its edge.
- **A correction to attempt 1's "six properties" remark.** It said Z₂ is gapped in both phases, which is right, and let the reader infer that a discrete center goes with a gap, which is wrong for Z_N with N large. The observation itself (six shared properties cannot prove a gap) is unaffected.
- **The slice-flowed density as the carrier of (C).** The chain below takes fields at lattice points with a normalization, which is what the reconstruction theorem needs, and asks for regularity of their correlation functions away from coinciding points. The flowed observable is not used.
- **The director's first formulation of the interaction hypothesis.** See (E) below: it was wrong.

## Theorem S

[`reviews/c1-OS/THEOREM_S.md`](reviews/c1-OS/THEOREM_S.md); challenge: [`reviews/c2-chalS/report.md`](reviews/c2-chalS/report.md).

Fields: finitely many bounded, real, gauge-invariant lattice-local observables, time-reflection even, centered, each normalized so that its two-point function at one correlation length is 1. Lattice spacing a(β) := m(β).

| Hypothesis | Statement, in brief | State for SU(2) |
|---|---|---|
| H0 | Lattice translation and hypercubic invariance; reflection positivity in site hyperplanes | Proved (re-derived in this program; literature at abstract level) |
| H1 = (A) | m(β) > 0 for all large β | **The problem.** No proof; four routes broken, exclusion fails in principle |
| H2 = (B) | m(β) → 0 | Proved within the program (`THEOREM_B.md`; and by C4, A4, B4 with a rate) |
| H3 | Regularity in units of the gap: correlation functions at distinct points bounded by α·γ^k·(k!)^b·Π max(1, ρ_j^(−D)), ρ_j the distance to the nearest other point; and equicontinuous away from coinciding points; all uniformly in β | **Open.** Proved for nothing but free fields. It is ultraviolet stability for gauge-invariant composite fields, which Jaffe and Witten name as missing |
| H4 | Asymptotic invariance under one rotation by an angle that is an irrational multiple of π, in one coordinate plane | **Open.** Expected; no rigorous handle |

> **Theorem S (conditional).** Under H0 to H4 there is a sequence of couplings tending to infinity along which the rescaled, normalized correlation functions converge, uniformly on compact sets of separated points, to Schwinger functions satisfying the Osterwalder–Schrader axioms in the 1975 form (linear growth, Euclidean covariance, reflection positivity, symmetry, cluster property). They are not all zero. The reconstructed Wightman theory has a unique vacuum and a mass gap of at least 1 in these units.

It asserts nothing about uniqueness of the limit, interaction, short-distance behaviour or other groups.

**Standing.** One builder, one challenger, same model family. The challenger's plain verdict: as a statement it is a correct conditional theorem; 12 items stand, 3 defects, 2 not checked.
- *Defect in the proof, repaired without changing the statement:* the step that reads off the gap used a positive transfer matrix, which site-plane reflection positivity does not give (it gives T² ≥ 0). The challenger exhibits a site-reflection-positive chain with a negative eigenvalue for which the step fails, and the repair: use |F(s)| ≤ e^(−s)·F(0), valid for any self-adjoint T. (For the Wilson action T is positive by Lüscher's theorem, which nobody here has read.)
- *Defect of wording:* the free-field test is a test of an analogue of the theorem (unbounded fields, moment bounds in place of boundedness), not of the theorem.
- *Defect of status lines:* H3 was listed as proved for the free field while resting on a Green-function bound taken from memory; fixed here by saying so.
- Stands, with the challenger's own work: the factorial growth needed by the reconstruction theorem is in H3 itself; the limit is a distribution on test functions vanishing at coinciding points and convergence holds there; **the hypercubic group together with one irrational rotation in one plane generates a dense subgroup of O(4)** (Kronecker, conjugation into all six planes, the six generators span the Lie algebra; checked numerically by a child and a grandchild to 2.5·10⁻⁴); nearest-point rounding suffices; reflection positivity passes to the limit; the cluster property and unique vacuum follow from the gap without any uniform clustering of products.
- Not checked: which of H3 and H4 are theorems for the two-dimensional Ising model, the one interacting model where the conclusion is known.
- The reconstruction theorem was read only through a secondary source (Kravchuk, Qiao and Rychkov, arXiv:2104.02090, equation (9.18) and section 9.2); neither Osterwalder–Schrader paper was read by anyone here.

**Known-answer test of the chain.** For the lattice free massive scalar field with mass tending to zero (fields φ and :φ²:), the analogue of every hypothesis holds and the limit is the continuum free field of mass 1: the lattice gap is 2·asinh(m/2) to 10⁻¹⁵; the limit two-point function agrees with K₁(|x|)/(4π²|x|) to 2.3·10⁻³ at mass 1/32 on and off axis; rotation differences fall from 3.9·10⁻² to 6.7·10⁻³ as the mass goes from 1/8 to 1/32. Two programs (builder, challenger). So the chain is neither vacuous nor wrong on the one model where everything is explicit. It returns a free field there, as it must.

## (E): what "interacting" has to mean, and what it cannot mean

[`reviews/c1-E/HYPOTHESIS_E.md`](reviews/c1-E/HYPOTHESIS_E.md). Formulates and grounds; proves nothing about Yang–Mills.

**The director's formulation was wrong, and the worker says why.** The brief asked for non-Gaussianity of a gauge-invariant observable. But the gauge-invariant local fields of a *free* gauge theory are quadratic in a Gaussian field and are not Gaussian: the observable of Theorem B′ has, in the free limit, a χ²-type law with normalized fourth cumulant 4. Any test of the form "fourth cumulant nonzero, hence interacting" would call free Maxwell theory interacting. Proved, elementary. Two more elementary facts close other exits: every reflection-positive Euclidean two-point function is that of a generalized free field, so **no statement about one two-point function, including its short-distance behaviour, establishes interaction**; and "a second mass" or "a bound state" does not either, since a generalized free field can carry any spectral measure.

What does distinguish, among the formulations examined:
- **A two-particle energy shift.** If the lightest mass is an isolated eigenvalue, then in a periodic box of side z/m the lowest two-particle energy at zero total momentum equals 2m exactly for every free algebra (the Fock Hamiltonian is additive). A nonzero shift excludes them all. It needs an isolated one-particle shell, which a gap alone does not give. Stands as an argument; its link to the scattering length is from memory.
- **Failure of the ring rule.** The connected n-point functions of a Wick square of free fields are sums over cycles of products of one propagator; a composite field whose correlations violate that pattern is not such a square. Repairs the cumulant test for composite fields.
- **The short-distance statement** the official text asks for, in the precise form x⁸·⟨Θ(x)Θ(0)⟩·log²(1/(xΛ)) → C for the trace of the energy–momentum tensor (the constant not derived; leading-order perturbation theory, not read). It identifies which theory, not whether it interacts, by the remark above.

Calibration, measured: on the free lattice field the quantities vanish within errors; four-dimensional Ising at fixed ratio of correlation length to box side shows a renormalized coupling falling with the size (36, 29, 22, 20 at sides 6, 8, 12, 16; a logarithmic law is not tested, and the stricter of the worker's predicates failed for lack of statistics); two-dimensional Ising at criticality gives the Binder value 0.611, far from zero. The worker also found that the critical Binder value is not a clean discriminator, since it is nonzero for Gaussian-limit models too.

Grounding, with how read: Aizenman and Duminil-Copin (abstract); Göpfert and Mack's free limit (search snippet only: not established here); the SU(2) running coupling of Lüscher, Sommer, Weisz and Wolff (abstract). **No rigorous non-Gaussian scaling limit of a lattice gauge theory in three or more dimensions was found.**

## The complete list, as it now stands

For SU(2) the official statement would follow from: H0 (proved), H1 (the problem), H2 (proved within the program), H3 (open: ultraviolet), H4 (open: rotations), then beyond Theorem S: an interaction statement of the two-particle or ring-rule kind (open; only measurable at present), the short-distance statement (open; the one piece conceivably within reach of renormalization-group methods), and the other groups. Of eight items, two are proved, and they are the two that hold for U(1) as well.

## Record

Six workers this round (style reader, conditional chain, interaction hypothesis, exclusion, challenger of the chain, and two paper writers still running at the time of writing), each admitted with its child and grandchild as tasks in the Rust host's task graph (`pcpos task-limits`, `task-admit --parent`, `task-release`; depth 4; register [`../pcp/linux-23nov/task-graph.jsonl`](../pcp/linux-23nov/task-graph.jsonl)), each with the control answered first and its own register. The director has not rerun the workers' programs this round and has not read the proofs line by line. One model family throughout; not independent review.

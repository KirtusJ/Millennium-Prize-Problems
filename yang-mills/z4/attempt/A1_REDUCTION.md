# Attempt 1, part I: scale by the gap. A reduction, written for attack

Director Z4 (Linux session), 23 November 2026. Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic).

Status: drafted for attack, before any worker has seen it. Nothing here is a result until the review record under it says so. This file proves no property of four-dimensional Yang–Mills theory. It states a chain, proves the part of it that is elementary, and names the three statements (A), (B), (C) on which everything else rests and which are not proved.

## 0. The idea, in one paragraph

The usual way to state the continuum limit fixes a trajectory β(a) in advance (asymptotic freedom) and then has to prove that the gap in lattice units vanishes exactly at that rate. This attempt turns it round. Let m(β) be the gap of the lattice theory in lattice units, and *define* the lattice spacing by it: a(β) := m(β), in units in which the physical gap is 1. Then the gap in physical units is 1 by definition, and what has to be proved is no longer a rate. It is: (A) m(β) > 0 for every β; (B) m(β) → 0 as β → ∞, so that the spacing goes to zero; (C) a local observable, propagated over one correlation length, has bounded physical energy, so that its correlations survive the rescaling. Part I shows that (A), (B), (C) give a nontrivial limit of the two-point function with a gap. It is the standard picture of a continuum limit as the scaling limit at a critical point; the only thing claimed as this file's own is the exact form of (C) and the bookkeeping.

## 1. Setting

For each β > 0, a lattice theory in the following abstract form. (Section 4 says where each item comes from for the Wilson theory and what is assumed.)

- A Hilbert space 𝓗_β with a unit vector Ω_β.
- A self-adjoint operator T_β with 0 < T_β ≤ 1 (strictly positive), T_βΩ_β = Ω_β. Write T_β = e^(−H_β) with H_β ≥ 0 self-adjoint, H_βΩ_β = 0. Time is counted in lattice steps.
- **Gap in lattice units:** m(β) := inf spec(H_β restricted to Ω_β^⊥) ∈ [0, ∞].
- A vector ψ_β ≠ 0 with ψ_β ⟂ Ω_β. Its spectral measure for H_β is ν_β, a finite positive measure on [m(β), ∞), and for real n ≥ 0

  C_β(n) := ⟨ψ_β, e^(−nH_β) ψ_β⟩ = ∫ e^(−nε) dν_β(ε).

In the application ψ_β = (O − ⟨O⟩)Ω_β for a bounded gauge-invariant function O of the spatial links of one time slice near the origin, the same function for every β (or a slice-flowed one, section 5), and C_β(n) is its connected correlation at time separation n.

## 2. The three hypotheses

- **(A) Gap at every coupling.** m(β) > 0 for all β ≥ β₁.
- **(B) Criticality at weak coupling.** m(β) → 0 as β → ∞. Write ξ(β) := 1/m(β), the correlation length in lattice steps.
- **(C) Bounded energy at the correlation time.** There is D < ∞ such that for all β ≥ β₁: C_β(ξ/2) ≤ D · C_β(ξ).

  Equivalent form. Let E := ε·ξ be the energy in units of the gap, and let μ_β be the probability measure on [1, ∞) with dμ_β(E) ∝ e^(−E) dν_β (the energy distribution of the vector e^(−ξH/2)ψ_β, normalized). Then (C) says ∫ e^(E/2) dμ_β(E) ≤ D. By Jensen it implies that the mean physical energy of that vector is at most 2 log D.

  **(C⁺)**, the stronger form used for short physical times: for every integer j ≥ 1 there is D_j with C_β(ξ/2^j) ≤ D_j · C_β(ξ) for all β ≥ β₁ with ξ(β) ≥ 2^j.

Remarks on (C). It is a statement about locality and nothing else: if ψ_β were allowed to be any vector, one could take it in the spectral subspace [m, 2m], where C(ξ/2)/C(ξ) ≤ e, and (C) would hold with D = e. (C) for a *lattice-local* ψ_β says that the spectral measure of a local observable is regular between the lattice scale and the gap scale. If the correlation decays like a power n^(−p) for 1 ≪ n ≪ ξ and like e^(−mn) beyond, then (C⁺) holds with D_j ≈ e·2^(jp). It fails if there is an intermediate range of n in which the correlation collapses faster than any fixed power.

## 3. Theorem R (the reduction)

Assume (A), (B), (C). Put G_β(t) := C_β(tξ)/C_β(ξ) for t ≥ 0, the correlation at physical time t normalized at physical time 1. Then:

1. **(R1) Representation.** G_β(t) = ∫ e^(−(t−1)E) dμ_β(E) for t ≥ 1/2, with μ_β a probability measure on [1, ∞).
2. **(R2) Tightness.** μ_β((K, ∞)) ≤ D·e^(−K/2) for every K ≥ 0 and every β ≥ β₁.
3. **(R3) A limit exists.** Every sequence β_k → ∞ has a subsequence along which μ_β converges weakly to a probability measure μ on [1, ∞), and G_β(t) → G(t) := ∫ e^(−(t−1)E) dμ(E) for every t > 1/2.
4. **(R4) The limit has a gap and is not zero.** G(1) = 1; 0 < G(t) ≤ e^(−(t−1)) for t ≥ 1; G(t) ≥ exp(−2(t−1) log D) for t ≥ 1. So the limiting two-point function is the Laplace transform of a probability measure carried by energies ≥ 1: a gap of at least 1 in the units chosen, with spectral weight at finite energy (at most 2 log D on average).
5. **(R5) Short times.** Under (C⁺), (R3) holds for every t > 0, and G(2^(−j)) ≤ D_j.
6. **(R6) The spacing goes to zero.** In the units in which the gap is 1 the lattice spacing is a(β) = m(β), which tends to 0 by (B).

**Proof.** (R1): by (A), ξ < ∞ and ν_β is carried by ε ≥ m, that is E ≥ 1. C_β(ξ) = ∫ e^(−E) dν_β > 0 since ν_β ≠ 0. So μ_β is a probability measure and C_β(tξ)/C_β(ξ) = ∫ e^(−tE) dν_β / ∫ e^(−E) dν_β = ∫ e^(−(t−1)E) dμ_β. The integral is finite for t ≥ 1/2 by (C).
(R2): ∫_{E>K} e^(−E) dν_β ≤ e^(−K/2) ∫ e^(−E/2) dν_β = e^(−K/2) C_β(ξ/2) ≤ e^(−K/2) D C_β(ξ). Divide by C_β(ξ).
(R3): tightness on the closed set [1, ∞) and Prokhorov's theorem give the subsequence and μ, a probability measure on [1, ∞). For t ≥ 1 the integrand e^(−(t−1)E) is bounded and continuous. For 1/2 < t < 1 the integrand e^((1−t)E) is continuous and uniformly integrable, because ∫ e^(E/2) dμ_β ≤ D and (1 − t) < 1/2: ∫_{E>K} e^((1−t)E) dμ_β ≤ e^(−(t−1/2)K) D. So the integrals converge.
(R4): G(1) = μ([1, ∞)) = 1. For t ≥ 1, E ≥ 1 on the support, so e^(−(t−1)E) ≤ e^(−(t−1)), and the integral of a positive function against a probability measure is positive. By Jensen G(t) ≥ exp(−(t−1) ∫E dμ), and ∫E dμ ≤ 2 log ∫ e^(E/2) dμ ≤ 2 log D (the bound passes to the limit by lower semicontinuity).
(R5): the same with ∫ e^((1−2^(−j))E) dμ_β = C_β(ξ/2^j)/C_β(ξ) ≤ D_j.
(R6): definition. ∎

## 4. What Theorem R does not give

Stated now so that nobody reads more into it. Each item is a further obligation; none is addressed in part I.

1. **Only one two-point function.** The official problem asks for a quantum field theory: all correlation functions of a family of local fields, with the Osterwalder–Schrader or Wightman axioms. (R3) is the two-point function of one observable along one time axis.
2. **Not Euclidean invariance.** Nothing shows that the limit is rotation invariant, or even that spatial and temporal correlation lengths agree.
3. **Not interaction.** A free massive field satisfies (A), (B), (C) on the lattice (mass parameter sent to zero) and Theorem R returns the free massive field. The official text requires agreement with asymptotic freedom at short distances; a Gaussian limit would not be Yang–Mills. So a further claim is needed: **(E)** the limit is not Gaussian and its short-distance behaviour is that of asymptotic freedom. Three-dimensional compact U(1) is the warning: there (A) and (B) are theorems, and the scaling limit in units of the gap is believed to be a free massive field.
4. **Not the relation between a and β.** The attempt never uses a(β) ~ exp(−β/(2b₀N))·(power). If (A), (B) hold, that relation is a statement about how fast m(β) → 0. It is not needed for a gap; it is needed for (E).
5. **Infinite volume.** In a finite periodic box the transfer matrix is compact with a strictly positive kernel, so the gap is positive for trivial reasons at every β. (A) is a statement about infinite volume: inf over boxes of the finite-volume gap. The existence and uniqueness of the infinite-volume state at every β is itself an assumption of section 1.
6. **Uniqueness.** The limit is along subsequences.

## 5. Where each item of section 1 comes from for the Wilson theory

To be filled from the literature worker's report with locators, and from the other directors' folders with their own scope. Expected: reflection positivity and the strictly positive transfer matrix at every β (Osterwalder–Seiler; Lüscher); a gap at small β (Osterwalder–Seiler); nothing at large β.

The slice-flowed observable of `../fixed-size/SPATIAL_FLOW.md` fits section 1 without change: at flow time s·ξ² in lattice units it is a bounded gauge-invariant function of one slice's spatial links, of fixed physical size √s. For it (C) is the uniform lower bound of S6‴ in another form.

## 6. The discriminators

Every argument offered for (A), (B) or (C) is to be run against these. If it goes through where the statement is false, it is wrong.

| Model | (A) | (B) | (C) | Limit |
|---|---|---|---|---|
| Compact U(1), four dimensions, weak coupling | **false** (massless photon; no gap) | n/a | n/a | none of this kind |
| Finite gauge group, four dimensions, weak coupling | true | **false** (the gap grows with β) | n/a | no continuum limit at β → ∞ |
| Compact U(1), three dimensions | true (all couplings) | true | not known to this file | believed free massive |
| SU(2) or U(1), two dimensions | true | true | true by explicit formula | finitely many levels; no local dynamics |
| Free massive lattice field, mass → 0 | true | true | true | free massive field: (E) fails |
| Free massless field | false | n/a | n/a | none |
| SU(2), four dimensions | **claimed in part II** | **claimed in part II** | **claimed in part II** | the target |

The sources for the first four rows are to be confirmed by the literature worker; until then they are as the director recalls them.

## 7. What would break part I

A wrong direction in (R2); a hidden use of ν_β having no atom at the bottom; a failure of weak convergence to preserve [1, ∞); the Jensen step; (C) being vacuous or contradictory with (A), (B) (for example, if (C) for a lattice-local ψ contradicted a known lower bound); a discriminator row that is wrong; a model satisfying (A), (B), (C) whose limit is degenerate in a way section 4 does not list.


---

# Review record (23 November 2026) and part I as it now stands

The text above is the draft as handed to the workers, unchanged. A challenger attacked it ([`reviews/a2-chalR/report.md`](reviews/a2-chalR/report.md)) and a formalizer put its inequalities into Lean for finite sums of atoms ([`reviews/a2-leanR/A1R.lean`](reviews/a2-leanR/A1R.lean), 12 theorems, exit 0, standard axioms, recompiled by the director). Both are of the director's model family; not independent review.

## Verdict

**Theorem R stands, line by line (R1 to R6).** Sixteen items stand, eight are defects, one was not checked. No defect touches the proof. All eight are in what the director wrote around it: the framing, the remarks on (C), section 4 and the table. The challenger's own atom families confirm the conclusions numerically and show what happens when (C) or (C⁺) is dropped.

## Defects of the draft, all Z4's

1. **The framing undersold where the difficulty is (the most important one).** Section 0 calls part I "the part that is elementary" and lists (A), (B), (C) as if on a level. The challenger: the conclusions "gap at least 1" and "not zero" hold by construction (the unit is the gap; the correlation is normalized at one correlation length). Theorem R is Prokhorov's theorem and Laplace transforms. **Its whole content is its hypotheses, and (A) at large β is the infinite-volume lattice mass gap at weak coupling, which is the hard core of the problem.** The reduction moves nothing; it only says in what form the difficulty has to be met. This should have been the first sentence.
2. **"(C) is a statement about locality and nothing else" is false.** Counterexample: two decoupled free lattice fields with masses m₁ ≫ m₂ = m and the local vector φ₁(0). (A) and (B) hold; C(ξ/2)/C(ξ) grows like e^(m₁ξ/2). So (C) also says that the observable overlaps the lightest states: it is a condition on the dynamics and on the choice of field, with locality only one part of it.
3. **"(A) is inf over boxes of the finite-volume gap" is wrong.** In the low-temperature Ising model the finite-volume gap tends to zero by tunnelling while each pure phase has a gap. Only liminf of the finite-volume gaps ≤ the infinite-volume gap holds in general. (A) is about the infinite-volume theory; the inf over boxes is a stronger statement that can fail where (A) holds.
4. **Section 4 omits four things.** (a) The lowest energy the chosen vector sees in the limit can be above 1, so "the gap is 1" is shown only as "at least 1". (b) The limit can be a single atom, a pure exponential, which is not what a local relativistic field gives at a fixed point of space. (c) The normalization C_β(ξ) tends to zero and nothing makes the normalizations of different fields consistent. (d) C_β(ξ/2) is not a lattice correlation when ξ/2 is not an integer; log-convexity reduces (C) to integer times, which the draft should have said.
5. **(R1) wording.** At fixed β the integral is finite for every t ≥ 0; (C) is needed for uniformity in β, not finiteness.
6. **The constant in the power-law remark.** For a spectral density ε^(p−1) the exact limit is D_j = 2^(jp)·Γ(p, 2^(−j))/Γ(p, 1). The growth 2^(jp) is right; the factor e is right only for p = 1.
7. **Table, three-dimensional U(1).** Göpfert and Mack treat the Villain action; and the free massive limit is their theorem (as the abstract states), not a belief.
8. **Table, two dimensions.** In infinite spatial volume a bounded gauge-invariant function of the links of a bounded region of one slice is constant in two dimensions, so there is no vector ψ at all and m = +∞. "True, true, true" holds only on a finite circle with a function of the holonomy, which is the finite-volume case section 4 set aside. The row is wrong as written.

## What the challenge adds

- **(C) can be weakened.** For every conclusion at t ≥ 1 except the explicit lower bound, tightness of μ_β suffices; and any c in (0, 1) can replace 1/2: C_β(cξ) ≤ D·C_β(ξ) gives the tail D·e^(−(1−c)K), mean energy at most log D/(1−c), and convergence for t > c. (In Lean: `A1R.L2`.) Without tightness the limit degenerates to G(1) = 1 and G(t) = 0 for t > 1.
- Every admissible D is at least √e. For a vector in the spectral subspace [m, 2m] the sharp constant is e (`A1R.L6`, `A1R.L6_sharp'`).
- Free massive lattice field, mass to zero, ψ the field at a site: C(ξ/2)/C(ξ) tends to 2K₁(1/2)/K₁(1) = 5.504 (computed by the challenger and its child to nine digits). So (C) holds there with an explicit constant.
- Discriminators the table should add: the four-dimensional φ⁴ and Ising models, whose scaling limit is proved Gaussian (Aizenman and Duminil-Copin), as the sharpest test of any argument for (E); the two-dimensional O(N) model for N ≥ 3; and the two-mass free field above as a test of any argument for (C). (Sources from the challenger's memory; to be confirmed.)
- In a finite box the argument for a positive gap is Jentzsch's theorem for a strictly positive continuous kernel together with compactness, on the gauge-invariant subspace (after the temporal links are integrated); on the full L² the operator is not strictly positive. From the challenger's memory.

## Part I as it now stands

**Theorem R′.** In the setting of section 1, assume (A), (B) and, for some c in (0, 1) and D < ∞, C_β(cξ) ≤ D·C_β(ξ) for all β ≥ β₁. Then along a subsequence the normalized correlation G_β(t) = C_β(tξ)/C_β(ξ) converges for every t > c to the Laplace transform, in t − 1, of a probability measure μ on [1, ∞) with ∫E dμ ≤ log D/(1 − c). Proved; finite-sum inequalities in Lean.

What it is: the statement that **if** the infinite-volume lattice theory has a gap at every coupling which closes at weak coupling, **and** a chosen local observable keeps bounded energy in units of that gap after one correlation length, **then** its two-point function has a nonzero gapped scaling limit. What it is not: any part of a proof of those hypotheses; a field theory (one two-point function, one time axis, subsequences); Euclidean invariant; interacting. A free field satisfies all of it.

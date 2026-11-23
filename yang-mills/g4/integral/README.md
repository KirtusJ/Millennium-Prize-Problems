# Integral reflection positivity for compact Wilson regulators

Director G4, continuation of the 22 November 2026 research session. This extends the [complex finite-test interface](../complex/README.md) to Bochner integrals on configuration spaces that need not be finite. The finite Gram criterion below is a conditional reflection-positivity theorem. It does not construct the four-dimensional Yang–Mills continuum theory or a mass gap.

## Measure and observable contract

For a positive measure μ, a specified reflection θ and complex observables, set

\[
B_{\mu,\theta}(F,G)=\int\overline{F(\theta x)}G(x)\,d\mu(x).
\]

[IntegralReflectionPositivity.lean](IntegralReflectionPositivity.lean) expands finite complex test combinations into their reflected integral kernel. Every pairwise reflected product is assumed integrable. The configuration space, measure, reflection and represented test functions may change with the regulator. Common labels, convergence of every kernel entry, and eventual positivity for each fixed finite complex test imply positivity of the limiting kernel. The eventual threshold may depend on the test. Neither a common convergence rate nor existence of the desired limit is supplied.

For a measurable q with q∘θ_X = θ_Y∘q, integration against **exactly** `Measure.map q μ` equals integration of the pulled-back reflected product. The source records the target product's almost-everywhere strong measurability and an equivalence of integrability. Positivity transport additionally assumes genuine integrability. This identifies the inherited measure; it gives no equality to a separately defined quotient Wilson action or repeated time-slice averaging.

## Finite compact-group Wilson application

Let G be a compact second-countable group with its Borel σ-algebra and normalized Haar measure h, and E a finite set of links. The configuration space G^E is compact. With μ₀ = h^E and a continuous real action S, the partition

\[
Z=\int e^{S(U)}\,d\mu_0(U)
\]

is finite and strictly positive. The normalized Wilson law is μ₀ tilted by S. The Lean theorem `wilson_link_tilt_probability` proves its probability normalization for any Borel probability base law; Haar invariance is not used in that normalization theorem. A group structure, Haar construction, plaquette holonomies and gauge invariance are not silently encoded in its parameter name. Supply normalized Haar when applying it to Wilson theory.

`wilson_action_continuous` accepts finite sums Σ β_p φ_p of continuous real plaquette functions. For a finite-dimensional continuous unitary representation, the usual real trace of the oriented plaquette holonomy supplies such functions analytically. Normalization allows arbitrary real coefficients. Nonnegative cross-plane coefficients and the chosen reflection geometry enter the separate positivity argument. Continuous reflected tests on this compact space are integrable under the normalized law. Constant one has expectation one, and the reflected square of the constant i is one.

Mathlib's Bochner integral is totalized: a nonintegrable function has integral zero. More sharply, `Measure.tilted` becomes the **zero measure** if exp(S) is not integrable. The source proves this control and does not mistake its zero reflected pairing for a normalized state. Compact continuity and the nonzero base measure exclude that case here.

## Finite Gram criterion and its Wilson boundary

For integrable complex modes u_r and real coefficients a_r on a finite index set,

\[
\int d\mu(x)\int d\mu(y)\sum_r a_r\overline{u_r(x)}u_r(y)
=\sum_r a_r\left|\int u_r\,d\mu\right|^2.
\]

The Lean proof justifies both finite-sum interchanges. The product-measure version takes joint integrability explicitly before Fubini. Nonnegative a_r and a strictly positive normalization imply a real nonnegative normalized integral.

For a split configuration (x,y), reflection swapping the halves, and the positive-half test F(y), the tested Wilson density must be identified with such a Gram expression. `reflectedIntegral_wilson_of_gram` states this condition explicitly. It is a sufficient criterion, not an assertion that every continuous action has it. Modes of the form u_r=φ_r F produce the familiar sum of squared half-integrals. Boundary variables can be conditioned on and integrated afterwards, provided the joint integrability and factorization statements are supplied; that additional conditioning construction is not formalized in this file.

The [direct Wilson-kernel proof](wilson-kernel.md) goes further analytically: real and imaginary matrix entries give a finite real feature decomposition of ReTr(A*B). The exponential's finite word expansions are Gram kernels, and an explicit uniform remainder bound passes their tested integrals to the full positive Wilson density. This proves RP for the displayed split holonomy action, including the actual compact-group kernel exp(β ReTr(ρ(x)*ρ(y))) with the first representation matrix adjointed, and continuous same-half actions. The matrix feature expansion and convergence estimate are not yet Lean formalized; identifying a given lattice's crossing plaquettes and boundary variables with that split action remains necessary.

The rendezvous supplied an actual geometry identification: [the finite open temporal slab with free ends](open-slab.md). Anchored temporal gauge preserves product spatial Haar at fixed temporal links. Strictly half-supported gauge-invariant tests are preserved, and crossing plaquettes become the matrix-feature kernel. Together these analytic arguments establish finite-slab RP under the stated reflected boundary and coupling hypotheses. Any extra end factors must be gauge invariant. Periodic temporal holonomy is excluded. Shared-boundary uniform estimates require bounded tests, for example joint continuity on the compact product, and fiber normalization must reweight the boundary law.

The Wilson character argument is a separate analytic input. [Lüscher's original transfer-matrix construction](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf), printed pp. 8–10, obtains nonnegative representation coefficients for its SU(N) single-link kernel by expanding the exponential and decomposing tensor products. It then relates the transfer construction to specified lattice boundary conditions. This source supports the factorization route; its representation theory, boundary construction and transfer identification have not been formalized here. Strict positivity of a fixed-regulator transfer operator does not give a uniform continuum mass gap.

Finite Gram approximants may have negative or nonreal off-diagonal values. Do not declare them probability densities. For the infinite character expansion, prove convergence of the **tested integrals** to those for the actual nonnegative Wilson density, then apply the closed-ray limit theorem. For bounded F, L¹ convergence of kernels suffices analytically through the bound ‖F‖∞²‖K_n−K‖₁. No infinite sum/integral interchange is included without such justification.

A strictly positive, symmetric two-point density with matrix [[1,2],[2,1]] is not reflection positive: with uniform product base measure and F=(1,−1), its normalized reflected expectation is −1/3. Conversely, the Gram matrix of (1,−1) has negative off-diagonal entries. These are analytic controls distinguishing positive densities from positive quadratic forms; the previous component contains compiled finite counterexamples of the same distinction.

## Coordination and remaining construction

- **C4:** use the exact pushed-forward measure and commuting reflection. The history-space sector and inherited dynamics need their own operator identification; no quotient action is substituted.
- **A4:** compact continuous observables supply integrability at each finite lattice. Their normalization and common limiting test maps remain inputs, and positive forms may still give a trivial limit.
- **B4:** a Wilson factorization or an identified positive transfer representation must connect the actual action, boundaries and admissible positive-time algebra. Fixed spatial mesh and volume, the time-continuum limit, the thermodynamic limit and spatial refinement remain distinct operations.
- **D4/Z4:** this provides complex reflected forms on common labels. It supplies neither a physical clock, a coherent cutoff spectral measure, a positive-time decay envelope, nor control of the full vacuum complement. Multiple vacuum states and endpoint spectral mass must be handled in the spectral argument.

The remaining OS axioms, continuum identification, null-space quotient and completion, nontriviality, and a positive mass gap in the same physical units remain open. The finite identities and normalization facts are elementary; no novelty is claimed.

See [execution.md](execution.md) for checked declarations, adverse controls, recursive PCP records and exact-byte reproduction.

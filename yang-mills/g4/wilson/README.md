# Wilson-kernel convergence and open-slab reflection positivity

Director G4, continuation of the 22 November 2026 research session. [WilsonReflectionPositivity.lean](WilsonReflectionPositivity.lean) formalizes exponential-kernel convergence under integration, its finite-word Gram expansion, and reflection positivity of an explicit finite compact-group Wilson slab. It builds on the [complex](../complex/README.md) and [integral](../integral/README.md) modules. The proof does not construct a continuum Yang–Mills theory or establish a mass gap.

The principal theorem is `openSlab_wilson_reflection_positive`. Its conclusion includes probability normalization of the original law, integrability of the reflected observable and a real, nonnegative expectation. The desired reflection-positive integral or its equality to a reduced integral is not a hypothesis. [Execution and evidence](execution.md)

The subsequent [periodic Haar-averaging extension](../periodic/README.md) retains two independent seam families, includes a concrete period-two theorem, and removes the gauge-invariance premise on continuous half tests by using auxiliary gauges. The source and evidence of this earlier open-slab module remain unchanged.

## Exact configuration and hypotheses

Let G be a compact second-countable topological group with its Borel measurable structure. Supply a probability measure m invariant under both left and right translations, and a finite-dimensional unitary representation ρ whose matrix entries are continuous. Normalized Haar and the representation are inputs; this module does not construct them.

A finite half-graph has edge set E and endpoint functions src,dst:E→V. A finite subset B of vertices marks the reflecting boundary. Each crossing term c in a finite index type C selects a half edge e(c), whose source and destination are specified members of B. The full configuration is

\[
 x=((U_0,U_1),h)\in(G^E\times G^E)\times G^B,
 \qquad \mu_0=(m^E\otimes m^E)\otimes m^B.
\]

The two halves may contain arbitrary internal edges. There is one family of links crossing the boundary. The reflection swaps the halves and sends every h_b to h_b⁻¹. Its continuity and involutivity are proved. With χ(g)=Re tr ρ(g), the actual exponent is

\[
 S(x)=s(U_0)+s(U_1)+\sum_c\beta_c\,
 \chi\!\left(U_0(e(c))h_{\mathrm{dst}(c)}U_1(e(c))^{-1}h_{\mathrm{src}(c)}^{-1}\right).
\]

Every crossing coupling β_c is nonnegative. The half action s is real, continuous and gauge invariant. The test F:G^E→ℂ is continuous and gauge invariant. `positiveHalfTest F` depends only on U₁, so its reflected product is exactly conjugate(F(U₀))F(U₁). The same s appears on both halves. An optional end action must be included in this half-local, reflected, continuous, gauge-invariant s.

`gaugeInvariant_wilsonHalfAction` and `continuous_wilsonHalfAction` prove the hypotheses for finite weighted sums of actual plaquette words U(e₁)U(e₂)U(e₃)⁻¹U(e₄)⁻¹. Their four incidence equations close the oriented walk. These lemmas can be substituted directly into the principal theorem. The half-action weights may be arbitrary real numbers; only the crossing couplings require a nonnegative sign.

The graph data allow repeated terms and degenerate closed walks. They do not encode a particular cubical cell complex or certify that a supplied list exhausts that complex's plaquettes. Applying the theorem to a named lattice requires supplying its finite data and incidence equations.

## Kernel convergence and positivity

For continuous real features v_r on a compact space X, define

\[
 D(x,y)=\sum_r v_r(x)v_r(y),\qquad
 K_N(x,y)=e^{s(x)+s(y)}\sum_{k<N}\frac{D(x,y)^k}{k!}.
\]

`tendsto_partialExp` proves the exponential series limit. `abs_partialExp_le` proves an N-independent bound by exp(|D|). `tendsto_testedTaylor_integral` proves

\[
 \int K_N(x,y)\overline{F(x)}F(y)\,d\mu
 \longrightarrow
 \int e^{s(x)+s(y)+D(x,y)}\overline{F(x)}F(y)\,d\mu
\]

for any finite Borel measure μ on X×X. The dominating function is constructed explicitly from the continuous half factors, exp(|D|) and the two test norms; compactness proves its integrability. Neither convergence nor domination is assumed. The formal result supplies pointwise and tested-integral convergence, not a quantitative uniform-tail rate.

At degree k, expansion over all ordered words w:Fin k→D gives a sum of

\[
 \frac1{k!}\overline{M_w(x)}M_w(y),\qquad
 M_w(x)=e^{s(x)}F(x)\prod_{i<k}v_{w(i)}(x).
\]

On an identical product probability law, each integral is (1/k!) times the squared modulus of the integral of M_w. The finite sums are therefore nonnegative complex numbers, and the proved integral convergence preserves that property. `split_wilson_reflection_positive` then divides by the finite, strictly positive partition. The auxiliary `normalized_testedWilson_of_integral_eq` is conditional; the concrete final theorem uses the separately proved normalized bridge instead.

For the Wilson application the features are the real and imaginary parts of every matrix entry of ρ(U(e(c))), each multiplied by sqrt(β_c). `dot_matrixFeatures` proves that their dot product is

\[
 \sum_c\beta_c\operatorname{Re}\operatorname{tr}
    \bigl(\rho(U_0(e(c)))^*\rho(U_1(e(c)))\bigr).
\]

The unitary inverse and real-trace identities are proved explicitly. This identifies the reduced exponent with the split-feature exponent used by the positivity theorem.

## Original links and the normalized measure

For each fixed h, extend h to a vertex gauge g_h by setting it to one outside B. Gauge only U₁:

\[
 U'_1(e)=g_h(\mathrm{src}(e))U_1(e)g_h(\mathrm{dst}(e))^{-1}.
\]

`crossingWord_eq_gauged` proves the noncommutative crossing-word identity. Gauge invariance keeps s and F unchanged. `positiveBoundaryEquiv` is a measurable equivalence preserving the product half law: every transformed edge is a left and right Haar translation. The original exponent and tested density are continuous on a compact space, so Fubini is justified. Integrating each fixed-h equality and then the constant h integral transports both the partition and numerator. `openSlab_integral_eq_reduced` proves the equality of the **normalized** original and reduced integrals.

This finite open-slab proof has one crossing family. It does not remove residual holonomy on a periodic time circle. B4's [periodic two-seam argument](../../transfer-operator/periodic-time/README.md) is a separate result. The earlier [analytic open-slab note](../integral/open-slab.md) remains an immutable historical candidate; this module supplies the formal double-half version without requiring all temporal links inside either half to be fixed.

## Validation and remaining scope

The source contains 62 theorems and 25 definitions. All 87 declaration reports were accepted by Lean 4.19.0 at the pinned Mathlib revision, with only standard axioms. The finite-dimensional feature identity, tested-integral convergence, explicit boundary gauge geometry and original-law positivity are now formalized. The compiler and native source receipts bind the same bytes; the recursive PCP source audit reviews those bytes. The negative controls and process records are described in [execution.md](execution.md).

The module supplies no infinite-volume limit, continuum-limit existence, nontriviality, four-dimensional reconstruction, Lorentz covariance, spectral estimate or positive mass gap. It does not claim all Osterwalder–Schrader axioms, reflection invariance of the full measure as a separate theorem, positivity for arbitrary nongauge-invariant half tests, or the periodic two-seam result.

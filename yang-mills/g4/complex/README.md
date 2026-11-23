# Complex reflection positivity on a common test family

Director G4, November 22, 2026. This extends the real result with conjugation, the zero-imaginary-part condition, finite reflected-function expansions, and exact finite quotient transport. The [director rendezvous](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1) coordinates this interface with A4's observables, B4's transfer estimates, C4's quotient measures and D4's spectral limits.

## The preserved condition

For a complex kernel K, a finite index type J, a label map i : J -> I and complex coefficients c,d, define

\[
B_K(i;c,d)=\sum_{a,b\in J}\overline{c_a}\,d_b K(i_a,i_b),\qquad
Q_K(i;c)=B_K(i;c,c).
\]

The condition is **Im Q = 0 and Re Q >= 0**. Re Q >= 0 alone is insufficient. The first slot is conjugate-linear and the second linear; both additivity and scalar laws are formalized. Labels may repeat.

Entrywise convergence of complex kernels on one common label set implies convergence of every such finite pairing. If each fixed test satisfies the full condition eventually, its limit satisfies it. The starting cutoff may depend on the whole finite test. The theorem does not exchange an infinite test sum with a limit or establish a single cutoff that works for all tests. Its underlying closure result works along any nontrivial filter. The sequence theorem quantifies the eventual cutoff inside the finite test.

For example, put -1 at diagonal label n and +1 at every other diagonal label of K_n on the natural numbers. Each fixed finite test eventually avoids that defective label, and the common entrywise limit is the identity kernel. At every cutoff a negative singleton test remains. This analytic example distinguishes test-dependent eventual positivity from a uniform cutoff; it is not an additional Lean theorem here.

## Reflected observables and quotient measures

On a finite configuration space X with weights w and a specified map theta, the reflected pairing is

\[
\langle F,G\rangle_{w,\theta}
=\sum_{x\in X} w_x\,\overline{F(\theta x)}G(x).
\]

The finite expansion theorem identifies the pairing of two complex linear combinations of test functions with B_K for their reflected kernel. The identity is algebraic and permits arbitrary complex weights and any theta. Positivity of those weights is not asserted to imply reflection positivity. In a physical application the weights, reflection, admissible positive-time tests and their regulator maps must be supplied.

The regulator interface allows X_n, weights, reflections and represented test functions to change with n. The common object is the label set I and the limiting pairings. Assuming entrywise convergence of those reflected kernels and eventual positivity of every represented finite test yields the full complex finite-test condition in the limit. Existence of the limit and positivity of the chosen interacting regulator remain separate inputs. Compact SU(2) link configuration spaces are not finite sets. Applying this finite-sum interface to them requires a justified approximation or a separate integral-expansion proof with its integrability hypotheses. The general complex kernel-limit theorem itself does not require configuration spaces to be finite; only its test sums are finite.

For a map q : X -> Y, the finite pushforward weight is exactly

\[
\bar w_y=\sum_{x:q(x)=y} w_x.
\]

If q(theta_X x) = theta_Y(q x), the reflected pairing downstairs equals the pairing of the pulled-back tests upstairs. Thus a nonnegative reflected test upstairs gives a nonnegative test for this exact pushforward. Neither injectivity nor surjectivity is required. This finite identity supplies no comparison to a different quotient action or to a procedure which averages signs anew at each time slice. C4's shared-edge measure remains the relevant input for its Wilson quotient. The continuum pushforward/integration result and inherited transfer dynamics are not formalized by this finite identity.

## Adverse tests

| Test | Checked distinction |
|---|---|
| One-point K = 1, c = i | The sesquilinear square is +1; the unconjugated bilinear expression is -1. |
| One-point K = i, c = 1 | Re Q = 0 but Im Q = 1, so the full condition fails. |
| Hermitian K = [[1,2i],[-2i,1]] | For real coefficients a,b, Q = a²+b²; for (1,i), Q = -2. Real coefficient tests do not replace complex ones. |
| Zero kernel | All forms vanish. Positivity alone supplies no nontrivial state. |
| Two points with weights 1/2, swapped by theta, F = (1,-1) | The reflected square is -1; with identity reflection it is +1. The swap is involutive and the weights positive, normalized and invariant under it. Positivity is relative to the specified test class; arbitrary functions on configuration space need not be admissible positive-time observables. |

The real-coefficient matrix theorem is stated for its two coordinate coefficients. Repeated real labels reduce to that case by adding their coefficients at each of the two labels; that reduction is an analytic observation, not a separate formal aggregation theorem.

## What this does not construct

The source closes the complex finite-kernel gap in the earlier G4 component. A Yang–Mills application still needs a common continuum positive-time test algebra and its regulator representations, convergence to the intended Schwinger functions, the other reconstruction hypotheses, control of the null-space quotient and its completion, nontriviality, and a uniform physical spectral estimate on the same reconstructed theory. None of these is replaced by an axiom-print command, a PCP receipt, the finite quotient identity, or a negative test of a different model.

The finite identities and closure theorem are elementary; no novelty or solution of the Millennium problem is claimed. [Lean source](ComplexReflectionPositivity.lean) · [Execution, model challenge and compiler evidence](execution.md)

**Subsequent extension:** [Integral reflected pairings](../integral/README.md) now provide the separate integral expansion and exact measurable pushforward described above, with explicit integrability, compact continuous Wilson normalization and a finite-Gram criterion. The [analytic split Wilson-kernel proof](../integral/wilson-kernel.md) supplies a matrix-feature convergence argument. This does not alter the finite scope of the present source or establish inherited quotient dynamics.

## Connection to the other directors' results

G4 read [B4's strong-coupling argument at ad36c25](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/ad36c2533f17313c2103d118da4450eae432224f/yang-mills/transfer-operator/strong-coupling), especially its slab-to-vacuum and dense-slice step. Conditional on the stated compact, positive self-adjoint physical transfer operator, simple leading eigenvalue and boundary overlaps, the order is sound: first send the two slab endpoints away at fixed spatial volume and insertion times; then use arbitrarily late insertion times for each fixed centered test. The comparison prefactor can depend on the test and volume because it disappears in the spectral-tail limit. Complex linearity of the common spectral projection then passes zero from the real multiplier states to their complex span, and closedness plus the stated density gives zero on the whole vacuum complement. Uniformity in volume belongs to the resulting transfer bound, not to an interchange of these limits.

The Hermitian adverse control above does not refute that argument: B4 supplies an already identified positive complex Hilbert-space transfer and spectral projection. Real tests of an otherwise arbitrary complex kernel do not supply those objects. G4's review is mathematical and conditional on that transfer construction; it is not a G4 Lean replay or an independent verification of the cited compact-kernel, gauge-projection and comparison theorems.

[D4's coherent-diagonal criterion](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/59d0aca9be4bf8f0f7978de77d16152e2a224768/yang-mills/spectral-support/diagonal) provides another route once the cutoff spectral measures converge weakly in a common physical transfer variable. The new G4 result supplies neither that convergence nor the physical clock. In every route, A4's normalization and test maps, C4's actual measure, B4's operator and D4's spectrum must describe the same construction.

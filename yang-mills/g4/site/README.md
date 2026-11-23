# Shared boundary normalization and site reflection

Director G4 · 23 November 2026 · Yang–Mills component, coordinated with C4 on [issue 1](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7095709237).

The [Lean module](SharedBoundaryPositivity.lean) proves the exact shared-boundary weight for a compact continuous product tilt and transfers an explicitly supplied fiber reflection inequality to the original normalized joint law. It also proves the group-word identity needed for straight-path rooted reversal. These are finite-measure statements, not a construction of continuum Yang–Mills theory or a mass gap.

Let `Y,Q` be compact, second-countable Borel spaces with probability measures `η,μ`, and let `S : Y × Q → ℝ` be continuous. The shared boundary is `y∈Y`; all remaining variables lie in `Q`. Set

\[
 Z_y=\int_Q e^{S(y,q)}d\mu(q),\qquad
 Z=\int_{Y\times Q}e^{S(y,q)}d(\eta\otimes\mu),\qquad b(y)=Z_y/Z.
\]

Every partition is strictly positive. The source proves integrability of `b` and `∫b dη=1`. For every continuous complex observable `P`, it proves

\[
 \int P\,d[(\eta\otimes\mu)^{S}]
 =\int_Y b(y)\left(\int_Q P(y,q)\,d\mu^{S_y}(q)\right)d\eta(y).
\]

The superscript denotes the normalized exponential tilt. In particular, normalized conditional laws cannot simply be averaged against the original boundary law `η`. A two-state example in the [exact finite controls](check_geometry.py) gives the correct expectation `3/4`, versus `1/2` when the factor `Z_y/Z` is omitted. Boundary-only action terms are included inside `S`; if `S(y,q)=w(y)+A(y,q)`, then `Z_y=e^{w(y)}∫e^{A(y,q)}dμ`.

For a continuous boundary-preserving map `Θ(y,q)=(y,θ_y(q))` and continuous `F`, the final positivity theorem assumes, for **every** `y`, the real nonnegativity of

\[
 \int_Q \overline{F(y,\theta_yq)}F(y,q)\,d\mu^{S_y}(q).
\]

It concludes that the original joint tilt is a probability measure, that the full reflected integrand is integrable, and that its integral is real and nonnegative. This is a theorem for each `F` satisfying its premise; quantifying over an appropriate test algebra remains an application obligation. No gauge-invariance assumption on `F` appears. Neither involutivity nor measure invariance of `Θ` is asserted by this positivity-transfer theorem.

The normalized mixture and positivity results require continuity, so their integrals are genuine integrable expectations. The auxiliary algebraic identity `weighted_fiberExpectation` permits arbitrary `P`; by itself it makes no integrability assertion. Its uses in the continuous-observable theorems discharge integrability separately.

## Application to site reflection

The [even-torus proof](even-torus/README.md) evaluates the positive fiber square for all four coordinate directions and applies it to the plaquette tail and the weak-coupling lattice-gap upper bound in periodic infinite-volume states.

For even periodic extents, `Y` can contain both fixed tangent-link layers. For odd extents it can contain the site-fixed layer while `Q` retains the far-cut variables. The [periodic Wilson module](../periodic/README.md) supplies related finite boundary-graph positive forms. Combining it with this mixture theorem requires an explicit identification of the original link product, action, test and reflection with the chosen fiber data. This release does **not** encode the complete even/odd lattice inventory or discharge that application premise automatically.

If the reflected plaquette has word `e⁻¹ p⁻¹ e` and the straight root paths obey `r_a=r_b e⁻¹`, the source proves in every group

\[
 r_b(e^{-1}p^{-1}e)r_b^{-1}=(r_a p r_a^{-1})^{-1}.
\]

Thus the straight-path conjugation is exact. Quaternion inversion supplies the imaginary-part sign in the analytic SU(2) argument. Comparing different prescribed fixed root paths still requires the near-identity loop estimate and tight scaled curvature; the Lean group identity proves neither of those analytic estimates.

## Cross-read and evidence

The [C4 review](cross-review.md) addresses rooted orientation, odd far seams, the four-copy block bound and physical-time order. Its conclusions are scoped and conditional where upstream analytic results are used. A separate local replay accepts C4's 22-declaration source at pinned commit `32e17b1836c139abf81c6d4cbce54e199185331c`; those scalar statements do not formalize the full Gaussian-field or spectral-limit argument.

The exact finite controls check 1,548 box/orientation cases using cube and face vertex sets, a rational Z2 gauge projection and odd-site quadratic form, and the boundary-reweighting counterexample. They support their finite claims only. See the [execution record](execution.md) for the compiler, adverse-source, recursive PCP, native calibration and recorded-byte verification scopes.

# Haar-averaged reflection positivity with two periodic seams

Director G4 · 23 November 2026 · autonomous continuation of the Millennium research program.

[PeriodicReflectionPositivity.lean](PeriodicReflectionPositivity.lean) proves reflection positivity for an explicit compact boundary-graph law and its period-two specialization. The seam variables are integrated under their original Haar reference law. The half action and half test need no gauge-invariance premise. This extends the [verified Wilson module](../wilson/README.md) and supplies the compact-integral counterpart of B4's [two-seam argument](../../transfer-operator/periodic-time/README.md). [Execution, audit and controls](execution.md)

## The exact finite law

Let X be a compact second-countable Borel space with probability μ. Let G be a compact second-countable Borel topological group with a left-invariant probability m. Supply a finite-dimensional unitary representation ρ with continuous matrix entries. Normalized compact Haar is the intended m; its construction is not part of this module. In particular, the integration proof only uses left invariance.

Choose finite sets B of boundary labels and C of crossing terms, endpoint functions src,dst:C→B, continuous maps U_c:X→G, nonnegative crossing coefficients β_c, a continuous real half action s and a continuous complex half test F. The reference measure and exponent are

\[
 \mu_0=(\mu\otimes\mu)\otimes m^B,
 \quad z=((x,y),h),
\]
\[
 S(z)=s(x)+s(y)+\sum_c\beta_c\operatorname{Re}\operatorname{tr}\rho
 \left(U_c(x)h_{\mathrm{dst}(c)}U_c(y)^{-1}h_{\mathrm{src}(c)}^{-1}\right).
\]

The sign convention is a density proportional to exp(S). A nonnegative real-character coupling in this exponent is essential. Shared endpoint labels retain the dependence between crossing faces incident on the same temporal link. Repeated crossing terms and loops are permitted.

Reflection sends ((x,y),h) to ((y,x),h⁻¹), and the positive-half observable is F(y). `boundary_wilson_reflection_positive` concludes that ν=μ₀.tilted S is a probability, conjugate(F(x))F(y) is ν-integrable, and

\[
 \int\overline{F(x)}F(y)\,d\nu\in[0,\infty)\subset\mathbb C.
\]

The definition of the original law contains every seam variable. The theorem does not assume its positivity, a normalized-integral identity or a desired pushforward equality. It assumes identical half reference laws and the same half action in reflected coordinates. Neither s nor F may depend on the seam variables.

## Why gauge invariance of the test is unnecessary

Introduce independent auxiliary p,q in G^B. On the enlarged half space X×G^B define the matrix features from

\[
 A_c(x,p)=\rho\left(p_{\mathrm{src}(c)}U_c(x)p_{\mathrm{dst}(c)}^{-1}\right),
\]

using real and imaginary matrix entries scaled by sqrt(β_c). The formal group and real-trace identities give

\[
 \langle v(x,p),v(y,q)\rangle
 =\sum_c\beta_c\operatorname{Re}\operatorname{tr}\rho
 \left(U_c(x)(p^{-1}q)_{\mathrm{dst}(c)}U_c(y)^{-1}
 (p^{-1}q)_{\mathrm{src}(c)}^{-1}\right).
\]

For each fixed p, left invariance makes p⁻¹q Haar. `integral_relativeMap` derives the equality of the original integral and the enlarged product integral by Fubini. Compact continuity supplies its integrability premises, including every fixed-parameter fiber. `integral_relativeMap_tilted` applies that result to the density and weighted observable separately, transporting both the numerator and partition. The positive finite partition is supplied by the preceding Wilson module.

The half action s(x) and test F(x) are left untouched: only the auxiliary gauges change. The enlarged-space split-kernel theorem therefore applies to every continuous half test. Its positivity follows from the already verified Taylor convergence and ordered-word Gram expansion. This differs from the previous open-slab proof, which changed the original positive-half configuration and consequently required its action and test to be gauge invariant.

## Period two and the two seam labels

`periodTwo_reflection_positive` makes the concrete choices

\[
 X=G^E,\quad\mu=m^E,\quad B=\mathrm{Bool}\times V,
 \quad C=\mathrm{Bool}\times E,
\]
\[
 \mathrm{src}(i,e)=(i,\mathrm{src}(e)),\qquad
 \mathrm{dst}(i,e)=(i,\mathrm{dst}(e)),\qquad U_{(i,e)}(x)=x_e.
\]

Thus the two seam terms use the same spatial boundary evaluation but retain distinct temporal coordinates. `twoSeamEndpoint_distinct` formally checks that the two tags at an edge's endpoint differ. Both crossing layers keep their multiplicities; they may have different nonnegative couplings. Identifying two oppositely directed physical temporal links merely because their unordered endpoints coincide would change this model.

The orientation comparison is also formal: `opposite_seam_character` proves that the real character of a h_d b⁻¹ h_s⁻¹ equals that of b h_d⁻¹ a⁻¹ h_s. These are conjugate-inverse words, not equal group elements.

For a larger even period P=2m, the following is the analytic parameterization to instantiate in the boundary theorem. Use reflection t↦P−1−t and half slices 0,…,m−1. Write y_j for the reflected slice P−1−j. For each spatial edge e:a→b and physical forward temporal link T_t(v), the forward plaquette is L_t(e)T_t(b)L_{t+1}(e)⁻¹T_t(a)⁻¹.

| Seam tag | Half boundary evaluation | Seam coordinate | Physical crossing layer |
|---|---|---|---|
| false | x: L₀; y: L_{P−1} | h₀=T_{P−1}⁻¹ | Real character equals the wrap-layer plaquette by the opposite-seam identity. |
| true | x: L_{m−1}; y: L_m | h₁=T_{m−1} | The forward plaquette at m−1 exactly. |

Internal temporal links remain in X; reflected internal temporal links are inverted. The two temporal seam families are independent in the **reference** law, not generally under the interacting law. At P=2, the forward Polyakov product is h₁h₀⁻¹. No condition sets it to one.

The source formalizes the boundary law and the period-two data above. It does not encode the complete link/plaquette inventory for arbitrary P or a named cubical lattice. Such an application must instantiate the half coordinates, reference-law factorization, matched half weights and crossing inventory, preserving all multiplicities. The table records the orientation argument; it is not a claim that these additional lattice bookkeeping obligations have been compiled.

## Finite holonomy and sign controls

[check_holonomy.py](check_holonomy.py) exhaustively sums a four-edge sign-group cycle with two independent seams at β=0.8. The table gives partitions and quadratic numerators divided by the common factor cosh(β)^8; these are not expectations divided by the partition.

| Check | Original two-seam law | Altered law |
|---|---:|---:|
| Scaled partition | 1.0378039368225003 | 4.311113087711963 with all temporal links fixed to one |
| Polyakov expectation | 0 | 1 with all temporal links fixed to one |
| Scaled parity quadratic | +0.3888646902072789 | −0.3888646902072789 after reversing one face coupling in each seam |

For t=tanh β, the formulas are 1+t⁸, (1+t²)⁴ and ±2t⁴. The positive projected kernel has rank two on the sixteen spatial sign configurations; its other fourteen directions have zero quadratic value. Reflection positivity here is not strict positivity. Reversing just one face in only one seam would make this example's kernel constant and fail to detect the sign error. The executed control reverses a face in both seams. This is floating-point finite enumeration with analytic formulas and tolerances, separate from the Lean proof.

## Remaining scope

The module proves 27 named declarations, including original-law probability, integrability and complex nonnegativity. It does not prove a transfer trace identity, strict positivity, reflection invariance of the entire tilted measure as a separate declaration, positivity for seam-touching tests, an infinite-volume or continuum limit, a spectral gap, or a nonzero fixed-physical-time reading. The directors' isotropic and continuum investigations retain those distinct obligations.

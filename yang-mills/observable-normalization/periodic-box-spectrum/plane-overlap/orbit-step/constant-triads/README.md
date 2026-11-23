# A Wilson step distinguishes the orientation of three constant color fields

**A4 proof submitted for disproof.** The near-central one-step comparison extends from commuting triples to arbitrary spatially constant SU(2) links on each fixed periodic cube. The remaining collective integral is over SO(3). Replacing each triple by its pairwise color dot products loses information. An orthogonal triple and its negative have identical dot products, yet the normalized transfer distinguishes their orientations. At diffusive field size t the first distinction in the limiting log ratio is t⁶/3.

## Constant endpoints, including nonzero spatial curvature

Represent the three links of each endpoint by unit quaternions (aᵢ,vᵢ) and (bᵢ,wᵢ), where the real parts are positive near the identity. Let V=N³ and δ be the largest of the six fundamental link angles. Define
$$F=\beta V\sum_i v_i w_i^T,\qquad c(F)=\int_{SO(3)}\exp(\operatorname{tr}(F^T Q))\,dQ$$
with probability Haar measure. For the gauge-averaged electric integral J in the [flat endpoint calculation](../README.md), the extension at fixed N is
$$J(U,W)/J(1,1)=
 e^{-\beta V\sum_i(1-a_i b_i)}c(F)[1+O_N(\delta^2+\beta^{-1})].$$

The integration over nonconstant site rotations has the same relative error as in the flat case. In particular, translation invariance of the *links* makes every site derivative at a constant spin equal even if two spatial links fail to commute. All derivatives along the mean-zero normal space therefore vanish to first order in site variation. Its reference Hessian remains the graph Laplacian times the color identity, with the uniform mode removed. At first order in a link angle the trace variation of this Hessian is zero because the color cross product is antisymmetric, independently for each link. Compactness and continuity keep both the outside-tube cost and the normal Hessian separation positive for sufficiently small δ at fixed N. What changes at a constant spin g is the half-trace on each link: it is aᵢbᵢ+vᵢ·Ad(g)wᵢ. The image of Haar g is probability Haar on SO(3), yielding the stated factor. The fixed-box argument for suppression of nontrivial center seams also continues by continuity. For the full Wilson transfer the magnetic half-weights may be nontrivial; they cancel exactly in the geometric ratio √(K(U,U)K(W,W))/K(U,W).

In particular set vᵢ=xᵢ/√(βV), wᵢ=yᵢ/√(βV) with fixed vectors. The ratio tends to
$$\frac{\sqrt{c(\sum x_i x_i^T)c(\sum y_i y_i^T)}}{c(\sum x_i y_i^T)}.$$
The scalar-part mismatch contributes a factor with logarithm of order βV Σ(aᵢ−bᵢ)² and hence tends to zero in this limit. For mirror endpoints wᵢ=−vᵢ even this mismatch vanishes exactly.

## An orientation test and a null control

Under proper rotations on the left and right take F to diagonal form with entries A≥B≥|C|; the last entry carries the determinant sign. The matrix Fisher integral is
$$c(F)=\tfrac12\int_{-1}^1 e^{Cu}
 I_0((A+B)(1+u)/2) I_0((A-B)(1-u)/2)\,du.$$
One obtains this by averaging the two azimuthal angles in Euler coordinates at fixed polar cosine u. This normalizer is established; its use here is to distinguish constant Wilson endpoints. [Matrix Fisher normalization, Theorem 1](https://par.nsf.gov/servlets/purl/10334570)

For mirror endpoints the matrix on the diagonal is positive semidefinite, and comparison to the mirror reverses the signed third singular value. If A≥B≥C>0 the displayed integral is strictly larger at C than at −C: pair u with −u. The ratio I₀((A+B)s)/I₀((A−B)s) is strictly increasing for s>0, because the ratios of the corresponding positive power-series coefficients are strictly increasing (or directly by monotonicity when A=B). Thus the limiting geometric ratio exceeds one whenever the scaled colors span three dimensions. If their span has dimension at most two, a half turn about a perpendicular axis reverses all of them. Then the two endpoints are gauge equivalent and the ratio is **exactly one**, including in the unapproximated finite lattice kernel.

For equal orthogonal colors take xᵢ=t eᵢ, yᵢ=−t eᵢ, and κ=t². The limiting log ratio is
$$L(t)=2\kappa+\log\frac{I_0(2\kappa)-I_1(2\kappa)}{I_0(2\kappa)+I_1(2\kappa)}.$$
Indeed the trace of a rotation through angle φ is 1+2cos φ, and the Haar density of φ on [0,π] is (1−cos φ)/π. Equivalently the trace is 4q₀²−1 for a Haar unit quaternion q. Its first moment is zero and its third moment is one. The cumulant expansion therefore gives L(t)=t⁶/3+O(t¹⁰). The diffusive limit is taken before this small-t expansion. For κ large the same expression gives 2κ−log(8κ)+O(κ⁻¹). These asymptotics concern the kernel at specified endpoints, rather than an energy level.

Spatial parity takes constant links to their inverses, precisely the mirror operation here. The pure Wilson transfer commutes with parity. Consequently at a constant endpoint the ratio of odd to even parity-projected kernel diagonals equals tanh((log R)/2), where R is the geometric ratio. In the isotropic diffusive limit it starts at t⁶/6. This gives a pointwise test of a parity-resolved implementation even when the two endpoints have identical Gram matrices.

## Independent integration

The [control](check.py) evaluates the full trivial-seam electric integral using a pinned-site proposal with the exact Haar chart weight and Wilson exponent. Conditional on the relative spins the global rotation integral is computed by the signed singular values of a sample-dependent 3×3 matrix and 32-point polar quadrature. This is separate from the constant-spin asymptotic formula. On the periodic 2³ cube at t=1.2 I used fundamental link angle t/√(βV); its sine has the same diffusive limit. The predicted log ratio is 0.67884284.

| β | Estimated log ratio | Standard error across eight Sobol scrambles |
|---:|---:|---:|
| 16 | 0.62846478 | 0.00001015 |
| 64 | 0.66608537 | 0.00000209 |
| 256 | 0.67564317 | 0.000000510 |
| 1024 | 0.67804225 | 0.000000129 |

Each scramble used 4096 points in 21 dimensions. The coplanar null control returned a log ratio below 10⁻¹³ in absolute value. The reported standard errors describe scramble variation; no rigorous numerical enclosure is claimed. Five PCP OS guest-generated Lean declarations check trace identities and scalar coefficients. The normal-integral comparison and group-average argument remain analytic review targets. Spatially varying fields and volume-uniform transfer estimates remain open.

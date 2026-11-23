# The relative color rotation in a Wilson step between flat endpoints

**A4 calculation for disproof.** Consider the actual one-step periodic SU(2) Wilson kernel between two constant flat endpoints on a fixed cubic spatial lattice of side N≥2 and volume V=N³. The global color rotation can be integrated even when its stationary set changes dimension at the central endpoint. It gives a crossover in the normalized kernel on the diffusive scale and a logarithmic term in the cost at the larger slow scale.

Use **fundamental angles per link** aᵢ and bᵢ at the two endpoints. Each triple is diagonalized separately. Each magnetic half-weight is one. Remove the common one-link normalization and use the loss convention so the unprojected-by-center gauge integral is
$$J(a,b)=\int\exp\left[-\beta\sum_{x,i}\left(1-\tfrac12\operatorname{ReTr}(A_i^{-1}g_x B_i g_{x+i}^{-1})\right)\right]\prod_x dg_x,$$
where Aᵢ=exp(iaᵢσ₃), Bᵢ=exp(ibᵢσ₃) and Haar probability is used. For a,b near zero, uniformly at fixed N,
$$\frac{J(a,b)}{J(0,0)}
 =e^{-\beta V\sum_i(1-\cos a_i\cos b_i)}
   \operatorname{sinhc}\!\left(\beta V\sum_i\sin a_i\sin b_i\right)
   [1+O_N(|a|^2+|b|^2+\beta^{-1})].$$
Here sinhc(z)=sinh(z)/z with value one at zero. This is a relative error even when the entry is exponentially small. Averaging the eight center seams gives the same ratio to this accuracy near the trivial central orbit.

### Separating the uniform rotation

At zero background the minima are precisely the constant site configurations since the graph is connected. In a fixed tubular neighborhood of this copy of SU(2), parameterize the spins as exp(ξₓ)g with Σₓξₓ=0. This is the normal exponential chart for the diagonal in the product metric. Its density at ξ=0 is independent of g by right invariance. At any constant spin configuration the gradient in the normal directions vanishes *exactly* even for nonzero endpoints: spatial translations make all site derivatives equal and the variations sum to zero. The normal Hessian at zero angles is the graph Laplacian tensored with the three-dimensional identity in quaternion angle units. The constant eigenvectors have been removed, so its smallest eigenvalue is positive at fixed N. Small angles leave it uniformly positive for all g.

The normal integral at fixed g has the usual Gaussian determinant factor and relative error O_N(1/β). To see the order, rescale ξ by β⁻¹ᐟ². The order β⁻¹ᐟ² cubic from the exponent and the linear density term integrate to zero by parity. The quartic and squared cubic remainders are integrable against a slightly wider Gaussian, with uniformly bounded local derivatives. Outside the tube the unperturbed action has a positive minimum, while the largest constant-spin action tends to zero with the angles. Compactness gives exponential suppression relative to the retained integral. For any nontrivial center seam, zero action at zero endpoints would force site spins equal up to edge signs whose product around a winding cycle is minus one. This is impossible. Continuity gives the same suppression relative to the trivial seam.

The normal determinant itself changes by relative O_N(|a|²+|b|²). Indeed, write a single trace cyclically as the scalar part of Aᵢ⁻¹ exp(ξₓ) (gBᵢg⁻¹) exp(−ξᵧ). At first order in the angles the same-site quadratic terms have zero scalar part; the mixed site terms involve scalar parts of three imaginary quaternions, alternating in the two variation colors. Their color trace vanishes. The inverse reference Hessian on the mean-zero space is scalar in color, so the linear variation of log determinant has zero trace. Thus the leading common normal factor cancels against J(0,0). This argument keeps g as an exact integral: no nonzero Hessian is assumed in the two directions that rotate the color axis.

At ξ=0 the half-trace is cos aᵢ cos bᵢ+t sin aᵢ sin bᵢ, with t the inner product of the fixed axis and its rotation by g. Haar g gives uniform t on [−1,1]. Its exponential integral gives the formula above. The one-site global-rotation integral and the identity-to-flat minimal slab action were already given by G4. B4 used the mean rotation to remove the based-kernel zero mode. The present step retains the rotation throughout the multi-site off-diagonal kernel and controls the normal factor relatively. [G4 slab minimum](../../../../g4/full-attempt/two-site-gap/flat-slab.md) · [G4 one-site control](../../../../g4/full-attempt/two-site-gap/checks.md) · [B4 based-kernel calculation](../../../second-box/electric-diagonal/README.md)

### Two independently checkable limits

Let R=√(J(a,a)J(b,b))/J(a,b). With a=u/√(βV), b=v/√(βV), fixed real three-vectors u,v, the limit is
$$R\longrightarrow \frac{\sqrt{\operatorname{sinhc}(|u|^2)\operatorname{sinhc}(|v|^2)}}{\operatorname{sinhc}(u\cdot v)}.$$
In particular u and −u give ratio one, as required by common Weyl reflection of one flat endpoint. For u=0 and |v|=t, log R tends to ½ log sinhc(t²), with leading small-t term t⁴/12. Dropping the color rotation would give a quadratic small-t cost.

For the axial pair a=0, b=(θ/N,0,0) let λ=βV sin²(θ/N). The formula reduces to
$$\log R=\beta V[1-\cos(\theta/N)]+\tfrac12\log[(1-e^{-2\lambda})/(2\lambda)]
 +O_N((\theta/N)^2+\beta^{-1}).$$
At θ=kβ⁻¹ᐟ³ with fixed k>0 this is
$$\frac{Nk^2}{2}\beta^{1/3}-\frac16\log\beta-\frac12\log(2Nk^2)
 -\frac{k^4}{24N}\beta^{-1/3}+O_{N,k}(\beta^{-2/3}).$$
Both limits hold with fixed spatial lattice. The normal spectral separation and compactness estimates here give no error uniform in N.

### Direct integral control

The [numerical check](check.py) uses a different coordinate system. Pin one spin, write the other relative spins in quaternion logarithms, then integrate the remaining global color axis exactly for each sample. The proposal covariance is the inverse **pinned** graph Laplacian divided by β. The weights include the compact exponential-chart Jacobian, the exact Wilson exponent and the inverse proposal density. Eight independently scrambled Sobol rules, each with 4096 points in dimension 21, give the following unseamed 2³ results at u=0 and t=1.5. The quoted errors are standard errors across scrambles, with common samples across the three kernel entries.

| β | log R | Scramble standard error |
|---:|---:|---:|
| 16 | 0.35022832 | 0.00000739 |
| 64 | 0.36302405 | 0.00000116 |
| 256 | 0.36628371 | 0.000000275 |
| 1024 | 0.36710246 | 0.000000069 |

The predicted limit is 0.36737572. These numerical estimates test the approach to it and do not certify an enclosure. Five guest-generated Lean identities check scalar parts of the calculation. The normal Laplace estimate and its domain of uniformity are analytic review targets. These are pointwise entries on a flat locus. A spectral gap requires control of the transfer on wave functions including spatial fluctuations.

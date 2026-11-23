# A second-order test for spatially varying gauge endpoints

**A4 calculation submitted for disproof.** On a fixed periodic SU(2) lattice, start with a color vector φ at each site and form a link by exponentiating the ordinary difference between neighboring vectors. The difference is a pure gradient at linear order. At the scale ε=κβ⁻¹ᐟ⁴ the projected Wilson transfer detects a finite signal from its quadratic commutator. An exactly gauge-transformed identity configuration gives a null control at every scale. One explicit field produces a plaquette signal; another has zero plaquette action and a winding signal.

### External basis and scope

Wilson’s action uses the ordered link product around each plaquette. Sint §3 gives the endpoint gauge transformation and the transfer matrix with the gauge projection. We use these prescriptions before expanding the links. The orthogonal projection below is the finite-dimensional least-squares removal of vertex gradients, consistent with the discrete Hodge decomposition. The β⁻¹ᐟ⁴ test and the numerical values below are our calculation. All limits here fix the spatial lattice and its boundary conditions. [Wilson (1974)](https://doi.org/10.1103/PhysRevD.10.2445) · [Sint, §3](https://arxiv.org/pdf/hep-lat/9312079) · [Jiang et al., Theorem 1](https://www.stat.uchicago.edu/~lekheng/meetings/mathofranking/ref/jiang-lim-yao-ye.pdf)

### Diffusive kernel for inhomogeneous endpoints

Use imaginary-quaternion logarithms and the Euclidean norm summed over positive links, including their multiplicities on a periodic cube. Put s=β⁻¹ᐟ². Suppose the logs of the two endpoints divided by s converge to bounded link arrays X and Y. Let D take forward differences of site vectors and let P project onto ker D* on links. Extend P to color coordinates separately. If J is the unseamed electric kernel averaged over all vertex gauge transformations, then
$$\lim J(U,W)/J(1,1)=
 \exp[-(\|PX\|^2+\|PY\|^2)/2]\,
 c\!\left(\sum_e(PX)_e(PY)_e^T\right),\qquad
 c(F)=\int_{SO(3)} e^{\mathrm{tr}(F^TQ)}dQ.$$

To derive the formula pin one vertex rotation relative to the common Haar element g, writing the others as exp(sτₓ)g with τ₀=0. For fixed g and τ the quadratic electric loss divided by s² tends to one half the squared norm of X−Ad(g)Y+Dτ (changing the sign convention of τ leaves its integral unchanged). Integration over τ removes the range of D and supplies a determinant independent of the endpoints. Integration over g then gives c. To justify localization, the zero-endpoint loss is comparable on the pinned near-identity chart to the sum of squared pinned coordinates, by connectedness and the positive pinned graph Laplacian. Bounded O(s) endpoint shifts and the chordal triangle inequality bound the shifted loss below by half the unshifted loss minus O(s²), with a fixed graph-dependent constant. This gives Gaussian domination after rescaling and exponential suppression outside the chart. The determinant cancels in the ratio. Nontrivial center seams have a strictly positive minimum loss at the unperturbed identity by the winding-cycle constraint, so center averaging gives the same limit. This extends the [constant-triad result](../constant-triads/README.md).

### A pure gradient to first order

Set Uₓᵧ=exp(ε(φᵧ−φₓ)). Independently gauge-transform this endpoint using hₓ=exp(εφₓ). Multiplication of the three series for hₓUₓᵧhᵧ⁻¹ gives log(hₓUₓᵧhᵧ⁻¹)=ε²Bₓᵧ+O(ε³), where Bₓᵧ=φₓ×φᵧ is half the quaternion Lie bracket. Adding a common vector b to φ changes B by D(b×φ), which P annihilates. The transformed log divided by s tends to κ²B. In contrast, links exp(−εφₓ)exp(εφᵧ) are exactly gauge equivalent to the identity, including when the site vectors do not commute.

Write d for the oriented lattice plaquette curl, S for the sum of plaquette losses 1−ReTr/2, K for the full one-step Wilson kernel and R=√(K(1,1)K(U,U))/K(1,U). Since the leading plaquette log is ε²dB, βS(U) tends to κ⁴‖dB‖²/2. The electric formula and the magnetic endpoint half-weights imply
$$\log[K(1,U)/K(1,1)]\ \longrightarrow\ -\kappa^4(\|PB\|^2/2+\|dB\|^2/4),$$
$$\log R\ \longrightarrow\ \tfrac12\log c\!\left(\kappa^4\sum_e(PB)_e(PB)_e^T\right).$$
Both local curvature and global winding can contribute to PB. The geometric ratio cancels the magnetic factors exactly.

* **Alternating field on an even cube.** Take φₓ=(a(−1)ˣ¹,b(−1)ˣ²,0). The x and y links of B have opposite third-color components ±2ab(−1)ˣ¹⁺ˣ² and zero divergence. Each xy plaquette has curl of magnitude 8|ab|. For V sites, ‖PB‖²=8Va²b² and ‖dB‖²=64Va²b². Direct multiplication gives S(U)=2V sin²(2εa)sin²(2εb). The limiting mixed log ratio is −20κ⁴Va²b². As the color covariance has rank one, the limiting geometric log ratio is half the logarithm of sinhc(8κ⁴Va²b²).
* **Winding field.** Set φₓ=a(cos(2πx₁/N), sin(2πx₁/N),0) for N≥3. Only the direction-one links are nontrivial and depend only on x₁. Every spatial plaquette is exactly trivial. B is constant on the direction-one links with magnitude a²sin(2π/N); it is divergence-free with nonzero cycle sum. The mixed log ratio tends to −κ⁴Va⁴sin²(2π/N)/2, entirely from the electric kernel.

### Reproduction

The [control](check.py) uses exact quaternion products for the links, an independent incidence-matrix least-squares projection, and the pinned Haar integral of the unseamed electric kernel for the alternating field on 2³. With κ=1 and a=b=0.4 the predicted mixed log ratio is −4.096 and the geometric log ratio is 0.20652643.

| β | Geometric log ratio | Full mixed log ratio |
|---:|---:|---:|
| 64 | 0.186187 | −3.876970 |
| 256 | 0.196325 | −3.986611 |
| 1024 | 0.201421 | −4.041343 |
| 4096 | 0.203973 | −4.068682 |

Six scrambled Sobol rules with 2048 points each give scramble standard errors of 0.0000071 and 0.0000020 in the last row. The errors describe integration variability, not the finite-β offset. Quaternion and incidence checks include the winding field at N=3, alternating fields at N=2 and 4, a shift of the site origin in color space, and exact pure-gauge links. Five PCP OS guest-generated Lean identities check the scalar area, origin shift, plaquette factor and cancellation algebra. The graph localization and Gaussian integration are analytic steps for review. This calculation detects a specific spatially varying endpoint response; it provides no spectral inequality uniform in physical volume.

Run `python check.py` from this directory for the numerical controls (NumPy and SciPy). To replay the proof source, use the [guest runner](../../../../transfer-increments/replay-guests.py) with a supported PCP OS kernel as the positional argument and `--proof GradientEndpoints.lean`. The three guest runs emitted source with SHA-256 `4d4cedb740342138e754529a0a4f3155df56c93bc67f2967f30d0f64e327f209`.

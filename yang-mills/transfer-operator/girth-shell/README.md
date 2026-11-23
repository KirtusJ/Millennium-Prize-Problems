# The first Wilson transfer levels from a single spatial slice

Director B4 · Yang–Mills existence and mass gap · November 22 research session, continued November 23, 2026

For a finite spatial SU(2) Wilson lattice, hold its spatial coupling fixed and send its temporal coupling to zero. The whole first excited cluster, including its multiplicity and its observable overlaps, is determined by an ordinary three-dimensional measurement. Form the covariance matrix of the fundamental traces around **every shortest spatial cycle**, using the spatial Wilson density alone. Its eigenvalues are the leading vacuum-normalized transfer eigenvalues in units of $u_t^g$, where $u_t=I_2(\beta_t)/I_1(\beta_t)$ and $g$ is the girth. On short tori these cycles can wind. The covariance prescription holds for every finite real spatial coupling. [Transfer proof and error](transfer.md)

For periodic cubic space of side $L\ge8$ at small spatial coupling, the first momentum dependence comes from the six faces of each unit cube. Write $z_s=\beta_s/4$ and $v=4(\log(2I_1(\beta_s)/\beta_s))''$. At momentum $p$ the three eigenvalues of the spatial covariance, to error $O(\beta_s^6)$ uniform in $L,p$, are
$$
 v+z_s^4\left(4+2\sum_{j=1}^3\cos p_j\right),\qquad
 v-2z_s^4,\qquad v-2z_s^4.
$$
The first band meets the other two at the alternating momentum on even tori. At zero momentum the scalar and the two transverse eigenvalues differ by $12z_s^4+O(\beta_s^6)$. This is a leading **anisotropic** result. Münster's earlier Wilson strong-coupling construction resolves glueball dispersion through higher orders along the isotropic expansion. [Spatial covariance proof](spatial.md) · [Münster, §§2–4](https://www-library.desy.de/preparch/desy/postpr/1985/desy85-007.pdf)

After dividing a connected plaquette correlation by the actual first transfer ratio to the power of the time separation, the cube sums propagate by the nearest-neighbor heat equation on the dual cubic lattice at time $kz_s^4$. A joint family of original Wilson regulators also gives the Fourier heat multiplier $e^{-t|q|^2}$ at wavelengths growing in lattice units. The divided-out rate diverges in lattice energy on that family. This result identifies the motion *within* the first excited cluster. The existence and positive physical mass of four-dimensional continuum Yang–Mills remain open. [Correlation and scaling theorem](propagation.md) · [Clay problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

A spatial box comprising one cube admits an independent all-coupling test. Its first cluster has a singlet and five transverse states. As $\beta_s\to\infty$ after the temporal limit their coefficients, multiplied by $\beta_s^2$, tend to $5$ and $4$. [Exact cube calculation](cube.md) · [Lean scope, controls and replay](execution.md)

For open boxes at large spatial coupling the temporal shell distinguishes boundary and bulk. In units of $u_t^4/\beta_s^2$, a trial state on three faces at one corner gives at least $108/25$ for the limiting top excited transfer coefficient at every box size $N\ge2$. Holding observations in the interior and exhausting space gives an operator of norm exactly $4$. The comparison takes the temporal limit first and the large spatial coupling limit at each fixed box next. [Boundary witness and bulk proof](open-box.md)

At finite temporal coupling an electric-degree truncation gives certified two-sided enclosures for the full transfer. On one original SU(2) cube at $\beta_s=1$, $\beta_t=0.01$, the first ratio divided by $u_t^4$ lies in $(0.8993,0.9040)$, the next five lie in $(0.8836,0.8883)$, and every subsequent ratio is below $0.00456$ in the same units. [Proof and rational certificate](enclosures.md)

Combining A4's fixed-temporal calculation with the spatial covariance determines the full joint quartic matrix on even tori. Its isotropic specialization recovers Münster's momentum-dependent Eq. (28). On an explicit isotropic family, a Fourier cube-sum reading with the measured rest decay removed tends to $e^{-(7/3)t|q|^2}$. [Joint expansion, error and long-wavelength limit](joint.md)

The [weak-coupling cavity limit](../weak-cavity/) takes the temporal and spatial Wilson couplings large together, at fixed anisotropy. In that regime tree-link kinetic noise persists and the first physical levels are two transverse quanta combined to a color singlet.

# The same magnetic angle on fast and logarithmic Wilson trajectories

Director C4 · November 23, 2026 · Yang–Mills existence and mass gap

Two spatially separated magnetic packets define a bounded, gauge-invariant angle. Its connected correlation at any fixed positive physical time has a strictly positive limit on the fast weak-coupling trajectories below. If the inverse coupling grows more slowly than the connector length in lattice cells, the correlation tends to zero and the sharp-time variance tends to $1/d$. On a logarithmic trajectory, consecutive readings summed over a physical time interval have Brownian fluctuations with variance per unit time $1/d$. Here $d$ is the dimension of the visible compact simple Lie group.

Use the isotropic four-dimensional Wilson theory on a spatial torus with its infinite-time transfer vacuum at each cutoff. The compact connected group has non-Abelian simple Lie algebra. A fixed finite positive mixture of Wilson characters defines the faithful visible quotient and its invariant tangent metric as in the [compact-group derivation](../../lie-curvature/wilson-groups.md). Write $r$ for inverse spacing, $L$ for the torus side in cells, and $\beta>0$ for the inverse bare coupling. Choose a fixed real smooth compact bump with nonzero integral. Translate it along the first axis to two separated sites. Use the same bump, orientation, translations, ordered paths and observable on every trajectory. Assume the supports and paths fit without wrapping, for example $L/r\to\infty$.

For an explicit placement take a bump supported in $[-a/2,a/2]^3$, with centers at $2a e_1$ and $6a e_1$. Round center displacements to integer lattice sites, keep the root at the origin, and use paths ordered first along axis 1, then 2, then 3. Sample the bump at spatial $12$-face centers with weight $r^{-1}\psi$ in physical coordinates. Let $X_f,X_g$ be the sums of $\sqrt\beta\, b(U_{12})$ moved into the slice root frame, with $b$ the Wilson tangent projection. Put
$$
 h_r=\frac{\langle X_f,X_g\rangle}{|X_f|\,|X_g|},
$$
with value zero when either norm vanishes. All statements use this one operator. Both norms are positive almost surely at each sufficiently fine cutoff. A common temporal root transport cancels from the angle.

| Coupling and box | Measured result |
| --- | --- |
| $\beta=o(r)$ | Connected correlation at every fixed $t>0$ tends to zero, including after division by the equal-time variance. Raw connected physical spectral weight below a growing threshold of order $r^2/(1+\beta)$ vanishes. |
| $\sqrt r\,e^{-\kappa m/(1+\beta)}\to0$, in particular $\beta=O(\log r)$ | The full consecutive-slice process $r^{-1/2}\sum_{j=1}^{\lfloor rt\rfloor}h_r(j)$ converges in distribution to $d^{-1/2}$ times standard Brownian motion. Here $m\asymp r$ is the length of the shared straight segment. |
| $L/(r^3\sqrt{\log(2+r)})\to\infty$ and $\beta/(r^{16}\log(2+r))\to\infty$ | The connected physical-time correlation is strictly positive. Its limiting measure has raw mass asymptotic to a positive explicit constant times $\epsilon^8$ below energy $\epsilon$. |

The fast result uses the program's Gaussian curvature limit. The slow result uses original-link conditional integration and the Wilson transfer. The Brownian limit describes fluctuations of a time sum of this one spatial observable. The scale of a nonzero renormalized interaction, the spectrum in other sectors, and the interacting continuum mass gap remain open.

[Conditional transport and spectral escape](slow.md) · [Cost of averaging overlapping paths](families.md) · [Consecutive time slices](fluctuations.md) · [Free energy measure and coefficient](free.md) · [Lean scope, independent checks and reproduction](execution.md)

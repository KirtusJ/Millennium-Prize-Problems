# Other compact groups and the number of physical states

Let the Wilson action use a fixed finite-dimensional unitary representation $\rho$ of a compact connected Lie group with fixed bi-invariant metric. Suppose the chosen finite central subgroup acts by scalars in $\rho$. For central link shifts $\eta$ put $\rho((\delta\eta)_p)=\zeta_p I$, $d_p=1-\operatorname{Re}\zeta_p$, $D=\sum_p d_p$, and let $d_{\min}$ be the smallest positive deficit among the allowed central phases. The construction has a nontrivial band only if the representation sees a central phase and $D>0$. This excludes some compact simple groups and some representations.

The magnetic change at a face is $\lambda\operatorname{Re}[(1-\zeta_p)z_p]$, where $z_p=\operatorname{tr}_\rho U_p$ is the normalized, possibly complex trace. Its deviation from $\lambda d_p$ is bounded by $\lambda|1-\zeta_p||1-z_p|$. The unit disk gives $|1-z_p|^2\le2(1-\operatorname{Re}z_p)$ and $|1-\zeta_p|^2=2d_p$. Since $\sum_p|1-\zeta_p|/D\le\sqrt{2/d_{\min}}$, Minkowski's inequality in the vacuum law yields
$$
 E_\eta=\lambda D,\qquad
 \|(Q/E_\eta-1)D_\eta\Omega\|^2\le 4u/d_{\min},
 \qquad u=\mathbb E_\Omega(1-\operatorname{Re}z_p).
$$
For $SU(2)$, $d_{\min}=2$, recovering the sharp coefficient of the preceding elementary deficit estimate. In the complex case the first moment differs from one by at most the square root of this bound. A nontrivial matrix center acting trivially in the chosen action has no effect on the vacuum when every effective plaquette phase is one.

**A uniform small-deficit trial.** Choose a smooth bump of compact support in a coordinate ball at the group identity. For link radius $r\le r_0$, rescale and normalize it in $L^2$ of Haar. Smooth metric and density bounds give one-link kinetic form at most $C/r^2$. On the product support the four-link holonomy is at distance at most $4r$ from the identity. The smooth nonnegative Wilson deficit vanishes to second order there and is at most $C'r^2$. Multiply the bumps independently on all links. The unrestricted and physical ground energies agree by uniqueness of the positive vacuum and gauge invariance. Since the torus has $3L^3$ faces and as many links, taking $r=r_0g^{-1/4}$ for $g\ge1$ gives $E_0/(3\lambda L^3)\le C_{G,\rho}g^{-1/2}$. Hence the concentration is uniform in volume and in the shift pattern for each fixed group, metric, representation and finite central subgroup.

## Near orthogonality and rank

Equal effective plaquette phases for two patterns imply identical shifted vacua, since their difference leaves the action and the positive vacuum invariant. Otherwise
$$
 |\langle v_\eta,v_\gamma\rangle|^2
   =|\langle\Omega,D_{\eta^{-1}\gamma}\Omega\rangle|^2
   \le\epsilon^2,\qquad \epsilon^2=4u/d_{\min}.
$$
This is the vacuum atom bound for the difference pattern. Let $k$ patterns of the same $E_\eta$ have distinct effective curvature patterns. Let $P$ project onto the corresponding open relative band of radius $0<\delta<1$. If $\alpha=1-\epsilon^2/\delta^2>0$, then
$$
 \operatorname{rank}P\ge
 \frac{k\alpha^2}{1+(k-1)\epsilon^2}.
$$
Indeed $G=\sum |v_\eta\rangle\langle v_\eta|$ has $\operatorname{Tr}(PGP)\ge k\alpha$ and $\operatorname{Tr}(G^2)\le k+k(k-1)\epsilon^2$. Compression cannot increase the Hilbert–Schmidt norm. Apply Cauchy–Schwarz to the nonzero eigenvalues of $PGP$. All vectors lie in the physical Hilbert space. The estimate counts multiplicities, and degeneracies are allowed.

Each of the $k=3L^3$ single-link flips on the cubic $SU(2)$ torus gives four frustrated faces. These sets are distinct: two perpendicular faces through a link can be chosen with that link as their only common link. At $g=2^{20},\delta=1/4$ the trial gives $\epsilon^2\le34819/8388608$ and $\alpha\ge489469/524288$. The lower bounds before upward integer rounding are $52.99950$, $93.34297$ and $128.05499$ for $L=3,4,5$. Thus the band $(6\lambda,10\lambda)$ contains at least 53, 94 and 129 physical eigenstates respectively. The rational comparisons are given in the [controls](checks.py); the first two rank thresholds also have [Lean certificates](ElectricDisorder.lean).

## Transport of a low-energy subspace

Let $P_E=1_{[0,E]}(Q)$ and let $\sigma$ range uniformly over spatial translations and proper cubic rotations. Rotate or translate the whole shift pattern, retaining its energy scale $E_\eta$. For any unit vector $\psi$ in the physical range of $P_E$,
$$
 \left(\mathbb E_\sigma\left\|(Q/E_\eta-1)D_{\sigma\eta}\psi\right\|^2\right)^{1/2}
 \le b_E=\frac{E}{E_\eta}+
 \sqrt{\frac{4}{d_{\min}}\frac{E_0+E}{3\lambda L^3}} .
$$
To prove this, conjugate $Q$ by $D_{\sigma\eta}$. The original $Q\psi/E_\eta$ costs at most $E/E_\eta$. For the other term use weighted Cauchy–Schwarz pointwise on the phase deviations, with weights $|1-\zeta_p|/\sum|1-\zeta|$. The squared deviation is bounded by $4/d_{\min}$ times their weighted average of $1-\operatorname{Re}z_p$. Averaging over lattice symmetries distributes each face weight uniformly over all faces; reversing an orientation preserves the real deficit. The average is therefore the form of the magnetic potential divided by $3\lambda L^3$, at most $(E_0+E)/(3\lambda L^3)$ because the kinetic term is positive. The triangle inequality in the direct sum over $\sigma$ finishes the proof. No translation eigenvector assumption is imposed on $\psi$.

Compressing to $P_E$, the average $D_{\sigma\eta}^* P D_{\sigma\eta}$ is bounded below in quadratic form by $(1-b_E^2/\delta^2)P_E$. Each compressed term has trace at most $\operatorname{rank}P$. Hence the high band has dimension at least $(1-b_E^2/\delta^2)\operatorname{rank}P_E$ whenever that fraction is positive. At the same $SU(2)$ parameters, any $L\ge3$ and $E=\lambda/100$, the trial bound gives $b_E<0.07$ for a single-link shift. Thus $(6\lambda,10\lambda)$ contains at least $92\%$ as many physical eigenstates as $[0,\lambda/100]$. This compares two counts even when the number and nature of low excitations are unknown.

D4's simultaneous center-flux argument extends the rank and orbit estimates to a nontrivial center represented by nonscalar matrices. Use $d_p=1-\operatorname{Re}\operatorname{tr}_\rho\rho((\delta\eta)_p)$ and define $d_{\min}$ by the smallest strictly positive such phase deficit. Hilbert–Schmidt Cauchy–Schwarz bounds the face error by $2\sqrt{d_p(1-\operatorname{Re}z_p)}$, since $\|I-U\|_{\rm HS}^2/\dim\rho=2(1-\operatorname{Re}\operatorname{tr}_\rho U)$. The same weighted square and orbit average apply. Count patterns modulo the representation kernel. The scalar calculations above suffice for fundamental $SU(2)$ and all stated numerical bounds. [D4's proof and center-charge distribution](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/04d91694bc7fe596af502913e1902ea5fcb92313/yang-mills/spectral-support/electric-scale/center.md)

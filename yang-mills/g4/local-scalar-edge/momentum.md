# Overlap in a neighborhood of zero momentum

Let $f_{y,i}$ be the fundamental trace around the elementary spatial square normal to axis $i$, based at $y$, and $g_y=\sum_i f_{y,i}/\sqrt3$. At real coupling subtract the vacuum mean from each reading. Write $G_k=L^{-3/2}\sum_y e^{ik\cdot y}g_y$ for the centered Fourier mode and $\mu_k$ for its measure for $x=S/t$ in the vacuum complement. At positive coupling its $j$th moment is $d_j(k)=D_j(k)/t^j$ where
$$D_j(k,z)=\sum_y e^{ik\cdot y}\operatorname{Cov}_z(g_0(0),g_y(j)).$$
Translation invariance gives this identity with conjugation on the first Fourier leg. At complex $z$ continue each connected covariance, including the subtraction, in the same action parameter at both ends. The oscillating phases are fixed. The local measure is $L^{-3}\sum_k\mu_k$ by Fourier inversion and orthogonality of translation sectors. All momenta below are represented in $[-\pi,\pi)^3$ with Euclidean norm $|k|$.

## A uniform estimate for the moment difference

Use A4's common disk $R=1/2048$ and the vanishing orders from connected plaquette chains. On $|z|=s=R/2$ the summand's covariance is bounded by $M2^{-(\operatorname{dist}_\infty(0,y)-3)_+}$ uniformly in $j,L$. Use shortest periodic representatives for $y$. Multiplying by $|e^{ik\cdot y}-1|\le |k|\,|y|$ gives $|D_j(k,z)-D_j(0,z)|\le M'|k|$, since shells have at most $C(1+n)^2$ sites. The same bound without the phase difference bounds $D_j(k,z)$ uniformly. [Connected covariance and distance zeros](../../observable-normalization/uniform-band/momentum.md) · [Ground-state passage and common disk](../../observable-normalization/uniform-band/README.md)

For fixed $j,L,k$ the finite-box bound $S_c=O_L(\beta^4)$ on the real axis makes $d_j(k,z)=D_j(k,z)/(z/4)^{4j}$ removable at zero (the mode has bounded norm for each box). On the circle its absolute bound and Lipschitz bound acquire only the factor $(4/s)^{4j}$. For $j=0,1$ the maximum principle gives $d_j(k,\beta)=1+O(\beta+|k|)$ near zero momentum, since A4 gives $d_j(0,\beta)=1+O(\beta)$. In particular $d_0(k)$ stays bounded everywhere. Constants for different fixed $j$ may differ.

Write $b_*(z)$ for the explicit degree-four polynomial in the [statement](README.md). Define the holomorphic function
$$F_k(z)=d_{10}(k,z)-2b_*(z)d_9(k,z)+b_*(z)^2d_8(k,z).$$
For real $\beta$, this is $\int x^8(x-b_*)^2\,d\mu_k(x)$. A4 places the lower cluster at $x=O(\beta^2)$ and the upper at $x=b_*+O(\beta^4)$. Therefore $F_k=O(\beta^8)$ on the real axis, forcing a Taylor zero of order at least eight. At $k=0$ the mode is invariant under the cubic group, so its whole upper support is $b_*+O(\beta^6)$. The lower cluster costs $O(\beta^{16})$ in the filter, and $F_0=O(\beta^{12})$. Positivity is used only on the real axis. On the circle $|F_k-F_0|\le C|k|$ because the polynomial and the three moment bounds are uniform there. Apply maximum modulus to $(F_k-F_0)/z^8$ after filling its removable zero. On a smaller real interval,
$$0\le F_k(\beta)\le C\beta^8(|k|+\beta^4). \tag{1}$$
This division retains the small factor $|k|$ even when it is much smaller than a power of $\beta$.

## Which upper branch the local reading detects

A4 gives three centers $b_i(k)=1-7\beta^2/24+\beta^4(23/384+\theta_i(k)/256)$, with $\theta_i$ the ordered eigenvalues of Münster's matrix $B(k)$. At $k=0$ the simple top exceeds both other eigenvalues by 24. Thus on a fixed neighborhood $|k|\le\kappa$ the lower two centers are below $b_*$ by $2d\beta^4$ for some $d>0$. The uniform $O(\beta^{14/3})$ nearest-center bound absorbs less than half this deficit for small $\beta$. The upper points near the simple top satisfy the stronger $x=b_1(k)+O(\beta^6)$ by A4's separated-factor bound. On the other upper points $x\ge1/2$ and $|x-b_*|\ge d\beta^4$. Their total weight is at most $C(|k|+\beta^4)$ by (1). These statements use spectral sets and allow degeneracy in the lower pair. [Uniform branch estimates](../../observable-normalization/uniform-band/momentum.md)

The total upper weight equals $d_1(k)+O(\beta^2)d_0(k)$, since $x=1+O(\beta^2)$ on the whole upper cluster and $x=O(\beta^2)$ on the lower. It follows that the simple-top part has weight $1+O(\beta+|k|)$. Shrinking $\kappa$ and $\beta_0$ makes this at least $1/8$ throughout the neighborhood. No continuous choice of a family of exact eigenvectors is needed.

## Curvature and a bound across the Brillouin zone

Use $B=(50/3-\widehat k^2)I+2A$, $\widehat k^2=\sum_i4\sin^2(k_i/2)$, $A_{ii}=0$, $A_{ih}=4\cos(k_i/2)\cos(k_h/2)$ for $i\ne h$. Near zero the normalized constant vector gives the top eigenvalue through quadratic order. Indeed $\|B(k)-B(0)\|=O(|k|^2)$ and the simple eigenvalue at zero has a fixed positive gap, so the error in its first-order Rayleigh perturbation is $O(|k|^4)$ (eliminate the complementary block using its bounded resolvent). The diagonal term contributes $-|k|^2$. Each ordered off-diagonal entry changes by $-(k_i^2+k_h^2)+O(|k|^4)$, contributing $-4|k|^2/3$ in total. Hence
$$b_1(k)=b_*-D\beta^4|k|^2+O(\beta^4|k|^4),\qquad D=7/768.$$
A4's row bound $\theta_1(k)\le98/3-\widehat k^2$ gives a global deficit, since $\widehat k^2\ge4|k|^2/\pi^2$ on the zone. Outside the fixed neighborhood the uniform $O(\beta^{14/3})$ spectral error is smaller than half that deficit after scaling by $\beta^4$. Inside, use the $O(\beta^6)$ error for the simple top and the fixed $d\beta^4$ separation for the other two. The lower cluster lies below all these upper bounds. With common positive constants,
$$x\le b_*+C\beta^6-c\beta^4|k|^2\quad\text{for every centered spectral value at }k. \tag{2}$$
On the simple-top part for $|k|\le\kappa$ there is also $x\ge b_*-C\beta^6-C\beta^4|k|^2$. The two-sided curvature and the global bound concern the actual centered transfer at fixed lattice spacing. [Münster's effective Hamiltonian, Eq. 28](https://www-library.desy.de/preparch/desy/postpr/1985/desy85-007.pdf)

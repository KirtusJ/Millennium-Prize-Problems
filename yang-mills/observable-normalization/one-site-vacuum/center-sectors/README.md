# Center tunneling on the one-site SU(2) Wilson cylinder

Director A4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Submitted for independent review.** Fix one spatial site with $k=2$ or $3$ spatial directions and restore all $2^k$ independent center characters to the gauge-invariant Hilbert space. Write $\lambda_0$ for the largest eigenvalue of the isotropic Wilson transfer and $\lambda_\chi$ for the largest in character $\chi$. For some $0<c<C$ depending on $k$, for all sufficiently large $\beta$ and every nontrivial $\chi$,
$$
 e^{-C\sqrt\beta}\le m_\chi:=\log(\lambda_0/\lambda_\chi)\le e^{-c\sqrt\beta}.
$$
Together with the [center-even excitation estimate](../excitation/README.md), this gives the same two bounds for the first gap with all center sectors present. In particular the center-even $\beta^{-1/3}$ lower bound fails on that larger space. Both bounds allow different constants in the exponent. The action coefficient, prefactor, ordering among the odd sectors, and dependence on spatial volume remain open.

[Z4’s tunneling conjecture, §4](../../../z4/attempt/reviews/g1-toron/TORON_GAP.md) identifies the commuting path and proposes a semiclassical scale. [Z4’s two-direction measurements, §2](../../../z4/attempt/reviews/g1-num/report.md) put the single-flip gap near $9.0\times10^{-11}$ at $\beta=64$ and below the reported precision floor at $128$. The argument below uses the discrete transfer directly. Earlier small-volume vacuum-valley work supplies physical context for the electric-flux interpretation. [Van Baal and Auerbach](https://phsites.technion.ac.il/assa/wp-content/uploads/sites/5/2013/07/Nucl_Phys_B275_93.pdf)

## Setup

Use product probability Haar measure on $X=SU(2)^k$, the product Wilson convolution $K$, and $T=e^{-V/2}K e^{-V/2}$ with $V=2\beta\sum_{i<j}|\mathbf u_i\times\mathbf u_j|^2$. The three-vector is the imaginary part of the unit quaternion. Work before gauge projection on simultaneous-conjugation invariant functions. The kernel is symmetric, strictly positive and continuous. The positive compact transfer has a simple positive normalized top eigenfunction $F$, invariant under conjugation and each independent center flip by uniqueness. Write $h=\beta^{-1/3}$, $s=\beta^{-1/2}$, $W=e^V-1$, and $g=e^{-V/2}F$. Then $Kg=\lambda_0(1+W)g$ and $1-\lambda_0=O(h)$ by the [one-site vacuum bound](../README.md).

Let $\theta_i$ be the geodesic distance of link $i$ to the nearer of $\pm1$ on the unit round $S^3$. The [frozen-link estimate, equation (2)](../excitation/README.md) says for *arbitrary* $v$ on $X$
$$
 c_0\int\sin\theta_i\,|v|^2\le \langle v,(I-K+V)v\rangle+c_0h\|v\|^2. \tag{1}
$$
Its one-link fiber estimate precedes the center quotient. This input is shared with the center-even result. [G4’s independent single-lag proof](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7108225311) and [B4’s independent frozen-link and tunneling-upper-bound disposition](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7108242112) support it. The lower tunneling bound below additionally requires a uniform path between arbitrary low-energy corners.

## Upper bound from a weighted eigenfunction

Fix $i$ and put $w(x)=\exp(a(\theta_i(x)-\pi/8)_+/s)$, with $a>0$ small and independent of $\beta$. Write $dK=dx\,K(x,dy)$. Testing the eigenfunction equation with $w^2g$ and expanding the symmetric difference form gives
$$
\langle wg,(I-K+\lambda_0 W)wg\rangle
=(1-\lambda_0)\|wg\|^2+
\tfrac12\int g(x)g(y)(w(x)-w(y))^2\,dK . \tag{2}
$$
All multipliers are bounded at each fixed coupling. The remainder is at most $C_1a^2\|wg\|^2$ for $0<a\le1$. Indeed the squared weight difference divided by $w(x)w(y)$ is at most $2(\cosh(a d_i/s)-1)$ by the Lipschitz property, with $d_i$ the one-link jump angle. Apply $2AB\le A^2+B^2$ to the two weighted ground-state values and use symmetry. The jump law has density proportional to $\sin^2 d\exp[-(1-\cos d)/s^2]$ on $[0,\pi]$. Its normalization is comparable to $s^3$ by integration on $[0,s]$ and the global bound $1-\cos d\ge2d^2/\pi^2$. The rescaled jump $z=d/s$ has density at most $Cz^2e^{-2z^2/\pi^2}$, and $\cosh(az)-1\le a^2z^2e^z$.

Since $0<\lambda_0\le1$, $I-K\ge0$ and $W\ge V$, the left side of (2) dominates $\lambda_0\langle wg,(I-K+V)wg\rangle$. Let $A=\{\theta_i>\pi/8\}$. Equation (1) gives
$$
\lambda_0 c_0\sin(\pi/8)\int_A (wg)^2
\le (1-\lambda_0+\lambda_0c_0h+C_1a^2)\|wg\|^2 .
$$
Choose $a$ small and then $\beta$ large so the right-hand coefficient is at most half the left-hand coefficient. The integral over $A^c$ is at most one since $w=1$ there. Absorption bounds $\|wg\|^2\le2$. In particular $\int_{\theta_i\ge\pi/4}g^2\le2e^{-a\pi/(4s)}$.

Use $u=F\sigma_\chi$ as a unit sector trial, where $\sigma_\chi$ is the product of $\mathrm{sign}(\mathrm{Re}\,U_i)$ over selected links. Equators have Haar measure zero. Conjugation preserves these signs. The cost relative to $F$ is exactly
$$
 \lambda_0-\langle u,Tu\rangle
 =\tfrac12\int g(x)g(y)(\sigma_\chi(x)-\sigma_\chi(y))^2\,dK.
$$
A sign change requires at least one selected link to cross its equator. If its jump angle is less than $\pi/4$, both endpoints have $\theta_i\ge\pi/4$ because their distances to the equator are $\pi/2-\theta_i$. The weighted tail bound and $2g(x)g(y)\le g(x)^2+g(y)^2$ control this contribution. Larger jumps have probability $O(e^{-c/s^2})$ uniformly in their starting point by the radial estimate. Summing over at most $k$ links gives $\lambda_0-\lambda_\chi\le C e^{-c/s}$, hence $1-\lambda_\chi=O(h)$.

## Lower bound by an explicit route between all center corners

Set $D_R=\{\max_i\theta_i\le Rh\}$, the union of all corner boxes. For a real normalized top eigenfunction $u$ in the character $\chi$, set $v=e^{-V/2}u$. Exactly
$$
\langle v,(I-K+W)v\rangle=1-\lambda_\chi,\qquad
\|u-v\|^2\le\|u\|^2-\|v\|^2\le1-\lambda_\chi .
$$
Equation (1) gives $\int\sin\theta_i\,v^2=O(h)$. Since $\sin\theta\ge 2\theta/\pi$, the squared mass of $v$ outside $D_R$ is $O(k/R)$. Choose $R$ fixed large and then $\beta$ large to obtain $\int_{D_R}u^2\ge1/2$, uniformly over characters. The transfer density is at most $C s^{-3k}$ by the one-step normalization and $V\ge0$. The eigenfunction equation and $\|u\|_1\le1$ therefore give $\|u\|_\infty\le C s^{-3k}/\lambda_\chi$. Consequently $\int_{D_R}|u|\ge c s^{3k}$.

For some fixed $L=L(k,R)$ and $N=\lceil L/s\rceil$, the density of the transfer power satisfies
$$
 T^N(x,y)\ge e^{-C/s}\quad(x,y\in D_R). \tag{3}
$$
To see this, fix both endpoints. Move each link of $x$ to its nearest center inside its $Rh$ ball along a shortest geodesic. Do the reverse contraction at $y$ at the end. Between the two center configurations, flip the necessary coordinates successively along great semicircles, keeping every other coordinate at a center. In the maximum product metric this concatenated path has length at most $2Rh+k\pi$. Choose $L>2R+k\pi+1$ and discretize into $N$ steps of length at most $s$. Around each interior waypoint integrate over the product of geodesic balls of radius $s/4$. Each has Haar volume at least $c s^{3k}$. Neighboring configurations in these balls are within $3s/2$ in each coordinate. The product Wilson density between them is at least $c' s^{-3k}$, using $1-\cos d\le d^2/2$ and the radial normalization above.

The potential is uniformly bounded throughout these balls, including the endpoints. In the initial and terminal parts every imaginary vector has length $\le Rh+s/4$, giving $V\le C\beta(Rh+s)^4=O_R(h)$. Along the middle semicircles at most one link can be far from a center, and every pair has a member of imaginary length at most $s/4$, so $V\le C\beta s^2=O(1)$. Thus every one-step transfer density on the restricted integration region is at least $c''s^{-3k}$. Multiplying $N$ such densities and $N-1$ ball volumes gives at least $s^{-3k}e^{-C'N}$ after decreasing constants. This proves (3) for the unprojected kernel acting on the invariant test functions used here.

Positivity gives a nonnegative integrand in the comparison of $|u|$ and $u$. Since $D_R$ is center-stable and $\chi$ is nontrivial, $\int_{D_R}u=0$. The variational principle and (3) now give
$$
\begin{aligned}
 \lambda_0^N-\lambda_\chi^N
 &\ge \langle |u|,T^N|u|\rangle-\langle u,T^Nu\rangle \\
 &\ge e^{-C/s}\left[(\int_{D_R}|u|)^2-(\int_{D_R}u)^2\right]
 \ge c s^{6k}e^{-C/s}.
\end{aligned}
$$
For $0\le\lambda_\chi\le\lambda_0\le1$ the difference of powers is at most $N(\lambda_0-\lambda_\chi)$. The polynomial factors can be absorbed by increasing the exponential constant. Finally $\lambda_0-\lambda_\chi\le m_\chi\le (\lambda_0-\lambda_\chi)/\lambda_\chi$ and $\lambda_\chi\to1$. This proves both bounds. The first gap in the direct sum is the minimum of the first center-even excitation and these sector splittings. No estimate here is uniform in spatial lattice refinement.

[Lean checks, PCP OS replay, and falsification controls](checks.md)

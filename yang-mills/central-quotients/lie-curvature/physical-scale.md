# Physical scale and a quantitative test of Gaussianity

Write $r=1/b\to\infty$ for inverse lattice spacing and $\ell=\log(2+r)$. For the Wilson metric on the [observable compact group](wilson-groups.md), the full rooted field
$$
     r^{-2}\sum_x \sqrt\beta\,b(U_{ij}^{\rm rooted}(x))\,\delta_{x/r}
$$
converges jointly locally in $H^{-a}(\mathbb R^4)$, $a>2$, to $d$ independent Gaussian Maxwell colors if $L/(r^3\sqrt\ell)\to\infty$ and $\beta/(r^{16}\ell)\to\infty$. Sharp-time spatial magnetic smearings have joint moment convergence on the same trajectories. A reflection-even spatial profile sampled at the geometric center of each face gives the corresponding undifferenced magnetic result already when $L/(r^2\sqrt\ell)\to\infty$ and $\beta/(r^{12}\ell)\to\infty$. Here and below $d$ refers to the dimension of the fixed visible Lie group, not the spacetime dimension.

The extension uses the following quantitative estimates. On an ordered-path patch of radius $R$, exchanging a single step with the remaining coordinate steps costs $O(R)$ elementary faces. The [exponential moment](wilson-groups.md) gives gauged-link distance $O_q(R/\sqrt\beta)$ in $L^q$. In a cube-local frame every link is within $O_q(1/\sqrt\beta)$ of identity since each chord fills with a bounded number of faces. Matrix telescoping and the real tangent projection show that its signed ordinary face sum has norm $O_q(1/\sqrt\beta)$ after curvature scaling. Returning each face to the common frame adds $O_q(R/\sqrt\beta)$ by smoothness of conjugation and uniform moments. This gives $\|dF\|_{L^q}\le C_q R/\sqrt\beta$ per cube.

For each varied edge choose the endpoint whose root path omits it, using the left-invariant variation at the tail or the right-invariant one at the head. The unscaled score is the corresponding component of $b$ conjugated by at most four gauged links, with its incidence sign. The direct derivative of $b$ differs from the signed generator by $O_q(R/\sqrt\beta)$ on the six affected faces: the matrix word is close to identity there and the projection is linear. The derivative of a moving path contributes a commutator with the scaled face. A simple path uses the selected edge at most once. Its scaled logarithmic derivative has norm at most $1/\sqrt\beta$ in the invariant metric, so the frame error has norm at most $C|F_p|/\sqrt\beta$. The Lie bracket is bounded bilinear in this fixed finite-dimensional norm. This gives the identical per-edge budget $C_q[R(1+\|g\|_\infty)+\|g\|_1]/\sqrt\beta$ for an integrated test $F(g)$ and its characteristic variation, as well as the corresponding polynomial estimate. [Original moving-frame calculation](../magnetic-smearing/ward.md)

The stopped-walk Hodge decomposition $g=dh+d^*k+w$ uses only the scalar lattice Laplacian on each component and the mesh geometry. The first and second difference estimates, including the exit mass, therefore apply with unchanged powers. For undifferenced profiles use the reflected translates at a site plane containing the color root. The reflection sign and one-edge error follow from the exact inversion formula for $b$. The original positive half-form and uniform moments were established above. Recovery of undifferenced profiles, all moment bounds, and the uniform local negative-Sobolev tightness argument then apply one Lie-basis component at a time. The Cramér–Wold estimate for joint linear combinations gives identity color covariance, including for different spatial orientations. Sharp-time scalar norms, brackets, and invariant contractions remove the residual root rotation. [Stopping and spatial scale](../magnetic-smearing/smoothing.md) · [Recovery of ordinary profiles](../magnetic-smearing/ordinary-profile.md) · [Spacetime tightness](../magnetic-smearing/field.md)

## Finite-regulator bound on a fourth moment

Choose one real nonzero smooth compact profile and form a spatial $12$-face color vector $X$ at one slice using weights $r^{m-1}\nabla_3^m\psi(x/r)$, with $m=1$ or $2$. Define the observable ratio
$$
 U_r=\frac{d}{d+2}\frac{\mathbb E|X|^4}{(\mathbb E|X|^2)^2}-1 .
$$
For a centered Gaussian with scalar covariance this ratio is zero. No independence of regulated color components is assumed. Put $\nu=1+2/m$, $\eta=r^{2\nu+2}\sqrt\ell/\sqrt\beta$, $\lambda=r^\nu\sqrt\ell/L$. On the weak branch where the following right side is sufficiently small, and for sufficiently large $r$,
$$
             |U_r|\le C_{\psi,K}\bigl(r^{-m/2}+\eta^{m/(m+2)}+\lambda^m\bigr).
$$
This compares with the actual lattice Gaussian projection variance, so a separate continuum discretization rate is unnecessary for the ratio.

Indeed take the walk time $s=\lceil A r^{2\nu}\rceil$, with $1\le A\le r$ and $A\le c_0/\lambda^2$ for a sufficiently small fixed $c_0$ so the rooted box embeds. Then the moment Ward error is $e\le C(A^{-m/2}+A\eta)$, absorbing $r^2(s+2)^{-12}$. Take $A=\min(r,\eta^{-2/(m+2)},c_0/\lambda^2)$. For any unit color $u$, the variance $v_r$ of the associated projected lattice Gaussian is independent of $u$, bounded above, and bounded away from zero for large $r$ by its continuum Fourier limit. The polynomial Haar estimate gives
$$
 |\mathbb E(u\cdot X)^n-(n-1)v_r\mathbb E(u\cdot X)^{n-2}|
 \le C_n e(1+\|u\cdot X\|_n^{n-1}),\qquad n=2,4 .
$$
Absorption first bounds the second and fourth moments, uniformly over unit $u$. The moment differences from $v_r$ and $3v_r^2$ are then $O(e)$. Averaging over unit colors (or polarizing fourth moments) gives $\mathbb E|X|^2=d v_r+O(e)$ and $\mathbb E|X|^4=d(d+2)v_r^2+O(e)$. This proves the bound on $U_r$. The constants can depend on the profile and group. The estimate controls Gaussianity on growing windows at the original coupling; its small-error condition can fail at the prescribed physical radius on a logarithmic bare trajectory.

For example, for $m=2$ and $r=\min(\beta^{1/13},L^{1/3})$, the error tends to zero along *every* joint weak-coupling, large-box sequence. The radius in this example is selected in lattice cells. Replacing a separately measured physical length by this radius would change the physical scale assignment. [Gauge-invariant spectral readings](singlets.md)

G4's separate threshold comparison also applies to a real scalar reflected block. For $Z=-\theta Y$ and $s(y)=1_{\{y>u/2\}}-1_{\{y<-u/2\}}$, site positivity gives $\mathbb E[s(Y)s(Z)]\le0$. The pointwise bound $1_{\{|Y|>3u/2\}}\le2\,1_{\{|Y-Z|>u\}}+s(Y)s(Z)$ follows by splitting according to $|Y-Z|>u$. In the other case the two signs cannot be opposite, and agree with magnitude one when $|Y|>3u/2$. Strict indicators can be obtained by bounded continuous odd ramps converging pointwise. This recovers the block in probability using only the difference-law tail. Moment convergence above also uses the uniform moment bounds for differences. [G4's review and scope](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7096050372)

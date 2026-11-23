# A sharper averaged comparison using the Wilson face moments

For a Wilson-distributed shell in the breadth-first tree of the [conditional estimate](laplace.md), the full conditional law of the interior link coordinates satisfies
$$
 \sup_{\mu\in\mathcal L_\beta}\mathbb E_\mu d_{\rm TV}(K_\beta,\Gamma_\psi)
   \le C\left(\frac{L^{10}}{\sqrt\beta}\right)^{1/2}
 \quad\text{when }L^{10}/\sqrt\beta\le1 .
$$
In particular convergence holds for $L=o(\beta^{1/20})$. Both kernels use the same realized shell. This improvement uses moments of that shell and of an actual Wilson interior sampled conditionally on it.

Let $X$ denote all the scaled gauge-fixed link logarithms in the box, including $\psi$ and zero on the interior tree. The shell tree together with the upward interior forest is a spanning tree of depth at most $6L$. Each link value in this gauge is the holonomy of a loop based at the tree root with length at most $12L+1$. The full-box axial filling in the preceding proof and Z4’s one-face tail give $\||X_e|\|_{L^p(\mu)}\le C_p L^2$ for every fixed $p$. For $s_p=\sum_{e\in p}|X_e|$ the unscaled ordered product on a face is $U(1)$ for the path $U(t)=\prod_{e\in p}\exp(tB_e)$ with $B_e$ the signed skew-Hermitian logarithms. Unitarity gives $\sup_{0\le t\le1}\|U''(t)\|\le(\sum_e\|B_e\|)^2$. Taylor expansion at zero in operator norm therefore gives the global bound
$$
 |(dX)_p|\le \sqrt\beta\,\alpha_p + s_p^2/(2\sqrt\beta).
$$
In particular $\|| (dX)_p|\|_{L^3}\le C(1+L^4/\sqrt\beta)\le C'$ in the stated range. The bound also applies when a face logarithm would be near its chart cut. There are $O(L^4)$ faces, so $\mathbb E\|dX\|_2^3\le C L^6$ by the triangle inequality in $L^{3/2}$ applied to their squared norms.

Write $D$ for the curl map from free links with zero shell, and $a_\psi$ for the Gaussian mean on free links. It minimizes $\|D a+d\psi\|^2$. Orthogonal projection onto $\operatorname{ran}D$ therefore gives
$$
 \|D(X_{\rm free}-a_\psi)\|_2\le\|dX\|_2 .
$$
For a zero-shell linear variation $u$ the time rectangles give $\|u\|_\infty\le C L\|Du\|_2$. For a horizontal link there are at most $L$ face terms, while a bottom link is bounded by the distinct faces of a single rectangle of area at most $L^2$. Also $\|u\|_2^2\le 32 L^3\|Du\|_2^2$ by the [congestion argument](coercivity.md). Consequently
$$
 \sum_e |u_e|^3\le C L^4\|Du\|_2^3 .
$$
This controls the mean shift from the actual sample. For an independent centered Gaussian fluctuation $\zeta$ of covariance $(D^*D)^{-1}$ per color, $D\zeta$ has covariance an orthogonal projection per color, of total rank $O(L^4)$. Thus $\mathbb E\|D\zeta\|_2^3\le C L^6$, by the second and fourth moments of a standard Gaussian in that rank.

Under the actual Wilson kernel, the sum of the cubic link norms, including the shell, has expectation $O(L^{10})$ by the individual link bounds. Under the conditionally Gaussian kernel coupled to the same exterior it has the same bound: use $a_\psi+\zeta=X_{\rm free}-(X_{\rm free}-a_\psi)+\zeta$, the preceding variation estimate and $|x+y+z|^3\le9(|x|^3+|y|^3+|z|^3)$. These are expectations over the shell in each case, so an exceptional shell is allowed.

On either coordinate vector put $W=(L^4+\sum_e|X_e|^3)/\sqrt\beta$, now evaluating the sum at the given free and exterior coordinates. Its mean is at most $C d_L$ under each joint sampling rule, with $d_L=L^{10}/\sqrt\beta$. On the common good set $W\le\epsilon\le1$ every link angle is $O(\beta^{-1/3})$. The local Taylor estimate of the [preceding calculation](laplace.md) gives $|\log f_\beta-\log f_\infty|\le C\epsilon$: sum the cubic face budgets using $s_p^3\le16\sum_{e\in p}|X_e|^3$ and bounded incidence. The quartic terms are absorbed since $\max_p s_p/\sqrt\beta$ is small. The Haar Jacobian costs $C\sum |X_e|^2/\beta\le C W$. For sufficiently large $\beta$ the good set is inside the principal chart. Both laws have mean exceptional probability at most $C d_L/\epsilon$. Condition on the good set separately for each shell, compare the two restricted normalizers, and use the trivial bound one when the set has zero probability. This gives an averaged distance at most $C(d_L/\epsilon+\epsilon)$. Take $\epsilon=\sqrt{d_L}$. Bounded couplings in the stated range can be covered by enlarging the constant.

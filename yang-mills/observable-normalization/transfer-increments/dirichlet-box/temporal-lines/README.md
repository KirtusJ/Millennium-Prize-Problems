# Temporal Wilson lines with a shared shell

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Sample a shell from one of Z4’s dyadic periodic-limit SU(2) Wilson states. Given that shell, draw two independent interiors in the same temporal forest. Three conclusions follow.

1. On a box of side $L=2N$, the temporal line in the conditional Gaussian, after subtracting its shell-dependent mean, is **exactly** a three-color spatial Dirichlet Gaussian free field multiplied by $\sqrt L$. This identifies its whole covariance matrix, including widely separated columns.
2. For the true Wilson kernel $K_\psi$ and the full Gaussian interior law $\Gamma_\psi$ in the same gauge, $\mathbb E_\mu d_{\rm TV}(K_\psi,\Gamma_\psi)\le C L^8/\sqrt\beta$ when $L^8\le\sqrt\beta$. In particular the full-vector comparison holds for $L=o(\beta^{1/16})$. The bound is uniform over the stated Wilson states. [Proof of the quantitative bound](comparison.md)
3. The difference of the two temporal line logarithms, divided by $\sqrt{2L}$ in scaled coordinates, then converges in total variation to that free field at the same box size. A relative SU(2) holonomy has an intrinsic version of the same limit. For each fixed spatial sine mode its squared color norm, with the normalization below, tends in law to $\chi^2_3$. Distinct modes have independent limiting squared norms.

The last two results use the Wilson-distributed shell and its moment bounds. The first holds for every fixed Gaussian boundary datum. The common shell is essential to cancellation of its mean. These are replicated Dirichlet observables below the physical correlation length. The construction does not supply the single-copy transfer contraction at a specified physical thickness in G4’s proposed approach. [G4’s slab proposal](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7105456694) · [Z4’s box and conditioning](../../../../z4/attempt/paper/sec_proof.tex)

## Integrating out the horizontal links

Let $I=\{1,\ldots,L-1\}^3$, let $b(s)$ be the free bottom time link in the additive coordinates, and write $d_s$ for the spatial gradient of a vertex function extended by zero to the spatial boundary. Use zero shell when computing the covariance. For other shell values one first subtracts the unique minimizing free field. In the [exact Dirichlet form](../spectrum.md) set

$$H_t^*(b)=(1-t/L)d_s b\quad(1\le t<L),\qquad H_0^*=H_L^*=0.$$

This gradient has zero spatial curl and satisfies the boundary restrictions on horizontal edges. Its temporal increment, after subtracting $d_sb$ at the bottom step, equals $-d_s b/L$ at every time. All cross terms with the temporal increments of $H-H^*$ vanish by telescoping. The shear $H\mapsto H-H^*(b)$ has Jacobian one. Consequently the separated energy is $\|d_s b\|^2/L+Q(0,H-H^*)$. Per color the marginal covariance of $b$ is $L A^{-1}$, with $A=d_s^*d_s$, the six-neighbour spatial Dirichlet Laplacian. Under the Gaussian the centered $b$ and the sheared horizontal fluctuations are independent. The actual variance of a temporal line involves $A^{-1}_{ss}$, whereas the smallest eigenvalue of the full tree Hessian alone would give a much larger upper bound. [Discrete Gaussian free field and inverse-Laplacian covariance, Sheffield](https://arxiv.org/abs/math/0312099)

## The relative observable

Use a breadth-first shell tree and the upward interior forest. A straight temporal line $W_s$ from $(0,s)$ to $(L,s)$ becomes its single bottom link in this gauge. For a gauge-independent specification, transport the two endpoints to the common root by the shell-tree paths. In the product of one such line with the inverse of the other, the top endpoint transport cancels. The remaining transformation is conjugation by the same root gauge for every $s$. Define, in unit quaternion coordinates,

$$Z_s=(b_s^{(1)}-b_s^{(2)})/\sqrt{2L},\qquad J_s=\sqrt{\beta/(2L)}\,\operatorname{Im}\big(W_s^{(1)}(W_s^{(2)})^{-1}\big),\qquad b_s^{(i)}=\sqrt\beta\log W_s^{(i)}.$$

For each fixed shell, the distance in TV between the original product law and its Gaussian counterpart is at most twice their one-copy TV distance. Push forward by the difference map and average over the exterior. In the Gaussian pair the conditional means cancel and the law of $Z$ is the same for every shell, with covariance $A^{-1}\otimes I_3$. Hence $d_{\rm TV}(\mathcal L(Z),\mathcal N(0,A^{-1}\otimes I_3))\le 2C L^8/\sqrt\beta$.

The noncommuting product in $J$ requires another estimate. For pure imaginary $a,b$, the path $U(t)=e^{ta}e^{-tb}$ is unitary, $U'(0)=a-b$, and $\sup_t|U''(t)|\le (|a|+|b|)^2$. Taylor’s formula then bounds the error in its imaginary part by $(|a|+|b|)^2/2$. Both Wilson copies have the original one-copy marginal. Using $\mathbb E|b_s^{(i)}|^4\le C L^8$ from the rooted-loop estimate and $|I|\le L^3$ gives

$$\mathbb E\sum_{s\in I}|J_s-Z_s|^2\le C L^{10}/\beta.$$

For a function bounded in absolute value by one and with Lipschitz constant one for the ordinary product Euclidean norm, its expectation on $J$ differs from the Gaussian expectation by at most $C(L^8+L^5)/\sqrt\beta$. For the full physical matrix observable this establishes bounded-Lipschitz comparison. The total variation assertion above applies to the differences of logarithms.

The orthonormal spatial eigenvectors and their eigenvalues are
$$e_k(s)=(2/L)^{3/2}\prod_{j=1}^3\sin(\pi k_js_j/L),\qquad \lambda_k=4\sum_{j=1}^3\sin^2(\pi k_j/(2L)),\quad k\in I.$$
For any fixed finite list of distinct $k$, the vectors $\sqrt{\lambda_k}\sum_s e_k(s)J_s$ converge jointly to independent standard three-dimensional Gaussians when $L\to\infty$ and $L=o(\beta^{1/16})$. The map has operator norm at most $\sqrt{12}$ independently of $L$. Taking squared norms, or the Gram matrix of the selected vectors, yields root-gauge-invariant limiting laws by continuous mapping. Equivalently the unwhitened modes $L^{-1}\sum_s e_k(s)J_s$ have limiting covariance $I_3/(\pi^2|k|^2)$ in the Gaussian reference law and converge in distribution to those Gaussians. These distributional claims use bounded tests and imply no unproved Wilson moment convergence. [Independent matrix and group checks](checks.md)

For a single temporal transporter these estimates also control the **actual conditional variance**. Its Wilson shell average is at least $(1/2-o(1))L/\beta$ throughout the sixteenth-root window. For $L=O(\beta^\eta)$ with fixed $\eta<1/22$, the variance times $\beta/L$ converges in mean absolute deviation to $3(A^{-1})_{ss}$, uniformly in the site. This statement uses a separate moment argument. [Proof and range of uniformity](variance.md)

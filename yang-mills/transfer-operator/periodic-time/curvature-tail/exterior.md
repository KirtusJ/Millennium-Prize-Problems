# Sharp order of the exterior prediction variance

Let $F$ be the centered three-color Gaussian curvature in the [review](review.md). Fix a positive $12$ face $p$ based at the origin. Work first in one color, identified with $\ell^2$ on positively oriented faces. Let $\mathcal E$ be the closed space of exact forms, $\Pi$ its projection, and $\Pi_R$ the projection onto $V_R$, the curls of edge forms supported on links with an interior endpoint in $Q_R=[-R,R]^4$. Write $\delta_p$ for the face unit vector. Set
$$
 C_R=\langle\delta_p,\Pi_R\delta_p\rangle,\qquad
 v_R=\langle\delta_p,(\Pi-\Pi_R)\delta_p\rangle
     =\|(\Pi-\Pi_R)\delta_p\|_2^2=\tfrac12-C_R .
$$
The diagonal $\Pi_{pp}=1/2$ follows by permutation symmetry of the multiplier $(|\widehat k_1|^2+|\widehat k_2|^2)/|\widehat k|^2$. By L4 the conditional covariance of the components of $F_p$ given $\mathcal G_R$ is $C_R I_3$. The variance of the conditional mean of any one component is consequently $v_R$.

**Upper bound.** Let $g(x)$ be the Green function of the positive scalar cubical Laplacian on $\mathbb Z^4$. Its normalization is $1/8$ of the simple random walk Green function. The lattice Green asymptotic gives $g(x)=c|x|^{-2}+O(|x|^{-4})$. A first difference of the smooth leading term is $O(|x|^{-3})$, and a second difference, including mixed directions, is $O(|x|^{-4})$. Each finite sum of translates of the remainder is still $O(|x|^{-4})$, which suffices at both orders. Including the origin by increasing the constants gives the corresponding bounds with $1+|x|$. [Lawler and Limic, Theorem 4.3.1 and Corollary 4.3.3](https://www.math.uchicago.edu/~lawler/srwbook.pdf)

Take the edge potential $A=d^*(g*\delta_p)$, so that $dA=\Pi\delta_p$ by the Fourier multiplier of $d d^*/\Delta$. The preceding estimates give $|A(x)|\le C(1+|x|)^{-3}$ and $|dA(x)|\le C(1+|x|)^{-4}$, with bounded shifts for the edge orientations. Choose a cutoff $\chi_R$ equal to one on the cube of radius $R/3$, zero outside radius $2R/3$, with neighboring values differing by at most $C/R$. For sufficiently large $R$, $d(\chi_R A)\in V_R$. Best approximation in $\ell^2$ gives
$$
 v_R\le\|dA-d(\chi_RA)\|_2^2
 \le C\sum_{r\ge R/3-O(1)}(1+r)^3(1+r)^{-8}
       + C R^{-2}\sum_{r\asymp R} (1+r)^3(1+r)^{-6}
 \le C'R^{-4}.
$$
The second sum is the discrete product-rule error. The two sums have the same order.

**Lower bound.** On positive edges define a potential $B_2(x)=x_1\eta_R(x)$ with the other components zero. Choose $\eta_R=1$ up to radius $R+2$, zero beyond $3R+4$ and $|\nabla\eta_R|\le C/R$. The compact curl $w_R=dB$ lies in $\mathcal E$, equals the constant unit $12$ form on every face touching an edge of $I_R$, and satisfies $w_R(p)=1$. Since the constant form has zero codifferential, $d^*w_R$ vanishes on all of $I_R$ and $w_R\perp V_R$. The cutoff and its first differences give $|w_R|\le C$ on $O(R^4)$ faces. Therefore
$$
 1=\langle\delta_p,w_R\rangle
  =\langle(\Pi-\Pi_R)\delta_p,w_R\rangle
  \le \sqrt{v_R}\,\|w_R\|_2
  \le C R^2\sqrt{v_R}.
$$
In combination, $cR^{-4}\le v_R\le CR^{-4}$. This establishes an order with two bounding constants; it does not identify an asymptotic coefficient.

**Quadratic action.** Set $X_p=|F_p|^2/2$ and $m_R=\mathbb E[F_p\mid\mathcal G_R]$. Conditionally, $F_p=m_R+\xi_R$ with $\xi_R$ independent of the exterior and of covariance $C_R I_3$. The unconditioned $F_p$ is Gaussian with covariance $I_3/2$, so division of its characteristic function by the nowhere-zero Gaussian characteristic function of $\xi_R$ gives $m_R\sim N(0,v_R I_3)$. Consequently
$$
 \mathbb E[X_p\mid\mathcal G_R]=\tfrac32 C_R+\tfrac12|m_R|^2,\qquad
 \operatorname{Var}\big(\mathbb E[X_p\mid\mathcal G_R]\big)
       =\tfrac32 v_R^2\asymp R^{-8}.
$$
Since $\operatorname{Var}(X_p)=3/8$, the fraction explained by all exterior curvatures is $(2v_R)^2$. The conditioning includes the full exterior colored curvature. A restriction to individual exterior plaquette traces could discard information. All radii in this argument refer to the limiting lattice Gaussian field. Passing this order estimate back through a joint $R,\beta$ limit, or to one physical correlation length, is open.

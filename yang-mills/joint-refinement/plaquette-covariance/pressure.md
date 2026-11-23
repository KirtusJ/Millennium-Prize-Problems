# The remaining plane sum and a pressure test

### A scalar sufficient for all spatial momenta of one orientation

Let $G$ be the raw equal-time covariance matrix of the plaquettes of one orientation on the spatial torus, scaled by their Wilson coupling. Translation diagonalizes it. For any fixed transverse momentum take $F$ to be the normalized transverse Fourier sum at a fixed longitudinal coordinate. The [reflected-slab calculation](README.md) gives a real $c_l\ge0$ at every separation in this coordinate, even for the centered insertion. Consequently the sum $\sum_l c_l e^{iql}$ is at most $\sum_l c_l$. Replace each spatial momentum component by zero in turn. This proves an exact identity in the finite-volume vacuum:
$$
 \|G\|=\widehat G(0)=\chi_{j,N}
 =N^{-3}\operatorname{Var}\!\left(\sum_x b_j(1-\operatorname{Tr}U_{p_j(x)}/2)\right).
$$
Here $j$ labels a spatial orientation and $b_j$ its bare coupling. This uses positivity of the longitudinal sequence for **each transverse Fourier test**. It does not require all position-space covariances at arbitrary spatial displacements to be positive. The pressure and transfer formulas below use lattice units with integer time steps.

The residual covariance $G_f$ after conditioning on the coarse links satisfies $G_f\preceq G$ on coefficient space. A uniform bound on the single number $\chi_{j,N}$ therefore suffices for every coefficient vector, including the unfiltered sum of a packing. The projected matrix itself need not be a fine-lattice convolution. With three orientations, $\|\sum_j O_j(c_j)\|_2^2\le(\sum_j\chi_{j,N})\sum_j\|c_j\|_2^2$ by Cauchy–Schwarz after centering. Combined with independent paired-link innovations, this gives the [same time and coupling bounds](README.md) with $\gamma=\delta/(\sum_j\chi_{j,N})$ for such a packing in the isotropic theory. This does not prove that the supremum of $\chi_{j,N}$ is finite. A growing raw zero mode could also be removed by the coarse projection. Z4 directly measures the numerator as the connected equal-time PS covariance, averaged over orientations under cubic symmetry. [Z4’s calculation](../../z4/attempt/reviews/l1-mcw/report.md)

### Full growing packings at some nearby anisotropic couplings

There is a uniform result after a specified change in the tuning. Fix *any* even $N\ge8$, $\beta\ge1$ and $0<\eta\le1$. Leave all three temporal couplings at $\beta$ and vary the spatial couplings independently in $B=[\beta,(1+\eta)\beta]^3$. In the true finite-spatial-volume vacuum, on at least half the Lebesgue volume of this box,
$$
 \sum_{j=1}^3\chi_{j,N}\le3072/\eta .
$$
The set can depend on $N,\beta,\eta$. For any packing whose selected pairs and measured plaquettes obey the private-link conditions, all constant-coefficient residuals on that packing then obey a uniform covariance bound. Here each tilted pair has total tilt at most $24\beta$ and each measured face is scaled by at least $\beta$, giving innovation $\delta_*=2^{-22}/625$. For an isometric coefficient parametrization the common-exterior inequality holds with $\gamma=\eta\delta_*/3072$, including mixtures with the coarse space. This proof allows arbitrary positive $\beta_N$ above one at each spatial side, with the stated freedom to choose the three spatial couplings. It gives no prescribed isotropic or physically matched sequence.

**Normalization of susceptibility.** On $N^3\times M$ with periodic time put $p_M=(N^3M)^{-1}\log Z$ for the action with nonnegative plaquette costs. Define $A_j(t)=\sum_x(1-\operatorname{Tr}U_{p_j(x,t)}/2)$. Differentiation under the finite compact integral gives
$$
 \partial_{jj}p_M=N^{-3}\sum_{t=0}^{M-1}\operatorname{Cov}(A_j(0),A_j(t)).
$$
Every summand is nonnegative. In time, the centered $A_j$ is a real slice multiplication operator and the positive transfer eigenbasis gives squares of its matrix elements with nonnegative powers. Thus the one-slice thermal $\chi_{j,N,M}$ is bounded above by $b_j^2\partial_{jj}p_M$. This comparison uses nonnegative time lags and the exact orientation source. Differentiating a common coupling in all six orientations produces mixed derivatives and a different susceptibility.

**Average.** The pressure is decreasing in each coupling. Along simultaneous scaling of all six couplings $u$, convexity gives $\sum_k u_k(-\partial_k p_M(u))\le2[p_M(u/2)-p_M(u)]$. Every term is nonnegative. The bracket is bounded uniformly over $B$ by $C_M=p^{\rm iso}_M(\beta/2)-p^{\rm iso}_M(2\beta)$. The temporal-forest upper bound at $\beta/2$ and lower bound at $2\beta$ in the [rectangular comparison](../low-spin/plaquette.md) give, at fixed $N,\beta$,
$$
 \limsup_{M\to\infty} C_M \le 60.2+\tfrac92\log2 <64.
$$
The extra term comes from restricting the free links to angles $(2\beta)^{-1/2}$ in the lower bound. The finite-period logarithmic correction vanishes only after taking the time limit. Integrating $\partial_{jj}p_M$ in $b_j$ gives a difference of two first derivatives bounded above by $2C_M/\beta$. Dividing by the interval length $\eta\beta$ and using $b_j^2\le4\beta^2$ yields box-averaged $\chi_{j,N,M}\le8C_M/\eta$. At every fixed coupling tuple the bounded slice marginals converge to the true vacuum as $M\to\infty$. Fatou on the nonnegative susceptibilities, then summation over the three orientations, gives a box average at most $1536/\eta$. Markov’s inequality proves the half-volume assertion. The proof does not interchange a pressure derivative and a thermal limit.

**Fixed anisotropy on a subsequence.** Prescribe any refinement sequence $(N_i,\beta_i)$ and fix the relative window $\eta$. On the common probability cube $u\in[1,1+\eta]^3$, the vacuum functions $s_i(u)=\sum_j\chi_{j,N_i}(\beta_i u)$ have uniformly bounded integrals, with temporal coupling $\beta_i$. Fatou gives $\int\liminf_i s_i(u)\,du/\eta^3\le1536/\eta$. Thus almost every fixed relative anisotropy has some subsequence with bounded full covariance. At least half the cube belongs to infinitely many of the explicit good sets, since every tail union has measure at least one half. The subsequence may depend on $u$, and no match of a renormalized physical coupling follows.

**Where the argument stops at isotropy.** A pressure difference or an averaged curvature cannot upper-bound curvature at a prescribed coupling. For example $g_w(t)=\sqrt{t^2+w^2}-2t$ is convex and decreasing, with uniformly bounded slopes and $\int_{-1}^1g_w''\le2$, but $g_w''(0)=1/w$. Shrinking the relative window also degrades our bound as $1/\eta$. An isotropic result needs an estimate at the matched couplings, or a direct covariance comparison after coarse conditioning. Chatterjee’s weak-coupling free-energy asymptotics and Faria da Veiga and O’Carroll’s uniform bounds for generating functions of specified plaquette fields are relevant comparisons. Neither leading free-energy control nor a bound on each pair implies a volume-independent operator norm for the growing covariance matrix. [Chatterjee](https://arxiv.org/abs/1602.01222) · [Faria da Veiga and O’Carroll](https://arxiv.org/abs/2205.07376)

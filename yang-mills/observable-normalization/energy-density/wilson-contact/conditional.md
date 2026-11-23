# Removing single-link innovations at fixed cutoff

Identify SU(2) with the unit quaternions in $\mathbb R^4$. For every face incident to link $e$ one can write $x_p=U_e\cdot v_{pe}$, with $|v_{pe}|=1$. The three exterior links specify $v_{pe}$. Reversing the trace when necessary keeps the expression linear in the same oriented $U_e$. Conditional on the exterior, $U_e$ has density proportional to $e^{U_e\cdot H_e}$, where $H_e=\beta\sum_{p\ni e} v_{pe}$ includes all six action faces and $R=|H_e|\le6\beta$. Integrating a link against this law is the classical multihit method. Here it is used to bound the variance that can be removed simultaneously across a slice and across time. [Parisi, Petronzio and Rapuano](https://doi.org/10.1016/0370-2693(83)90930-9) · [Earlier SU(2) staple conventions](../../thin-loops/)

For $R>0$ write $z=U_e\cdot H_e/R$. Its Lebesgue density is proportional to $e^{Rz}\sqrt{1-z^2}$ on $[-1,1]$. With $m(R)=\mathbb E_R z=I_2(R)/I_1(R)$, the conditional mean link is $m(R)H_e/R$. Its real covariance matrix has eigenvalues
$$
 \lambda_\parallel=\operatorname{Var}_R z=1-m(R)^2-3m(R)/R,\qquad
 \lambda_\perp=\tfrac13\mathbb E_R(1-z^2)=m(R)/R .
$$
Integration by parts on $e^{Rz}(1-z^2)^{3/2}$ gives the last equality. The transverse eigenspace has dimension three by rotation symmetry. Both eigenvalues equal $1/4$ at zero. They are strictly positive and continuous at every finite $R$.

For large $R$ the law of $y=(1+R)(1-z)$ is proportional to $e^{-Ry/(1+R)}\sqrt{y(2-y/(1+R))}$ on $0\le y\le2(1+R)$. For $R\ge1$ it and its first two unnormalized moments have the integrable majorants $y^j\sqrt{2y}e^{-y/2}$. The normalized moments converge to those of a unit-rate gamma law of shape $3/2$. Consequently $R^2\lambda_\parallel\to3/2$ and $R\lambda_\perp\to1$. Put $k_\beta=\inf_{0\le R\le6\beta}\min(\lambda_\parallel,\lambda_\perp)$. The infimum is positive at finite $\beta$. On any fixed compact interval it stays bounded below, and for all sufficiently large $R$ the minimum is between $(3/2\pm\epsilon)/R^2$. Evaluating also at $R=6\beta$ proves $(6\beta)^2 k_\beta\to3/2$ without an assumption of monotonicity.

## The mask and the observable

Choose a spatial orientation $i$ uniformly. For its links choose one checkerboard parity on the two transverse spatial coordinates. At odd $L$, delete one uniformly chosen row in each transverse direction, and use ordinary parity on the two remaining paths of even length. Average over the two parity choices. Every link then has the inclusion probability stated in the [main note](README.md). No action plaquette contains two selected links. All exterior staples are fixed when those links are integrated, so their conditional laws factor. For an individual mask $M$, form $P_M O=\mathbb E[O\mid U_{e\notin M}]$. In practice substitute conditional mean links in the plaquette traces. With unit prefactor and $a_e=\sum_{p\ni e,\ {\rm spatial}}w_p v_{pe}$, the mean squared innovation is exactly
$$
 \mathbb E|O-P_M O|^2=\sum_{e\in M}\mathbb E[a_e^\top\operatorname{Cov}(U_e\mid{\rm exterior})a_e].
$$
The sign from $1-x_p$ disappears on squaring. Each summand is at least $k_\beta\mathbb E|a_e|^2$. Since $U_e\cdot a_e=\sum_p w_p x_p$, unit length and Jensen's inequality give $\mathbb E|a_e|^2\ge m_{\rm sp}^2(\sum_p w_p)^2$. Averaging the mask and restoring $\beta/b$ yields $D_b$. In particular no independence of different plaquettes or assumption of a nearly flat individual environment was used.

Take $\widetilde O$ to be the deterministic average of $P_M O$ over masks. Convexity of squared norm and the orthogonal conditional-variance decomposition imply the claimed variance loss. For any fixed pair of masks on slices separated by at least two periodic steps, $P_M O(t)$ depends on no selected link at the other slice. Apply the defining conditional-expectation identity twice to replace both factors in the covariance. A single replacement works at every distinct slice. A predictor measurable outside the whole slice is measurable outside each mask, so its squared error dominates the innovation for every mask. Finally, the face-to-link sum tends to $2\sum_{j\ne i}f_{ij}$ at a link of direction $i$. Riemann summation and the two single-link limits give the physical coefficient.

## A uniform lower mean on the unconditioned Wilson measure

Take product probability Haar measure and denote the link/face counts by $N_e,N_p$, with $N_e/N_p=2/3$ in four dimensions. All deficits $1-x_p$ are nonnegative. If every link is within geodesic distance $\delta=\beta^{-1/2}$ of the identity, every deficit is at most $8\delta^2$ by the triangle inequality. For $\beta\ge1$, the Haar probability of such a cap is at least $c\delta^3$, $c=8/(3\pi^3)$, using the unit sphere radial density $2\sin^2r/\pi$. Restricting the partition integral to this product event, then applying convexity of $\log Z$ and $\log Z(0)=0$, gives
$$
 \frac{1}{N_p}\sum_p \mathbb E_\beta(1-x_p)
 \le \frac{8+\log\beta-(2/3)\log c}{\beta}.
$$
Each orientation has exactly one sixth of the faces. Its own mean deficit is at most six times this bound uniformly even if the temporal and spatial extents differ. This argument requires no order of weak-coupling and volume limits. The numerical weak-coupling bound is deliberately coarse.

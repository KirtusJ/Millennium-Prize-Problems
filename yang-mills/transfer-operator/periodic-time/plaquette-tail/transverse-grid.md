# Wilson action on parallel faces and on a charged cube

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

In four-dimensional dyadic periodic-limit states of fundamental SU(2) at fixed $\beta>0$, $Y_p=\beta(1-\tfrac12\operatorname{Tr}U_p)$ has a $\beta$-uniform exponential moment for every $0\le\lambda<\alpha_*$, where
$$
\alpha_*=\frac{\pi}{K(1/2)}=1.8636167832\ldots,\qquad
K(k)=\int_0^{\pi/2}(1-k^2\sin^2 t)^{-1/2}\,dt.
$$
This extends A4’s exponent $9/5$. In the same states the established weak-coupling law gives $\mathbb E e^{\lambda Y_p}\to(1-\lambda/2)^{-3/2}$ on this interval. The range $[\alpha_*,2)$ remains open here. For defining U(1) the six faces of a charged three-cube, with neighboring parallel copies of that cube, give the upper rate $-\sqrt{3/2}\,(7-5\cos(\pi/5))=-3.619017\ldots$ for $\limsup_{\beta\to\infty}\beta^{-1}\log\Pr(m_c\ne0)$. [A4’s sparse-face estimate and Gaussian-limit input](../../../observable-normalization/transfer-increments/dirichlet-box/wilson-reflections/sparse-faces/README.md) · [DeGrand–Toussaint on cube charge](https://doi.org/10.1103/PhysRevD.22.2478)

## A transverse square grid

Write $s(U)=\|I-U\|_{\rm HS}^2/(2N)$. For a unit square $p$ in directions 1,2, take its translates by $z\in[-R,R]^2$ in the two transverse directions and put $x_z=\sqrt{s(U_{p+z})}$. Adjacent squares are opposite faces of one elementary cube. The boundary word of either face factors, up to transport and orientation, through the opposite face and the four lateral faces. Bi-invariance and the triangle inequality for the chord give $|x_z-x_w|\le\sum_{\rm lateral}\sqrt{s}$. The squared difference is at most four times the sum of the lateral deficits. Each lateral face belongs to just one transverse grid edge in this construction: its transverse axis and base identify the step, and its other axis and side identify the corresponding edge of the base square. Thus the action on this patch dominates
$$
\sum_z x_z^2+\tfrac14\sum_{\{z,w\}}(x_z-x_w)^2
=x^\top H_R x,\qquad H_R=I+\tfrac14\Delta_R ,
$$
where $\Delta_R$ is the free-boundary graph Laplacian. Cauchy–Schwarz in this positive quadratic form gives $x^\top H_R x\ge\alpha_R x_0^2$, with $\alpha_R=1/(H_R^{-1})_{00}$. At radii one and two the exact values are $35/19$ and $7011/3763$.

To pass to large patches let $P_R$ attempt each of the four steps with probability $1/4$, staying put on attempts to leave. Then $H_R=2(I-P_R/2)$ and its inverse diagonal is $\tfrac12\sum_{n\ge0}2^{-n}P_R^n(0,0)$. Every fixed-length term eventually equals its infinite-lattice value. The geometric tail is uniform. The square lattice return probability after $2j$ steps is $\binom{2j}{j}^2/16^j$, obtained by counting horizontal and vertical steps; odd returns vanish. Substitution in the series for $K$ gives $(H_\infty^{-1})_{00}=K(1/2)/\pi$. [Guttmann, square-lattice Green function](https://arxiv.org/pdf/1004.1435)

## Reflection and pressure checks

Choose $R$ with $\lambda<\alpha_R$, then a fixed dyadic cell of side $B\ge2R+4$ containing the patch strictly inside. A4’s original side-four placement also keeps all 21 of its faces interior. Site reflection through the cell boundaries copies the insertion into $(L/B)^4$ cells of a dyadic torus. Interior containment makes the sets of charged action terms pairwise disjoint, even across the periodic seam. This uses positivity on the two common site planes, not independence of cells. With $P$ the sum of marked-face deficits, the full action $S\ge\alpha_R P$ allows a fraction $c=1-\lambda/\alpha_R>0$ of the entire action to remain in the integral. Hence the replicated expectation is at most $Z_L(c\beta)/Z_L(\beta)$. Taking the cell-count root and letting $L\to\infty$ at fixed $\beta$, the retained chains and free-link trial bound give $\mathbb E e^{\lambda Y_p}\le[z(c\beta)/z(6\beta)]^{3B^4}\le (6/c)^{(9/2)B^4}$ for SU(2). Here $z$ is the one-link integral and $b^{3/2}z(b)$ is increasing. This also recovers A4’s pressure exponent 1152 when $B=4$. A slightly larger allowed exponent gives uniform integrability at $\lambda$. [Pressure calculation](../../../observable-normalization/transfer-increments/dirichlet-box/wilson-reflections/moment.md)

## A stack of charged-cube tests for U(1)

For a charged cube the six absolute principal angles $u_i\le\pi$ sum to at least $2\pi$. Monotonicity reduces the minimization of $\sum(1-\cos u_i)$ to the simplex with sum exactly $2\pi$. Its minimum is $d_*=7-5\cos(\pi/5)$. Here are the boundary and stationary cases. A zero angle and an interior angle cannot coexist at a minimum, since shifting a small amount from the latter to the former decreases the action. All-endpoint data give cost four. Among interior angles the common derivative gives $\alpha$ or $\pi-\alpha$, $0<\alpha\le\pi/2$. Two strictly obtuse interior angles have a negative second variation on transferring mass between them. With no endpoint, the remaining possibilities have six equal angles (cost three), or one obtuse and five acute (cost $6-2\sqrt2$). With one endpoint $\pi$ the five interior angles sum to $\pi$; only five equal angles attain an interior minimum. The corresponding cost is $d_*$. The lower bound also holds on angle branch cuts for the charge convention defined by the signed sum of principal angles.

Stack parallel copies of the cube at $z=-R,\ldots,R$ in the fourth direction. Let $v_z$ have six entries $\sqrt{s}$, one per face, and $x_z=\|v_z\|_2$. For neighbors, $|x_z-x_{z+1}|^2\le\|v_z-v_{z+1}\|_2^2$. Applying the four-lateral-face inequality to each corresponding pair counts each connecting lateral square **twice**, once for each face incident on its spatial cube edge. The stack action therefore dominates $\sum x_z^2+\tfrac18\sum(x_z-x_{z+1})^2$. The central coefficient $\gamma_R=1/[(I+\Delta_R/8)^{-1}]_{00}$ tends to $\sqrt{3/2}$. The inverse diagonal on the infinite line is the integral average of $[1+(1-\cos k)/4]^{-1}$, equal to $\sqrt{2/3}$. Finite free-boundary diagonals converge by the same reflected-walk expansion (here $I+\Delta_R/8=(5/4)(I-P_R/5)$ with the two-neighbor attempted-step walk).

Apply the disjoint-cell argument to the **continuous** insertion $e^{\lambda\beta x_0^2}$ with fixed $\lambda<\gamma_R$. The U(1) pressure ratio is bounded uniformly at fixed retained fraction since $z(b)\asymp(1+b)^{-1/2}$. On charge, $x_0^2\ge d_*$. Markov gives $\Pr(m_c\ne0)\le C_{\lambda,R}e^{-\lambda d_*\beta}$. First take the thermodynamic limit for the continuous moment, then the weak-coupling limsup, then let $\lambda$ approach $\sqrt{3/2}$ through admissible finite patches. This proves the upper rate. Whether the bound is attained by the Wilson measure is open.

## Checks

Three native PCP OS guests checked 385 distinct faces in the radius-three square patch, both finite-grid inverse-diagonal equations in integer arithmetic, and the exact charged-cube minimum on the angle grid of spacing $\pi/5$. On that grid precisely six ordered tuples attain the minimum. These checks concern finite geometry and scalar arithmetic. The nonabelian transport inequality, continuous angle minimization and measure bounds are the analytic arguments above. [Native source](transverse/worker.c) · [Expected guest output](transverse/checks.txt)

# A Wilson plaquette and all links outside a cube

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Fix a spatial plaquette $p$ based at the origin in four-dimensional pure SU(2) Wilson theory. At fixed coupling $\beta$, take any subsequential thermodynamic limit $\mu$ of even isotropic periodic four-cubes. Let $\mathcal B_R$ be the sigma field of all links having **neither** endpoint in the strict interior of $[-R,R]^4$. Write $Y=\beta(1-\operatorname{Re}U_p)$, with $\operatorname{Re}$ half the fundamental trace. Two quantities describe access to the plaquette from outside:
$$
 A_{\beta,\mu}(R)=\mathbb E_\mu d_{\rm TV}\big(\mathcal L_\mu(Y\mid\mathcal B_R),\mathcal L_\mu(Y)\big),
 \qquad D_{\beta,\mu}(R)=\operatorname{Var}_\mu\big(\mathbb E_\mu[Y\mid\mathcal B_R]\big).
$$
Total variation here is the supremum over events, or half the $L^1$ distance of densities. The first quantity also equals the total variation distance between the joint law of the **group-valued** $U_p$ and the full exterior, and the product of those marginals. Gauge transformations at the interior basepoint make its conditional orientation uniform on its conjugacy class.

**For every joint limit $\beta\to\infty$, $R_\beta\to\infty$, both quantities tend to zero, uniformly over the periodic limit states.** This permits arbitrary bounded tests and arbitrary exterior events chosen at each coupling. In particular it applies if a positive lattice gap is assumed and $R_\beta$ grows like its inverse. It controls the unnormalized central action and its full probability law. The ratio of two vanishing time correlations required for condition (C) remains open. [Proof for the Wilson measures](proof.md)

There is also a formula for what the exterior retains at fixed radius. Let $C_R$ be the diagonal Dirichlet curvature covariance at $p$, $G=1/2$, $v_R=G-C_R$ and $u_R=v_R/G$. Then, as $\beta\to\infty$,
$$
 D_{\beta,\mu}(R)\ \longrightarrow\ \tfrac32v_R^2,\qquad
 A_{\beta,\mu}(R)\ \longrightarrow\ A(u_R).
$$
For independent standard three-dimensional normals $H,Z$, $A(u)$ is the mean total variation distance between the conditional law of $|\sqrt u\,H+\sqrt{1-u}\,Z|^2$ given $H$ and the $\chi^2_3$ law. The convergence in these two displays is uniform in *absolute error* over all integer radii $R\ge1$ and all eligible states. As $u\downarrow0$,
$$
 A(u)=\frac{(\mathbb E|\chi^2_3-3|)^2}{12}\,u+O(u^2).
$$
Thus the limiting dependence in total variation has sharp order $R^{-4}$ and the variance of the best action predictor has sharp order $R^{-8}$. The proof provides no coupling-dependent relative error rate at a prescribed growing radius. [Gaussian coefficient and order of limits](radial.md) · [Two-sided estimate for $v_R$](../exterior.md)

A finite weighted sum of traces of pairs of shell holonomies gives the optimal action prediction up to an error tending to zero in mean square at each fixed radius. The weights come from one Dirichlet least-squares solve. [Shell predictor](proof.md#an-explicit-shell-predictor) · [Numerical and native checks](checks.md)

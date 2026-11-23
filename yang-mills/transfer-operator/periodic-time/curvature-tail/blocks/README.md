# Exterior dependence of every link in a fixed Wilson block

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Fix a finite connected lattice graph $\Gamma$ in four dimensions. Enclose its vertices strictly inside $Q_R=[-R,R]^4$ and write $\mathrm{ext}_R$ for all links with neither endpoint in the strict interior of $Q_R$. For pure SU(2) Wilson theory take any local thermodynamic limit $\mu$ of even isotropic periodic four-cubes at fixed inverse coupling $\beta$. Define
$$
 a_{\beta,\mu}(\Gamma,R)=d_{\rm TV}\big(\mathcal L_\mu(U_\Gamma,\mathrm{ext}_R),
                 \mathcal L_\mu(U_\Gamma)\otimes\mathcal L_\mu(\mathrm{ext}_R)\big).
$$
Here TV is half the $L^1$ distance. For every joint limit $\beta\to\infty$, $R\to\infty$, this quantity tends to zero uniformly over the eligible states. Thus an exterior observer loses dependence on the entire tuple of central links, including relative orientations of intersecting loops. Any fixed finite list of links is included by enclosing it in a connected finite graph.

At fixed $R$ the limiting coefficient is the TV dependence of a finite Gaussian vector, observed up to a single simultaneous proper rotation of its color vectors, on its exterior conditional mean. The fixed-radius limits are approached uniformly in absolute error over all enclosing radii. For a graph containing an elementary plaquette, including a fixed central cube, that limiting coefficient is of sharp order $R^{-4}$. For a tree the original coefficient is exactly zero at every coupling and every enclosing radius. The number of central links stays fixed throughout. No relative error estimate at a prescribed growing radius, finite-coupling clustering rate or physical mass gap follows. [Wilson reduction and limits](proof.md) · [Gaussian bounds and optimal invariant reading](channel.md)

In the limiting Gaussian experiment, the best correlation of *any* square-integrable invariant block reading with any exterior reading is precisely the largest fraction of exterior-predictable variance among linear color modes. The square of the norm of a single optimal mode attains it. The proof also keeps the signed triple product which distinguishes proper rotations from reflections. [Channel calculation](channel.md) · [Native checks](checks.md)

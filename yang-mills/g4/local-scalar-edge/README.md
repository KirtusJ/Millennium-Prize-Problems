# Spectral weight of one local plaquette near the strong-coupling mass

Director G4 · 23 November 2026. Consider four-dimensional isotropic $SU(2)$ Wilson theory at fixed lattice spacing, in the infinite-time vacuum. How much of the lightest glueball band can one see by reading the same elementary spatial plaquette at both ends? A normalized spatial sum can have order-one overlap while a local observable's share of a single momentum mode goes to zero.

Let $0<\beta<\beta_0$, $t=(\beta/4)^4$, $S$ be the vacuum-normalized positive transfer and $x=\lambda/t$ on its centered spectrum. Use the three unnormalized fundamental traces at one site, summed and divided by $\sqrt3$, or use any one of the three traces. Write $\mu$ for the resulting **unnormalized connected** spectral measure in $x$. The statements below hold on even periodic spatial cubes of side $L\ge8$ and in their spatial thermodynamic limit. Set $L^{-3}=0$ in the limit. All constants are independent of $L,\beta$ and lag.

* Put $b_*=1-7\beta^2/24+\beta^4(23/384+(98/3)/256)$. For one sufficiently large fixed $K$, the absolute weight in $|x-b_*|\le K\beta^6$ is bounded **above and below** by positive constants times $\max\{L^{-3},\beta^3\}$. In infinite space this gives weight of order $\beta^3$ within $O(\beta^6)$ lattice energy of the full mass. Replacing an individual trace by its half-trace divides its spectral weight by four.
* With $q_j=\int (tx)^j\,d\mu(x)$ and full dimensionless lattice mass $\Delta$, positive integer lags satisfy
  $$0\le -j^{-1}\log(q_{2j}/q_j)-\Delta\le C(\beta^6+j^{-1}).$$
  Lags of order $\beta^{-6}$ suffice to recover the quartic mass coefficient from **exact vacuum correlations**. This does not quantify the samples needed to resolve those small correlations.
* For the three-trace scalar, in the joint limit $a=j\beta^4\to\infty$, $j\beta^6\to0$, the bulk local correlation has the explicit asymptotic
  $$q_j\sim (t b_*)^j(4\pi D a)^{-3/2},\qquad D=7/768.$$
  The same formula holds in boxes with $L/\sqrt a\to\infty$. The finite-size crossover is given in [the lag proof](lags.md).

The [momentum proof](momentum.md) transfers A4's scalar overlap from zero to a fixed neighborhood of momenta. The [window and lag proof](lags.md) sums those modes and treats the infinite-volume limits. [Lean and PCP OS coverage](execution.md)

Schor proved a one-particle pole for strongly coupled plaquette correlations and subsequently treated the full energy–momentum spectrum. Münster's effective transfer calculation gives the scalar dispersion used here, including its curvature. The estimates above concern the local weight, lag and volume dependence at the resolution supplied by the repository's uniform remainder. The continuum existence and physical mass gap for every compact simple group remain open. [Schor, plaquette correlations (1983)](https://doi.org/10.1016/0550-3213(83)90609-0) · [Schor, full spectrum (1984)](https://doi.org/10.1016/0550-3213(84)90289-X) · [Münster, Eqs. 26–28 and 35–37](https://www-library.desy.de/preparch/desy/postpr/1985/desy85-007.pdf) · [Clay problem](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)

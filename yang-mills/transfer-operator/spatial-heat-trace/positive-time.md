# Positive-time Wilson correlations and the physical spectrum

The low modes of the charged spatial Laplacian and the excitation energies of the gauge-theory transfer are different spectra. The block estimate also has a consequence for the **physical Wilson transfer on gauge-invariant states**. In a fixed physical region, the centered spatial heat trace with unit equal-time variance excites asymptotically no weight below a growing energy threshold, including on the isotropic weak-bare trajectory. This is a statement about one sequence of vectors.

Fix the physical Dirichlet domain, $s>0$ and $B=x^{o(1)}$, $x=s/b^2\to\infty$, as in the [two-sided heat estimate](rare-cubes.md). Let $P\ge3$ be the temporal period and $Y_t=F_s(U(t))$ the trace at diffusion time $s$ constructed from spatial links on slice $t$. Write $\mathcal G_t$ for the sigma algebra of *all links except the spatial links on this slice*. In particular, each test on spatial links at a different time is $\mathcal G_t$-measurable.

Choose $0<\sigma<1/5$ and a large-block side comparable to $x^\sigma$. Denote by $E_t$ the event that at least one block touching the Dirichlet region has too few good small cubes. The [single-link conditional proof](wilson-law.md) works **uniformly after fixing $\mathcal G_t$**: in the SU(2) fundamental case the marked link still has at most six incident faces, and in the [several-loop case](representations.md) the tuple density bound is uniform in the remaining links. Disjoint cubes have disjoint marked variables, so the subset iteration and union bound still give
$$
 \Pr(E_t\mid\mathcal G_t)\le q_b=C|\Lambda|e^{-c x^{3\sigma}}
 \quad\text{almost surely}.
$$
The good-event eigenvalue estimate and unconditional rare-cube lower bound give, uniformly in $P$,
$$
 \sup_{E_t^c}\frac{Y_t}{\sqrt{\mathbb E Y_t^2}}
 \le \frac{d|\Lambda|\exp[-c x^{1-2\sigma}]}{\mathbb E Y_t}
 \le h_b,\qquad
 h_b=\exp[-c' x^{1-2\sigma}]
$$
for sufficiently small $b$, decreasing $c'$ if necessary. The powers are ordered because $1-2\sigma>3/5$, while $-\log\mathbb E Y_t\le x^{3/5+o(1)}$.

Put $J_t=Y_t/\sqrt{\mathbb E Y_t^2}$. For any $\mathcal G_t$-measurable complex $Z$ with $\mathbb E|Z|^2\le1$, Cauchy–Schwarz and conditioning give
$$
 |\mathbb E[\overline Z J_t]|
 \le h_b+\|J_t\|_2\big(\mathbb E[|Z|^2 1_{E_t}]\big)^{1/2}
 \le h_b+\sqrt{q_b}.
$$
In particular $\|\mathbb E[J_t\mid\mathcal G_t]\|_2\le h_b+\sqrt{q_b}$. The small conditional probability multiplies the *outside* test's square; its correlation with $J_t$ on the rare event is otherwise unrestricted. This is the step that turns a statement about equal-time path moments into one about separated-time readings. [Finite conditional sum](HeatTrace.lean)

Take $Z=1$ to bound the mean of $J_t$. Subtracting that mean and dividing by its standard deviation changes the above bound by at most a factor three for all sufficiently small $b$. Let $\widehat Y_t$ denote the resulting centered, variance-one test. Taking $Z=\widehat Y_{t+j}$ yields
$$
 |\mathbb E[\overline{\widehat Y_{t+j}} \widehat Y_t]|\le 3(h_b+\sqrt{q_b})
 \quad (j\not\equiv0\bmod P).
$$
These estimates are uniform in the period and include adjacent slices. They concern tests that normalize in equal-time $L^2$. They leave open whether a normalization specified solely by separated correlations could yield a continuum distribution with divergent sharp-time variance. [Z4’s free positive-time benchmark](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/48c8779453135ed74159be4e0f4061c5ac703eb6/yang-mills/z4/fixed-size/STATEMENT.md)

## Physical transfer at one Wilson time step

For fixed $b$ and finite spatial gauge volume, send $P\to\infty$ in the time-homogeneous Wilson law. The positive compact transfer has a simple physical vacuum, and the periodic trace gives $\langle v_b,S_b^j v_b\rangle$ for the centered vacuum vector $v_b$ made by this observable with unit norm. Here $S_b$ is the gauge-invariant transfer divided by its top eigenvalue. Uniformity in $P$ allows the preceding bound to pass to the single-step correlation. Finite-volume expectations of $Y_t,Y_t^2$ converge as well, and the variance stays positive by the uniform estimates above and the positive lower bound on the mean at fixed cutoff. Use a positive temporal coupling and a positive-type Wilson kernel, as for a nonnegative coefficient of the real normalized unitary character. Its Taylor products are positive definite and ensure a nonnegative transfer. [Physical trace at periodic time](../periodic-time/README.md)

Let $a$ denote the physical separation of successive slices and let $\nu_b$ be the spectral probability measure of $v_b$ for the physical log-transfer energy $-a^{-1}\log S_b$. A zero transfer eigenvalue, if present, is assigned infinite energy for these bounds. Since $\int e^{-aE}\,d\nu_b(E)=\langle v_b,S_bv_b\rangle$,
$$
 \nu_b([0,R])\le 3e^{aR}(h_b+\sqrt{q_b}).
$$
In particular for **every** $0<\eta<3/5$,
$$
 \nu_b\!\left([0,(s/b^2)^\eta/a]\right)\longrightarrow0 .
$$
Choose $\eta/3<\sigma<1/5$. Then $1-2\sigma>3\sigma>\eta$, and the two exponentials beat $e^{x^\eta}$ and the polynomial site count. This applies directly with $a=b$ in the original isotropic theory at the stated couplings. The vector is gauge invariant and the energy is in the gauge-transfer clock. A low physical excitation orthogonal to these vectors is compatible with the estimate. Establishing the full vacuum-complement gap, or finding an observable with surviving nonzero finite-energy weight in four dimensions, requires further input.

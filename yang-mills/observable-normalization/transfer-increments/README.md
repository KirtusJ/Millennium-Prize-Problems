# Testing a centered observable with one transfer step

Director A4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For a positive self-adjoint contraction $T$ and a centered vector $F$, set $V=\|F\|^2$, $D=\langle F,(1-T)F\rangle$, and $C_k=\langle F,T^k F\rangle$. The scalar inequality $1-x^k\le k(1-x)$ on $[0,1]$ gives $V-C_k\le kD$ by spectral integration. The companion Lean file checks the scalar and finite spectral sum inequalities. The bounded integrand permits the same argument for any finite positive spectral measure.

At cutoff $n$, let $a_n>0$ be one step in common units. If $V_n\ge v>0$ and $D_n/a_n\le M$, then $C_{k_n}\ge v-tM$ whenever $k_na_n\le t$. Thus a convergent sequence has a strictly positive limit when $tM<v$. The formal limit lemma accepts eventual estimates and varying step counts. Identifying a physical time requires $k_na_n\to t$ as well as convergence of the correlator there. A stationary real observable has $D=\frac12\mathbb E[(F(X_1)-F(X_0))^2]$ when its two-slice law realizes this transfer form, since both marginals have the same second moment. This reduces the upper estimate to an increment of the same observable whose variance provides the lower estimate.

**Comparison with the first-energy-moment test.** Let $a=1/n$, $\mu_n=(1-1/n)\delta_1+(1/n)\delta_{n^3}$ and transfer eigenvalue $x=e^{-aE}$. Then $V_n=1$, $D_n/a\le 2$ by $1-e^{-y}\le\min(y,1)$ for $y\ge0$, while the energy first moment is $1-1/n+n^2$. A common finite energy-form bound is sufficient for the transfer test and can fail when the transfer test succeeds. Both bounds concern the same physical units.

**B4’s sharp first-moment bound.** If total mass is at least $v>0$ and the energy first moment is at most $M\ge0$, the tangent line to $E\mapsto e^{-tE}$ at $M/v$ gives $C(t)\ge v\exp(-tM/v)$ for every $t\ge0$. The single atom $v\delta_{M/v}$ attains equality. Lean checks the finite-sum inequality for arbitrary nonnegative weights. Integrating the same tangent proves the positive-measure version under finite mass and finite first moment on nonnegative energies. This sharp bound applies directly at a time selected by another director. [B4’s derivation and independent replay of the earlier lemmas](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7090815043)

The [single-plaquette action estimate](local-action/README.md) compares unfiltered four-dimensional Wilson covariances uniformly in time and resolves the centered action’s low-energy spectral weight at growing lags.

The [cross-check of Z4’s manuscript](dirichlet-box/README.md) identifies a transfer zero mode and gives quantitative Dirichlet box estimates.

## A uniform estimate in the E2 transfer model

Use E2’s normalized SU(2) central convolution on Haar space. In representation dimension $n$, its eigenvalue is $\lambda_{\gamma,n}=I_n(\gamma)/I_1(\gamma)$ for $\gamma>0$. Write $r_m=I_{m+1}(\gamma)/I_m(\gamma)$, so $\lambda_{\gamma,n}=\prod_{m=1}^{n-1}r_m$. E2 gives $0<r_m<1$ by its integral representation. [K. Justus, E2 §1](https://github.com/KirtusJ/From-Prephysical-Hypotheses-to-Physical-Models/blob/aca29276aa180af3c81ccc9f3aa06b4e2ae4d404/edition/PAPERS/E2_Compact_Group_Transfer_Spectra_and_Ultraviolet_Operator_Limits/source/01_editable_Compact_Group_Transfer_Operators.md) · [NIST DLMF 10.32.2](https://dlmf.nist.gov/10.32.E2)

For $m\ge1$ put $b=m-1/2$. The substitution $u=1-x$ in the integral representation for $r_m$ gives $1-r_m=\mathbb E[u]$ for the probability density proportional to $p(u)=e^{-\gamma u}u^b(2-u)^b$ on $(0,2)$. Integrating $(u p(u))'$ yields

$$\gamma(1-r_m)=b+1-b\,\mathbb E[u/(2-u)] < m+1/2.$$

Both boundary values of $u p(u)$ vanish. The derivative is integrable even at $m=1$, where the worst right-end power is $-1/2$. Summing the factor defects bounds the product defect, as checked in Lean by `productLoss`. For **every** $\gamma>0$ and $n\ge1$,

$$0\le \gamma(1-\lambda_{\gamma,n})\le\sum_{m=1}^{n-1}(m+1/2)=(n^2-1)/2.$$

For $n>1$ the upper inequality is strict at finite $\gamma$. For each fixed $n$ the coefficient is sharp as $\gamma\to\infty$, by the fixed-order Bessel expansion. This bound controls a difference quotient. The logarithmic generator in E2 has different high-index asymptotics. [NIST DLMF 10.40.1](https://dlmf.nist.gov/10.40.E1)

For a fixed vector with squared weights $w_n$ across the isotypic spaces, $\gamma\langle F,(1-T_\gamma)F\rangle$ converges to $\sum_n w_n(n^2-1)/2$ in the extended nonnegative reals. If the sum is finite, use the displayed domination and dominated convergence. If it is infinite, finite partial sums and the pointwise limits make the liminf infinite. This identifies the limiting form domain for **this difference quotient on fixed vectors**. The Bessel calculation and the passage to infinite sums are analytic proofs on this page. The companion Lean file checks the finite transfer algebra, limit interface and exponential tangent.

## A closed-loop observable and a scaling obstruction

Take independent copies of the E2 step on oriented links of a finite spatial lattice, with product Haar equilibrium. On a simple closed loop of $L$ distinct edges, use the fundamental SU(2) character of the ordered holonomy, reversing a matrix on a backwards edge. Site gauge transformations conjugate the holonomy at the basepoint. The holonomy is Haar by integrating any one of the distinct links. Character orthogonality therefore gives mean zero and variance one. Each link enters in the fundamental representation or its dual, on which the central transfer has eigenvalue $r_1$. Expanding the trace into matrix entries gives the **exact** $k$-step centered correlation $r_1^{kL}$. Repeated edges require a different representation decomposition.

Let the step be $a$, the spatial mesh $h$, $ka\to t>0$, and $Lh\to\ell>0$ as $a,h\to0$ and $\gamma\to\infty$. Since $-\gamma\log r_1\to3/2$, the deciding ratio is $Lk/\gamma$. If $\gamma a h\to c\in(0,\infty)$, the correlation tends to $\exp[-3t\ell/(2c)]$. If $\gamma a h\to0$ it vanishes; if $\gamma a h\to\infty$ it tends to one. Thus even a centered gauge-invariant observable with variance exactly one can disappear at fixed physical separation when the loop length grows. The single-link limit gives the wrong prediction if the growing number of links is dropped.

This example sets the spatial plaquette interaction to zero. Matching its scaling by tuning $\gamma$ supplies no scale-setting theorem for four-dimensional Yang–Mills. The outstanding estimate is on the interacting two-slice Wilson law, with the same spatial smearing, renormalization, time step, gauge group and infinite-volume trajectory as the other lanes. A usable transfer comparison must control the variance and increment after inserting the spatial action and vacuum weights, uniformly in volume and cutoff.

[Weight near the gap at one correlation length](gap-weight/) gives the sharp bound on the two-time ratio from raw low-energy weight, a necessary and sufficient test on the half-time law, and the optimal positive temporal smearing over a bounded slab.

[A growing spatial Wilson packet](spatial-packet/) gives a uniform $O(\beta^{-1/8})$ upper bound on the lattice gap in even-periodic limit states and positive spectral weight at energies of that order.

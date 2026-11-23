# Concentration around the electric energy of an edge-simple loop

Use the round $S^3$ metric on each link, $H=-\gamma\sum_e\Delta_e+\lambda\sum_p(1-x_p)$, $\gamma=\kappa/4$, $x_p=\operatorname{Tr}(U_p)/2$, and normalized Haar measure. Periodic cubic boxes of side at least three have four distinct incident plaquettes per link. The unique positive finite-volume ground state is gauge invariant. Denote it by $\Omega$, its energy by $E_0$, and set $g=\lambda/\kappa$. [A4’s Hamiltonian](../../observable-normalization/hamiltonian-variance/) · [D4’s arbitrary-coupling adjoint estimate](../adjoint-band/)

## Remove the plaquettes on one link

Remove the additive constants of the incident faces. The resulting Hamiltonian is $-\gamma\Delta_e+H_{\rm out}+W_e$, where the spectator operator acts only on the other links and $\|W_e\|\le4\lambda$. Each incident trace has zero single-link Haar average even with all spectators fixed. The spectator ground state tensored with the constant in $e$ has average interaction zero, hence $E_0\le\inf\sigma(H_{\rm out})$ in this energy origin. The trial and comparison can both be made upstairs in the full product space, where $\Omega$ is also the ground state.

Let $P_e$ average over the link, $R=I-P_e$, $\delta=\|R\Omega\|$, $K=\|\nabla_e\Omega\|^2$ and $A=-\gamma\Delta_e+H_{\rm out}-E_0$. Then $A$ commutes with $R$ and $AR\Omega=-RW_e\Omega$. Pair with $R\Omega$. The spectral gap of the round sphere is $3$, and the spectator contribution is nonnegative. Thus
$$
 3\delta^2\le K,\qquad \gamma K\le 4\lambda\delta,\qquad
 \delta\le16g/3,\qquad K\le256g^2/3.
$$
This estimate is local in the incident interaction strength. An exterior bounded real potential can be included in $H_{\rm out}$. A4’s translation-invariant product trial also gives $K\le4B$, $B=\min(g,17\sqrt g/8+3/16)$. Write $b_*=\min(B,64g^2/3)$ when using these bounds for the kinetic form. Potential-energy expectations keep their separate trial bound. [A4’s product-trial estimate](../../observable-normalization/hamiltonian-variance/)

## A loop is an approximate eigenvector in the true vacuum

Take an oriented closed loop $C$ with $\ell$ distinct edges. Let $F=\chi_n(U_C)$ be the spin-$n/2$ character, $n\ge1$, $m=\langle F\rangle$, and $f=F-m$. A single incident edge is an isometric coordinate for the total holonomy with the other edges fixed. Its Laplacian contributes $-n(n+2)F$. In the class angle $\theta$, $\chi_n(\theta)=\sum_{j=0}^n e^{i(n-2j)\theta}$, so the one-link gradient has norm at most $L_n=\sum_{j=0}^n|n-2j|$. Continuity covers the two poles. Set $a_C=\gamma\ell n(n+2)$.

The smooth product rule gives $(H-E_0)(f\Omega)=a_CF\Omega-2\gamma\,\nabla_C F\cdot\nabla_C\Omega$. Project off the normalized vacuum. Both $(H-E_0)(f\Omega)$ and $f\Omega$ already lie in its orthogonal complement. The constant remaining after replacing $F$ by $f$ disappears. Cauchy–Schwarz on the $\ell$ edges now gives
$$
 \|(H-E_0-a_C)f\Omega\|
 \le 2\gamma\sqrt{\ell}\,L_n\,(4\ell b_*)^{1/2}
 =\kappa\ell L_n\sqrt{b_*}.
$$
The squared norm is exactly the integral of $(E-a_C)^2$ in the centered vector’s spectral measure. Its ratio to $a_C^2$ is bounded by $16L_n^2 b_*/[n^2(n+2)^2]$. For fixed spin this is $O(g^2)$ uniformly in length and box size. For the variance-normalized law one divides by the variance. The single-link argument below gives a variance bounded away from zero for fixed spin and sufficiently small $g$. Repeated traversals of one edge can change the Laplacian and its cross terms. Edge simplicity is used in this calculation.

For $n=1,2$, the respective real character ranges are $[-2,2]$ and $[-1,3]$. Haar orthogonality on one edge gives $\|(F-m)P_e\Omega\|^2=(1+m^2)\|P_e\Omega\|^2$. The norm of $(F-m)R\Omega$ is at most $4\delta$. The triangle inequality therefore gives $\|f\Omega\|\ge1-5\delta$. For general fixed $n$, replace $4$ by the oscillation of $\chi_n$.

If $g\le\sqrt3/512$, then $b_*\le1/4096$ and $\delta^2\le4b_*/3$, hence $\delta\le1/54$. For $n=1$ take a radius $a_C/6=\kappa\ell/8$. For $n=2$ take $a_C/8=\kappa\ell/4$. In either case the mass outside the closed interval of that radius about $a_C$ is at most $256b_*\le1/16$ by the second moment about $a_C$. The inside mass is at least $(49/54)^2-1/16>3/4$. For a plaquette $\ell=4$ this gives the two intervals on the [main page](README.md). The estimates use no perturbation expansion or global gap hypothesis.

## Three readings in physical time

For a fundamental plaquette set $u=2^{-E/\kappa}$ and $q=1/16$. On its core band $5\kappa/2\le E\le7\kappa/2$ one has $1/12\le u\le1/4$ and $(u-q)(1-u)\ge1/64$. Elsewhere on $[0,1]$ this multiplier is at least $-1/16$. The three-reading excess is its integral, at least $(3/4)/64-(1/16)/16=1/128$. The same proof on any edge-simple loop uses $\tau=4\log(2)/(\kappa\ell)$ and tests a candidate energy $\kappa\ell$. This length-dependent clock is fixed for each chosen loop. When comparing different cutoffs in one physical time unit, the clocks must be converted explicitly. [Exact window and error propagation](FiniteReadings.lean) · [One-cycle numerical controls](check_loops.py)

The three strictly positive readings at $\tau,2\tau,3\tau$ also suffice for a plaquette. Their combination $-C_3+(17/16)C_2-C_1/16$ integrates $u(u-q)(1-u)$. On the core this is at least $1/768$. For $u<q$ the adverse magnitude is at most $u(q-u)\le q^2/4=1/1024$. The measured combination is therefore at least $15/16384$. More generally the detector shifted by $j$ steps is at least $(3/256)12^{-j}-(1/256)16^{-j}$ for each integer $j\ge0$. These are absolute signal floors for the same physical clock. [Proof of the positive-time arithmetic](FiniteReadings.lean)

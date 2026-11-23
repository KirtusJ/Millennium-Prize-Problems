# Locality for bounded electric and magnetic observables

The loop estimate implies a propagation bound for **every bounded operator supported on a finite set of links**. This includes spectral projectors of the electric Casimir, with no dependence on the spin threshold. Two cuts of the Hamiltonian suffice. The speed stays the same. The prefactor and its allowed growth under refinement depend on which observables are used.

Let $X,Y$ be nonempty disjoint link sets, $r$ their least midpoint separation. Let $J_X,J_Y$ be the sets of faces touching them; $|J_X|\le4|X|$, $|J_Y|\le4|Y|$. Operators supported on $X$ or $Y$ act on the full product link space with identity on its complement. Gauge-invariant such operators can subsequently be restricted to physical vectors. Denote the speed exponent by $h=\sqrt{2\kappa\lambda S K(\mu)}$.

**One cut.** For a normalized trace word $F$ on $X$ of length $\ell_F$ and an arbitrary bounded $B$ on $Y$,
$$
 \|[\tau_t(F),B]\|
 \le 2\|B\|\kappa\lambda |J_Y|\ell_F S |t|^2
         e^{-\mu(r/b-1)+h|t|}.
$$
Delete every face touching $Y$. The resulting Hamiltonian separates the links in $Y$ from their complement, so the corresponding evolved $F$ commutes exactly with $B$. Each removed face is at midpoint distance at least $r-b$ from $X$, since any two midpoints on a face are at distance at most $b$. Apply the boundary comparison and the norm inequality for the commutator with the difference. This also works if some interactions have already been deleted.

**Two cuts.** For any bounded $A,B$ on $X,Y$, respectively, and $r>b$,
$$
 \boxed{
 \|[\tau_t(A),B]\|
 \le \tfrac{16}{3}\|A\|\|B\|\,\kappa\lambda^2 S
 |J_X||J_Y|\,|t|^3\; e^{-\mu(r/b-2)+h|t|} .\ }
$$
Again delete $J_Y$, calling the new Hamiltonian $H'$. Comparing the time evolutions by Duhamel costs at most
$\lambda\sum_{p\in J_Y}\int_0^{|t|}\|[\tau_s^{H'}(A),\operatorname{Re}\operatorname{tr}U_p]\|\,ds$.
This integral estimate is valid for arbitrary bounded $A$ by passing to the interaction picture for a bounded perturbation and integrating on vectors. Commuting the resulting difference with $B$ costs $2\|B\|$. By unitary time reversal, the integrand is the commutator of $A$ with the evolved four-letter loop at $p$. Its links are disjoint from $X$ because $r>b$. Apply the one-cut estimate inside $H'$, now cutting at $X$; the distance from $p$ to $X$ is at least $r-b$. Integrating $s^2$ gives the factor $1/3$. The argument works for either sign of $t$, and for arbitrarily many additional missing faces.

In bare $SU(2)$ units the one-cut prefactor uses $\kappa\lambda=2/b^2$ for every $\beta>0$. The two-cut prefactor uses $\kappa\lambda^2=2\beta/b^3$. For polynomial support sizes and norms and $\log^+\beta=o(1/b)$, the commutator of arbitrary bounded observables therefore tends to zero outside the same physical cone. Every polynomial or logarithmic growth law for $\beta$ is included. The loop-to-bounded result has no growth restriction on $\beta$ for the factor $\kappa\lambda$. Arbitrarily fast growth of $\beta$ can overwhelm the general two-cut prefactor, and no limit estimate in that case follows here. At fixed mesh the same argument with a cubical boundary also gives convergence in norm at each fixed time of the finite-volume dynamics on any bounded local operator. It suffices to sum the one-cut estimate for boundary loops against the local operator. On-site free evolution on the full bounded-operator algebra need only be strongly continuous.

These are operator-norm statements on the Hamiltonian regulators. Their vacuum transfer through Wilson time for nonsmooth electric operators separately requires control of the Hamiltonian form energies of intermediate vectors. The [Wilson comparison](wilson-real-time.md) gives the criterion for such vectors.

As an adverse test of the time powers, replace both loop multipliers in the unrestricted abelian chain control by the bounded electric translations $f(\theta_j)\mapsto f(\theta_j+\pi)$, diagonal on Fourier modes with sign $(-1)^{n_j}$. At distances 1, 2 and 3 the first nonzero commutators on the constant vector occurred at orders 1, 3 and 5. Their integer coefficient $\ell^1$ norms were 8, 64 and 512. In particular a uniform cubic startup at distance one would already fail in this control model. [Exact Fourier calculation](checks.py)

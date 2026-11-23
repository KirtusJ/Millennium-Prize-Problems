# Independent check of the Wilson readings in A4's stress-tensor test

Director B4 · source reviewed at A4 commit [ad7901c](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/ad7901cc3ed9db23f3f4c2d4a91a7c1083da9175/yang-mills/observable-normalization/energy-density/lorentz-test)

The three Wilson readings are admissible at each fixed physical resolution used by A4. They can also be realized for all dyadic resolutions on a **single sequence of periodic Wilson measures**, with the same clock for the electric and magnetic pieces. Identifying the limiting correlations with the stated covariant continuum stress tensor is an additional assumption.

Write $D=2^i$ for the spatial dilation, $b$ for the spatial lattice spacing, $z_b$ for the prefactor and $\varphi_D(x)=\varphi(Dx)$. This $D$ is independent of the number of lattice sites per edge. For padded support and $bD\le1$, substituting the support size $\ell/D$ and Lipschitz bound $D\|\nabla\varphi\|_\infty$ into the finite-mesh first moment gives
$$
 M_1(z_b\varphi_D)\le A_\varphi |z_b/b^2|^2/D .
$$
The positive polynomial $e^{-u}(1-e^{-u})^2\le u$ then gives the Hamiltonian triple at $t=1/D$ a ceiling $A_\varphi |z_b/b^2|^2/D^2$. Vacuum centering makes no difference to this polynomial. On a covariant band, $F(E/D)$ is bounded below on $D\le|\mathbf k|\le2D$ for $D\ge\sqrt{s_{\max}}$. The spatial integral of $|\mathbf k|^4|\widehat{\varphi_D}|^2$ contributes a factor $D$ and the $1/(2E)$ costs at most a factor $6D$ in its denominator. This confirms the incompatible dilation dependence given the stated shell law and a positive coefficient on a bounded band. [A4's fixed-resolution argument](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/ad7901cc3ed9db23f3f4c2d4a91a7c1083da9175/yang-mills/observable-normalization/energy-density/lorentz-test/README.md)

To realize the measurements, take a sequence of boxes with $b_s\downarrow0$ and the required support padding. Choose an increasing finite family of dilations at index $s$ with $D\le1/b_s$ and eventually including each fixed $2^i$ (in fixed reference units). In each box the coupling and every weight are finite. Halve $a_s$ until every $n_{s,D}=1/(Da_s)$ in the family is an integer at least four, using a dyadic spacing small enough for the largest $D$. Keep halving until each uncapped vacuum comparison is at most $2^{-s}$. All times and weights are fixed during this finite inner search. Increase a single even period $P_s$ and a single Haar cell resolution until the thermal and integration errors are each at most $2^{-s}$ for every member. Each estimate then compares the same periodic measure's readings at $n_{s,D},2n_{s,D},3n_{s,D}$ to the corresponding Hamiltonian triple with error at most $3\cdot2^{-s}$. For centered energy the unsubtracted history formula works directly because the vacuum constant cancels in the vacuum polynomial. In a normalized thermal trace, a scalar shift of either insertion adds a time-independent term which the same coefficients cancel.

At each fixed $D$, the cutoff errors vanish before sending $D\to\infty$. The schedule does not establish Wilson/Hamiltonian matching for an arbitrary preassigned aspect ratio or a fixed numerical table. For example, a unit spectral atom at energy $D$ has triple $e^{-1}(1-e^{-1})^2$ at $t=1/D$. If $aD>1$, flooring the first spacing gives $n=0$ and its three repeated readings cancel. Even when $n\ge1$, rounding the three target times separately can destroy the exact polynomial identity. The common dyadic clock avoids both errors. The time continuum in this comparison is the anisotropic Hamiltonian-matched Wilson regulator; transferring the test to a prescribed isotropic regulator requires a separate matching argument. [Uncapped comparison](graph-norm.md) · [Periodic trace and error bounds](measurements.md)

I also recompiled A4's 14 printed declarations against the pinned Lean 4.19.0/Mathlib and reran the shell-control script. The maximum matrix residual was $6\times10^{-15}$, and its massive stress reading at dilation 64 was 1.095441010 against 1.095531582 for the massless control. The formal module supplies particular scalar, integral and limiting steps. The statement about the stress tensor remains conditional on the spectral hypotheses in A4's note, including the open-null-shell law. [A4's formal scope](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/ad7901cc3ed9db23f3f4c2d4a91a7c1083da9175/yang-mills/observable-normalization/energy-density/lorentz-test/execution.md)

## Unequal weights on the electric and magnetic terms

The obstruction survives a controlled difference between the two renormalization coefficients. More generally let each energy term have coefficient $z_{i,b}$, take a reference $z_b$ (for instance the electric coefficient), and write $\theta_b=\sup_i|z_{i,b}-z_b|$. Sample at $y_i$ with $|y_i-x_i|\le r b$ for a fixed $r\ge0$. Set $w_i=z_{i,b}\varphi(D y_i)$. Allow arbitrary dependence of the coefficient errors and the displacements on the term and the box. Assume the box contains the enlarged support and its neighbors, the spatial side has at least three sites, $bD\le1$, and the finite-box bare matching and $\beta\ge1$ conditions of A4's first-moment estimate hold.

For any neighboring pair the sampling points are at most $(1+2r)b$ apart. Decomposing the weights into their common coefficient and the two remainders gives
$$
 |w_i-w_j|\le |z_b|(1+2r)bD\|\nabla\varphi\|_\infty
                         +2\theta_b\|\varphi\|_\infty .
$$
Charge each active unordered pair to one endpoint carrying a nonzero weight. At most $6(\ell/(bD)+2+2r)^3$ endpoints are possible and each has at most sixteen neighbors. The absolute off-diagonal first moments are at most $25/b^3$. A4's exact first-moment difference formula, followed by the filter inequality $F(E/D)\le E/D$, now gives
$$
 0\le D_H(1/D)\le 2400(\ell+2+2r)^3
 \left[
 \frac{|z_b|(1+2r)\|\nabla\varphi\|_\infty}{b^2 D}
 +\frac{2\theta_b\|\varphi\|_\infty}{b^3 D^2}
 \right]^2 .
$$
This uses the row-sum conservation identity even though the differently weighted sum itself need not be conserved. The unequal coefficients enter before the square; the mixed term must be retained. The scalar calculation is checked in Lean. [First-moment support and row sums](../../observable-normalization/energy-density/README.md) · [Mesh bound](../../observable-normalization/energy-density/spatial-limit.md) · [Lean dilation estimate](PeriodicTime.lean)

If both $|z_b|/b^2$ and $\theta_b/b^3$ remain bounded on one subsequence, the right side vanishes when one takes the cutoff limit there at each fixed dyadic $D$ and then lets $D$ grow. Under A4's positive covariant shell identification, this excludes positive-energy vacuum stress weight, including the open null shell. It covers independent electric and magnetic coefficients whose difference is $O(b^3)$ when their common scale is $O(b^2)$, with arbitrary bounded mesh-scale displacements of their sampling centers. A nonzero stress limit along the full sequence requires $\max(|z_b|/b^2,\theta_b/b^3)\to\infty$. Exceeding this necessary scale alone gives no positive signal. For growing numerical resolution the measured floor and the explicit cutoff errors have to be compared at that resolution.

For the prefactor powers there is a simple adverse control on using the first-moment information alone. Place two coincident term types in each mesh cell and use a first-moment matrix with independent two-by-two blocks $b^{-3}\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)$. It is positive semidefinite, local and has zero row sums. Opposite coefficient perturbations of magnitude $\theta_b$ give exactly $4b^{-3}\theta_b^2\sum_x|\varphi(Dx)|^2$. For fixed $D$, ordinary Riemann summation makes this asymptotic to $4(\theta_b/b^3)^2 D^{-3}\int|\varphi|^2$. Thus an $O(b^2)$ difference alone cannot yield a uniform first-moment bound from those structural estimates. This example tests the inference from the matrix assumptions; the actual Wilson matrix may satisfy stronger cancellations.


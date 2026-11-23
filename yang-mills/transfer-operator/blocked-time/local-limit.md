# The joint local limit and its range in physical units

Fix the spatial mesh, $\kappa>0$ and $0\le z=\kappa\lambda\le1/384$. Use the link metric, time normalization and open temporal slabs in the [blocked transfer proof](README.md). For bounded local multiplication observables at a fixed finite list of physical times, the difference between normalized Wilson and Hamiltonian vacuum correlations at the same spatial volume is **$O(a^{1/3})$ uniformly in the side length**, in fixed time units. Both have the same thermodynamic local correlations along any $a\downarrow0$, $L\to\infty$. The constants may depend on the observables, their time separations, the couplings and the spatial mesh. Full finite-volume spectra above the lower gap bound are outside this comparison.

## Removing a distant spatial boundary

Anchor every positive spatial edge at its initial vertex. In a large torus let the inside consist of the edges whose anchors belong to an embedded cube. Remove the magnetic plaquette factors with both inside and outside edges. The resulting lifted measure factors across the cut. All one-link endpoint and bridge reference laws remain the same. Inside, spatial plaquettes entirely contained in the edge set retain their Wilson factors. The resulting open spatial system is identical in any larger box containing this cube with at least one layer of padding. This comparison on the unrestricted link space avoids imposing a gauge condition at the artificial boundary.

For the single-site Dobrushin comparison with the original measure as reference, each difference of conditional laws has total variation at most one, and vanishes unless the site touches a removed plaquette. The reference influence matrix has unweighted row sum at most $q=647/960$. Across one influence step the sup-norm distance between spatial anchors is at most one, also for opposite sides of a face. If every site of an observable is at graph distance at least $d$ from the boundary discrepancy, the first $d$ terms of its comparison series vanish. Every remaining row sum is at most $q^k$ in term $k$. Hence for a bounded real observable $A$,
$$
|\mathbb E A-\mathbb E_{\rm cut} A|
\le \Big(\sum_i\delta_i A\Big)\frac{q^d}{1-q}.
$$
The constants are independent of the number of temporal slabs. Taking open ends to infinity gives the same estimate for the vacuum expectation. The cut system also has a strictly positive finite-volume ground state. Alternatively one may compare two *uncut* tori through the common cut integral in finite time and then send their ends to infinity together. [Finite-propagation lemma](BlockedTime.lean) · [Comparison theorem](https://web.math.princeton.edu/~rvan/dobrushin130819.pdf)

For a fixed local product of insertions, each observed edge at an interior fine time uses only its two adjacent block endpoints and its outgoing bridge seed, grouped with the left endpoint. Thus its lifted dependence uses at most two sites per occurrence of an edge. Its sum of site oscillations is bounded by twice this support count times the product of the insertion norms. The bound is uniform in the time step, even when an insertion moves across a block boundary. For complex insertions apply the estimate to real and imaginary parts. At distinct observation times use actual fine-slice positions $\lfloor t_i/a\rfloor$; changing an interval step count by one is included in the time-rounding estimate for positive separations. Combine equal-time multiplication operators before rounding.

In particular, if the observed spatial anchors are in a cube of radius $r$ and the cutting cube has radius $r+d+2$ in lattice units, two tori containing the cut cube with padding have correlation difference at most $2(\sum_i\delta_i A)q^d/(1-q)$. On the fixed pair of tori this inequality is independent of $a$. Their finite-volume time-cutoff convergence transfers it to the Hamiltonian correlations as well. Thus each family has a thermodynamic local limit, and the spatial truncation error is uniform in the time step. [Fixed-volume convergence including vacua](../joint-cutoff/README.md)

## Uniform time error for a fixed observable

Choose a periodic reference cube of side $O(r+d+1)$ large enough to contain the common cutting cube and its padding. Compare a larger torus through the cut with this reference torus, on each of the two sides of the time limit. For smaller tori compare Wilson and Hamiltonian directly there. All direct finite-volume comparisons now have spatial side $O(r+d+1)$.

On any such torus use $c=6\lambda L^3+6/\kappa=O((1+d)^3)$. The uniform physical gap of the Hamiltonian is at least $4\log3/(13\kappa)$. The finite-volume bound on the vacuum vector error is therefore $O(ac^2)$ whenever $ac^2$ is sufficiently small. For a fixed positive time lag $t$, the norm error for the normalized evolution is $O_t(a^{1/3}+ac^2+a c)$: use $k=\lceil(t/a)^{1/3}\rceil$ in the explicit finite-volume inequality. Choosing individually rounded times only changes the time-lag estimate by $O_t(a+ac)$. Telescoping the finitely many factors, and adding the spatial truncation error, gives
$$
|C_{a,L}-C_{H,L}|\le C\,[q^d+a^{1/3}+a(1+d)^6]
$$
for sufficiently small $a$ relative to $d$. Take $d=\lceil\log(t_0/a)/|\log q|\rceil$ for any fixed time unit $t_0$ and $a<t_0$. Then $q^d\le a/t_0$, $a(1+d)^6=o(a^{1/3})$, and all low-energy and vacuum small-step conditions eventually hold. This proves the stated rate and arbitrary-path convergence. For any fixed bounded operators this argument requires spatial localization as specified above. Extensive insertions, time separations shrinking to zero and whole-volume norm-resolvent convergence need their own estimates. [Finite-volume evolution error](../joint-cutoff/evolution.md) · [Eigenvalue and vacuum estimates](../joint-cutoff/README.md)

## A nonvanishing excitation at fixed mesh and an obstruction on refinement

Let $F$ be the fundamental trace around one fixed plaquette. In the Hamiltonian vacuum, its centered variance is at least $5/9$ and its energy divided by its variance is at most $12/\kappa$ throughout this coupling interval. Jensen's inequality for the normalized centered spectral measure gives
$$
C_{H,L}^{\rm conn}(t)\ge C_{H,L}^{\rm conn}(0)e^{-12t/\kappa}.
$$
The joint local limit preserves both sides. Thus the limiting connected plaquette correlation is at least $(5/9)e^{-12t/\kappa}$ at each fixed $t>0$. In each Wilson box it is also bounded above by its equal-time variance times $\exp[-a\lfloor t/a\rfloor\,\Delta_{a,L}]$. Along every fixed-coupling joint path, the variance converges to a positive value, so
$$
\frac{4\log3}{13\kappa}\le\liminf\Delta_{a,L}\le\limsup\Delta_{a,L}\le\frac{12}{\kappa}.
$$
This local argument gives upper and lower limits for the first gap, without identifying an actual limit of those gaps. [Plaquette variance and Dirichlet energy](../hamiltonian-time/README.md)

Now let a spatial mesh $b\downarrow0$ and take the bare tree-level parameters $\kappa=\beta b$, $\lambda=\beta/b$. If $0<\beta^2\le1/384$ and $a\le\kappa/4$, the lower gap in the original physical clock diverges at least as $4\log3/(13\beta b)$, for arbitrary spatial volumes. For centered vectors of norms with product at most $M_b$, the separated normalized matrix element is at most $M_b\exp[-(t-a)4\log3/(13\beta b)]$. In particular it tends to zero if $\log^+M_b=o(1/(\beta b))$. This includes polynomial normalizations in $1/b$. It rules out surviving finite-positive-energy weight for uniformly norm-bounded centered states along this particular interacting trajectory. The time-zero law and contact terms require separate analysis. The weak bare-coupling trajectory $\beta\to\infty$ falls outside the estimate. Nontrivial continuum existence, Euclidean covariance and a positive finite physical mass there remain open. [Jaffe–Witten problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

### A spatial obstruction even if the clock is changed

The spatial influence estimate also has a consequence independent of how elapsed time is rescaled. For insertions whose physical spatial supports are at periodic distance at least $\ell>0$, their lifted sites are separated by at least $\ell/b-O(1)$ lattice steps (using physical sup-norm distance). On the small-coupling interval the connected covariance is bounded by a site-oscillation prefactor times $q^{\ell/b-O(1)}$ at **all** fine-time separations. A prefactor growing as $\exp(o(1/b))$ cannot compensate. This includes spatial smearings using polynomially many bounded local insertions and polynomial renormalization factors. The same conclusion holds for the faithful-character range with $q=2/3$.

Suppose along such a refinement the connected two-point distributions of a translation-invariant probe converge, with the above prefactor control on tests of disjoint spatial support, and suppose the limit is a Euclidean scalar. Its difference distribution is supported on the time axis, since it vanishes when the spatial supports are separated. Rotation invariance then places its support in the intersection of the rotated axes, which is the origin. Only contact terms can survive for that scalar probe. This extends the earlier free-plaquette rotation test to an interacting interval and holds even under a change of clock. It does not identify an individual oriented plaquette as a continuum scalar, or exclude other trajectories or observables outside the oscillation bounds. [Earlier uncoupled calculation](../hamiltonian-time/README.md)

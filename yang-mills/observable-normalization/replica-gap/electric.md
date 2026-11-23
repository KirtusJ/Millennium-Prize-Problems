# A volume-uniform thermal estimate on the four-dimensional Wilson lattice

Let space be the nearest-neighbor cubic torus of side $L\ge5$, $V=L^3$, and time periodic with $N$ steps. Use temporal Wilson coupling $\gamma>0$ and spatial coupling $\sigma\ge0$, with plaquette action $\beta(1-\tfrac12\operatorname{Tr}U_p)$. Normalize the one-link kinetic kernel to preserve constants. At $\sigma=0$ the full physical transfer $K$ is the product of the temporal convolutions restricted to local gauge invariants. Write

$$
 \rho_m=I_{m+1}(\gamma)/I_1(\gamma),\quad u=\rho_1,\quad v=\rho_2,\quad r=u^4.
$$

On a spin network whose edge labels are twice their spins, the eigenvalue is $\prod_e\rho_{m_e}$. The one-link character integral gives the stated ratios. Strict Bessel Turán inequalities give $\rho_m\le u^m$ by multiplying successive quotients, strictly for $m\ge2$. Also $0<u<1$ since $u$ is the mean scalar part of the increment under its tilted Haar law. [Parent-program one-link spectrum and references](../../transfer-operator/) · [Baricz and Ponnusamy, §1](https://arxiv.org/pdf/1010.3346)

A vertex with a single nontrivial incident representation has no invariant tensor. Every nonempty support therefore contains a cycle. The girth is four, and its four-edge cycles are exactly the $3V$ elementary plaquettes. A length-four walk cannot wind on this torus. A bivalent cycle forces the same spin on every edge and has one intertwiner state. Hence the full dimensionless gap is $-\log r$ and its multiplicity is exactly $3V$. The orthonormal eigenfunctions at $r$ are the unnormalized fundamental characters around the individual squares. The calculation covers all winding sectors. Shorter periodic sides can change the conclusion. [B4's girth and isotropic strong-coupling bound](../../transfer-operator/connected-rectangles/gap.md)

## Uniform pressure with an explicit remainder

Put $y=u^N$ and $w=y^4$. Use the electric normalization $Z_{0,N}=\operatorname{Tr}_{\rm phys}K^N$. Uniformly in $L\ge5$ and $\gamma>0$ as $y\to0$,

$$
 \log Z_{0,N}=3V y^4+O(V y^5).
$$

To see the upper bound, decompose a nonzero spin assignment into its vertex-connected components. Gauge dimensions and eigenvalue weights factor over vertex-disjoint supports. On $k$ edges the multiplicity for fixed labels is bounded by the entire product link representation dimension $\prod_e(m_e+1)^2$. The total activity for a fixed connected support is therefore at most $\tau^k$ with $\tau=\sum_{m\ge1}(m+1)^2 y^m=(1+y)/(1-y)^3-1$. There are at most $V\,36^k$ connected supports of size $k$, since a walk of length $2k$ can traverse the doubled support. Keeping every component independently only increases the positive sum, and $\log(1+a)\le a$. For a square, keep its exact fundamental activity $w$ and use the multiplicity-one cycle bound for higher spins. This gives

$$
 \log Z_{0,N}\le 3Vw+\frac{3V y^8}{1-y^4}
              +V\frac{(36\tau)^5}{1-36\tau},\qquad 36\tau<1.
$$

For the lower bound keep only vertex-disjoint fundamental squares. Each square conflicts with at most 48 others. Insert the $3V$ candidate squares one at a time. At any intermediate stage the occupation probability of a specified square is at most $w/(1+w)$, as follows by deleting that square. A union bound gives a partition multiplier of at least $1+w(1-48w)$. Its logarithm is $w+O(w^2)$ for small $w$, uniformly in the stage and the box. This proves the matching coefficient.

With $p_{\sigma,N}=Z_{\sigma,2N}/Z_{\sigma,N}^2$, the consequence at the electric endpoint is

$$
 -\log p_{0,N}=6V y^4(1+O(y)),\qquad
 \frac{\log p_{0,2N}}{\log p_{0,N}}=u^{4N}(1+O(y)).
$$

Both relative error statements remain valid for arbitrarily growing spatial volume. They recover the already identified full gap through an intensive quantity in this model. Langelage, Münster and Philipsen obtained the leading glueball contribution to the isotropic finite-temperature pressure and higher terms in its small-coupling series. Their Eq. (30) resolves one scalar and two tensor polarizations. Here the volume estimate is for arbitrary temporal coupling in the electric model and an explicitly shrinking magnetic neighborhood. [Strong coupling expansion for finite temperature Yang–Mills theory, §3.1](https://arxiv.org/pdf/0805.1163)

## Restoring the magnetic coupling

On an original periodic electric history multiply each spatial link column (one oriented spatial edge at every time) by its own common independent center sign. Each temporal face is unchanged and Haar measure is invariant. For a base history write $x_p(t)=\tfrac12\operatorname{Tr}U_p(t)$. Under these signs the random spatial sum $X=\sum_{p,t}x_p(t)\prod_{e\in\partial p}\epsilon_e$ has mean zero, as each square uses four distinct edges. Changing one sign alters at most $4N$ terms by at most two each. Reveal the $3V$ independent signs in order. Each centered martingale increment has conditional range of length at most $8N$. The exponential bound for a centered variable of range $c$ is $\exp(s^2c^2/8)$, and iteration gives $\mathbb E_\epsilon e^{\sigma X}\le\exp(24VN^2\sigma^2)$. Jensen gives a lower bound of one. Averaging over the original history proves

$$
 0\le H_N=\log Z_{\sigma,N}-\log Z_{0,N}+3VN\sigma
 \le 24VN^2\sigma^2.
$$

The deterministic action constant cancels when forming the purity. Its logarithmic change is $H_{2N}-2H_N$, of magnitude at most $96VN^2\sigma^2$. Consequently, for $y\to0$ and $N\sigma=o(y^4)$,

$$
 \frac{\log p_{\sigma,2N}}{\log p_{\sigma,N}}
  =u^{4N}\left[1+O(y)+O(N^2\sigma^2/y^8)\right].
$$

This estimates positive-coupling thermal partitions uniformly in volume. An additional way to test the actual spectrum is useful at fixed volume. With spatial half-weight $M$, the physical transfer $MKM$ has the same nonzero eigenvalues as $K^{1/2}M^2K^{1/2}$. In quadratic form order the latter is between $e^{-6V\sigma}K$ and $K$. The min–max principle then bounds $|\Delta_{\sigma,L}-\Delta_{0,L}|\le 6V\sigma$. At fixed $L,\gamma$, the [degenerate perturbation calculation](band.md) gives the exact quadratic response and its sign. Neither the pressure perturbation nor the min–max estimate by itself controls the interacting continuum spectrum at fixed physical scales.

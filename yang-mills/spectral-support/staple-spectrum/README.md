# Energy and momentum of a squared temporal-link insertion

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00) · Millennium Prize Problems, Yang–Mills

A4's squared temporal-link observable has an explicit limiting energy–momentum measure in lattice units on **every** joint weak-coupling, large-spatial-box trajectory of the original isotropic four-dimensional SU(2) Wilson vacuum. For total spatial momentum $Q$ in $[-\pi,\pi]^3$, its limiting intensity fills the interval
$$
\left[\omega(Q),\;2\operatorname{arcosh}\!\left(4+\sum_{j=1}^3\cos(Q_j/2)\right)\right],
\qquad \omega(k)=2\operatorname{arsinh}\!\left(\sqrt{\sum_j4\sin^2(k_j/2)}/2\right).
$$
There is one exception on the momentum torus. At $Q_c=(\pi,\pi,\pi)$ the entire fiber vanishes. The intensity recovers quadratically with distance from $Q_c$. A wide spatial packet with alternating signs in all three directions isolates this zero. After multiplying the adjacent-slab reading by the squared width, the limiting spectral weight reappears and has a strictly positive **lattice** threshold $\operatorname{arcosh}7$. [Momentum support and packet experiment](momentum.md)

With momentum integrated out, the support is $[0,E_*]$, $E_*=2\operatorname{arcosh}7$. The adjacent-slab measure has a density proportional to $E^7$ at zero and to $(E_*-E)^2$ at the upper edge. Both coefficients are determined below. At any spacing tending to zero, the fraction of this vector's adjacent-slab norm with bounded physical energy tends to zero. A4's positive-physical-time gamma law on selected trajectories weights a different part of this same measure. A construction with a nonzero renormalized interaction and a positive physical mass gap remains open. [Two energy edges](edges.md) · [A4's source and trajectory selection](../../observable-normalization/energy-density/staple-response/positive-time.md)

## Which finite Wilson measure converges?

At a temporal link let $W$ be the six incident scaled actions minus their conditional mean given all other links. In the vacuum on the periodic spatial torus let $B$ be the one-slab insertion of $W^2$ with the same normalization as the transfer $S$, let $v=B\Omega-\langle\Omega,B\Omega\rangle\Omega$, and let $U(r)$ translate the slice by $r$. For $n\ge1$ the connected Wilson reading between links at $(0,0)$ and $(n,r)$ is
$$
 C(n,r)=\langle v,S^{n-1} U(r)v\rangle .
$$
Indeed the two selected temporal links belong to different slabs and never share a face. Conditional on the joint exterior their Boltzmann weights factor, including when the slabs touch. Replacing each square by its conditional second moment preserves the double insertion. The spatial boundary at a shared time is integrated just once, with both half-weights. Reflection through the middle of a slab takes each temporal path to its inverse, preserves the six-trace expression and exchanges the half-weights. Hence the two end insertions are adjoints. There are $n-1$ ordinary transfer steps between them. At $n=1,r=0$ the connected reading is precisely $\|v\|^2$. The equal-link fourth moment is a different Wilson integral. [Two adjacent conditional Haar integrations and offset control](execution.md) · [Lüscher, positive Wilson transfer (1977)](https://doi.org/10.1007/BF01614090)

Let $x\in[0,1]$ be the eigenvalue of $S$ and take spatial characters $e^{iQ\cdot r}$. The commuting transfer and translations define their joint positive measure in $v$. Multiply this measure by $\beta^4$. Its masses and mixed moments $x^{n-1}e^{iQ\cdot r}$ are exactly $\beta^4 C(n,r)$. We take $\beta,L\to\infty$ with the vacuum selected at each finite spatial side $L$. For each fixed $(n,r)$, A4's uniform $L^2$ expansion of the conditional variance reduces the covariance to the two local staple deficits divided by $48^2$. C4's jointly rooted fixed-patch tangent law and uniform action moments apply at these two translates, including separated spatial sites. The scalar products within a deficit are invariant under a common color rotation at its base. Wick contraction in three colors gives
$$
 \lim\beta^4 C(n,r)=\|K(n,r)\|_F^2/1536.
$$
$K$ is real in position space. Translation multiplies A4's one-color electric Fourier symbol by the character of $r$. These are fixed-lattice inputs, with no growing-patch rate assumed. [A4's deficit expansion](../../observable-normalization/energy-density/staple-response/) · [C4's microscopic input](../../central-quotients/tangent-curvature/)

A4 subsequently constructed a bounded even reading of the six ordinary plaquette traces with exactly the same one-slab insertion at every cutoff. It gives the same translated vectors, momentum packets and positive-time normalizations in these results. The raw equal-link variance depends on the choice of reading. [A4's Abel reconstruction at fae562d](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/fae562d68b51a8f6ec475c85cc239d9655801bc3/yang-mills/observable-normalization/energy-density/star-reconstruction)

## The positive joint measure

Write $dk$ for normalized Haar measure on the momentum torus. Set $p_j=e^{ik_j}-1$, $A=p^*p$, $h=\sqrt{A/(4+A)}$, and $R=I-pp^*/A$ for $A>0$. The $6\times3$ matrix $D(k)$ has entries $-1,e^{-ik_j}$ in column $j$ on its two signed face rows. Put $B(k)=h(k)D(k)R(k)D(k)^*$, taking $B(0)=0$. Here $B(k)$ denotes the Fourier matrix of the tangent covariance. The transfer insertion $B$ above acts on a different space. A4's kernel is $K(n,r)=-\int e^{ik\cdot r-n\omega(k)} B(k)\,dk$. Complex conjugation at $-k$ makes every entry of this integral real.

Use $l=Q-k$, $E=\omega(k)+\omega(l)$ and
$$
 F(k,l)=\frac{h(k)h(l)}{1536}
 \big\| R(k)\operatorname{diag}(1+e^{iQ_j})\overline{R(l)}\big\|_F^2.
$$
In the squared position-space kernel the two Fourier phases add. The entrywise product sums to $\operatorname{tr}(B(k)\overline{B(l)})$, and $D(k)^*\overline{D(l)}=\operatorname{diag}(1+e^{iQ_j})$. Factoring both transverse projections gives the displayed nonnegative weight. The joint limit is the image of
$$
                  e^{-E}F(k,Q-k)\,dk\,dQ
       \quad\text{under}\quad (k,Q)\longmapsto(Q,x=e^{-E}).
$$
The factor $e^{-E}$ is fixed by adjacency. Testing against $e^{iQ\cdot r}x^{n-1}$ reproduces each measured limit, starting with the total mass $c(1)>0$. Trigonometric polynomials in $Q$ times polynomials in $x$ are a conjugation-closed algebra that separates points of the compact product and contains constants. Uniform approximation and the bounded masses give weak convergence of the complete sequence. In particular no limiting mass is lost at $x=0$. Only the spatially integrated finite-time moments are needed for the scalar reconstruction theorem checked in Lean. [Formal source and coverage](execution.md)

The formula gives a canonical momentum disintegration tested with continuous functions of energy, by dominated convergence in $k$. On finite spatial tori the assertion gives convergence after momentum testing. It supplies no pointwise convergence of the weight of a single Fourier mode of the regulator. All observables here belong to the original Wilson measure; the limiting measure was derived using the Gaussian fixed-patch tangent. [Precise momentum conclusions](momentum.md)

## Zero total momentum and comparison with published work

A wide **untwisted** finite packet realizes the zero-momentum energy density. Its large-lag reading is $1/(2048\pi^2 n^5)$ to leading order. On a common selection of original Wilson regulators, positive-time energy weighting gives a gamma law of shape five for this packet and shape eight for the point insertion. [Derivation, order of limits and constants](zero-momentum.md)

The use of two transverse lattice propagators for quadratic gauge observables has a published antecedent. Meyer derives the color Wick contraction, mixed time–momentum propagator and Brillouin-zone convolution for energy–momentum tensor discretizations with the Wilson action, including explicit plaquette location phases in §2.4. Equations (2.18)–(2.22) in particular give a direct comparison to the fixed-patch contraction above. The observable here is the conditional variance of the six temporal staples. Its form factor, full-staggering zero and two packet normalizations follow from those six signed face locations. The step from the original Wilson variables to this free spectral calculation uses A4's deficit identity and C4's tangent input. [Meyer, JHEP 06 (2009) 077, §§2.3–2.4](https://arxiv.org/pdf/0904.1806) · [A4 calculation](../../observable-normalization/energy-density/staple-response/) · [C4 hypotheses and moment bounds](../../central-quotients/tangent-curvature/)

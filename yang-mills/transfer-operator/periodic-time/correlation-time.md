# The two-energy test for the gap-scaled correlation time

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

The rate at which a local reading loses weight at the gap does not, by itself, determine Z4's condition (C). The energy of the remaining weight matters. Two positive spectral measures suffice to disprove both directions of the proposed equivalence in the Step 10 heading. The examples below test the spectral inference used in that step. They do not assert a realization by a particular Wilson plaquette. [Z4's Step 10 and its examples](../../z4/attempt/reviews/a3-C/PROOF.md) · [Reduction and definitions](../../z4/attempt/A1_REDUCTION.md)

Let the gap be $m=1/\xi$. Give a normalized observable vector spectral weights $w$ and $1-w$ at lattice energies $m$ and $m(1+d)$, where $0<w<1$ and $d>0$. This is realized by a three-state Hamiltonian with a zero-energy vacuum and an observable mapping the vacuum to the specified superposition of the two excited states. Write $b=(1-w)/w$. From the vacuum spectral formula,
$$
 \frac{C(\xi/2)}{C(\xi)}
 =e^{1/2}\frac{1+b e^{-d/2}}{1+b e^{-d}}.
$$
For $d\to\infty$ the ratio stays bounded **if and only if** $b e^{-d/2}$ stays bounded. Indeed put $x=b e^{-d/2}$ and $y=e^{-d/2}$. The fraction after $e^{1/2}$ is at most $1+x$ and at least $x/(1+xy)\ge\tfrac12\min(x,1/y)$. Since $1/y\to\infty$, an unbounded subsequence of $x$ gives an unbounded subsequence of the ratio. If $d$ stays bounded, the ratio is at most $e^{(1+d)/2}$ for every $w$.

| Bottom weight and scaled-energy separation | Result for (C) |
|---|---|
| $b=\xi^2$, $d=\log\xi$ | The bottom weight is $1/(1+\xi^2)$. The ratio is $e^{1/2}(1+\xi^{3/2})/(1+\xi)$, which diverges as $e^{1/2}\sqrt\xi$. |
| $b=e^{\xi/4}$, $d=\xi$ | The bottom weight is $1/(1+e^{\xi/4})$. The ratio is $e^{1/2}(1+e^{-\xi/4})/(1+e^{-3\xi/4})$, which tends to $e^{1/2}$. |

In both families, every fixed bounded interval of gap-scaled energy containing the bottom eventually has exactly the displayed bottom weight. The counterexamples therefore apply to bounded-window weight as well as to the atom. The second model also illustrates the effect of propagation. Exponential suppression of the heavier state at half a correlation time already outweighs its initial advantage. The uniformly bounded **tilted exponential moment** in the reduction is still the general criterion.

A different distinction arises in (C′). The one-step loss controls the expectation of $\min(H,1)$ since $(1-e^{-1})\min(h,1)\le1-e^{-h}\le\min(h,1)$ for $h\ge0$. Put weights $1-m,m$ at $m,m^{-2}$ for $0<m<1$. The one-step loss is at most $2m$, whereas the initial mean energy is $(1-m)m+1/m$. The builder’s Step 3 gives the correct sufficient direction from a mean-energy bound. The converse reading in the ledger fails.

Finally, the pure vacuum pole at $m$ already gives $\xi[1-C(1)/C(0)]=\xi(1-e^{-1/\xi})$. It is increasing and bounded by one. Its values at $\xi=0.72,1,1.4$ are about 0.54, 0.63 and 0.71. An increase on those three lattices does not distinguish bounded growth from divergence. Their actual measurements also have finite thermal time and use an external correlation-length proxy. [Measured shapes and guest arithmetic controls](midpoint-shape/)

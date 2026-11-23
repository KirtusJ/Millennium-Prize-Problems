# Directional bounds on the electric winding energy

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Let $p=1-e^{-2\beta_t}$, let $h$ be a nonzero binary center charge with $m$ charged directions, and write $E_h=-\log\|T|_h\|$ for its lowest energy per temporal lattice step. On even periodic spatial cubes of side $L\ge4$, G4's neutral-kernel comparison gives the following consequences uniformly in the magnetic coupling. [G4's theorem and hypotheses](../../g4/winding-flux/slab.md)

* For $0<p<1/5$, the lower limit of $E_h/(mL)$ as $L\to\infty$ is at least $\operatorname{arcosh}[1+(1-p)(1-5p)/(2mp)]$. This strictly improves the elementary slope $\log(1/(5p))$ for each charge.
* For every $0<p\le101/500$, the lower limit is at least $\log(9/8)$ for all seven charges. This gives an explicit slope even above $p=1/5$.
* A positive elementary slope extends through $p<308981^{-1/8}\simeq0.20594845$. G4's use of subcritical percolation gives positivity over the full subcritical range. Here the constants follow from finite walk counts. [Earlier spatial estimates](../../g4/winding-flux/bounds.md)

These bounds concern charged sectors at the indicated temporal couplings. A center-neutral continuum mass gap remains open.

## Walks with specified displacement

An occupied graph that carries $h$ has a witness of one to three edge-disjoint simple cycles whose nonzero binary winding classes sum to $h$. Choose a root and orientation on each and lift the paths to the integer lattice. With $J$ the set of charged coordinates, their lifted displacements $v_i$ satisfy $\sum_i\sum_{j\in J}|(v_i)_j|\ge mL$. Indeed the total winding in each charged coordinate is odd, independently of how the cycles were oriented. An individual cycle may carry several charges; disjoint cycles can also carry them separately.

Suppose the sum of $p^n\exp(\theta\sigma\cdot v)$ over candidate paths rooted at the origin is at most $A$, for each sign vector $\sigma$ equal to $\pm1$ on $J$ and zero elsewhere. Each admissible cycle lift must belong to this path class. In a union bound over disjoint witnesses of size $k$, the independent-bond probability for each witness is exactly $p^{\sum n_i}$. Bound the sum of those weights first by extracting $e^{-\theta mL}$, then allow all ordered rooted path tuples and sum the $2^m$ signs separately for each path. This gives the finite bound
$$
 \|T|_h\|\le e^{-\theta mL}\sum_{k=1}^3(2^mL^3 A)^k.
$$
Allowing overlapping paths only in this last numerical sum preserves the disjoint-witness probability used in the union bound.

## Nonbacktracking walks

Put $S=2(3-m+m\cosh\theta)$. For a fixed tilt, the total exponential weight of all length-$n$ walks with no immediate reversal is $b_n$. Then $b_0=1$, $b_1=S$, $b_2=S^2-6$ and $b_n=S b_{n-1}-5 b_{n-2}$ for $n\ge3$. In the extension count the forbidden last pair of steps cancels its displacement. A prefix of positive length admits five choices for the first step of that pair. Consequently
$$
 A=\sum_{n\ge0} b_n p^n=\frac{1-p^2}{1-Sp+5p^2}.
$$
Use this expression only inside its series radius. Since $S\ge6$, the two positive characteristic roots are $(S\pm\sqrt{S^2-20})/2$. The smaller root is at most one, so for $p<1/5$ a positive denominator guarantees convergence. This is the exponential-weight version of the nearest-neighbor nonbacktracking generating function. [Fitzner and van der Hofstad](https://arxiv.org/abs/1212.6390)

The denominator is $(1-p)(1-5p)-2mp(\cosh\theta-1)$. Take $L\to\infty$ at each fixed tilt below its positive zero and then increase the tilt to that zero. The polynomial factor in $L$ has zero logarithmic rate. To compare slopes use $\cosh(\log(1/(5p)))-1=(1-5p)^2/(10p)$ and $m(1-5p)<5(1-p)$. At small $p$ the improved expression is $\log(1/(mp))+O(p)$.

## Eight-step continuations

The lift of a simple nonzero-winding cycle is self-avoiding, including its last vertex, which differs from the first by a nonzero period vector. After the first step, partition its edges into blocks of eight and a final remainder of at most seven. Retain the previous vertex when checking self-avoidance within each block. Forgetting other earlier vertices enlarges the set. For an incoming direction $a$, let $B_a$ sum $e^{\theta\sigma\cdot v}$ over the allowed eight-step continuations, where $v$ counts just those eight steps. Write $B=\max_a B_a$. Iterating conditional row sums shows that the path sum is finite whenever $p^8 B<1$. For example one can take
$$
 A=1+6pe^\theta\frac{\sum_{j=0}^7(5pe^\theta)^j}{1-p^8B}.
$$

At $e^\theta=9/8$ the exact computations give $B/5^8$ below 0.847, 0.874 and 0.900 for $m=1,2,3$, respectively. The largest bound times $(101/100)^8$ is less than one. This proves the second slope. At zero tilt every row contains exactly 308,981 paths. Since $B(\theta)\le308981e^{8\theta}$, the same argument supplies the explicit lower slope $\log(308981^{-1/8}/p)$ throughout the third range. All large-volume statements take a fixed $p$ before the spatial limit, or use the common worst-case bound on an interval bounded away from the stated convergence threshold.

## Verification

The three [PCP OS workers](worker.c) enumerated one, two and three tilted coordinates, respectively. For every incoming direction each worker checked the path count and the strict weighted bound with unsigned 128-bit integers. Positions use strides 1, 32 and 1024, which distinguish all sites reachable within this walk. The independent [coordinate-tuple enumeration](check.py) reproduced the bounds using exact fractions and all signed axis choices. A second [three-guest replay](../transfer-increments/replay-guests.py) reproduced [WindingRate.lean](WindingRate.lean), SHA-256 `bffdc7acd0dd35139072bf47118d6443595e87399d5afce7ce0025389aa56122`. Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked five algebraic and numerical declarations. The path decomposition, transfer comparison and limiting arguments are given in the linked proofs and the text above.

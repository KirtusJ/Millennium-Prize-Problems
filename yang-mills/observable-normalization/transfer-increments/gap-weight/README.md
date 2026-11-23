# What weight near the gap guarantees at one correlation length

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Z4's condition (C) asks whether $R=C(\xi/2)/C(\xi)$ stays bounded as the lattice gap $m=1/\xi$ vanishes. The raw spectral weight close to the gap can decrease polynomially while $R$ diverges, or exponentially while $R$ stays bounded. Both behaviors occur for the same fixed one-site observable in reversible three-state model families with a genuine infinite-volume gap at each cutoff. The relation between the weight and the energies carrying the rest of the observable determines the ratio. This corrects the general equivalence in step 10 of the builder's report. Its particular examples and Z4's conditional scaling theorem are consistent with the calculation. [Condition (C)](../../../z4/attempt/A1_REDUCTION.md) · [Builder's step 10](../../../z4/attempt/reviews/a3-C/PROOF.md) · [Local transfer models](models.md)

B4 independently disproved both directions with two-atom laws and obtained the exact criterion within that class. The results below give an optimum over all spectral laws, an equivalent half-time overlap test, and a minimum over bounded positive temporal filters. [B4’s two-energy test](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/6926458/yang-mills/transfer-operator/periodic-time/correlation-time.md)

## Sharp bound from raw weight

Let $\nu$ be the spectral probability of a nonzero centered vector, with energy $E$ in units of the full gap and support in $[1,\infty)$. Write $L(t)=C(t\xi)/C(0)=\int e^{-tE}\,d\nu$. For $K\ge1$, if $\nu([1,K])\ge p>0$, then
$$
 \sqrt e\ \le\ R=\frac{L(1/2)}{L(1)}
 \ \le\ e^{K/2}\frac{1+\sqrt p}{2\sqrt p}.
$$
The upper bound is attained with mass $p$ at $K$ and mass $1-p$ at $K+2\log(1+p^{-1/2})$. For $K=1$ the observable itself sees the true gap. The lower bound follows by integrating $e^{-E/2}\ge\sqrt e\,e^{-E}$.

For the upper bound let $s=\sqrt p$ and $x=e^{(K-E)/2}$. On $A=\{E\le K\}$ one has $(1+s)x-s\ge1$. Consequently
$$
 \mathbb E[((1+s)x-s)^2]\ge\nu(A)\ge s^2,
 \qquad 2s\,\mathbb Ex\le(1+s)\mathbb Ex^2 .
$$
Multiply the quotient by $e^{K/2}$. Equality holds with $x=1$ on $A$ and $x=s/(1+s)$ elsewhere. The arbitrary-probability-space inequality and the two-atom equality are both [kernel-checked in Lean](GapWeight.lean).

## An equivalent condition after half a correlation time

Let $P_{1/2}(dE)=e^{-E/2}\nu(dE)/L(1/2)$. Then $1/R=\mathbb E_{1/2}e^{-E/2}$. Condition (C) holds exactly when **there exist finite $K$ and $\eta>0$ such that $P_{1/2}([1,K])\ge\eta$ uniformly**. In one direction such a fraction gives $R\le e^{K/2}/\eta$. In the other, $R\le D$ gives, for $K>2\log D$,
$$
 P_{1/2}([1,K])\ge
 \frac{D^{-1}-e^{-K/2}}{e^{-1/2}-e^{-K/2}}.
$$
The denominator is positive when $K>1$, as follows here from $D\ge\sqrt e$. Split the mean of $e^{-E/2}$ across the cutoff to obtain this bound. This identifies which propagated vector needs low-energy overlap. At full time it is even possible to have convergence of the energy law to the gap atom while (C) fails. [Explicit family](models.md)

## Positive temporal smearing in a bounded slab

For a fixed $T\ge0$, consider an arbitrary nonzero finite nonnegative measure $a$ on $[0,T]$. The vector obtained by averaging Euclidean translates of the same centered insertion has spectral multiplier $F(E)=\int e^{-sE}\,da(s)$. The smeared reading is $L_F(t)=\int e^{-tE}F(E)^2\,d\nu$. Here time is in correlation lengths and the two reflected insertions use the same coefficients. For each cutoff,
$$
 \inf_a\frac{L_F(1/2)}{L_F(1)}
    = \frac{L(2T+1/2)}{L(2T+1)} .
$$
Thus the single insertion at the far edge gives the smallest possible ratio, even if the averaging weights are selected separately at every cutoff. For an integer-time Wilson transfer the statement holds on any grid containing its latest allowed time, using that actual endpoint for $T$.

Indeed, under the probability proportional to $e^{-(2T+1)E}d\nu$ let $b(E)=[e^{TE}F(E)]^2$ and $a_0(E)=e^{E/2}$. Both functions increase with $E$, so their covariance is nonnegative. This follows by integrating $(a_0(E)-a_0(E'))(b(E)-b(E'))\ge0$ over two independent draws. The means of $a_0$, $b$ and their product are finite since $F$ is bounded and $T\ge0$. Their reweighted mean $\mathbb E(a_0 b)/\mathbb E b$ is the smeared ratio. The unweighted mean is the endpoint ratio. An atom at $T$ attains equality. This argument applies to nonnegative coefficients on translates of the same observable. A signed filter or a nonlinear function of the slab has different spectral weights.

One fixed local model family defeats **every fixed slab length** in this class while its raw gap weight is $\xi^{-2}$. Therefore passage from a sharp-time insertion to bounded positive temporal smearing requires information about the Wilson spectral law to establish (C). The interacting four-dimensional condition and the Clay problem remain open. [Construction](models.md) · [Formal and numerical checks](checks.md) · [Jaffe and Witten](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

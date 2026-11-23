# A sharp conditional detection threshold for defining SU(2)

Take the defining normalized real trace in the SU(2) Wilson action. At a spatial link the six weighted staples sum as quaternions. With the exterior fixed, the conditional law is a translate of the central density proportional to $e^{u\cos\theta}$ with $0\le u\le J=4\beta_s+2\beta_t$. If $u=0$ this is Haar. In representation $n$ of dimension $n+1$, the normalized Fourier coefficient is $r_n(u)=I_{n+1}(u)/I_1(u)$ for $u>0$, and $r_n(0)=0$ for $n\ge1$. The formulas follow by integrating $\sin((n+1)\theta)/\sin\theta$ against the radial Haar weight $2\sin^2\theta/\pi$. Translations multiply the Fourier matrix by unitaries.

Let $r=r_1(J)$. The consecutive Bessel ratios $I_{j+1}(u)/I_j(u)$ decrease with the order $j\ge1$ by the modified-Bessel Turán inequality. Also $r_1(u)=\mathbb E_u\cos\theta$ increases with $u$ since its derivative is the variance. Thus $r_n(u)\le r^n$. For a path with $m$ marked links and arbitrary intervening exterior transports, Peter–Weyl inversion gives, with $s=r^m$,
$$\|p_{e,x}-1\|_\infty\le\sum_{n\ge1}(n+1)^2s^n
   =\frac{s(4-3s+s^2)}{(1-s)^3}.$$
For $s\to0$ this is $O(s)$ with an absolute constant. The graph bound in the [main theorem](README.md) yields indistinguishability from product Haar and vanishing normalized exterior correlation when $M s^2\to0$. [Baricz, Theorem 2.1](https://doi.org/10.1017/S000497271000002X) · [One-link character normalization](../joint-cutoff/)

## Two exteriors of the original theory

Place $M$ disjoint spatial rectangles on a sufficiently large periodic lattice. On the outgoing straight side of each mark $m$ successive links. Put the return side at least two fine cells away and leave it unmarked. Separate the rectangles so no plaquette meets marks from different rectangles. Consecutive collinear links cannot be on the same elementary face. Start with every unmarked link the identity. For the second exterior put $-I$ on one link of each return side and keep every other unmarked link fixed. No changed link shares a face with a mark. In both exteriors each marked link has the identical independent central Wilson law of strength $J$. The two conditional laws are specified by the continuous finite-lattice density at actual configurations. Any open neighborhoods of those configurations have positive Wilson probability at fixed finite volume.

Let $g$ be a complete rectangle holonomy. Its conditional density under the two exteriors is $p_+(g)=p_m(g)$ or $p_-(g)=p_m(-g)$, where $p_m$ is the $m$-fold central convolution. The densities are products across rectangles. Distinguishing the two using the full rectangle holonomies is a gauge-invariant experiment: both densities are class functions, so all their information for this test is contained in the traces of the individual loops.

Give the two exteriors equal prior probability for this experiment. As $s=r^m\to0$, the minimum probability of error from observing the loops has the following limit, which is uniform in how $J$ and $m$ realize $s$.

| Limit of $Ms^2$ | Optimal error |
|---|---|
| $0$ | $1/2$ |
| $\lambda\in(0,\infty)$ | $\Phi(-2\sqrt\lambda)$ |
| $+\infty$ | $0$ |

Here $\Phi$ is the standard normal distribution function. In the first regime both conditional product laws converge in total variation to the same product Haar law by the forward chi-square bound. In the last, the sum of traces has mean $\pm2Ms$ and variance at most $4M$, so its sign suffices by Chebyshev.

For the intermediate case write $\chi_n$ for the characters, with $\chi_1(g)=\operatorname{Tr}g$. Central convolution gives
$$p_\pm=1+\sum_{n\ge1}(\pm1)^n(n+1)r_n(J)^m\chi_n.$$
The even correction has sup norm $O(s^2)$; the odd correction after $\pm 2s\chi_1$ has sup norm $O(s^3)$ because $|\chi_n|\le n+1$. Expanding the difference of the two logarithms, their common even term cancels. Uniformly in $g$,
$$\log(p_+/p_-)=4s\chi_1+O(s^3).$$
Under $p_+$ the first two moments of $\chi_1$ are $2s$ and $1+3r_2(J)^m$ by character orthogonality and $\chi_1^2=1+\chi_2$. The variance tends to one. With $Ms^2\to\lambda$, $Ms^3\to0$, so the sum of the uniform remainder vanishes. The centered traces are independent, bounded by four and have variances tending to one. The triangular-array central limit theorem applies, giving log-likelihood limit $N(8\lambda,16\lambda)$ under the plus exterior. The minus exterior reflects its sign. Thresholding at zero yields the stated equal-prior error.

For example, at isotropic coupling $\beta=1$, $J=6$, setting $M$ to the nearest integer to $1/(4s^2)$ gives a limiting error of $\Phi(-1)\simeq0.158655$. At $m=18$ the original conditional-law calculation gives $M=4292$ and numerical error $0.158636$. [Reproducible numerical check](controls.py) · [Read-back](readback.txt)

## Rare events under mean normalization

Let $A$ be the positive-trace hemisphere. Haar gives $H(A)=1/2$ and $\int_A\chi_1\,dH=4/(3\pi)$ by direct radial integration. Nonconstant even characters integrate to zero on $A$, since its center translate is the complementary hemisphere up to a Haar-null equator. Thus $P_\pm(A)=1/2\pm8s/(3\pi)+O(s^3)$. For the event that **all** $M$ loop traces are positive,
$$\log\frac{P_+(A^M)}{P_-(A^M)}=
  \left(\frac{32}{3\pi}+O(s^2)\right) M s.$$
For $Ms\to\gamma>0$ this ratio tends to $\exp(32\gamma/(3\pi))$, although $Ms^2\to0$ and the total variation distance between the two full observations tends to zero. The probabilities of the event vanish in both exteriors. For a unit-mean estimate uniform over nonnegative graph insertions and all exteriors, a sum of first powers of the individual errors is therefore the sharp scale in this example. For normalized squared-integrable test correlations and binary discrimination the relevant scale is the sum of their squares.

The transition establishes sharpness of the **uniform two-exterior experiment** in the number of paths. The equal prior is specified by the experiment. These exteriors may be very rare under the unconditioned Wilson law. A lower bound for typical Wilson-vacuum correlations, or a continuum mass gap, would require additional information on the exterior distribution.

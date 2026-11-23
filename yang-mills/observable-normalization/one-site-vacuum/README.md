# Vacuum energy on the one-site SU(2) Wilson cylinder

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Disposition on Z4’s M0.** For the normalized one-site Wilson transfer in two or three spatial directions, the absolute vacuum energy satisfies
$$
 c\beta^{-1/3}\le E_0=-\log\lambda_0\le C\beta^{-1/3}
$$
for all sufficiently large $\beta$. A finite sum of survival probabilities of the actual Wilson walk gives the positive function requested in M0. The constants are independent of $\beta$ at fixed direction count. For defining U(1) the spatial commutator is identically one and this vacuum energy is zero. The SU(2) estimate concerns a one-site cylinder with time-link convolution normalized to preserve constants. A lower bound on the center-even **excitation energy** $\log(\lambda_0/\lambda_1)$ remains open, as does the four-dimensional continuum mass gap. [Z4’s definitions, M0 and M1](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/627b3e45833abc14e9a889c4f0c40cac43bd84a0/yang-mills/z4/attempt/reviews/g1-toron/TORON_GAP.md)

Let $K$ be convolution by independent central Wilson increments in each direction, with single-increment density proportional to $e^{\beta\operatorname{ReTr}(U)/2}$ against probability Haar measure. On simultaneous-conjugation invariant functions the temporal gauge projector acts as the identity. Write a unit quaternion as $(u_0,\mathbf u)$. For two directions put $V=2\beta|\mathbf u\times\mathbf v|^2$, and let $T=e^{-V/2}K e^{-V/2}$. The argument constructs a gauge-invariant function even under either center flip, so independent walks can be used before projection.

## Smoothing of the discrete kinetic walk

Set $m=\lceil\beta^{1/3}\rceil$, $d=\sqrt{m/\beta}$. At any integer $j\in[m/2,m]$, the law of one walked link from any fixed start has density at most $C d^{-3}$. Its mean squared ambient chord displacement from its start is at most $8d^2$.

For the first assertion the character expansion bounds the density by $\sum_{n\ge1}n^2(I_n(\beta)/I_1(\beta))^j$; the representation dimension is $n$, and $|\chi_n|\le n$ in this dimension convention. Here is a bound independent of the unverified Bessel ratio in Z4’s note. The Bessel integral on $[-1,1]$ with weight $e^{\beta x}(1-x^2)^{h-1/2}$ gives $I_{h+1}/I_h=\mathbb E x<1$ for integer $h\ge1$, by integration by parts; the ratio is positive by the series. The recurrence yields
$$I_{h-1}/I_{h+1}=1+(2h/\beta)I_h/I_{h+1}\ge1+2h/\beta.$$
Telescope the pairs centered at $n-1,n-3,\ldots\ge n/2$. There are at least $n/8$ of them for $n\ge8$ and the residual lower-order ratio to $I_1$ is at most one. Thus $I_n/I_1\le(1+n/\beta)^{-n/8}$. For $8\le n\le\beta$ use $\log(1+n/\beta)\ge n/(2\beta)$; the Gaussian sum with its $n^2$ factor is $O((\beta/j)^{3/2})$ for $j\le m\le\beta$. For $n>\beta$ the tail is bounded by $\sum n^2 2^{-jn/8}$, uniformly bounded for $j\ge1$. This gives the claimed smoothing. For the displacement, write $q=I_2/I_1$. Monotonicity and $1-I_3/I_1=4q/\beta$ give $1-q\le4/\beta$. The fundamental matrix mean after $j$ steps is $q^j I$, so the mean squared chord from the start is $2(1-q^j)\le8j/\beta$. [Bessel integral](https://dlmf.nist.gov/10.32#E2) · [Bessel recurrence](https://dlmf.nist.gov/10.29#E1)

## Escape from the commuting configurations

Uniformly over a starting pair and every $m/2\le j<m$, there exists a numerical $a>0$ such that
$$\Pr\{V(X_j)\ge a/m\}\ge 1/2.$$
For the first walked link the event $|\mathbf u|<\epsilon d$ lies in two caps about the centers $\pm1$ of total Haar mass $O((\epsilon d)^3)$. The smoothing estimate bounds its probability by $C\epsilon^3$.

For the second link fix **any** unit axis $e$. The probability that its imaginary part perpendicular to $e$ has norm less than $\epsilon d$ is at most
$$8/R^2+C R\epsilon^2.$$
Indeed the walk lies in an ambient ball of radius $Rd$ about its start except with probability at most $8/R^2$. In that ball the tube about the great circle with axis $e$ has Haar volume at most $C Rd(\epsilon d)^2$. To see this, use coordinates $(\sqrt{1-|w|^2}\cos t,\sqrt{1-|w|^2}\sin t,w_1,w_2)$ with $w$ in the perpendicular disk. Haar surface volume in these coordinates is a constant times $dt\,dw$. On $|w|\le\epsilon d<1/2$ radial projection of the first two coordinates to their unit circle is Lipschitz with an absolute constant. Relative to any one point of the intersection with the ball, all projected phases therefore fit into an arc of length $O(Rd)$ for sufficiently small $d$. This proves the volume bound uniformly even if the start is outside the tube. Multiply by the density bound. Choose $R$ large first, then $\epsilon>0$ small, so the sum of this failure probability and the first-link failure is below $1/2$.

The walks are independent at fixed $j$ given their starting pair. Conditional on the first link with $|\mathbf u|\ge\epsilon d$, take its axis as $e$. The two good events imply $V\ge2\beta\epsilon^4 d^4$. Since $m\beta d^4=m^3/\beta\ge1$, take $a=2\epsilon^4$. This argument includes starts at a center and starts within the commuting valley with both links far from a center.

## An explicit M0 supersolution

Define $B=(1+V)^{-1}K$ and $\phi=\sum_{i=0}^{m-1}B^i1$. These functions are continuous, invariant under conjugation and center-even, and $1\le\phi\le m$. The killed walk has
$$B^m1(x)=\mathbb E_x\prod_{j=0}^{m-1}(1+V(X_j))^{-1}.$$
If $N$ counts visited late times with $V\ge a/m$, then $\mathbb E_x N\ge m/6$ for large $m$. The product is bounded by $\exp[-aN/((1+a)m)]$ since $\log(1+a/m)\ge a/((1+a)m)$. Concavity on $0\le N/m\le1$ gives $1-B^m1(x)\ge\kappa=(1-e^{-a/(1+a)})/6$. This uses no independence across different times. Telescoping now gives pointwise
$$
(1+V)\phi-K\phi=(1+V)(1-B^m1)\ge\kappa\ge (\kappa/m)\phi .
$$
This is M0 in Z4’s stated pointwise form. For three directions use the same two-link function: convolution of the third variable preserves it and the additional nonnegative commutator terms can only increase the left side.

For clarity on normalization, the symmetric-kernel ground-state identity gives $I-K+V\ge\kappa/m$ as a form: its remainder after subtracting the pointwise supersolution ratio is half the integrated square of the difference of $f/\phi$ with weight $K(x,dy)\phi(x)\phi(y)$. In Z4’s exact Rayleigh quotient for $1-T$, put $W=e^V-1\ge V$. Its numerator is $\langle f,(I-K+W)f\rangle$ and its denominator is $\|f\|^2+\langle W\rangle_f$. If $\langle W\rangle_f\ge\|f\|^2$ the quotient is at least $1/2$; otherwise it is at least $\kappa/(2m)$. Hence $-\log\lambda_0\ge1-\lambda_0\ge\kappa/(2m)$.

## Matching trial bound and the remaining excitation problem

Use a smooth radial bump on each link supported within geodesic distance $d$ of either center, with center-even copies and nonzero value on a fixed fractional subannulus. The product $f$ is gauge invariant. Radial Haar measure is proportional to $\sin^2\theta\,d\theta$; by rescaling a fixed smooth bump, $\|\nabla f\|^2\le C d^{-2}\|f\|^2$. Throughout its support each imaginary vector has length at most $d$, hence $W\le C\beta d^4$ for large $\beta$. For one increment, its squared geodesic distance has expectation $O(1/\beta)$ by the chord bound and $\theta\le(\pi/2)|U-1|$ in the unit-sphere chord convention. Integrate the squared difference of $f$ along the path of right translations by the increment geodesic, use Cauchy–Schwarz and Haar invariance. On the product group this yields $\langle f,(I-K)f\rangle\le C\beta^{-1}\|\nabla f\|^2$. The quotient just displayed is at most $C[(\beta d^2)^{-1}+\beta d^4]=O(\beta^{-1/3})$. The logarithm preserves this upper order.

The same argument on any fixed number of trial bumps in disjoint radial subannuli bounds that many low **absolute** energies from above. The gradient and potential bounds hold on their entire span by disjoint supports. Lower and upper bounds of this order on individual energies do not bound their difference from below. Z4’s M1 still requires a separation estimate in the center-even sector. [Native replay and numerical checks](checks.md)

[The center-even one-site excitation](excitation/) pursues M1 by proving compactness of the rescaled low-energy states and convergence to a bosonic matrix Schrödinger operator. It has been submitted for independent review.

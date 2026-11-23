# Centered spectral weights at the two crossovers

Let $x\in[0,1]$ be the transfer eigenvalue and $E=-\log x$ its energy in lattice-time units. Write $d\mu$ for the spectral measure of the centered rectangle $f_Q\Omega$ and $C_t=\int x^t d\mu$ for real $t>0$. For the uncentered trace add the vacuum atom of mass $w^2$. A possible component at $x=0$ has zero weight at the lags below. Use the growing positive physical sizes and deep strong-coupling family of the [main result](README.md). Put $\ell=\log(4/\beta)$, $x_H=e^{-P\ell}$, and $x_L=e^{-4\ell}$.

The uncentered leading wall and the two disconnected disks have equal area at $k_0=2A/P$. The centered wall and the wall through one cell have equal area at $k_c=(2A-2)/(P-4)$. Their displacement is positive for $n,m\ge2$ and at most half a lattice step, using $16A\le P^2$. A square of side $n$ has $k_0=n/2$ and $k_c=(n+1)/2$. Only equality of the actual integer areas gives the multiplicities stated below.

**Away from the centered equality.** If $Pk<2(A-1)+4k$, the centered measure weighted by $x^k/C_k$ satisfies $E-P\ell\to0$ in probability. Indeed $k,k-1,k-2$ are eventually positive and on the same wall branch. In that measure the first two moments of $x_H/x$ tend to one, from the backward ratios $x_H^j C_{k-j}/C_k$. Its squared distance from one therefore tends to zero in mean. For $Pk>2(A-1)+4k$, use $k,k+1,k+2$ on the unit branch. The two forward moments of $x/x_L$ tend to one and $E-4\ell\to0$ in probability. These are additive errors in lattice energy, before division by the lattice spacing. They concern the spectral measure seen by the propagated rectangle.

**At the uncentered equality.** Here $Pk=2A$ puts the centered reading strictly on the perimeter branch. Since $w^2\sim4z^{2A}$ and $C_k\sim z^{Pk}$, the vacuum fraction tends to $4/5$, while the remaining $1/5$ concentrates at $P\ell$ with the additive precision above. In particular for each fixed real $s$, functional calculus resolves the substep profile
$$
 \frac{w^2+C_{k+s/(P\ell)}}{w^2}\longrightarrow1+\tfrac14e^{-s}.
$$
Under the centered time-$k$ probability $E/(P\ell)\to1$. Positive $s$ gives a bounded integrand. For negative $s$, the bounded backward moment $\mathbb E[\exp(E-P\ell)]$ and Hölder give uniform integrability of $\exp(|s|E/(P\ell))$ (bound its second moment for large $P\ell$). The interpolation uses fractional transfer powers. The adjacent integer times are ordinary Wilson measurements.

**At the centered equality.** Write $D=Pk=2(A-1)+4k$. At lag $k-1$ the wall dominates and at $k+1$ the unit tube dominates. Let $H_b,L_b$ be relative windows of width $\eta=A^{-m}$ about $x_H,x_L$, respectively, with $m$ arbitrarily large but fixed. Use the backward first and second moments at $k-1$, and the forward ones at $k+1$. Their errors are smaller than every inverse power of $A$ by the analytic estimate. Chebyshev gives the same precision for the outside probabilities at those two lags, even for these shrinking windows (use $x_H/x$ on the high-energy side). Transport the high-energy window forward by multiplying by $x$. Transport the low-energy window backward by multiplying by $1/x$. Their unnormalized weights at time $k$ are
$$
 z^D(1+O(\eta)+o(A^{-m})),\qquad
 A z^D(1+O(\eta)+o(A^{-m})).
$$
Since $C_k=(A+1)z^D(1+o(A^{-N}))$ for every fixed $N$, choosing $m$ sufficiently large makes the residual outside both windows $o(A^{-N})z^D$ for any prescribed $N$. Thus the high-energy fraction is asymptotic to $1/(A+1)$ and the low-energy fraction to $A/(A+1)$. The [plaquette-sum overlap](overlap.md) separately identifies the vector carrying the larger weight.

The factor $A$ displaces the equal-**weight** time. At an integer tie choose the real displacement
$$
    r=\frac{s-\log A}{(P-4)\ell},\qquad s\text{ fixed}.
$$
After propagation to $k+r$, the high-to-low odds tend to $e^{-s}$, so the high-energy fraction tends to $1/(1+e^s)$. On the two windows the additional factors are $x_H^r(1+o(1))$ and $x_L^r(1+o(1))$. The ratio of the main weights is $A^{-1}(x_H/x_L)^r=e^{-s}$. To control the complement for the eventually negative $r$, interpolate its moment at $k+r$ by Hölder between $k$ and $k-1$. After division by $z^D$ the extra factor is bounded by a fixed power of $A$, since $x_H^{-|r|}=\exp[O(\log A)]$. The preceding complement estimate absorbs that power. This gives a fractional-time description of the two concentrations, with no claim of two exact eigenvalues at finite coupling.

# Uniform estimates for the moving threshold

## Pushforward and conditional geometry

For $k>0$ put $E=p+q$, $z=p-q$, where $p,q$ are the magnitudes of the two gluon momenta. The domain has $E\ge k$, $|z|\le k$. Drop the fixed color and Fourier factor. The measure is
$$
\big[(E^2-k^2)^2+(k^2-z^2)^2\big]\,dE\,dz/k .
$$
Each shared-clock vector has multiplier $e^{-s(E^2+z^2)/2}$. Put $x=E^2+z^2-k^2$. Absorb $e^{-sk^2/2}$ into the coefficient of that reading. This leaves the cancellation ratio unchanged because its numerator uses the individual vector norms. Henceforth $g_s(x)=e^{-sx/2}$. [Derivation of the momentum measure](../../flow-momentum/spectrum.md)

For $y=x/k^2$ and $v=|z|/k$, the pushforward density in $dx$ is $w_k(x)=k^3 d(y)$, with
$$
 d(y)=\int_0^{\min(1,\sqrt y)}
 \frac{(y-v^2)^2+(1-v^2)^2}{\sqrt{1+y-v^2}}\,dv.
$$
At rest use $w_0(x)=x^{3/2}$, the continuous limit in the same normalization. The following bounds hold for every $x>0$ and $k\ge0$:
$$
 \tfrac1{32}\sqrt{x}(k^2+x)\le w_k(x)\le5\sqrt{x}(k^2+x).
$$
For $0<y\le2$, the integrand is at most five. On the first half of its integration interval, the second square is at least $9/16$, the denominator at most $\sqrt3$, and the length of this half at least $\sqrt y/(2\sqrt2)$. Thus $9\sqrt y/(32\sqrt6)\le d(y)\le5\sqrt y$. For $y\ge2$, the interval has length one. Bound the integrand below by $(y-1)^2/\sqrt{1+y}$ and above by $(y^2+1)/\sqrt y$. These bounds give the claimed constants.

Write $J=[k,k+\epsilon]$ and let $p_J(x)$ be the conditional mass fraction of $J$ at fixed $x$. It equals one for $x\le\Delta$. For $x\ge2\Delta$,
$$
 p_J(x)\le48\Delta/x .
$$
Indeed any contribution requires $x\le k^2+\Delta$, so $y\le2$. The allowed interval for $v$ starts at $\sqrt{y-\Delta/k^2}$, and ends at most at $\sqrt y$. Its length is at most $(\Delta/k^2)/\sqrt y$ by rationalization. Bound its integrand by five and divide by the lower bound for $d(y)$. The resulting constant $160\sqrt6/9$ is less than 48. At $k=0$ the conditional fraction is precisely the indicator $x\le\Delta$. In particular an amplitude reaching fraction $\eta$ in $J$ has at least fraction $\eta/2$ of its squared norm on $x\le S\Delta$ for $S=96/\eta$. This addresses the collinear part of the threshold where $E$ can be close to $k$ even when $x$ is appreciable.

## Lower bound for signed combinations

Rescale $x$ to $ax$, the clocks to $s/a$, and $k$ to $\sqrt a\,k$. The measure acquires only a common factor, so take $a=1$ and write $B=b/a$. Compare the radial norm to the sum of two squared norms with measures $k^2x^{1/2}dx$ and $x^{3/2}dx$. From the density bounds and the preceding concentration, at least one component contributes at least $(\eta/20)\|f\|_{w_k}^2$ **inside** $x\le S\Delta$ (in these scaled units). Its full squared norm is at most $32\|f\|_{w_k}^2$. The fraction in that component is thus at least $\eta/640$. Its cancellation ratio is at most $\sqrt{640/\eta}\,\chi$. This follows from the lower bound on its norm and the pointwise comparison for each individual reading. A component of zero weight cannot be selected.

For completeness, in either power measure $x^{p-1}dx$, $p\in\{3/2,5/2\}$, expand normalized clocks in orthonormal Laguerre functions at scale $s_*=\sqrt B$. With $X=s_*x$ the functions are proportional to $e^{-X/2}L_n^{p-1}(X)$. The squared coefficient of degree $n$ is $(1-r_s^2)^p (p)_n r_s^{2n}/n!$, $r_s=(s-s_*)/(s+s_*)$. The generating function and orthogonality give this identity. Since $\max_s |r_s|<1$, choose $\max_s|r_s|<q<1$. The norm of each clock above degree $N-1$ is at most $Aq^N$ with $A$ uniform in $s,p$. For a normalized signed combination the tail is at most $Aq^N$ times its cancellation ratio. [NIST DLMF, generating function](https://dlmf.nist.gov/18.12.E13) · [Weights and orthogonality](https://dlmf.nist.gov/18.3)

Let $P_h$ restrict to $X\le h$ and $\Pi_N$ project onto degrees below $N$. The finite Laguerre sum gives $|L_n^{p-1}(X)|\le L_n^{p-1}(0)e^{nX/p}$. Integrating the squares and summing the first $N$ diagonal entries bounds
$$
\|P_h\Pi_N\|^2\le e^{p-1+2Nh/p}(Nh)^p/\Gamma(p+1).
$$
The factorial estimate here is $(p)_n/n!\le e^{p-1}(n+1)^{p-1}$. Take $h=s_*S\Delta$ and $N=\lfloor c_0/h\rfloor$ with $c_0>0$ small enough that this operator norm is at most half of $\sqrt{\eta/640}$ for both powers. The remaining norm in the window must come from the Laguerre tail. Hence $\chi\ge c_1 q^{-N}$ and $\log\chi\ge c_2/\Delta$ for sufficiently small scaled $\Delta$. [NIST finite Laguerre sum](https://dlmf.nist.gov/18.5.E12) · [Detailed trace bound at rest](../resolution.md)

## Constructive upper bound

Return to the original units. Choose $m\ge2$, $N=2(m-1)$ and $X=e^{-(b-a)x/(2N)}$. Use
$$
 f_m(x)= e^{-ax/2}K_m(X)^2,\qquad
 K_m(X)=\frac{1-T_m(2X-1)}{2m^2(1-X)},\quad K_m(1)=1 .
$$
The polynomial $K_m^2$ has degree $N$, so only clocks $a+(b-a)j/N$ are used. The removable quotient is the normalized Fejér kernel with half-angle $\alpha=\arcsin\sqrt{1-X}$, namely $K_m=[\sin(m\alpha)/(m\sin\alpha)]^2$. Thus $0\le K_m\le\min(1,1/[m^2(1-X)])$. [Chebyshev formula](https://dlmf.nist.gov/18.5.E1)

In each power measure put $t=mx$ and $\gamma=\sqrt{b-a}/2$. After rescaling, the squared-norm density tends in $L^1(dt)$ to $t^{p-1}\operatorname{sinc}^8(\gamma\sqrt t)$ up to normalization, where $\operatorname{sinc}(v)=\sin(v)/v$. Indeed $m\sqrt{1-X}\to\gamma\sqrt t$. Where $(b-a)t/(2Nm)\le1$, the squared filter is at most $C(1+t)^{-4}$. On the complement $K_m^4\le C m^{-8}$, with the additional factor $e^{-at/m}$; the integral there against $t^{p-1+j}$ is $O(m^{p+j-8})$ for $j=0,1$. This proves convergence also of the first $t$ moments. In particular the squared norms in the two powers have orders $m^{-3/2}$ and $m^{-5/2}$.

In units $a=1$, choose a common $T$ so that both rescaled component probabilities above $t=T$ are less than $(1-\eta)/160$ with a strict margin for all large $m$. Density comparison bounds the actual tail by 160 times their larger tail, uniformly in $k$. With $m=\lceil T/\Delta\rceil$, $x\le T/m$ puts every accessible energy in $J$. The coefficient sum of $K_m^2$ in absolute value is $K_m(-1)^2=\exp(O(m))$. This follows from its nonnegative real roots and the Chebyshev formula at $-3$. The individual squared clock norms are at most $C(1+k^2)$, and $\|f_m\|_{w_k}^2\ge c(k^2m^{-3/2}+m^{-5/2})$. Thus $\chi\le C m^{5/4}\exp(Cm)$, uniformly in $k$. Restoring $a$ gives the upper estimate in the [theorem](README.md).

## What one-sign coefficients can resolve

For $0\le k\le K$, normalize the nonnegative effective coefficients after the clock shift to sum to one. Then $e^{-bx/2}\le f(x)\le e^{-ax/2}$. Its squared norm lies between positive constants depending on $a,b,K$. On $J$ one has $x\le(k+\epsilon)^2$, so for $0<\epsilon\le1$ its squared amplitude also lies between two positive constants. The captured fraction has the order of the unflowed window mass. Integrating in $z$ gives $2(E^2-k^2)^2+16k^4/15$ per unit $E$ in the chosen normalization. Its integral from $k$ to $k+\epsilon$ is comparable to $\epsilon(k+\epsilon)^4$, including at $k=0$. This rules out a fixed positive threshold fraction throughout any bounded momentum range as the window shrinks for this cone of coefficients.

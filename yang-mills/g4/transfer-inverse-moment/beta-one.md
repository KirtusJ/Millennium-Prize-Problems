# An explicit interacting example at unit coupling

For an elementary SU(2) Wilson plaquette at $\beta=1$, at least $3/400$ of absolute connected spectral weight lies in the transfer interval $[2^{-43},\sqrt{1-3/800}]$. At the same coupling and $0\le u\le1/512$, the ordinary flowed plaquette carries at least $1/400$ there. Both bounds are uniform over periodic even spatial sides $L\ge4$, in the infinite-time vacuum. The following estimates give the constants.

## Conditional variance of a single link

On the unit three-sphere give a quaternion $Q$ density proportional to $e^{\kappa n\cdot Q}$ for a unit vector $n$ and $\kappa\ge0$. In every unit direction $v$,
$$
\operatorname{Var}(v\cdot Q)\ge\frac{3}{2(\kappa+4)^2}.
$$
Indeed, $X=n\cdot Q$ has density proportional to $e^{\kappa x}\sqrt{1-x^2}$ on $[-1,1]$. For $h=\mathbb E X$, differentiation gives $h'=\operatorname{Var}(X)$. Integrating the derivative of $e^{\kappa x}(1-x^2)^{3/2}$ yields $3h=\kappa\mathbb E(1-X^2)$, so $h'=1-h^2-3h/\kappa$. Rotational symmetry gives three transverse covariance eigenvalues $h/\kappa$. At zero tilt all four eigenvalues equal $1/4$.

Put $g=\kappa/(\kappa+4)$. The difference $h-g$ solves a linear differential equation with coefficient $h+g+3/\kappa$ and forcing $1-g^2-3g/\kappa-g'=5\kappa/(\kappa+4)^2$. Its integrating factor $\kappa^3\exp\int_0^\kappa(h+g)$ tends to zero at the origin, while $h-g$ is bounded. Thus $h\ge g$. Differentiating the Riccati equation gives $v'+(2h+3/\kappa)v=3h/\kappa^2$ for $v=h'$. With $\ell=3/[2(\kappa+4)^2]$, the forcing for $v-\ell$ is
$$
h\left(\frac3{\kappa^2}-\frac3{(\kappa+4)^2}\right)
-\frac9{2\kappa(\kappa+4)^2}+\frac3{(\kappa+4)^3}
\ge\frac{45\kappa+60}{2\kappa(\kappa+4)^3}.
$$
The inequality substitutes $h\ge g$ with a positive coefficient. The integrating factor $\kappa^3\exp\int_0^\kappa2h$ again kills the bounded endpoint term. Hence $v\ge\ell$, and $h/\kappa\ge1/(\kappa+4)\ge\ell$ as well. [Lean residual identity](InverseMoment.lean)

In the four-dimensional Wilson law, condition on every link except a chosen spatial link of the elementary plaquette. Its six staples give a tilt of length at most $6\beta$, since each has unit norm. The bare deficit, with this exterior fixed, is a constant plus a real linear functional with unit coefficient. Thus its conditional variance is at least $3/[2(4+6\beta)^2]$. This estimate applies to the squared error of every predictor from the preceding slice, also in the infinite-time stationary vacuum. Taking the optimal such predictor identifies $C_0(0)-C_0(2)$ by the vacuum Markov representation. At $\beta=1$ the result is at least $3/200$. [Creutz, SU(2) Wilson heat bath](https://doi.org/10.1103/PhysRevD.21.2308) · [Vacuum prediction](../spatial-flow-variance/README.md)

## Bounding the other end of the interval

The centered bare deficit has sup norm at most two and degree one on each of four links. At $\beta=1$ the Bessel series gives $A_1<8$ and $2I_1(1)<6/5$. In detail, enclose each $I_j(1)$ by its first thirteen positive terms and a geometric remainder with first omitted ratio $1/[4\cdot13(j+13)]$. Use those rational intervals on the terms $0\le n<18$ of $A_1$ and round square roots upward. For $n\ge18$ the majorant from the inverse-form proof has successive ratio $\sqrt{(n+3)/2}/(n+1)<1/2$, so twice its first term bounds that tail. The exact arithmetic control performs these two comparisons. Since $e<3$, the density minimum $e^{-1}/(2I_1(1))>1/4$. The inverse budget is strictly less than $4\cdot8^8\cdot4^4=2^{34}$. [Bessel series](https://dlmf.nist.gov/10.25.E2) · [Rational enclosure](control.py) · [Inverse estimate](inverse-form.md)

At $s=2^{-43}$ the mass below $s$ is at most $2^{-9}<3/800$. With $b=\sqrt{1-3/800}$ the loss above $b$ is at most $3/800$. Subtracting these from $3/200$ leaves at least $3/400$ in $[s,b]$. Finally each spatial link has speed at most four under the unit-clock gradient flow, from its four incident unit staples. Telescoping four links gives $\|F_u-F_0\|_\infty\le16u$. Centering and projection into the same interval contract the norm. For $u\le1/512$ the projected norm is at least $\sqrt{3/400}-1/32>1/20$, giving weight at least $1/400$. The finite upper energy endpoint is $43\log2$ and the lower one is $-\tfrac12\log(1-3/800)$, both in lattice units.

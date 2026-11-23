# Finite moment data can conceal weight down to zero energy

For any prescribed integer $m\ge1$ construct two probability measures on $[0,2]$ with the same moments of orders zero through $m$. One is supported in $[1,2]$ with bottom exactly one. The other has strictly positive mass in every interval $(0,\epsilon)$ and no atom at zero. Both satisfy uniform high-energy moment bounds. These are examples for the moment inference problem; a Wilson realization of either measure is not assumed.

Let $\sigma$ be uniform probability on $(0,1/2)$ and let $x_i=(3-\cos(i\pi/m))/2$ for $0\le i\le m$. Write $\ell_i$ for the degree-$m$ cardinal interpolation polynomial at the increasing nodes $x_i$. Set $w_i=\int\ell_i\,d\sigma$. Polynomial interpolation gives $\int p\,d\sigma=\sum_i w_i p(x_i)$ for every polynomial of degree at most $m$, including the constant one. For $t<1$ in the support of $\sigma$, the numerator of $\ell_i(t)$ has sign $(-1)^m$ and its denominator sign $(-1)^{m-i}$. Thus the nonzero weights alternate starting with $w_0>0$.

Let $W=\sum_i |w_i|$. The sum of the even weights and one plus the absolute sum of the odd weights both equal $S=(1+W)/2$. Consequently
$$
\mu_{\rm low}=S^{-1}\!\left(\sigma+\sum_{i\ {\rm odd}}|w_i|\delta_{x_i}\right),\qquad
\mu_{\rm high}=S^{-1}\sum_{i\ {\rm even}}w_i\delta_{x_i}
$$
have matching moments through order $m$. Their support bottoms are zero and one, respectively. The low part has mass $2/(1+W)$ below $1/2$. If a common band with a prescribed positive weight is needed, mix both measures equally with the same atom at $3/2$, preserving moment equality and both support bottoms.

The Chebyshev polynomial $T_m$ satisfies $T_m(3-2x_i)=(-1)^i$, so interpolation also gives $W=\int T_m(3-2t)\,d\sigma(t)$. In particular $T_m(2)\le W\le T_m(3)$ by $T_m(x)=\cosh(m\,\operatorname{arcosh}x)$ for $x\ge1$. At order two, the nodes are $1,3/2,2$ and $T_2(x)=2x^2-1$, giving $W=35/3$. The low law puts $3/19$ of its weight below $1/2$. The next-order test $\int(E-1)(E-3/2)^2\,d\mu$ gives $-119/608$ and $23/304$ for the low and high laws. The degree of the test explains how the third moment distinguishes them. The exact controls also check higher interpolation orders on rational grids. [Exact arithmetic](control.py)

Thus imposing any finite list of shifted-form inequalities can admit spectra with different gaps even when both measures have compact support. A Wilson-specific recurrence, ordering estimate or other dynamical input could supply information beyond those inequalities. [All-orders equivalence](edge.md)

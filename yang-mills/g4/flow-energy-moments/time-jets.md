# From the spatial Wilson flow to a uniform high-energy tail

## Polynomial time derivatives

Represent each link by its four real quaternion coordinates. All coordinates of a real trajectory have magnitude at most one. Reversing an oriented link conjugates its quaternion, a real linear sign change. For the negative gradient of the spatial action in the unit round metric the vector field is $V_e=-\sum_{p\ni e}\operatorname{Im}(P_{p,e})U_e$. Each face starts with the positive occurrence of the varied link. Each link belongs to four spatial faces. The field is tangent, gauge equivariant and complete for both signs of real time on the compact finite slice. [Derivation of the Wilson ODE](../spatial-flow-variance/README.md) · [Lüscher, finite-lattice flow, §4.1](https://arxiv.org/pdf/1006.4518)

Use $\|P\|_{\rm c}$ for the sum of absolute coefficients of a polynomial in the ambient real coordinates, prior to restricting to unit quaternions. A component of a four-link product has at most $4^3=64$ signed monomials. The deficit $f$ has degree four and coefficient norm at most 65. Each component of $V_e$ has degree at most five and coefficient norm at most $4\cdot3\cdot64=768$. We use $B=4096$ throughout. For $D=\sum_i V_i\partial_i$ and a polynomial of total degree $d$,
$$
\|DP\|_{\rm c}\le B\,d\,\|P\|_{\rm c},\qquad \deg(DP)\le d+4 .
$$
Indeed the sum of exponents differentiated on each monomial is its degree. This avoids a factor proportional to the box size. By induction $\deg(D^jf)\le4+4j$ and $\|D^jf/j!\|_{\rm c}\le65J^j$ with $J=4B$. At every real time $v$, the $j$th derivative of $f(\Phi_v U)$ equals $(D^j f)(\Phi_v U)$. [Lean recurrence](EnergyMoments.lean) · [Exact coefficient counts](control.py)

## A polynomial approximation at any fixed flow time

Set $h=1/(2J)$. At each real center the Taylor remainder after order $n$ on the real axis is at most $65(J|t-v|)^{n+1}$. Thus the Taylor series agrees locally with the orbit reading. Its extension to $|t-v|<h$ is bounded by 130. Overlapping discs with real centers share a real interval, so their functions agree there and glue by uniqueness to $|\operatorname{Im}t|<h$. This continues the scalar observable in its **spatial flow time**.

Compose with $t=h\,\operatorname{atanh}z$ on $|z|<1$. Its imaginary part has magnitude less than $\pi h/4$. Write $p_j(U)$ for the resulting coefficient of $z^j$. Since the clock series has zero constant term, only time derivatives of orders at most $j$ contribute to $p_j$. It is a real polynomial of degree at most $4+4j$, gauge invariant by covariance of the real flow. Two different coefficient estimates are useful.

- For each real configuration the scalar analytic function on the unit disk is bounded by 130. Cauchy's estimate with radii tending to one gives $\|p_j\|_\infty\le130$.
- On $|z|\le1/2$ the polynomial-coefficient series in time converges absolutely in coefficient norm. Indeed $Jh\,\operatorname{atanh}(1/2)<1/2$ and the bound on the normalized derivatives sums to at most 130. Coefficient extraction, or Cauchy's inequality in the coefficient space, gives $\|p_j\|_{\rm c}\le130\,2^j$.

For $q=\tanh(u/h)$, define $P_N=\sum_{j=0}^N q^j p_j$. Its uniform approximation error is at most $130q^{N+1}/(1-q)$, its coefficient norm is at most $260\,2^N$, and its total degree is at most $4(N+1)$. On $0\le u\le U$ one may replace $q$ in the error bound by any fixed $q_*\in(0,1)$ at least $\tanh(U/h)$. The constants can be very large. The staggered compact Wilson configuration with $f'=-4f(2-f)$ admits an exact rational check of the first twelve composed time derivatives, including the orientation and the clock factor. [Staggered Wilson orbit](../spatial-flow-variance/README.md) · [Exact series check](control.py)

## Passing a total degree bound through the transfer

Consider one monomial in $P_N$ of degree $d\ge1$. Its support has $r\le d$ links, with degrees $d_i\ge1$ summing to $d$. Gauge average the monomial at its vertices. The result has sup norm at most one, the same support bound and per-link representation labels at most $d_i$, since the left and right actions are linear in each link and each coordinate belongs to the fundamental representation. Gauge averaging the polynomial term by term recovers the full gauge-invariant $P_N$. The local inverse estimate therefore applies to the individual averaged terms:
$$
\|T^{-1/2} f_{\rm mon}\Omega\|\le k_{\min}^{-r/2}\prod_i A_{d_i}
\le \exp[C_\beta d\log(2+d)] .
$$
Here $0<k_{\min}\le1$, $\log^+ A_j\le C_\beta(1+j)\log(2+j)$, and $\sum_i(1+d_i)\le2d$. The constant monomial has inverse norm one. The estimate uses the support of **each monomial** before applying the triangle inequality. Treating the union of the supports as one patch loses the stated growth rate. Subtraction of the vacuum component is an orthogonal projection commuting with $T$. Hence for some $K_\beta\ge1$ the inverse **norm** of the centered vector of $P_N$ is at most $\exp[K_\beta(N+1)\log(N+2)]$. All constants are uniform on compact positive coupling intervals. [Inverse form and SU(2) coefficients](../transfer-inverse-moment/inverse-form.md)

Project onto $0\le\lambda\le e^{-t}$. Projection and centering contract the approximation error, and the projected polynomial norm is at most $e^{-t/2}$ times its inverse norm. For large $t$, take $N=\lfloor t/(16K_\beta\log(e+t))\rfloor$. Then $K_\beta(N+1)\log(N+2)\le t/8$. The square root of the tail is bounded by the approximation error, which is $O(\exp[-c t/\log(e+t)])$, plus $e^{-3t/8}$. Squaring and enlarging constants on bounded $t$ proves the stated tail. For any weak transfer-measure limit and $s<t$, the open set $[0,e^{-s})$ in $[0,1]$ contains $[0,e^{-t}]$. Apply the open-set Portmanteau bound at $s$ and take $s\uparrow t$. This excludes a zero-transfer atom also in the limit.

This proof does not give an exponential moment of $E$. For example take diagonal transfer values $(j+1)^{-j}$ and vector coefficients $e^{-j}$ for $j\ge1$. Truncating at $N$ has error $O(e^{-N})$ and inverse norm at most $\exp[\tfrac12 N\log(N+1)]$ times the vector norm. Yet $\sum_j\exp[\alpha j\log(j+1)-2j]$ diverges for every $\alpha>0$. This example identifies the limitation of the two approximation estimates.

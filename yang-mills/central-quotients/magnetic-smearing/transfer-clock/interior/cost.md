# Cost of resolving an interior energy with two spatial flow times

Fix units of momentum, $0<a<b$, external momentum magnitude $k>0$, target energy $E_0>k$ and retained fraction $0<\eta<1$. In the continuum free magnetic scalar channel let $p,q$ be the magnitudes of the two massless momenta and write $E=p+q$, $z=p-q$. Up to a common positive constant the squared norm integrates against
$$
 d\nu=\big[(E^2-k^2)^2+(k^2-z^2)^2\big]\,dE\,dz/k,\qquad E>k,\quad |z|<k .
$$
The tensor contraction and the change of variables are derived in the [momentum calculation](../../flow-momentum/spectrum.md). For $s,t\in[a,b]$, define
$$
 A_{s,t}(p,q)=\tfrac12(e^{-sp^2-tq^2}+e^{-tp^2-sq^2}),\qquad
 \chi(F;c)=\frac{\sum_i |c_i|\|A_{s_i,t_i}\|_\nu}{\|F\|_\nu},
 \qquad F=\sum_i c_i A_{s_i,t_i}\ne0 .
$$
Let $\chi_\epsilon$ be the infimum over all finite representations retaining at least $\eta$ of their squared norm in $|E-E_0|\le\epsilon$. Then
$$
                   \log\chi_\epsilon=\Theta(\epsilon^{-2})\qquad(\epsilon\downarrow0).
$$
Both constants may depend on the five fixed parameters. The same order holds if the pair coefficients must form a real rank-one positive semidefinite matrix on a common grid. The matrix entries can have either sign. If the entries all have one sign, the attainable fraction is $\Theta(\epsilon)$ uniformly over the choices: scale their sum to one and sandwich $|F|$ between $e^{-b(p^2+q^2)}$ and $e^{-a(p^2+q^2)}$. The norms of the envelopes are finite and positive and their marginal energy densities are continuous and positive near $E_0$. With a single shared clock, even signed combinations have a ceiling of order $\sqrt\epsilon$. [Shared-clock conditional measure](../../flow-basis/moving.md)

## Lower bound for every representation

Use $x=E^2-k^2$ and $x_0=E_0^2-k^2>0$. Write $H=L^2(x^2\,dx\,dz)$ on the same strip and set $G=e^{-dx}F$ for a fixed $d>0$. In these variables the physical density relative to $dx\,dz$ is
$$
 \frac{x^2+(k^2-z^2)^2}{2k\sqrt{k^2+x}}.
$$
Thus $\|G\|_H\le C\|F\|_\nu$ globally. On a fixed compact neighborhood of $x_0$ inside $(0,\infty)$ the tilted density $e^{-2dx}x^2$ and the physical density bound each other by positive multiples independently of $z$. Normalize $\|F\|_\nu=1$. For the image $I$ of the energy band we have $|I|=4E_0\epsilon$ and $\|1_I G\|_H\ge c\sqrt{\eta}$.

At fixed $z$, each tilted symmetric atom equals
$$
 e^{-(s+t)(k^2+z^2)/4}e^{-A x}\cosh\!\left(B\sqrt{k^2+x}\right),\quad
 A=d+(s+t)/4,\quad B=(s-t)z/2 .
$$
The even combination is important. Use the orthonormal Laguerre basis
$\ell_n(x)=e^{-x/2}L_n^{(2)}(x)/\sqrt{(n+1)(n+2)}$ in $L^2(x^2dx)$. Integration of the Laguerre generating function gives the coefficient of $e^{-wx}$, for $\operatorname{Re} w>0$,
$$
 b_n(w)=\frac{\sqrt{(n+1)(n+2)}}{(w+1/2)^3}
                \left(\frac{w-1/2}{w+1/2}\right)^n .
$$
Circles of a common radius $\rho>0$ about all possible $A$ lie in a compact subset of the right half-plane. On these circles the modulus of the ratio is bounded by a common $q_*<1$. Since
$(k^2-\partial_A)^j b_n=(-1)^j e^{A k^2}\partial_A^j(e^{-A k^2}b_n)$, the Cauchy estimate bounds this expression by $C(n+1)q_*^n j!\rho^{-j}$. Expand the cosh in even powers. The sum of $|B|^{2j}j!\rho^{-j}/(2j)!$ converges uniformly. In the original integrals the summed series is dominated, at fixed $n$, by a polynomial times $e^{-(A+1/2)x+|B|\sqrt{k^2+x}}$. This proves geometric decay of the coefficient uniformly over $s,t,z$. [Laguerre generating function, NIST DLMF §18.12](https://dlmf.nist.gov/18.12.E13)

Let $\Pi_N$ project onto the first $N$ Laguerre modes in each $z$ fiber. For any $q_*<q_1<1$, Parseval and integration over the bounded $z$ range give a tail at most $Cq_1^N$ per tilted atom. Every physical atom dominates the same positive integrable lower envelope in norm. Summing the tails gives $\|(1-\Pi_N)G\|_H\le C\chi(F;c)q_1^N$.

On the fixed interior neighborhood of $x_0$, the uniform fixed-argument Laguerre asymptotic gives $|\ell_n(x)|\le C(n+1)^{-1/4}$. Therefore on each fiber, pointwise Cauchy–Schwarz on the first $N$ coefficients and integration over $I$ give a squared operator norm for $1_I\Pi_N$ of at most
$$
  \int_I \sum_{n<N}|\ell_n(x)|^2x^2\,dx\le C\epsilon\sqrt N.
$$
Integrate the same bound in $z$. With $N=\lfloor c_0/\epsilon^2\rfloor$ and $c_0>0$ sufficiently small, the low-mode contribution to $\|1_I G\|_H$ is at most $c\sqrt{\eta}/2$. The remaining tail forces $\chi(F;c)\ge c' q_1^{-N}$ for all small $\epsilon$. [Laguerre interior asymptotic, NIST DLMF §18.15(iv)](https://dlmf.nist.gov/18.15.E14)

## A rank-one construction attaining the order

Choose $m\ge2$, $N=2(m-1)$, $h=(b-a)/N$, $p_0=E_0/2$ and $\theta(p)=2\arcsin\sqrt{1-e^{-hp^2}}$, $\theta_0=\theta(p_0)$. With continuous values at removable singularities, define
$$
 D_m(\theta)=\left(\frac{\sin(m\theta/2)}{m\sin(\theta/2)}\right)^2,\quad
 H_m(\theta)=D_m(\theta-\theta_0)+D_m(\theta+\theta_0),\quad
 L_m(p)=e^{-ap^2}H_m(\theta(p))^2,\quad F_m=L_m(p)L_m(q).
$$
In $X=e^{-hp^2}$ we have $\cos\theta=2X-1$. The finite Fourier expansion gives
$$
 H_m=2/m+(4/m^2)\sum_{j=1}^{m-1}(m-j)\cos(j\theta_0) T_j(2X-1).
$$
After squaring, the degree is at most $N$. Thus $L_m$ uses the clocks $a+jh$, $0\le j\le N$. The three-term recurrence gives $\|T_j(2X-1)\|_{\mathrm{coeff},1}\le 7^j$ by induction. Multiplication of polynomials and the rank-one product cost at most $\exp(Cm)$ in coefficient sum. The symmetric atoms give exactly the same product since the pair coefficients are $c_i c_j$. [Chebyshev polynomials, NIST DLMF §18.5](https://dlmf.nist.gov/18.5.E1)

In $u=\sqrt m(p-p_0)$ and $v=\sqrt m(q-p_0)$, the normalized squared-norm laws converge to the product of two densities proportional to $\operatorname{sinc}^8(cu)$, $c=\sqrt{(b-a)/2}$, with $\operatorname{sinc} w=\sin(w)/w$. Indeed $m(\theta(p)-\theta_0)/2\to cu$ at fixed $u$. The reflected kernel tends to zero since $p_0>0$ and $m^2\sin^2((\theta+\theta_0)/2)$ grows linearly in $m$. The physical weight is smooth and strictly positive at $(p_0,p_0)$, in the interior of the allowed triangle, and $dE\,dz=2\,dp\,dq$.

For domination, on $0\le p\le C_0\sqrt m$ the derivative
$$
 \theta'(p)=2\sqrt h\,\frac{\sqrt h\,p\,e^{-hp^2/2}}{\sqrt{1-e^{-hp^2}}}
$$
is bounded above and below by positive multiples of $m^{-1/2}$, with its continuous value at zero. Both kernels are bounded by $C/(1+m(p-p_0)^2)$ there. For the reflected term use $\sin^2((\theta+\theta_0)/2)\ge\sin^2((\theta-\theta_0)/2)$. For $p>C_0\sqrt m$ each denominator sine is bounded away from zero for all sufficiently large $m$, and the factor $e^{-ap^2}$ provides an exponentially small tail, including any fixed polynomial moment. In the first region the squared field is bounded by $C(1+u^2)^{-4}$. This bound absorbs the degree-four physical weight and a further quadratic moment, in both variables. Dominated convergence therefore gives $\|F_m\|_\nu^2\asymp m^{-1}$ and
$$
 m\,\mathbb E_m[(E-E_0)^2]\ \longrightarrow\
 2\,\frac{I_6}{c^2 I_8}=\frac{210}{151(b-a)},\qquad
 I_j=\int_0^\infty \sin^8(w)w^{-j}\,dw .
$$
Here $I_6=\pi/12$ as in the [threshold profile](../../flow-basis/threshold/profile.md), and $I_8=151\pi/630$. For the latter, $128\sin^8w$ is the linear combination of $1-\cos(tw)$ with $(t,\text{weight})=(2,56),(4,-28),(6,8),(8,-1)$. The terms of degrees 2, 4 and 6 cancel. After subtracting them from each term, six integrations by parts reduce the integral to $-\pi t^7/10080$ using $\int_0^\infty(1-\cos y)y^{-2}dy=\pi/2$. The signed seventh-power sum is $-309248$.

Choosing $m=\lceil C_\eta/\epsilon^2\rceil$ with sufficiently large $C_\eta$ puts at least $\eta$ in the band by the second-moment bound. Each atomic norm is uniformly bounded above, so normalization costs only a factor of order $\sqrt m$ beyond the coefficient sum. This proves the upper bound using $O(\epsilon^{-2})$ clocks on each field.

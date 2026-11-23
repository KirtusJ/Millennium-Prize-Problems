# Recovering a correlation-length covariance from earlier times

Let $M_r=\int_0^1 u^r\,d\nu(u)$ be the buffered, centered Wilson moments and let $B\ge M_0$. Fix an integer target $j\ge1$. Ordinary correlations up to time $2+2d$ determine the integral of any degree-$d$ polynomial in $u$. Bailas, Hashimoto and Ishikawa use this shifted Chebyshev basis for lattice transfer observables. Sachdeva and Vishnoi derive the random-walk approximation of monomials. Here the target varies with the unknown Wilson gap, and the error must be measured relative to the vanishing normalization. [Wilson moment representation](README.md) · [Bailas, Hashimoto and Ishikawa, §2](https://arxiv.org/abs/2001.11779) · [Sachdeva and Vishnoi, §3](https://sachdevasushant.github.io/pubs/fast-algos-via-approx-theory.pdf)

## A finite interval with an exact remainder

For $0\le d\le j$ put $p_{j,d}(u)=\sum_{\ell=0}^d a_\ell T_\ell(2u-1)$, where $a_0=4^{-j}\binom{2j}{j}$ and $a_\ell=2\,4^{-j}\binom{2j}{j+\ell}$ for $\ell>0$. Writing $u=(1+\cos\theta)/2$ and expanding $\cos^{2j}(\theta/2)$ proves the identity $p_{j,j}=u^j$. With $q_{j,d}=1-\sum_{\ell=0}^d a_\ell$,

$$
 \|u^j-p_{j,d}\|_{\infty,[0,1]}=q_{j,d}
   =\Pr(|X-j|>d)\le 2e^{-d^2/j},
 \qquad X\sim\mathrm{Binomial}(2j,1/2).
$$

The upper bound follows from the two elementary binomial Chernoff tails, or by applying $\cosh(t/2)^{2j}\le e^{jt^2/4}$ and optimizing $t$. Equality of the uniform error with the exact omitted mass is attained at $u=1$. Therefore $M_j$ lies within $Bq_{j,d}$ of $\int p_{j,d}\,d\nu$.

Expand $p_{j,d}=\sum_{r=0}^d c_r u^r$. If $M_r\in[l_r,h_r]$, bound $\sum c_r M_r$ termwise, reversing endpoints for negative $c_r$, then widen both ends by $Bq_{j,d}$. Intersect with $[0,B]$ and the bounds from moment monotonicity. Uniform input errors $\delta$ about a center contribute at most $\delta\sum|c_r|\le\delta(3+\sqrt8)^d$. Indeed the roots of $T_\ell(2u-1)$ lie in $(0,1)$, so its monomial coefficients alternate and their absolute sum is $T_\ell(3)\le(3+\sqrt8)^\ell$. Degree zero contributes one. The exact signed-coefficient interval can be substantially narrower. At $d=j$ simply use the supplied target interval.

For $N=2+2J$ and $J\ge1$, the even time just below or equal to $N/2$ has index $h=\lfloor(J-1)/2\rfloor$. Given enclosures $I_h=[L_h,U_h]$ and $I_J=[L_J,U_J]$ with $L_J>0$, the midpoint ratio lies in $[L_h/U_J,U_h/L_J]$. The ratio between adjacent moments tends to one at all diverging times. Thus even rounding at either clock changes the asymptotic ratio by a multiplicative $1+o(1)$. For noninteger time use the positive spectral interpolation $\int u^s\,d\nu$ and monotonicity between consecutive integers; one-step Wilson time translations agree with that interpolation at odd separations by positivity of $T$. [Wilson transfer positivity](https://doi.org/10.1007/BF01614090)

One further exact lower bound can help with short input lists. If $l_r>0$ and $r\ge1$, log-convexity gives $M_j\ge l_r(l_r/h_{r-1})^{j-r}$ for $j\ge r$. The calculator uses the largest certified adjacent ratio in its input prefix. For example, exact $M_0=1,M_1=1/2$ already imply $M_{63}\ge2^{-63}$.

## How many earlier times suffice?

The implementation also intersects the ratio interval with $[1,\rho^{-(J-h)}]$ when a certified positive adjacent-ratio lower bound $\rho\le M_r/M_{r-1}$ is available for $r\le h+1$. Every ratio $M_{i+1}/M_i$ for $h\le i<J$ then lies in $[\rho,1]$. This can give a useful upper endpoint even when both individual moments have wide intervals.

With exact inputs, try degrees $0,1,2,4,\ldots$, capped at $j$. Stop as soon as $L_j>0$ and $U_j\le(1+\epsilon)L_j$. For $\epsilon=\epsilon_j\in(0,1]$ with $\log(1/\epsilon_j)=o(j)$, the stopping degree is $o(j)$ along every weak-coupling sequence with $j\to\infty$. To see this, after intersecting with valid bounds, $L_j\ge M_j-2Bq_{j,d}$ and $U_j-L_j\le2Bq_{j,d}$. It suffices that $2Bq_{j,d}\le \epsilon_j M_j/(1+\epsilon_j)$. A sufficient degree is therefore the ceiling of

$$
 \sqrt{j\log\!\left(\frac{4B(1+\epsilon_j)}{\epsilon_j M_j}\right)} .
$$

The [site-scalar lower bound](README.md) makes this $o(j)$, and rounding up to a doubling step costs at most a factor of two. The stopping rule itself never queries the unknown $M_j$ to choose a degree below $j$. Apply the argument to $J$ and $h\sim J/2$ with the same tolerance, for instance $\epsilon_J=e^{-\sqrt J}$. Both enclosures then have vanishing relative width from moments through a common $d=o(J)$. Directly querying all moments up to the earlier time $2+2d$ gives a sublinear range in lattice time.

For interval inputs the finite interval remains valid at every degree. The degree theorem assumes exact correlations. One sufficient accuracy condition at a chosen degree is that $2\delta(3+\sqrt8)^d$ and $2Bq_{j,d}$ together are at most $\epsilon_j M_j/(1+\epsilon_j)$ for intervals of radius $\delta$. This need for precision limits what can be inferred from the available absolute-error estimates at weak coupling. The algorithm takes the integer target clock as external information. A uniform finite upper bound on the computed ratios over a physical family would establish that family's midpoint condition. At present there is no such certified sequence of Wilson inputs. [A4’s single-face error estimate](../../observable-normalization/transfer-increments/local-action/README.md) · [Z4’s condition (C)](../../z4/attempt/A1_REDUCTION.md)

## A quantitative bound for the actual Wilson clock

A4’s mixed-orientation estimate gives the full 24-face field used here, with $M_J$ equal to 16 times A4’s covariance for the quarter-sum of the scaled deficits. At the actual clock it implies $M_J\ge c\beta^{-1/8}\exp(-C J\beta^{-1/64})$. The constants absorb $\xi=2J+O(1)$. The same floor applies to $M_h\ge M_J$. The bound $m\le C'\beta^{-1/7}$ gives $J\ge c'\beta^{1/7}$ on positive-gap sequences. [A4’s clock estimate](../../observable-normalization/transfer-increments/local-action/site-scalar/README.md) · [A4’s seventh-root lattice bound](../../observable-normalization/transfer-increments/spatial-packet/strip/README.md)

Fix $p>0$ and take $\epsilon=\beta^{-p}$. The degree bound above is $O_p(\sqrt{J\log\beta}+J\beta^{-1/128})=O_p(J\beta^{-1/128})$, since $\log\beta=o(J\beta^{-1/64})$. The same degree order works for $\epsilon=\exp(-J\beta^{-1/64})$. Thus the Wilson covariances through time $O(J\beta^{-1/128})$ suffice in principle to enclose both target moments with vanishing relative width. Their ratio interval has upper-to-lower quotient at most $(1+\epsilon)^2$ when both moment intervals meet the tolerance. With the degree prefactor chosen sufficiently large, uniform absolute input radii $\delta\le\exp(-KJ\beta^{-1/128})$ suffice for a sufficiently large constant $K$ by the coefficient bound. These are sufficient accuracies for this procedure. The available Wilson comparison has algebraic absolute accuracy and supplies the denominator floor. Evaluating the Wilson midpoint ratio still requires more precise moment intervals.

## Exact arithmetic

Run the calculator with `python clock.py moments.json`. The JSON object has an integer `target_index` $J\ge1$, an ordered list `moments` of inclusive pairs $[l_r,h_r]$ starting at $r=0$, and an optional `relative_width` in $(0,1]$. Use integers or quoted rational/decimal strings for the endpoints and tolerance. For example `{"target_index":63,"moments":[[1,1],["1/2","1/2"]],"relative_width":"1/100"}` describes two specified moments. The output gives interval endpoints for both times and, when the denominator lower bound is positive, their ratio. A false `width_reached` flag leaves the returned bounds valid. The input intervals must enclose the actual moments of the same nonnegative spectral measure. [Calculator](clock.py) · [Independent rational controls](check.py)

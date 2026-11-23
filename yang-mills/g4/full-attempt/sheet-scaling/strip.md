# The exact growth rate of a one-tile-wide strip

Let $C_m=C_{1\times m}$ be the real-height integral in the [time-refinement estimate](README.md), and set $C_0=1$. For a small spatial magnetic coupling in continuous time, $(\kappa/6)^m C_m$ is the leading coefficient of the normalized Wilson loop around the strip. At each $m$ the spatial period is large enough to contain the embedded rectangle and to make its complement sheet strictly larger.

### From ordered heights to a Bessel quotient

For $S$ a subset of the strip let $P(S)$ be the number of exposed lattice edges. The coarea integral over the positive coordinates with support $S$ is $H(S)$, with $H(\varnothing)=1$ and
$$
 P(S)H(S)=\sum_{i\in S} H(S\setminus\{i\}).
$$
Indeed order the positive heights, lower the smallest to zero, and integrate that common increment against $e^{-P(S)t}$. Coincident heights have measure zero. The signs of the real coordinates split the full integral into $\sum_S H(S)H(R\setminus S)$. $H$ factors on disconnected components because the edge energy splits with exterior heights zero. If $h_k$ is $H$ on $k$ consecutive sites, its perimeter is $2(k+1)$, and deleting site $i$ splits the remaining interval. Therefore
$$
 h_0=1,\qquad 2(k+1)h_k=\sum_{a+b=k-1}h_a h_b \quad(k\ge1).
$$
A nonempty signed strip is a sequence of monochromatic runs of positive lengths, with two choices of the first sign. Its weight is the product of the $h_k$ of its runs. Thus with $H(z)=\sum_{k\ge0}h_k z^k$,
$$
 \sum_{m\ge0} C_m z^m=1+2\frac{H(z)-1}{2-H(z)}
                     =\frac{H(z)}{2-H(z)} .
$$
The recurrence gives $2(zH)'=2+zH^2$. Write $zH=-2z u'/u$. The resulting equation is $zu''+u'+u/2=0$ with regular solution $u(0)=1$, namely $u=J_0(\sqrt{2z})$. Hence $H=2J_1(x)/(xJ_0(x))$ for $x=\sqrt{2z}$. The derivative identity $J_1'(x)=J_0(x)-J_1(x)/x$ yields
$$
 \boxed{\displaystyle \sum_{m\ge0} C_m z^m=\frac{J_1(x)}{xJ_1'(x)},\qquad x=\sqrt{2z}.}
$$
Both sides take the value one at zero. The initial values $C_1=1/2$ and $C_2=7/24$ reproduce the one- and two-tile normalizations. [Bessel equation and defining series](https://dlmf.nist.gov/10.2) · [Derivative identities](https://dlmf.nist.gov/10.6)

### A spatial transfer with the same spectrum at its upper end

Put $w(x)=e^{-2|x|}$ and let $Tf(x)=\int e^{-|x|-|x-y|-|y|}f(y)\,dy$ on $L^2(\mathbb R)$. For $m\ge1$,
$$
 C_m=\langle w,T^{m-1}w\rangle .
$$
The extra endpoint factors give $3|x|$ at either end when $m>1$, and $4|x|$ for one tile. The kernel is symmetric, Hilbert–Schmidt and strictly positive. Its top eigenfunction can be chosen strictly positive and even. Positivity of the quadratic form follows from the Fourier transform $2/(1+\xi^2)$ of the middle convolution. Simplicity of the top eigenvalue also follows directly: a maximizing vector may be replaced by its absolute value; a sign-changing real maximizer would strictly increase its quotient, and two independent top vectors would give a sign-changing one orthogonal to the positive vector. The positive boundary vector has nonzero overlap.

For an even positive eigenfunction with eigenvalue $\lambda$, set $h(x)=e^{|x|}f(x)$. Its equation reads $\lambda h=e^{-|\cdot|}*(e^{-|\cdot|}f)$. The convolution is continuously differentiable and decays at infinity, and
$$
 h''+\big((2/\lambda)e^{-2|x|}-1\big)h=0,\qquad h'(0)=0 .
$$
On the positive half-line the substitution $t=v e^{-x}$, $v=\sqrt{2/\lambda}$, gives the Bessel equation of order one. Decay excludes $Y_1(t)$ at $t=0$. The Neumann condition gives $J_1'(v)=0$ and positivity requires $J_1(t)>0$ for $0<t\le v$. By interlacing this selects the first positive derivative zero. Thus $\lambda_* = 2/v^2$ for $v=j'_{1,1}$. The calculation gives a spatial transfer check on the run recurrence and the endpoint normalization. [Positive zeros and interlacing](https://dlmf.nist.gov/10.21.i)

The top eigenvalue is isolated and simple. From the spectral representation of $C_m$ the generating function has its unique nearest pole at $z_*=v^2/2$. Equivalently, its first positive denominator zero in the Bessel expression is simple. The differential equation gives $J_1''(v)=-(1-v^{-2})J_1(v)$. Expanding the quotient at this pole, the coefficient of $(1-z/z_*)^{-1}$ is $2/(v^2-1)$. Positivity of the operator excludes a negative eigenvalue of the same magnitude, and compactness separates the remainder. Therefore
$$
 C_m\sim \frac{2}{v^2-1}\left(\frac{2}{v^2}\right)^m .
$$
The normalized Wilson coefficient has the additional factor $(\kappa/6)^m$. This rate is for a growing strip at its first nonzero magnetic order. [Exact recurrence and spectral quadrature](check.py)

At finite temporal coupling, integer heights give the analogous operator on $\ell^2(\mathbb Z)$ with kernel $q^{|a|+|a-b|+|b|}$ and boundary vector $q^{2|a|}$. Its top eigenvalue $\lambda(q)$ is the growth rate of $Z_{1\times m}(q)$. Compactness and strict positivity follow by the same arguments, and the middle convolution has positive Fourier series $(1-q^2)/(1-2q\cos\theta+q^2)$. Applying (1) to strips gives $|\log[\epsilon\lambda(e^{-\epsilon})/\lambda_*]|\le2\epsilon$. The time and length limits therefore commute for the strip coefficient as well.

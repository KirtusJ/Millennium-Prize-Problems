# Undifferenced magnetic profiles and polynomial observables

For real $\psi\in C_c^\infty(\mathbb R^3)$ the ordinary magnetic smearing uses $g_r(x)=r^{-1}\psi(x/r)$ on spatial $12$ faces, at a fixed physical time. It has no spatial difference. Under the first-order conditions $L/(r^3\sqrt{\log(2+r)})\to\infty$ and $\beta/(r^{16}\log(2+r))\to\infty$, the commonly rooted vectors have joint continuum Gaussian limits with convergence of all fixed polynomial moments. The covariance in the [spectral calculation](spectrum.md) is $C_0(t)$, with the factor $p_3^{2m}$ replaced by one. Multiple profiles and multiple physical times are allowed. Reflection across axis $1$ makes it possible to recover the part that a finite-support Hodge difference cannot directly estimate.

## Moment form of the Ward bound

In the [growing-box Ward proof](ward.md) every face score, moving-frame error and local cube estimate has the same bound in $L^q$ for every fixed finite $q$; use the exponential single-face estimate and Hölder with larger powers at products. In particular $\|F(w)\|_{L^q}\le C_q\|w\|_1$. For a real linear test $X=F(g)$ replace the characteristic function in Haar integration by $X^{n-1}$, for even $n\ge2$. At fixed regulator this is a bounded smooth cylinder function. Its derivative is $(n-1)X^{n-2}$ times that of $X$. With $v=\|Pg\|^2$ bounded, the expansion gives
$$
 \left|\mathbb E X^n-(n-1)v\,\mathbb E X^{n-2}\right|
 \le C_n e_r(1+\|X\|_{L^n}^{\,n-1}),
$$
where $e_r$ is the sum of the error terms in the Ward proof including the variance correction. For example the score error is paired by Hölder against $X^{n-1}$, the derivative error against $X^{n-2}$, and the coexact and residual errors against $X^{n-1}$. The same finite moment of $X$ on the right suffices for all terms. If $e_r\to0$, induction in $n$ bounds $\|X\|_{L^n}$: a nonnegative $y$ satisfying $y^n\le C+o(1)(1+y^{n-1})$ stays bounded. Convergence in distribution and uniform higher moments now give *all* joint polynomial moments of the difference tests. This applies to general tests with the size and antiderivative bounds used in [smoothing](smoothing.md). The differencing direction may be any spatial axis, and the proof allows weights varying with $r$ if their free covariances converge.

## Recovering the general profile by site reflection

Treat one color of one profile first. Denote its rooted component by $X$. Translate its entire array of scalar weights to $j\lfloor ar\rfloor e_1$, $j=1,\ldots,M$, keeping the color root at zero and using the same ordered paths. Choose a fixed $a$ larger than twice the profile's support radius plus two. Write $Y_M$ for the arithmetic mean of the translated components. Each translated face and its base path lie in the positive half for the site plane $x_1=0$, also when the path initially runs along the time axis in that plane. This is true on the finite periodic box for sufficiently large $r$ with $M$ fixed. Negative translated copies are represented in the same root frame. [Site reflection for the original measure and odd spatial sides](../tangent-curvature/reflection.md)

Let $Z_M=-\theta Y_M$, where $\theta$ is reflection of the entire rooted observable. Reflection reverses the orientation of each $12$ face. Thus $Z_M$ differs from the ordinary positive-orientation sum on the reflected squares, denoted $Y_M^-$, by $O_{M,q}(r^3/\sqrt\beta)$ in every fixed $L^q$. In fact the reflected path is the coordinate path to the reflected base. Replacing the reversed plaquette by its inverse at the positively oriented base $(-x_1-1,x_2,x_3)$ adds a one-edge conjugation in the common rooted frame. This gauged edge has $L^{2q}$ distance $O_M(r/\sqrt\beta)$, and the sum of the absolute weights is $O_M(r^2)$. The sign from inversion is already in the definition of $Z_M$.

Both $X-Y_M$ and $Y_M-Y_M^-$ are first differences in direction $1$ of compact arrays. At fixed transverse coordinates and time their coefficients sum to zero, exactly on the lattice. Take the partial sums along each such line. Their total $\ell^1$ norm is at most its support length $O_M(r)$ times the original $\ell^1$ norm $O_M(r^2)$. This is the $O_M(r^3)$ antiderivative bound needed for $m=1$. The weights have $\ell^\infty$ norm $O_M(1/r)$ as required. Their free covariances converge by the Fourier calculation for undifferenced smooth translated and reflected profiles (bounded spatial translations converge in physical coordinates; the one-cell base shift tends to zero). The difference tests therefore converge with all moments for each fixed $M$.

The reflected-block means can now be removed uniformly after taking the regulator limit. For integer $q\ge1$ put $f_q(y)=\operatorname{sgn}(y)|y|^q$. Site reflection gives $\mathbb E[f_q(Y_M)f_q(Z_M)]\le0$, and $Z_M$ has the same absolute moments as $Y_M$. Consequently
$$
 \sqrt2\,\|Y_M\|_{2q}^q
 \le \|f_q(Y_M)-f_q(Z_M)\|_2
 \le 2q\,\|Y_M\|_{2q}^{q-1}\|Y_M-Z_M\|_{2q}.
$$
The second inequality uses $|f_q(x)-f_q(y)|\le q(|x|^{q-1}+|y|^{q-1})|x-y|$ and Hölder; for $q=1$ it holds directly. Thus $\|Y_M\|_{2q}\le\sqrt2\,q\|Y_M-Z_M\|_{2q}$, also if the left side is zero. For fixed $M$, the last difference has the limiting norm of the corresponding free Gaussian difference of reflected block means. Each free block mean has variance tending to zero as $M\to\infty$. Its Fourier integrand contains $|M^{-1}\sum_{j=1}^M e^{ijap_1}|^2$, which tends to zero almost everywhere and is at most one against the integrable spectral density. The reflected block has the same variance. Hence $\lim_{M\to\infty}\limsup_{r\to\infty}\|Y_M\|_{2q}=0$.

Finally $X=(X-Y_M)+Y_M$. The known difference law and this bound identify the full field. For bounded Lipschitz tests the error tends to zero by the $L^1$ bound. The argument for a finite collection uses one block per component and the triangle inequality. Uniform higher moments for $X$ follow already by fixing one sufficiently large $M$ and using the bounds on the two summands. This gives joint moment convergence by uniform integrability. All observables built from norms are independent of the auxiliary color root rotation on each time slice.

## A shorter box for symmetric profile sampling

There is an additional second-order result. Suppose $\psi$ is even in coordinate $1$, and sample it at the geometric face center in that coordinate, so the weights on each transverse line satisfy $g(x_1)=g(-1-x_1)$. Use $M^{-1}\sum_{j=1}^M(2T_j-T_{2j})g$ for the positive block, with $T_j$ translating by $j\lfloor ar\rfloor e_1$. The coefficients sum to one and their weighted displacements sum to zero. The signed blocks still give real half-tests. $X-Y_M$ is a sum of $(I-T_j)^2g$. For $Y_M-Y_M^-$ the line mass and first moment both vanish: reflection sends a line's moment $m_1$ to $-m_1-m_0$, and the positive block keeps $m_1=-m_0/2$ of the original sampled even profile. Taking partial sums twice yields a compact antiderivative of $\ell^1$ norm at most $O_M(r^2)\,O_M(r^2)=O_M(r^4)$. Each of the two free translated block means still tends to zero. The same proof now applies under $L/(r^2\sqrt{\log(2+r)})\to\infty$ and $\beta/(r^{12}\log(2+r))\to\infty$. Center sampling and node sampling have the same limiting Fourier profile; this second-order cancellation uses center sampling at finite regulator.

## Positive-time readings of the coherent magnetic energy

Take $J=\int\psi\ne0$ and the time-slice observable $Q_r=|X_r|^2/2$. It is bounded at each finite regulator and its limiting distribution is unbounded. The mean tends to $3C_0(0)/2$, the variance tends to $3C_0(0)^2/2$, and
$$
 \operatorname{Cov}(Q_r(0),Q_r(\lfloor rt\rfloor))
       \longrightarrow \tfrac32 C_0(t)^2 .
$$
The limit is positive for every finite $t>0$. The ratio to the mean squared tends to $(2/3)[C_0(t)/C_0(0)]^2$. This is a spatial double sum with parallel transport between its two faces. A spatial sum of individual plaquette energies has different cross terms.

Its limiting connected physical-energy measure is $\tfrac32\mu*\mu$, with $\mu$ the radial pushforward for $m=0$ in the [spectral calculation](spectrum.md). Near zero $\mu(dE)=[|J|^2 E^3/(6\pi^2)+O(E^5)]\,dE$. Thus $C_0(t)\sim |J|^2/(\pi^2t^4)$, and the connected mass below $\epsilon$ is asymptotic to $3|J|^4\epsilon^8/(2\pi^4\,8!)$. For the bounded observable $\exp(-\sigma|X_r|^2)$ the determinant and positive convolution series in the same calculation hold at $m=0$, also with exponent eight. Positive masses on arbitrarily low fixed physical windows prove the stated gap upper bound using either observable.

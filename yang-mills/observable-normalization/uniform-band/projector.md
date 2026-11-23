# Measuring the isolated band with finitely many ordinary lags

On the strong-coupling interval of the [uniform exclusion theorem](README.md), put $Y=S_c/(tb)$ with $b=1-7\beta^2/24$. Its spectrum lies either in $[0,d_0]$ or in $[1-d_1,1+d_1]$, where $d_0=O(\beta^2)$ and $d_1=O(\beta^4)$ independently of volume. Reduce the common interval so both are less than $1/4$. Write $P$ for the upper spectral projection. For $r\ge1$ use the degree-$3r-1$ polynomial
$$
 H_r(y)=\sum_{j=2r}^{3r-1}\binom{3r-1}{j}y^j(1-y)^{3r-1-j}.
$$
At the lower interval, $|H_r(y)|\le 2^{3r-1}d_0^{2r}$. At the upper interval the complementary binomial sum has powers of $1-y$ at least $r$, including when $y>1$. Thus $|1-H_r(y)|\le2^{3r-1}(1+d_1)^{2r}d_1^r$. The spectral theorem gives
$$
 \|H_r(Y)-P\|\le
 \left[8\max\{d_0^2,(1+d_1)^2d_1\}\right]^r .
$$
This applies to every physical vector at once and also in the infinite-volume vacuum. For $r=1$ it simply uses $Y^2$. In particular the second connected lag divided by $(tb)^2$ gives the upper-band weight of any centered unit vector to absolute error $O(\beta^4)$, at any sufficiently small fixed positive $\beta$. The target is weight in the actual interacting shell. Its deviation from the Haar weight of a specified observable is a different quantity.

Higher orders involve only lags $2r$ through $3r-1$. If those moments of $Y$ have simultaneous absolute errors at most $\delta$, their polynomial combination has additional error at most $3^{3r-1}\delta$. Indeed the sum of absolute monomial coefficients of $y^j(1-y)^{D-j}$ is $2^{D-j}$ and the full binomial sum of these bounds is $3^D$. Raw transfer correlations require precision commensurate with the powers of $tb$. The convergence guarantee by itself gives no sampling-cost bound.

The upper-band weight of a fixed bounded local slice reading also admits a holomorphic strong-coupling germ on a volume-independent disk. For the centered vector let $h_{r,L}(z)$ be the expectation of the polynomial obtained by replacing $y^j$ by the holomorphic $c_j(z)/b(z)^j$. Each is bounded on $|z|=R$ by $M_G D^r$ with an absolute $D>1$: use the coefficient bound above, $|b|>1/2$ there and $|c_j|\le M_G A^j$. On the real axis the difference of consecutive approximants is $O_{r,L,G}(\beta^{4r})$ by the projector inequality. It has a Taylor zero of that order. The circle estimate on the difference followed by the maximum principle bounds it on the smaller disk by $2M_G D^{r+1}(|z|/R)^{4r}$. For $D(|z|/R)^4<1$ these differences are normally summable on compact sets. The limit agrees with the interacting band weight at positive real coupling. Each Taylor coefficient below degree $4r$ can already be extracted from the lag polynomial $h_{r,L}$; volume dependence is confined to the underlying correlations. The same conclusion for a fixed local test in the bulk follows from convergence of its finite-time moments and the uniform bounds. No analyticity in physical continuum units is asserted.

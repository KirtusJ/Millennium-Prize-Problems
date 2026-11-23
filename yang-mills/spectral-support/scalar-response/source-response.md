# Local and integrated action response

Keep the local source normalization $Y_f=\beta\sum_p f_pD_p$ fixed when varying $w$. For $w=\mathbf1+\sum s_i f_i$ one has, exactly at every positive $\beta$,
$$
 \kappa(Y_{f_1},\ldots,Y_{f_m})=(-1)^m\partial_{s_1}\cdots\partial_{s_m}\log Z .
$$
The compact integral can be differentiated under the integral sign. The cumulant generating function is the logarithm of the partition-function ratio with the opposite sources. In particular, $-\partial_{s_h}V_{fg}=\kappa(Y_f,Y_g,Y_h)$. This holds for intersecting supports too. When $V_{fg}>0$, division by $V_{fg}$ gives the logarithmic sensitivity of the pair.

At $w=\mathbf1$ put $H_i=B^\top\operatorname{diag}(f_i)B$. The leading pair and triangle are
$$
 V^0_{ij}=\tfrac32\operatorname{tr}(CH_iCH_j),\qquad
 T^0_{123}=3\operatorname{tr}(CH_1CH_2CH_3).
$$
Differentiate the Gaussian log determinant and use $\partial_i C=-CH_iC$. The two orders in the triangle are equal by transposition and cyclicity, since $H_i$ and $C$ are symmetric. The next terms are $V^1_{ij}=\partial_{ij}A$ and $T^1_{123}=-\partial_{123}A$. For $R=T/\sqrt{V_{12}V_{13}V_{23}}$ with positive leading pairs this gives
$$
 R_1=\frac{T^1-(T^0/2)\sum_{i<j}V^1_{ij}/V^0_{ij}}
 {\sqrt{V^0_{12}V^0_{13}V^0_{23}}}.
$$
These differentiations account for changes in the denominator as well as the observable insertion.

## The all-plaquette identity

Let $V_{fg}(\beta)=\beta^2\operatorname{Cov}_\beta(D_f,D_g)$ with $D_f=\sum f_pD_p$. For the all-ones insertion,
$$
 \sum_p\kappa(Y_f,Y_g,Y_p)=2V_{fg}-\beta\,dV_{fg}/d\beta .
$$
This follows from the derivative of the normalized integral and the two explicit factors of $\beta$. Equivalently, multiplying every source weight by $u$ replaces the pair by $u^{-2}V_{fg}(\beta u)$ when the insertions retain the original $\beta$. The Gaussian integrated coefficient is $2V^0_{fg}$ and the first correction is $3V^1_{fg}$. The latter also follows without differentiating an asymptotic remainder in $\beta$, since $A(uw)=A(w)/u$ gives the identity directly for weight derivatives.

For the two end cells at times 0 and 4 on the $5\times1^3$ box, the exact sum splits as follows. A face belongs to the first applicable row. Rounded entries are contributions to the *unnormalized* integrated triangle.

| Third insertion | Faces | Gaussian coefficient | Wilson first coefficient |
|---|---:|---:|---:|
| Face in an endpoint cube | 48 | 0.0003229932 | 0.0014997166 |
| Other face meeting an endpoint link | 24 | −0.0002691497 | −0.0010513921 |
| Face of the link-disjoint middle cube | 24 | 0.0001347261 | 0.0007438158 |

Exact rational sums give $2V^0_{fg}$ and $3V^1_{fg}$ respectively. The variation over all weights combines terms of both signs, including overlapping plaquettes. Only the last row directly samples the separated middle cube. [Exact decomposition](evidence/coefficients.json)

**Infinite time at fixed spatial box.** The integrated identity also holds for bounded local plaquette probes in the transfer vacuum at fixed finite spatial volume and fixed positive $\beta$. Take a periodic time cylinder, counting every spatial and temporal plaquette once. In temporal gauge on the gauge-invariant space use the Wilson transfer kernel with half the spatial action at each endpoint. One may equivalently average the intervening temporal links. At fixed spatial volume the resulting kernel is continuous, strictly positive, and bounded above and below on the compact link product. It is compact, positivity improving and analytic in $\beta$ in operator norm. Its leading eigenvalue is simple and separated in modulus. Locally in $\beta$ the leading eigenprojection and eigenvalue are analytic, and the normalized powers on the complementary subspace are bounded by $Cq^n$ for some $q<1$ by spectral separation. On the full link space gauge averaging maps into the invariant space, with the same nonzero spectrum.

A fixed cylinder insertion gives a bounded kernel by integration over its finitely many intervening slices. The cylinder trace converges locally analytically to its vacuum expectation: isolate the leading projection in the long empty time interval; two factors of the Hilbert–Schmidt kernel suffice to bound the trace of the remainder. The power estimate is uniform on a small complex neighborhood, justifying differentiation of the finite-time identity. Alternatively, for an inserted third face a distance $d$ along the time circle from the fixed interval containing the first two, subtract the rank-one contribution between the clusters. The connected cumulant is $O(q^d)$, with $d$ the shorter time distance and a fixed number of faces per slice. This proves absolute summability and yields the infinite-time sum including all contact slices. The constants here depend on spatial volume and $\beta$. This argument extends the exact response identity. The open-box saddle coefficients use different boundary conditions.

## Independent compact-group control

The six faces of one open three-dimensional elementary cube form a sphere. Expanding each central Wilson weight in characters and integrating each shared link by Schur orthogonality leaves one dimension label $n=2j+1$ common to all faces. The face coefficient per dimension is $2e^{-x_p}I_n(x_p)/x_p$ by the $SU(2)$ class integral; the Euler characteristic contributes $n^2$. Thus
$$
 Z=\sum_{n=1}^\infty n^2 \prod_p 2e^{-x_p}I_n(x_p)/x_p,\qquad x_p=\beta w_p.
$$
For $S=\sum_p w_p^{-1}$ the first coefficient obtained from this independent expression is
$$
 A_{\rm sphere}=\frac1{24}\sum_p\left(\frac3{w_p}
       -\frac{18}{S w_p^2}+\frac{15}{S^2 w_p^3}\right).
$$
To see the coefficients, put $u=n/\sqrt\beta$ in the Fourier integral of $e^{-x}I_n(x)$. The first correction to its Gaussian Fourier transform is $(z^4-6z^2+3)/(24x)$ with $z=n/\sqrt x$. The leading sum tends to the three-dimensional radial Gaussian with weight $u^2 e^{-Su^2/2}$; its second and fourth moments are $3/S$ and $15/S^2$. Poisson summation of the even polynomial times Gaussian gives exponentially small mesh error, with zero term annihilated by $u^2$. For control of the first correction truncate at $n=\sqrt\beta\log\beta$. A contour shift in the Bessel integral bounds the omitted tail by a Gaussian until $n$ is of order $\beta$ and exponentially beyond. On the retained range the absolute Gaussian Fourier Taylor remainder for each face, after removal of its leading $x^{-1/2}$ factor, is $O(x^{-2})$ uniformly in $n$. Its contribution after the radial sum is $O(\beta^{-2}\log^3\beta)=o(\beta^{-1})$. Equality for positive weights identifies the analytic coefficient and its derivatives.

At unit weights $A=5/48$. For three distinct single faces the tree pair and triangle are $1/24$ and $-1/72$. The first coefficients are $7/288$ and $-11/1728$. Direct differentiation of the character sum at finite coupling gives an independent test: average over $n$ with its normalized positive weight. The mixed derivatives for distinct faces are the covariance and third cumulant of the individual logarithmic face scores, with a minus for the three-insertion observable. The finite-$\beta$ tests recover both slopes at the recorded precision. [Character and group-word checks](check_words.py) · [Source and spanning-tree tests](check_response.py)

## A bulk annulus with a specified normalization

The choice of 24 faces in a four-cube fixes a perturbative matching factor. Take generators $\sigma^a/2$, spacing $a$, canonical smooth curvature $F^a_{\mu\nu}$ and Wilson $\beta=4/g_{\rm YM}^2$. At tree level one face gives $\beta D_p=a^4\sum_a(F^a_{\mu\nu})^2/2$ to leading order. Four parallel faces occur for each $\mu<\nu$, so the full cube gives $a^4F^2$, where $F^2=2\operatorname{Tr}(F_{\mu\nu}F_{\mu\nu})$ sums both orders of the spacetime indices. In the bulk, summing cube sources around a shell counts each interior plaquette four times. Summing individual plaquettes once instead requires the corresponding factor of four.

For a single spherical shell about one endpoint, keep $a\ll\rho<\sigma\ll|y|$ and both physical separations perturbative. Divide the integrated connected three-point function by the endpoint covariance. The continuum spin-zero OPE coefficient $4\beta_0g^2/(\pi^2|x|^4)$ predicts $8\beta_0g^2\log(\sigma/\rho)$ for its leading shell contribution. The angular volume in four dimensions is $2\pi^2$. In the source's 't Hooft convention $g^2=2g_{\rm YM}^2$ for $SU(2)$ and $\beta_0=11/(48\pi^2)$ in the pure theory. At leading matching order this gives $(44/(3\pi^2))\log(\sigma/\rho)/\beta$. The corresponding scalar-projected normalized short-pair ratio has coefficient $11/(18\pi^2)$ per $1/\beta$. These predictions assume control of scale logarithms or a running-coupling treatment, and leading power in the squeezed geometry. They refer to the unfiltered bulk field. The signed profiles in this folder test different observables. An actual Wilson derivation of the shell coefficient needs the angular projection, control of the finite free contribution, and a uniform cutoff and boundary analysis. [Becchetti and Bochicchio, §§2.3, 3.2 and 4.1](https://arxiv.org/abs/1810.08527)

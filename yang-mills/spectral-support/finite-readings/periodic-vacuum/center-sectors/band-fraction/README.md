# How much of the one-site vacuum tensor signal lies in the measured band?

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00) · Submitted for disproof

On the three-link, one-spatial-site SU(2) Wilson regulator at β=4, **more than 88.8% of the vacuum variance** of $O=(s_1-s_2)/\sqrt2$ lies between $\log(7/3)$ and $\log 3$ in lattice energy. The absolute weight exceeds **0.0736**. The same band carries more than 88.8% of the zero-temperature correlator at every integer time separation. This answers a question about C4's calibration model. The fraction of a finite-period measurement due to vacuum transitions and the lower mass gap in the continuum remain open. [C4's operator and original certificate](../README.md) · [Directors' period comparison](../../period-doubling/README.md) · [Wilson transfer positivity](https://doi.org/10.1007/BF01614090)

## Angular quadrature read-back

Write $u=n_1\cdot n_2$, $v=n_1\cdot n_3$, $w=n_2\cdot n_3$ for three independent uniform directions on the sphere. For a monomial $u^iv^jw^k$, integrate $n_3$ first by pairing its Cartesian components. If $j+k$ is odd the moment vanishes. Otherwise, pair $r$ slots belonging to $n_1$ with $r$ belonging to $n_2$. The remaining within-direction pairs give one, the cross pairs give $u^r$, and integrating $u$ gives $1/(i+r+1)$ for even $i+r$. Thus for even $j+k$ the moment equals

$$
\frac{1}{(j+k+1)!!}
\sum_{\substack{0\le r\le\min(j,k)\\j-r,\ k-r,\ i+r\ {\rm even}}}
\binom jr\binom kr r!\,(j-r-1)!!(k-r-1)!!\,\frac{1}{i+r+1}.
$$

Here $(-1)!!=1$. This is the spherical Wick formula specialized to three dimensions. It agrees in rational arithmetic with C4's azimuthal integration on **all 4,555 distinct monomials** in our covering set. The set takes the pairwise products of all angular basis terms across the two certified sectors and multiplies them by every even-power monomial arising from up to 18 powers of the potential. [Vignat and Bhatnagar, theorem for the uniform sphere](https://arxiv.org/pdf/0709.1999)

C4's change of variables gives $w=uv+\sqrt{1-u^2}\sqrt{1-v^2}z$, with arcsine-distributed $z$. Integrating the $z$ rule first kills its odd powers. The surviving terms have degree at most $i+k$ in $u$, $j+k$ in $v$, and at most $k$ before integration in $z$. The two marginal polynomials are even in their respective variables throughout the covering set. The maximum of these three degrees is 44. Including the squared observable gives radial degree at most $2\cdot6+2\cdot18+4=52$ in the even sector. The order-32 rules are exact through degree 63. The positive quadrature and the Haar integral each incur at most the parent certificate's uniform Chebyshev error $\delta$ on replacing the exponential by its polynomial. The resulting operator error for $L^*O^2L$ is at most $2\delta$, since $\|O^2\|\le1/2$. [NIST Gaussian quadrature](https://dlmf.nist.gov/3.5#v) · [NIST modified Bessel expansion](https://dlmf.nist.gov/10.35.E2)

## Tightening the projection estimate

Use C4's $L=A P\sqrt K$, $T_P=LL^*$, $M=L^*L$, $J=L^*OL$ and unit physical trial vectors $f_i=Lv_i/\|Lv_i\|$. In the all-even center and inversion singlet sector, the largest omitted electric product for degrees below 16 is approximately 0.00021901166908, attained at permutations of $(6,4,0)$. Rational Bessel bounds also cover the infinite tail, since the factors are at most one and decrease above degree 16. Consequently $0\le T-T_P\le eI$ with $e=0.00022$. The parent compressed bounds give $\|L\|\le\sqrt{0.0529}=0.23$, $\lambda_0\in(0.0526,0.05312)$, and excited eigenvalues in this sector below 0.02062. [Original enclosure and cutoff proof](../README.md)

For each trial, center the missing operator at $eI/2$. With $a_0=0.052695$, $a_1=0.0200$ and $b_i=a_i+e/2$, the spectral theorem gives

$$
\|(T-b_i)f_i\|\le 0.23\,\frac{\|(M-a_i)v_i\|}{\|Lv_i\|}+e/2.
$$

Let $t=\|(T-b_0)f_0\|/(b_0-0.02062)$, using its certified upper bound. The norm of the component of $f_0$ perpendicular to the vacuum is at most $t$. After choosing the vacuum phase, $\|f_0-\Omega\|\le t\sqrt{2/(1+\sqrt{1-t^2})}$. Let $P_B$ project onto $(\lambda_0/3,3\lambda_0/7)$. Dividing the second residual by the distance from $b_1$ to the allowed band complement bounds $\|(I-P_B)f_1\|$ by $d$. The new matrix $H=L^*O^2L$ encloses $\|Of_0\|^2=v_0^*Hv_0/\|Lv_0\|^2$. Both this enclosure and the $J$ amplitude use the same trial vectors.

| Outward consequence | Bound |
|---|---:|
| $\|Of_0\|^2$ | < 0.081447 |
| $\|f_0-\Omega\|$ | < 0.003546 |
| $|\langle f_1,O\Omega\rangle|$ | > 0.275868 |
| $\|O\Omega\|$ | < 0.287896 |
| $\|(I-P_B)f_1\|$ | < 0.050813 |

To see how the last three quantities constrain the weight, write $x=O\Omega$, let $m$ be the lower overlap bound, and let $U$ be the upper norm bound. Set $h=P_B f_1/\|P_B f_1\|$. Its inner product with $f_1$ is at least $\sqrt{1-d^2}$. Choose the sign of $x$ for positive overlap. Decomposing $h$ and $x$ along $f_1$ and applying Cauchy–Schwarz on its perpendicular space gives

$$
\|P_B x\|\ge m\sqrt{1-d^2}-d\sqrt{U^2-m^2}.
$$

Applying the same inequality to $x/\|x\|$ with overlap at least $m/U$ gives the fractional bound. The unrounded interval computation gives absolute weight above 0.0736190 and fraction above 0.8882226.

## Positive-time correlator

Exchanging the first two links reverses $O$ and preserves the unique vacuum, so $O\Omega$ has zero vacuum component. Every other eigenvalue in its symmetry sector is below $0.02062<3(0.0526)/7$. The spectral measure outside $B$ therefore lies at $\lambda/\lambda_0\le1/3$, while all the measure in $B$ has $\lambda/\lambda_0>1/3$. At lag $t$ the positive weights in $B$ retain at least $3^{-t}$ of their initial mass and the complementary weights retain at most $3^{-t}$. Dividing by the full positive correlator proves the stated lower bound at every lag. At temporal period 48 the Gibbs trace also contains transitions from excited states. Their initial states and matrix elements fall outside this argument.

## Reproduction

Run the [parent certificate](../certify.py), then run `OPENBLAS_NUM_THREADS=2 python check.py` from this directory with NumPy and SciPy and assertions enabled. The [check](check.py) reuses C4's outward binary64 matrix arithmetic and independently compares angular moments by Cartesian contraction. The angular audit does not supply an independent implementation of that interval arithmetic. Three PCP OS guest runs generate the [Lean source](VacuumBand.lean) for the centered scalar tail, perpendicular norm, Hilbert-space overlap inequality, degree arithmetic, and order-preservation step at positive lag. The infinite-dimensional spectral reduction and the quadrature-to-operator estimate are analytic arguments. [Guest runner](../../../../../observable-normalization/transfer-increments/replay-guests.py)

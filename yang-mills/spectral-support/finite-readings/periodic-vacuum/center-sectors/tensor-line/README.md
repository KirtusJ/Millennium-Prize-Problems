# Resolving the one-site vacuum tensor line

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00) · Submitted for disproof

The tensor signal previously enclosed in a band on the one-site SU(2) Wilson regulator at β=4 comes from **one energy of multiplicity two**. In lattice units its energy satisfies **0.9681 < E < 0.9694**. A distinct scalar level satisfies **1.1830 < E < 1.1847** and has zero overlap with the vacuum tensor observable. These enclosures contain Z4's independently computed point estimates of 0.968930 and 1.184132. The multiplicities here refer to the gauge singlet sector even under each link inversion and each center flip. B4's sector ordering identifies the doublet as the first excitation of the entire center-neutral space, giving the same energy enclosure for the one-site neutral gap. C4 encloses the full one-site gap at 0.061–0.063 in the charged sector. The continuum mass gap and the limit in spatial volume remain open. [B4's sector ordering](../full-gap/README.md) · [C4's charged and thermal estimates](../static-floor/README.md) [C4's transfer and basis](../README.md) · [A4's band-weight certificate](../band-fraction/README.md) · [Z4's numerical levels](../../../../../z4/attempt/reviews/g2-three/report.md) · [Lüscher on positivity of Wilson transfer](https://bib-pubdb1.desy.de/record/396349)

For $O=(s_1-s_2)/\sqrt2$, with $s_i=|\mathrm{Im}\,U_i|^2$, this doublet carries more than 0.0736 absolute vacuum weight and more than 88.8% of the equal-time variance. Other tensor lines decay faster. At lag four the doublet supplies more than **99.72%** of the vacuum correlator. At lag eight the effective energy exceeds the doublet energy by **less than 0.000059** lattice units. At temporal period 48, combining the same line with C4’s thermal bounds shows that vacuum transitions into this doublet supply **more than 82.06% of the signed four-lag contrast**. This percentage uses the signed population contrast in the denominator.

## Counting levels by symmetry

Order the full transfer eigenvalues in the specified even sector in decreasing order with multiplicity, starting at $\lambda_1=\lambda_0^{\rm vac}$. Let $P$ be the electric cutoff from C4 and $L=A P\sqrt K$, with $T=AKA$, $M=L^*L$, $T_P=LL^*$. Two upper bounds for $T$ follow from min–max on the retained matrix and the previously certified $0\le T-T_P\le eI$, $e=0.00022$. We find $\lambda_4<0.016423$ and $\lambda_5<0.007663$. For each bound the checker takes the subspace spanned by the requisite number of lowest candidate columns, encloses the Gram defect and divides the row-sum matrix bound by the lower Gram bound. The original vacuum interval gives $0.016423<\lambda_0^{\rm vac}/3$.

Let $B=(\lambda_0^{\rm vac}/3,3\lambda_0^{\rm vac}/7)$. For any spectral projection commuting with the link permutations, apply it to the three cyclic differences $(s_i-s_j)\Omega$. The resulting real vectors $u,v,w$ have the same length and sum to zero. If one is nonzero, $\langle u,v\rangle=-\|u\|^2/2$, and their two-vector Gram determinant is $3\|u\|^4/4>0$. Every transfer eigenvalue visible to this vacuum tensor therefore uses at least two dimensions. Compactness and the certified positive weight in $B$ give at least one such eigenvalue there. The fourth-eigenvalue bound permits at most two dimensions in $B$ after the vacuum. Consequently $B$ contains precisely one doublet. The earlier upper bound $\lambda_2<0.02062<3\lambda_0^{\rm vac}/7$ also excludes a higher tensor line. A second visible line above the fifth-eigenvalue bound would require five dimensions counting the vacuum.

The fourth level can be labeled directly. In the electric representation $\sqrt K A^2\sqrt K$ the compression to $P$ is $M$; its positive spectrum on the full space agrees with that of $T$ through the factorization by $A\sqrt K$, which commutes with permutations. Take the electric product states with all three angular labels zero, sum them on each of the 12 permutation orbits of radial degrees, and take two dyadic linear combinations. The checker certifies that their $2\times2$ Rayleigh matrix minus 0.013 times their Gram matrix is positive definite, including the integration error. Its determinant is above $0.0000335$. Thus two permutation-invariant states lie above 0.013 by min–max in the invariant sector. The vacuum is one. The doublet's two-dimensional span of cyclic differences contains no fixed vector (the three-cycle has sum of its first three powers equal to zero on this span). The fifth eigenvalue is below 0.013. This forces the other invariant state to be the fourth level, of multiplicity one. Exchanging links 1 and 2 then forbids its vacuum transition through $O$.

## Energy enclosures

Fix a finite trial vector $q$, put $\ell^2=q^*Mq$, $f=Lq/\ell$, $D=T-T_P$, and let $a$ approximate its finite eigenvalue. The residual bounds use the second magnetic moment $H=P\sqrt K A^4\sqrt K P$. For $K_P$ restricted to retained electric states,

$$
0\le \langle f,D f\rangle\le d=
\frac{e}{\ell^2}\left(q^*Hq-\|K_P^{-1/2}Mq\|^2\right).
$$

Indeed $D=A(I-P)K(I-P)A$. The quantity in parentheses is the squared norm of the discarded part of $A^2\sqrt K q$. The relation $D^2\le eD$ gives $\|Df\|\le\sqrt{ed}$. We enclose $\mu=\langle f,Tf\rangle$ by adding $[0,d]$ to the finite physical Rayleigh quotient $\|Mq\|^2/\ell^2$. That finite quotient equals $q^*Mq/\|q\|^2$ plus the variance of $M$ on $q/\|q\|$ divided by its Rayleigh quotient. For the full variance $v=\|(T-\mu)f\|^2$ the bound is

$$
\sqrt v\le 0.23\,\|(M-a)q\|/\ell + \sqrt{ed},
$$

using $\|L\|\le0.23$ from the parent certificate. The numerical trial vectors need neither exact degeneracy nor exact symmetry.

For $H$ the integrand includes $e^{-2V}$, where $0\le V\le24$. The verification squares the enclosed magnetic value at each positive quadrature node. On $[0,48]$ the uniform degree-25 Chebyshev tail, counted once for the true integral and once for the discrete rule, is bounded by
$4\exp(-24+12^2/27)12^{26}/(26!(1-12/27))$.
This follows from the positive Bessel series and the Chebyshev expansion. The verifier upper-bounds the exponential using the reciprocal of a positive Taylor partial sum. The maximum radial degree is $2\cdot6+2\cdot25=62$, within order-32 Gaussian exactness through 63. The same angular parity argument as in the parent calculation applies, with angular degree at most $2\cdot4+50=58$. [NIST Bessel expansion](https://dlmf.nist.gov/10.35.E2) · [NIST Gaussian quadrature](https://dlmf.nist.gov/3.5#v)

If $(a_-,a_+)$ contains just the target eigenvalue $\lambda$ and contains $\mu$, Kato–Temple gives $\mu-v/(a_+-\mu)\le\lambda\le\mu+v/(\mu-a_-)$. The two inequalities come from integrating $(x-a_\pm)(x-\lambda)$ against the trial's spectral measure. Each integrand is nonnegative on its support. For the vacuum use the Rayleigh lower bound and the one-sided upper bound above the excited spectrum. For the doublet use the fourth-eigenvalue upper bound and the vacuum lower bound as endpoints, and for the scalar use the fifth-eigenvalue upper bound and the enclosed doublet lower bound. The checker validates the displayed energy intervals by rational exponential bounds. [Kuroda, Kato–Temple estimate](https://www.kurims.kyoto-u.ac.jp/~prims/pdf/43-2/43-2-24.pdf)

| Trial | Upper bound on omitted mean | Upper bound on standard deviation | Full transfer eigenvalue enclosure |
|---|---:|---:|---:|
| Vacuum | 0.000007132 | 0.00004375 | (0.05269133, 0.05270567) |
| Tensor doublet | 0.000013306 | 0.00005914 | (0.01999279, 0.02001213) |
| Scalar | 0.000014701 | 0.00006244 | (0.01612097, 0.01614222) |

## How quickly the vacuum correlator resolves the line

Write $C(t)=W(\lambda_E/\lambda_0^{\rm vac})^t(1+r_t)$, where $W$ is the doublet weight. The remaining positive weights give $0\le r_t\le (0.112/0.888)(\lambda_5^{\rm upper}/\lambda_E^{\rm lower})^t$ and $r_{t+1}\le r_t$. It follows that $0\le \log[C(t)/C(t+1)]-E\le\log(1+r_t)\le r_t$. Per-lag bounds use the unrounded eigenvalue endpoints. The period-48 transfer trace also admits excited-to-excited transitions. [Vacuum band and positive-lag weights](../band-fraction/README.md) · [Blossier et al. on energy extraction from lattice correlations](https://arxiv.org/abs/0902.1265)

| Lag | Minimum doublet share | Maximum effective-energy excess |
|---:|---:|---:|
| 1 | 95.38% | 0.04835 |
| 2 | 98.18% | 0.01853 |
| 4 | 99.72% | 0.00273 |
| 8 | 99.994% | 0.000059 |

## Attribution of the signed period-48 contrast

C4's four-lag filter is $W=-C(1)+(13/3)C(2)-(13/3)C(3)+C(4)$. The combined temporal orientations of a vacuum pair with ratio $x=\lambda/\lambda_0^{\rm vac}$ give the kernel
$$k_{48}(x)=(x-x^{44})(1-x)(3-x)(x-1/3).$$
The doublet lies above the crossing at $1/3$. All remaining vacuum transitions lie below the crossing and contribute nonpositively. Let $x_-,x_+$ bound the doublet ratio. Its contribution alone is at least
$$D_{48}\ge \frac{0.0736}{Z_{48}}(x_- - x_+^{44})(1-x_+)(3-x_+)(x_- -1/3)>0.001789.$$
The normalized partition upper bound sums C4's three charged upper endpoints at their multiplicities $3,3,1$, adds the vacuum, and allows $1402(0.020764/\lambda_0^{\rm vac})^{47}$ for the remaining spectrum. With C4's signed excited-pair upper bound $0.000391$ and its positive population total, $D_{48}/W\ge D_{48}/(D_{48}+0.000391)>0.8206$. A signed contribution can exceed the total when other transitions cancel. This attribution uses C4's certified inputs directly and makes no statistical assumption about either Monte Carlo stream. [Thermal and trace inputs](../static-floor/README.md)

Run `OPENBLAS_NUM_THREADS=2 python check.py` in this directory after the band-fraction and static-floor certificates. The [interval calculation](check.py) shares C4's quadrature and integer matrix-product implementation. The [Lean declarations](TensorLine.lean) check the Gram determinant argument, the scalar Kato–Temple algebra, the fraction-from-odds step and the signed kernel factorization. Three PCP OS guest runs generated the declarations. The operator construction, symmetry count and quadrature error estimates are analytic arguments. [Guest replay](../../../../../observable-normalization/transfer-increments/replay-guests.py)

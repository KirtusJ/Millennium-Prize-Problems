# The static floor and the signed tensor contrast at one SU(2) site

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00) · **FOR DISPROOF**

At $\beta=4$ and temporal period 48, diagonal tensor matrix elements of the lightest states in the one- and two-center-odd sectors account for **more than 99.9999% of the exact midpoint correlator**. The signed four-lag measurement gives a different answer. Its time-independent part cancels exactly, its full population value is positive, and **vacuum-to-excited transitions supply more than 74% of that signed value**. The full one-site gap lies between **0.061 and 0.063 lattice units** and its first level is threefold degenerate. These computer-assisted bounds concern the full three-link transfer operator and use no confidence assumption about the Monte Carlo data. They substantiate Z4’s proposed origin of the static floor on this regulator. The physical-volume and continuum questions remain open. [Z4’s original hypothesis](../../../../../z4/attempt/reviews/i1-mc3/report.md) · [Earlier finite-period test](../../README.md) · [One-site transfer conventions](../README.md)

## Measurements in a common normalization

Take $O=(s_1-s_2)/\sqrt2$ with $s_i=|\operatorname{Im}U_i|^2$. The equilibrium mean is zero by permutation symmetry. Averaging the two orthonormal tensor components gives the same correlation at every lag. The analytical columns below use this normalization, as do the stored-chain read-backs after restoring both component factors for the period-16 data.

| Period | Enclosed static contribution of the lightest center states | Enclosed full midpoint | Upper bound on midpoint minus that contribution | Archived midpoint ± one chain standard error |
|---:|---:|---:|---:|---:|
| 16 | [0.001121, 0.001446] | [0.001121, 0.002497] | 0.001052 | 0.0016724 ± 0.0002710 |
| 24 | [0.000834, 0.001088] | [0.000834, 0.001108] | 0.0000198 | 0.0008804 ± 0.0000656 |
| 48 | [0.000250, 0.000334] | [0.000250, 0.000335] | $2.00\times10^{-10}$ | 0.0003923 ± 0.0000618 |

The midpoint excess has its own direct bound. Subtracting rounded interval endpoints would discard it. The lower bound on the static share at period 24 is 97.6%. G4's period-48 sample mean is about one estimated standard error above the upper enclosure. The errors measure variation across stored chains (64, 32 and 32 respectively). Fresh sampling would be required for independent statistical confirmation. [Z4’s period-16 source](../../../../../z4/attempt/reviews/i1-mc3/xcheck/b4.json) · [G4’s pinned period-24 and period-48 archive](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/b785aef751f0b699fadbb141f3a986cef7dfeb84/yang-mills/joint-refinement/z4-controls.zip)

The falloff across these two periods also tests the interpretation of a fitted energy. The absolute midpoint ratio $C_{24}(12)/C_{48}(24)$ lies between 3.059 and 3.657. Its logarithm divided by 24 lies between 0.0465 and 0.0541. The lightest state in the isolated one-odd, inversion-even block has energy between 0.061 and 0.063. The two-odd contribution and the change in the thermal partition function both enter the midpoint ratio. Z4’s earlier slope near 0.065 used estimated plateau heights normalized by the separate equal-time readings. These observables and normalizations must be specified before comparing slopes.

## How the center states produce the floor

Let $B=AKA$ denote the positive transfer operator of the parent certificate, $b_0$ its vacuum eigenvalue, and $b_k$ the isolated highest eigenvalue in the inversion-even block with $k$ flipped center characters ($k=1,2,3$). The character multiplicities for $k=0,1,2,3$ are $1,3,3,1$. The eight states are isolated within their own symmetry blocks. Put $r_k=b_k/b_0$ and $Z_T=\operatorname{Tr}(B/b_0)^T$.

| Representative center character | Enclosed $b_k$ | Enclosed diagonal $\langle O\rangle$ in its top state |
|---|---:|---:|
| $(+,+,+)$ | [0.0526909, 0.0527167] | 0 by symmetry |
| $(-,+,+)$ | [0.0495428, 0.0495658] | [−0.0590, −0.0523] |
| $(+,-,-)$ | [0.0463811, 0.0464010] | [+0.0573, +0.0637] |
| $(-,-,-)$ | [0.0431708, 0.0431873] | 0 by symmetry |

Write $d_1,d_2$ for the two nonzero representative diagonals. In each three-character orbit the three diagonals are $d_k,-d_k,0$. This follows by permuting the distinguished link while using equality of the other two link expectations. The center-invariant observable has zero matrix elements between distinct characters. Equal eigenvalues across those sectors therefore add no cross terms. The eight states have the following time-independent contribution at every lag:

$$
S_T=\frac{2d_1^2r_1^T+2d_2^2r_2^T}{Z_T}.
$$

All remaining eigenvalues in the four inversion-even representative blocks lie below 0.020380. The largest upper bound over the other 16 permutation classes is 0.020764. All 64 joint center/inversion characters occur in the 20 classes. These ceilings also identify the **full one-site spectral gap**. The top four intervals are strictly ordered, and even the lowest of the four exceeds every remainder ceiling. The largest eigenvalue below the vacuum is therefore $b_1$, with exact multiplicity three from the three single-odd characters. The checker compares $b_0/b_1$ to rational Taylor bounds on $e^{0.061}$ and $e^{0.063}$, giving $0.061<\log(b_0/b_1)<0.063$. This full-space gap is much smaller than the observed center-neutral tensor energy near 0.969. B4 independently identified the same triplet by ordering the folded real-sign kernels and bounding rational Haar traces. His full-gap enclosure is $0.0543<\Delta<0.0695$. [B4’s sector ordering](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/b6a6c53fc16d9d2cf319a711a3c9712957cd4dee/yang-mills/spectral-support/finite-readings/periodic-vacuum/center-sectors/full-gap/README.md) For a common upper bound $b_R$ on the remainder set $h=b_R/b_0$, and set $h_e$ using only the second eigenvalue ceilings of the inversion-even blocks. G4’s one-step trace estimate gives a remaining unnormalized thermal weight at most $D_T=1402h^{T-1}$. Thus $Z_T$ lies between $Z_8=\sum_k m_k r_k^T$ and $Z_8+D_T$, where $m_k$ are the multiplicities. [G4’s trace estimate](../../../../../joint-refinement/periodic-occupation.md)

The periodic spectral trace at the midpoint weights an unordered unequal-state pair by $2(r_i r_j)^{T/2}|O_{ij}|^2/Z_T$. When both states are in the remainder, the arithmetic–geometric mean inequality and $\|O\|^2\le1/2$ bound their combined contribution, including diagonals, by $D_T/(2Z_8)$. For transitions between a top state and the remainder, $O$ preserves the inversion and center characters. Row summation bounds that contribution by $h_e^{T/2}\sum_k m_k r_k^{T/2}/Z_8$. Both bounds are positive and give the direct midpoint excess in the table. In the ratio of periods, keeping the same $d_1,d_2,b_1,b_2$ in both expressions gives $0.705<(r_1^{24} C_{24}(12)/C_{48}(24))<0.824$. [Thermal trace in lattice spectroscopy, Eq. (5)](https://arxiv.org/abs/2601.22272) · [Umeda on static contributions in finite-temperature meson correlators](https://arxiv.org/abs/hep-lat/0701005)

## Attribution of the signed four-lag signal

Use $W=-C(1)+(13/3)C(2)-(13/3)C(3)+C(4)$. For a pair whose upper transfer eigenvalue is $b$ and whose lower-to-upper ratio is $x$, the pair contributes its squared matrix element times $(b/b_0)^T k_T(x)/Z_T$, where
$$
k_T(x)=x[-1+x(13/3+x(-13/3+x))]+x^{T-4}[1+x(-13/3+x(13/3-x))].
$$
This accounts for both temporal orientations. At $x=1$ the coefficient vanishes. Transitions in different frequency ranges can have opposite signs.

The neutral transfer eigenvalues of ranks two and three have ratios to $b_0$ in [0.37917, 0.38677]. Higher ranks in the same center- and inversion-even block have ratio below 0.31321. The checker bounds rank three from below by a three-column Rayleigh subspace and rank four from above on a codimension-three subspace. The trial-vector residuals bound leakage outside ranks two and three. Explicitly, if $s_0$ is the vacuum trial’s sine error and $s_E$ the norm of the tensor trial outside this subspace, then its vacuum amplitude is bounded below by the trial overlap minus $s_0+s_E\|O\Omega\|$. Here $\|f_0-\Omega\|\le\sqrt2s_0$ and $\|O\|\le1/\sqrt2$. The enclosed $O^2$ insertion gives vacuum variance below 0.08256. The two-state weight exceeds 0.07189. A4’s independent check gives weight above 0.0736 in the wider band $\log(7/3)<E<\log3$. [A4’s band-fraction analysis](../band-fraction/README.md)

For the vacuum pairs we enclose $k_T$ on the two allowed energy-ratio ranges by interval polynomial evaluation. For each charged top state we separately enclose the component-averaged squared observable $\sum_{i<j}(s_i-s_j)^2/6$ on its eigenvector. This positive operator has spectral width $1/3$, so its expectation changes by at most one third of the trial-state sine error. The allowed interval $0\le x\le b_{k,2}/b_k$ bounds its possible transitions, with $b_{k,2}$ the second eigenvalue ceiling in the same block. For pairs wholly in the remainder, each lag is bounded by $D_T/(3 Z_T)$ by the weighted arithmetic–geometric mean inequality for the two orientations and row summation. Multiplying by the sum of absolute stencil coefficients gives $32D_T/(9Z_T)$.

| Period | Enclosed signed vacuum pairs | Enclosed signed excited pairs | Enclosed total $W$ |
|---:|---:|---:|---:|
| 24 | [0.000717, 0.001500] | [−0.002270, 0.001176] | [−0.001553, 0.002676] |
| 48 | [0.001132, 0.002360] | [−0.000718, 0.000391] | [0.000415, 0.002751] |

At period 48 the lower bound on the vacuum share is $0.001132/(0.001132+0.000391)>0.74$. This share refers to a signed sum and may exceed one if the other terms cancel. At period 24 the enclosure leaves the sign of the total unresolved. As a numerical comparison, the tighter of two finite electric cutoffs gives $W=0.00179530$ at period 48, including $+0.00174410$ from vacuum pairs, $+0.00005868$ from one-odd sectors, $-0.00000730$ from two-odd sectors, and $-0.00000019$ from the three-odd sector. Those point estimates retain only inversion-even blocks. G4’s archived period-48 reading is $0.00191245\pm0.00009707$. [Point calculations at both cutoffs](contrast.py) · [Original four-lag archive analysis](../../check.py)

## Enclosure and reproduction

The four inversion-even blocks use the [parent electric cutoff and outward arithmetic](../certify.py). In addition to $M=L^*L$ and $J=L^*OL$, we integrate $G=L^*A^2L$ with the full squared magnetic weight $e^{-2V}$. For $K_P$ the retained electric diagonal and $f=Lv/\sqrt{N}$, $N=v^*Mv$, the omitted electric contribution can be bounded using
$$
\tau=\|(I-P)Af\|^2=\frac{v^*Gv-\|K_P^{-1/2}Mv\|^2}{N}.
$$
Indeed $L^*f=\sqrt{K_P}P A f=Mv/\sqrt N$. The omitted operator $D=B-LL^*$ then satisfies $\|Df\|\le\epsilon\sqrt\tau$ and $0\le\langle f,Df\rangle\le\epsilon\tau$. With $R=\langle f,Bf\rangle$ and a validated second-eigenvalue ceiling $b_2<R$, the upper bound $R+\|(B-a)f\|^2/(R-b_2)$ follows from Temple’s inequality. Dividing the residual by $a-b_2$ bounds the angle to the isolated top state. For the diagonal expectation of $O$ its spectral width times that sine bounds the error. The squared magnetic weight uses a degree-23 Chebyshev approximation on $[0,48]$. Its uniform error is bounded by $2(12^{24}/24!)/(60000000(1-12/25))$ by the positive Bessel series. The order-32 Gaussian rules integrate the resulting basis products exactly. [Kato–Temple spectral estimates](https://www.kurims.kyoto-u.ac.jp/~prims/pdf/43-2/43-2-24.pdf) · [Bessel expansion, DLMF 10.35](https://dlmf.nist.gov/10.35)

The 16 classes with nontrivial inversion use a coarser electric cutoff of 0.005 to enclose their largest eigenvalues. The radial basis evaluation requires the additional factor $\sqrt{1-x_i^2}$ for odd angular $l_i$. When $\sum_i l_i$ is odd, the scalar singlet under proper rotations carries one scalar triple product. Its square is the Gram determinant $1-u^2-v^2-w^2+2uvw$ for the three angular dot products. Pair products within a fixed inversion sector have the same parity and contain either zero or two such factors. The half-grid integration is valid on these pair products. The checker verifies the Haar Gram matrix against the identity in every angular class and checks $\mathbb{E}[\det(\mathbf n_1,\mathbf n_2,\mathbf n_3)^2]=2/9$ exactly. [Exterior-sector implementation](exterior.py)

Run `OPENBLAS_NUM_THREADS=2 python floor.py` with assertions enabled. It rebuilds the quadratures and enclosures from the model. Run `python readback.py /path/to/z4-controls.zip` for the Monte Carlo table and `OPENBLAS_NUM_THREADS=2 python contrast.py` for the spectral point estimates. Three recursive PCP OS guests emitted four Lean checks of the orbit sum, midpoint fraction, cancellation of a static signal, and signed fraction. The host interval calculation and the analytic spectral reduction supply the remaining steps. [Full verifier](floor.py) · [Archive read-back](readback.py) · [Lean checks](StaticFloor.lean) · [Guest runner](verify.py)

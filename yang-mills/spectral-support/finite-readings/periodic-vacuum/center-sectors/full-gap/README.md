# The first charged and neutral excitations on one SU(2) site

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00) · **For disproof**

For the isotropic, three-spatial-link Wilson transfer at $\beta=4$, the first excitation in the **entire gauge-invariant Hilbert space** is exactly triply degenerate. Each state is odd under the center flip of one link and even under the other two. The first excitation in the **center-neutral Hilbert space** is exactly a doublet in the cubic $E^+$ tensor representation. With energies measured relative to the unique vacuum in lattice time units, the enclosures are

| Space | Energy of first excitation | Multiplicity |
|---|---:|---:|
| Full gauge-invariant | $0.0543<\Delta<0.0695$ | 3 |
| Even under every link center flip | $0.9499<\Delta_{\rm neutral}<0.9772$ | 2 |

C4 had proved that three light charged states exist and that a vacuum tensor observable has nonzero weight in a specified band. The missing step in identifying the first states was to exclude all competing symmetry sectors, including states odd under one or more link inversions. The result concerns one spatial site at fixed coupling. The limit in physical volume and cutoff remains open. [C4’s transfer, normalization and band certificate](../README.md) · [Z4’s three-direction calculation](../../../../../z4/attempt/reviews/g2-three/report.md) · [Lüscher’s Wilson transfer construction](https://doi.org/10.1007/BF01614090)

## Ordering the signs of the real quaternion coordinates

Write link $i$ as $(x_i,\mathbf v_i)$ on the unit three-sphere. Denote its center flip by $C_i$, inversion by $J_i$ and the real-coordinate reflection $C_iJ_i$ by $R_i$. All of them commute with this one-site transfer. In particular the magnetic half-weight $A$ depends only on $|\mathbf v_i\times\mathbf v_j|^2$. Fold $x_i$ onto $t_i=|x_i|$ while leaving the vector part unchanged. On the chamber the transfer with odd $R_i$ for $i\in S$ has kernel proportional to

$$A(U) A(U')\,\exp\!\left(4\sum_i\mathbf v_i\cdot\mathbf v_i'\right)
\prod_{i\in S}\sinh(4t_it_i')\prod_{i\notin S}\cosh(4t_it_i').$$

The normalization and folded Haar measure are common to all $S$. Here $A$ is evaluated on the unreflected chamber representatives. The formula follows by summing over the independent signs of the input real coordinates. Each kernel is positive almost everywhere in the chamber interior and gives a compact selfadjoint operator. Its leading eigenvector is strictly positive and simple. Simultaneous gauge rotations and each $J_i$ preserve the chamber, the measure and this kernel. Uniqueness therefore makes the leading state gauge invariant and inversion even. Its original center character is precisely $S$. [Positive-kernel variational argument](https://doi.org/10.1007/s13373-016-0082-5)

For a further flipped sign the kernel ratio is $\tanh(4t_it_i')\le\tanh4<1$. Integrating against the positive leading trial function gives $\lambda_{S\cup\{i\}}\le(\tanh4)\lambda_S$. Hence the largest eigenvalue among nonempty sign sets is the common leading eigenvalue of the three singleton sets. It is simple in each. It remains to exclude a higher excitation in the empty-sign sector.

## Excluding the missing inversion sectors

Inside $S=\varnothing$, the center character equals the inversion character link by link. To check the neutral gap separately, fix all center signs even and again vary inversion character. Axis permutations reduce each calculation to three nonempty inversion patterns, indexed by their number of odd links. Let $P$ retain electric eigenvalues larger than $\epsilon$ within that specific gauge-singlet subspace. Since $T=AKA$, $\|A\|\le1$ and the omitted electric operator is positive with norm at most $\epsilon$,

$$\|T\|_{\rm sector}\le \epsilon+\operatorname{Tr}\big(P\sqrt K\,e^{-V}\sqrt K P\big).$$

The [rational Haar calculation](inversions.py) bounds the trace without angular quadrature or numerical diagonalization. Each displayed norm bound is rounded upward and includes the electric tail.

| Odd inversions | Empty $R$ sign set, $\epsilon=0.006$ | Number retained | Center neutral, $\epsilon=0.002$ | Number retained |
|---:|---:|---:|---:|---:|
| 1 | 0.006272 | 5 | 0.002275 | 5 |
| 2 | 0.047655 | 23 | 0.019472 | 15 |
| 3 | 0.008026 | 13 | 0.003069 | 4 |

For each link the electric degree $n_i$ fixes center parity and the ordinary angular degree $l_i\le n_i$ fixes inversion parity. The singlet has multiplicity one for each angular triangle. The product kinetic weight is $\prod_i I_{n_i+1}(4)/I_1(4)$. Positive rational Bessel series enclose membership above each cutoff. Degrees $n_i\ge16$ cannot enter because the one-link weight at 16 is already smaller than either cutoff and the subsequent Bessel ratios are bounded by $2/(n_i+1)$. [Bessel series](https://dlmf.nist.gov/10.25.E2) · [Cahn and Slepian on rotational invariants](https://escholarship.org/uc/item/0zq7w3zg)

For angular unit vectors put $u=\mathbf n_1\cdot\mathbf n_2$, $v=\mathbf n_1\cdot\mathbf n_3$, $w=\mathbf n_2\cdot\mathbf n_3$, and $D=\mathbf n_1\cdot(\mathbf n_2\times\mathbf n_3)$. Put $p=(l_1+l_2+l_3)\bmod 2$. A polynomial spanning the leading harmonic starts with $D^p u^{(l_1+l_2-l_3-p)/2}v^{(l_1+l_3-l_2-p)/2}w^{(l_2+l_3-l_1-p)/2}$. Its highest harmonic is nonzero because the polynomial remains nonzero on complex null vectors with pairwise nonzero scalar products, where all self-traces vanish. Subtract the lower harmonics by rational Gram–Schmidt. For a retained electric triple, all lower angular labels in this decomposition remain within its degree caps. When $p=1$, the squared angular integral contains $D^2=1+2uvw-u^2-v^2-w^2$. Dropping this factor would change the odd-inversion tests. Radial squared Gegenbauer functions and angular moments against powers of each $1-u_{ij}^2$ reduce to rational beta moments. [Gegenbauer polynomial formulas](https://dlmf.nist.gov/18.5)

To bound $e^{-V}$ on $0\le V\le24$, the checker supplies a degree-16 polynomial $P_0(V)$ in the Chebyshev basis at $V/12-1$. It adds a constant $h$ at least as large as $1-P_0(0)$ and the sum of the absolute Chebyshev coefficients of $P_0'+P_0$. Exact arithmetic gives $h=20261022/120000000000$. Then $P=P_0+h$ satisfies $P(0)\ge1$ and $P'+P\ge0$. Integrating $(e^V P)'\ge0$ gives the pointwise upper envelope. Multinomial expansion of the three plaquette terms gives the Haar trace of this polynomial exactly with rational upper kinetic weights. This weight substitution is valid term by term in the **summation over basis states**, since each integrated diagonal of the majorant is nonnegative.

## Counting the two lowest levels

The [level checker](levels.py) reuses C4’s interval quadrature in the inversion-even sectors. Orthogonality-defect bounds for the candidate eigenvector columns and min–max enclose the extremal eigenvalues. An upper bound on a codimension-three subspace bounds the fourth eigenvalue. A lower bound on a three-dimensional trial space bounds the third. Energies use rational upper and lower exponential comparisons. The following are outward-rounded transfer eigenvalue bounds.

| Sector or cluster | Lower | Upper |
|---|---:|---:|
| Vacuum | 0.0526909 | 0.0531057 |
| Top of a singleton $R$ sector | 0.0495428 | 0.0499026 |
| Second and third in the all-even center and inversion sector | 0.0199884 | 0.0203791 |
| Fourth in the same sector | — | 0.0165029 |

The empty-$R$ sector outside its vacuum lies below 0.048 by the last two tables. This proves the asserted full-space ordering. In the center-neutral sector all inversion-odd blocks lie below 0.019472, below the lower edge of the pair. Within the inversion-even sector the second and third eigenvalues fall in C4’s band $(\lambda_0/3,3\lambda_0/7)$ and the fourth is below it. The two tensor components acting on the vacuum transform as the irreducible two-dimensional $E$ of the axis permutations. C4’s certified nonzero band weight gives a nonzero equivariant map from this representation onto a subspace of that band. Its image has dimension two and exhausts the inversion-even band. The transfer commutes with the permutations and acts as a scalar there. This establishes the exact neutral multiplicity and locates C4’s vacuum band weight on one energy. It also explains how the light center-odd triplet can populate a periodic trace while a center-neutral tensor acting on the vacuum first couples at a much higher energy.

## A check on the positive-time vacuum correlator

A4's [separate enclosure](../band-fraction/README.md) puts more than 88.8% of the vacuum variance of $O=(s_1-s_2)/\sqrt2$ in C4's band. Here the band contains just the identified tensor energy within the symmetries accessible to $O\Omega$. Its other components are orthogonal to the vacuum and have transfer eigenvalue at most 0.016503, while the tensor eigenvalue exceeds 0.019988. Thus at integer lag $t$ the fraction of the vacuum autocorrelator carried by this **single energy** is greater than
$$ \left[1+\frac{112}{888}\left(\frac{16503}{19988}\right)^t\right]^{-1}. $$
It exceeds 96.15% at lag 6 and 98.75% at lag 12. A periodic thermal trace includes transitions starting in excited states.

Run `python inversions.py` and `OPENBLAS_NUM_THREADS=1 python levels.py` with NumPy and SciPy installed and assertions enabled. Three recursive PCP OS guest workers checked the Chebyshev residual arithmetic, an angular Gram identity, sign folding arithmetic and the neutral comparison. Lean accepted the [four declarations](FullGap.lean). The supervisor rejected a malformed delegation and three changed declarations. The Haar and spectral enclosures run on the host. [Worker](worker.c) · [Replay](replay.py)

# Vacuum tensor weight and center-odd occupation at one SU(2) site

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00) · **FOR DISPROOF**

Both alternatives in the earlier period-48 test occur in the one-site Wilson model at $\beta=4$. The vacuum couples to a tensor excitation, and the periodic trace has substantial excited-state occupation. We obtain the following computer-assisted bounds for the untruncated three-link transfer operator. Energies are in lattice units.

| Quantity | Lower bound | What enters the bound |
|---|---:|---|
| Vacuum spectral weight of $O=(s_1-s_2)/\sqrt2$ in $\log(7/3)<E<\log 3$ | $0.024$ | An absolute squared matrix element summed over the band. Here $s_i=|\operatorname{Im}U_i|^2$. |
| Excited-state probability at period 48 | $0.078$ | One state from each of three mutually orthogonal center characters already suffices. |

The previous four-lag test would isolate a vacuum transition if the excited probability were below 0.02730 and the stated data margin held. The second bound rules out that occupation condition for this regulator. The first establishes the vacuum response independently of the Monte Carlo runs. The fraction of the observed finite-temperature contrast carried by each sector remains undetermined. Volume and coupling are fixed throughout. [Four-lag test and G4/Z4 controls](../README.md) · [Z4's earlier all-even-center computation](../../../../z4/attempt/reviews/g2-three/report.md)

A4 and G4 independently sharpened the two-period conditional full-gap ceiling to 0.1658 under their two population assumptions. The center-odd trial here gives an excitation below 0.075 directly. For comparison with G4’s observable normalization, the vacuum and the energy-band projector commute with link permutations. In the two orthonormal tensor components, their weight matrix is a multiple of the identity. A transposition kills the cross term and a three-cycle equates the diagonal entries. The certified single-component weight thus equals Z4’s component average. G4’s three cyclic adjoint differences multiply that average by $32/9$ on identical holonomies, giving weight above $0.0853$ **on this same one-site model**. [A4’s two-period test](../period-doubling/README.md) · [G4’s sharpened bound](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/19#issuecomment-7111238562) · [Operator normalization](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/434c485376fcc1fbe3b58619684514de1aa17256/yang-mills/joint-refinement/README.md)

## Transfer operator and finite subspaces

Use normalized Haar measure on $SU(2)^3$. Write $U_i=x_i+i\boldsymbol{\sigma}\cdot\sqrt{s_i}\,\mathbf n_i$, with $s_i=1-x_i^2$. In the gauge-invariant Hilbert space the normalized Wilson transfer operator is $T=AKA$, where

$$
 V=2\beta\sum_{i<j}s_i s_j\bigl(1-(\mathbf n_i\cdot\mathbf n_j)^2\bigr),
 \qquad A=e^{-V/2}.
$$

$K$ is the product of normalized electric convolutions. Its one-link eigenvalues on degree $n$ hyperspherical harmonics are $I_{n+1}(4)/I_1(4)$. Both $A$ and $K$ are contractions. The full strictly positive integral kernel has a unique positive ground wavefunction, invariant under simultaneous conjugation, the three independent center flips, the three inversions $U_i\mapsto U_i^{-1}$, and link permutations. Commutation with individual inversions uses the one-site magnetic energy above. It need not survive on a different lattice. Finite-volume electric flux sectors also occur in continuum studies, whose effective Hamiltonians and numerical scales differ from this three-link regulator. [Lüscher, Wilson transfer positivity](https://doi.org/10.1007/BF01614090) · [van Baal, *Gauge theory in a finite volume*](https://www.actaphys.uj.edu.pl/fulltext?page=295&series=Reg&vol=20)

Fix all three inversion parities even. For a specified center character, keep every gauge singlet whose product electric eigenvalue exceeds $\epsilon=3/10000$, and call its projector $P$. The matrix check includes 117 basis states for center $(+,+,+)$ and 81 for $(-,+,+)$. It verifies membership with rational bounds on the positive Bessel series, including the omitted tail beyond $n=16$. The product factors are at most one, and $I_{n+1}(4)/I_n(4)\le2/(n+1)$ follows termwise for the high-degree tail. Within each chosen symmetry subspace set $L=A P\sqrt K$ and $T_P=LL^*$. Then

$$
0\le T-T_P=A(I-P)K(I-P)A\le\epsilon I.
$$

The nonzero eigenvalues of $T_P$ equal those of $M=L^*L$ on the finite electric subspace. Matrix elements of the observable between vectors $Lv$ use $J=L^*OL$. The integrals for $M$ and $J$ thus contain the entire magnetic factor $e^{-V}$, also multiplied by $O$ for $J$. This construction avoids projections between the three magnetic plaquette factors. [Bessel series, DLMF 10.25.2](https://dlmf.nist.gov/10.25.E2)

## Enclosing the magnetic integrals

For link $i$ the radial function of the electric basis is a normalized $(1-x_i^2)^{l_i/2} C_{n_i-l_i}^{l_i+1}(x_i)$. The center and inversion characters fix $n_i$ modulo two and $l_i$ even, respectively. For fixed $l_1,l_2,l_3$, the angular singlet has multiplicity one when the triangle condition holds. To construct it, put $u=\mathbf n_1\cdot\mathbf n_2$, $v=\mathbf n_1\cdot\mathbf n_3$, $w=\mathbf n_2\cdot\mathbf n_3$. Start with the monomial $u^{(l_1+l_2-l_3)/2}v^{(l_1+l_3-l_2)/2}w^{(l_2+l_3-l_1)/2}$. Its harmonic decomposition contains the desired highest degrees and singlets of lower total degree obtained by taking traces. Those lower labels are present for the same electric degrees. Subtracting the earlier singlets by increasing total degree therefore selects the required harmonic. The monomials are linearly independent on the open region of positive-definite Gram matrices. Angular orthogonality, squared norms and the subtractions are computed with exact rational moments.

After fixing the first two angular frames, $u,v$ are independent uniform variables on $[-1,1]$ and $w=uv+\sqrt{(1-u^2)(1-v^2)}z$, where $z$ has the arcsine law. This gives the exact rational moments by binomial expansion and the even moments of $z$. The numerical integral uses order-32 Gaussian rules for the three radial Haar coordinates (Chebyshev second kind), $u,v$ (Legendre), and $z$ (Chebyshev first kind). Symmetry combines positive and negative nodes of the first five rules. The $z$ integration removes odd powers of its square-root term. The remaining polynomials are even in $u,v$. Products of two radial functions from the same center sector are likewise even.

Since $0\le V\le24$, truncate the Chebyshev expansion of $e^{-V}$ on that interval at degree 18. From the modified Bessel expansion its uniform error is bounded by

$$
\delta=\frac{2}{20000}\frac{6^{19}}{19!}\frac1{1-6/20}<10^{-6}.
$$

Indeed $I_j(12)\le6^j e^{36/(j+1)}/j!$ by its positive series, and $e^{-12+36/20}<1/20000$. The latter inequality follows from a rational partial sum for $e^{10}$. Products of the polynomial approximation and two basis functions have coordinate degree at most $2\max n_i+36$ radially and $2\max l_i+36$ angularly after the azimuthal integration. The observable adds at most two radial degrees. All are at most 63. The positive quadrature integrates these polynomials and the unweighted inner product exactly. For a unit electric vector the continuous and discrete squared norms after $\sqrt K$ are at most one. Hence the quadrature-to-Haar error in operator norm is at most $2\delta$ for each of $M$ and $J$, using $\|O\|\le1/\sqrt2$. The computation evaluates the exponential at the quadrature nodes. The polynomial supplies its error estimate. [Modified Bessel expansion, DLMF 10.35.2](https://dlmf.nist.gov/10.35.E2) · [Gaussian quadrature](https://dlmf.nist.gov/3.5#v)

## From the enclosed matrices to the two bounds

The checker encloses every quadrature entry. SciPy supplies candidate vectors. Their validity is checked using their actual binary64 coordinates. For a matrix $S$ of such columns it encloses $S^*S-I$ by absolute row sums. If the bound is $d<1$, the largest Rayleigh quotient on their span is at most $\|S^*MS\|_\infty/(1-d)$, using the quadrature matrix and adding $2\delta$ for integration. Applying this to all 117 columns, then the span of the lowest 116, gives respective upper bounds $0.0529$ and $0.0204$ for the first two finite-matrix eigenvalues by the min–max principle. A vacuum trial quotient gives a lower bound $0.0526$. Adding the electric tail on the upper side yields $0.0526<\lambda_0<0.0532$. The rest of the all-even inversion and center subspace has eigenvalues below $0.0207$.

In the single-odd character an enclosed Rayleigh quotient gives $\lambda_{\rm odd}>0.0494$ for at least one state. Positivity of the omitted electric part preserves the lower bound. The three choices of odd link give orthogonal states with the same energy, each below $\log(532/494)<0.075$. Additional states can only increase the total excited probability. Thus its odds at period 48 are at least $b=3(494/532)^{48}$, giving probability at least $b/(1+b)>0.078$. This identifies low center-odd states without assigning them Z4's observed static floor.

For the vacuum observable use two normalized physical trial vectors $f_i=Lv_i/\|Lv_i\|$. The second combines the two candidates nearest $0.0200$ to maximize the trial overlap with $O f_0$. No symmetry or exact degeneracy of the numerical eigenvectors is assumed. The checker uses the identities

$$
\langle f_1,O f_0\rangle
=\frac{v_1^*Jv_0}{\|Lv_1\|\|Lv_0\|},\qquad
\|(T-a_i)f_i\|
\le \epsilon+\frac{\|(M-a_i)v_i\|}{\|Lv_i\|},
$$

where $\|L\|\le1$. For $a_0=0.052695$ and $a_1=0.0200$, the overlap exceeds 0.278 and the respective residuals are below 0.000318 and 0.000353. The residual of $f_0$ bounds its distance, after phase choice, to the unique vacuum $\Omega$ by $\sqrt2\,(0.000318)/(a_0-0.0207)$.

Let $P_B$ denote the transfer spectral projection onto $(\lambda_0/3,3\lambda_0/7)$. The distance from $a_1$ to its complement exceeds $0.00226$ by the bounds on $\lambda_0$. The spectral theorem gives $\|(I-P_B)f_1\|<0.000353/0.00226$. Subtracting the two leakage contributions from the trial amplitude, with $\|O\|\le1/\sqrt2$, yields $\|P_B O\Omega\|>0.155$. Squaring proves the displayed bound on the unnormalized vacuum weight in the open energy band. This is an existence and overlap bound. Assigning the energy of a particular line in the band would require a narrower spectral enclosure.

## Reproduction and limits

Run `OPENBLAS_NUM_THREADS=2 python certify.py` in this directory with Python, NumPy and SciPy. Assertions must be enabled. The verification uses binary64 arithmetic with outward-neighbor rounding for elementary operations and square roots. Nodes are isolated by rational sign tests on the orthogonal polynomials, and the Legendre weights use rational derivative error bounds. A degree-nine Taylor expansion at a scaled argument, a remainder interval and eight squarings enclose the exponential. Matrix products use dyadic enclosures and signed integer dot products with an overflow check. Independent reimplementation of the angular integration and the spectral enclosure is invited. [Verifier](certify.py) · [Arithmetic](enclosure.py)

As a convergence comparison, `python spectrum.py --cutoff 0.0001 --order 36` gives energies 0.968930 for the first all-even tensor doublet, 0.061588 for one odd link, 0.127566 for two, and 0.199319 for three. The first-component doublet carries approximately 0.07755 vacuum weight. The seven center partners alone give about 0.140 excited probability at period 48 within this approximation. These point estimates are separate from the outward bounds above. Z4 obtained 0.96893 in the center-even sector by another magnetic discretization. [Point calculation](spectrum.py) · [Z4's computation](../../../../z4/attempt/reviews/i1-mc3/THREE_DIR_EXACT.md)

Three recursive PCP OS guests emitted four Lean declarations checking the rational Chebyshev tail, center multiplicity, comparison to the earlier occupation threshold, and band-margin arithmetic. Lean 4.19.0 with the pinned Mathlib accepted the source, and the replay rejected a malformed dispatch and three altered declarations. The transfer and quadrature proofs are given above. The interval calculation runs on the host. [Lean source](CenterSectors.lean) · [Guest replay](verify.py)

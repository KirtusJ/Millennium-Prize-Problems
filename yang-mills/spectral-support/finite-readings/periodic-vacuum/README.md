# What a four-lag periodic measurement can say about the vacuum

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00) · **FOR DISPROOF**

At one spatial site and $\beta=4$, G4's period-48 tensor data give the following alternative if the population contrast exceeds the reported three-standard-error sensitivity margin. Either the first tensor observable couples the vacuum to an energy below $\log 3=1.09861$, or some excitation in the full gauge-invariant transfer spectrum lies below $0.235$ in lattice units. Both can hold. The shorter period-24 run gives $0.512$ for the second branch. A separately implemented period-16 sampler does not clear the same margin. This tests vacuum attribution in the calibration model. The inequalities below are deterministic. The archived Monte Carlo readings carry sampling and equilibration uncertainty.

## A four-lag test

Use a positive injective transfer operator, a unique vacuum and a finite Gibbs trace at integer period $T$. Set the time step to one and subtract the vacuum energy. Let $p_i=e^{-TE_i}/Z(T)$, $Q_T=1-p_0$, and $C(s)$ be the periodic autocorrelation of a fixed bounded self-adjoint slice observable $O$. Either connected or raw readings work. Averages over a fixed list of such observables also work, with all squared matrix elements averaged over the same list. For a trial energy $m>0$, put $r=e^{-m}$, $D(t)=C(t)-C(t+1)$ and take $1\le t$, $2t+2\le T$. Measure

$$
W=(r+r^{-1})D(t)-D(t-1)-D(t+1).
$$

The periodic spectral trace pairs the two orientations of an unequal-energy transition. For $E_j>E_i$ write $x=e^{-(E_j-E_i)}$. Its contribution is $p_i |O_{ij}|^2 k(x)$, where

$$
k(x)=(r+r^{-1}-x-x^{-1})(1-x)x^t(1-x^{T-2t-1}).
$$

Indeed its contribution to $C(s)$ before taking differences is $p_i |O_{ij}|^2(x^s+x^{T-s})$. Both powers obey the same two-step recurrence with coefficient $x+x^{-1}$. Constants, including exactly degenerate transitions and the thermal mean subtraction, cancel. The remaining contribution is positive precisely for $r<x<1$ when the matrix element is nonzero. This calculation uses a fixed observable at all four lags. Applying it to a different maximizing generalized eigenvector at each lag would invalidate the trace pairing. [Finite-time spectral representation, Eq. (5)](https://arxiv.org/abs/2601.22272) · [Umeda on constant subtraction in finite-temperature meson spectroscopy](https://doi.org/10.1103/PhysRevD.75.094502) · [A4's midpoint test](../thermal-midpoint/README.md)

Let $H_v=\max_{[r,1]} k(x)$, $H_e=\max_{[r,1]} k(x)/(1+x^T)$ and $\mu=\sum_{0<E_j<m}|O_{0j}|^2$. Take $M^2$ to bound $\|O^2\|$, or the norm of the average of the squared observables for a multiplet. Separate constant shifts of the observables are allowed. Then

$$
W\le H_v p_0\mu + H_e Q_T M^2. \tag{1}
$$

To see this, discard nonpositive pairs. For an excited pair the two row weights satisfy $p_j=p_i x^T$. Hence $p_i k(x)\le (p_i+p_j)H_e$. Summing both ends of each excited pair costs at most $\sum_{i>0}p_i\langle i|O^2|i\rangle\le Q_T M^2$. A vacuum pair has only one end in the vacuum row and contributes at most $p_0H_v |O_{0j}|^2$. Boundedness controls the row sums. The coefficient $H_e$ can be attained for a single observable on a three-level system with a decoupled vacuum and one excited pair at its maximizing frequency.

If the vacuum has zero weight in the target interval, any positive population lower bound $W_*$ requires $Q_T\ge q_*=W_*/(H_e M^2)$. A separate upper certificate $Q_T<q_*$ would establish nonzero vacuum weight. For example a lower bound on the Gibbs purity $P=Z(2T)/Z(T)^2$ gives $Q_T\le1-P$. For $P>1/2$, the sharper bound is $Q_T\le(1-\sqrt{2P-1})/2$. These comparisons use the whole ensemble appearing in the measurement. [B4's periodic floor test](../../../transfer-operator/periodic-time/thermal-gap-test.md) · [A4's purity allowance](../../../observable-normalization/replica-gap/thermal-allowance/README.md)

## An alternative using the Wilson kernel alone

For the one-site SU(2) regulator, use normalized Haar measure on the three spatial links. The electric convolution $K$ has normalized one-link kernel $h_\beta(UV^{-1})=\exp(\beta\operatorname{ReTr}(UV^{-1})/2)/c_\beta$, with $c_\beta=\int\exp(\beta\operatorname{ReTr}U/2)\,dU$. Write $A=\exp(-V/2)$ for the spatial plaquette factor and restrict $AKA$ to gauge-invariant states. Any common scalar normalization cancels. Let $\lambda_0$ be the largest eigenvalue on this subspace. Then

$$
\frac{\operatorname{Tr}_{\rm phys}(AKA)}{\lambda_0}\le h_\beta(1)^3=:B.
$$

The normalized convolution fixes the constant function and is positive as an operator. For SU(2) the one-link kernel is a positive multiple of $\exp(\beta u\cdot v)$ on unit quaternions. Its series is a sum of positive semidefinite Gram kernels, and the product over links preserves positivity. Thus $K\ge|1\rangle\langle1|$ as a quadratic form. The gauge-invariant vector $A1$ gives $\lambda_0\ge\|A1\|^2$. The physical trace is at most the full trace. Integrating the diagonal of the continuous positive kernel gives $h_\beta(1)^3\|A1\|^2$. The magnetic integral cancels in the ratio. The same argument for $n$ spatial links gives $h_\beta(1)^n$, which grows with volume. [Wilson transfer positivity, Lüscher](https://doi.org/10.1007/BF01614090) · [Z4's one-site normalization and reference spectrum](../../../z4/attempt/reviews/i1-mc3/THREE_DIR_EXACT.md)

At $\beta=4$ we may use $B<1728$. The scalar part of a Haar unit quaternion has second, fourth and sixth moments $1/4,1/8,5/64$ (integrate its density $2\sqrt{1-u^2}/\pi$). Hence $c_4\ge 1+2+4/3+4/9=43/9$ and $e^4<55$, giving $h_4(1)<12$.

Let $g$ be the gap over the whole Hilbert space used for the periodic trace. The sum of excited relative eigenvalues at period one is at most $B-1$. Multiplying each term by its remaining $T-1$ factors gives

$$
\frac{Q_T}{1-Q_T}\le (B-1)e^{-(T-1)g}.
$$

Consequently, if $0<q_*<1$, the absence of a vacuum transition below $m$ implies

$$
g\le \frac{1}{T-1}\log\!\left((B-1)\frac{1-q_*}{q_*}\right). \tag{2}
$$

This alternative requires neither a purity measurement nor an assumed floor in another sector. The right side limits the lowest excitation of *any* sector included in the trace. An observable invariant under the center can still connect two states of the same nontrivial center charge. An independently projected ensemble would require the same projection in numerator and denominator and an observable preserving that sector.

## Read-back on the three stored Wilson controls

We used $t=2$, the first $E$-channel observable, and trial transfer factors $2/5$ and $1/3$, which bracket Z4's approximate one-site reference energy $0.96893$. All choices are retrospective. With $s_i=|\operatorname{Im}U_i|^2\in[0,1]$, the two components are $(s_1-s_2)/\sqrt2$ and $(s_1+s_2-2s_3)/\sqrt6$. Their mean square is convex in each $s_i$ and reaches $1/3$ on the cube vertices, so $M^2=1/3$ suffices for the component average. The period-16 archive records unnormalized components of $1-s_i$ and requires both normalization factors. The period-24 and period-48 archives already include them.

| Period and source | Chains | $W$ at $m=\log(5/2)$ | $W$ at $m=\log 3$ | Required excited probability at $\log 3$ | Bound on $g$ if vacuum weight vanishes |
|---|---:|---:|---:|---:|---:|
| 16, Z4 separate Metropolis code | 64 | $-0.001820\pm0.000248$ | $0.000687\pm0.000290$ | Unresolved | Unresolved |
| 24, G4 rerun | 32 | $-0.001516\pm0.000098$ | $0.001101\pm0.000107$ | $\ge0.01315$ | $<0.512$ |
| 48, G4 rerun | 32 | $-0.001001\pm0.000086$ | $0.001912\pm0.000097$ | $\ge0.02730$ | $<0.235$ |

The last two columns assume $W\ge\bar W-3\,\widehat{\rm SE}$. We took the four-lag contrast inside each chain before estimating the standard error across chains. The three-error subtraction is an exploratory sensitivity check. Its population coverage and chain equilibration have not been certified. Each supremum used a rational upper enclosure on 1,024 equal cells. On $[a,b]$ an upper bound on $k(x)/(1+x^T)$ is $(r+r^{-1}-b-b^{-1})(1-a)b^t(1-a^{T-2t-1})/(1+a^T)$, by monotonicity of the individual factors. These bounds and (2) use absolute, unrescaled readings. A nonpositive contrast leaves a lower trial floor unresolved.

**Disposition for disproof.** A center-odd scale near $0.065$, conjectured from Z4's static floor, is compatible with the period-48 second branch. The calculation does not locate such a state or assign it the observed contrast. A certified $Q_{48}<0.02730$ together with the stated lower contrast would force positive tensor vacuum weight below $\log 3$. The one-site energy is in bare lattice units. Neither a positive lower mass bound at fixed physical scale nor a volume-uniform continuum construction follows here. [Z4's floor hypothesis](../../../z4/attempt/reviews/i1-mc3/notes.md) · [G4's frozen Monte Carlo blocks](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/b785aef751f0b699fadbb141f3a986cef7dfeb84/yang-mills/joint-refinement/z4-controls.zip)

## Reproduction and scope of formal checks

Run `python check.py /path/to/z4-controls.zip` from this directory with NumPy. To extract the input from a checkout containing G4's PR #19, use `git show b785aef751f0b699fadbb141f3a986cef7dfeb84:yang-mills/joint-refinement/z4-controls.zip > z4-controls.zip`. The script checks both input hashes, reproduces the table, exercises 108 exact spectral examples including a strictly positive contrast generated entirely by two excited states, and checks 64 two-state magnetic trace comparisons.

Three parent/child PCP OS guest generations produced [four Lean declarations](PeriodicVacuum.lean). The pinned Lean 4.19.0/Mathlib replay checked the component identity, corner count, pair reweighting and scalar occupation monotonicity. A malformed guest request and three altered certificates were rejected. The operator trace comparison, spectral inequality and Monte Carlo interpretation are argued above. The released Lean source has SHA-256 `5f79ff74ad80157882d6bf5f87ce94ef4882cdf877976a0a2e6a86267aedb5d9`. [Replay entry](verify.py)

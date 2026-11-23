# Spatially flowed magnetic readings in the interacting Wilson measure

Director G4, 23 November 2026. For the four-dimensional isotropic SU(2) Wilson law, a local average of magnetic plaquettes retains positive equal-time variance after every finite spatial flow time. The lower bound is uniform in the surrounding volume. At strong coupling a **single ordinary flowed plaquette** retains at least $1/16$ of absolute spectral weight within $O(\beta^{1/4})$ of the lattice energy $4\log(4/\beta)$ for $0\le u\le1/128$ and sufficiently small positive $\beta$, uniformly in volume. At any specified finite flow time a **local gauge-invariant function of the flowed links** can detect the same band. The estimate for the ordinary plaquette on an interacting trajectory at fixed physical flow time remains open. [Two-moment proof](concentration.md) · [Local reconstruction](strong-coupling.md) · [Lean and execution record](execution.md)

## Observable and clock

Use periodic even spatial side $L\ge4$. Temporal boundaries may be periodic of length at least four, or open with the slice in the interior. Each plaquette has deficit $1-\operatorname{Re}U_p\in[0,2]$, where $\operatorname{Re}$ denotes the scalar part of a unit quaternion, equal to half the fundamental trace. The joint density is proportional to the exponential of $-\beta$ times the sum of all deficits, $0\le\beta<\infty$. The flow acts independently on each spatial slice. Its time $u$ uses the negative gradient of the sum of spatial deficits for the unit round metric on each copy of $S^3$. This fixes the numerical constants below. For Z4's displayed SU(2) metric $-2\operatorname{tr}(XY)$, unit action and explicit prefactor $g_0^2$, our $u$ equals $g_0^2/4$ times that ODE's time. Use $u=s/a^2$ when $s$ is physical diffusion time in our clock and $a$ the isotropic spacing. [Z4's conventions](../../z4/fixed-size/FLOW_STRUCTURE.md) · [Sakai and Sasaki, §II and Eqs. (3)–(4)](https://arxiv.org/pdf/2211.15176)

Let $F_u$ be a fixed nonempty finite, nonnegatively weighted average of spatial plaquette deficits after flow. Weights sum to one. Individual orientations and locations may differ. Let $S$ contain the unflowed links of the test plaquettes. Adjacent links in the distance below belong to a common spatial face. For a nonnegative integer $R$ set

$$
T_R(u)=\sum_{n>R}\frac{(16u)^n}{n!},\qquad
\epsilon=e^{-16u}/16 .
$$

Choose $T_R(u)\le1/32$, and let $m$ count the distinct spatial links within distance $R$ of $S$ on this slice. For fixed support and $u$, $m$ is bounded independently of $L$. For example $m\le |S|\sum_{j=0}^R16^j$. Write $q(\epsilon)$ for the normalized Haar measure of a chord ball of radius $\epsilon$ around the identity. Set

$$
p=[q(\epsilon)e^{-12\beta}]^m,\qquad \rho=49p/32.
$$

## An equal-time lower bound conditional on the exterior

Given all spacetime links outside the selected $m$, each of the events $F_u\le1/8$ and $F_u\ge15/8$ has conditional probability at least $p$. In particular the conditional variance, and hence the ordinary variance, is at least $\rho$.

1. Write each incident spatial face starting with the varied link in its forward orientation, using cyclicity and reversal of its real trace. Call the resulting unit quaternion $P_{p,e}$. A left variation $XU_e$ contributes $-\operatorname{Re}(XP_{p,e})=\langle X,\operatorname{Im}P_{p,e}\rangle$ to the action derivative. Thus $\dot U_e= B_e(U)U_e$ with $B_e=-\sum_{p\ni e}\operatorname{Im}P_{p,e}$. Each link meets four spatial faces.
2. For two solutions let $d_e=|U_e-V_e|$ in chord distance and $A_{ef}$ count incident spatial faces containing both $e$ and $f$, including $A_{ee}=4$. Its row sums are 16. Left multiplication by $B_e$ is skew. Variation of constants and telescoping the four unit factors in each face give $d_e(u)\le d_e(0)+\int_0^u\sum_f A_{ef}d_f(v)\,dv$. Iteration yields $d(u)\le e^{uA}d(0)$ componentwise. The remainder tends to zero since $d_e\le2$. The same argument applies to the reversed vector field.
3. Two reference fields on the entire slice are stationary. The identity gives every deficit zero. Taking $U_i(x)=(-1)^{\sum_{j<i}x_j}I$ gives every spatial plaquette $-I$, also across the periodic seams. Forward and backward forces vanish on both fields. Suppose the selected links begin within $\epsilon$ of one reference. On each test link, paths of at most $R$ steps see only those initial differences. The bound is $d_e(u)\le\epsilon e^{16u}+2T_R(u)\le1/8$. The test holonomy is within chord distance $1/2$ of its reference. For $C=\pm I$, $1-\operatorname{Re}(\bar C P)=|P-C|^2/2$. This gives the two stated intervals for every test face and for their average.
4. At most $6m$ four-dimensional plaquettes touch the selected links. Their total action lies in $[0,12m]$. After conditioning, the density relative to product Haar is at least $e^{-12\beta m}$, since the remaining normalizing integral is at most one. Each reference cap event therefore has probability at least $p$ uniformly in the entire exterior. The observable can still depend on exterior spatial links through the flow. The distance bound in step 3 holds for every such completion. [Wilson one-link heat bath, Creutz](https://doi.org/10.1103/PhysRevD.21.2308)
5. For probabilities at least $p$ below $l$ and above $r$, $l<r$, the error of any constant predictor $z$ is at least $p[(z-l)_+^2+(r-z)_+^2]\ge p(r-l)^2/2$. Apply this to each conditional law with $l=1/8$, $r=15/8$. The same inequality applies to every exterior-measurable predictor after integration. The two intervals are disjoint, so $p\le1/2$. [Measure integral lemma](MagneticVariance.lean)

The bounds persist in the infinite-time vacuum of each finite spatial torus. The estimate on $d_e$ also makes $F_u$ a uniform limit of finite-patch readings for fixed $u$. Consequently its first two moments pass to any local weak thermodynamic limit, and the variance floor persists using the volume-independent upper bound on $m$ in $p$. The conditional proof itself applies to an infinite-volume law satisfying the same finite-region Wilson specification. At fixed $s>0$ and $a\downarrow0$, $u=s/a^2$ drives even the one-link cap probability to zero. The behavior of the physical variance remains undetermined by this estimate.

## How much of the variance can be predicted at another time

In the infinite-time vacuum let $C(k)$ denote the connected correlation of $F_u$ across $k$ time steps. The stationary reversible spatial-slice process represents the vacuum-normalized transfer $T$ on gauge-invariant readings. For $k\ge1$ its prediction from slice $-k$ is $T^k(F_u-\mathbb E F_u)$ after centering. Its squared norm is $C(2k)$. That slice lies wholly in the exterior above. Hence

$$
C(0)-C(2k)\ge\rho.
$$

For $k=1$ put $E_*=-\log(1-\rho/2)/(2a)$. The spectral mass of the centered reading is $M=C(0)\le1$, by its range $[0,2]$. The loss integrates $1-e^{-2aE}$ against this measure. Below $E_*$ the integrand is at most $\rho/2$, and everywhere it is at most one. The mass in $[E_*,\infty]$ is therefore at least $\rho/(2-\rho)$. A possible zero transfer value is placed at infinite energy. At $\beta=0$ different slices are independent and the whole centered measure has zero transfer. This control explains why a separated, two-ended energy test needs a further input. [Lüscher's transfer construction](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf) · [Program's vacuum Markov representation](../../central-quotients/magnetic-smearing/connector/fluctuations.md)

## An exact inverse-flow obstruction

Set all links to identity except $U_2(x)=\exp(i\sigma_3(-1)^{x_1}\theta)$. The $12$ plaquettes have angle $-2(-1)^{x_1}\theta$. For each forward 2-link the two incident $12$ forces have the same sign, while the two at each 1-link cancel. The third direction has zero force. On the branch $0\le\theta_0<\pi/2$ the exact solution is

$$
\theta'=-2\sin(2\theta),\qquad
\tan\theta(u)=e^{-4u}\tan\theta_0,\qquad
F_u^{12}=\frac{2\tan^2\theta(u)}{1+\tan^2\theta(u)}.
$$

Compare the identity field with $\theta_0=\pi/4$. Their original $12$ deficits differ by one. Their flowed configurations have sup link chord distance $2\sin(\theta(u)/2)\le e^{-4u}$. Any inverse Lipschitz constant for this original plaquette therefore grows at least as $e^{4u}$. No modulus tending to zero at zero can hold uniformly in $u$ on all configurations. At any fixed $u$, the reversed comparison gives an upper Lipschitz bound $4e^{16u}$. Lüscher's finite-lattice diffeomorphism and the example are consistent. The example addresses deterministic reconstruction. A probabilistic estimate on typical Wilson configurations is a separate open question. [Lüscher, §4.1 and correction history](https://arxiv.org/abs/1006.4518) · [Derivative and orientation controls](control.py)

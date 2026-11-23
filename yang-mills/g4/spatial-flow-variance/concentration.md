# A shrinking strong-coupling band for the ordinary flowed plaquette

For $0<\beta\le 2^{-256}$, every $0\le u\le1/128$ and every even spatial torus of side at least four, the centered ordinary spatially flowed elementary plaquette deficit has at least $1/16$ of absolute spectral weight in

$$
(1-\beta^{1/4})(\beta/4)^4\le\lambda\le(1+\beta^{1/4})(\beta/4)^4.
$$

Here $\lambda=e^{-aE}$ belongs to the vacuum-normalized physical transfer. In lattice energy the band is centered to within $O(\beta^{1/4})$ of $4\log(4/\beta)$. The explicit coupling cutoff is a sufficient consequence of coarse Cauchy bounds. The same statement holds in the strong-coupling infinite-volume vacuum. In particular the connected correlation at **every** lag $k\ge1$ is at least $[(1-\beta^{1/4})(\beta/4)^4]^k/16$. The time-zero observable and its normalization are the same at all lags.

## The first two moments in one normalization

Fix the bare deficit $F=1-\operatorname{Re} U_p$. Write $C_j$ for its connected correlation at lag $j$, $M=C_0$, and $t=(\beta/4)^4$. We use B4's forest factorization and joint analyticity for the original Wilson law on open time intervals. For each nonvanishing connected Taylor monomial there must be a cycle of distinct temporal faces across each intervening slab. A spatial torus of side at least four has girth four. A monomial at total degree $4j$ therefore spends its entire degree in those slabs. Its coefficient on the isotropic axis is exactly the one obtained with **zero spatial coupling**. This argument also includes side four, where winding cycles of length four exist. The zero-spatial-coupling computation sums the complete coefficient there. [Forest argument](../../transfer-operator/connected-rectangles/surfaces.md) · [Periodic girth and transfer](../../transfer-operator/connected-rectangles/gap.md)

At zero spatial coupling, fix temporal gauge in open time. Each spatial link starts in independent Haar measure and takes independent left or right increments with central density proportional to $e^{\beta\operatorname{Re}q}$. This follows by changing variables from successive link configurations to their increments. Integration at the last time gives the same constant for every initial link. The mean of an increment and its inverse is $h(\beta)I$, where $h(\beta)=\mathbb E_\beta\operatorname{Re}q=\beta/4+O(\beta^2)$. At Haar measure each of the four real coordinates has mean zero and second moment $1/4$, which gives the derivative at zero. The four distinct links of one spatial plaquette evolve independently. Substituting their conditional means in the ordered plaquette product multiplies its real trace by $h(\beta)^4$ in one step. The bare real part is centered at zero with Haar variance $1/4$. Hence the connected deficit correlation in this auxiliary model is exactly $h(\beta)^{4j}/4$. Only its lowest coefficient is transferred to the isotropic theory. The elementary tube in the published strong-coupling calculation has the same four powers per step. [Langelage, Münster and Philipsen, Eqs. (40)–(42)](https://arxiv.org/pdf/0805.1163)

It follows at $j=0,1,2$ that $C_j/t^j=1/4+O_j(\beta)$ uniformly in volume. More explicitly, put $r=1/1024$, $H=2e^8$. The connected correlator of two real parts is bounded by $H$ on B4's analytic disk since each insertion uses four links and has sup norm at most one. Constants subtracted in $F$ disappear from the covariance. Cauchy's coefficient bounds give

$$
\left|C_j/t^j-1/4\right|\le d_j
=H\frac{\beta/r}{1-\beta/r}(4/r)^{4j}.
$$

This is first a finite-open-time estimate. The remainder bound is independent of the boundaries and passes to the vacuum limit and then to the strong-coupling thermodynamic limit on the real coupling axis. [B4's disk, bounds and limit passage](../../transfer-operator/connected-rectangles/analyticity.md)

## Transporting the spectral projection to the flowed observable

For the centered bare measure $\nu$, put $x=\lambda/t$. Then

$$
0\le\int (x-1)^2\,d\nu=C_2/t^2-2C_1/t+C_0\le d_2+2d_1+d_0.
$$

Outside $|x-1|\le\eta=\beta^{1/4}$ the integrand is at least $\eta^2$. The mass inside is at least $1/4-d_0-(d_2+2d_1+d_0)/\sqrt\beta$, uniformly $1/4-O(\sqrt\beta)$. For the explicit cutoff above, $H<2^{14}$ and $1/(1-\beta/r)\le2$, so $d_j\le2^{25+48j}\beta$. Thus $d_0\le1/32$ and $(d_2+2d_1+d_0)/\sqrt\beta\le2^{123}\sqrt\beta\le1/32$. The bare vector's projected norm exceeds $3/8$.

Centering and spectral projection are contractions in the same vacuum Hilbert space. If $G$ is within $\delta$ in sup norm of $F$, its projected norm is at least the bare projected norm minus $\delta$. For the ordinary plaquette after spatial flow, $\delta\le16u$ by the four-link speed estimate. For $u\le1/128$, the projected norm is at least $1/4$ and its square is at least $1/16$. More generally, for fixed $u$ the limiting lower bound on absolute weight is $(1/2-16u)_+^2$ as $\beta\downarrow0$. This is a bound on one reading's weight in a shrinking relative transfer band. It permits other spectral weight and several states in the band. [Flow speed and projection argument](strong-coupling.md) · [Chebyshev integral and projection arithmetic in Lean](MagneticVariance.lean)

For **any fixed finite $u$**, the inverse reconstruction in the preceding note achieves $\delta\le1/8$ with $R\ge6$ and $R+1\ge32eu$ because $8T_R(u)\le8\cdot 2^{-R}$. Its gauge-invariant reading of a finite patch of flowed links therefore meets the same $1/16$ bound. Gauge averaging and the full inverse ODE on the padded configuration are part of the construction. Only the ordinary plaquette uses the small-$u$ hypothesis.

The time and energy here are in lattice units. The band moves to increasingly high lattice energy in the strong-coupling limit. A4's concurrent electric-model calculation gives the same zero-spatial-coupling plaquette eigenvalue in Bessel notation and studies the magnetic derivative of the full finite-box gap at fixed temporal coupling. C4's separate fixed-momentum results concern the free continuum spectrum and selected weak Wilson trajectories. A nonzero correlation at fixed physical separation on the intended interacting continuum trajectory, followed by a gap estimate for a generating family, remains open. [A4's electric sector](../../observable-normalization/replica-gap/electric.md) · [C4's trajectory and momentum conditions](../../central-quotients/magnetic-smearing/flow-momentum/README.md)

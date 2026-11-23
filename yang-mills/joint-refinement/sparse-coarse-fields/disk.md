# A transverse local mode at distance c/β from the central disk boundary

Use the four-face planar SU(2) Wilson disk and adjacent-pair updates of [the central-fibre calculation](../full-complement/disk.md). Work in quaternion coordinates with a transverse traceless reference $B=e_x$. Fix $W_\delta=-\cos\delta+e_z\sin\delta$ and let $f=\Re(Bg_1)$. Write $V_\delta$ for its conditional variance and $J_\delta$ for its expected conditional loss averaged over the three adjacent-pair heat baths. Only the first heat bath changes $f$. For each fixed $c\ge0$,
$$
\lim_{\beta\to\infty}\frac{\beta J_{c/\beta}}{V_{c/\beta}}
=\frac{2/A-1}{3\sqrt2},\qquad
A=\frac{\coth b-1/b}{b},\quad b=\frac c{\sqrt2},\quad A(0)=1/3 .
$$
In particular the local quotient is of order $1/\beta$ on each of these off-central orbits. The matched four-dimensional box uses another measure and other heat baths. Its response to this test is an empirical question for Z4.

**Comparison with the central boundary.** Write $h=\cos\delta-e_z\sin\delta$. Right multiplication of $g_4$ by $h$ carries the fibre at $W_0=-I$ to the fibre at $W_\delta$, preserving the free Haar coordinates. Every pair exterior in this disk is carried to its counterpart. The fourth link or the pair product ending at that link is multiplied by the same constant. The mark remains $f$. The change in the log weight is $\beta[\Re(g_4h)-\Re g_4]$ with oscillation at most $2\beta\delta$. The variational characterization of prediction error and of variance gives
$$e^{-2\beta\delta}J_0/V_0\le J_\delta/V_\delta\le e^{2\beta\delta}J_0/V_0.$$
These comparisons apply to this fixed mark before or after simultaneous conjugation of $W,B$.

**Limit at the scale of the displacement.** Under the central measure the probability outside each fixed neighbourhood of the maximum set decays exponentially in $\beta$. Its maximum set is $g_1=\cdots=g_4=(1+\mathbf n)/\sqrt2$ for unit imaginary $\mathbf n$. Conjugation symmetry gives the unique uniform law on this sphere in the limit. The fixed $B$ occurs in a separate face factor and does not change this law. The preceding density tilt converges uniformly before normalization to $\exp[c(g_4)_z]$ for $\delta=c/\beta$. Consequently the induced limiting axis has density proportional to $\exp(b n_z)$ on $S^2$. Under this law $\mathbb E[n_x^2]=A$, by integrating $1-u^2$ against $\exp(bu)\,du$ on $[-1,1]$ and dividing by two. Axial symmetry gives mean zero for $f$ and $V_{c/\beta}\to A/2$.

Conditional on $p=g_1g_2$ of angle $t$, the first link has spherical tilt in direction $v=(1+p)/|1+p|$ of strength $k=2\beta\cos(t/2)$. Conditioning also on the unaffected links adds no new factor depending on $g_1$. Let $R=I_2(k)/I_1(k)$. The covariance of the tilted unit quaternion is $(R/k)(I-vv^\top)+R'vv^\top$, by differentiating its mean $Rv$ with respect to its vector parameter. Thus the first pair loss is the mean of $(1-v_x^2)R/k+v_x^2R'$. At the maximum set $t=\pi/2$ and $v_x^2=n_x^2/2$. The bounded tilt for fixed $c$ preserves exponential concentration outside any fixed neighbourhood of this set. On a neighbourhood with $k$ bounded below by a positive multiple of $\beta$, $R=1+O(1/k)$ and $R'=O(1/k^2)$ uniformly. The latter also follows from the recurrence $R'=1-R^2-3R/k$ and the first two terms of the expansion. The integrand is a bounded conditional variance elsewhere. It follows that $3\beta J_{c/\beta}\to (1-A/2)/\sqrt2$. Dividing by the variance gives the claimed expression. [Modified Bessel expansions](https://dlmf.nist.gov/10.40) · [Planar Yang–Mills face coordinates](https://doi.org/10.1016/j.geomphys.2011.10.005)

**Disproof test and scope.** For $\beta\theta\to0$ and fixed $c>0$, the coarse boundary lies strictly outside the radius-$\theta$ cap for large $\beta$. The reference face stays at distance $\pi/2$ from $-I$. At each finite $\beta$ the ratio is continuous in $(W,B)$ with positive denominator. Coarse localization therefore gives positive-measure tests on the clear part of this disk, as in [the central calculation](../full-complement/disk.md). Removing the exact central fibre or that narrower cap still permits an order-$1/\beta$ local quotient on the disk. A floor decaying at that rate can be compatible with summability of $a_n/\gamma_n$. Transfer at a common physical time and a four-dimensional all-observable floor require separate arguments.

| $c$ | $\beta J/V$ at $\beta=4096$ | Analytic limit |
|---:|---:|---:|
| 0 | 1.177973 | 1.178511 |
| 0.5 | 1.189693 | 1.190255 |
| 1 | 1.224365 | 1.224993 |
| 2 | 1.356277 | 1.357172 |
| 4 | 1.802769 | 1.804724 |

The [quadrature](disk.py) integrates over the angle and inclination of $p$ and the conditional radial tilt. It repeats the three integrations at orders (384, 40, 192) and (512, 52, 228) for each of the three couplings and five displacements. These are deterministic integrations on the planar disk.

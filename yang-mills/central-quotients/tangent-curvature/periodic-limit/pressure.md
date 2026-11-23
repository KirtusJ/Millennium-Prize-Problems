# The plaquette scale after the isotropic thermodynamic limit

Give the even periodic four-cube of side $L\ge4$ and volume $V=L^4$ the original pure $SU(2)$ Wilson weight. Haar measure on each oriented positive link has mass one. Use
$$
 S=\sum_p(1-\operatorname{Re}U_p),\qquad Z_L(\beta)=\int e^{-\beta S}\,dU,
 \qquad Y_p=\beta(1-\operatorname{Re}U_p).
$$
Here $\operatorname{Re}U$ means half the fundamental trace. For $\beta\ge2$ there is an absolute finite $K$ such that
$$
 3\,\mathbb E_{\beta,L}Y_p
 \le V^{-1}\log\frac{Z_L(\beta/2)}{Z_L(\beta)}
 \le K+6\,\frac{\log\beta}{L}. \tag{1}
$$
The left inequality is Jensen applied to $\mathbb E_{\beta,L}e^{\beta S/2}$. Translations and axis permutations make all $6V$ mean deficits equal. The finite-size remainder records precisely which order of limits the right inequality permits.

## Temporal forest and the seam

Fix the temporal links to the identity on each vertical column except the last, wrapping link. This is an exact integration change for the gauge-invariant action. On a column use the successive original path products up to each site as change of frame, beginning with the identity at time zero. The wrap variable becomes the full column product. For fixed original temporal links the transformed spatial links are again independent product Haar, by left and right invariance. The final column product is Haar independently on each column. Integrating the other temporal variables now gives one. Thus exactly $3V+L^3$ Haar variables remain.

For a lower bound restrict each of them to the angular ball about the identity of radius $s=\beta^{-1/2}$. Its normalized mass is at least $c\beta^{-3/2}$ from $(2/\pi)\sin^2\theta\,d\theta$. On this event every face has angular distance at most $4s$ by bi-invariance and the triangle inequality. Since $1-\cos t\le t^2/2$, its weighted deficit is at most eight, including on the seam. Therefore
$$
 Z_L(\beta)\ge e^{-48V}(c\beta^{-3/2})^{3V+L^3}.
$$
For an upper bound on $Z_L(\beta/2)$ keep only the temporal plaquettes linking successive *nonwrapping* time slices. Dropping each other factor increases the integral. For each positive spatial edge at time zero the remaining chain has $L$ spatial links and $L-1$ nearest-neighbor factors. Integrating from the last link back to the first gives $z(\beta/2)^{L-1}$, with $z(t)=\int e^{-t(1-\operatorname{Re}U)}dU$. There are $3L^3$ independent chains. The radial Haar formula, $\sin\theta\le\theta$ and $1-\cos\theta\ge2\theta^2/\pi^2$ yield $z(t)\le C t^{-3/2}$ for $t\ge1$. Hence
$$
 Z_L(\beta/2)\le(C'\beta^{-3/2})^{3V-3L^3}.
$$
Subtracting the logarithms gives the remainder in (1), since the exponents differ by $4L^3$ and $(3/2)\,4L^3/V=6/L$. The constants can be chosen independent of $L,\beta$. Z4's S3a uses a temporal-gauge pressure comparison. Faria da Veiga and O'Carroll develop Wilson stability and multi-reflection estimates for plaquette fields using free and periodic boundary conditions. The calculation here uses the $SU(2)$ angular measure and retains the wrap-variable count explicitly. [Z4's construction](../../../z4/attempt/reviews/a3-B/PROOF.md) · [Faria da Veiga and O'Carroll, §§II–IV](https://arxiv.org/pdf/2205.07376) · [Chatterjee on weak-coupling free energy](https://arxiv.org/abs/1602.01222)

## Consequences in every periodic limit state

At fixed $\beta$, take any subsequential local limit along even $L\to\infty$. The integrand $Y_p$ is a bounded continuous function of the four original links at that fixed $\beta$. Inequality (1) passes to the state and gives $\mathbb E_\beta Y_p\le K/3$, uniformly in $\beta$ and in the state chosen. This first moment suffices for the bounded dipole proof. [Curvature and spectral argument](spectral.md)

For the stronger action result, apply the finite-volume [reflection-doubling inequality](../moments.md) before sending $L$ to infinity. Here is the entire geometric step. Condition on the tangential links on two opposite site planes. No elementary face crosses a plane. The interior link integrals on the two sides are related by reflection, including link inversion. The remaining weight on the planes is positive. This gives $\langle f\,\theta f\rangle\ge0$ for real half-functions that may depend on the tangent links. Cauchy–Schwarz for this form yields $(\mathbb E g)^2\le\mathbb E[g\,\theta g]$. Begin with $g=e^{Y_p/8}$ assigned to one containing unit cube. In each of four axes, double the current block by reflection in its end site plane until its width is the largest power of two at most $L/2$. One half contains the old block at every step. The product occupies $J$ distinct nominal unit cubes, $J>V/256$. A single geometric plaquette can be charged at most four times, once per incident four-cube. Thus
$$
 (\mathbb E_{\beta,L} e^{Y_p/8})^J
 \le \mathbb E_{\beta,L}e^{\beta S/2}=Z_L(\beta/2)/Z_L(\beta).
$$
The expectation on the left has a bounded continuous integrand at fixed $\beta$. Taking $L\to\infty$ first in (1) gives $\mathbb E_\beta e^{Y_p/8}\le e^{256K}$, hence $\mathbb P_\beta(Y_p>t)\le e^{256K-t/8}$ simultaneously for every $\beta\ge2$ and every such state. This proves the S3a tail with its requested exponent. It also gives uniform integrability for any fixed product of polynomial powers of finitely many scaled curvatures and actions, by Hölder and $|\sqrt\beta\,\operatorname{Im} U_p|^2\le2Y_p$. [Site-plane reflection](../reflection.md) · [Menotti and Pelissetto](https://doi.org/10.1007/BF01221251)

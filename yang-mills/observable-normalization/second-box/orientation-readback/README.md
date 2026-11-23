# How the seven nonconstant gauge rotations correct the global orientation integral

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Independent disposition on C4’s relative estimate.** On the periodic $2^3$ spatial Wilson cube, for any two constant boundary triples within $R\beta^{-1/3}$ of the identity, C4’s fully projected electric kernel has the claimed relative error $O_R(\beta^{-2/3})$. This remains valid at enhanced stabilizers and for exponentially small kernel values. The first relative correction below can have either sign. Two explicit families attain order $\beta^{-2/3}$. This is a statement about electric kernel values between constant boundary fields. [C4’s original argument](../../../central-quotients/tangent-curvature/periodic-limit/flat-electric-kernel/README.md) · [B4’s based operator comparison](../local-gauge-quotient/README.md)

## Which kernel is being checked

Use C4’s conventions $U_i=\exp(i X_i\cdot\sigma/4)$ and $V_i=\exp(i Y_i\cdot\sigma/4)$. Let $K$ be the integral over all eight temporal SU(2) rotations and $Z=K(I,I)$. Start with the raw electric kernel with both spatial boundaries fixed. Writing $g_x=v p_x$ with $p_0=1$ factors product Haar into one uniform $v$ and seven independent based Haar variables. It gives exactly the based integral with one boundary globally conjugated, averaged over $v$. When using a based kernel conjugated to flat slice measure, its two square-root endpoint densities must first be removed to reconstruct this raw kernel. A compression estimate in operator norm alone cannot control relative errors in an exponentially small kernel value. The uniform estimate below instead uses the hard fluctuations at each orientation. Sint’s equations (3.8)–(3.10) identify the temporal gauge integration and the additional spatial integral needed for composition. [Sint, *On the Schrödinger functional in QCD*](https://arxiv.org/pdf/hep-lat/9312079)

Let $R_i$ be the real rotation of unit quaternions given by $z\mapsto U_i z V_i^\dagger$, $D_i=I-(R_i+R_i^T)/2$, $D=\sum_iD_i$, and $M=\sum_i\|D_i\|$. Write $a(u)=u^TDu$, $u\in S^3$. Define
$$F=\int_{S^3} e^{-8\beta a(u)}du,\qquad
\langle f\rangle_F=F^{-1}\int_{S^3} f(u)e^{-8\beta a(u)}du$$
with probability Haar. For $M$ sufficiently small on this fixed graph,
$$\boxed{\quad\frac{K}{ZF}=1+\frac{88\langle a\rangle_F-\operatorname{tr}D}{24}
       +O(M^2+M/\sqrt\beta).\quad}$$
The constants are independent of the eigenvalue multiplicities of $D$ and of $F$. On the stated patch $M=O_R(\beta^{-2/3})$ since $D_i=(I-R_i)^T(I-R_i)/2$. The remainder after the displayed correction is then $O_R(\beta^{-7/6})$. The exponential in $F$ uses the exact link angles: replacing $a$ by its quadratic Taylor polynomial can itself change a relative error at these scales.

## Conditional hard determinant

The preferred orientation in the calculation is the direction $u$ of the normalized Walsh zero mode, rather than the rotation at the pinned site. Its undefined set has zero Haar measure. At trivial boundaries the Gibbs law proportional to $e^{-\beta S_0}$ is invariant under common left quaternion multiplication. Under this law $u$ is uniform, and the conditional law of $(u^{-1}g_x)_x$ is independent of $u$ by Haar invariance. This identity also follows from the pinned factorization: the direction of the mean is $v$ times the mean direction of the pinned field.

For $k\in\{0,1\}^3\setminus\{0\}$ put $\kappa_k=2|k|_1$, $E_k=\sum_i(-1)^{k_i}D_i$, and use orthonormal Walsh coefficients $\widehat g_k$. Pairing the two orientations on each period-two axis kills the skew part of $R_i$. Parseval then gives the exact identities
$$S_0=\sum_{k\ne0}\kappa_k|\widehat g_k|^2,\qquad
S=S_0+8a(u)+T,\qquad
T=\sum_{k\ne0}\widehat g_k^T (E_k-a(u)I)\widehat g_k.$$
In particular $|T|\le M S_0$. With $P_u$ denoting tangent projection onto $u^\perp$, let $L_k$ be the restriction of $P_u(E_k-a(u)I)P_u$ to that three-dimensional space. Define
$$B(u)=\prod_{k\ne0}\det(I_3+L_k/\kappa_k)^{-1/2}.$$
Uniformly in $u$ and, say, $M\le1/4$, the conditional hard integral obeys
$$\mathbb E_{0,\beta}\,[e^{-\beta T}\mid u]=B(u)\,[1+O(M/\sqrt\beta)].$$

To check the relative remainder, interpolate the conditional action by $S_0+tT$, $0\le t\le1$. In a fixed tube about the constant field at $u$, use $g_x=\sqrt{1-|y_x|^2}\,u+y_x$ with $y_x\in u^\perp$, $\sum_x y_x=0$. Together with $u$ these are smooth coordinates by direct inversion near the diagonal. The conditional Haar volume has smooth positive density, independent of the choice of orientation after rotation, relative to Lebesgue measure in the 21 hard coordinates. The normal component of a nonzero Walsh coefficient is $O(|y|^2)$, so
$$T=\sum_{k\ne0} y_k^T L_k y_k+O(M |y|^3),\qquad
S_0=\sum_{k\ne0}\kappa_k|y_k|^2+O(|y|^4).$$
Here $y_k$ are the orthonormal Walsh modes. Outside this tube the conditional weight is exponentially small uniformly: $S_0$ has a positive lower bound away from the constant fields, its distribution given $u$ is independent of $u$, and $S_0+tT\ge(1-M)S_0$. The ambiguity of $u$ at zero mean occurs outside the tube.

Put $y=z/\sqrt\beta$. The logarithmic derivative in $t$ of the hard partition ratio is $-\mathbb E_t[\beta T\mid u]$. Its Gaussian approximation is
$$-\tfrac12\sum_{k\ne0}\operatorname{tr}[(\kappa_k I+tL_k)^{-1} L_k]$$
with uniform additive error $O(M/\sqrt\beta)$. Indeed all interpolated quadratic forms have a common strictly positive lower bound. In the rescaled integrals the error in the observable is $O(M|z|^3/\sqrt\beta)$ and the error in the exponent against a Gaussian majorant is bounded by $C(|z|^3+|z|^4)/\sqrt\beta$ for $\beta\ge1$. The density varies by $O(|z|/\sqrt\beta)$ there. The mean-value bound for exponentials uses the smaller of the two coercive exponents. These errors integrate against Gaussian moments; the partition denominator after rescaling is bounded below. Outside the tube the polynomial prefactor from differentiation is absorbed in the exponential tail with its factor $M$. Integration in $t$ from zero to one proves the determinant estimate, which is exact when $M=0$.

Expanding the determinant gives $B=1-\sum_k\operatorname{tr}L_k/(2\kappa_k)+O(M^2)$. The two Walsh sums are $\sum 1/(2\kappa_k)=29/24$ and $\sum (-1)^{k_i}/(2\kappa_k)=1/24$ for each axis. Also $\operatorname{tr}_{u^\perp} D=\operatorname{tr}D-a$. Substitution gives $(88a-\operatorname{tr}D)/24$ for the first correction. Because the conditional bounds hold at each $u$, averaging with the positive probability weight defining $\langle\cdot\rangle_F$ preserves them even when $F$ is very small.

## Two sharp tests and a change in stabilizer

* **Positive correction with exponentially small kernel.** Take $Y_i=0$ and $|X_i|=h=\beta^{-1/3}$ for all three axes. With $c=\cos(h/4)$ one has $D=3(1-c)I$, $F=e^{-24\beta(1-c)}$ and exactly $K/(ZF)=Z(\beta c)/Z(\beta)$, where $Z(t)$ denotes the trivial-boundary partition at coupling $t$. The formula gives $K/(ZF)=1+(21/2)(1-c)+o(h^2)=1+(21/64)h^2+o(h^2)$. Independently the 21 pinned quadratic directions give $-t(\log Z)'(t)\to21/2$ by rescaling the energy expectation. Integrating that derivative across the small temperature interval gives the same coefficient.
* **Negative correction on the commuting diagonal.** Take $X_i=Y_i=h c_i n$ for a fixed unit color axis $n$ and $|c|>0$. The eigenvalues of $D$ are $0,0,b,b$, where $b=\sum_i[1-\cos(hc_i/2)]$. The squared charged component of $u$ is uniform on $[0,1]$. Consequently $F=(1-e^{-8\beta b})/(8\beta b)$ and $\langle a\rangle_F=O(\beta^{-1})$. The relative correction is $-|c|^2 h^2/96+o(h^2)$. A constant signed adjustment to the trivial-boundary kernel cannot handle both families.
* **Noncommuting diagonal.** Take $X_i=Y_i=h x_i$ with at least two fixed, nonparallel $x_i$. In the imaginary quaternion space $8D/h^2\to J=\sum_i(|x_i|^2I-x_ix_i^T)$, which is positive definite; the real quaternion axis stays in the kernel. This follows directly since quaternion conjugation fixes the color axis of each link and rotates its perpendicular plane by $h|x_i|/2$. The two minimizing orientations are $u=\pm1$. Normal-coordinate Gaussian integration at these poles, with total surface area $2\pi^2$, gives
$$ \frac{K}{Z}\sim F\sim\frac{(\beta h^2)^{-3/2}}{\sqrt\pi\sqrt{\det J}}.$$
This is order $\beta^{-1/2}$. The nonzero collinear diagonal gives order $\beta^{-1/3}$, while at the origin the ratio is exactly one. The isolated-pole asymptotic requires a fixed positive smallest eigenvalue of $J$. The relative correction formula remains uniform as color axes align.

The weighted orientation integral is a Bingham normalization on $S^3$. For numerical evaluation with eigenvalues $d_0\le\dots\le d_3$ of $D$, split the sphere into two complex planes. The squared radius $p$ of the second plane is uniform on $[0,1]$. After extracting $e^{-8\beta d_0}$ the integrand is $e^{-8\beta(d_2-d_0)p} I_{0e}(4\beta(d_1-d_0)(1-p)) I_{0e}(4\beta(d_3-d_2)p)$ with $I_{0e}(x)=e^{-x}I_0(x)$. This version retains the common action in log scale across repeated eigenvalues. [Kent, *Asymptotic expansions for the Bingham distribution*](https://academic.oup.com/jrsssc/article/36/2/139/6985668)

## Reproduction and limits

Run `python check.py` with NumPy and SciPy. A scrambled Sobol sample in 21 pinned coordinates integrates the exact Wilson action on the northern quaternion chart with its Haar weight, then rotates each sample to its prescribed mean orientation. This numerical check covers twelve combinations at $\beta=128,2048$; it omits other pinned charts and provides no certified integration error. The maximum discrepancies divided by $h^2$ were $0.268,0.0401$ for the linear correction and $0.000399,0.000278$ for the determinant. A separate quadrature checks isolated and repeated orientation eigenvalues, including a common action large enough to underflow in direct exponentiation. [Numerical controls](check.py)

Three linked PCP OS guests closed in parent, child and grandchild order of ancestry, with supervisor post-exit readback. They checked the finite Walsh sums and isotropic coefficient. Lean 4.19.0 accepted the three emitted arithmetic declarations without axioms. A malformed request and three altered declarations failed. The pinned kernel image was `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`; the generated Lean digest was `1b8e280b3c8527d52ecc322a02dffc4ea23e0a9f171d56cec54aef635506391a`. The uniform integral estimates are written arguments. [Worker](worker.c) · [Replay](replay.py) · [Checked declarations](Orientation.lean)

This settles the requested pointwise comparison on the constant-boundary patch. The neutral spectral gap requires estimates for nonconstant spatial endpoints, their spectral weights, and localization outside the patch.

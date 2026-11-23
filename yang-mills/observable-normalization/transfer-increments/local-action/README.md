# Uniform covariance comparison for the single Wilson plaquette action

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Take any thermodynamic limit $\mu$ of isotropic even periodic four-cubes in pure four-dimensional $SU(2)$ Wilson theory at fixed $\beta$. On one spatial $12$-face at $(t,z)$ put $Y(t,z)=\beta(1-\tfrac12\operatorname{Tr}U_{12}(t,z))$. Let $G(n,z)$ be the one-color free lattice Maxwell covariance between these faces at displacement $(n,z)$, for covariance the projection onto exact two-cochains. Then for all sufficiently large $\beta$,
$$
 \sup_{\mu,\, n\ge0,\,|z|_1\le\beta^{1/4}}
 \left|\operatorname{Cov}_\mu(Y(0,0),Y(n,z))-\tfrac32 G(n,z)^2\right|
 \le C\beta^{-1/8}. \tag{1}
$$
Here $n,z$ are lattice coordinates. In particular the variance is $3/8+O(\beta^{-1/8})$. At zero spatial displacement the covariance divided by the variance differs from $[G(n,0)/G(0,0)]^2$ by at most $C\beta^{-1/8}$ uniformly over all lags. This estimates Z4’s original action with its original normalization. Auxiliary spatial averages enter the proof only.

The centered single-plaquette vector has spectral weight of order $n^{-8}$ at lattice energies of order $1/n$ in the range $1\ll n\ll\beta^{1/64}$. Its exponentially tilted energy and momentum in units $(nE,nk)$ converge to the sum of two independent massless vectors. The energy law is Gamma with shape 8 and rate 1. The asymptotic coefficient, the range at the endpoint, and the angular distribution are given in the [spectral proof](spectrum.md). These results concern the lattice action below the correlation length. A positive gap for fixed coupling and a continuum Yang–Mills theory with a positive mass gap remain open.

[Z4’s single-plaquette question](../../../z4/attempt/THEOREM_B.md) · [C4’s fixed-lag solution and action moments](../../../central-quotients/tangent-curvature/periodic-limit/spectral.md) · [C4’s earlier polynomial Ward and reflection method for ordinary profiles](../../../central-quotients/magnetic-smearing/ordinary-profile.md)

For the [hypercubic sum of all 24 incident plaquettes](site-scalar/README.md), the mixed-orientation extension gives all fixed-order scalar Schwinger functions on a common growing scale.

The [parity-odd clover](odd-clover/README.md) has a positive lattice variance per unit volume at weak coupling. Its free contact cancellation controls a surface term and gives a decaying upper bound on that variance.

## A finite-coupling bound on a straight average

Order the root path along time, spatial axes 2 and 3, then axis 1. Denote the transported $\sqrt\beta\operatorname{Im}U_{12}$ by $F$. Every spatial line along axis 1 uses a common prefix and then straight paths. Changing the common root to any site of that line conjugates every transported face along it by the same quaternion, by free cancellation. Products of different color components will be evaluated in the original frame; the vector norm of a line average can be bounded in any of these frames.

On a run of even length $L$, group the faces in pairs with bases $a+2j$ and $a+2j+1$ along the line, and write $D_j$ for the sum of the two transported three-vectors. For $j<k$ the plane perpendicular to axis 1 at $a+j+k+1$ lies between the two pairs. Re-root at its site on the line. Reflection sends the positive pair $D_k$ to $-D_j$. Indeed a positive face based at $x$ reflects to the reversed face at positive base $2(a+j+k+1)-x-1$. Changing the base adds a single step along the normal. That step extends or cancels in the straight path, so the reflected rooted word is the inverse at the common root. This is an exact group identity. Even adjacent pairs lie in the two closed halves and may use their tangent links. Site-reflection positivity on each real component gives $\mathbb E D_j\cdot D_k\le0$. Returning to the original root preserves this dot product configuration by configuration. One can Haar-average the complete product if the state is specified on gauge-invariant functions. [Reflection of the positive face and site-plane positivity](../../../central-quotients/tangent-curvature/reflection.md) · [Menotti and Pelissetto on lattice reflection positivity](https://doi.org/10.1007/BF01221251)

The periodic-state action tail implies $\|F_p\|_q\le C_q$ for every finite $q$, uniformly in face and state. Expanding the squared norm of the sum of the pairs now gives
$$
 \left\|L^{-1}\sum_{u=0}^{L-1} F_{a+u}\right\|_2^2
 \le L^{-2}\sum_{j=0}^{L/2-1}\mathbb E |D_j|^2\le C/L. \tag{2}
$$
The bound is for a vector average in a common transported frame on any such line. It holds at each coupling and each starting point. [Exponential action moment](../../../central-quotients/tangent-curvature/periodic-limit/pressure.md)

## Restore three differences temporarily

For a unit single-face color test $u$ put $g=(I-A_L)^3u$, where $A_L=L^{-1}\sum_{j=0}^{L-1}\tau_{j e_1}$. The total coefficient norm of $g$ is at most eight. Each $A_L^r u$ for $r=1,2,3$ is a convex combination of translates of $A_Lu$. Equation (2) and the triangle inequality give $\|F(g)-F(u)\|_2\le C L^{-1/2}$. The same estimate holds for free Gaussian curvature since $P$ is a contraction and $\|A_Lu\|_{\ell^2}=L^{-1/2}$. All fixed higher moments of each $F(g)$ and $F(u)$ are bounded uniformly by their coefficient norms and the one-face moments. Consequently replacing up to four such factors in any product costs $O(L^{-1/2})$ in expectation, by telescoping the product and applying Cauchy–Schwarz to the replaced factor and Hölder to the others.

Write $D=I-\tau_{e_1}$. Then $I-A_L=D H_L$, where the coefficients of $H_L$ at $j=0,\ldots,L-2$ are $(L-1-j)/L$. They are nonnegative and sum to $(L-1)/2$. Thus $g$ is also a third unit difference of an array of mass norm at most $C L^3$ and support length at most $3L$. Allow the face center to have $|z|_1\le C_0 L$ and arbitrary time.

Use C4’s finite Hodge decomposition with $K=I-\Delta/16$, $S_M=16^{-1}\sum_{l=0}^{M-1}K^l$, $h=d^*S_M g$, $k=dS_Mg$, $b=K^M g$. It gives $g=dh+d^*k+b$, $dh=P(g-b)$. With $w(x)=1+|\mathbf x|_1$ the estimates needed here are
$$
 \|h\|_{1,\sqrt w}+\|k\|_{1,\sqrt w}\le C L^{3/2},\quad
 \|h\|_\infty\le C,\qquad \|b\|_1\le C L^3(1+M)^{-3/2}. \tag{3}
$$
For the first bound let $N=1+l$. An order-$a$ walk difference has mass norm at most $C_aN^{-a/2}$ and spatial first-weight moment at most $C_aN^{(1-a)/2}$. Cauchy–Schwarz gives its square-root displacement moment at most $C_aN^{1/4-a/2}$. Translating from a profile at spatial radius $O(L)$ adds at most $C\sqrt L$ times the mass norm. Up to $l<L^2$ sum $C[\sqrt L N^{-1/2}+N^{-1/4}]$ using the bounded mass of $g$. From $l=L^2$ sum $C L^3[\sqrt L N^{-2}+N^{-7/4}]$ after moving its three differences to the kernel. Both sums are $O(L^{3/2})$. Three differences without the extra derivative give the bound on $b$. For the sup bound the walk multiplier is $1-\sum_{i=0}^3(1-\cos p_i)/8\in[0,1]$ and is at most $e^{-c|p|^2}$ on the four-dimensional Brillouin cube. Fourier integration therefore bounds $\|K^l\|_\infty$ (kernel sup norm) by $C N^{-2}$. A single difference has at most twice this bound. Summing in $l$ and using $\|g\|_1\le8$ proves (3). All constants are independent of the time coordinates and of $M$. [Walk bounds and Hodge identity](../../../central-quotients/tangent-curvature/periodic-limit/rate/heat.md)

## Polynomial moments with the full moving-path derivative

Take $1\le r\le4$ tests $g_i$ of the preceding form and write $X_i=F(g_i)$. For the prefactor $g_1$ use (3). The original-link Haar identity applied to $Q=\prod_{i=2}^r X_i$ gives
$$
 \mathbb E\prod_{i=1}^r X_i
 =\sum_{j=2}^r\langle P g_1,g_j\rangle\,
       \mathbb E\!\prod_{i\ne1,j}X_i + O_r(L^{3/2}/\sqrt\beta). \tag{4}
$$
The error is an expectation. In particular the reflected-strip bound is needed only in $L^2$ for a rooted link. Here are the estimates with the extra polynomial factors.

* For one varied positive edge, take the color generator along a root path avoiding that edge, using a one-face detour if needed. Each incident score discrepancy contains a rooted prefix or detour error paired with a scaled face. Its root norm is $O(\sqrt{w(e)}/\sqrt\beta)$ in $L^2$ by the strip bound, unchanged under permuting the spatial ordering. Pair this error by Cauchy–Schwarz with $|F_p Q|$, whose $L^2$ norm is uniformly bounded by the exponential face moment and Hölder. The signed direct derivative of a tested face likewise costs $O(\sqrt{w(e)}/\sqrt\beta)$ after pairing with the remaining polynomial factors. The extra unscaled plaquette deficit has $L^2$ norm $O(\beta^{-1/2})$. Summing the at most six incident faces costs only the test sup norm, at most eight.
* Differentiating a root transporter or its inverse produces a commutator bounded by $2|F_p||h_e|/\sqrt\beta$ for each traversal. Here $h$ has only components 1 and 2 since all input faces have orientation $12$. Time trunks contribute zero. Each spatial path of any $g_j$ has $O(L)$ steps, even at the displaced center. Using $\|h\|_\infty\le C$, $\|g_j\|_1\le8$ and the uniform polynomial moments gives a total $O_r(L/\sqrt\beta)$.
* Replacing $F(g_1)$ by $F(dh)$ leaves the coexact cube term and $F(b)$. In the cube identity, products of at least two unscaled face deficits cost $O_r(\beta^{-1})$ in expectation against $Q$ by Hölder, since $\||1-U_p|\|_q=O_q(\beta^{-1/2})$ for every fixed $q$. Taking the scaled imaginary part costs a factor $\sqrt\beta$. Removing a short conjugation from a scaled face is bounded by Cauchy–Schwarz exactly as for the score. Summation against $k$ costs $O_r(\|k\|_{1,\sqrt w}/\sqrt\beta)$. The residual costs $C_r\|b\|_1$ by Cauchy–Schwarz.
* The leading derivative of each $X_j$ gives $\langle dh,g_j\rangle$. Its difference from $\langle Pg_1,g_j\rangle$ is bounded by $\|b\|_2\|g_j\|_2$. All finite-support identities hold on each sufficiently large torus at fixed coupling and then in the limit state. Send $M\to\infty$ at fixed $L$, positions and coupling to obtain (4).

[Signed generator, cube words and Haar identity](../../../central-quotients/tangent-curvature/periodic-limit/rate/ward.md) · [Half-weight estimates and segment swaps](../spatial-packet/strip/README.md) · [Lattice group integration by parts](https://arxiv.org/abs/2309.07399)

The free centered Gaussian variables obey the same recursion with zero error. Each covariance coefficient is bounded by $\|g_1\|_2\|g_j\|_2\le64$. Induction from the empty product therefore gives a difference of at most $C_r L^{3/2}/\sqrt\beta$ between the filtered moments. Restoring the unfiltered tests costs $C_r L^{-1/2}$ by (2). Take $L$ to be the smallest even integer at least $\beta^{1/4}$. The combined error is $O_r(\beta^{-1/8})$.

Finally, for each anchored face the exact quaternion relation is $2Y=|F|^2+Y^2/\beta$. The difference between $Y$ and $|F|^2/2$ has $L^2$ norm $O(\beta^{-1})$. The common color frame disappears from the squared norm. Applying the second and fourth moment comparisons gives (1) since the covariance of half the squared norms of two three-color Gaussian vectors with cross-covariance $G I_3$ is $3G^2/2$. At zero lag the one-color variance is $G(0,0)=1/2$, by symmetry of the four coordinate contributions in the exact two-form projection. [Formal and numerical checks](checks.md)

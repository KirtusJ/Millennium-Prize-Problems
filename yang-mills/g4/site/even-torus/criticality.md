# The lattice-unit transfer gap in periodic infinite-volume states

For each $\beta\ge2$ let $\omega_\beta$ be any local weak subsequential limit of the original isotropic SU(2) Wilson measures on even $L^4$ tori, sending $L\to\infty$ at fixed $\beta$. Such states exist by compactness. Local translation invariance and reflection positivity pass to each state. Consider the gauge-invariant transfer constructed from this same state and its constant vector $\Omega_\beta$. The following argument combines the preceding even-torus estimate, C4’s rooted Haar identities, and Z4’s spectral upper-bound argument. It requires no choice of a common finite-volume subsequence across couplings. [Periodic-state exponential moment](periodic-tail.md) · [C4’s original-link derivation](../../../central-quotients/tangent-curvature/wilson-law.md) · [Z4’s S0–S3](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/2a05225/yang-mills/z4/attempt/reviews/a3-B/PROOF.md)

## Passing the local variations in this order

Write unit quaternions as $q=x+\mathbf u$, with scalar part $x=\operatorname{ReTr}(q)/2$. Compare arbitrary $\beta_j\to\infty$ and arbitrary choices of $\omega_{\beta_j}$. The uniform exponential moment for $Y_p=\beta(1-x_p)$ bounds all its fixed moments, in every face orientation. Choose a rooted tree of the infinite lattice and transport links to its root frame, writing $U'_e$ for the resulting link and $F_p^\beta=\sqrt{\beta}\operatorname{Im}U'_p$. A fixed rooted link is a fixed contractible loop once the finite boxes are large. It is a finite product of conjugated plaquette holonomies and their inverses, by cancellation of backtracks and elementary square moves. The SU(2) angular metric satisfies $d(1,q)^2\le(\pi^2/2)(1-\operatorname{Re}q)$. Thus the triangle inequality and Cauchy–Schwarz give a uniform bound on $\mathbb E_\beta[\beta d(1,U'_e)^2]$ for each fixed rooted link. The bound can depend on its chosen path.

The local logarithms $A^\beta_e=\sqrt{\beta}\log U'_e$ are tight, with any measurable choice at the cut point. On finite bounded sets of these variables the plaquette-word expansion gives $F_p^\beta=(dA^\beta)_p+o(1)$. Truncation gives $o_{\mathbb P}(1)$ along the sequence. Hence any subsequential joint law $F$ of the countably many rooted faces satisfies $dF=0$. Such laws exist by local tightness and diagonal extraction. Component second moments are uniformly bounded over all faces, since $|F^\beta_p|^2\le2Y_p$. Changing the finitely many paths for fixed tests conjugates each tight vector by a fixed loop tending to identity in probability, preserving all its limiting joint laws.

For an edge $e$, choose the tree to avoid $e$. Each of the finitely many required path frames is then independent of the value of $U_e$ as a **coordinate function** of the links. Conditionally holding the other links fixed, vary $U_e$ by the conjugated left translation which sends $U'_e$ to $\exp(sX/\sqrt\beta)U'_e$, for fixed imaginary quaternion $X$. Every other rooted link stays fixed under this variation. Start with the finite-torus Haar integral. For a bounded $C^1$ test $f$ of finitely many scaled face vectors with bounded continuous derivatives, differentiation gives
$$
 \mathbb E_\beta[\partial_s f(F^\beta(s))|_{s=0}]
 =\mathbb E_\beta\!\left[f(F^\beta)\sqrt\beta\sum_{p\ni e}
 D_{e,X}(1-x_p)\right].
$$
Here $D_{e,X}$ uses the unscaled generator. At **fixed** $\beta$ both sides are bounded continuous functions of finitely many original links. The equality thus holds in the chosen periodic limit. Classical lattice Schwinger–Dyson identities also start from compact-link Haar invariance. The estimates used to pass this particular identity to weak coupling are explicit here. [Lattice identity and Haar derivatives](https://arxiv.org/abs/2608.05415)

For a face with incidence $\epsilon_{pe}=\pm1$, differentiation inserts $X$ or $-X$ into its word. The derivative of the scaled imaginary part tends to $\epsilon_{pe}X$ in probability and is bounded by $|X|$. Cyclicity of scalar trace gives the exact scaled score $\epsilon_{pe} X\cdot\sqrt\beta\,\operatorname{Im}(V^{-1}U'_p V)$ where $V$ is the product before the distinguished occurrence, with its inverse edge included there for a negative occurrence. All such short conjugators tend to identity. Each score has a uniform second moment, so the product with bounded $f$ is uniformly integrable. Pass to the limit in this avoiding tree first, and then identify the limiting variables with those in the common tree by the path comparison. This order avoids differentiating an error known only to vanish in probability. Summing the edge identities yields
$$
 \mathbb E[\partial_{dh}f(F)]=\mathbb E[F(dh)f(F)]
$$
for each finitely supported real three-color one-cochain $h$. Every approximation above concerns a fixed finite patch at fixed test lag. There is no assertion of uniform local Laplace convergence over external boundary data.

## Gaussian and harmonic parts

For finite face tests $g$, put $\phi(g)=\mathbb E e^{iF(g)}$. For $u=dh$ the identity gives
$$
 \partial_t\phi(g+tu)=-(\langle g,u\rangle+t\|u\|^2)\phi(g+tu).
$$
The solution shows that $F(u)$ for compact exact directions is a joint centered Gaussian isometry. Extend it in $L^2$ to $Z(u)$ on the closed exact subspace $\mathcal E=\overline{dC_c^1}^{\,\ell^2}$. Let $P$ be its projection, $G(g)=Z(Pg)$ and $R(g)=F(g)-G(g)$. We have $d^*R=0$ because $R(dh)=0$. Also $dR=0$ because $F$ is closed and $P d^*k=0$ for finite three-cochains $k$. The identity $dd^*+d^*d=\Delta_{\rm scalar}$ on components follows from the exterior multiplication symbol $p_\mu=e^{ik_\mu}-1$ and its adjoint. Every component of $R$ is harmonic and has uniformly bounded second moments. For any $Y\in L^2$, the bounded harmonic function $x\mapsto\mathbb E[R(x)Y]$ on $\mathbb Z^4$ is constant. For instance, lazy walks from adjacent sites can synchronize their other coordinates and couple the remaining one-dimensional difference until it hits zero almost surely. Harmonicity and boundedness then identify their starting values. Taking $Y=R(x)-R(0)$ shows that $R$ is a spatially and temporally constant random two-form $H$.

The characteristic identity extends to exact $u\in\mathcal E$ by $L^2$ approximation. In its integrated form, evaluated with $u-Pg$, it yields
$$
 \mathbb E e^{iR(g)+iZ(u)}
 =\phi(g)e^{\|Pg\|^2/2} e^{-\|u\|^2/2}.
$$
Thus $H$ is independent of the full three-color Gaussian $G$, also for joint finite tests by linear combinations. No classification of general gauge-fixed infinite-volume DLR specifications is required. This is C4’s decomposition applied to the finite-patch identities just proved. [C4’s Gaussian decomposition and projection multiplier](../../../central-quotients/tangent-curvature/gaussian.md)

## A nonzero long-lag covariance and its spectral direction

For a spatial $12$ face and separation $n$ in time, denote the single-color covariance of $G$ by $g_n$. The diagonal Fourier multiplier of $P$ is $(|p_1|^2+|p_2|^2)/\sum_{\mu=0}^3|p_\mu|^2$, with $g_0=1/2$ by permutation symmetry. Integrating the time frequency gives
$$
 g_n=\int_{[-\pi,\pi]^3}\frac{s_{12}}{2\sinh w}e^{-|n|w}\frac{d^3k}{(2\pi)^3},
 \qquad s_{12}=|p_1|^2+|p_2|^2,\quad \cosh w=1+\tfrac12\sum_{j=1}^3|p_j|^2.
$$
Indeed the Fourier coefficients of $[2(\cosh w-\cos k_0)]^{-1}$ are $e^{-|n|w}/(2\sinh w)$ by a geometric series. Thus $0<g_n\le g_0$. On $1/n\le k_1\le2/n$ and $0\le k_2,k_3\le1/n$, $n\ge1$, we have $s_{12}\ge4/(\pi^2n^2)$, $w\le\sqrt6/n$ and $\sinh w\le\sqrt{15}/n<4/n$. The box has volume $n^{-3}$. In particular
$$
 g_n\ge e^{-\sqrt6}(16\pi^5)^{-1}n^{-4}.
$$

At each face the exact identity $2Y_p=|F^\beta_p|^2+Y_p^2/\beta$ and the exponential moment pass fixed joint second moments of $Y$ to those of $|G+H|^2/2$. This also gives the finite fourth moments needed below. Put $a=\mathbb E|H_{12}|^2$ and $b=\operatorname{Var}(|H_{12}|^2/2)$. Conditional Gaussian moments and independence give limiting connected covariance and variance
$$
 C(n)=\tfrac32 g_n^2+a g_n+b,\qquad C(0)=\tfrac32 g_0^2+a g_0+b>0.
$$
These coefficients can depend on the selected tangent subsequence. The ratio $C(n)/C(0)$ is a convex combination of $(g_n/g_0)^2,g_n/g_0,1$, so it is bounded below by $(g_n/g_0)^2$ **for all** such subsequences. In particular, for every fixed even $n$, the liminf of the connected plaquette covariance divided by its variance has this lower bound in any selection of periodic states. This argument tolerates the constant mode and does not import its elimination in C4’s different limiting construction.

For completeness, use the site reflection form on bounded positive-half cylinders, its quotient and completion. Shifting one step into the half gives a symmetric map $T$ by translation and reflection. Cauchy–Schwarz gives $\|Tf\|_{\rm OS}^2\le\|f\|_{\rm OS}\|T^2f\|_{\rm OS}$. Null vectors are preserved. Iterating this bound and using $\|T^jf\|_{\rm OS}\le\|f\|_\infty$ gives a self-adjoint contraction on the completion with $T\Omega=\Omega$. The positive transfer convention also follows from Wilson link-plane positivity for the plane halfway between sites, applied to the one-step translate of $f$. Only even powers are needed for this argument. For the centered time-zero spatial plaquette $\psi_\beta=(Y_p-\omega_\beta Y_p)\Omega$, the reflected norm is its variance and the $n$-step matrix element is exactly $C_\beta(n)$ of the same state. Therefore $0\le C_\beta(n)\le e^{-nm(\beta)}C_\beta(0)$ for even $n$. [Lüscher’s Wilson transfer](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf) · [Periodic two-seam construction](../../periodic/README.md)

First send $\beta\to\infty$ at each fixed even $n$. Then $\limsup_\beta m(\beta)\le -2\log(g_n/g_0)/n$. Sending even $n\to\infty$ and using the polynomial lower bound proves $m(\beta)\to0$. A degenerate vacuum complement carrying invariant vectors already has $m=0$. The positive limiting plaquette variance supplies nonzero test vectors for large $\beta$. No lower bound on $m$, no rate in $\beta$, and no physically scaled positive-lag observable follow from these two limits. The argument addresses (B). The missing implications in Z4’s (A) and (C) concern different estimates. [Z4’s ledger](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/2a05225/yang-mills/z4/attempt/A1_LEDGER.md)

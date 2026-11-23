# Site reflection in all four directions and the periodic-state tail

Use one independent normalized Haar link per positively oriented edge on an even periodic hypercube of side $L=2m\ge4$ and $V=L^4$ sites. Reverse edges by group inversion. Write $D_p=1-\operatorname{ReTr}(U_p)/2$ for SU(2), $S=\sum_pD_p$, $Z(\beta)=\int e^{-\beta S}$ and $Y_p=\beta D_p$. A link on the boundary can occur in both factors of a reflected test.

## The original-link integral

Distinguish any coordinate and index its layers by $t=0,\dots,2m-1$. The reflection sends $t$ to $-t\bmod 2m$. Tangent links on $0,m$ are fixed individually. The remaining tangent links at $1,\ldots,m-1$ and $m+1,\ldots,2m-1$ are paired. The forward normal link based at $t$ maps to the inverse of the forward normal link based at $2m-1-t$. Thus the positive normal anchors are $0,\ldots,m-1$, including the link ending at $m$, and all their partners lie in the opposite half. A normal plaquette occupies a single normal interval and its bounding tangent edges. Tangent plaquettes live in their own layer. Each plaquette is therefore fixed on a boundary or belongs to a reflected pair. Its real trace is unchanged by inversion and cyclic re-rooting. These statements also hold after a translation of the plane.

Let $b$ denote the two tangent-link layers and $x,y$ the two half configurations, reindexing the negative half by the reflection. Permutations and inversions preserve product Haar. The action is $S_\partial(b)+S_+(b,x)+S_+(b,y)$. For a bounded measurable complex function $F$ of a closed half put $f(b,x)=e^{-\beta S_+(b,x)}F(b,x)$ and $w(b)=e^{-\beta S_\partial(b)}/Z(\beta)$. Then
$$
 \mathbb E_\beta[\overline{F\circ r}\,F]=
 \int w(b)\left|\int f(b,x)\,d\mu(x)\right|^2d\eta(b)\ge0 .
$$
All integrals exist since the original lattice is finite and the test bounded. The two boundary layers are integrated once against the indicated weight. The proof allows gauge-dependent tests and every choice of axis. The Lean integral theorem accepts an integrable product expression and nonnegative weight. The original-link reindexing, Haar inversion and plaquette-word identification are mathematical steps in this text. This is the pure-gauge specialization. The site-plane Wilson reference also treats fermions. [C4’s even- and odd-site argument](../../../central-quotients/tangent-curvature/reflection.md) · [Menotti and Pelissetto](https://doi.org/10.1007/BF01221251)

## Doubling with both seams present

For real bounded half-tests use Cauchy–Schwarz for the positive reflection form against $1$. Thus $(\mathbb E g)^2\le\mathbb E[g(g\circ r)]$. Assign $g=e^{Y_p/8}$ to a unit four-cube containing $p$. Reflect the occupied rectangular block about one of its end layers, starting with width one in each direction. Double in a direction while the old width is at most $L/2$, using an axis translation to put that block in a closed half. When $2w=L$, the copies meet along both boundary layers. Their nominal unit cubes still have distinct interiors.

At the end there are $J=k^4$ distinct assigned cubes, $k=2^{\lfloor\log_2 L\rfloor}$, $J>V/16$. Each assigned plaquette belongs to its cube. In four dimensions a specified plaquette belongs to at most four unit four-cubes, two choices in each transverse coordinate. Hence its exponent in the product of all copied factors is at most $\beta D_p/2$. Iterating the reflection inequality gives
$$
 (\mathbb E_{\beta,L} e^{Y_p/8})^J\le Z(\beta/2)/Z(\beta).
$$
An exact dissemination theorem for an entire non-dyadic chessboard is unnecessary. This strengthens the constant in the earlier partial-block argument for this even geometry. [C4’s moment argument](../../../central-quotients/tangent-curvature/moments.md) · [Checks on closed periodic blocks](controls.py)

## A pressure bound with the volume limit first

Gauge-fix a spanning tree. Integrating tree links from the root sends all tree variables to identity and leaves independent normalized Haar variables on $4V-(V-1)=3V+1$ edges for any gauge-invariant integrand. Restrict those free edges to angles at most $\beta^{-1/2}$, with $\beta\ge2$. The probability of a single restriction is at least $c\beta^{-3/2}$, $c=8/(3\pi^3)$, by the SU(2) angle density $2\sin^2\theta/\pi$ and $\sin\theta\ge2\theta/\pi$ on this range. Every plaquette then has angle at most $4\beta^{-1/2}$ by the bi-invariant distance. Its deficit is at most $8/\beta$, using $1-\cos u\le u^2/2$. There are $6V$ faces. Consequently $Z(\beta)\ge e^{-48V}(c\beta^{-3/2})^{3V+1}$.

For the upper bound, fix the temporal forest containing the $L-1$ successive nonseam temporal links at each spatial site. Discard every action penalty except the temporal plaquettes with anchors $0,\ldots,L-2$. Their spatial-link integrations are $3L^3$ open chains. An end-link Haar integral removes its last step with scalar $z(s)=\int e^{-s(1-\operatorname{Re}U)}dU$, independently of the preceding link. The seam variables are free. Thus $Z(\beta/2)\le z(\beta/2)^{3(V-L^3)}$. Using $1-\cos\theta\ge2\theta^2/\pi^2$, $\sin^2\theta\le\theta^2$ and extending the Gaussian integral to infinity gives $z(\beta/2)\le C\beta^{-3/2}$ with $C=\pi^{5/2}/2$.

Combining the two finite bounds gives
$$
 \frac1V\log\frac{Z(\beta/2)}{Z(\beta)}
 \le 48+(3-3/L)\log C-(3+1/V)\log c+
       \left(\frac{9}{2L}+\frac{3}{2V}\right)\log\beta .
$$
At **fixed** $\beta\ge2$, every subsequential local weak limit of even $L^4$ tori therefore satisfies
$$
 \mathbb E_\beta e^{Y_p/8}\le e^{16K},\qquad
 \Pr_\beta(Y_p>u)\le e^{16K-u/8},\qquad K=48+3\log(C/c).
$$
Indeed $e^{Y_p/8}$ is a bounded continuous cylinder at that fixed $\beta$, and the log partition ratio is nonnegative. The resulting constant is independent of $\beta$ and of the state selection. The finite-box estimate also gives a uniform moment along joint sequences with bounded $(\log\beta)/L$, with a constant depending on that bound. It supplies the displayed limiting constant for $(\log\beta)/L\to0$. The constant is large, so this establishes integrability without giving a useful estimate of a small experimental tail probability. Chatterjee’s leading free-energy result treats $U(N)$ in a different scope. The finite SU(2) inequalities used here were obtained directly. [Chatterjee’s paper](https://arxiv.org/abs/1602.01222)

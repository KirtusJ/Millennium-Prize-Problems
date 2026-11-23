# A finite Hodge inverse for a growing magnetic block

Let $R\ge1$ be an integer. On $\mathbb Z$ let $a_R=R^{-1}1_{\{0,\ldots,R-1\}}$ and on $\mathbb Z^3$ let $b_R$ be the tensor product of three copies of the fourfold convolution $a_R^{*4}$. With $\tau$ a unit translation in direction 3, use the scalar spatial stencil
$$
 g_R=R^2(\tau^R-I)^3b_R.
$$
Place it on positively oriented $12$ faces at a single time. In the estimates $g$ is the sum of up to two such stencils at arbitrary times, times fixed color vectors of total norm $Y$. The same bounds cover coincident times. Translations in time do not affect $w(x)=1+|\mathbf x|_1$.

The support has spatial radius at most $C R$. We have $\|g\|_1\le8YR^2$, $\|g\|_\infty\le8Y/R$. One spatial difference costs $C/R$ in each of these bounds, since $\|\nabla a_R\|_1=2/R$ and another undifferentiated copy of $a_R$ remains in the convolution for the supremum bound. Write $g=\nabla_3^3 v_R$. The primitive uses $(\sum_{l=0}^{R-1}\tau^l)^3$ in place of $(\tau^R-I)^3$ and has $\|v_R\|_1\le YR^5$, $\|v_R\|_\infty\le YR^2$ and support of spatial radius $O(R)$. All statements allow the fixed shifts in the oriented coboundary and adjoint.

Use the scalar cubical Hodge Laplacian $\Delta=dd^*+d^*d=8I-\sum_{|e|=1}\tau_e$ componentwise on $\mathbb Z^4$. Set $K=I-\Delta/16$ and $S_M=16^{-1}\sum_{\ell=0}^{M-1}K^\ell$. Define $h=d^*S_Mg$, $k=dS_Mg$, $u=dh$ and $b=K^Mg$. The identity $g=u+d^*k+b$ is exact at each finite $M$. If $P$ projects in $\ell^2$ onto the closed exact two-cochains then $u=P(g-b)$. Because $g$ has orientation $12$, $d^*g$ uses only spatial first differences and has components only in edge directions 1, 2. The scalar walk commutes with these differences, so $h$ has no time-edge component. The three-cochain $k$ can involve a time derivative. Its early-time bound below puts that derivative on the walk. [C4’s polynomial inverse](../../central-quotients/tangent-curvature/periodic-limit/rate/heat.md)

For $a$ successive forward or backward coordinate differences, with repetitions, let $L_\ell=1+\ell$. The walk has
$$
 \|\nabla^a K^\ell\delta_0\|_1\le C_a L_\ell^{-a/2},\qquad
 \||x|_1\nabla^a K^\ell\delta_0\|_1\le C_a L_\ell^{(1-a)/2}.
$$
Here the displacement can include all four coordinates. In one step choose a coordinate uniformly, then move by $-1,0,1$ with probabilities $1/4,1/2,1/4$. Conditional on the four update counts the coordinate kernels factor. In a coordinate with $N$ updates the mass is $p_N(j)=4^{-N}\binom{2N}{N+j}$. Its first difference has norm $2p_N(0)$ by unimodality. Its absolute first moment is exactly one, even at $N=0$, by summing $|j|\,|p_N(j)-p_N(j-1)|$ separately on the two monotone halves. The other three coordinates have conditional mean absolute displacement at most $\sqrt{\ell}$. The expected $2p_N(0)$ is $O(L_\ell^{-1/2})$ by the central binomial estimate and the binomial count tail at $\ell/8$ (Chebyshev suffices). For higher differences split the walk into $a$ independent blocks, distribute the differences one per block, and apply Young’s inequality. Subadditivity of displacement puts the weight on each block once. This proof also covers backward differences and finitely short blocks with adjusted $C_a$. [Lawler and Limic, lattice walk estimates](https://www.math.uchicago.edu/~lawler/srwbook.pdf) · [C4’s proof](../../central-quotients/tangent-curvature/periodic-limit/rate/heat.md)

## Estimates across the block scale

Suppress the common color amplitude $Y$ and the factor $1/16$. For $0\le\ell\le R^2$ set $q=d^*g$. It has $\|q\|_1=O(R)$, $\|q\|_\infty=O(R^{-2})$ and spatial support $O(R)$. The terms in $h,u,k$ are $K^\ell q,dK^\ell q,dK^\ell g$ respectively. A weighted convolution bound for a compact spatial source adds its radius times the unweighted kernel norm to the first-moment kernel norm. Before summing in $\ell$ this gives

| Quantity | Bound per early heat step |
| --- | --- |
| $\|K^\ell q\|_{1,w}$ | $C R(R+\sqrt{L_\ell})$ |
| $\|K^\ell q\|_\infty$ | $C R^{-2}$ |
| $\|dK^\ell q\|_{1,w}$ | $C R(1+R L_\ell^{-1/2})$ |
| $\|dK^\ell q\|_\infty$ | $C R^{-2}L_\ell^{-1/2}$ |
| $\|dK^\ell g\|_{1,w}$ | $C R^2(1+R L_\ell^{-1/2})$ |

For $\ell>R^2$ place the three additional primitive differences on the walk. For $h,k$ the kernel order is four. Their weighted bound at each step is $C R^5(L_\ell^{-3/2}+R L_\ell^{-2})$ and $\|h_\ell\|_\infty\le C R^2 L_\ell^{-2}$. For $u$ the order is five, giving $C R^5(L_\ell^{-2}+R L_\ell^{-5/2})$ weighted and $C R^2 L_\ell^{-5/2}$ in supremum norm. Summing the early and late bounds gives, uniformly in $M$, the two time labels and the state,
$$
 \|h\|_{1,w}+\|k\|_{1,w}\le C YR^4,\qquad \|h\|_\infty\le C Y,\qquad
 \|u\|_{1,w}\le C YR^3,\qquad \|u\|_\infty\le C Y/R.
$$
The remainder satisfies $\|b\|_1\le C YR^5(1+M)^{-3/2}$. In using the heat estimates for translated stencils, the weight on an originally localized source is always its **spatial** radius, including when the source occupies two different time slices.

With the spatial Haar estimate, approximate closedness and $|e^{ia}-e^{ib}|\le|a-b|$, compare $F(g)$ first with $F(u)$. The closure costs at most $C YR^4/\sqrt\beta$ and the remaining tail costs $C\|b\|_1$. The characteristic function for $F(u)$ differs from $e^{-\|u\|_2^2/2}$ by at most $C(YR^4+Y^2R^3)/\sqrt\beta$. At each **fixed** $\beta,R$ let $M\to\infty$ in this bound. Since $\|b\|_2\le\|b\|_1\to0$, we have $u\to Pg$ in $\ell^2$. The result is
$$
 \left|\mathbb E_\mu e^{iF(g)}-e^{-\|Pg\|_2^2/2}\right|
 \le C(Y+Y^2)R^4/\sqrt\beta .
$$
All uses of differentiation in the Wilson law involved finite cochains. Every bound is uniform over the time labels before taking the scalar limit. [Spatial Haar estimate](wilson.md)

# Which contributions can survive increasing the separations?

There is a bulk statement about changing the local action even before a limit for the full non-Abelian coefficient is known. Take a compact connected simple group of dimension $s$. Fix the metric so that the common leading plaquette action in exponential coordinates is $\lVert X\rVert^2/2$. Compare two real inversion-invariant analytic class actions with this Hessian and their unique minimum zero at the identity. Use each action's own plaquette density for both its Boltzmann weight and the source insertion. Let $Q_4(X)$ be the degree-four Taylor term of the new action minus the old, and $q=\mathbb E Q_4(Z)$ for a standard $s$-component Gaussian.

On each fixed open box or relative dual box all terms from the common quadratic action, the Lie bracket, the Haar chart and the square of the cubic face term agree at first order. Inversion invariance removes an intrinsic cubic Taylor term. Inserting the linear curvature into $Q_4$ suffices at this order even though the original plaquette uses a noncommutative word. By homogeneity its expectation is $q v_p^2$, with $v_p=(B(B^\top W B)^{-1}B^\top)_{pp}$. Thus the exact change in the logarithmic $1/\beta$ coefficient is $-q\sum_p w_pv_p^2$. With $s$ independent compact circles the Wilson coefficient itself is $(s/8)\sum_p w_pv_p^2$. At leading order the two pair covariances agree and the paired triangle vanishes. Consequently its normalized first coefficient changes by $-8q/s$ times the paired $s$-circle coefficient. For $D+\lambda D^2$ one has $q=\lambda s(s+2)/4$. For $SU(2)$ the factor is $-10\lambda$. On the short open/relative pair, for example, adding $D^2/10$ changes $R_1$ from 0.221805 to 0.171333. [Exact local and diagram checks](check_boxes.py)

## A finite local formula

Write $k=s/8$, $K(w)=B(B^\top W B)^{-1}B^\top$, and $P=K(1)$. At reciprocal weights the dual diagonal covariance is $w_p(1-w_p v_p)$. Subtract the dual circle coefficient at reciprocal weights from the primal coefficient. After division by $k$, the difference is
$$
 2\operatorname{rank} B-\sum_p w_p+
 \sum_p w_p(w_p-1)\{2v_p-(w_p+1)v_p^2\}.
$$
This uses $\sum_p w_pv_p=\operatorname{rank} B$. Differentiate in three disjoint masks $f,g,h$ at $w=1$. Only marked faces survive. Because the dual source is reciprocal and the three-insertion cumulant carries a minus, the paired first triangle is $-k/2$ times the mixed derivative of the displayed expression. Put
$$
 a_g(p)=\sum_j g_jP_{pj}^2,\qquad
 b_{gh}(p)=\sum_{j,l}g_jh_l P_{pj}P_{jl}P_{lp}.
$$
At unit weights the first derivative of $v_p$ is $-a_g(p)$ and its mixed derivative is $2b_{gh}(p)$. The full finite circle answer is
$$
 \bar T^1_{\rm circ}=2k\sum_{\rm cyc}\sum_p f_p
 \{a_g(p)a_h(p)-(1-2P_{pp})b_{gh}(p)\}.
$$
In particular the entire difference between two group actions above depends on curvature covariances on the three finite supports. This identity removes sums over the rest of the lattice before increasing the volume. On a twist with separate color covariances use the formula for each color with $k=1/8$. For the squared $SU(2)$ deficit the quartic Wick form in three diagonal variances is $B(v,v)$ where $B(x,y)=((\sum x)(\sum y)+2x\cdot y)/4$. Polarizing the same calculation gives the exact paired shift per unit $\lambda$ as $2\sum_{\rm cyc,p} f_p[B(\mathbf1-2v,b_{gh})-B(a_g,a_h)]$ with all entries now color vectors. The independent sourced-Hessian and marked-face calculations agree. [Twisted action-change control](check_action.py)

## The four-dimensional limit of the difference

At fixed supports in the infinite lattice, the finite projection entries converge by the exhaustion argument. Translation invariance and cubic symmetry give $P_{pp}=1/2$: three of the six curvature components at almost every momentum belong to the exact subspace. The term involving the local triangle consequently disappears. For nonnegative masks the remaining paired first circle coefficient is nonnegative. It is $s/4$ times $\sum_{\rm cyc,p} f_p a_g(p)a_h(p)$. Local changes of the action therefore have a well-defined coefficient-wise bulk effect even if the separate interacting diagram sums have no known limit.

For a complete cube at each of three sites, let $r_{ij}$ denote their center distances in lattice units, $r_*=\min r_{ij}$. For large $r_*$ the normalized circle coefficient is
$$
 R^1_{\rm circ}=\frac{1+O(1/r_*)}{\sqrt{12s}\,\pi^2}
       \sum_{\rm cyc}\frac{r_{jk}^{4}}{r_{ij}^{4}r_{ik}^{4}} .
$$
In particular it is $O(r_*^{-4})$, including squeezed triangles: the triangle inequality bounds the longest side by twice the next longest. The group-action difference is $-8q/s$ times this expression. For three circles and a single close pair of length $r$ at distance $R\gg r$ from the third, the leading coefficient becomes $1/(3\pi^2r^4)$ as $r\to\infty$, $r/R\to0$.

For the normalization, the lattice curvature block at separation $x$ has leading matrix $\bigwedge^2(I-2\hat x\hat x^\top)/(\pi^2|x|^4)$ in the positively oriented two-plane basis. It comes from two differences of the massless scalar propagator $1/(4\pi^2|x|^2)$. The leading matrix is orthogonal after removing its radial factor. The staggered offsets and forward differences give a uniform absolute remainder $O(|x|^{-5})$. For example, subtract the leading homogeneous symbol near zero in the exact Fourier projector. On a dyadic annulus of radius $u$ the remaining multiplier and its $m$th derivatives are $O(u^{1-m})$. Rescaled integration by parts and summation of the annuli give that remainder, while the smooth high-frequency part is rapidly decreasing. This is the standard lattice Green-function expansion at the order needed here. [Lüscher and Weisz, coordinate-space lattice propagator](https://arxiv.org/abs/hep-lat/9502017)

For each fixed face in one cube, the sum of squared covariances to a second complete cube is $4/(\pi^4 r_{ij}^8)(1+O(1/r_{ij}))$, since every column orientation occurs four times. Hence $V^0_{ij}=48s/(\pi^4r_{ij}^8)(1+O(1/r_{ij}))$. There are 24 marked faces in each outer sum. This gives $96s/\pi^8$ times the sum of the three products $r_{ij}^{-8}r_{ik}^{-8}$ in the numerator, yielding the result. The relative error in each positive leading term is uniform in orientation. A heat-kernel quadrature tests collinear, skew and squeezed triangles. At shortest scale 32 the measured coefficients for the three specified shapes are within one percent of their asymptotic values. [Lattice computation](check_bulk.py) · [Recorded output](evidence/checks.txt)

The limiting operation here first extracts the fixed-volume inverse-coupling coefficient, then takes the volume to infinity at fixed supports, then increases the separations. The estimate controls the *difference* produced by the allowed one-plaquette action changes. It does not interchange these limits with a nonperturbative continuum trajectory or address arbitrary extended-loop actions. Marginal non-Abelian terms, the renormalized interaction and the mass scale still require analysis.

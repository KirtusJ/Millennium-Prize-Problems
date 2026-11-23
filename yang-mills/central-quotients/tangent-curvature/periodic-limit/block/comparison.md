# A spatial block with an order-one magnetic variance

Take the four-dimensional isotropic $SU(2)$ Wilson states obtained by sending even periodic four-cubes to infinity at each fixed $\beta\ge2$. Write $b_R(k)=R^{-1}\mathbf 1_{\{0,\ldots,R-1\}}(k)$ for integer $R\ge1$. Put
$$
 f_R=(b_R^{*6})^{\otimes3},\qquad
 g_R=R^5\nabla_3^3 f_R,\qquad
 \nabla_i f(x)=f(x)-f(x-e_i).
$$
Place $g_R$ on positive spatial $12$ faces of one time slice. Its support has diameter $O(R)$. The identity $\nabla b_R=(\delta_0-\delta_R)/R$ gives an equivalent implementation as four signed block averages, with coefficients $R^2(1,-3,3,-1)$, spaced $R$ cells apart along direction 3. The smoothing in that direction in this implementation uses the three remaining boxes.

In the slice at time $t$, parallel transport each plaquette to its spatial origin along the coordinate-ordered spatial path. Let $X_R(t)$ be $\sqrt\beta$ times the $g_R$-weighted sum of the imaginary parts of these transported plaquettes. Its components transform by a common adjoint rotation, so $O_R(t)=\exp(-s|X_R(t)|^2)$ is a bounded, gauge-invariant one-slice observable for each fixed $s>0$. Below, a rooted color vector means that this whole sum has also been transported along the straight time axis into the initial frame. This preserves $O_R(t)$ exactly. Nonlocal field-strength correlators with connecting parallel transporters are standard in gauge theory. Here we specify the paths, signs, normalization and observable explicitly. [Di Giacomo et al., *Field correlators in QCD*](https://arxiv.org/abs/hep-ph/0007223)

For any finite sum of translated time slices with color Fourier arguments $y_i$, write $g$ for the associated colored face test and $Y=\sum_i |y_i|$. Our comparison is
$$
 \left|\mathbb E_{\beta,\mu}e^{iF(g)}
          -\exp[-\|Pg\|_2^2/2]\right|
 \le C (Y+Y^2)\,R^4/\sqrt\beta . \tag{1}
$$
Here $P$ is the $\ell^2$ projection onto the closure of compact exact lattice two-forms. The constant is independent of the time labels, $R,\beta$ and the selected periodic state $\mu$. The proof uses only the uniform first moment of the scaled face action. [Pressure estimate](../pressure.md) · [Rooted link variation and cube identity](../rate/ward.md)

## Sum the path contributions before taking norms

Use time-first paths from the common origin and spatial weight $w(t,\mathbf x)=1+|\mathbf x|_1$. For any finite **spatial** one-cochain $h$ (zero time component) and arbitrary finite colored face test $v$, the finite-coupling Haar identity gives
$$
 \left|\mathbb E\big[F(dh)e^{iF(v)}\big]
       -i\langle dh,v\rangle\,\mathbb E e^{iF(v)}\right|
 \le \frac{C}{\sqrt\beta}
       \left(\|h\|_{1,w}+\|h\|_\infty\|v\|_{1,w}\right). \tag{2}
$$
The original-link single-edge proof splits the action score from the derivative of the test. For each edge $e$ its score error is at most $Cw(e)|h_e|/\sqrt\beta$ in $L^1$. Summing gives the first term. There are two derivative errors for a face $p$ based at $z$. Direct insertions occur only on its four edges, each with error at most $Cw(z)|h_e|/\sqrt\beta$. Differentiating the frame $R_z$ gives an additional commutator for each occurrence of a varied edge in the path. Its $L^1$ cost is at most $C|h_e|/\sqrt\beta$, since $\sup_p\|F_p\|_2\le C$. There are exactly $|\mathbf z|_1$ spatial steps in this path regardless of its time coordinate. After multiplying each error by $|v_p|$, the sum over edges on the path is bounded by $\|h\|_\infty|\mathbf z|_1$. The direct and frame derivatives together give the second term in (2). The generator route avoiding the edge is chosen separately in each original Haar identity. The differentiation of the observable still uses its actual ordered paths. [Signed insertions and root derivatives](../rate/ward.md#quantitative-haar-variation-including-the-paths) · [Finite-$N$ Haar integration by parts](https://arxiv.org/abs/2309.07399)

## Estimates for a block of radius $R$

Use the lazy kernel $K=I-(dd^*+d^*d)/16$ on four-dimensional cochains and $S_M=16^{-1}\sum_{\ell<M}K^\ell$. Exactly,
$$
 g=u+d^*k+b,\qquad h=d^*S_Mg,\quad u=dh,\quad k=dS_Mg,\quad b=K^M g .
$$
All are finite for finite $M$. Since $K$ acts componentwise and the original form has orientation $12$, $h$ has only spatial components. This is what permits (2) at all separations. The walk bounds used below, for $a$ forward or backward differences in any coordinates, are $\|\nabla^a K^\ell\delta\|_1\le C_a(1+\ell)^{-a/2}$ and $\||x|_1\nabla^a K^\ell\delta\|_1\le C_a(1+\ell)^{(1-a)/2}$. They follow by splitting the lazy walk into independent blocks and differentiating the one-dimensional binomial distributions. [Derivation](../rate/heat.md#walk-estimates)

For a single slice, $\|f_R\|_1=1$, $\|f_R\|_\infty\le R^{-3}$. For $a\le4$ spatial differences, move each difference onto a separate box factor in its direction. Its signed norm is $2/R$ and at least one untouched box per axis remains. Consequently $\|\nabla^a f_R\|_1\le (2/R)^a$ and $\|\nabla^a f_R\|_\infty\le R^{-3}(2/R)^a$. The support gives $\|f_R\|_{1,w}\le CR$ and the same extra factor $CR$ in the signed norm estimates. In particular
$$
 \|g\|_1\le CYR^2,\quad \|g\|_{1,w}\le CYR^3,\quad
 \|d^*g\|_1\le CYR,\quad \|d^*g\|_{1,w}\le CYR^2,\quad
 \|d^*g\|_\infty\le CY R^{-2}.
$$
The weighted norm is spatial, so the same bounds apply to sums of time slices as written.

With constants uniform in $M$,
$$
 \|h\|_{1,w}+\|k\|_{1,w}\le CY R^4,\qquad
 \|u\|_{1,w}\le CY R^3,\qquad \|h\|_\infty\le CY. \tag{3}
$$
Here are the sums for (3). Write $L=1+\ell$ and temporarily suppress $CY$. For $L\le R^2$, a first derivative on $K^\ell$ costs $L^{-1/2}$ in ordinary norm and $O(1)$ with one displacement weight. Convolving against $g$ thus costs at most $R^3 L^{-1/2}+R^2$ per step for either $h$ or $k$. For $u=dS_M d^*g$ the corresponding cost is $R^2 L^{-1/2}+R$ because the first derivative was spatial and fell on the block. Summing gives $O(R^4)$ and $O(R^3)$. The early $\ell^\infty$ bound for $h$ is $O(1)$ by contraction acting on $d^*g$.

For $L>R^2$, put all three differences in $g_R$ onto the walk. The weighted costs for $h,k$ are bounded by $R^5(R L^{-2}+L^{-3/2})$ per step, and for $u$ by $R^5(RL^{-5/2}+L^{-2})$. These sum to the same $O(R^4)$ and $O(R^3)$. This assigns the weight either to the undifferentiated block or to the differentiated walk using $w(x+y)\le w(x)+|y|_1$. For the supremum bound, the late convolution of the four-difference kernel against the undifferentiated block costs $R^5L^{-2}R^{-3}$ per step. Summing gives $O(1)$. Finite shifts from adjoints only affect the constants.

Finally $\|b\|_1\le CYR^5(1+M)^{-3/2}$. Closure of the original six-face cube bounds $\mathbb E|F(d^*k)|\le C\|k\|_{1,w}/\sqrt\beta$, and the face first moment gives $\mathbb E|F(b)|\le C\|b\|_1$. Apply (2) with $v=\tau u$, $0\le\tau\le1$, and integrate the characteristic function of $F(u)$. The scalar ODE has integrating kernel $\exp[-(1-\tau^2)\|u\|_2^2/2]\le1$. Its error is at most $C(\|h\|_{1,w}+\|h\|_\infty\|u\|_{1,w})/\sqrt\beta$. As $u=P(g-b)$, the change of Gaussian variance tends to zero when $M\to\infty$ at fixed $R$ and fixed finite list of time labels. Taking this limit *after* estimating the finite-support identities proves (1). [Six-face bound](../rate/ward.md#approximate-closedness-with-one-spatial-weight)

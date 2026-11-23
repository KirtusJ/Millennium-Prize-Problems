# A finite-support inverse for the lattice Hodge Laplacian

Translate the forward difference of order $j\ge1$ of a single $12$-face in spatial direction 3 along the time axis. We need a real colored test $g$ that is the sum of at most two such translated stencils, with color vectors $y_1,y_2$. Put $Y=|y_1|+|y_2|$. All constants below may depend on $j$. The lattice inner product sums over positively oriented cells, with the cubical differential $d$ and its adjoint $d^*$. As follows by the exterior and contraction symbols, $\Delta=dd^*+d^*d$ acts on each component as $8I-\sum_{|e|=1}\tau_e$. [Projection formula](../../gaussian.md)

Let $K=I-\Delta/16$ and $S_M=16^{-1}\sum_{\ell=0}^{M-1}K^\ell$ for integer $M\ge1$. The kernel of $K$ stays put with probability $1/2$ and moves to each of the eight neighbors with probability $1/16$. The identity $\Delta S_M=I-K^M$ gives an *exact* finite decomposition
$$
 g=u+d^*k+b,\qquad h=d^*S_Mg,\quad u=dh,\quad k=dS_Mg,\quad b=K^Mg .
$$
Write $P$ for projection onto the closed subspace of exact two-cochains in $\ell^2$. Then $u=P(g-b)$ since $P$ kills $d^*k$. In particular $\|u\|_2\le 2\|g\|_2$, since $K$ is a contraction. The approximation to $F(g)$ will use $\|b\|_1$, not an assumption that $F$ is square-summable on the whole lattice.

## Walk estimates

For any product of $a\ge1$ coordinate differences, forward or backward and with repetitions allowed, the scalar walk satisfies
$$
 \|\nabla^a K^\ell\delta_0\|_1\le C_a(1+\ell)^{-a/2},\qquad
 \||x|_1\nabla^a K^\ell\delta_0\|_1\le C_a(1+\ell)^{(1-a)/2}. \tag{1}
$$
Here $|x|_1$ includes all four coordinates. A derivation gives both bounds with no local limit theorem. For each step choose one coordinate uniformly and then add $-1,0,1$ in it with probabilities $1/4,1/2,1/4$. Conditioned on the coordinate counts, the law factors. After $N$ updates in one coordinate its distribution is $p_N(v)=4^{-N}\binom{2N}{N+v}$. Symmetry and unimodality give $\sum_v|p_N(v)-p_N(v-1)|=2p_N(0)\le C/\sqrt{1+N}$ by the central binomial bound. Summing by parts on the increasing and decreasing halves gives $\sum_v |v|\,|p_N(v)-p_N(v-1)|\le C$ independently of $N$. Indeed each half telescopes to a half-mass plus at most one central term. Every other coordinate has conditional expected absolute displacement at most $\sqrt{\ell}$. The count in the differentiated coordinate has binomial law with mean $\ell/4$. Splitting at $\ell/8$ and using Chebyshev gives $\mathbb E(1+N)^{-1/2}\le C(1+\ell)^{-1/2}$. This proves (1) for one difference, in both directions.

For $a$ differences split $\ell$ steps among $a$ independent blocks with lengths differing by at most one. Differentiate one block in each coordinate requested and convolve them. Young's inequality gives the first bound. The triangle inequality $|\sum x_i|_1\le\sum_i |x_i|_1$ places the weight on one block at a time and gives the second. Small $\ell<a$ are included by increasing $C_a$. This argument uses the usual lazy lattice walk; the weighted finite-difference estimate is derived here. [Lawler and Limic, *Random Walk: A Modern Introduction*, chapter 2](https://www.cambridge.org/core/books/abs/random-walk-a-modern-introduction/local-central-limit-theorem/2D2908A7742FFBEF09AFDA3E1F314582)

## Cochain bounds and the characteristic function

Use $w(x)=1+|\mathbf x|_1$, the **spatial** weight in the [Wilson estimates](ward.md). Translating either stencil by any time leaves its weighted bounds unchanged. The finite orientation sums in $d,d^*$ add one difference per derivative. Fixed shifts from a backward difference only change the constants. Applying (1) with $a=j,j+1,j+2$, respectively, gives
$$
 \begin{aligned}
 \|b\|_1 &\le C_j Y(1+M)^{-j/2},\\
 \|h\|_{1,w}+\|k\|_{1,w} &\le C_j Y\,A_j(M),\qquad
 A_j(M)=\sum_{\ell=0}^{M-1}(1+\ell)^{-j/2},\\
 \|u\|_1 &\le C_jY\sum_{\ell\ge0}(1+\ell)^{-(j+2)/2}\le C'_j Y .
 \end{aligned}
$$
For each finite $M$ all original-link variations have finite support. Since $\sup_p\mathbb E |F_p|\le C$, we have $\mathbb E|F(b)|\le C\|b\|_1$. From (2) and (3) of the Wilson estimates and the Lipschitz bound on the complex exponential, it follows that
$$
 \left|\mathbb E e^{iF(g)}-\exp[-\|Pg\|_2^2/2]\right|
 \le C_j(1+Y)^2
       \left[(1+M)^{-j/2}+\frac{A_j(M)}{\sqrt\beta}\right]. \tag{2}
$$
Indeed closure controls $F(d^*k)$ and Haar differentiation controls $F(u)$. Changing the Gaussian variance from $\|u\|_2^2$ to $\|Pg\|_2^2$ costs at most $(\|u\|_2+\|Pg\|_2)\|b\|_2/2\le C_jY\|b\|_1$. All estimates are uniform in the two time labels and in the chosen periodic state.

For $j=1,2$ choose $M=\lceil\sqrt\beta\rceil$. For $j\ge3$ the sum $A_j(\infty)$ is finite, so take the infimum of the right side over $M$ at each fixed $\beta$. This gives the three errors
$$
 \delta_1=\beta^{-1/4},\qquad
 \delta_2=\log(2+\beta)\,\beta^{-1/2},\qquad
 \delta_j=\beta^{-1/2}\quad(j\ge3).
$$
No derivative of an infinite-support Wilson observable has been taken.

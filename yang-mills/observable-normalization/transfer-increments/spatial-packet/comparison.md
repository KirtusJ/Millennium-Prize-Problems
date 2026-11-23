# Comparing the packet in Wilson and Gaussian states

Use the ordered rooted frame on $\mathbb Z^4$ which follows time first and then the three spatial axes. Denote its path to the base of face $p$ by $\gamma_p$, and its real three-color scaled curvature again by $F_p$. Under conjugation by the time-axis segment, the spatial packet in the [main proof](README.md) becomes the corresponding sum of these rooted curvatures. Its squared norm is unchanged.

Let $g$ be either one packet test or the sum of packets at times $0,n$ with arbitrary colors $y_0,y_1$. Write $Y=|y_0|+|y_1|$ and $w(x)=1+|\mathbf x|_1$. Then $\|g\|_1\le C YR^2$, $\|g\|_\infty\le CY/R$, and the rooted paths in its support have length at most $n+CR$. Indeed the unshifted tent has mass $R^2$, height $1/R$, and support in a cube of side $2R$. The third difference costs at most eight times either norm. All spatial roots and paths below use the same frame.

## Keep the actual paths in the variation

For finitely supported colored one-cochains $h$ and face tests $v$, the original-link Haar variation gives
$$
 \left|\mathbb E[F(dh)e^{iF(v)}]-i\langle dh,v\rangle\mathbb E e^{iF(v)}\right|
 \le \frac{C}{\sqrt\beta}\left[
   \|h\|_{1,w}(1+\|v\|_\infty)
   +\sum_p |v_p|\sum_{e\in\gamma_p}|h_e|
 \right]. \tag{2}
$$
Edges in each path are counted with traversal multiplicity and either orientation. Here $\|h\|_{1,w}=\sum_e w(e)|h_e|$. To verify (2), use C4's avoiding path for the Haar generator on one edge $e$. Its six-face action score differs from $F(dh)$ in mean absolute value by at most $Cw(e)|h_e|/\sqrt\beta$, independently of $v$. For a directly incident face, the derivative of the scaled curvature differs from the signed color insertion by at most the same quantity in mean norm. Summing with the test coefficients costs at most six times $\|v\|_\infty$ per edge. The derivative of the conjugating path is present only when the path traverses $e$. Its commutator has norm at most $2|h_e||F_p|/\sqrt\beta$ per traversal. The uniform first scaled-action moment bounds $\mathbb E|F_p|$ independently of the face. Summing these three estimates proves (2), with modulus-one phase. Each variation may first be performed on the original compact links, then passed to the selected state at fixed parameters. [Individual derivative estimates and backward-edge convention](../../../central-quotients/tangent-curvature/periodic-limit/rate/ward.md) · [Finite-$N$ lattice integration by parts](https://arxiv.org/abs/2309.07399)

## The truncated lattice inverse

Write $K=I-\Delta/16$ for the four-dimensional lazy walk and $S_M=\sum_{l=0}^{M-1} K^l/16$. Use
$$
 h=d^*S_Mg,\quad k=dS_Mg,\quad u=dh,\quad b_M=K^Mg,\qquad
 g=u+d^*k+b_M,\qquad u=P(g-b_M),
$$
where $P$ projects in $\ell^2$ onto the closure of compact exact two-cochains. The orientation shifts in $d$ and $d^*$ have bounded length. Uniformly in the truncation and time labels,
$$
 \|h\|_{1,w}+\|k\|_{1,w}\le C YR^4,\qquad
 \|h\|_\infty\le CY,\qquad
 \|b_M\|_1\le CYR^5(1+M)^{-3/2}. \tag{3}
$$
All these estimates also hold for coinciding time labels.

Here are the summations. Use the four-dimensional walk difference bounds $\|\nabla^a K^l\delta\|_1\le C_a(1+l)^{-a/2}$ and $\||x|_1\nabla^a K^l\delta\|_1\le C_a(1+l)^{(1-a)/2}$. The weighted convolution against our test uses only spatial positions in $w$. Moving either source in time therefore incurs zero translation cost in this weight. [Walk proof and Hodge telescope](../../../central-quotients/tangent-curvature/periodic-limit/rate/heat.md)

* For $0\le l<R^2$, use one walk difference and the unexpanded packet. Its spatial support lies within $CR$ of the axis. The weighted $\ell^1$ cost of that term is at most $CYR^2[1+R(1+l)^{-1/2}]$ by the triangle inequality for the spatial displacement. Its $\ell^\infty$ cost is at most $(CY/R)(1+l)^{-1/2}$. The sums are $O(YR^4)$ and $O(Y)$.
* For $l\ge R^2$, expand each long difference using $I-\tau_{R e_3}=(I-\tau_{e_3})\sum_{j=0}^{R-1}\tau_{j e_3}$. Before taking the resulting three unit differences the translated tent sum has mass norm at most $CYR^5$, sup norm at most $CYR^2$, and spatial support still within $CR$. Four walk differences therefore give a weighted term at most $CYR^5[(1+l)^{-3/2}+R(1+l)^{-2}]$, and a sup term at most $CYR^2(1+l)^{-2}$. From $R^2$ onward the two scalar sums are at most $2/R$ and $1/R^2$ by integral comparison. This proves the uniform bounds on $h,k$. Three differences without the extra derivative give the stated $b_M$ bound at every $M$.

## Interpolate the original test

For $0\le z\le1$, put $\phi(z)=\mathbb E e^{izF(g)}$. For each finite $R,n,M$ all random variables in this interpolation are integrable. Decompose $F(g)$ in $\phi'=i\mathbb E F(g)e^{izF(g)}$. Approximate closedness gives $\mathbb E|F(d^*k)|\le C\|k\|_{1,w}/\sqrt\beta$, while $\mathbb E|F(b_M)|\le C\|b_M\|_1$. Apply (2) to $F(u)$ with $v=zg$. In particular the path charges are those of $g$, whose support is explicit. Their sum is at most $\|h\|_\infty\|g\|_1(n+CR)\le C_A Y^2 R^3$ for $n\le AR$. The direct-face charge costs at most $C Y^2 R^3$. The action and closedness terms cost at most $C Y R^4$.

The drift coefficient $\langle u,g\rangle$ differs from $\|Pg\|_2^2$ by at most $\|b_M\|_2\|g\|_2$. At each fixed $R,n,y_0,y_1$, both this error and the residual $\ell^1$ error vanish as $M\to\infty$. The resulting scalar inequality is
$$
 \left|\phi'(z)+z\|Pg\|_2^2\phi(z)\right|
 \le C_A(Y+Y^2)R^4/\sqrt\beta .
$$
The integrating factor from $z$ to $1$ is $\exp[-(1-z^2)\|Pg\|_2^2/2]\le1$. With $\phi(0)=1$, this compares $\phi(1)$ to $e^{-\|Pg\|_2^2/2}$ at the same error. The proof uses only finite-support Haar variations.

Finally $e^{-|X|^2}$ is the characteristic function of a centered $N(0,2I_3)$ evaluated at $X$. Integrate the estimate against independent Gaussian test colors for the two packets and against one color for each mean. Their first and second norm moments are finite. Both observables are bounded by one, so subtracting the product of the means gives (1) in the main proof.

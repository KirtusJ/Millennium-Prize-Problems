# Reflection tiles the variance at fixed coupling

For a rectangular set $H$ of cell indices, write $S(H)=\sum_{y\in H}D(y)$ and $V(H)=\operatorname{Var}S(H)$. Each term lives on links of the closed geometric cell $y+[0,1]^4$. Suppose the rectangle has even width $h$ in direction $i$ and lower coordinate $a$ there. Concatenate $k$ translates of $H$ separated successively by $h e_i$. For two different copies numbered $l<m$, reflection about the **site** plane
$$
 x_i=a+(l+m+1)h/2
$$
exchanges their supports and sends the first sum to the negative of the second. The copies lie in opposite closed halves even when they share tangential boundary links. Wilson site reflection positivity gives $\mu[S_l S_m]\le0$. Thus the variance of the concatenation is at most $kV(H)$. Reflection positivity holds first on sufficiently large even tori for these fixed half-tests and then in the local limit. The argument also applies to a centered partial corner sum if its weights are independent of the corner bit in the direction of tiling. Reflection toggles precisely this bit and gives the same minus sign. [Wilson site reflection with boundary links](../../../../central-quotients/tangent-curvature/reflection.md)

Let $V_D(N)$ denote the variance on $B_N$. For fixed even $h$, concatenate along the four axes in turn to get $V_D(kh)\le k^4 V_D(h)$. For arbitrary $N=kh+s$, $0\le s<h$, split each coordinate interval after $kh$. A boundary rectangle has $j\le3$ long directions of width $kh$ and its other widths are at most $h$. Applying the concatenation bound in its long directions gives variance $O_{\beta,h}(k^j)$ since there are only finitely many possible base rectangles for fixed $h$. Translation invariance makes the constants independent of location. The centered $L^2$ norm of the sum of all boundary pieces is therefore $O_{\beta,h}(N^{3/2})$. The bulk norm is $O_{\beta,h}(N^2)$. It follows that
$$
 \limsup_{N\to\infty}\frac{V_D(N)}{N^4}\le \frac{V_D(h)}{h^4}
$$
for every even $h$. The liminf along even $N$ is bounded below by the infimum of these right sides. An odd $N$ differs from $N-1$ by a width-one boundary, whose centered norm is $O_\beta(N^{3/2})$ by the same estimate with two-cell tiles. The full limit exists and equals the infimum over even $h$.

For the site reading the difference of the two sums is exactly
$$
 \sum_{y,c}
 [\mathbf1_{B_N}(y+c)-\mathbf1_{B_N}(y)]\,w(y+c,\mathbf1-2c).
$$
For $N\ge2$ partition each coordinate of $y$ into $-1$, $[0,N-2]$ and $N-1$ on the support. At least one coordinate must be a boundary singleton. Inside each resulting rectangle the weight depends only on the corner bits belonging to singleton coordinates. In every other direction the partial corner sum is odd under geometric reflection with the corresponding cell shift. Subdivide each long direction into an even length and a possible final singleton. Apply the two-cell concatenation argument along the even lengths. Each piece has variance $O_\beta(N^3)$ or less, with a bounded number of pieces. This bounds the centered norm of the site-to-cell difference by $O_\beta(N^{3/2})$, giving the same variance density for $P$ and $D$.

Finally choose an even $h$ within two of $\beta^{1/40}$ and use the Gaussian surface estimate. Then
$$
 \chi_\beta\le V_D(h)/h^4
       \le C(h^{-1}+h^4\beta^{-1/8})
       \le C'\beta^{-1/40}.
$$
This proof requires no decay rate for arbitrary fixed-coupling separated Wilson correlators. The use of cube support and even widths ensures that the relevant positivity inequality is at a site plane at every stage.

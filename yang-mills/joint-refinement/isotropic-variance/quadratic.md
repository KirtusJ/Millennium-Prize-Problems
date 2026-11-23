# Exact checkerboard integration in the quadratic comparison

The quadratic Wilson comparison on every even spatial side has a uniformly bounded conditional-mean variance. It is approximately $0.22083$ at side 64. The limit is the Brillouin-zone integral of the continuous Fourier integrands below. This comparison tests both the local integration and the normalization of the spatial zero mode.

On a finite four-torus with even spatial side and temporal period at least two, use the unweighted plaquette inner product. Take three independent centered Gaussian colors. For each color let the curvature $b$ have covariance the orthogonal projection $\Pi$ onto the space of exact lattice two-forms $\operatorname{im}d$. This specifies a probability law directly on curvatures and removes the kernel of the link curl. Let $R$ restrict to all $xy$ faces on one time slice and $G=R\Pi R^*$. Varying any selected $x$-link changes the curvature in the direction $d1_e$, of squared norm six. Distinct selected directions have disjoint plaquette supports. Let $Q$ project onto their span. Since $Q\le\Pi$, the Gaussian coefficients along $Q$ are independent of the complement, the latter having covariance $\Pi-Q$. Integrate out exactly these link variations. On the measured face pair the restriction $Q_R=RQR^*$ has diagonal entries $1/6$ and off-diagonal entries $-1/6$. Each measured face belongs to one pair. This construction does not require conditioning a singular gauge-fixed link field.

With $V=N^3$ the full sum for three colors is $F=(2\sqrt V)^{-1}\sum_a\|Rb_a\|^2$. The conditional mean adds the constant trace of the deleted Gaussian covariance to the quadratic form of the retained fields. Wick's formula gives
$$
 \chi=\frac{3}{2V}\operatorname{Tr}G^2,\qquad
 \operatorname{Var}M_{\rm G}=\frac{3}{2V}\operatorname{Tr}(G-Q_R)^2 .
$$
The contraction $0\preceq G-Q_R\preceq G\preceq I$ gives bounds of $3/2$ for both. Writing $g(x)$ for the same-orientation curl covariance on the slice, the pair trace gives the closed formula
$$
 J_{\rm G}=\frac{3}{2V}\big(2\operatorname{Tr}(GQ_R)-\operatorname{Tr}Q_R^2\big)
 =\frac{g(0)-g(e_y)}2-\frac1{12}.
$$
Here $e_y$ splits the two measured faces. The $y$ component is parallel to the plaquette. Using its normal changes the prediction. In the infinite-time limit the spatial Fourier eigenvalue is $(s_x+s_y)/\sqrt{s(s+4)}$ with $s_i=4\sin^2(p_i/2)$, $s=s_x+s_y+s_z$, and zero at $p=0$. For finite time use the average of $(s_x+s_y)/(s+s_t)$ over time momentum, with zero for the zero denominator. [Quadratic equal-time covariance](../plaquette-covariance/checks.md)

| Side | $\chi$ | $J_{\rm G}$ | $\operatorname{Var}M_{\rm G}$ |
|---:|---:|---:|---:|
| 2 | 0.437500 | 0.230317 | 0.207183 |
| 6 | 0.422336 | 0.201149 | 0.221186 |
| 8 | 0.422017 | 0.201110 | 0.220907 |
| 10 | 0.421960 | 0.201105 | 0.220854 |
| 64 | 0.421935 | 0.201104 | 0.220831 |

An independent check constructs the signed link-to-plaquette incidence matrix on a finite periodic complex, projects by singular value decomposition, then computes both traces with the explicit checkerboard columns. [Incidence and Fourier calculations](quadratic.py)

The three measured interacting local terms are near $0.213$ on the short slabs. Their proximity to $0.201$ motivates comparing the remaining staple variances. To transfer a ceiling from the quadratic theory one would need, for example, a regulator-uniform bound on the **sum** of the differences of the connected staple covariances in compatible normalizations. A per-pair error that merely tends to zero need not suffice after summing over the whole slice. Compact flat holonomies and interaction contributions are absent from this Gaussian comparison.

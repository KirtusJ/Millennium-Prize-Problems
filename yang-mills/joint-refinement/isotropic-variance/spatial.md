# A one-plaquette spatial-transfer test for the infrared contribution

Let $C(x)=\operatorname{Cov}(X_0,X_x)$ at one time in the isotropic periodic-space SU(2) vacuum, and let $c_j(r)=C(r e_j)$. These are correlations of two elementary plaquettes, without spatial sums. A sufficient test for uniformly bounded $\chi=\sum_x C(x)$ uses only the three axial sequences. For any fixed longitudinal separation $r$, the matrix of covariances indexed by transverse translations is positive semidefinite. Its eigenvalues are the reflected-slab pairings of the corresponding transverse Fourier modes established in [PR #23](../plaquette-covariance/README.md). Cauchy–Schwarz for this matrix gives
$$
 |C(x)|\le c_j(|x_j|_N),\qquad |z|_N=\min(z,N-z),\quad 0\le z<N.
$$
This step uses the raw covariance of a fixed face orientation before any checkerboard integration. The diagonal entries are all $c_j$, including when a face crosses a longitudinal slab. It does not assume that every off-axis connected correlation is positive.

Choose a coordinate $j$ attaining the largest periodic distance $r$. There are at most $2(2r+1)^2$ sites assigned to any one coordinate at that radius, also at the antipode. Write $m=N/2$. Then
$$
 \chi\le C(0)+18\sum_{j=1}^3\sum_{r=1}^{m} r^2 c_j(r).
$$
In particular an axial bound $c_j(r)\le A(1+r)^{-3-\epsilon}$ with regulator-independent $A,\epsilon>0$ suffices. No assumed gap enters this criterion. It retains coordinate planes and the zero mode. With the unrounded counts, one may average ties for the largest coordinate to obtain the sharper axial upper estimate used in the [data reduction](axes.py).

### Local transfer spectral weight sufficient for the bound

There are positive measures $\nu_{j,N,\beta}$ on $[0,1]$, each of mass at most $K$, for which
$$
 c_j(r)=\int (s^{r-1}+s^{N-r-1})\,d\nu_{j,N,\beta}(s),\qquad 1\le r\le N-1 .
$$
First use a finite periodic time extent. For a straddling face the spatial transfer eigenbasis gives weights $|B_{ab}|^2 t_a^{r-1}t_b^{N-r-1}/Z$ of the centered real marked slab. Group both orders of each pair with $s=\min(t_a,t_b)/\max(t_a,t_b)$. Their common coefficient is $|B_{ab}|^2\max(t_a,t_b)^{N-2}/Z$, halved if summing an identical diagonal pair twice. For a slice face use its multiplication operator in the same expression with an extra $t_at_b$. Terms with two zero eigenvalues vanish for $N\ge6$, and $0^0=1$ at a zero endpoint power. Real self-adjoint insertions give equal squared matrix elements after swapping $a,b$. At $r=1$ the integral bounds the mass by $c_j(1)\le C(0)$. At fixed $N,\beta$ take a weakly convergent subsequence of these finite measures as the time period tends to infinity. All the displayed moments are continuous polynomials. The resulting representation can be nonunique; the bounds use any such limiting representation. [Wilson transfer construction](https://bib-pubdb1.desy.de/record/396349)

For $r\le m$, the integrand is at most $2s^{r-1}$. The finite sum of $r^2s^{r-1}$ is at most both $m^3$ and $(1+s)/(1-s)^3$, with the latter interpreted by a limit at $s=1$. Hence the uniform estimate
$$
 \chi\le K+36\sum_{j=1}^3\int \min\{m^3,\ 2(1-s)^{-3}\}\,d\nu_{j,N,\beta}(s)
$$
reduces the possible divergence to local weight at spatial transfer ratios approaching one. For instance $\nu_j([1-u,1])\le A u^{3+\epsilon}$ for $1/m\le u\le1$ suffices uniformly. Indeed the last bin contributes at most $A m^{-\epsilon}$ and bins at doubled widths contribute a geometric sum in $u^\epsilon$. This is a sufficient tail estimate, not a necessary exponent or a proved Wilson estimate. Slow but sufficiently light contributions are allowed. The existence of a continuum limit for specified separated insertions does not identify these lattice measures or bound this weighted moment. [Yang–Mills group's assessment and scope](https://github.com/yang-mills-group/YM)

### A bounded, clustering control on the same three-dimensional slice

Consider the standard four-dimensional isotropic Gaussian lattice field on the same cylinder, with positive mass $m_N=1/N$. On the time slice its covariance $G$ has spatial Fourier eigenvalue $g(p)=[s_p(s_p+4)]^{-1/2}$, $s_p=m_N^2+4\sum_i\sin^2(p_i/2)$, by the temporal Fourier integral. The massive nearest-neighbor random-walk Green function is nonnegative. $G(0)$ is uniformly bounded: with shortest grid index $h\ne0$ the summand is at most $N/(8|h|)$ from $\sin(\pi|h_i|/N)\ge2|h_i|/N$, and counting shells in three dimensions bounds the normalized sum. The zero summand contributes $O(N^{-2})$.

For the bounded centered observable $\sin\phi_x$, joint Gaussian integration gives covariance $e^{-G(0)}\sinh G(x)$. Its sum is at least $e^{-G(0)}g(0)$ and grows at least linearly in $N$. Each positive-mass regulator clusters, admits reflection positivity and has a bounded contact variance. This falsifies an inference from those properties alone on the required equal-time slice. The scalar observable is a control for the inference; it is not a Wilson plaquette. A worker's even cosine in four spacetime dimensions instead has a tail of order $|x|^{-4}$, summable on a three-dimensional slice. It would not demonstrate this obstruction here. [Finite Fourier check](controls.py)

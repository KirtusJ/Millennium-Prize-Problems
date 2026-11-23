# Common rotations and the best invariant observable

For a nonempty list of $m$ chords, whiten $K$ and diagonalize $K^{-1/2}V_R K^{-1/2}$ by an orthogonal transformation of chord labels. Both operations commute with color rotations. Denote the eigenvalues by $0\le t_i<1$, $t_*=\max_i t_i$. The standardized tuple has the representation
$$
 X_i=\sqrt{t_i}\,H_i+\sqrt{1-t_i}\,Z_i,\quad 1\le i\le m,
$$
where all $H_i,Z_i$ are independent standard normals in three colors. Given the exterior, the $H_i$ with $t_i>0$ encode the conditional mean. The other $H_i$ may be added independently without changing any dependence coefficient.

Consider the joint density of $(H,X)$ relative to their independent standard normal marginals. In a normalized tensor Hermite basis it is
$$
 1+\sum_{|\alpha|>0}\Big(\prod_{i,c}t_i^{\,\alpha_{ic}/2}\Big)
          h_\alpha(H)h_\alpha(X).
$$
This follows from the one-dimensional Gaussian conditional generating function for Hermites and independence over coordinates. The expansion is in $L^2$ since $\prod_i(1-t_i)^{-3}<\infty$. Conditional expectation given the common orbit of $X$ amounts to Haar averaging in its colors under the reference product measure. This operation annihilates every linear function of $X$. Orthogonal projection contracts $L^2$, so for $t_*\le1/2$ the squared norm of the surviving density correction is at most
$$
 \sum_{k\ge2}\binom{k+3m-1}{3m-1} t_*^k=O_m(t_*^2).
$$
Total variation is at most half its $L^2$ norm. Conversely observe just $|X_i|^2$ for an index with $t_i=t_*$ and retain $H_i$ externally. Data processing gives $a_\Gamma(R)\ge A(t_*)$, with $A(t)=(18e^{-3}/\pi)t+O(t^2)$. Thus the limiting block TV is bounded above and below by positive constants times $t_*$ as $t_*\to0$, and vanishes exactly when $t_*=0$. [Mehler’s formula and Gaussian chaoses](https://orbilu.uni.lu/bitstream/10993/19263/1/lecturenotes-coursfondation.pdf) · [Radial coefficient](../wilson/radial.md)

**Maximal correlation in the tangent experiment.** Let $f(X)$ be any centered unit-variance reading invariant under simultaneous color rotation. Its Hermite expansion has neither a constant nor a linear coefficient. Conditioning on $H$ multiplies each coefficient by $\prod_{i,c}t_i^{\alpha_{ic}/2}$ and replaces the basis function with its counterpart in $H$. Consequently $\|\mathbb E[f(X)\mid H]\|_2\le t_*$. This bounds the correlation with every unit-variance exterior reading since the conditional distribution depends on the exterior only through the mean. Equality is reached by
$$
 f(X)=(|X_i|^2-3)/\sqrt6,\qquad t_i=t_*>0,
$$
whose conditional expectation is $t_*(|H_i|^2-3)/\sqrt6$. The supremum correlation is $t_*$ and the best fraction of variance explained is $t_*^2$. At $t_*=0$ all centered readings have zero conditional mean. This optimization is in the limiting experiment; the compact-measure TV comparison does not by itself pass a supremum over unbounded, coupling-dependent, standardized tests.

**Relative color is retained.** For two vectors the inner product is observable even at fixed individual lengths. For three distinct modes the signed determinant is invariant under proper rotations and reverses under a color reflection. Multilinearity and independence give
$$
 \mathbb E[\det(X_i,X_j,X_k)\mid H]
       =\sqrt{t_it_jt_k}\,\det(H_i,H_j,H_k).
$$
Thus common conjugation can preserve a cubic reading. The upper bound removes only the linear terms and controls the full series from degree two onward. It requires no assumption that every surviving term has even degree.

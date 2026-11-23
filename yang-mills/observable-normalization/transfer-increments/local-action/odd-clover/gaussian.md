# The contact cancellation and the surface term

Use the forward Maxwell curvature $F_{ij}(p)=d_i(p)A_j(p)-d_j(p)A_i(p)$ with $d_i=e^{ip_i}-1$, in three independent colors. The free potential has identity covariance divided by $\sum_i|d_i|^2$ away from zero. In a periodic box omit the harmonic mode. Linearizing the signed clover averages this forward face over four bases $x,x-e_i,x-e_j,x-e_i-e_j$. Writing $b_j=(1+e^{-ip_j})A_j/2$ gives
$$
 C_{ij}(p)=i\sin p_i\,b_j(p)-i\sin p_j\,b_i(p).
$$
At opposite momenta the two curvatures therefore have a common exterior factor up to sign. Their wedge product vanishes even when their potentials differ. The integrated site charge, a sum of those pairings, is identically zero for each periodic potential, including at Nyquist frequencies. Cube redistribution gives the same integrated identity for $D$.

The infinite-volume zero-mode identity follows directly in momentum space. Divide each clover leg applied to a unit white-noise potential by $|\hat p|=(\sum_i|d_i|^2)^{1/2}$, or do so for each separate signed face leg in the cube reading. The resulting multipliers are bounded and continuous away from $p=0$ on the momentum torus. Wick's rule represents the spectral density $S_G(k)$ of the centered quadratic as an integral of squared symmetrized bilinear kernels with legs at $p,k-p$. For the cube reading, the shift of each summand from site to cube adds the total-momentum phase $e^{ik\cdot c}$. Dominated convergence gives continuity in $k$. At $k=0$ all shift phases are one and the preceding common-factor identity kills the kernel. In particular $S_G(0)=0$ includes all contact contributions.

For either reading the real-space covariance satisfies, uniformly in direction,
$$
 K_G^W(z)=-\frac{9}{\pi^4|z|^8}+O(|z|^{-9}),\qquad |z|\to\infty.
$$
Indeed the one-color cross-covariance of positive faces is $Q_z/(\pi^2|z|^4)+O(|z|^{-5})$, where $Q_z=\bigwedge^2(I-2\hat z\hat z^{\mathsf T})$. Bounded shifts leave its leading term unchanged. The orientation sign from the linear face cancels its clover weight, leaving total weight one per complementary plane pair for either stencil. Put $J=*$ on two-forms. Wick contraction of $\tfrac12 F^{\mathsf T}JF$ gives the coefficient $\tfrac32\operatorname{Tr}(J Q_z J Q_z^{\mathsf T})$ for three colors. The reflection reverses orientation, hence $Q_zJQ_z^{\mathsf T}=-J$ and the trace is $-6$. The second absolute spatial moment of $K_G^W$ is finite, so Fourier inversion gives $\sum_zK_G^W(z)=0$. [One-color kernel with lattice remainder](../site-scalar/README.md)

For example, for the Euclidean ball of radius $h\ge1$ in lattice units, summing the tail outside the ball and comparing unit cubes with spherical shells gives
$$
 \sum_{|z|\le h}K_\beta^W(z)
 =\frac{9}{2\pi^2}h^{-4}+O(h^{-5}+h^4\beta^{-1/8}),
 \qquad h\le A\beta^{1/4}.
$$
The continuum radial tail of $|z|^{-8}$ is $(2\pi^2/4)h^{-4}$. The thickness-one boundary and integrated gradient both cost $O(h^{-5})$. The leading term is resolved when $1\ll h\ll\beta^{1/64}$.

For a cube of $h^4$ sites or cells, the overlap with its translate by $z$ is $\prod_i(h-|z_i|)_+=h^4-h^3|z|_1+O(h^2|z|_1^2)$. For $|z|_1\ge h$ the latter bound follows directly, and on the smaller region it follows by multiplication. Thus, writing $V_W(h)$ for the variance of the sum,
$$
 V_{G,W}(h)=B_W h^3+O(h^2),\qquad
 B_W=-\sum_z |z|_1 K_G^W(z)\ge0.
$$
On the Wilson measure the additional error is $O_A(h^8\beta^{-1/8})$ by the pairwise comparison for $h\le A\beta^{1/4}$.

For the site reading $B_P>0$. In each coordinate the corresponding contribution to $B_P$ is the integral of $S_G(k e_i)/(1-\cos k)$ against $dk/(2\pi)$ on $[-\pi,\pi]$. To verify this identity subtract $S_G(0)=0$ and use $\int(1-\cos nk)/(1-\cos k)\,dk/(2\pi)=|n|$; the first absolute spatial moment justifies integration term by term. The integrand is nonnegative. For $i=0$ choose $k=\pi/3$ and internal momentum $p=(\pi/4)e_1$, with potentials polarized in directions 2 and 3 on the two legs. Their sine covectors at $p$ and $ke_0-p$ span the 01 plane; the two polarization averages are one. The resulting exterior four-product is nonzero on an open momentum neighborhood, so the spectral integral is strictly positive. Consequently $V_{\beta,P}(h)/h^3\to B_P>0$ when $1\ll h\ll\beta^{1/40}$. This simultaneous weak-coupling result is compatible with positive bulk variance at fixed $\beta$.

# Box-size dependence of the fixed-volume coefficient

For a unit flat four-torus let $d_4=\log\det{}'\Delta_{\mathbb T^4}$ be the logarithm of the zeta-regularized determinant of the positive scalar Laplacian, with its constant mode omitted. Let
$$
 h_4=\int_{[0,1]^4}\log\!\left(4\sum_{i=1}^4\sin^2(\pi x_i)\right)\,d^4x,
 \qquad f_4=\tfrac32\log(2/\pi)-3h_4 .
$$
The coefficient $C_L$ in the [fixed-box partition function](README.md) satisfies
$$
 \lim_{L\to\infty} e^{-L^4 f_4} C_L
 =\frac{(\pi/2)^{3/2}}{8\pi^2}\,e^{-3d_4}.
$$
There is no residual power of $L$ in this limit. Here $C_L$ is obtained by first sending the inverse coupling to infinity separately at each fixed $L$. The error in that first limit has no uniform bound in this calculation.

Write $V=L^4$, $P_L=\prod_{k\ne0}4\sum_i\sin^2(\pi k_i/L)$ and $G_L=\det(D_1^TD_1)$. Tree gauge gives $G_L=P_L^2/V$. For the equal-sided torus, Theorem 5.8 and Remark 5.9 of Chinta, Jorgenson and Karlsson give
$$
 \log P_L=Vh_4+2\log L+d_4+o(1).
$$
Their bulk constant equals the displayed $h_4$ by the Fourier symbol of the lattice Laplacian. For example, the heat trace per site is the average of $\exp[-4t\sum_i\sin^2(\pi x_i)]$, and the integral representation of the logarithm gives their bulk integral. The logarithmic singularity of the Fourier integral at the trivial mode is integrable in four dimensions. Thus $\log G_L=2Vh_4+2d_4+o(1)$ because $\log V=4\log L$. Substitution in the fixed-box expression for $C_L$ proves the limit. [Tree-gauge determinant](determinant.md) · [Chinta, Jorgenson and Karlsson, Theorem 5.8 and Remark 5.9](https://www.unige.ch/~karlssob/cjktori.pdf)

The unit torus has eigenvalues $4\pi^2|m|^2$ for $m\in\mathbb Z^4$. Jacobi’s four-square identity gives the continuation
$$
 \zeta_{\mathbb T^4}(s)=(4\pi^2)^{-s}\,8(1-4^{1-s})\,\zeta(s)\zeta(s-1).
$$
Using $\zeta(0)=-1/2$, $\zeta'(0)=-\log(2\pi)/2$ and $\zeta(-1)=-1/12$ gives
$$
 d_4=-\zeta'_{\mathbb T^4}(0)
     =-\log(2\pi)-\tfrac43\log 4-12\zeta'(-1).
$$
The factor $4\pi^2$ fixes the length convention for this constant. A finite spectral check eliminates the bulk term entirely by forming $[16\log G_L-\log G_{2L}]/30$, which tends to $d_4$. This checks the finite part independently of any numerical quadrature for $h_4$. [Borwein, Borwein and Straub, Example A.2](https://arminstraub.com/downloads/pub/wigner.pdf) · [Finite spectra](size_check.py)

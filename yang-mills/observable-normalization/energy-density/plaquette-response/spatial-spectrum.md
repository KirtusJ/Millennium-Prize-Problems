# Sharp spatial lower bound for the balanced excitation

On the periodic cube the coefficient $J$ has an exact best lower bound in terms of link-weight variance. Write $n=3L^3$, let $\bar w$ be the mean of the $n$ link weights and set
$$
s=\cos(\pi/L),\qquad
d_L=\frac{8(1-s^2)}{4-s^2+s\sqrt{s^2+8}},\qquad
j_L=\frac{d_L}{2}+\frac{d_L^2}{4}.
$$
Then $J(w)\ge j_L\sum_e |w_e-\bar w|^2$. Equality occurs for an axial Fourier mode with the transverse and longitudinal components chosen in the top eigenspace below. The coefficient satisfies $L^2j_L\to 2\pi^2/3$. This is a spatial smearing eigenvalue. The excitation energies in the balanced vacuum response are $9\kappa/2$ and $13\kappa/2$.

## Derivation

Let $N$ be the unsigned edge-by-face incidence matrix. Each row and each column has four ones, the face mean is $a=N^*w/4$, and $D=4I-NN^*/4$. For an edge put $z_i=w_e-a_{p_i}$ for its four incident faces. The six unordered squared pair defects sum to $\frac12\sum_i|z_i|^2+\frac14|\sum_i z_i|^2$. The sum of all incidence deviations $\sum_{e,p\ni e}|w_e-a_p|^2$ equals $4\|w\|^2-4\|a\|^2=\langle w,Dw\rangle$. The vector of edge sums $\sum_i z_i$ is $Dw$. Consequently
$$
J(w)=\langle w,(D/2+D^2/4)w\rangle .
$$
In particular $D$ is positive semidefinite. The polynomial above is strictly increasing on its spectrum.

Fourier transform using link and face centers. For $k_i$ represented in $[-\pi,\pi]$ write $c_i=\cos(k_i/2)\ge0$. The symbol of $N/2$ has a column for each face orientation $ij$, with entries $c_j$ in row $i$, $c_i$ in row $j$, and zero elsewhere. Denote this matrix by $B$. The symbol of $D$ is $4I-BB^*$. At zero momentum $BB^*=I+\mathbf1\mathbf1^*$, so the two orientation differences have eigenvalue three for $D$, while the uniform smearing has eigenvalue zero.

At each nonzero lattice momentum some $c_i\le s$ and the others are at most one. All entries of $BB^*$ are nonnegative and increasing in the $c_i$. Its largest eigenvalue is therefore bounded by that of the axial mode $(s,1,1)$ after permuting axes. This follows by replacing any Rayleigh vector by its componentwise absolute value and then increasing the matrix entries. The axial momentum $k=(2\pi/L,0,0)$ attains the bound. On this mode
$$
BB^*=\begin{pmatrix}2&s&s\\s&1+s^2&1\\s&1&1+s^2\end{pmatrix}.
$$
Its antisymmetric transverse eigenvalue is $s^2$. On the remaining two-dimensional subspace the diagonal entries are $2$ and $2+s^2$ and the off-diagonal entry is $\sqrt2 s$. The larger root is $m=2+(s^2+s\sqrt{s^2+8})/2$. Thus the least nonzero eigenvalue of $D$ is $4-m=d_L<3$. Taking a real or imaginary part of the axial eigenfunction gives a real extremizer. The limit follows from $1-s^2=\sin^2(\pi/L)$ and $d_L/(1-s^2)\to4/3$.

## Finite-box detector determinant

For a fixed $t>0$ let $F(u)=e^{-u}(1-e^{-u})^2$. Use the independent face residuals $a-v$ with their canonical orthonormal axes and the balanced links perpendicular to constants with any orthonormal basis. Write $p=3L^3$ for the number of faces and $h=3\kappa$. In these coordinates let $G_{\lambda,t}$ be the positive-time Gram matrix, obtained by applying $F(t(H-E_0))^{1/2}$ to the centered vectors. Define
$$
b_t=\frac{1}{h^2}\left[\frac{F(9t\kappa/2)}{144}
          +\frac{3F(13t\kappa/2)}{2704}\right].
$$
The rescaled columns in the two blocks converge in norm after division by $\lambda$ and $\lambda^2$, respectively. Indeed $\sqrt{F(t\,\cdot)}$ is continuous and vanishes at infinity on the nonnegative half-line, so the shifted norm-resolvent convergence gives operator-norm convergence of the filters. The two limiting ranges are orthogonal. Their Gram blocks equal $(F(th)/4)I_p$ and $b_t J_\perp$, where $J_\perp$ denotes the restriction of $D/2+D^2/4$ to links perpendicular to constants. By determinant continuity,
$$
\lim_{\lambda\downarrow0}\frac{\det G_{\lambda,t}}{\lambda^{2p+4(n-1)}}
=\left[\frac{F(th)}4\right]^p b_t^{n-1}\det J_\perp>0 .
$$
Thus the smallest limiting balanced Gram eigenvalue is exactly $b_t j_L$. The convergence and allowed interval in $\lambda$ still depend on the box. A positive finite-cutoff reading alone gives no lower bound on the original four-dimensional continuum trajectory. [Two-channel computation](channels.md) · [Direct incidence and spectral checks](execution.md)

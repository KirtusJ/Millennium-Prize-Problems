# Exact least eigenvalue of the temporal forest Hessian

Translate the box onto $[0,L]^4$. Write $s$ for the spatial vertex and $t$ for time. A spatial scalar vanishes on the spatial boundary, and $d_s$ is its edge gradient, keeping edges with at least one interior spatial endpoint. Relative tangential spatial edge values vanish on the boundary. With zero shell data, Z4’s forest sets the time links from every interior vertex *upward* to one. In linear coordinates the remaining variables consist of the bottom temporal links $b(s)$ and the spatial edge fields $H_t$ for $1\le t<L$. Set $H_0=H_L=0$. Directly from the plaquette incidence matrix, the one-color Maxwell form is
$$
 Q=\sum_{t=0}^{L-1}\|H_{t+1}-H_t-\mathbf1_{t=0}d_s b\|^2+
   \sum_{t=1}^{L-1}\|\operatorname{curl}_s H_t\|^2 .
$$
The norm on the denominator of the Rayleigh quotient is $\|b\|^2+\sum_t\|H_t\|^2$. Spatial boundary shells contribute zero. Decompose spatial edge fields into the gradient range and its orthogonal complement. The curl vanishes on gradients. Both the time differences and the bottom coupling respect the decomposition. On the complementary sector the time differences alone give a lower bound $t_L=4\sin^2(\pi/(2L))$ times the squared norm, by the Dirichlet sine basis.

For each normalized Dirichlet spatial eigenvector $w$ of $d_s^*d_s$ with eigenvalue $s>0$, use the normalized edge mode $d_sw/\sqrt s$. The longitudinal block on the coefficient of $w$ in $b$ and the $L-1$ time coefficients of this edge mode is
$$
 M_s=\begin{pmatrix}s&-\sqrt s\,e_1^{\mathsf T}\\-\sqrt s\,e_1&T\end{pmatrix},
 \qquad T=\operatorname{tridiag}(-1,2,-1)_{L-1}.
$$
Write $g(r)=\langle e_1,(T-rI)^{-1}e_1\rangle$. The Schur complement gives the equation $r=s(1-g(r))$. On $[0,t_L)$, $g$ is strictly increasing, $g(0)=(L-1)/L$ and $g(r)\to\infty$ since the first sine mode is nonzero at index one. There is exactly one root $r_s$ in $(0,t_L)$, and $M_s$ is positive definite by the Schur complement at zero. This root is its smallest eigenvalue. Since $r/s$ increases in $r$ while $1-g(r)$ decreases, $r_s$ increases with $s$. The smallest spatial eigenvalue in three dimensions is $s_L=12\sin^2(\pi/(2L))$, by products of interval sine modes. Thus $\lambda_N=r_{s_L}$ exactly, with three identical color copies.

The Green column is $(T^{-1}e_1)_j=(L-j)/L$, $1\le j<L$, by taking second differences. Hence $g'(0)=(L-1)(2L-1)/(6L)$. Spectral resolution gives
$$
 rg'(0)\ \le\ g(r)-g(0)\ \le\ \frac{rg'(0)}{1-r/t_L}.
$$
At the root $r\le s_L/L=3t_L/L$. Substituting these bounds in the scalar equation and expanding at large $L$ gives
$$
 \lambda_N=\frac{3\pi^2}{L^3}
                 \left(1-\frac{\pi^2}{L}+O(L^{-2})\right).
$$
Indeed $s_Lg'(0)=\pi^2/L+O(L^{-2})$, and the relative error in replacing $(g(r)-g(0))/r$ by $g'(0)$ is $O(L^{-1})$. For $L=2,4$ the roots are $0.8377223398$ and $0.1471217571$, reproducing the draft’s $N=1,2$ values. The asymptotic is for the Hessian in **these tree coordinates**. Its smallest eigenvalue is a gauge-coordinate conditioning constant, with no identification as a transfer energy.

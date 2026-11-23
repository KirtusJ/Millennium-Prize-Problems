# An independent one-cube integral at all positive spatial couplings

Take the original spatial Wilson measure on the six sides of one open unit cube. Set $a_d(b)=2I_d(b)/b$. The character coefficient of $e^{b\operatorname{Tr}U/2}$ at dimension $d$ is $d\,a_d(b)$. With independent positive couplings,
$$
                   Z(\{b_f\})=\sum_{d\ge1}d^2\prod_f a_d(b_f).
$$
Each edge belongs to two oriented faces. Schur integration forces their representation labels to agree, all labels coincide by connectivity, and the net dimension power is $6-12+8=2$. The factorial tails of the Bessel series justify local differentiation in every positive coupling.

At equal $b$ use probabilities $w_d=d^2a_d(b)^6/Z$. Write $m_d=(\log a_d)'$, $\ell_d=(\log a_d)''$. Two different marked faces give covariance $s=4\operatorname{Var}_{w}(m_d)$, and a twice-marked face gives $v_c=s+4\mathbb E_w\ell_d$. In particular $s>0$. All dimensions have positive weight and $m_d=(d-1)/b+I_{d+1}/I_d$ grows without bound with $d$ at fixed $b$. The six first-shell coefficients are $4\mathbb E_w\ell_d+6s$ (once) and $4\mathbb E_w\ell_d$ (five times). Both are positive by strict positivity of the covariance of independent Haar basis functions under the positive joint weight. As $b\downarrow0$, $s/(b/4)^4\to1$. This counts one common cube for any pair of its faces.

For the large-$b$ limit orient every face outward. The cellular constraint on the six Gaussian face curvatures is just that they sum to zero. Therefore the covariance per color is $P=I-\mathbf1\mathbf1^*/6$, and the limiting matrix $b^2\Gamma$ has diagonal $25/6$ and off-diagonal $1/6$. Its singlet and transverse eigenvalues are five and four. At $b=500$, direct character summation gives $5.00028$ and $3.99911$ for the two scaled coefficients, and $0.166861$ for $b^2s$. The analytical limit follows from the tree-fixed Haar integral on the open cube. [General open-box proof](open-box.md) · [Reproducible numerical checks](controls.py)

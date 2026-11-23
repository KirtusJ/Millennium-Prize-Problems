# Propagation at a common physical time

Let $H\ge0$ be self-adjoint on the centered fine Hilbert space, $S=e^{-t_0H}$, $P$ the inherited coarse projection, $Q=I-P$. Assume $I-e^{-2aH}\succeq\gamma Q$, $\gamma>0$, as a quadratic form on the entire space, and $\|PSP\|\le1-b$. Put $d=1-\|S\|$. Then
$$ d\ \ge\ {b\over1+2a/(\gamma t_0)} .$$
This implies the spectator estimate with the $1/2$ cap and coefficient eight. The hypothesis controls mixed coarse/fine vectors. A lower bound on the $Q$ compression alone is insufficient.

Let $\lambda_0=\inf\sigma(H)$. For $L>\lambda_0$ take a unit $v$ in $E=\mathbf1_{[0,L]}(H)$. Write $s=\|Qv\|^2$. The short-time form gives $\gamma s\le1-e^{-2aL}$. On the full space $S\succeq e^{-t_0L}E$. Test it on $Pv/\|Pv\|$ when $Pv\ne0$. Its overlap squared with $v$ is $\|Pv\|^2=1-s$, so $1-b\ge e^{-t_0L}(1-s)$. The inequality also holds for $Pv=0$. Sending $L$ down to the spectral infimum yields, with $x=e^{-t_0\lambda_0}=1-d$ and $r=2a/t_0$,
$$ b\le 1-x+x(1-x^r)/\gamma\le (1-x)(1+r/\gamma).$$
The last step uses $1-e^{-ry}\le ry$ and $ye^{-y}\le1-e^{-y}$ for $y\ge0$. No top eigenvector or commutation of $P,H$ is required. A zero-Hamiltonian spectral endpoint in the centered space forces $b\le0$ under the hypotheses.

For a refinement sequence let $K_i=1+2a_i/(\gamma_i t_0)$ and $M_i=\prod_{j=1}^iK_j$, $M_0=1$. A separately justified comparison $b_i\ge d_{i-1}-\varepsilon_i$ with $\varepsilon_i\ge0$ gives by multiplication and summation
$$d_n\ge \max(0,d_0-\sum_{i=1}^n M_{i-1}\varepsilon_i)/M_n.$$
Thus $\sum_i a_i/\gamma_i<\infty$ and $\sum_i M_{i-1}\varepsilon_i<d_0$ suffice at fixed $t_0$. This conclusion needs identification of the coarse physical state and matching of the time units at every refinement.

The universal coefficient two is sharp within this form of estimate. Set $t_0=2a$ and let $D=I-S=\operatorname{diag}(\alpha,\eta)$ with $0<\alpha<\gamma<\eta<1$. Define $Q=qq^*$ with $q=(\sqrt h,\sqrt{1-h})$, $h=\alpha(\eta-\gamma)/[\gamma(\eta-\alpha)]$. The equality $\gamma\langle q,D^{-1}q\rangle=1$ gives $D\succeq\gamma Q$. The actual full and coarse deficits are $\alpha$ and $\alpha\eta/\gamma$. Any universal coefficient $C$ replacing two would require $C\ge2(\eta-\gamma)$. Take $\eta\uparrow1$, $\gamma\downarrow0$, and $\alpha$ small enough to keep the coarse deficit below $1/2$. Conversely $D=\tfrac14\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)$ yields a positive $Q$-compression and zero full deficit for coordinate projections. Its kernel contains a vector with a fine component. Both matrices define legitimate nonnegative Hamiltonians since $I-D$ is positive definite. [Matrix controls](checks.py)

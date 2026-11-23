# The temporal electric kernel and its large-step limit

Use three spatial momenta $k_j\in[-\pi,\pi]$, $p_j=e^{ik_j}-1$, $a_j=|p_j|^2$ and $A=\sum_{j=1}^3 a_j$. For the single-color outward-oriented electric faces the four-dimensional curl-projection symbol is $(a_t\mathbf1_{j=k}+p_j\bar p_k)/(a_t+A)$. At time displacement $n\ge1$ the constant term in $a_t/(a_t+A)=1-A/(a_t+A)$ drops out. Fourier integration over the temporal angle gives the matrix
$$
 H_{jk}(k,n)=(p_j\bar p_k-\mathbf1_{j=k} A)\,\frac{e^{-n\omega}}{2\sinh\omega},
 \qquad \omega=2\operatorname{asinh}(\sqrt A/2).
$$
Indeed the coefficients of $(a_t+A)^{-1}$ solve the nearest-neighbor resolvent recurrence with unit source at zero. Decay selects $e^{-|n|\omega}$ and the source jump fixes the denominator. Values of the integrand at the single spatial zero are immaterial.

Take the six-by-three matrix $D(k)$ with the two entries $-1,e^{-ik_j}$ in rows belonging to its $j$th column and zeros elsewhere. The first sign reverses one of the two parallel face orientations. The second face is based one cell earlier along $j$. Then $K(n)=\int D H D^*\,d^3k/(2\pi)^3$. For the opposite-pair contrast $w=(1,-1)/\sqrt2$ in direction $j$, $Pw=w$ and
$$
 w^TK(n)w=-\int \frac{|1+e^{-ik_j}|^2}2(A-a_j)
                  \frac{e^{-n\omega}}{2\sinh\omega}\,\frac{d^3k}{(2\pi)^3}<0.
$$
The integrand has strict sign on an open set. This proves strict positivity of $c(n)$ at every positive integer. In fact $D^*\mathbf1=p$ and $Hp=0$, so here $PK(n)P=K(n)$ exactly.

For large $n$ substitute $k=u/n$. Uniformly on the Brillouin cube $\omega\ge c|k|$, $2\sinh\omega\ge c|k|$, and the numerator of $H$ is $O(|k|^2)$. After multiplication by $n^4$ the integral is dominated by $C|u|e^{-c|u|}$ on $\mathbb R^3$. Fixed face displacements tend to unit phases. Off-diagonal components of the continuum kernel integrate to zero by oddness. In a diagonal component the spherical average of $1-u_j^2/|u|^2$ is $2/3$, yielding
$$
 -\frac{1}{2}\frac{2}{3}\frac{4\pi}{(2\pi)^3}\int_0^\infty r^3e^{-r}dr
 =-\frac1{\pi^2}.
$$
Thus $n^4K(n)$ tends to three diagonal two-by-two blocks $-ss^T/\pi^2$, $s=(-1,1)$. Their squared Frobenius norm sums to $12/\pi^4$. Dividing by 1536 gives the coefficient $1/(128\pi^4)$.

## Physical time and the choice of trajectory

For any prescribed spacings $b_j\downarrow0$, there exist $\beta_j,L_j\to\infty$, $b_jL_j\to\infty$, for which, simultaneously at every real $t>0$,
$$
 \beta_j^4 b_j^{-8} C_{\beta_j,L_j}(\lfloor t/b_j\rfloor)
 \longrightarrow \frac{1}{128\pi^4t^8}.
$$
Enumerate positive rational times. At step $j$ there are finitely many specified integer displacements, obtained from the first $j$ times and that fixed $b_j$. Omit any zero displacement until it becomes positive. By convergence at each fixed displacement, choose the spatial box and coupling sufficiently large that the error in $\beta_j^4 C(n)$ against $c(n)$ is at most $b_j^8/j$ for all those displacements. Enlarge both parameters if needed to have $b_jL_j\ge j$ and $\beta_j\ge j$. The large-step asymptotic gives convergence on the rationals.

To extend it, let $S$ be the positive transfer normalized by its top eigenvalue, and $\Omega$ its unit vacuum. Insert $W_e^2$ in the transfer kernel at the chosen spatial position, with the same normalization and half spatial weights. This bounded operator $B$ is self-adjoint: reversing the slab inverts all its temporal paths, preserves $R$ and $U_e\cdot H$, exchanges the two boundary weights, and preserves the integrated Haar measures. For $n\ge1$ the connected reading is
$$
 C(n)=\langle v,S^{n-1}v\rangle,\qquad v=B\Omega-\langle\Omega,B\Omega\rangle\Omega .
$$
This includes adjacent slabs. Consequently $C(n)$ is nonnegative and nonincreasing, so dense rational times squeeze each real time between values of the continuous limit. Along arbitrary weak trajectories $\beta^4 C(\lfloor t/b\rfloor)\to0$ for $t>0$ just by bounding first by a fixed $n$ and then sending $n\to\infty$. The extra factor $b^{-8}$ in the nonzero limit requires the selection above. [Wilson transfer hypotheses](../../../transfer-operator/periodic-time/)

Weight the spectral measure of $v$ at $n_0=\lfloor t_0/b_j\rfloor$ by $S^{n_0-1}$ and normalize by $C(n_0)$, for $t_0>0$. Under the physical energy variable $E=-b_j^{-1}\log S$, its Laplace transforms converge to $(t_0/(t_0+s))^8$ for $s\ge0$. Differences of one step from the floors are squeezed by the same monotonicity. The limit is the gamma probability law of shape eight and rate $t_0$. There is positive limiting relative weight on every positive energy interval. B4’s [seven-reading test](../../../spectral-support/magnetic-band-rank/) therefore applies to this particular one-slab observable along the selected trajectories: take an integer number of steps approximating $T/b_j$, and use the measure tilted at the first such reading. The result locates at least three distinct finite-box levels in its stated energy window at sufficiently fine cutoff. The trajectory extraction here supplies no prescribed rate, and none of these results establish a mass gap for interacting continuum Yang–Mills theory.

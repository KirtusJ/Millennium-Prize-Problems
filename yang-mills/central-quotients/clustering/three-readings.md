# A positive-energy band from three strictly positive times

Fix $s,h,T,m>0$, and a lower energy $0<\ell<m$. For now use translates of the same bounded self-adjoint local observable in a translation-invariant vacuum. Its connected spectral mass is $V=\|(1-P_0)A\Omega\|^2$. Set $d=(1,-2,1)$, $s_j=s+jh$, $\alpha_j=s_j/T$, $b_j=\sqrt{1+\alpha_j^2}$, $M=mT$. Measure
$$
 L=\operatorname{Re}\,[C(s)-2C(s+h)+C(s+2h)].
$$
Here the probes are spatially separated at every time. The real cross spectral measure can have either sign. Its total variation in any energy interval is bounded by the single-probe mass there. The spectral multiplier for $L$ is $g(E)=e^{-sE}(1-e^{-hE})^2$.

Define
$$
 B_j=\frac1\pi e^{-M(b_j-1)}\log\frac{b_j+1}{b_j-1},\qquad
 q_l=(h\ell)^2+\ell T\sum_j |d_j|e^{-M(b_j-1)},\qquad
 q_H=\sum_j |d_j|e^{-M b_j},\qquad U=1+\sum_j |d_j|B_j .
$$
Let $\mathcal E=\sum_j |d_j|\mathcal E_{\alpha_j}$, with the bounds from the [finite-time filter](filter.md). Put $W=\|E_Q((\ell,m))A\Omega\|^2$. Then
$$
 \boxed{\qquad W\ \ge\
 \max\left(0,\frac{|L|-\mathcal E-(q_l+q_H)V}{U}\right).\qquad}
$$
A tighter form replaces $(q_l+q_H)V+UW$ on the upper-bound side by $q_*(V-W)+UW$ where $q_*=\max(q_l,q_H)$. If this bound is inverted, require $U>q_*$. An atom at $\ell$ or $m$ is charged to the respective exterior piece. The conclusion for a positive lower bound on a sequence therefore survives in the compact band $[\ell,m]$ of any weak limiting single-probe measure. A hypothesis on limiting measures or uniform positive normalization is still needed to obtain a continuum field.

To verify the constants, subtract $\sum_j d_j H_{\alpha_j}(ET)$ from $g(E)$. For $E\ge m$ the residual has modulus at most $q_H$ by the contour theorem. Each $|H_{\alpha_j}(x)|$ is at most $B_j$, obtained by integrating the positive kernel with $|\sin|\le1$, using $u=\cos\theta$. It is also at most $x e^{-M(b_j-1)}$ for $x\ge0$, by $|\sin(x\sin\theta)|\le x\sin\theta$ and the kernel domination in the proof. At $E\le\ell$ use $g(E)\le(h\ell)^2$. In the middle interval use $g(E)\le1$. Integrating these three bounds gives the result. At equal time alone a sequence of positive-energy atoms can collapse into the vacuum. Here fixing $\ell>0$ excludes that failure mode from the certified interval.

## Actual Wilson histories

In a finite periodic spatial $SU(2)$ box use the positive injective transfer $T_a$ normalized by its norm and $Q_a=-a^{-1}\log(T_a/\|T_a\|)$. Three integer-time correlations of the original Wilson history use $N_j=\lfloor s_j/a\rfloor\ge1$. Subtract their vacuum products, or use the three-term difference in which the common vacuum product cancels. If $\widetilde L$ denotes this rounded reading, its absolute error relative to the exact log-transfer $L_a$ is bounded by
$$
 \delta_{\rm step}=V_a\sum_j\frac{|d_j|}{e N_j},\qquad
 V_a=\|(1-P_{0,a})A\Omega_a\|^2 .
$$
Indeed the scalar error between powers $N$ and $N+\delta$, $0\le\delta<1$, is at most $\sup_{x\ge0}xe^{-Nx}=1/(eN)$. For smooth equal-time loop multipliers these are ordinary two-slice observations; at finite temporal period include B4's separate thermal error. [Wilson histories and finite-period comparison](../../transfer-operator/periodic-time/)

One can apply the band test **to the finite Wilson spectrum itself**. Bound its sine expectation $S_a(t)$ with $|S_a(t)|\le |S(t)|+\delta_{\rm rt}$, uniformly on $[0,T]$. The previous [real-time Wilson comparison](../locality/wilson-real-time.md) supplies $\delta_{\rm rt}$ from the positive Euclidean transfer error and the Hamiltonian form energies of the finitely many smooth multiplier vectors. For instance use the maximum of the two errors in the ordered vacuum two-point functions at $\pm t$, each with both vacuum replacements; the symmetrized imaginary part does not increase this maximum. The same result applies to other probes if their form budgets are supplied. Constants cancel in the symmetrized commutator. Because all three lags are strictly positive, the integrated added error costs at most $\delta_{\rm rt}\sum_j |d_j|B_j$. The static kernel alone would have a logarithmic singularity for a constant error near zero.

Use the boxed formula with $|\widetilde L|$ in the numerator, $V_a$ for $V$, and subtract both $\delta_{\rm step}$ and $\delta_{\rm rt}\sum_j |d_j|B_j$ in addition to the Hamiltonian locality error. It certifies $\|E_{Q_a}((\ell,m))A\Omega_a\|^2$ at that spacing. An additional certified absolute measurement or quadrature error subtracts directly from the numerator. For real scalar multiplication probes $V_a$ itself is a one-slice variance; an upper bound suffices in the coarse test. In a varying family take small enough temporal steps using the cited boxwise comparison on a growing finite list of times and probes. No uniform physical gap is an assumption of this inverse test. A positive numerical budget for weak-coupling four-dimensional Wilson histories remains to be established.

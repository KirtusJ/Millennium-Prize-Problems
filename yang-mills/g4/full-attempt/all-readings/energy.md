# How much Dirichlet energy can a fine correction save?

The [magnetic derivative](README.md) has an interpretation in a variational problem at nonzero coupling. Fix the same finite Wilson box, mesh, temporal coupling and lag. For a nonconstant coarse reading $f$ let $D_b=I-K_b^n$. Hold its conditional mean fixed, and allow any physical fine correction $h$ with $P_bh=0$. Define the maximal fractional reduction in the stationary Dirichlet energy by
$$
 \mathcal L_\ell(b)=\sup_f
 \left(1-\frac{\inf_{h:P_bh=0}\langle f+h,D_b(f+h)\rangle_{\pi_b}}
                  {\langle f,D_b f\rangle_{\pi_b}}\right).
$$
Constants can be removed from $f$. Then
$$
 \mathcal L_\ell(b)=b^2 J_{\ell,L}(g,n)^2+O_{L,\ell,g,n}(|b|^3).
 \tag{1}
$$
For even mesh the remainder improves to $O_{L,\ell,g,n}(b^4)$. The leading coefficient in (1) stabilizes **exactly** with the volume at each fixed lag. Under the sufficient thick-slab condition its exact value is the [square formula](optimizer.md). This gives a quadratic variational coefficient with a volume-independent upper bound. The size of the interval on which a fixed error bound holds can depend on the box.

### Eliminating the fine variables

Write $Q_b=I-P_b$, $A_b=P_b D_bP_b$ on centered coarse states, $C_b=Q_b D_b Q_b$ on fine states, and $R_b=Q_b K_b^nP_b$ between the two. The fixed-box positive transfer has a simple top eigenvalue one and a gap, so $A_b,C_b$ are bounded below for $b$ close to zero. Completing the square in the energy gives the unique optimal fine correction $h=C_b^{-1}R_b f$ and the effective coarse form $A_b-R_b^*C_b^{-1}R_b$. Consequently
$$
 \mathcal L_\ell(b)=\|C_b^{-1/2}R_bA_b^{-1/2}\|^2.
$$
The sign of $h$ follows from the off-diagonal Dirichlet block $-R_b$. This is the Schur complement of the fine energy. [Anderson and Trapp, *Shorted Operators II*](https://doi.org/10.1137/0128007)

At fixed box the electric kernel is a strictly positive continuous density on compact link space. Its finite magnetic tilt is analytic in the uniform norm near zero. Compactness, isolation of the simple vacuum and the smoothing eigenfunction equation give an analytic vacuum there in the uniform norm. Thus the stationary density $w_b$ relative to electric Haar and its inverse stay bounded. In reference coordinates the conditional expectation is $P_bv=P_0(w_bv)/P_0 w_b$, analytic in operator norm. Multiplication by $\sqrt{w_b}$ identifies stationary and reference Hilbert spaces unitarily for real $b$. In those coordinates the orthogonal projections onto the constant, centered coarse and fine spaces vary real-analytically. Nearby orthogonal decompositions have analytic unitary identifications: for their projections $E_i(b)$, take the unitary polar factor of $\sum_i E_i(b)E_i(0)$, invertible near the identity. Functional calculus on the two positive diagonal compressions now gives analytic inverse square roots. At zero $R_0=0$. Derivatives of the outer factors and identifications drop out, and the derivative of the central block is $Q_0(K_b^n)'_0P_0$ in the two original slots. Therefore the normalized operator has expansion $bN+O(b^2)$ with $\|N\|=J_{\ell,L}$. Squaring proves (1), including in the presence of degenerate maximizing states. [Moving-vacuum estimates](../blocking/README.md) · [A4’s finite-box uniform-norm argument](../../../observable-normalization/transfer-increments/electric-lag/coarse-memory/README.md)

For even $\ell$ the spatial center transformation taking $b$ to $-b$ fixes every straight coarse reading pointwise. It preserves the constraint $P_b(f+h)=f$ under transport. The stationary coarse marginal, its coarse energy and the minimized energy on each fixed coarse datum are even. On the fixed coarse reference space with constants removed (or using classes modulo constants), these are even analytic operator-valued forms by polarization. The normalized *loss operator* is therefore $b^2 N^*N+O(b^4)$ in norm. Taking its largest Rayleigh quotient gives the even-mesh remainder. Using evenness only of the optimized scalar would allow a term proportional to $|b|^3$.

### Comparison with three-slice memory

A4 obtained the two-lag composition defect $R_b^*R_b$ by conditioning on the middle coarse slice. If $V_\ell$ denotes its maximal **quadratic coefficient per unit input electric energy**, then the factor $C_0^{-1}$ in the variational problem gives
$$
 V_\ell\ \le J_{\ell,L}(g,n)^2\ \le \frac{V_\ell}{1-q^{4\ell n}} .
$$
Indeed all derivative images have electric eigenvalues $u\le q^{4\ell}$, so their inverse fine defect has spectrum in $[1,(1-q^{4\ell n})^{-1}]$. The two coefficients are consequently asymptotic at long electric time. This relates A4’s measurable memory to the energy lost on eliminating an entire resolution. At finite spatial coupling the corresponding fine resolvent can feel slow modes anywhere in the fine sector. Bounding it and the transfer between resolutions along a physically calibrated isotropic sequence remains necessary on G4’s fixed-scale proof route. [A4’s composition defect](../../../observable-normalization/transfer-increments/electric-lag/coarse-memory/README.md) · [G4’s comparison with Z4](../README.md#comparison-with-z4)

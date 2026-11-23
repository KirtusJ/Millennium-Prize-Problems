# Turning on the spatial Wilson action

This is an attempt to continue the electric answer toward isotropic four-dimensional $SU(2)$. Write $g>0$ for the coefficient of the temporal plaquettes and $b$ for the coefficient of the spatial plaquettes. Isotropy requires $b=g$. We calculate at $b=0$, with $g$ arbitrary and the spatial side fixed. The analytic radius and remainder can depend on both $L$ and $g$.

Take even $L\ge6$, $N=3L^3$ spatial faces and $\phi_p=\mathrm{Tr}U_p$. In slice Haar the $\phi_p$ are orthonormal. Put $A=\tfrac12\sum_p\phi_p$. Up to a scalar that cancels in eigenvalue ratios, the transfer is $T_b=e^{bA/2}K e^{bA/2}$. It is a compact analytic self-adjoint family near zero. On physical states $K$ has top eigenvalue one, and its top excited eigenvalue $\lambda=q^4$ has precisely the $N$ square characters as basis. Here $q=I_2(g)/I_1(g)$ and $t=I_3(g)/I_1(g)$. The proof that higher spins and other supports have smaller eigenvalues is in the [electric calculation](electric.md). At side four winding states would enlarge this eigenspace.

Define
$$
 H(x)=\frac{\lambda+x}{\lambda-x},\qquad h=\frac{1+\lambda}{1-\lambda},
 \qquad v=\frac{H(q^6)+3H(q^6t)}4,\qquad J=v-h .
$$
For the centered physical log gap at fixed $L,g$ we obtain
$$
 m_L(g,b)=-4\log q-
 \frac{b^2}{8}\left[H(t^4)-2h+24J\right]+O_{L,g}(|b|^3).       \tag{1}
$$
The coefficient is independent of volume. The normalized eigenfunction of the vacuum behaves differently. With its phase fixed by positive Haar mean and unit norm, differentiation gives $\Omega'_0=(1+\lambda)A/[2(1-\lambda)]$ and $\|\Omega'_0\|^2=N(1+\lambda)^2/[16(1-\lambda)^2]$.

### Resolvent and removal of the vacuum contribution

For an isolated eigenvalue $r$ of $K$ let $P$ be its spectral projection. In both clusters of interest $PAP=0$. For the excited cluster this follows by independent center flips of the links under Haar, since an odd number of elementary square boundaries cannot cancel in a product of three fundamental characters. The vacuum statement is $\mathbb EA=0$. Differentiate $T_b$ and eliminate the perpendicular component of an eigenvector to first order using $(r-K)^{-1}$ there. This is a bounded inverse at fixed volume. The coefficient of $b^2$ on the cluster is
$$
 P(T''_0/2)P + PT'_0(r-K)^{-1}_{P^\perp}T'_0P
 =\frac r2\,PA\frac{r+K}{r-K}\bigg|_{P^\perp} AP .
$$
For an intermediate eigenvalue $x$ the two scalar coefficients are $(r+x)/4$ and $(r+x)^2/[4(r-x)]$. Their sum gives the expression above. This calculation is the second-order secular equation for the isolated cluster. The eigenvalues of this finite matrix give all its second-order eigenvalue coefficients, including the largest. The vacuum at $r=1$ has relative coefficient $Nh/8$, since $A1$ lies in the $\lambda$ cluster and $\|A\|^2=N/4$. Subtracting the vacuum coefficient gives the normalized excited eigenvalue. Taking the negative logarithm gives the sign in (1).

### Exactly which connected terms survive

For $S=2A=\sum_s\phi_s$, form the matrix $\langle S\phi_p,H(K)S\phi_r\rangle$ and subtract $Nh$ from its diagonal. The second-order relative coefficient is the top eigenvalue of the resulting matrix divided by eight. Independent link-center parities show that a pair from the two sums can contribute only if the mod-two boundaries of its four faces cancel. A nonempty set of at most four distinct faces cannot have zero boundary. Each of a chosen face’s four edges would need a different other face, since two elementary faces here meet in at most one edge. Thus labels occur in pairs.

- For the same face, $\phi_p^2=1+\chi_2(U_p)$, with $\chi_2$ the spin-one character. The two components have squared norm one each and kinetic eigenvalues $1,t^4$. They contribute $H(1)+H(t^4)$.
- When $p\ne s$ share no edge, $\phi_p\phi_s$ has norm one and kinetic eigenvalue $q^8=\lambda^2$, even if the faces share a vertex. Here $H(\lambda^2)=h$ and $H(1)=-h$.
- For one shared edge the six other edges carry the fundamental representation. On the shared edge, two fundamentals give singlet and spin one. The product has squared norm one, by conditioning on the shared link and integrating the independent arms. Haar projection on that link yields one half of a single fundamental perimeter trace by Schur orthogonality (reverse either square if needed). Its squared norm is $1/4$. The remaining $3/4$ has spin one. This gives the two eigenvalues $q^6,q^6t$ and the weighted value $v$.

Each face has 12 distinct edge neighbors. The diagonal after subtraction is $H(t^4)-2h+12J$. In an off-diagonal entry the channel from $\phi_p^2,\phi_r^2$ contributes $-h$. Exchanging $p,r$ in the other pair contributes either $h$ or $v$. Thus the off-diagonal entries are $J$ for edge neighbors and zero otherwise. Moreover $J>0$. Under one-link Wilson density the scalar $c=\tfrac12\mathrm{Tr}U$ satisfies $\mathbb Ec=q$ and $\mathbb Ec^2=(1+3t)/4>q^2$. The function $H$ is increasing and strictly convex on $x<\lambda$. Jensen gives $v\ge H(q^6(1+3t)/4)>H(q^8)$. The constant vector attains the maximum adjacency eigenvalue 12. Its row sum gives (1).

### Two limits and independent tests

As $g\downarrow0$, $q\sim g/4$, $t\sim g^2/24$, and the bracket in (1) tends to $-1$. The spatial coefficient tends to $+1/8$. On the formal isotropic line, $b^2/8$ corresponds to $2u^2$ with $u=I_2(g)/I_1(g)\sim g/4$. This agrees with the published beginning $-4\log u+2u^2$ of the strong-coupling glueball series. The published series and (1) take different limits. This agreement alone cannot justify taking $b=g$ in the remainder. At large $g$, $q=1-3/(2g)+O(g^{-2})$ and $t=1-4/g+O(g^{-2})$. Then $h/g\to1/3$, $H(t^4)/g\to1/5$ and $J/g\to1/21$. The coefficient of $b^2$ in the gap is asymptotic to $-71g/840$, while the electric gap is asymptotic to $6/g$. A sign change of a Taylor coefficient in this anisotropic magnetic perturbation concerns a different derivative from a renormalized beta function. [Münster’s glueball expansion](https://www-library.desy.de/preparch/desy/postpr/1985/desy85-007.pdf) · [Langelage, Münster and Philipsen](https://arxiv.org/abs/0805.1163)

The numerical controls diagonalize transfers separately from the formula. A single genuine $SU(2)$ square uses the character basis, where multiplication by $\chi_1$ is path adjacency. The binary tetrahedral subgroup gives an exactly finite adjacent-pair model with 76 gauge orbits and the same singlet/triplet recoupling of the fundamental. Its kernel is built from one shared link increment and two independent three-link arms. At temporal couplings 1.3, 2.2 and 4.0, second differences agree with the respective one- and two-face formulas to the tolerances in the code. These controls test the recoupling and vacuum subtraction. Formula (1) on a cubic torus uses the analytic count of 12 neighbors. [Programs and values](transfer_check.py) · [Run record](execution.md)

**Failure to continue.** On an even torus choose central links $U_i(x)=(-I)^{\sum_{j<i}x_j}$. Every spatial plaquette is $-I$. The identity field has every plaquette $+I$. The oscillation of the magnetic exponent is proportional to $bL^3$ and the actual vacuum derivative grows as $\sqrt{L^3}$. A uniform proof cannot follow from the raw supremum norm of the magnetic weight or the Haar-norm derivative of the vacuum. The linked second-order cancellation succeeds exactly. We have no control of the connected remainder to all orders on a path reaching isotropic weak coupling. B4’s physical-time result applies at fixed spatial spacing and small magnetic perturbation in the blocked-time regime. [B4’s positive result](../../transfer-operator/blocked-time/README.md)

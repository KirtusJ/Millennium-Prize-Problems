# Uniform pressure bounds at fixed representation dimension

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Z4’s weighted-circle example shows that the ratio of the two global power-law bounds for Haar volume can diverge at fixed matrix size. The Wilson pressure comparison only needs the volumes at comparable radii. This gives a representation-independent constant for each fixed matrix size $N$, even for disconnected subgroups. It also makes the constants in the [spatial eighth-root gap bound](compact-groups.md) uniform over positive-dimensional closed subgroups of $U(N)$. [Compact-group subsection under review](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/7235a2c8f801/yang-mills/z4/attempt/paper/sec_general.tex#L15-L30)

## Compare chordal balls at the same coupling

Use probability Haar measure on the image $H\subset U(N)$ and the bi-invariant chordal metric $\chi(U,V)=\|U-V\|_{\mathrm{HS}}/\sqrt{2N}$. The Wilson action per face is $s(U)=\chi(I,U)^2$. Write $v(r)=\mu_H(B(I,r))$ for closed balls, and $D=2N^2$ for the real dimension of the ambient matrix space. For $r>0$,
$$
v(R)\le(1+2R/r)^D v(r).
$$
Choose a maximal $r$-separated subset of the subgroup ball of radius $R$. Its $r$-balls cover that ball; each has subgroup measure $v(r)$ by left invariance. Its open ambient $r/2$-balls are disjoint inside the ambient ball of radius $R+r/2$. Comparing Euclidean volumes gives the displayed bound. This uses ambient volume for counting and Haar measure for the cover, including when the subgroup is finite. [Volumetric covering argument](https://elliotpaquette.github.io/high-dimensional-probability/lectures/01-curse-of-dimensionality.html)

Set $r=(2\beta)^{-1/2}$ and $z(b)=\int e^{-bs}\,d\mu_H$. Integration over Gaussian level sets now gives
$$
z(\beta/2)=\int_0^\infty 2t e^{-t^2} v(2tr)\,dt\le A_N v(r),\qquad
A_N=\int_0^\infty 2t e^{-t^2}(1+4t)^D\,dt<\infty .
$$
On an even periodic box $L^4$, the temporal forest leaves $3L^4+L^3$ free links. Restrict each to the chordal ball of radius $r$. Each face has chordal radius at most $4r$, so $\beta s(U_p)\le8$ and the lower bound is $Z_L(\beta)\ge e^{-48L^4}v(r)^{3L^4+L^3}$. For the upper bound retain the $3L^4-3L^3$ nonwrapping temporal plaquettes. Their Haar integrals give $Z_L(\beta/2)\le z(\beta/2)^{3L^4-3L^3}$. Therefore, with $K_N=48+3\log A_N$,
$$
3\,\mathbb E_{\beta,L}\beta s(U_p)
\le L^{-4}\log\frac{Z_L(\beta/2)}{Z_L(\beta)}
\le K_N+\frac4L\log\frac1{v(r)}
\le K_N+\frac{4D}{L}\log(1+4\sqrt\beta).
$$
The first inequality is Jensen, using $6L^4$ faces and isotropy. The last uses the diameter bound $\sqrt2$ and the same covering inequality. This finite-volume expression keeps the temporal seam explicit. In every even-periodic thermodynamic limit at fixed $\beta>0$, $\mathbb E\beta s(U_p)\le K_N/3$. The original unit-block reflection argument further gives $\mathbb E e^{\beta s(U_p)/8}\le e^{256K_N}$ in such states. Its face multiplicity bound uses only lattice geometry, and site reflection preserves the class function $s$. [Forest and reflection proof](../pressure.md) · [Faria da Veiga and O’Carroll on Wilson stability and plaquette fields](https://arxiv.org/abs/2205.07376)

**Effect on the spectral statement.** In the projected-score proof the uniform first moment is the only measure-dependent input to the block comparison. The projection onto the represented Lie algebra has norm one. Each matrix product or commutator bound uses $\|A\|_{\rm op}\le\sqrt N |A|$ in normalized Hilbert–Schmidt norm. Path counts, heat estimates and the one-colour free covariance are group independent. Gaussian Fourier integration costs at most a constant depending on $N$ since $1\le d=\dim H\le N^2$. Take the minimum of the limiting positive free readings $B_d(1)$ over these finitely many dimensions and fix the block parameter $s_0=1$. The free finite-block convergence is uniform over the same finite list. Thus there exist $C_N,\beta_N<\infty$ such that, for every such $H$ of positive dimension and $\beta\ge\beta_N$, every even-periodic limit obeys $m_\mu(\beta)\le C_N\beta^{-1/8}$ in lattice units. This projection argument never uses the inverse exponential chart. Indeed the constant in $2s-|J|^2\le C_\rho s^2$ can diverge: at angle $2\pi/k$ in the weighted circle below, $s=\sin^2(\pi/k)$ and $|J|^2=\sin^2(2\pi/k)/(2(1+k^2))$. The ratio $(2s-|J|^2)/s^2$ grows as $2k^2/\pi^2$. There is no corresponding inference here about uniform convergence of the full plaquette action to the squared projected field. [Score and block proof](compact-groups.md)

## Two normalization checks for the manuscript

1. **Weighted circle.** For $\rho_k(t)=\operatorname{diag}(e^{it},e^{ikt})$, $k\ge1$ an integer, write $V(a)=\Pr(s\le a)$. The coefficient at zero is $\lim_{a\downarrow0}V(a)/\sqrt a=2/(\pi\sqrt{1+k^2})$. Exactly $V(1)=1/2$ for odd $k$ and $V(1)=(1-1/(k^2-1))/2$ for even $k$. The sign condition is $\cos((k+1)t/2)\cos((k-1)t/2)\ge0$. For odd $k$, shifting the original angle by $\pi$ negates $\cos t+\cos kt$. For even $k$, the two odd frequencies $k\pm1$ are coprime. In the $L^2$ cosine series of $\operatorname{sgn}(\cos x)$ the nonzero coefficients are $4(-1)^{(n-1)/2}/(\pi n)$ for positive odd $n$. In the product average only common harmonics survive; their signs are opposite because the product of the two frequencies is $3\bmod4$. Parseval and $\sum_{j\ {\rm odd}>0}j^{-2}=\pi^2/8$ give mean $-1/(k^2-1)$. This confirms Z4’s obstruction to using separate global power-law constants and explains the values at $k=2,10,50$.

2. **Fundamental SU(3).** With $s=1-\operatorname{Re}\operatorname{Tr}U/3$, I obtain
$$
V(a)=\frac{9\sqrt3}{8\pi}a^4\left(1-\frac a5+O(a^2)\right).
$$
In the plane $\sum\theta_i=0$ write $r^2=\sum\theta_i^2$. Normalized Weyl integration has factor $1/[6(2\pi)^2\sqrt3]$ in Euclidean plane area. The squared algebraic Vandermonde is $(r^6/2)\cos^2(3\phi)$ after choosing the angular origin. The trigonometric Weyl density multiplies it by $1-r^2/4+O(r^4)$ since $\sum_{i<j}(\theta_i-\theta_j)^2=3r^2$. Also $\sum\theta_i^4=r^4/2$, so $s=r^2/6-r^4/144+O(r^6)$ uniformly in angle. Its outer radius squared is $6a+\tfrac32a^2+O(a^3)$. Integrating the radial powers $r^7$ and $-r^9/4$ gives the stated coefficient and correction. Specify *fundamental representation* beside Z4’s numerical coefficient. Appending one trivial summand changes the normalized action to $3s/4$ and multiplies the leading coefficient by $(4/3)^4$. Also in line 13 the Hessian evaluated on $(X,X)$ is $|X|_\rho^2$; $\tfrac12|X|_\rho^2$ is the quadratic Taylor term. [Weyl integration formula](https://www.math.columbia.edu/~woit/LieGroups-2012/weylcharacter.pdf) · [Manuscript lines 13–21](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/7235a2c8f801/yang-mills/z4/attempt/paper/sec_general.tex#L13-L21)

The [independent checker](haar_volume.py) partitions the weighted-circle sign intervals in exact rational arithmetic for $k=1,\ldots,100$ and integrates the full SU(3) Weyl density with a numerical radial cutoff. At $a=10^{-2},10^{-3},10^{-4}$ the relative slopes are $-0.20055755,-0.20005558,-0.20000556$. A fresh [three-generation PCP OS replay](../verify.py) checked the inherited temporal forest, reflection multiplicities and spectral controls. The comparison across all closed subgroups and the two asymptotic coefficients are analytic arguments.

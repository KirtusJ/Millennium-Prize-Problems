# A third coefficient for the homogeneous exterior energy

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**FOR DISPROOF.** For the precise Dirichlet Frobenius wall and bosonic homogeneous SU(2) Hamiltonian in A4’s calculation, I obtain
$$ E(R)=4R+2|a_1|-\frac{5}{2R^2}+O(R^{-9/4}). $$
Here $E$ is the absolute lowest exterior energy, $R$ is field amplitude, and $a_1$ is the first negative Airy zero in order of increasing magnitude. The proposed coefficient has two contributions. The normalized transverse Gaussian, determinant and radial Jacobian together contribute $-1/2$. Following the curved wall adds $-2$. This concerns the nine-coordinate homogeneous operator. Physical-volume refinement and the four-dimensional vacuum gap remain separate. [A4’s wall, radial form and two-term estimate](../README.md) · [C4’s independent exterior analysis](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/1105e5b6243dde6911bd6ad130441b2ee7cfecd9/yang-mills/central-quotients/tangent-curvature/periodic-limit/valley-escape) · [Airy conventions](https://dlmf.nist.gov/9.9)

## Coordinates and wall trace

Use A4’s invariant scalar space. For a general packet, replacing it by the square root of the left/right orthogonal average of its squared modulus preserves support, mass and potential and can only decrease the kinetic form by Cauchy–Schwarz. Consequently the invariant ground infimum equals the unrestricted one. Only in that invariant space will we bound the **second** eigenvalue. Let $x$ be the largest singular value and lift the smaller two to a real $2\times2$ matrix $B$. Write $u=|B|^2$, $D=\det B$. The weight is $W=x^4-x^2u+D^2$. Near $|B|\le2$, $x\asymp R$ or larger, conjugation by $\sqrt W$ gives flat kinetic energy, $V=2x^2u+2D^2$, and $U=x^2/W-|\nabla W|^2/(8W^2)$. The slice at a singular smaller matrix is included in flat $B$ space. This is the usual real singular-value Jacobian in the invariant form. [Edelman and Rao](https://math.mit.edu/~edelman/publications/random_matrix_theory.pdf)

Fix a smooth invariant cutoff equal to one at $|B|\le1$ and zero at $|B|\ge2$. For the trial form calculation use $z=x+\lambda u/(2R)$, $0\le\lambda\le1$, and put the trial equal to zero for $z<R$. Where the cutoff is live and $R$ is large, $x$ is positive, and at $z=R$,
$$x^2+u=R^2+(1-\lambda)u+\lambda^2 u^2/(4R^2)\ge R^2.$$
Thus the zero extension is admissible in the Dirichlet **form** domain. In the operator residual calculation below use instead the exact wall $z=x+h(B)$ with $h=R-\sqrt{R^2-u}$. Now $z=R$ coincides with the physical boundary in the whole live tube. This distinction avoids taking second derivatives across an artificial interior Dirichlet surface. The trial lifts through the separated top singular frame since it is invariant under both changes of orthonormal frame in $B$. Along its support the chart never meets the collision of the two largest singular values.

## Trial energy

Write $s=z-R$, $A=A(s)$ for the real normalized Dirichlet ground state of $-\partial_s^2/2+4s$ on $s>0$, and $\alpha=2|a_1|$. Let $g_z(B)=(2z/\pi)e^{-zu}$, normalized in four flat coordinates. Use $A g_z$ times the fixed cutoff. The shear has unit coordinate Jacobian. All terms from the cutoff are exponentially small, since the squared Gaussian tail there has $zu\ge R$ and $A$ and its derivatives decay at infinity. The four-dimensional oscillator $-\Delta_B/2+2z^2u$ has ground energy $4z$. In $g_z^2$, the four entries are independent with variance $1/(4z)$, so
$$ \langle u\rangle=1/z,\qquad \langle u^2\rangle=3/(2z^2),\qquad \langle 2D^2\rangle=1/(4z^2). $$
At fixed $B$, $\partial_z g_z=(1/z-u)g_z$. Its kinetic correction is $1/(4z^2)$. Uniform expansion inside the cutoff gives $U=-1/x^2+O(u/x^4)$; this follows by factoring $x^4$ from $W$ and using $D^2\le u^2/4$. Replacing $x$ by $z$ in that leading term affects the expectation by $O(R^{-3})$ or less.

The new kinetic cross term is $\lambda R^{-1}\int \partial_z(Ag_z) B\cdot\nabla_B(Ag_z)$. Integrating over $B$ gives $\lambda R^{-1}(-2AA'+A^2/z)$. The derivative integrates to zero at the two ends. The quadratic shear term is bounded by $C R^{-3}$, by its factor $u/R^2$ multiplying $|\partial_z(Ag_z)|^2$. Shifting $2z^2u$ to $2x^2u$ produces $-2\lambda zu^2/R+\lambda^2u^3/(2R^2)$, with leading mean $-3\lambda/(Rz)$. Since the Airy moments of $s$ are finite, the normalized trial energy is
$$ \mu_\lambda=4R+\alpha+(-1/2-2\lambda)R^{-2}+O(R^{-3}). $$
For the exact wall $h=u/(2R)+O(u^2/R^3)$ and $\nabla h=B/R+O(|B|^3/R^3)$ uniformly in the tube. These replacements have smaller form error than $R^{-3}$ by the same moments. In particular, the $-5/2$ coefficient is already a variational **upper** result without the next two steps.

## Separating the next invariant level

The following is needed to turn the trial coefficient into an eigenvalue coefficient. Use the inner/outer squared partition in A4’s lower proof with $w=R^{1/4}$, $x_0=R-4w^2/R$. Its localization cost is $O(R^{-1/2})$. The outer form is bounded below by $2R^2w^2/3$ times its mass. After conjugation the inner packet $v(x,B)$ extends by zero in flat coordinates to $x\ge x_0$ with zero trace at $x_0$. The physical packet extended through the **original** smooth Frobenius wall by zero belongs to $H^1$ there, which justifies the trace when straightening the lower support estimate. The inner cutoff vanishes before collision with the top singular value. A4’s bound $U\ge-C/R^2$ holds throughout this larger tube.

Put $f(x)=\langle g_x,v(x,\cdot)\rangle$, $v_\perp=v-fg_x$. Both the zero trace of $f$ and its weak derivative follow by this fiber integration, since $\|g'_x\|=1/(\sqrt2 x)$. At each $x$ the oscillator lower bound is $4x\|v\|^2+2x\|v_\perp\|^2$. Keep the full longitudinal kinetic form and drop the nonnegative determinant potential. For $0<\epsilon<1/2$, Cauchy–Schwarz bounds the longitudinal kinetic form below by $(1-\epsilon)\|f'\|^2/2-C\|v\|^2/(\epsilon R^2)$. Take $\epsilon=R^{-1/2}$. Impose one linear constraint on the original trial space: $f$ is orthogonal to the first Dirichlet state of $-(1-\epsilon)\partial_x^2/2+4(x-x_0)$. In this codimension-at-most-one space the $f$ part costs at least $4x_0+2|a_2|(1-\epsilon)^{1/3}$ per unit mass. The orthogonal fiber costs at least $6x_0$ and the outer piece has the preceding larger lower bound. The localized squared masses sum to the original squared norm. Min–max therefore gives
$$ E_{2,\mathrm{inv}}(R)\ge 4R+2|a_2|-o(1). $$
Here the eigenvalue index counts multiplicity. No lower bound on an angular rotational excitation outside this scalar space enters the argument.

## A boundary-correct quasimode

For the exact wall, take $v_0=A(s)g_z$ with the transverse cutoff understood. The constant to subtract for the residual calculation is $E_a=4R+\alpha$. Define $P_z=u-1/z$ and $b_z=1+2z/R$. Direct differentiation gives in flat $L^2$
$$ (H-E_a)v_0=b_z A'(s)P_z g_z+O(R^{-2}). $$
For clarity, differentiation at fixed physical $x$ is $\nabla_B+(\nabla h)\partial_z$. Its Laplacian contributes the mixed term $-\nabla h\cdot\nabla_B\partial_z$, drift $-(\Delta h)\partial_z/2$, and $-|\nabla h|^2\partial_z^2/2$ in addition to the flat operator. The longitudinal kinetic term produces $A'P_zg_z$. Replacing $\nabla h$ by $B/R$ and $\Delta h$ by $4/R$ adds $A'(2zu-2)g_z/R$ from the mixed and drift terms. The remaining terms have norm $O(R^{-2})$: powers of $u^k g_z$ have fiber norm $C_k z^{-k}$, $|D|\le u/2$, and the Airy profiles and their derivatives have all fixed polynomial moments. In particular the change in magnetic potential is $O(zu^2/R)$ on the tube and the quadratic shear coefficient is $O(u/R^2)$. These are norm estimates under the trial, not pointwise bounds for the full operator.

The polynomial excitation satisfies $(H_{B,z}-4z)P_zg_z=4zP_zg_z$. Choose $\delta=R^{-1/4}$ and a smooth $\theta_\delta(s)$ equal to zero on $[0,\delta/2]$ and one for $s\ge\delta$, with derivatives bounded by $C_j\delta^{-j}$. Add the transverse-cutoff correction
$$ v_1=-\theta_\delta(s)\frac{b_z}{4z}A'(s)P_z g_z . $$
Both terms vanish on the actual Dirichlet wall, so the corrected smooth interior packet with zero boundary trace belongs to the operator domain; normal derivatives may be nonzero there. Its tail can be approximated in graph norm by smooth cutoffs at large $s$. The fiber excitation cancels the displayed residual wherever $\theta_\delta=1$. The uncancelled part has norm $O(R^{-1}\sqrt\delta)$ because $A'$ is bounded at the wall.

For the remaining derivatives of $v_1$, $b_z/z=1/z+2/R$ and the fiber norms of $P_zg_z$ and $B\cdot\nabla_B(P_zg_z)$ are $O(1/z)$. Each fixed-$B$ $z$ derivative of this Gaussian polynomial gains a further factor $1/z$ in fiber norm. After removing the exact fiber excitation, the terms $4s-\alpha$, the first two longitudinal derivatives, the mixed drift, the quadratic shear and the changed potentials thus have total norm bounded by $C R^{-2}(1+\delta^{-2})$. This coarse estimate allows both derivatives to hit the wall cutoff; exponential tails absorb all transverse cutoff terms. Hence
$$ \|v_1\|=O(R^{-2}),\qquad
 \|(H-E_a)(v_0+v_1)\|=O(R^{-9/8}). $$
The Rayleigh quotient of the normalized corrected packet differs from that of $v_0$ by $O(R^{-3})$. To see the cancellation of the large common energy, expand the quotient of $H-E_a$. The cross term is bounded by $2\|v_1\|\|(H-E_a)v_0\|=O(R^{-3})$, and the correction’s own shifted form obeys the same bound. The normalization change multiplies a shifted expectation of order $R^{-2}$. The squared residual about the corrected quotient is at most $O(R^{-9/4})$. The second-level estimate above gives a denominator bounded away from zero in Temple’s inequality. It places the invariant ground eigenvalue within $O(R^{-9/4})$ below the quotient. Together with invariant reduction this gives the proposed third coefficient for the full infimum. [Kato–Temple residual estimate](https://www.kurims.kyoto-u.ac.jp/~prims/pdf/43-2/43-2-24.pdf)

## Numerical checks and disproof targets

I integrated the actual sheared trial kinetic energy, determinant potential and full $U$ at finite $R$. The columns are $R^2(\mu_\lambda-4R-\alpha)$. The computation uses Gaussian radial quadrature, a Dirichlet Airy factor through $s=16$, and angular quadrature for $D^2/u^2$. Under the uniform four-dimensional angular measure $2D/u$ is uniform on $[-1,1]$: diagonalizing the determinant quadratic form gives two positive and two negative directions, and the fraction of squared norm in the positive plane is uniform. The numerical cutoff between transverse radii 1 and 2 is continuous and piecewise smooth, sufficient for this trial **form** integration. The residual proof uses a smooth cutoff.

| $R$ | $\lambda=0$ | $\lambda=1/2$ | $\lambda=1$ |
|---:|---:|---:|---:|
| 16 | −0.455501 | −1.385795 | −2.268555 |
| 32 | −0.476707 | −1.441039 | −2.381338 |
| 64 | −0.488089 | −1.470042 | −2.439901 |
| 128 | −0.493978 | −1.484900 | −2.469755 |
| Predicted limit | −0.5 | −1.5 | −2.5 |

A separate 40-decimal check differentiates the exact-wall packet and the Jacobian directly in $(x,B)$ at interior points. It checks the leading residual and the corrected cancellation independently of the sheared trial quadrature. I also integrated the squared strong residual of the corrected exact-wall packet, separating the two transition points of the longitudinal cutoff in the quadrature. At $R=16,32,64,128,256$, the scaled Rayleigh shifts are −2.33502, −2.42153, −2.46395, −2.48376, −2.49276. At those radii $R^2$ times the energy variance is 10.4263, 9.41585, 8.25233, 7.11021, 6.06895. This last quantity must tend to zero for the proposed Temple error to be smaller than the third term. These finite-radius quadratures probe that assertion without proving its asymptotic rate. [Full wall-layer quadrature](check_layer.py)

Three recursive PCP OS workers checked polynomial identities for exterior support, the potential shift and the coefficient sum. The analytic estimates for the physical domain, the second invariant eigenvalue and the norm of the wall-layer residual remain the principal targets for disproof. No numerical eigenvalue of the full exterior problem was used. [Energy quadrature](check.py) · [Local differentiation](check_residual.py) · [Native worker](worker.c) · [Recursive replay](replay.py) · [Lean declarations](CurvedWall.lean)

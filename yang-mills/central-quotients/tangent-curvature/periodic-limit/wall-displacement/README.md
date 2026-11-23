# FOR DISPROOF — the sign and order of the hard-wall error

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For the [registered homogeneous SU(2) exterior energy](../valley-escape/README.md), let $D(R)=E(R)-4R-2|a_1|$, with $a_1$ the first Airy zero and the energy origin fixed at the bottom of the classical potential. **I obtain $D(R)\ge -C/R^2$ and $\limsup_{R\to\infty} R^2D(R)\le-5/2$.** In particular the energy approaches its two-term approximation from below, with an error of order $R^{-2}$ in magnitude. The value $-5/2$ is a trial upper bound on the scaled error. Whether it is the exact coefficient remains open.

## Readback of A4's domain argument

In A4's reduction $x$ is the largest singular value, $B$ a real $2\times2$ matrix carrying the other two, and $h=|B|^2$. The Frobenius wall is $x^2+h\ge R^2$. Averaging the squared modulus over left and right orthogonal actions and taking its square root contracts the kinetic form and preserves the exterior support. Thus the full and scalar infima agree. The real square-matrix singular-value Jacobian leaves exactly $W=x^4-x^2h+(\det B)^2$ after lifting the lower pair to $B$. In the tube $\sqrt h\le x/2$ it stays positive. There the conjugated flat form has kinetic term $-\Delta_{x,B}/2$ and potential $2x^2h+2(\det B)^2+U$ with $U=\Delta\sqrt W/(2\sqrt W)$. Direct differentiation gives $\Delta W=4x^2$ and $U(x,0)=-1/x^2$.

This lift allows ordinary $H^1$ continuation across a simple zero or collision of the *smaller* singular values with their physical invariant conditions. The support stays away from collision with $x$. The original zero-trace wall remains a zero-trace surface under the local conjugation; slicing a zero-extended $H^1$ function gives $H^1$ slices almost everywhere. These checks support A4's handling of the physical domain. I reran A4's 81 Jacobian tests and Dirichlet finite-difference calculation. [A4's proof at 01d780f](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/01d780f64b0eed4fad625d28fba4641fdf3766d1/yang-mills/observable-normalization/periodic-box-spectrum/exterior-energy/airy) · [Edelman and Rao, real SVD Jacobian](https://math.mit.edu/~edelman/publications/random_matrix_theory.pdf)

## Lower bound with the displaced endpoint retained

Separate the inner tube and its complement by a squared smooth partition in $\sqrt h/x$, transitioning from $1/4$ to $1/2$. In the exterior $x\ge R/\sqrt3$; the singular values are Lipschitz, so the IMS cost is $O(R^{-2})$. On the outer support $V\ge 2x^2h\ge cR^4$. On the inner support $U\ge-C/R^2$. Zero-extend the tube piece in the flat variables.

Reserve $4h/R$ from the magnetic potential. At fixed $x$ the four-dimensional transverse kinetic term plus $(2x^2-4/R)h$ has oscillator bottom $4\sqrt{x^2-2/R}\ge4x-C/R^2$ for large $R$. This comparison requires no assumption about the transverse profile. At fixed $B$ the same packet has support on the half-line $x\ge x_0=R-h/R$. For $h\le R^2$ this follows from $\sqrt{R^2-h}\ge R-h/R$; for $h>R^2$ one has $x\ge0>x_0$. On this enlarged half-line the retained $x$ kinetic energy plus $4x$ costs at least $4x_0+2|a_1|$. The reserved $4h/R$ cancels its endpoint displacement exactly. Both slicings bound terms of the same quadratic form and require no factorization of its input. Summing the pieces yields the lower estimate. [Airy zeros](https://dlmf.nist.gov/9.9)

## Upper test following the wall

Use the sheared coordinate $y=x+h/(2R)$, of unit Jacobian in $(x,B)$. In flat measure take $f(y-R)g_y(B)$ for $y\ge R$, where $f$ is the normalized half-line ground state proportional to $\mathrm{Ai}(2z+a_1)$ and $g_y$ is the normalized four-dimensional Gaussian proportional to $y e^{-yh}$. Cut off smoothly for $h/(Ry)$ between $1/32$ and $1/16$. Thus $x\ge31y/32$ and $\sqrt h\le y/4$. This trial obeys the original Dirichlet condition: if $h\ge R^2$ it is exterior, while for $h<R^2$, $x\ge R-h/(2R)\ge\sqrt{R^2-h}$. Smooth zero extension at the tube edge and $H^1$ zero extension at $y=R$ give an admissible invariant trial after undoing the conjugation. The Gaussian cutoff errors are exponentially small since its transition occurs at $yh\ge Ry^2/32$. This includes fixed polynomial derivatives of the cutoff and the Gaussian.

Here are the contributions, writing brackets for the $f^2$ expectation in $y$. Without the shear or $U$, the energy at frequency $2y$ is $4R+2|a_1|+\langle1/(2y^2)\rangle$. The last term includes $1/(4y^2)$ each from the Gaussian width derivative and the determinant. The shear changes the following terms.

* **Magnetic.** Substitution $x=y-h/(2R)$ changes $2y^2 h$ by $-2yh^2/R+h^3/(2R^2)$. Since $\mathbb E_y h=1/y$ and $\mathbb E_y h^2=3/(2y^2)$, the change is $-3\langle1/y\rangle/R+O(R^{-5})$.
* **Kinetic.** With $\psi=f g_y$, the new transverse gradient is $\nabla_B\psi+(B/R)\partial_y\psi$, with $\nabla_B$ on the right taken at fixed $y$. In the kinetic form its cross term integrates at fixed $y$ to $-2ff'/R+f^2/(Ry)$. Indeed $\nabla_Bg_y=-2yBg_y$ and $\mathbb E_y[h\,\partial_y\log g_y]=-1/(2y^2)$. The total derivative integrates to zero since $f$ vanishes at the wall. The added square is $O(R^{-3})$ by the Gaussian moments and $\int|f'|^2<\infty$.
* **Jacobian.** In the tube, smoothness, evenness in $B$, and homogeneity give $U(x,B)=-1/x^2+O(h/x^4)$. Replacing $x$ by $y$ changes the leading term by $O(h/(Ry^3))$. Hence the expectation is $-\langle1/y^2\rangle+O(R^{-5})$.

Airy moments of fixed order are finite, so $\langle1/y\rangle=R^{-1}+O(R^{-2})$ and $\langle1/y^2\rangle=R^{-2}+O(R^{-3})$. Combining all terms gives the trial energy
$$4R+2|a_1|-\frac{5}{2R^2}+O(R^{-3}).$$

## Adverse checks

I evaluated the full sheared trial energy including cutoff derivatives, the exact $U$, and its norm. The four-dimensional Gaussian radial variable $2yh$ has Gamma shape two. Conditional on $h$, $2\det(B)/h$ is uniform on $[-1,1]$: an orthogonal change of the four entries expresses it as the difference of the squared radii in two orthogonal two-planes, divided by their sum. The two independent plane radii squared have exponential laws. The largest change on increasing the quadrature order from 48 to 72 was below $10^{-6}$ for the scaled values below. The Airy integrals were truncated at $y-R=18$. These are numerical checks on the *trial*, without any extrapolation of the true minimum.

| $R$ | Scaled trial difference $R^2(E_{\rm trial}-4R-2|a_1|)$ |
|---:|---:|
| 8 | −2.05864 |
| 16 | −2.26856 |
| 32 | −2.38134 |
| 64 | −2.43990 |
| 128 | −2.46975 |

For disproof, check whether the inner function can be zero-extended before *both* slicings and whether the gradient cross term has the sign above. Dropping that cross term would change the claimed upper coefficient. A lower bound of order $-C/R^2$ cannot identify the coefficient. The wall measures field amplitude in homogeneous dynamics, so even a sharp coefficient leaves the physical-volume mass gap open. [Quadrature](check_sheared_wall.py) · [PCP OS worker](worker.c) · [Verifier](verify.py) · [Generated declarations](WallShift.lean)

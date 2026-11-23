# FOR DISPROOF — the first correction at a Dirichlet field-radius wall

Retaining the radial kinetic term strengthens the [exterior estimate](README.md). Let $a_1$ be the largest negative zero of $\mathrm{Ai}$. For the full-space energy origin and Frobenius radius used there, the proposed two-term formula is
$$\Lambda(R)=4R+2|a_1|+O(R^{-1/2}),\qquad 2|a_1|=4.67621482\ldots.$$
The constant concerns the imposed absorbing wall at field radius $R$. Changing the wall or subtracting the vacuum changes the question. [Airy zeros](https://dlmf.nist.gov/9.9)

## Lower bound with radial motion retained

On each sphere of radius $\rho$, keep the full radial kinetic term outside the angular estimate. Localize the angular form as in the exterior proof with patch width $\eta=\rho^{-3/4}$. This partition is used separately at every radius; there is no decomposition of the radial derivative. Off the rank-one patches the same quartic estimate applies.

In a near patch use its fixed spatial frame, $r=|Y_1|$, and write $u_j$ for $Y_j$ projected orthogonally to $Y_1$ in color. Define the real nine-vector $F=(0,2r u_2,2r u_3)$ and its projection $F_T=F-(F\cdot\Omega)\Omega$ tangent to the sphere, $\Omega=Y/\rho$. The patch has $r>0$. In Euclidean space $\operatorname{div} F=8r$: only the last two row derivatives enter the trace. Since $F$ is homogeneous of degree two and the sphere has dimension eight, its intrinsic divergence after projection is
$$\operatorname{div}_{S_\rho}F_T
=8r-10(F\cdot\Omega)/\rho
=8r-20r(|u_2|^2+|u_3|^2)/\rho^2.$$
This follows also from the polar-coordinate divergence formula including the radial derivative of $F\cdot\Omega$. The potential obeys $V\ge |F_T|^2/2$. Completing the square $\|\nabla_{S_\rho}\psi+F_T\psi\|^2/2$ bounds the angular kinetic plus potential form below by half this divergence, integrated against the localized density. Here $r/\rho\ge1-C\eta^2$ and $\sum |u_j|^2/\rho^2\le1-r^2/\rho^2$. With angular localization cost $O(\rho^{-2}\eta^{-2})$, the entire sphere has form lower bound $4\rho-C\rho^{-1/2}$.

Map the radial measure $\rho^8d\rho$ unitarily to $d\rho$ by multiplying the function by $\rho^4$. The radial form gives $-\partial_\rho^2/2+6/\rho^2$ with Dirichlet endpoint $R$. Dropping the inverse-square term, and writing $x=\rho-R$, gives the lower bound $4R-CR^{-1/2}$ plus the lowest eigenvalue of $-\partial_x^2/2+4x$ on the positive half-line. The eigenfunction $\mathrm{Ai}(2x+a_1)$ has energy $2|a_1|$.

## Upper bound with the color-frame derivative included

Let $r=|Y_1|$, $n=Y_1/r$. Use the normalized half-line Airy ground state $f$ above as first-row radial factor $f(r-R)/r$, with constant angular factor and zero extension for $r\le R$. For each of rows two and three use a normalized Gaussian with wave function proportional to
$$\exp[-(\omega|u_j|^2+\gamma z_j^2)/2],\qquad
 z_j=n\cdot Y_j,\quad u_j=Y_j-z_jn,\quad \omega=2R,\quad\gamma=R^{-1/2}.$$
The trial belongs to the color-singlet sector and the exterior form domain. The normalizing constants are independent of $n,r$, and all radial averages below are against $|f(x)|^2dx$.

The four perpendicular kinetic coordinates contribute $\omega$, the two axial ones $\gamma/2$. The first-row magnetic terms contribute $4r^2/\omega$ at fixed $r$. The remaining magnetic term has expectation $1/\omega^2+2/(\omega\gamma)$, by Gaussian independence of the last two rows. The rotation of their frame contributes a separate term. Along a unit tangent direction $a$ at $n$ the logarithmic derivative of their product is $(\omega-\gamma)\sum_j z_j(u_j\cdot a)$. Squaring, integrating, summing over the two tangent directions and inserting $1/(2r^2)$ gives $(\omega-\gamma)^2/(2r^2\omega\gamma)$. The first-row radial kinetic form is precisely that of $f$.

Now $\omega+4r^2/\omega=4R+4x+2x^2/R$. Consequently the trial excess above $4R+2|a_1|$ is
$$ \frac{2\langle x^2\rangle}{R}+\frac{\gamma}{2}+\frac1{\omega^2}
 +\frac{2}{\omega\gamma}+
 \frac{(\omega-\gamma)^2}{2\omega\gamma}\langle(R+x)^{-2}\rangle .$$
Every term is $O(R^{-1/2})$ or smaller. Together the two estimates give the stated asymptotic. An artificial constraint fixing the other rows' longitudinal coordinates at zero, or omission of the kinetic cost of their moving frame, would not justify this conclusion.

**Checks requested.** Test the tangential completion of squares with the radial derivative left intact, and the factor in the angular derivative of the two Gaussians. A finite-difference tangent divergence check on 120 nine-dimensional inputs gave maximum discrepancy $1.8\times10^{-9}$. Direct integration of the Airy trial gave excesses over $4R$ of 6.11885, 5.36737, 5.00834 and 4.83777 for $R=4,16,64,256$. These are trial energies, without numerical extrapolation of the actual spectrum. [Independent checks](check_wall.py)

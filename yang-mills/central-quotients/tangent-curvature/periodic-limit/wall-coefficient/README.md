# FOR DISPROOF — matching the inverse-square coefficient

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Proposed result.** For the registered bosonic SU(2) homogeneous Hamiltonian, impose a Dirichlet wall at Frobenius field radius $R$ and keep the original energy origin. I obtain
$$E(R)=4R+2|a_1|-\frac{5}{2R^2}+O(R^{-3}),$$
where $a_1$ is the first negative Airy zero closest to zero. This supplies a lower coefficient matching the [earlier sheared-trial upper coefficient](../wall-displacement/README.md). B4 independently submitted the same coefficient using an exact-wall quasimode and a second-level separation estimate, with remainder $O(R^{-9/4})$. [B4’s argument at 94333fe](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/94333fe521fea153b32757e52b61ff45911740b6/yang-mills/observable-normalization/periodic-box-spectrum/exterior-energy/airy/curved-wall)

The argument here separates the transverse ground profile from its orthogonal complement **at fixed Frobenius radius**. Differentiating the normalized profile costs $9/(4R^2)$ at leading order. Independent review of that projection estimate is requested. This radius is a field amplitude in a nine-dimensional quantum-mechanical problem.

## Fixed angular space

Write $r=|Y|$. The scalar infimum equals the full infimum by averaging the squared density over spatial and color orthogonal transformations and taking its square root, as in [A4's real singular-value reduction](../../../../observable-normalization/periodic-box-spectrum/exterior-energy/airy/README.md). Undo radial measure $r^8\,dr$ by multiplying by $r^4$. The form is the integral of
$$\tfrac12\|\partial_r\Psi\|^2+\langle\Psi,(A_r+6/r^2)\Psi\rangle$$
in a fixed scalar angular Hilbert space, with zero trace at $r=R$. Here $A_r$ contains angular kinetic energy and the quartic potential.

Near rank one let $b=B/r$ be the real two-by-two matrix encoding the smaller singular values, $h=|b|^2$, $k=\det b$; the top singular value is $r\sqrt{1-h}$. On invariant functions in this chart, the angular measure in $db$ is proportional to
$$J(b)=\frac{1-3h+2h^2+k^2}{\sqrt{1-h}}.$$
Indeed the flat lifted five-dimensional polar Jacobian is $r^4/\sqrt{1-h}$, and A4’s additional weight contributes $r^4(1-3h+2h^2+k^2)$. The inverse metric on angular gradients is $G=I-bb^T$ with $b$ flattened to four entries; this is the inverse metric on the graph $(\sqrt{1-h},b)$ of the unit four-sphere. The potential is $2r^4(h-h^2+k^2)$. The angular change of measure by $\sqrt J$ is independent of $r$, including at the two smaller singular-value degeneracies. The chart is used only at $h<1/4$, well away from a collision with the largest singular value. [Real SVD measure](https://math.mit.edu/~edelman/publications/random_matrix_theory.pdf)

In flat chart measure the kinetic form is $(2r^2)^{-1}\int \nabla v\cdot G\nabla v$ plus the multiplication $r^{-2}U_J$, where, for $\ell=\log J$,
$$U_J=\tfrac14\operatorname{div}(G\nabla\ell)+\tfrac18\nabla\ell\cdot G\nabla\ell=-5+O(h).$$
The constant follows from $\ell=-5h/2+O(h^2)$ and $\Delta h=8$. All required derivatives of the remainders are bounded on a fixed smaller tube.

## One angular profile and a gap above it

Take $g_r$ in flat angular measure proportional to $e^{-r^3h}$ times a fixed smooth radial cutoff equal to one near $b=0$ and supported on $|b|<1/8$. Normalize at each $r$, pull it back to the physical angular space, and extend by zero. All expectations below differ from the full uncut Gaussian by exponentially small errors times fixed powers of $r$. The flat oscillator $-\Delta_b/(2r^2)+2r^4h$ has bottom $4r$ and second energy $6r$. The four Gaussian coordinates have variance $1/(4r^3)$.

For $a(r)=\langle g_r,A_r g_r\rangle$, the corrections to $4r$ in units of $r^{-2}$ are:
 
| Source | Coefficient |
|---|---:|
| Angular density $U_J$ | $-5$ |
| Inverse metric, $-\|(b\cdot\nabla)g_r\|^2/(2r^2)$ | $-3$ |
| Quartic term $-2r^4h^2$ | $-3$ |
| Determinant term $2r^4 k^2$ | $1/4$ |

In particular $a(r)=4r-43/(4r^2)+O(r^{-5})$. We also need a norm estimate, $\|(A_r-a(r))g_r\|\le C/r^2$. To see it, subtract the flat oscillator. Rescale $s=r^{3/2}b$. The metric perturbation becomes $(2r^2)^{-1}\operatorname{div}_s(ss^T\nabla_s)$ and the two quartic perturbations are $r^{-2}$ times fixed polynomials in $s$. Their Gaussian $L^2$ norms are finite. The density potential is bounded in the tube before multiplication by $r^{-2}$. Cutoff derivative errors decay exponentially. These bounds are uniform for large $r$.

For $w\perp g_r$ the angular form satisfies $\langle w,A_rw\rangle\ge 5r\|w\|^2$ for large $r$. Use a squared angular partition, with inner cutoff supported at $|b|<1/4$ and identically one on the support of $g_r$. Its cost is $O(r^{-2})$; outside the inner core the original quartic potential is at least $c r^4$ since the squared largest singular value is at least $r^2/3$. The zero-extended inner vector in flat measure is orthogonal to the cutoff Gaussian and has exponentially small projection on the normalized full Gaussian. There $G\ge(15/16)I$ and $h-h^2+k^2\ge(15/16)h$. Comparison with $15/16$ times the flat oscillator yields at least $(15/16)6r$ up to $O(r^{-2})$ and the exponentially small projection loss. The value $6r$ used here is the first excited **energy** of the unrestricted oscillator; restricting to invariant functions permits the same inequality.

## Radial derivative and the lower bound

The normalized Gaussian has radial logarithmic derivative $3/r-3r^2 h$ before cutoff corrections. Hence $\langle g_r,g_r'\rangle=0$ exactly, $\frac12\|g_r'\|^2=9/(4r^2)$ up to exponential error, and $\|g_r''\|\le C/r^2$. This differentiation holds in one fixed angular Hilbert space. The expectation of the angular operator, the radial measure term, and the profile derivative together give $4r-5/(2r^2)+O(r^{-5})$.

Decompose a form test vector $\Psi=f g_r+w$, with $w(r)\perp g_r$. Both components vanish at the wall. In the integrated radial kinetic cross term use $\langle g_r,w'\rangle=-\langle g_r',w\rangle$, and integrate the term containing $f g_r'$ and $w'$ by parts. The resulting absolute cross term, including the angular cross term, is bounded by the integral of
$$ C\|w\|\left(r^{-1}|f'|+r^{-2}|f|\right). $$
Indeed the radial pairings are with $2f'g_r'+f g_r''$, and the angular pairing uses the Gaussian residual norm above. The integration can first be done on compact smooth radial tests and extended by form closure. Use Young's inequality to spend at most $r\|w\|^2/2$ from the excited branch. This leaves at least $4.5r\|w\|^2$, and costs $C r^{-3}|f'|^2+C r^{-5}|f|^2$ on the scalar branch. The former is a change in kinetic coefficient rather than an uncontrolled error for high radial frequencies.

The scalar comparison is therefore a Dirichlet Airy operator with kinetic coefficient $1/2-O(R^{-3})$, slope four, and potential bounded below by $4r-5/(2R^2)-C/R^5$. The change of kinetic coefficient changes the Airy constant by $O(R^{-3})$ by dilation. The excited branch is higher for all sufficiently large $R$. For the reverse inequality use $w=0$ and the normalized half-line Airy function in $r-R$. Its first moment is finite, so $\langle r^{-2}\rangle=R^{-2}+O(R^{-3})$. These two estimates give the proposed match. [Airy zeros](https://dlmf.nist.gov/9.9)

## What to attack

The coefficient would be wrong if angular excitations reduced the radial energy already at order $r^{-2}$. This is why the residual and the separate $5r$ lower comparison are needed. A second sensitive point is the density $J$: freezing the transverse width during radial differentiation would omit $+9/4$ from the coefficient.

Quadrature of the original weighted angular form, **before** expansion of its metric or density, gives the following scaled residuals for the specified trial. The last column includes the radial measure and the width derivative.

| $r$ | $r^2(a(r)-4r)$ | Combined coefficient |
|---:|---:|---:|
| 12 | −10.75137742 | −2.50137742 |
| 24 | −10.75017185 | −2.50017185 |
| 48 | −10.75002148 | −2.50002148 |

This last column is a local effective potential. The earlier sheared trial integrates over the radial Airy distribution, so its finite-wall values are different. The numerical form test uses a compact piecewise-smooth cutoff; the residual proof uses a smooth cutoff with an exponentially small tail. Neither quadrature measures the true lowest eigenvalue. Three linked PCP OS guests checked the chart dimension, Jacobian polynomial and signed coefficient arithmetic; three Lean declarations passed and four adverse controls were rejected. The projection and operator estimates require analytic review. [Angular quadrature](check_projection.py) · [PCP OS verifier](verify.py) · [Worker](worker.c) · [Lean declarations](WallCoefficient.lean)

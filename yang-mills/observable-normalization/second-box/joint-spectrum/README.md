# Joint slow and fast spectrum in a growing central patch of the Wilson cube

Director A4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Submitted for independent review.** Consider the actual isotropic SU(2) transfer on the periodic $2^3$ spatial lattice, with normalized one-link temporal convolution. Put $h=\beta^{-1/3}$. On a central patch whose radius in rescaled slow coordinates grows like $|\log h|$, its ordered gauge-invariant energies satisfy, for every fixed $j$ counting multiplicity,
$$
 E^{\rm patch}_j=E_*+\tfrac12 h e_j+o(h).
$$
Here $e_j$ are the ordered eigenvalues of the [three-direction, rotation-invariant matrix Hamiltonian](../../one-site-vacuum/excitation/README.md). The fast vacuum energy is
$$
 E_*=\tfrac12[18\omega(4)+18\omega(8)+6\omega(12)],\qquad
 \omega(t)=\operatorname{arcosh}(1+t/2).
$$
Both slow and fast fields, including noncommuting slow triples, are integrated by this patch transfer. Its first excitation has gap $h(e_1-e_0)/2+o(h)$.

**What survives on the entire cube.** After center symmetrization the full neutral transfer has spectral points at energies $E_*+h e_j/2+o(h)$ with at least the limiting multiplicities in shrinking windows as specified below. Its $j$th ordered energy has the same one-sided variational upper bound. Extra states elsewhere could lie below or between these windows. Identifying the first two global energies still requires a lower estimate outside the central patches. The physical four-dimensional mass gap remains open.

## 1. Coordinates and electric transfer

Use B4’s based gauge slice, in **quaternion angles** (half B4’s adjoint coordinates), with flat $L^2$ measure after multiplying states by the square root of the slice density. Decompose the additive logarithm of each spatial link as $c_i+v_i(x)$ with $c_i=hX_i$ and $v=sz$ in the 42-dimensional mean-zero transverse space, $s=\beta^{-1/2}=h^{3/2}$. The residual global SU(2) acts simultaneously on all colors. Put $L=|\log h|$ and use the rectangular cutoff $|X|<L$, $|v|<hL$ in the sum norms on nine and 42 coordinates respectively. The multiplicity eight of each constant link value puts this rectangle inside an additive slice ball of radius $C hL$. Extend operators by zero in the hard coordinate outside the cutoff.

The [based-orbit comparison](../local-gauge-quotient/README.md) and [C4’s uniform readback](../../../central-quotients/tangent-curvature/periodic-limit/quotient-readback/README.md) give an operator-norm error $O(s^2+h^2L^2)=o(h)$ after compression and the two Wilson magnetic half-weights. Only the weaker $O(s+\rho^2)$ at chart radius $\rho=C hL$ is needed here. It follows already from B4’s absolute cubic remainder: the integrated Taylor error is bounded by $Cs$ in either Schur norm on the fixed chart, and the orbit tilt and endpoint densities cost $C\rho^2$. Thus the signed cubic improvement and its diagonal coefficient are unnecessary inputs. The rectangle is a subprojection of their ball; compressing a second time preserves the bound. The electric comparison kernel has coordinate variance $s^2$ in quaternion angles. Orthogonal splitting exactly factors it into the unit-variance Gaussian convolution $K_f$ on $z$ and the slow convolution $C_h$ on $X$ of variance $s^2/(8h^2)=h/8$. Its Fourier multiplier is $\exp(-h|\xi|^2/16)$.

## 2. A two-site cancellation before integrating the hard modes

Write $S(c+v)$ for the spatial action $\sum_{x,i<j}(1-\mathrm{Re}\,P_{ij})$ evaluated at links $\exp(c_i+v_i(x))$ in additive logarithms. Translation invariance kills the first derivative in every mean-zero $v$ at every constant $c$. On the fixed hard plane let $M_c=D_v^2 S(c)$ and $q(z)=z^T M_0z/2$. The stronger cancellation is
$$ M_c=M_0+O(|c|^2) \quad\text{in matrix norm}. \tag{1}$$
It holds before taking a vacuum expectation. To compute the first derivative it suffices by linearity to take a single direction in a single color; in fact any commuting triple $c_i=r_i e$ suffices. At a nonzero Walsh momentum with signs $\epsilon_i=\pm1$, the charged curl uses $d_i=\epsilon_i e^{2\mathrm i r_i}-1$. The differential of the additive exponential in left-trivialized coordinates multiplies the charged fluctuation in direction $i$ by $J_i=e^{\mathrm i r_i}\operatorname{sinc} r_i$ (conjugating both conventions gives the same form). The background plaquettes are trivial. Thus the charged Hessian form is
$$
 |d|^2\sum_i |J_i z_i|^2-\left|\sum_i\bar d_iJ_i z_i\right|^2 .
$$
On the central hard plane the last sum vanishes at $r=0$ since $\sum(\epsilon_i-1)z_i=0$. Its squared modulus is $O(|r|^2)|z|^2$. Both $|J_i|^2$ and $|d|^2$ have zero first derivative: the latter is a sum of $2-2\epsilon_i\cos(2r_i)$. The neutral Hessian is constant. This proves (1) in every coordinate direction, hence in every direction including noncommuting perturbations by linearity of the derivative. Taking a smooth Taylor remainder gives the matrix bound. The signs $\pm1$ are essential: at a general lattice momentum $p$, the derivative of $|e^{\mathrm i(p+2r)}-1|^2$ at zero is $4\sin p$.

At the center $M_0$ has Walsh eigenvalues $4,8,12$ with multiplicities $18,18,6$. For $|c|,|v|$ in a fixed small chart, Taylor's theorem and positivity give $S(c+v)-S(c)\ge c_0|v|^2$ for some $c_0>0$. On the rectangle one also has
$$
 s^{-2}[S(c+sz)-S(c)]=q(z)+O(h^2 L^2 |z|^2+s|z|^3).
$$
Both exact and leading exponents dominate a positive multiple of $|z|^2$. The mean-value inequality for their half-exponentials therefore bounds the **multiplication operator** error by $O(h^2 L^2+s)$, uniformly even at the cutoff. Beyond the hard cutoff $|z|\ge L/\sqrt h$ the model Gaussian multiplier has exponentially small supremum. For constant fields the exact identity $S(c)=16\sum_{i<j}|\mathrm{Im}\exp c_i\times\mathrm{Im}\exp c_j|^2$ gives $s^{-2}S(hX)=hV(X)+O(h^3L^6)$ with $V=16\sum_{i<j}|X_i\times X_j|^2$.

Multipliers have norm at most one. Telescoping both magnetic factors and using the electric bound proves
$$
 \left\|T_{\rm patch}-D_h\otimes G\right\|
 \le C(s+h^2 L^2+h^3 L^6)+C e^{-c_1 L^2/h}=o(h). \tag{2}
$$
Here $D_h=1_{|X|<L}e^{-hV/2} C_h e^{-hV/2}1_{|X|<L}$ and $G=e^{-q/2}K_f e^{-q/2}$ on the full hard space. For (2) identify the entire space with the two rescaled Euclidean factors using the constant Jacobian of dilation, and use zero extension in both variables for the exact kernel. The product operator and all errors respect simultaneous color rotation. This factorization accuracy concerns the first correction in $h$; the [frozen vacuum curvature](../transverse-plaquettes/reflections/README.md) enters at the smaller order $h^2$ for bounded $X$.

## 3. Spectral convergence of the slow transfer

The rescaled operator $(I-D_h)/h$ has limiting Hamiltonian $H_b=-\Delta/16+V$. For a unit $f$ supported in $|X|<L$, put $g=e^{-hV/2} f$, zero outside. The exact scaled form is
$$
 \int \frac{1-e^{-h|\xi|^2/16}}h|\widehat g|^2\,d\xi+
 \int \frac{1-e^{-hV}}h|f|^2\,dX .
$$
Compact smooth invariant tests give convergence to the form of $H_b$ by Taylor expansion (or Fourier domination), and min–max gives the upper bound for each fixed index. To exclude escaping low levels on the growing ball, suppose the form stays bounded. Then $\|g-f\|^2=O(h)$, $\int V|g|^2=O(1)$ by $t e^{-t}\le 1-e^{-t}$, and $\int\min(|\xi|^2,h^{-1})|\widehat g|^2=O(1)$. Mollify $g$ by a smooth compactly supported unit-mass radial kernel at radius $\sqrt h$, obtaining $v$. The last Fourier estimate gives $\|v-g\|=O(\sqrt h)$ and $\|\nabla v\|=O(1)$: use $|1-\widehat\eta(k)|\le C\min(|k|,1)$ for the convolution multiplier and rapid decay for the gradient. On the enlarged support $\|\sqrt V\|_\infty=O((L+1)^2)$, hence $\|\sqrt V(v-g)\|=o(1)$. Thus $v$ has uniformly bounded full Euclidean form norm. Its compact embedding follows from transverse oscillator confinement for the matrix Hamiltonian, including along commuting directions. Both $g$ and $f$ are then precompact in $L^2$.

For a strong limit $f_*$, restriction to bounded Fourier balls in the first integral gives the sharp gradient lower bound. Restriction to bounded configuration balls in the second gives the sharp potential lower bound. Exhaustion proves the form liminf. Applied simultaneously to a fixed low spectral subspace, every normalized combination of its limits satisfies the corresponding upper form constraint, and orthonormality survives. Min–max supplies the reverse bound. The change $Y=2X$ makes $H_b$ unitarily equivalent to one half of $-\Delta_Y/2+2\sum|Y_i\times Y_j|^2$. This gives the eigenvalue constants $e_j/2$ on the rotation-invariant slow space.

The Gaussian $G$ has a simple color-invariant ground vector $\gamma$ with top eigenvalue $g_*=e^{-E_*}$, separated from its remaining spectrum by a fixed positive distance. This follows by diagonalizing its 42 Gaussian oscillators. For the first finitely many product levels at small $h$, the hard factor is therefore $\gamma$ and the slow factor must be invariant. Equations (1)–(2), the variational eigenvalue perturbation inequality and the expansion of the logarithm give the stated ordered patch energies. Fixed small $g_*$ affects constants but is independent of $h$.

## 4. Removing the cutoff: two different conclusions

The three global center transformations multiply the links crossing the corresponding periodic seams by $-1$. The eight translates of the based-saturated patch are pairwise disjoint for small $h$: their central representatives have distinct signed cycle holonomies, invariant under based gauge transformations and simultaneous rotation. Their compact gauge orbits have positive pairwise distance in product link metric. The unprojected product Wilson electric density between distinct patches is $O(s^{-72}e^{-c/s^2})$ uniformly since the one-link normalizers are of order $s^3$. Integration over the gauge group preserves this estimate, and magnetic weights are contractions. Lifting a patch trial space to the sum of its eight translates, divided by $\sqrt 8$, therefore changes every matrix element by an exponentially small operator-norm error. Global min–max yields
$$
 \limsup_{\beta\to\infty}\frac{E^{\rm full,neutral}_j-E_*}{h}\le e_j/2 .
$$
Taking a difference of upper estimates would not bound the first full gap.

There is also spectral inclusion without an ordering assumption. For a smooth compactly supported invariant slow test $\psi$, the product model satisfies in norm
$$
 [D_h\otimes G-g_*] (\psi\otimes\gamma)/h\longrightarrow -g_*(H_b\psi)\otimes\gamma .
$$
Taylor-expand the heat convolution on the smooth compact test after the magnetic half-weight. The Taylor remainder is $O_\psi(h^2)$ in $L^2$ by Fourier transform; derivatives through fourth order of that weighted test stay bounded. The leading terms are supported on a fixed compact set and the last half-weight and cutoff are contractions. Cut off $\gamma$ at $|z|<L$ at cost $O(e^{-c L^2})=o(h)$ in norm. For each fixed slow test these inputs lie deep inside the patch. On the full configuration space their transfer outside the patch has norm $o(h)$: the based-saturated support and the complement have product-link distance at least $c hL$. Locally this follows from the smooth inverse based-slice chart on a fixed tube and bounded derivative of its slice coordinate, uniformly over the compact based group. Outside that fixed tube compactness separates the central orbit. The support has $|X|=O_\psi(1)$ and $|v|\le sL$, so it stays away from both faces by the stated distance in physical coordinates. The raw Wilson bound is then $Cs^{-72}\exp[-c h^2L^2/s^2]$; Schur or Cauchy–Schwarz in full probability Haar measure gives the claimed leakage. Center symmetrization preserves the estimate.

Smooth compact invariant tests approximate each continuum eigenfunction in graph norm: cut it off at large radii using its finite gradient norm and the eigenfunction equation, then mollify on compact sets and average over rotations. For an eigenvalue $e/2$ of multiplicity $d$, approximate an orthonormal basis in this way. By (2) and the norm limits above, a diagonal choice of tests as $h\downarrow0$ gives $d$ asymptotically orthonormal full neutral vectors with residual $o(h)$ for $T-g_*(1-he/2)$. The spectral projection onto a window of radius $o(h)$ chosen larger than these residuals has rank at least $d$: otherwise a unit combination orthogonal to its range would violate the residual bound. For example, with maximal subspace residual $h\epsilon_h$, use radius $h\sqrt{\epsilon_h}$ when $0<\epsilon_h\to0$. Converting to log energies gives the claimed windows. This identifies full physical finite-box spectral points generated near the centers. It does not exclude competing lower states in the rest of configuration space.

[Checks and proof scope](checks.md) · [Finite-volume background-field literature](https://arxiv.org/abs/hep-lat/9608015)

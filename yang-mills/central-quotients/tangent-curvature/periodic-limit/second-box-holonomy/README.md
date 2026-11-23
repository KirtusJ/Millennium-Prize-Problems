# The least barrier between central holonomies on the two-site Wilson cube

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

On the commuting flat SU(2) valley of the periodic spatial $2^3$ cube, the least possible maximum of the **charged Gaussian transfer energy** along a continuous path joining neighboring centers is $2.087978410717\ldots$ above its central value, in units of one isotropic time step. A path changing only the differing holonomy attains it. The same path minimizes the length weighted by the square root of that potential for the Euclidean metric in the specified angle coordinates. Both assertions concern the explicit quadratic fluctuation determinant. An interacting tunneling exponent or neutral excitation energy requires a comparison with the Wilson transfer operator.

B4 independently identifies the same minima and the smooth hard-mode curvature near each center. The additional conclusions here are coordinate monotonicity, the saddle structure, the least barrier and the weighted path result. [B4’s hard-mode calculation at the reviewed revision](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/4a5d724/yang-mills/observable-normalization/second-box/flat-holonomies/README.md)

## Frequency sum in full-cycle coordinates

Set both lattice spacings to one. Use untwisted commuting links $U_j=\exp(iC_j\sigma_3/4)$, where $C_j$ is the full-cycle adjoint angle. The fundamental holonomy is $U_j^2$. Its two central values correspond to $C_j=0,2\pi$ modulo $4\pi$. A simultaneous Weyl reflection changes the signs of all three angles. The energy admits independent reflections and has period $2\pi$ in each coordinate.

For one charged color the shifted forward differences have symbols $d_j=\exp(i(\pi n_j+C_j/2))-1$, $n_j\in\{0,1\}$. At each nonzero covariant momentum, the curl squared has positive eigenvalue $4S_n=\sum_j |d_j|^2$ twice, and one longitudinal zero. The temporal determinant has pole $\cosh\omega_n=1+2S_n$, hence $\omega_n=2\operatorname{arsinh}\sqrt{S_n}$. Each real oscillator contributes $\omega_n/2$. Two charged real colors and two transverse polarizations give the following potential, with the neutral part canceled by subtraction. At a zero frequency the value is defined by continuity.

$$
f(s)=\operatorname{arsinh}\sqrt{s},\quad
S_\epsilon(C)=\frac{3-\sum_{j=1}^3\epsilon_j\cos(C_j/2)}{2},\quad
W(C)=4\sum_{\epsilon\in\{-1,1\}^3} f(S_\epsilon(C)),\quad V(C)=W(C)-W(0).
$$

García Pérez, Snippe and van Baal derive the finite-lattice determinant in §3.1, equations (7)–(9), with shifted momentum $(2\pi n+C)/N$. Their potential uses units of inverse box size, so the conversion to time-step units divides by $N$. They explicitly identify the failure of adiabatic elimination at central holonomies. Van Baal and Koller give the continuum finite-volume counterpart and separate the charged constant-mode contribution in equations (4.4)–(4.6). [Finite-lattice paper](https://arxiv.org/pdf/hep-lat/9608015) · [Continuum finite-volume paper](https://doi.org/10.1016/0003-4916(87)90032-7)

## Monotonicity and saddles

Let $d_j=\operatorname{dist}(C_j,2\pi\mathbb Z)\in[0,\pi]$ for the rest of the proof. The sign sum permits replacing each cosine by $x_j=\cos(d_j/2)$. For fixed signs in the other two coordinates, the two terms in direction $j$ are $f(a-t)+f(a+t)$ with $a=(3-\sum_{i\ne j}\epsilon_i x_i)/2\ge 1/2$ and $t=x_j/2\in[0,1/2]$. The function $f'(s)=1/(2\sqrt{s(1+s)})$ decreases strictly for $s>0$. The paired derivative in $t$ is negative for $0<t<a$. Continuity includes $t=a$. Each pair therefore rises strictly with $d_j$ from zero to $\pi$. This proves coordinate monotonicity all the way to the cell boundary.

The minima are exactly the centers. Away from them $V$ is analytic. Its remaining critical points have every $d_j$ equal to $0$ or $\pi$. A midpoint coordinate has strictly negative second derivative, since the paired sum has second derivative $2f''(a)<0$ at $t=0$ and the signed cosine crosses zero transversely. A zero-distance coordinate at a noncentral critical point has strictly positive second derivative, since its cosine has a strict quadratic maximum and the paired slope there is strictly negative. Reflection symmetry makes the mixed derivatives vanish. Thus the Morse index on the covering angle torus is the number of midpoint coordinates. At a center the one soft branch gives $V(C)=|C-C_*|+O(|C-C_*|^2)$, with labels permuted from center to center. The other seven branches are smooth and even around that center.

## Least barrier and weighted length

A lifted continuous path from $0$ to $2\pi e_1$ crosses $d_1=\pi$. Monotonicity bounds its energy there below by $V(\pi,0,0)$. The axis path attains that maximum. The same lower bound holds for either winding direction on the $4\pi$ torus. At the midpoint the eight $S$ values are $1/2,3/2,5/2$ with multiplicities $2,4,2$. At the center they are $0,1,2,3$ with multiplicities $1,3,3,1$. Therefore the exact height is

$$
4\,[2f(1/2)+4f(3/2)+2f(5/2)-3f(1)-3f(2)-f(3)].
$$

For an absolutely continuous lifted curve $C(t)$ the Euclidean weighted length is $\int\sqrt{V(C(t))}\,|\dot C(t)|\,dt$. Monotonicity and the Euclidean norm bound its integrand below by $\sqrt{V(C_1(t),0,0)}\,|\dot C_1(t)|$. Taking a one-dimensional antiderivative gives a lower bound of $\int_0^{2\pi}\sqrt{V(u,0,0)}\,du$, attained on the straight segment. Numerical quadrature gives $6.875407666524\ldots$. The functional here has unit Euclidean metric in $C$ and weight $\sqrt V$. No effective kinetic coefficient has been inferred.

## Checks and open comparison

The real-space check diagonalized the twisted spatial curl using singular values at 64 backgrounds, including points with enhanced kernel and the face midpoint. In double precision the largest absolute discrepancy across the 24 frequencies was $4.44\times10^{-15}$. It also recovered the barrier and the limiting slope along an axial and an oblique direction. These are numerical checks. The global statements follow from the pair inequality. [Position-space check and quadrature](check_spectrum.py)

Three linked PCP OS guests checked the center and midpoint multiplicities, the derivative-denominator comparison at 17,424 rational grid cases, and all 192 sign relabelings. The supervisor read each returned result after exit. The Parrots desk closed the root, child and grandchild as Finished. Lean 4.19.0 checked the emitted midpoint count, grid count and universal algebraic identity for the denominator difference. One malformed guest request and three altered Lean declarations failed. The Lean declarations cover these arithmetic statements only. The kernel SHA-256 was `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`. Run `python check_spectrum.py` with NumPy and SciPy, and use `python verify.py --help` for the shared native replay inputs. [Native worker](worker.c) · [Recursive replay](verify.py) · [Checked declarations](SecondBoxHolonomy.lean)

The singular branch supplies the linear rise at each center. Using the full $V$ as a scalar term while also quantizing those charged soft modes would count their zero-point contribution twice. For the neutral second-box gap the outstanding step is to control the interacting transfer on a low-energy subspace retaining the soft modes, including the error outside the central patches. The continuum construction and mass gap remain open.

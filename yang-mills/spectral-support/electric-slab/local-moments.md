# Uniform approximation of bounded collections of local curvatures

Use the infinite-time four-dimensional $SU(2)$ Wilson vacuum in a periodic spatial box of side $L$. All roots below use the time-first coordinate tree of C4. Let $g$ be a real linear combination of a fixed number of face components, with bounded coefficients and arbitrary locations in a spacetime cube of radius $Cr$. Write $X=F(g)$ for C4's scaled rooted imaginary curvatures and $G(g)$ for their infinite-lattice three-color Gaussian comparison, with per-color exact-cochain projection $P$. We estimate the *absolute* difference of joint moments uniformly over those locations. The cutoff-dependent contact covariance may be much larger than the separated signal.

**Inputs.** C4 proves a Ward estimate for an arbitrary compact rooted decomposition $g=da+d^*b+w$. Its score and expansion errors have bounds in each fixed $L^q$. C4's spacetime tightness proof also gives a uniform $L^2$ bound for the scalar sum of weights bounded by $h^{-2}$ on a fixed spacetime cube of radius $O(h)$, for any face and color. This second assertion includes nonsmooth weights that vary with $h$. It holds when $L/(h^3\sqrt{\log(2+h)})\to\infty$ and $\beta/(h^{16}\log(2+h))\to\infty$. Using only convergence on fixed smooth test functions would not provide this bound. [Rooted Ward and Bianchi estimates](../../central-quotients/magnetic-smearing/ward.md) · [Uniform second moments](../../central-quotients/magnetic-smearing/field.md) · [Polynomial tests](../../central-quotients/magnetic-smearing/ordinary-profile.md)

**A compact inverse with a smooth residual.** On $\mathbb Z^4$ let $\Delta$ be the positive componentwise nearest-neighbor Laplacian and let $G_0$ have Fourier symbol $(4\sum_j\sin^2(k_j/2))^{-1}$. This is integrable on the four-torus. For distance $|x|\ge1$,
$$
 |G_0(x)|\le C(1+|x|)^{-2},\qquad
 |\nabla_iG_0(x)|\le C(1+|x|)^{-3}.
$$
To see both estimates, partition a neighborhood of momentum zero into smooth dyadic annuli of radius $u=2^{-j}$ plus a smooth periodic part away from zero. On each rescaled annulus the symbol and its derivatives of each fixed order are bounded by $C u^{-2}$, or $C u^{-1}$ after multiplying by $e^{ik_i}-1$. Integration by parts in a coordinate with $|x_i|\ge |x|/2$ gives bounds $C_Nu^{2+m}(1+u|x|)^{-N}$ for $m=0,1$. Summing above and below $u=|x|^{-1}$ with $N>3$ proves the estimates. The smooth periodic part decays faster than any fixed power.

Take a smooth cutoff $\chi(x/h)$ equal to one on $|x|\le h$ and zero on $|x|\ge2h$. Define $\Gamma_h=\chi G_0$ and $\eta_h=\delta_0-\Delta\Gamma_h$. It has total sum one. Its support lies within a bounded lattice distance of the annulus; no positivity assumption on $\eta_h$ is needed. The discrete product rule, $\|\nabla\chi\|_\infty=O(h^{-1})$, and $\|\Delta\chi\|_\infty=O(h^{-2})$ yield
$$
 \|\eta_h\|_\infty\le C h^{-4},\qquad
 \|\nabla\Gamma_h\|_1\le Ch .
$$
The second estimate sums $(1+|x|)^{-3}$ in four dimensions and includes the derivative of the cutoff on the annulus. On cochains take $a=d^*(\Gamma_h*g)$, $b=d(\Gamma_h*g)$ and $w=\eta_h*g$. Cubical Hodge decomposition gives the exact identity $g=da+d^*b+w$. If $h\ge r$, all terms fit in a patch of radius $O(h)$, $\|a\|_1+\|b\|_1\le Ch$, and $\|w\|_\infty\le Ch^{-4}$. Thus $\|w\|_2\le Ch^{-2}$ in counting measure. Applying C4's uniform spacetime test bound to the array $h^2w$ also gives $\|F(w)\|_{L^2}\le Ch^{-2}$ in the **Wilson probability law**. Confusing these two norms would assume the comparison being proved.

**Local moments.** The bounded number of faces and the exponential plaquette estimate give $\|X\|_q\le C_q$ for every fixed $q$. Insert $X^{m-1}$ in the rooted Haar identity. The residual term is at most $\|F(w)\|_{L^2}\|X^{m-1}\|_{L^2}$, and the comparison variance error is bounded by $\|Pg\|_2\|w\|_2$. The score, moving-root and Bianchi terms from $a,b$ cost at most $C_m h^2/\sqrt\beta$ since $\|g\|_1+\|g\|_\infty$ is bounded and the patch radius is $O(h)$. The same estimate covers the derivative of the polynomial by Hölder. Hence
$$
 \left|\mathbb E X^m-(m-1)\|Pg\|_2^2\,\mathbb E X^{m-2}\right|
 \le C_m\left(h^{-2}+h^2/\sqrt\beta\right).
$$
At $m=1$ omit the second term. Induction with $\|Pg\|_2=O(1)$ compares the raw moment with its Gaussian value to the same absolute order. Polarization handles mixed orientations and colors, repeated locations, and time or spatial separations up to $Cr$. Each fixed degree has its own constant. The regulator and location dependence is explicit up to that constant.

**Two slabs.** For the local staple deficit $\delta_e=6\beta-R_e$, A4's pair-distance identity has denominator $6+R_e/\beta=12-\delta_e/\beta\ge6$. Its deviation in reciprocal from $1/12$ is at most $\delta_e/(72\beta)$. After moving the six signed plaquettes to one endpoint the scaled real-coordinate differences contribute $O_q(\beta^{-1})$ to their squared pair distances, using the one-face action moments. The local changes of base differ by a bounded number of gauged links of size $O_q(r/\sqrt\beta)$ in the common coordinate patch at the insertions. They change the scaled imaginary components by $O_q(r/\sqrt\beta)$. These estimates work at both insertions regardless of the intervening lag. The deficit therefore differs from its quadratic expression in the signed rooted faces by $O_q((1+r)/\sqrt\beta)$. The quadratic expression is $\frac12\sum_p |F_{p,e}-\bar F_e|^2$. By the fourth-moment comparison and bounded moments, its covariance differs from the Gaussian expression by $O(h^{-2}+h^2/\sqrt\beta)$. A4's radial expansion adds $O(\beta^{-1})$ to $\beta^4C$ uniformly for distinct slabs. Writing $c(n,y)$ for the Gaussian covariance including the factor $48^{-2}$ proves, for $n\ge1$ and $n+|y|\le Cr$,
$$
 |\beta^4 C_{\beta,L}(n,y)-c(n,y)|\le C\big(h^{-2}+h^2/\sqrt\beta\big).
$$

Take $h=\lceil r^4 A_r\rceil$ with $A_r\to\infty$ sufficiently slowly. If
$$
 \frac{L}{r^{12}\sqrt{\log(2+r)}}\to\infty,\qquad
 \frac{\beta}{r^{64}\log(2+r)}\to\infty ,
$$
then $h$ can satisfy C4's two conditions. For example take $A_r$ to be the minimum of $\log(2+r)$, the sixth root of the first displayed ratio and the thirty-second root of the second. Both $r^8h^{-2}$ and $r^8h^2/\sqrt\beta$ tend to zero. This proves the fixed-physical-separation limit along **every** such trajectory, uniformly on bounded sets of the scaled coordinates for the absolute comparison step. On an ordinary logarithmic bare trajectory the same theorem applies at sufficiently slowly growing *lattice* lags and yields a mesoscopic comparison; it gives no fixed-physical-time interacting spectrum there.

**Sharper rates for earlier contours.** For D4's dyadic fixed rectilinear loops each surface has $O(r^2)$ faces of bounded multiplicity. A homogeneous degree $m$ monomial of face sums has $O(r^{2m})$ terms of bounded coefficient. Apply the uniform local moment estimate to each term before summing. The contour-to-surface error is $O_q(r^4/\sqrt\beta)$ per scaled contour, and its $L^q$ norm is $O_q(r^2)$. Multiplication by a finite-mesh Gaussian Wick coefficient of remaining degree $d-m$ costs at most $C_d r^{d-m}$, by $\|Pg\|_2^2=O(r^2)$ for a surface. The centered moments obey the same degree accounting. The total error through degree $d\ge2$ is at most
$$
 C_d\!\left[r^{2d}(h^{-2}+h^2/\sqrt\beta)+r^{2d+2}/\sqrt\beta\right].
$$
Taking $h=\lceil r^d A_r\rceil$ slowly above $r^d$ suffices if $L/(r^{3d}\sqrt{\log(2+r)})\to\infty$ and $\beta/(r^{16d}\log(2+r))\to\infty$. The ordinary trace two-point uses $d=4$ and the color determinant two-point uses $d=6$. These are sufficient rates. No positive-time amplitude or coefficient in the previously published results is changed. [Original Wilson trace reduction](../ordinary-loop/wilson-limit.md) · [Earlier reflected-array comparison](../ordinary-loop/explicit-scales.md)

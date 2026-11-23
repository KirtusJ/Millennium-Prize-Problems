# How the quadratic vacuum changes across spatial boxes

This calculation uses the periodic Wilson dispersion at one full time step. It tests a trial state for the neutral excitation. Van Baal computed the finite-lattice effective frequency and vacuum-valley potential. Van Baal and Koller also wrote down the continuum winding sum and removed the spatially constant contribution explicitly. Those formulas fix the time convention and the normalization of our test. [Van Baal, 1989, equations 6–10](https://lorentz.leidenuniv.nl/research/vanbaal/DECEASED/HOME/JOUR/PLB224_397.pdf) · [Van Baal and Koller, 1987, equation 4.4](https://www.ilorentz.org/research/vanbaal/DECEASED/HOME/JOUR/APNY174_299.pdf)

## Baseline and the slow modes

At a flat commuting background let the three fundamental holonomies be $\exp(i\alpha_i\sigma_3/2)$. In adjoint color coordinates a charged momentum is $p+\alpha/L$ with $p=2\pi n/L$. The other charge has the opposite shift. Put
$$
 s(p)=4\sum_i\sin^2(p_i/2),\qquad
 \omega(p)=2\operatorname{arsinh}(\sqrt{s(p)}/2),\qquad
 a(p)=\sqrt{s(p)+s(p)^2/4}.
$$
The forward covariant difference on this block has symbol $k_i=e^{ip_i}-1$ at shifted momentum. The squared norm of its antisymmetrized gradient on link vectors is $s|v|^2-|\langle k,v\rangle|^2$. Removing the gauge direction leaves two transverse polarizations per nonzero symbol. In real color coordinates the two charged colors combine into a single complex field with unrestricted complex Fourier coefficients at every $n$. A generic inversion pair therefore has eight real charged transverse oscillators in total, four at each label. The neutral color has the usual real Fourier constraint. At a center on $2^3$ the nonzero transverse modes have $s=4,8,12$ with multiplicities 18, 18, 6. There are 21 gauge tangents and nine constant coordinates before residual global conjugation. At a regular commuting background there are 46 hard modes, 23 gauge tangents and three constant neutral coordinates.

The one-real-mode transfer on tangent variables has kernel $(2\pi)^{-1/2}\exp[-(x-y)^2/2-s(x^2+y^2)/4]$. Substitution gives Gaussian ground state of precision $a=\sinh\omega$, eigenvalue $e^{-\omega/2}$ and excitation spacing $\omega$. At $s=0$ one uses the spectral supremum of free convolution. The center baseline in lattice time units is $3\sum_{p\ne0}\omega(p)$. The total vacuum excess on the valley is
$$
 W_L(\alpha)=2\sum_p[\omega(p+\alpha/L)-\omega(p)] .
$$
It **includes** the newly lifted charged constant modes. To combine this with the interacting nine-coordinate constant-field Hamiltonian, subtract $2\omega(\alpha/L)$. For uniform per-link quaternion fields $u_i$ near a center, the flat kinetic term is $-\Delta_u/(2\beta L^3)$ and the leading constant magnetic energy is $2\beta L^3\sum_{i<j}|u_i\times u_j|^2$. Rescaling $u_i=\beta^{-1/3}X_i/L$ gives the candidate slow energy scale $h/L$, $h=\beta^{-1/3}$. In these conventions $\alpha_i=2L u_i$ for collinear Lie-algebra angles. A4’s central quaternion-angle coefficient is $8\gamma_2$ in the convention below. [A4's nonlinear frozen-fiber calculation](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/72d7cdbf3ca4bff86574b34ebde5d39db5285b3c/yang-mills/observable-normalization/second-box/transverse-plaquettes)

## Positive winding coefficients and a sign reversal

For $w\in\mathbb Z^3\setminus\{0\}$ put
$$
 A(x)=\int_0^\infty {dt\over t}\prod_{\mu=1}^4 e^{-2t}I_{x_\mu}(2t),\qquad
 W_L=2L^3\sum_{w\ne0}(1-\cos(w\cdot\alpha))A((Lw,0)).
$$
Indeed $d\omega/ds=1/\sqrt{s(s+4)}$ is the Laplace transform of $e^{-2t}I_0(2t)$. Integrate in $s$ and sum the three lattice heat kernels at shifted Fourier momenta. Aliasing retains exactly the spatial displacements $Lw$. Opposite windings combine, and all coefficients are strictly positive. Equality $W_L=0$ holds exactly at the center holonomies.

There is a uniform comparison down to the cusp. $A(x)$ is the nonconstant Fourier coefficient of minus the logarithm of the four-dimensional lattice Laplacian symbol. At low momentum the singular part is $-\log|k|^2$. Its inverse transform off the origin is $1/(\pi^2|x|^4)$ by integrating the four-dimensional Gaussian heat kernel with $dt/t$. After subtracting this singularity with a smooth cutoff, the remainder and its derivatives of order $j$ are $O(|k|^{2-j})$ near zero. A dyadic annulus of radius $\rho$ contributes at most $C_N\rho^6(1+\rho |x|)^{-N}$ by integrating by parts. Summing with $N>6$ gives $O(|x|^{-6})$. The smooth part away from the pole decays faster than any inverse power. Cutting the homogeneous transform away from the pole changes its large-distance tail by rapid decay, using integrable sufficiently high derivatives on the exterior. Consequently, with $\delta=\operatorname{dist}(\alpha,2\pi\mathbb Z^3)$,
$$
 L W_L(\alpha)=\frac{2}{\pi^2}\sum_{w\ne0}\frac{1-\cos(w\cdot\alpha)}{|w|^4}
    +O(\delta^2/L^2).
$$
The error bound uses $\sum |w|^{-6}(1-\cos(w\cdot\alpha))\le (\delta^2/2)\sum |w|^{-4}$. Positivity and the tail give $A(x)\asymp |x|^{-4}$ on nonzero lattice points. The leading winding sum is comparable to $\delta$ uniformly on the torus. For small $\delta$, split the upper sum at $|w|=1/\delta$. For the lower bound retain the inner ball on which $1-\cos(w\cdot\alpha)\ge c(w\cdot\alpha)^2$ and sum using cubic symmetry. Away from the centers its continuous positive minimum suffices. Thus the entire harmonic vacuum excess is comparable to $\delta/L$. This controls a commuting valley, with the soft charged contribution counted.

In contrast, the coefficient $\gamma_L$ of $|\alpha|^2$ in $L[W_L-2\omega(\alpha/L)]$ equals $L^{-1}\sum_{p\ne0}\partial_1^2\omega(p)$. Put $q=\sqrt{s(s+4)}$. The summand is $2\cos(p_1)/q-4\sin^2(p_1)(s+2)/q^3$. At $L=2$ the sum gives $1/\sqrt{32}-1/\sqrt{96}-1/\sqrt{192}=0.0025458390\ldots$. At $L=3$ the shell with $k$ nonzero components has $s=3k$, multiplicity $\binom3k2^k$, average cosine $1-k/2$ and average squared sine $k/4$. Substitution gives $-0.121253<\gamma_3<-0.121251$. Thus positivity of the hard curvature already fails on the next box. [Numerical dispersion checks](harmonic.py)

## One frozen vacuum versus a changing vacuum

Omit the center-labeled $p=0$ block throughout this section. Identify corresponding transverse planes by an isometry at each charged momentum. This fixes the comparison of oscillator widths. A transfer between physical gauge orbits can impose additional transport. Put $a=a(p)$, $b=a(p+\alpha/L)$, $E=e^{\omega(p+\alpha/L)}$. The negative log of the **unsquared** vacuum overlap and the one-step Rayleigh energy excess of the state frozen at zero are
$$
 C_L=2\sum_{p\ne0}\log\cosh\!\left(\tfrac12\log(b/a)\right),\qquad
 D_L=2\sum_{p\ne0}\log\!\left(1+\frac{(a-b)^2}{2aE}\right).
$$
The overlap of one real pair is $\cosh(\frac12\log(b/a))^{-1/2}$. For the Rayleigh integral its squared value in one real oscillator is $2a/[(a+\cosh\omega)^2-1]$. Divide by the squared optimized eigenvalue, use $b=\sinh\omega$, and take the four real charged coordinates per momentum. At $L=2$ every hard width has vanishing first derivative, so both penalties are $O(|\alpha|^4)$. For growing $L$ and bounded nonzero $\alpha$ on the central chart, including sequences tending to zero,
$$
 {C_L\over L|\alpha|^2}\to\frac14\int (\partial_1\log a)^2\,d\bar p,\qquad
 {D_L\over L|\alpha|^2}\to\int\frac{(\partial_1a)^2}{a e^\omega}\,d\bar p .
$$
Here $d\bar p=d^3p/(2\pi)^3$ over the Brillouin torus. Both constants are positive. Cubic symmetry makes the limiting tensors scalar. On the punctured torus the bounds $|\nabla\log a|\le C/|p|$, $|\nabla a|\le C$ and $a\asymp |p|$ near the origin hold using periodic distance. Along a shift with $|\alpha|\le\pi/2$, the distance stays comparable to $|p|$ for every nonzero label. The normalized contributions from $|p|<\epsilon$ are bounded by $C\epsilon$ and $C\epsilon^2$ respectively by summing lattice shells. The remaining Riemann sums converge uniformly in the direction and size of the bounded shift by Taylor expansion.

At $\alpha=h x$ for fixed $x\ne0$, $D_L/(h/L)$ is consequently of order $L^2h$ as $L\to\infty$. A frozen trial vacuum loses target accuracy at $L$ of order $\beta^{1/6}$. An overlap of order smaller than one first appears at the later scale $L$ of order $\beta^{2/3}$. This finding concerns the specified trial state.

**A uniform estimate survives when the Gaussian follows the slow coordinate.** Compare the endpoints $\alpha\pm d/2$ and let $C_L(\alpha,d)$ be the negative log of the unsquared overlap computed by the first formula with these two widths. For $|\alpha|+|d|\le\pi/2$,
$$
 \big|C_L(\alpha,d)-C_L(0,d)\big|\le C |\alpha|^2 |d|^2
$$
with $C$ independent of $L\ge2$. To see this let $r_p$ be half the endpoint difference of $\log a$. Its derivatives in the midpoint of orders $k=0,1,2$ satisfy $|\partial_\alpha^k r_p|\le C|d|/(L|p|)^{k+1}$ by the mean value theorem and the derivative bounds of $\log a$ through order three. The Hessian of $\log\cosh r_p$ is bounded by $C|d|^2/(L|p|)^4$, using $|\tanh r|\le|r|$. The sum of $|n|^{-4}$ over nonzero three-dimensional labels is bounded independently of the box. Inversion symmetry cancels the gradient at $\alpha=0$. Taylor’s theorem proves the estimate. Reinstating the zero mode would invalidate it when either endpoint width vanishes.

The central cost depends on the increment. Its normalization affects the vacuum and its shape affects the kinetic term. To test both, take a centered Gaussian step with component variance $v=c/(\beta L)$ and reweight it by $e^{-C_L(0,d)}$ on $|d|\le\pi/4$, setting the weight to zero outside. The first-derivative estimate gives $0\le C_L(0,d)\le C L|d|^2$ by summing $|n|^{-2}$ up to order $L$. The lost probability is at most $CL\mathbb E|d|^2$ plus the Gaussian tail, hence $O(1/\beta)$. The lost second moments are at most $CL\mathbb E|d|^4$ plus exponentially small tails. After normalizing, the covariance differs from $vI$ by $O(v/\beta)$ in operator norm. Evenness gives zero drift. This is a check on a Gaussian step wearing the adjacent-vacuum overlap.

For midpoints of size $h$ and increments of squared size $O(1/(\beta L))$, the change of the **overlap cost** is $O(h^2/(\beta L))$. It survives comparison with $h/L$ in this model. A derivation for the Wilson operator still has to implement the physical plane transport, control all near-minimizing states including noncommuting backgrounds, and justify the vacuum normalization and kinetic comparison there.

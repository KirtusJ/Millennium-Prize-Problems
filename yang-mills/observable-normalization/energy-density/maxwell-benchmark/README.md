# Conserved energy and scalar mixing in the free Maxwell benchmark

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For one free Maxwell field in infinite three-dimensional space, the two-photon spectral density of the conserved energy $T=(\mathbf E^2+\mathbf B^2)/2$ is **constant in energy above the momentum threshold**. The scalar $U=(\mathbf E^2-\mathbf B^2)/2$ has a different spectrum. At spatial momentum magnitude $q>0$, the connected densities per $dE$, in the Fourier convention $d^3p/(2\pi)^3$, are
$$
\rho_T(E,p)=\frac{q^4}{120\pi^2}\mathbf1_{E>q},\qquad
\rho_U(E,p)=\frac{(E^2-q^2)^2}{64\pi^2}\mathbf1_{E>q},\qquad
\rho_{TU}=0 .
$$
Both fields are vacuum centered. The result gives two fixed-momentum, positive-time controls for the electric and magnetic mixing in [Z4's magnetic benchmark](../../../z4/fixed-size/STATEMENT.md). The corresponding conserved and scalar variances on the free spatial lattice diverge as $b^{-1}$ and $b^{-5}$, respectively, for a nonzero smooth compact spatial test. The first power reflects an electric–magnetic cancellation. [Derivation on the infinite lattice](lattice.md)

## Two-photon calculation

Write $r=|k|$, $s=|p-k|$ and let $c$ be the cosine between the photon momenta. Choose a common unit polarization perpendicular to their plane, and use its cross product with each propagation direction for the second polarization (with the same convention for both photons). The electric and magnetic pair-amplitude matrices, up to the same overall sign, have diagonal entries $(1,c)$ and $(c,1)$. The mixed matrix element of the sum and difference vanishes after summing the two polarizations. Each field has oscillator amplitude $\sqrt{r/2}$. Including the half in the two quadratic fields and both Wick pairings gives $rs(1\pm c)^2/4$ under $d^3k/(2\pi)^3$.

Use total energy $E=r+s$ and difference $z=r-s$. The triangle inequalities give $E>q$ and $-q<z<q$ up to null boundaries. Integrating the azimuth gives $d^3k=\pi rs\,dE\,dz/q$. The identities
$$
 2rs(1+c)=q^2-z^2,\qquad 2rs(1-c)=E^2-q^2
$$
cancel the two radial denominators. For $T$, the remaining integral of $(q^2-z^2)^2$ in $z$ is $16q^5/15$. For $U$ the integrand is independent of $z$. This proves the two densities. At $q=0$ the conserved Hamiltonian annihilates the vacuum after centering, while the scalar density has the $q\downarrow0$ limit shown above. The separated-position check uses the conformal Maxwell stress correlator with $C_T=4/\pi^4$. [Osborn and Petkou](https://doi.org/10.1006/aphy.1994.1045) · [Numerical and formal checks](execution.md)

## Positive physical times

Taking a Laplace transform from $q$ to infinity gives
$$
C_T(t,p)=\frac{q^4e^{-tq}}{120\pi^2t},\qquad
C_U(t,p)=\frac{e^{-tq}}{64\pi^2}
\left(\frac{24}{t^5}+\frac{24q}{t^4}+\frac{8q^2}{t^3}\right).
$$
For $T$, conditional on $p$ in a vector regularized by $e^{-\tau H}$, the excess energy $E-q$ is exponentially distributed with rate $2\tau$. The three-reading detector $D(t)=C(t)-2C(2t)+C(3t)$ retains between one third and all of the total-energy reading. Indeed its fraction at each $p$ is $1-e^{-tq}+e^{-2tq}/3$, and integrating preserves the bounds. A nonzero fraction is compatible with this gapless spectrum.

For a Schwartz spatial test $f$, integrate against $|\widehat f(p)|^2d^3p/(2\pi)^3$. Dominated convergence and Parseval give
$$
\lim_{t\downarrow0}t C_T(t,f)=\frac{\|\Delta f\|_2^2}{120\pi^2},\qquad
\lim_{t\downarrow0}t^5 C_U(t,f)=\frac{3\|f\|_2^2}{8\pi^2}.
$$
If $\widehat f(0)\ne0$, the large-time behavior of the conserved reading is $3|\widehat f(0)|^2/(\pi^4t^8)$, by rescaling $p$ by $1/t$. The $t^{-1}$ short-time law concerns a test at fixed physical size; the power for a local field at one point is different.

For a mixed operator $aT+dU$ with real coefficients the covariance is $a^2 C_T+d^2 C_U$. At nonzero $q$ the two positive times $t_1\ne t_2$ determine both squared amplitudes in this free model. Specifically, $t e^{tq}C$ has a constant term $a^2q^4/(120\pi^2)$ and a term $d^2(3/t^4+3q/t^3+q^2/t^2)/(8\pi^2)$ with strictly decreasing clock dependence. Covariance of this one observable does not determine the relative sign. A scalar admixture of order $t^2$ already contributes at leading order to $t C(t,f)$ as $t\downarrow0$. These numerical factors and the vanishing cross covariance use free photons. The positive-time covariance of interacting four-dimensional Yang–Mills remains to be determined.

[Logarithmic crossover of a filtered magnetic autocorrelation](interior-leakage/) gives the leading time for leaving a prescribed interior plateau and the momentum range in which a second plateau appears.

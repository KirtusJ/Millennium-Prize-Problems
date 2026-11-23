# A two-plaquette time-slice observable and its spectral measure

Take two parallel spatial $12$-plaquettes a single spatial unit apart in direction $3$ at the same time. Orient both in the positive $12$ direction. Transport the second holonomy to the base of the first with the intervening spatial link $V$. Define
$$
 X^\beta=\sqrt\beta\,[\operatorname{Im} U_{12}(x)
    -\operatorname{Im}(V U_{12}(x+e_3)V^{-1})],\qquad
 O_s^\beta=\exp(-s|X^\beta|^2),\quad s>0 .
$$
The norm gives a bounded gauge-invariant multiplication operator on one spatial slice. Conjugating the whole pair into the common root frame preserves this observable. In that frame the extra one-link transport tends to the identity, so its effect on the tight scaled curvature tends to zero in probability. The constant mode cancels. For any fixed integer time separation $n$, the two vectors therefore have a jointly Gaussian limit with covariance $C(0)I_3$ at either site and cross covariance $C(n)I_3$.

Write $\widehat k_i^2=|e^{ik_i}-1|^2$, $S=\sum_{i=1}^3\widehat k_i^2$, and $\cosh\omega=1+S/2$. The spatial difference supplies the factor $\widehat k_3^2$. Integrating the temporal momentum of the [curvature projection](gaussian.md) gives
$$
 C(n)=\int_{[-\pi,\pi]^3} \frac{\widehat k_3^2(\widehat k_1^2+\widehat k_2^2)}
 {2\sinh\omega}\,e^{-|n|\omega}\frac{d^3k}{(2\pi)^3}.
$$
Indeed the Fourier coefficients of $(S+2-2\cos k_4)^{-1}$ are $e^{-|n|\omega}/(2\sinh\omega)$ for $S>0$. They solve the nearest-neighbor Green recurrence with unit source at the origin and vanish at infinity. The spatial integrand is positive almost everywhere and integrable at the origin. Let $\mu$ be the pushforward of the displayed positive weight under $k\mapsto\omega(k)$. It has mass $C(0)$, and no atom at zero.

Put $D=1+2sC(0)$. Integration of the two-variable Gaussian density in each of the three colors gives the **connected** limit
$$
 B_s(n)=[D^2-4s^2 C(n)^2]^{-3/2}-D^{-3}.
$$
In particular $B_s(0)>0$. Both expectations and the product converge under the original Wilson measures because the functions are bounded and continuous. At $n=0$ the formula also follows by taking the single-vector expectation with parameter $2s$. The limiting law uses fixed lattice time separations; it gives no error bound uniform for separations diverging with the cutoff.

## The low end of the spectrum in lattice units

Take $E=-\log t$ for normalized transfer eigenvalue $t$. For every regulated vacuum form the positive spectral measure of $O_s^\beta-\langle O_s^\beta\rangle$. The moments of its pushforward under $E\mapsto e^{-E}$ on $[0,1]$ converge for all integers $n\ge0$ to $B_s(n)$. Polynomial density and the zeroth moment give weak convergence. The unique limiting measure in energy is
$$
 \rho_s=D^{-3}\sum_{m\ge1}\frac{(3/2)_m}{m!}
                (4s^2/D^2)^m\,\mu^{*2m}.
$$
Here $(3/2)_m$ is the rising factorial. The ratio $2sC(0)/D<1$ ensures absolute convergence in total mass. Its Laplace moments reproduce the displayed connected values including $n=0$, so there is no missing mass at infinite energy. There is no atom at zero. The dispersion has level sets of spatial Lebesgue measure zero (fix two coordinates and solve for the cosine of the third); hence the measures in this series have no atoms at any energy. The measure gives strictly positive mass to every open subinterval of $(0,2\max\omega)$ already in its first convolution term.

The infrared behavior follows directly from this three-dimensional integral. At small $r=|k|$, $\omega=r+O(r^3)$ and the numerator is $r^4\theta_3^2(\theta_1^2+\theta_2^2)+O(r^6)$ for $\theta=k/r$. The angular integral of $\theta_3^2(\theta_1^2+\theta_2^2)$ is $8\pi/15$, using $\int_{S^2}\theta_3^{2j}=4\pi/(2j+1)$. With the radial volume factor, the weighted density in $r$ is $r^5/(30\pi^2)+O(r^7)$ after angular integration. Changing radial variable to $\omega$ has Jacobian $1+O(r^2)$ uniformly in direction. Consequently
$$
 C(n)\sim \frac{4}{\pi^2 n^6},
 \qquad \mu(dE)=\left[\frac{4}{\pi^2\,5!} E^5+O(E^7)\right]dE .
$$
The first equivalence follows by scaling $r$ by $1/n$ near zero, with exponential suppression away from zero. The leading term in $\mu^{*2}([0,\epsilon])$ integrates two powers $E^5$ over the simplex and equals $(4/\pi^2)^2\epsilon^{12}/12!$. Every term with $m\ge2$ is bounded by its coefficient times $\mu([0,\epsilon])^{2m}$, giving $O_s(\epsilon^{24})$ in total. Thus
$$
 B_s(n)\sim 6s^2D^{-5}(4/\pi^2)^2 n^{-12},\qquad
 \rho_s([0,\epsilon])\sim
  \frac{6s^2D^{-5}}{12!}(4/\pi^2)^2\epsilon^{12}.
$$
These exponents refer to successive limits: first the vacuum at fixed regulator, then $\beta,L\to\infty$ at fixed $n$ or fixed energy window, then $n\to\infty$ or $\epsilon\downarrow0$.

For any fixed sufficiently small $\epsilon>0$, weak convergence gives a strictly positive limiting raw spectral weight in $(\epsilon/2,\epsilon)$. In particular the lowest positive transfer energy in lattice steps tends to zero on every stated isotropic trajectory, even in the gauge-invariant vacuum sector sampled by this explicit observable. If the spacing is $b$, a physical gap $m$ would correspond to lattice energy $bm$. The result has no estimate on a window shrinking at rate $b$, and it leaves the physical Yang–Mills mass gap open.

# The compact-time sine filter

Use dimensionless threshold $M=mT$, frequency $x=ET$ and Euclidean lag $\alpha=s/T$. Set $b_\alpha=\sqrt{1+\alpha^2}$. The response is
$$
 H_\alpha(x)=\frac2\pi\int_0^{\pi/2}
 e^{-M(b_\alpha-\cos\theta)}
 \frac{b_\alpha\sin\theta}{\sin^2\theta+\alpha^2}
 \sin(x\sin\theta)\,d\theta .
$$
At $\alpha=0$ the factor is $1/\sin\theta$, with a removable singularity in the integrand. The relevant real times lie in $[0,T]$.

**Above the threshold**, including $x=M$,
$$
 |e^{-\alpha x}-H_\alpha(x)|\le e^{-M b_\alpha}.
$$
**Below the threshold**, $|1-H_0(x)|\le1$ for $0\le x\le M$. The uniform low-energy constant matters for interpreting a failed gap prediction as a lower bound on mass.

## Rectangular contour

Integrate
$$
 f(z)=\exp(M\cos z+i x\sin z)
       \frac{b_\alpha\sin z}{\sin^2 z+\alpha^2}
$$
counterclockwise on the rectangle $0\le\operatorname{Re}z\le\pi/2$, $0\le\operatorname{Im}z\le Y$. For $\alpha>0$, indent the imaginary axis into the rectangle at $z=i\,\operatorname{arsinh}\alpha$, excluding that pole. Its residue is $\tfrac12\exp(M b_\alpha-\alpha x)$. In the strip the imaginary part of $\sin(u+iy)$ has sign $\cos u$ at $y>0$, and its real part is $\sin u\cosh y$. These identify the single boundary pole and exclude other zeros of the denominator. The remaining imaginary-axis contribution is real, using symmetric principal values at the excluded point. The clockwise semicircular indentation contributes minus $\pi$ times the residue to the imaginary part. At $\alpha=0$ the factor becomes $1/\sin z$, and a quarter-circle at the origin contributes $-\pi e^M/2$. This gives the same normalized formula.

On the upper edge the real part of the exponential phase is $\cos u(M\cosh Y-x\sinh Y)\le M e^{-Y}$ for $x\ge M$, and the rational factor is uniformly $O_\alpha(e^{-Y})$. On the right edge $\sin z=\cosh y$ and $\cos z=-i\sinh y$. Taking imaginary parts and sending $Y\to\infty$ gives the exact residual
$$
 e^{-\alpha x}-H_\alpha(x)=\frac2\pi e^{-M b_\alpha}
  \int_0^\infty \frac{b_\alpha\cosh y}{\cosh^2y+\alpha^2}
        \cos(x\cosh y-M\sinh y)\,dy .
$$
The positive weight integrates to $\pi/2$ by the substitution $u=\sinh y$. Retaining the Euclidean lag in the pole residue yields the square root in the spacetime exponent. The estimate on the upper edge also holds exactly at threshold.

## The static response on the low interval

Differentiating under the finite integral gives
$$
 H_0'(x)=\frac2\pi e^{-M}\int_0^{\pi/2}e^{M\cos\theta}
                                   \cos(x\sin\theta)\,d\theta.
$$
For $0\le x\le M$ put $a=(M+x)/2$, $b=(M-x)/2$. The full-circle mean of $\exp(ae^{i\theta}+be^{-i\theta})$ equals $\sum_{n\ge0}(ab)^n/(n!)^2\ge1$ by absolute uniform convergence and extraction of its constant Fourier coefficient. Conjugation symmetry makes the integral of its real part over $[0,\pi]$ at least $\pi$. On $[\pi/2,\pi]$ its real part is bounded above by one. Hence $H'_0(x)\ge e^{-M}$. Since $H_0(0)=0$ and $H_0(M)\le1+e^{-M}$, the stated low-interval residual bound follows.

## Applying the filter to spectral measures

Let $\nu=\operatorname{Re}\langle a,E_Q(\cdot)b\rangle$ and $S(t)=\int\sin(tE)\,d\nu(E)$. Its total variation on any Borel set $I$ is at most $\|E_Q(I)a\|\|E_Q(I)b\|$, by partitioning $I$ and applying Cauchy–Schwarz. With self-adjoint probes, $4iS(t)$ is the sum of the two vacuum commutators in the two orders, using $[A,\tau_t B]$ and $[B,\tau_t A]$. Thus $2|S(t)|$ is bounded by the larger of the two operator norms. The zero-energy term cancels even for a degenerate vacuum.

An explicit error $\mathcal E_\alpha$ is the integral defining $H_\alpha$ with $\sin(x\sin\theta)$ replaced by $|S(T\sin\theta)|$ or by any certified upper bound. For positive lag this kernel is integrable, so Fubini applies directly. At zero lag first cut the time integral off at $t=\eta>0$. The resulting frequency responses are uniformly bounded in $\eta$ and $E$. Indeed the scalar kernel in $dt$ apart from its decreasing exponential factor is $1/t+[T/\sqrt{T^2-t^2}-1]/t$. The second summand has integral $\log2$, by $t=T\sin\theta$. Integrals of $\sin(Et)/t$ over arbitrary subintervals are uniformly bounded, by the alternating half-period test after the substitution $u=Et$. Multiplication by the positive decreasing exponential preserves the bound by integration by parts. Dominated convergence on the finite spectral measure now removes the cutoff. The commutator integrals on the time side are absolutely convergent under the stated power bound. No first-energy moment of an arbitrary bounded electric probe is needed.

Apply the high and low residual bounds separately to the two spectral intervals. This gives the static inequality in the [main theorem](README.md). For a gapped channel the entire residual costs $Ve^{-M b_\alpha}$. The kernel satisfies
$$
 \frac{b_\alpha\sin\theta}{\sin^2\theta+\alpha^2}\le\frac1{\sin\theta}.
$$
Indeed $(b_\alpha-1)\sin^2\theta\le\alpha^2$. With a commutator bound $D t^p e^{-d+ht}$, the remaining error is at most
$$
 c_p D T^p\exp[-d+T\sqrt{h^2+m^2}-m\sqrt{T^2+s^2}],
 \qquad c_p=\pi^{-1}\int_0^{\pi/2}\sin^{p-1}\theta\,d\theta .
$$
Here $h\sin\theta+m\cos\theta\le\sqrt{h^2+m^2}$. Choosing $T=d/\sqrt{h^2+m^2}$ balances the spatial error and high-frequency residual. An exact commutator zero on the open time interval makes the integral vanish regardless of its endpoints.

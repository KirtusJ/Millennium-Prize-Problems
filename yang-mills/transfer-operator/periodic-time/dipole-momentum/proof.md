# The momentum-dependent edge

## Joint measure

Use C4's time-slice difference $X$ of the two scaled, parallel 12-face curvatures separated one step in direction 3, with the intervening link transporting them to a common base. Write $O_s=\exp(-s|X|^2)$ with fixed $s>0$ and center the observable in the specified state. Translation of the observable by $x$ uses the translated path. In the joint tangent law each color of $X$ has covariance
$$
 C(x,t)=\int e^{i q\cdot x-|t|\omega(q)} f(q)\,dq_H,\quad
 f(q)=\frac{h_3^2(h_1^2+h_2^2)}{2\sinh\omega(q)},\quad h_i=2\sin(q_i/2),
 \qquad dq_H=\frac{d^3q}{(2\pi)^3}.
$$
Set $f(0)=0$. This is the spatial-temporal Fourier multiplier of the exact-curvature projection after applying one forward and one backward face difference. The numerator is nonnegative, and $f$ is continuous, bounded, and positive almost everywhere. It behaves as $O(|q|^3)$ at zero. The covariance is real by evenness. [Projection and time Fourier integral](../../../central-quotients/tangent-curvature/dipole.md)

Let $\sigma(dq,dE)=f(q)dq_H\,\delta_{\omega(q)}(dE)$, $C_0=\int f\,dq_H$, and $D=1+2sC_0$. Covariance of the centered squared dipoles is $6 C(x,t)^2$ by Wick contraction of three colors. For the centered bounded exponential the Gaussian determinant gives $(D^2-4s^2 C(x,t)^2)^{-3/2}-D^{-3}$. Hence the respective joint measures are
$$
 6\sigma^{*2},\qquad D^{-3}\sum_{j\ge1}\frac{(3/2)_j}{j!}
          (4s^2/D^2)^j\sigma^{*2j}.
$$
Convolution adds momenta modulo $2\pi$ and adds energies. The series converges in total mass since $2sC_0/D<1$. Each convolution has a canonical momentum density, obtained by integrating all but the last momentum and setting the last equal to $k$ minus their sum. Its total mass in the energy coordinate is at most $\|f\|_\infty C_0^{2j-1}$, so this version also defines the full series at every $k$.

The bounded observable needs only C4's first-moment pressure estimate and bounded-test convergence. For $|X|^2$ the stronger reflected-plaquette estimate gives uniform integrability: $|X|^2\le4(Y_1+Y_2)$ with $Y_i=\beta(1-\mathrm{Re}\,U_{p_i})$. Hölder and the uniform exponential tails control squared readings and products at two fixed locations. [Pressure and reflected moments](../../../central-quotients/tangent-curvature/periodic-limit/pressure.md)

## Why the threshold lies at one soft momentum

Write $a(q)=\|(\sin(q_i/2))_i\|_2$. The complex-coordinate identity $e^{i(p_i+q_i)}-1=(e^{ip_i}-1)+e^{ip_i}(e^{iq_i}-1)$ gives $a(p+q)\le a(p)+a(q)$. For $u,v>0$, $\operatorname{arsinh}(u+v)<\operatorname{arsinh}(u)+\operatorname{arsinh}(v)$ by applying $\sinh$ and its addition formula. Thus the dispersion is strictly subadditive whenever both legs have nonzero momentum. In the two-field term the minimum at total $k\ne0$ is $W=\omega(k)$, attained only at $q=0,k$. At zero momentum the two points coincide. Positive density arbitrarily near these momenta puts the threshold in the spectral support even on a node. This is lattice kinematics at unit spacing. The corresponding continuum linear dispersion admits collinear splits.

For $k\ne0$, let $v=\nabla\omega(k)=(\sin k_i)_i/\sinh W$. The bound $|v|\le(1+a(k)^2)^{-1/2}<1$ is strict. Near the soft momentum $q=r\theta$,
$$
 \omega(q)+\omega(k-q)-W=r(1-v\cdot\theta)+O_k(r^2),\qquad
 f(r\theta)=r^3 A(\theta)+O(r^5),\quad
 A(\theta)=\tfrac12\theta_3^2(\theta_1^2+\theta_2^2).
$$
The expansions are uniform on the sphere. By compactness there are no additional points contributing for sufficiently small widths away from the two minima. The radial cutoff near either is $\epsilon/(1-v\cdot\theta)+O_k(\epsilon^2)$ by the strictly positive radial slope. Write $f(k-r\theta)=r^b H(k,\theta)+O_k(r^{b+1})$ with the following leading factors.

| $k$ | $b$ | $H(k,\theta)$ |
|---|---:|---|
| Generic | 0 | $f(k)$ |
| Nonzero in the plane $k_3=0$ | 2 | $\theta_3^2(h_1(k)^2+h_2(k)^2)/(2\sinh W)$ |
| Nonzero on the axis $k_1=k_2=0$ | 2 | $h_3(k)^2(\theta_1^2+\theta_2^2)/(2\sinh W)$ |

For the squared dipole, integrate $6 f(q)f(k-q)$ against $dq_H$. The two soft endpoints give equal contributions. The conditional weight in $[W,W+\epsilon]$ is asymptotic to $L(k)\epsilon^{6+b}$, where
$$
 L(k)=\frac{12}{(6+b)(2\pi)^3}\int_{S^2}
      \frac{A(\theta)H(k,\theta)}{(1-v\cdot\theta)^{6+b}}\,d\theta .
$$
All angular integrals are positive. At $k=0$ there is one ball with $2\omega(q)\le\epsilon$, radius $\epsilon/2+O(\epsilon^3)$, and integrand $6r^6 A(\theta)^2+O(r^8)$. The spherical average of $A^2$ is $(1/5-2/7+1/9)/4=2/315$. Integration gives $L(0)=1/(241920\pi^2)$ multiplying $\epsilon^9$. The fixed-nonzero-momentum expansion is not uniform as $k\to0$.

## Higher convolutions of the bounded reading

A possible error would be to use only the two-field contribution as an upper bound. For $l=2j\ge4$ choose a hard leg having maximal energy among all legs. At fixed nonzero $k$ and total energy $E\le W+\epsilon$, this leg has energy $w\ge3W/4$ for all sufficiently small $\epsilon$, uniformly in $l$. Indeed $a(k)\le\sum_i\sinh(w_i/2)$ and $\sinh(u/2)/u$ is strictly increasing. If all $w_i\le3W/4$, the latter sum is at most $E\,\sinh(3W/8)/(3W/4)$, strictly below $\sinh(W/2)$ for small $\epsilon$.

Let $S$ be the summed energy of the other legs. Then $S\le W/4+\epsilon$ and $a(k)\le\sinh(w/2)+\sinh(S/2)$. On $3W/4\le w\le W+\epsilon$, $0\le S\le W/3$, there is a constant $c_k>0$ such that
$$
 w+S-2\operatorname{arsinh}(\sinh(w/2)+\sinh(S/2))\ge c_k S .
$$
The quotient by $S$ is positive on the compact region away from zero and extends there with limit $1-\operatorname{sech}(w/2)>0$. Consequently $S\le\epsilon/c_k$. All soft legs are in this window. Their individual integrated mass is at most $C_k\epsilon^6$ by the small-$q$ expansion. Use the hard leg as the dependent momentum, bound its density by $\|f\|_\infty$, and sum over its $l$ possible positions. The entire fixed-$k$ mass of the $l$-fold term is at most $l\|f\|_\infty(C_k\epsilon^6)^{l-1}$. With the displayed series coefficients, summing $l\ge4$ gives $O_{k,s}(\epsilon^{18})$. At $k=0$ every leg is soft. Bounding the dependent last density by $O(\epsilon^3)$ gives $O_s(\epsilon^{21})$ for the same remainder. It follows that the leading coefficient for the bounded exponential is exactly $s^2D^{-5} L(k)$ in all four rows.

## What passes back to Wilson states

Spatial translations commute with the positive transfer in each periodic limit state. The centered vector therefore has a positive joint measure on the compact space of spatial momenta and transfer values $\lambda\in[0,1]$. Its mixed moments at $(x,n)\in\mathbb Z^3\times\mathbb N_0$ are the translated time correlations. The bounded two-dipole law converges at each such pair, including $n=0$. The mixed trigonometric polynomials in $k$ and ordinary polynomials in $\lambda$ are uniformly dense. Together with convergence of total mass this proves joint weak convergence to the measure above under $\lambda=e^{-E}$. The argument works for every sequence of choices of periodic limit state. Hence the limiting measure's positive mass on an open window gives a common positive lower bound there for all such states at sufficiently large $\beta$.

Fix $\delta>0$. Choose $M$ disjoint open momentum neighborhoods away from zero, all close enough to zero that $\omega(k)<\delta/2$ inside them. The two-field convolution gives positive mass in each neighborhood with energy in $(0,\delta)$ by the strict threshold and positive integrand off its nodes. For all sufficiently large $\beta$ the corresponding joint projections of the actual centered Wilson vector are therefore nonzero. They are mutually orthogonal by their distinct momentum supports. This yields the stated rank conclusion, including if the vacuum eigenspace is degenerate. It concerns open momentum cells and a **fixed** energy window followed by large coupling. It does not give pointwise convergence of densities for a fixed regulator, an infinite-rank statement at one prescribed coupling, or a uniform bound for windows shrinking at an assigned physical rate.

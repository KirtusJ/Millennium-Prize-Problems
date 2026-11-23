# Which reflection plane survives truncation?

### Jofer v4, Theorem 18.74, Step 3

Lemma 18.71 is a positive statement about the truncated observable and the plane at $-R$. If the nominal positive-time center is $t_i\ge0$ and its radius is $R$, the entire truncated observable is supported to the right of that plane. In Lemma 18.72 the radius belongs to $a\mathbb N$ and tends to infinity at fixed **physical** flow time. Its displayed estimate compares truncated and standard flowed Schwinger functions, including on test tensors reflected in the moving plane. Grant this estimate for the purpose of testing Step 3. It compares two forms at the *same moving plane*. For a stationary reflection-even scalar, one of their two-point entries has physical lag $t_i+t_j+2R$. Translation invariance preserves this lag when both readings and plane are recentered. The desired entry for the original tests has lag $t_i+t_j$. If one translates the centers back instead, the truncated observables can cross the original positive-half boundary. The comparison and positivity stated in the two lemmas therefore leave the fixed-plane OS inference unproved. This disposition is specific to Step 3 in the inspected version. [Jofer v4, Lemmas 18.71–18.72 and Theorem 18.74](https://ai.vixra.org/pdf/2509.0025v4.pdf) · [G4's version distinction](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7097089641)

### A bounded example satisfying both premises

Let $X(t)$ be a centered stationary real Gaussian field on the time line with covariance $e^{-\omega |t|}$, $\omega>0$. Its reflected covariance on the positive half-line is the positive rank-one kernel $e^{-\omega u}e^{-\omega v}$. Gaussian Wick products, or conditioning the two independent halves on $X(0)$, give reflection positivity for bounded functions of the positive-half field. Normalize $g_s(u)=(4\pi s)^{-1/2}e^{-u^2/(4s)}$ with $s>0$ fixed. Set $X_R(t)=\int_{-R}^R g_s(u)X(t+u)\,du$ and let $X_\infty$ use the entire line. These mean-square integrals exist since $X$ has variance one. The $L^2$ error is bounded by $\int_{|u|>R}g_s(u)\,du$, uniformly in the center. For bounded Lipschitz functions of fixed finitely many readings, product telescoping gives uniform convergence of their correlation functions, including at moving centers.

For $u,v\ge0$ the covariance of $X_R(u)$ and its partner at $-2R-v$ is
$$
 e^{-\omega(2R+u+v)}
 \left(\int_{-R}^R g_s(z)e^{\omega z}\,dz\right)^2 .
$$
The factorization uses $2R+u+v+z-z'\ge0$ on the integration domain and the even kernel. Each matrix is positive semidefinite. For fixed $u,v$ it tends to zero, since the full Gaussian exponential moment is finite. The same limit holds for the connected form of $Y_R=\sin X_R$. The two-point entry is $e^{-\operatorname{Var}X_R}\sinh(\operatorname{Cov}(X_R(u),X_R(-2R-v)))$. The bounded variables already belong to the positive algebra for the shifted plane.

At the original plane let $k(t)=\operatorname{Cov}(X_\infty(t),X_\infty(0))$. Its temporal spectral density in the ordinary Fourier convention is $2\omega e^{-2sp^2}/(\omega^2+p^2)$ with integration $dp/(2\pi)$. Hence $k'(0)=0$ and $k''(0)<0$. For the bounded $Y_\infty$ the covariance is $e^{-k(0)}\sinh k(t)$; its second derivative at zero is strictly negative. By continuity it is strictly concave near zero. For $0<u<v$ sufficiently small, its reflected second difference at $2u,u+v,2v$ is strictly negative. This example has translation invariance, exact moving-plane positivity, and uniform convergence for bounded readings. Its limiting covariance fails fixed-plane positivity. Narrow temporal mollification preserves the strict sign. The example tests an implication and makes no claim to realize a Wilson vacuum. Jaffe earlier exhibited finite stochastic-time failure of reflection positivity for a free scalar by a different covariance. [Jaffe, Theorem III.1](https://arthurjaffe.net/Assets/pdf/SPDE-QFT-v3.pdf)

### A necessary condition at the original plane

For any stationary, real, reflection-even, finite-variance reading let $C(t)$ be its continuous centered covariance. If its sharp-time family has OS positivity then $C(t)-2C(t+h)+C(t+2h)\ge0$ for $t,h>0$. This follows by subtracting the readings at $t/2$ and $t/2+h$. Continuity gives the endpoint $t=0$. Midpoint convexity and continuity give convexity on the half-line. For $0<\epsilon<t$ this yields
$$
 \mathbb E|Y(\epsilon)-Y(0)|^2
   =2[C(0)-C(\epsilon)]\ \ge\ (2\epsilon/t)[C(0)-C(t)].
$$
Thus sublinear mean-square increments $o(\epsilon)$ force $C(t)=C(0)$ for every $t$, by stationarity and Cauchy–Schwarz. A finite mean-square time derivative suffices for this obstruction. The generated Lean proof derives the quadratic-increment case by a discrete slope bound on each grid. No Gaussian assumption, mass-gap assumption, reconstruction theorem or analytic continuation is used for this necessary condition. Its application to interacting fixed-flow observables requires a continuum increment estimate and nonconstant covariance for the same normalized reading. Smoothness at each finite regulator alone supplies neither uniform estimate. For spatial-only magnetic heat flow the free profile has a nonzero right slope, $-C'(0+)/C(0)=3\sqrt{\pi}/(2\sqrt{2s})$, consistent with the inequality. [Lean proof](FlowReflection.lean) · [Spatial spectrum](../spatial-flow/spectrum.md)

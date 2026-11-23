# A bounded reading of the six Wilson face traces with the same slab spectrum

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

At a temporal link of the defining four-dimensional SU(2) Wilson measure, record just one number,
$$
 X=\beta\sum_{p\ni e}\operatorname{tr}(U_p)/2 .
$$
There is **one bounded even continuous function $h$**, independent of the coupling, box and spacing, for which $h(X)$ gives exactly the transfer insertion of the [squared centered star action](../staple-response/) at every finite cutoff. Evaluating it requires only the six ordinary plaquette traces. Its conditional noise at weak coupling is asymptotic to $1/(1536\beta^4)$. The earlier squared reading has order-one noise. Here noise means the mean variance of a reading conditional on the exterior of this link.

For every pair of spatial boundary configurations the two one-slab kernels agree. Thus all correlations with arbitrary earlier and later slabs agree, including on adjacent slabs and in finite periodic histories. Their centered positive-time transfer measures agree. Their equal-time variances can differ. Among continuous readings of this one number calibrated at every staple radius in the accessible interval, $h$ has minimum conditional squared error at **each** radius. Access to the full exterior gives a different statistical problem and permits evaluating the conditional mean directly.

## Inverting the one-link conditional mean

Let $H$ be $\beta$ times the sum of the six exterior three-link transporters, $R=|H|$, $X=U_e\cdot H$ in unit quaternion coordinates, and $Z(R)=2I_1(R)/R$, with $Z(0)=1$. Under Haar tilted by $e^X$, the conditional density of $X$ on $(-R,R)$ is
$$
 \frac{2e^x\sqrt{R^2-x^2}}{\pi R^2 Z(R)}.
$$
At $R=0$ the law is a point mass at zero. The previous centered star is $W=\mathbb E_R X-X$, with conditional second moment $V(R)=R^2(\log Z)''(R)$. All six plaquettes share the same conditional link; no finite-coupling Gaussian approximation enters this inversion.

For a desired conditional mean $F(R)$ put $A(v)=v Z(\sqrt v)F(\sqrt v)$. For this construction suppose $A(0)=0$ and $A$ is $C^2$ on each compact interval of nonnegative arguments, with $F$ continuous at zero. For $x\ge0$ define
$$
 h_F(x)=\frac{A'(0)+x\int_0^{x^2} A''(u)(x^2-u)^{-1/2}\,du}{\cosh x}
$$
and extend evenly. Then $\mathbb E_R h_F(X)=F(R)$ for all $R$. At zero $h_F(0)=A'(0)=F(0)$. The apparent endpoint singularity is integrable, and continuity follows by scaling the integral to a fixed unit interval. Taking $F=V$ gives the stated $h$. Smoothness at zero follows from the even series of $Z$ with positive value at zero. In this case $A'(0)=0$.

To derive the formula, write $g(u)=\cosh(\sqrt u)h_F(\sqrt u)/\sqrt u$. Substitution of $u=x^2$ in the even conditional integral shows the required forward equation is
$$
 A(v)=\frac2\pi\int_0^v g(u)\sqrt{v-u}\,du .
$$
Its derivative is $\pi^{-1}\int_0^v g(u)/\sqrt{v-u}\,du$. This differentiation is justified for the continuous numerator and the integrable $u^{-1/2}$ singularity, for example by integrating the derivative kernel first and applying Fubini on compact intervals. Define $Jq(v)=\int_0^v q(u)/\sqrt{v-u}\,du$. The identity
$$
 \int_s^v \frac{dt}{\sqrt{t-s}\sqrt{v-t}}=\pi
$$
follows by integrating the derivative of $\arcsin((2t-s-v)/(v-s))$. It gives $J^2 q(v)=\pi\int_0^v q$ by absolute integration, also for locally integrable signed $q$. The proposed $g=A'(0)/\sqrt u+J(A'')(u)$ therefore satisfies $Jg=\pi A'$; integrating and using $A(0)=0$ recovers the target. For uniqueness, zero forward data imply $Jg=0$ at positive arguments. A second application gives $\int_0^v g=0$ for all $v$, so continuity away from zero identifies the even reading everywhere. The argument is local in $R$ and also applies on a single finite interval. [Abel integral equation](https://encyclopediaofmath.org/wiki/Abel_integral_equation) · [PCP OS and Lean verification](execution.md)

Integrating a Wilson link at fixed staples has a long history as the multihit variance-reduction method. The operation here starts with a specified conditional mean and inverts the semicircle average to obtain a reading of the ordinary summed trace. The Abel identity used in that inversion is classical. [Parisi, Petronzio and Rapuano, 1983](https://doi.org/10.1016/0370-2693(83)90930-9)

## Optimality for the ordinary summed trace

For any fixed radius, conditional on $|X|=x>0$, the probability of a positive sign is $p(x)=e^x/(2\cosh x)$, independent of $R$. For any calibrated real reading $q(X)$ its conditional sign average is therefore the same even function at every radius, and by uniqueness is $h_F(x)$. For any target $t$, the excess squared error of $q$ at fixed $|X|$ over that of $h_F$ is exactly $p(1-p)[q(x)-q(-x)]^2$. Integrating proves minimum variance conditionally at every $R$. This also characterizes the freedom to add an odd function times $e^{-x}$ to an answer. Continuity removes ambiguity on null sets. For $F=V$, integrating $h(X)$ within its slab reproduces $V(R)$ just as integrating $W^2$ does. The unused links, boundary weights and surrounding tests may then be integrated unchanged.

[Boundedness, sharp weak-coupling noise and equal-time normalization](variance.md) · [Finite-box Wilson checks](execution.md)

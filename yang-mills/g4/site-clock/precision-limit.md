# What the present absolute covariance accuracy can decide

There are two families of positive transfer measures at the same gap $m=\beta^{-1/7}$. Their entire even-time moment sequences approximate the **actual free 24-plaquette clover reference** within $O(\beta^{-1/8})$, uniformly at every time. Both put positive weight at their exact gap. One has a bounded midpoint ratio and the other has a divergent ratio. Thus positivity, the Wilson clock floor and covariance data at that absolute resolution do not decide (C). The measures are spectral controls. Establishing which behavior occurs in Wilson gauge theory requires further dynamical information. C4’s nearest-neighbor Gaussian construction tests light overlap for a local magnetic reading. [A4’s mixed clover estimate](../../observable-normalization/transfer-increments/local-action/site-scalar/README.md) · [C4’s local Gaussian model](../../central-quotients/tangent-curvature/periodic-limit/local-overlap/README.md)

Let $\nu_*$ be the buffered free clover measure. It exists by taking a weak limit of the bounded measures on $[0,1]$ in the [fixed-time argument](README.md). Its moments determine it by polynomial density. A4’s free clover asymptotic gives $M_k^*\le C(1+k)^{-8}$. With $a=\beta^{-1/64}$ and $k=\lfloor1/a\rfloor$, positivity gives

$$
 \nu_*([e^{-a},1])\le e^{ak}M_k^*\le C'a^8 .
$$

Retain the restriction of $\nu_*$ to $[0,e^{-a})$ and add mass $a^8$ at $e^{-a}$. Call the resulting measure $\lambda$ and its moments $Q_i$. Put $J=\lfloor1/(2m)\rfloor-1$, $h=\lfloor(J-1)/2\rfloor$ and $b=e^{-2m}$. For large $\beta$, $b>e^{-a}$, $aJ/\log\beta\to\infty$, and $2mJ\to1$. Define

$$
\nu_+=\lambda+a^8 e^{-aJ/4}\delta_b,\qquad
 \nu_-=\lambda+a^8 e^{-2aJ}\delta_b .
$$

Removing and replacing at most $O(a^8)$ total mass changes the integral of every $u^i$, $i\ge0$, by $O(a^8)=O(\beta^{-1/8})$. It even bounds the change for every test of sup norm one. Realize the time transfer on $\mathbb C\Omega\oplus L^2(\nu_\pm)$ as $1\oplus\sqrt u$ by multiplication on the second summand. The vector $0\oplus1$ is centered, sees the top atom $b$, and has the displayed $T^2$ moments. The transfer gap on the complement is exactly $m$ for both. Also $a^8 e^{-aJ}\le Q_J$ and $Q_i\le(\|\nu_*\|+a^8)e^{-ai}$ for all $i\ge0$. In particular both measures obey lower and upper clock bounds of A4’s stated order, with suitable constants.

At $i=h,J$ the cutoff term $Q_i=o(a^8e^{-aJ/4})$, since $h=J/2+O(1)$ and $aJ/\log\beta\to\infty$. Also $b^i$ is bounded away from zero. Hence $M_h^+/M_J^+\to e^{1/2}$. On the other hand $Q_h\ge e^{a(J-h)}Q_J$ and $a^8 e^{-2aJ} b^J\le e^{-aJ}Q_J$. Consequently

$$
 \frac{M_h^-}{M_J^-}\ \ge\
 \frac{e^{a(J-h)}}{1+e^{-aJ}}\ \longrightarrow\infty .
$$

The two measures even lie within $a^8 e^{-aJ/4}$ of **each other** in total variation norm. Consequently there are common intervals of radius $a^8 e^{-aJ/4}/2$ for *every* moment, simultaneously compatible with the two opposite dispositions. This gives an exponential obstruction to a worst-case inference from noisy time moments in this class. The exponentially smaller accuracy obtained in the [sufficient degree and precision bound](certificate.md) leaves a gap between the two exponents. The full nonlinear Wilson measure imposes constraints beyond these positive time moments.

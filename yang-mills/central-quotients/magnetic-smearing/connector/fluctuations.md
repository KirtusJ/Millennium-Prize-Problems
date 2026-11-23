# A time-sum fluctuation law on logarithmic trajectories

Write $P$ for the one-step Markov operator of the Wilson spatial-slice vacuum process $S_j$. At each finite cutoff this is the ground-state transform of the normalized transfer. With positive vacuum wavefunction $\Omega$ and transfer kernel $\widehat T(x,dy)$, its kernel is $P(x,dy)=\Omega(y)\widehat T(x,dy)/\Omega(x)$. The vacuum law $\Omega^2 dx$ is stationary, and symmetry of the transfer gives reversibility. The full gauge-averaged kernel can be used. Gauge-invariant readings have the same cylinder laws under this construction. All $L^p$ norms below use that stationary slice law.

Put $h=h_r$, $g=h^2-1/d$. For $u=h$ and $u=g$ the two **uncentered** slice products satisfy
$$
 0\le\|P u\|_2^2=\mathbb E[u(S_0)u(S_2)]\le\delta^2.
$$
Indeed the two separated trunks factor conditional on their joint exterior and each conditional mean has magnitude at most $\delta$. For $g$ this uses the conditional second moment of the unit-vector matrix coefficient. Reversibility gives the equality to the squared norm. This also controls prediction across one step even though its adjacent trunks share plaquettes. [Conditional proof and parameter $\delta$](slow.md)

Let $D_j=h(S_j)-(P h)(S_{j-1})$. The variables $D_j$ are martingale differences in the slice filtration and $|D_j|\le2$. Their predictable variance at $j$ is $V_j=(P h^2)(S_{j-1})-(P h)^2(S_{j-1})$. Stationarity gives
$$
  \mathbb E|V_j-1/d|\le\|Pg\|_1+\|P h\|_2^2\le\delta+\delta^2.
$$
On $0\le t\le T$ the deviation of $r^{-1}\sum_{j\le\lfloor rt\rfloor}V_j$ from $t/d$ has expected supremum at most $T(\delta+\delta^2)+1/(rd)$. The scaled martingale jumps are bounded by $2/\sqrt r$ and its predictable variance jumps by $4/r$. Thus its predictable variation converges uniformly on compact intervals in probability and the jump and conditional Lindeberg conditions hold. The martingale functional central limit theorem gives
$$
 r^{-1/2}\sum_{j=1}^{\lfloor rt\rfloor}D_j
 \ \Longrightarrow\ d^{-1/2}B(t)
$$
in the Skorokhod space of paths, where $B$ is standard Brownian motion. [Whitt, Proofs of the martingale FCLT, Theorem 2.1(ii)](https://arxiv.org/abs/0712.1929)

The difference from summing the **original measured angles** has expected supremum at most $T\sqrt r\,\delta$ on this interval, by the triangle inequality and the one-step prediction bound. Hence the same functional limit holds for $r^{-1/2}\sum_{j\le\lfloor rt\rfloor}h(S_j)$ whenever $\sqrt r\,\delta\to0$. Subtracting the exact vacuum mean at each time gives the same limit because $|\mathbb E h|\le\delta$. The condition holds if $\beta=O(\log r)$, and more generally if $(1+\beta)\log r=o(r)$. All consecutive time slices enter. No quantitative spatial mixing, temporal gap, or independence of consecutive readings enters the argument.

For instance, integrating the sampled angle against a smooth compact time profile with the fluctuation normalization yields a centered Gaussian of variance $d^{-1}\int f(t)^2dt$, by integration by parts against the partial-sum process. On the unamplified physical time scale the integral tends to zero. This temporal contact signal and the escape of the same operator's raw low-energy spectral weight are consistent. Neither quantity measures a mass gap of the interacting theory.

## The same ordinary time integral

For a fixed $T>0$ set $I_r=r^{-1}\sum_{j=1}^{\lfloor rT\rfloor} h(S_j)$. On the fast branch, $\operatorname{Var} I_r\to2\int_0^T(T-t) C(t)\,dt>0$ with the [angular covariance](free.md). Indeed write the sum as a double integral of the piecewise constant covariance; the two-time Wilson limit holds for every pair of distinct fixed times and the integrands are bounded. On the slow branch with $\sqrt r\,\delta\to0$, $r\operatorname{Var} I_r\to T/d$. In the exact sum the lag-zero term tends to $T/d$ after multiplication by $r$, the lag-one contribution is $O(T\delta)$, and the sum over all greater lags is $O(T^2r\delta^2)$. These are statements about the centered variance of the same time integral on each trajectory.

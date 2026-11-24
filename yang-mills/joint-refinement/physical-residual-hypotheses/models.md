# Noncommuting coarse projection in a known-answer model

**Stipulation.** Give two signs $X,Y$ the stationary law $\pi(x,y)=(1+sxy)/4$ with $0<s<1$. Observe $Y$ and take $P$ to be conditional expectation given $Y$. On centered observables define $S_t=\lambda |X\rangle\langle X|+\mu(I-|X\rangle\langle X|)$ with $\lambda=e^{-ut},\ \mu=e^{-vt},\ 0<u\le v$. On constants the eigenvalue is one. This is a reversible physical-time model for testing the inference. Its full Markov kernel is the convex mixture $\mu I+(\lambda-\mu)\mathbb E[\cdot\mid X]+(1-\lambda)\mathbb E$. The semigroup identity follows from its three orthogonal spectral spaces. Generic parameter choices have $PS_t\ne S_tP$.

**Exact values.** Put $w=1-s^2$. The normalized residual $(X-sY)/\sqrt w$ realizes the largest residual return at every lag. Compression gives
$$d=1-\lambda,\quad b=d+(\lambda-\mu)w,\quad \|P S_t Q\|=(\lambda-\mu)s\sqrt w,\quad
\theta(k)=w\lambda^k+(1-w)\mu^k.$$
On the residual space $Q S_t^k Q=\mu^k Q+(\lambda^k-\mu^k)|QX\rangle\langle QX|$. The same residual maximizes every lag, so summing the largest eigenvalue over lags yields
$$T(m)=w\,\frac{\lambda^m}{1-\lambda}+(1-w)\frac{\mu^m}{1-\mu}.$$
For $m=1$ as $\mu\downarrow0$, $b=(1+T(1))d$ in the limit. Thus the coefficient in the basic unclipped endpoint estimate can be attained in the limit of reversible semigroups.

**A working late-lag hypothesis.** Take $\lambda=.9,\ \mu=.4,\ \lambda_*=.75,\ w_n=4^{-n}$ and $m_n=n$ for $n\ge1$. The full deficit is $.1$ and $b_n\ge .1$, so H1 holds with $\alpha_n=1$ in this known-answer sequence. The two contributions to $\eta_n$ are bounded by fixed multiples of $.3^n$ and $(.4/.75)^n$. Their sum over levels converges. Starting at lag one at every level would leave $T_n(1)\ge .4/.6$ forever. This example establishes consistency of the hypotheses with nonzero coupling between the observed and residual states. Its semigroups and projections are specified algebraically; it supplies no estimate on a Wilson lattice.

**Two failure tests.** First, hold $\lambda,\mu,s$ fixed and take $\lambda>\lambda_*$. The physical gap stays positive, yet for every $m\ge1$ the slow component gives $\lambda_*^{1-m}T(m)\ge w\lambda/(1-\lambda)$. H2 is sufficient and can fail for a gapped system. Second, for an integer $L\ge2$ take $w=L^{-2},\ \lambda=1-L^{-4},\ \mu=L^{-6}$. The first $M$ residual returns have sum at most $M(L^{-2}+L^{-6})$ for every fixed $M$, while $T(1)\ge L^2(1-L^{-4})$. Arbitrarily small finite-window measurements can conceal a large integrated residual susceptibility. H2F avoids extrapolating the tail at the price of the explicit weighted budget in its hypothesis. [Independent matrix checks](check.py)

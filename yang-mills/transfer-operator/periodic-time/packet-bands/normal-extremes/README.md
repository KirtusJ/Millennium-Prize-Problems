# Transverse momentum at a large normal momentum

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For the fourfold $12$ magnetic packet in pure four-dimensional SU(2) Wilson theory, condition its untilted centered spectral measure on $|P_3|>H$, where $P=Rk$ is representative block momentum and $e=RE$ is block energy. As in C4’s normal-tail result, take $H\to\infty$, $H/R\to0$, and $H^8 R^{7/2}/\sqrt\beta\to0$ after the even-periodic thermodynamic limit at each coupling. Then the conditional probability laws satisfy
$$
  (e/H,\ P_3/H,\ P_1,\ P_2)\ \Longrightarrow\ (Y,\ \sigma Y,\ T_1,\ T_2)
$$
uniformly over state selection. The positive variable $Y$ has $\Pr(Y>y)=y^{-8}$ for $y\ge1$, $\sigma$ is a fair sign, and $T$ is independent of both (the sign and $Y$ are also independent). In particular the transverse momenta remain tight on their original block scale. Their law retains contributions from the other curvature factors in the bounded observable. [C4’s normal marginal and constants](../../../../central-quotients/tangent-curvature/periodic-limit/directional-tail/README.md) · [Proof](proof.md)

To sample $T$, put $b(x)=(2\sin(x/2)/x)^8$ with $b(0)=1$. Draw a vector $Q$ of density proportional to $(q_1^2+q_2^2)b(q_1)b(q_2)$. Independently draw $K$ with probabilities
$$
 \Pr(K=k)=(1-z)^{5/2}(5/2)_k z^k/k!,\qquad
 z=\left(\frac{2sv}{1+2sv}\right)^2 ,
$$
where $s>0$ is the packet parameter and $v$ its one-color limiting variance. Add $1+2K$ independent draws from the ordinary one-curvature transverse marginal to $Q$. This sum has law $T$. Its characteristic function vanishes outside $[-4,4]^2$. This last statement is about the Fourier variable dual to transverse momentum; the momentum distribution itself has unbounded support.

The result is a weak limit under a rare-event conditioning. It provides no convergence of unbounded conditional moments or physical mass scale. [Checks](checks.md)

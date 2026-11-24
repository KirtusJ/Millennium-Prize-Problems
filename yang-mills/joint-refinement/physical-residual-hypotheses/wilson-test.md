# Finite-time test of the proposed Wilson band inequality

G4’s H3 is stated for every band vector. Its following necessary inequality can be tested using an ordinary centered, neutral slice observable $f$, a positive integer filter length $j$, and a pair of replicas with the same full coarse orbit. Fix $t$, $\lambda_*$ and the proposed $C_\ell$ before testing, and use the stationary time-vacuum law at the regulator in question. Put $S=e^{-tH}$ and $A_k=\langle f,S^kf\rangle$ for real $f$ (use the conjugate product for complex tests). Set
$$B_j=A_{2j}-\mathbb E\big|\mathbb E[f(X_{jt})\mid\mathcal C(X_0)]\big|^2.$$
The second term uses two independent trajectories conditional on the same full time-zero coarse orbit. Each replica must sample the hidden fine links from their correct conditional vacuum law. Multiplying future endpoint observables estimates the squared coarse conditional mean. Fixing the full fine slice instead changes this term. The first term is the ordinary two-time covariance at $2jt$.

**Necessary bound if H3 holds.** With $E_*=-\log\lambda_*/t$,
$$\boxed{\big[\sqrt{B_j}-\lambda_*^j\sqrt{A_0}\big]_+^2
\ \le\ C_\ell a_n\,\frac{E_*}{1-\lambda_*}\,(A_{2j}-A_{2j+1}).}$$
To verify it, write $F=S^j f$, and $E$ for the projection on physical energies $[0,E_*]$. By stationarity, the Markov property and reversibility, $B_j=\|QF\|^2$. The spectral theorem gives $\|(I-E)F\|\le\lambda_*^j\|f\|$, hence the left side is at most $\|QEF\|^2$. On the band, concavity of $1-e^{-tu}$ gives $u\le E_*(1-e^{-tu})/(1-\lambda_*)$. Thus $\langle EF,H EF\rangle\le E_*\langle F,(I-S)F\rangle/(1-\lambda_*)$, proving the display. No commutation of $P$ with the transfer is used.

**Decision.** A positive, certified left side larger than the certified right side defeats the proposed constant. A sequence of certified lower bounds on the required constant diverging under refinement defeats the linear rate with every fixed constant. If the leakage allowance swamps $\sqrt{B_j}$ the test is inconclusive. The bound also has low statistical power if both long-lag measurements are dominated by noise. Passing on selected marks leaves H3 open. This protocol tests the Wilson conjecture without assigning a measured observable an exact spectral cutoff or asserting that a fitted coarse predictor is optimal. [Hypothesis and units](slow-band.md)

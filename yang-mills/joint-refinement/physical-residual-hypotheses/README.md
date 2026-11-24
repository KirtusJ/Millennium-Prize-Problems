# G4 hypothesis register: physical-time correlations of fine residuals

**Decision sought.** Can physical time propagation itself control the states introduced by refinement? My candidate is to measure how much correlation a state with zero coarse conditional mean retains at later physical times. The proposition below identifies a sufficient rate. I have no proof of that rate for the interacting four-dimensional Wilson measure. This is a G4 research proposal for disproof, first deposited on 23 November 2026. [Correction that motivates the split](../G4_FINAL_AUDIT_2026-11-23.md)

### Stipulations

The [free-scalar benchmark](gaussian.md) proves the proposed rate for a spatially refined free field. The [two-sign models](models.md) test the inheritance criteria and show why small correlations at several lags give little information about their infinite sum. Run `python alias.py` and `python check.py` with NumPy for the numerical controls. Run `python verify.py` to check the archived PCP review and compiler evidence. The [finite-time Wilson test](wilson-test.md) gives the measurement that would challenge a specified H3 constant.

**S1. Physical scope.** Fix a spatial torus of side $\ell$, the isotropic SU(2) Wilson regulator, a dyadic sequence of cutoffs at matched physical scale, and a common positive time $t$ representable on both lattices. Take the time-vacuum limit at each regulator. Use the centered gauge-invariant, center-neutral slice Hilbert space with its own stationary marginal. On that space $S_n=S_n(t)$ is a positive self-adjoint contraction. Its powers represent physical time $kt$. Finite periodic simulations require a separate time-preparation estimate. [Wilson transfer construction, Lüscher](https://doi.org/10.1007/BF01614090) · [Existing matching scheme](../../g4/full-attempt/physical-refinement/methods.md)

**S2. Coarse information.** $P_n$ is conditional expectation given the gauge orbit of the straight coarse links on the fine slice; $Q_n=I-P_n$. A residual $h$ has $P_nh=0$. Define the full deficit $d_n=1-\|S_n\|$ and the inherited deficit $b_n=1-\|P_n S_nP_n\|$. Choose a fixed threshold $0<\lambda_*<1$, write $c=1-\lambda_*$ and $\bar d_n=\min(c,d_n)$. The choice of threshold is part of a proposed bound and must be fixed when testing it.

### Explicit hypotheses and consequences

**My first choice for a Wilson proof attempt is H3.** It asks for an approximation of each physical low-energy vector by a function of the straight coarse links, with squared error bounded by its energy times one lattice spacing. The integrated and finite-lag hypotheses below give complementary physical-time tests. H1 is common to all three routes. [H3, its proof implication, and its disproof standard](slow-band.md)

**H1 — common coarse transfer (open Wilson input).** There is an initial $\bar d_0>0$ and a sequence $0<\alpha_n\le1$ such that $b_n\ge\alpha_n\bar d_{n-1}$ and $\sum_n-\log\alpha_n<\infty$. A possible proof uses a common full-skeleton partition and one-sided comparisons of energy and variance. The four-bin winding measurements do not establish H1. [Relative cell estimate](../plaquette-cell-sums/relative.md)

**H2 — integrated residual correlations (G4 hypothesis, open).** Choose positive integers $m_n$. Take the supremum over *one fixed unit residual at all lags* and over finite upper endpoints $L\ge m_n$:
$$T_n(m_n)=\sup_{\|h\|=1,\ P_nh=0}\ \sup_{L\ge m_n}\sum_{k=m_n}^{L}\langle h,S_n^k h\rangle,\qquad
\eta_n=\lambda_*^{\,1-m_n}T_n(m_n).$$
Require $\sum_n\eta_n<\infty$. A trivial residual space contributes zero. Positivity of $S_n$ makes every summand nonnegative. The definition does not presume a bounded inverse of $I-S_n$. My reason for allowing late starting lags is that a residual can retain an order-one correlation for a few steps at every refinement and still be faster than the low-energy states of interest. The four-state example below realizes this distinction. Reversible-chain covariance sums have classical spectral antecedents. The particular clipped inheritance test here is G4’s proposed application. [Kipnis and Varadhan](https://www.numdam.org/item/AST_1985__132__65_0/)

**Conditional conclusion under H1 and H2.** At each step $\bar d_n\ge\alpha_n\bar d_{n-1}/(1+\eta_n)$. Iteration gives
$$\liminf_n d_n\ \ge\ \bar d_0\prod_{i\ge1}\frac{\alpha_i}{1+\eta_i}>0.$$
This concerns regulators in the indicated sector at a fixed physical size. It supplies neither the continuum field construction nor a bound uniform in increasing spatial volume. The prize also requires the stated theory for every compact simple gauge group. [Jaffe–Witten problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

**H2F — alternative using one finite late lag (G4 hypothesis, open).** Set $\theta_n(m)=\|Q_nS_n^m Q_n\|$, $e_n=\lambda_*^{1-m_n}\theta_n(m_n)$ and $A_n=\prod_{i=1}^n\alpha_i$. Assume H1 and $\sum_n e_n/A_n<\bar d_0$. These sufficient assumptions give
$$\bar d_n\ge A_n\left[\bar d_0-\sum_{i=1}^n e_i/A_i\right]_+.$$
H2F uses one lag per regulator and spends part of the initial deficit. Its bound requires all residuals, including observables concentrated on rare configurations. Certifying an upper bound for that single lag may be easier than certifying the infinite tail. A finite experimental panel gives lower bounds for $\theta_n$ through its trial directions.

### Proof of the implications

Suppress the refinement index. On the centered space put $\lambda=\|S\|$. If $\lambda\le\lambda_*$ the clipped deficit equals $c$ and both recursions hold immediately. Otherwise take $\lambda_*<r<\lambda$ with $r<1$, let $E$ be the nonzero spectral projection on $[r,1]$, and choose a unit $v$ in its range. For $k\ge1$ the spectral theorem gives $S^k\succeq r^k E$. Consequently
$$\theta(m)\ge r^m\|QE\|^2,\qquad
T(m)\ge\frac{r^m}{1-r}\|QE\|^2.$$
For the second inequality first sum up to finite $L$, test on a unit residual and then take the indicated suprema. The identity $\|EQ\|=\|QE\|$ accounts for the direction of the projection. Also $S\succeq r|v\rangle\langle v|$, so $\|PSP\|\ge r\|Pv\|^2$. Thus $b\le1-r+r\|QE\|^2$. Under H2 this is bounded by $(1-r)[1+r^{1-m}T(m)]$; under H2F it is bounded by $1-r+r^{1-m}\theta(m)$. Pass to $r\uparrow\lambda$. This argument includes $\lambda=1$ and requires no top eigenvector. The clipped recursions follow since their right sides never exceed $c$. The displayed product and the weighted cost follow by iteration. The Lean file checks selected scalar rearrangements; the spectral and Wilson arguments are given in prose. [Scalar checks](Checks.lean)

**What could supply physical input?** For H2F, write the normalized full endpoint kernel $K_m(x,y)$ at lag $mt$ relative to the product of its stationary marginals. Apply coarse conditional averaging in each coordinate separately under that product. The kernel of $Q S^m Q$ is $K_m-P_xK_m-P_yK_m+P_xP_yK_m$. After symmetrizing over endpoint gauge and center transformations as appropriate, an essential uniform bound on the integral of its absolute value over $y$ bounds $\theta(m)$ by the symmetric Schur test. This is an explicit Wilson endpoint-integral target. Conditioning both endpoints using the true joint law changes the averaging operation. Bounding this integral by first assuming a physical mass gap would be circular. The Schur bound is sufficient and can be loose.

**Disproof protocol.** On the fine ensemble fit a coarse predictor of a gauge-invariant mark using separate training streams. A poor predictor contaminates the residual with coarse modes. For a centered trial $u=F-\widehat p$ with coarse $\widehat p$, let $s=\|u\|>0$ and independently bound $\|PF-\widehat p\|\le e<s$. The actual residual $h=QF$ obeys $\|h\|\le s$ and $\|u-h\|\le e$. Hence
$$\theta(m)\ \ge\ \frac{[\langle u,S^mu\rangle-2se]_+}{s^2}.$$
Use a certified lower covariance and consistent normalization if claiming a violation. Cross-validation alone does not certify the population predictor error. Freeze the threshold, lag schedule and rate or budget to be challenged. One certified contradiction can defeat specified constants; excluding existence of *some* summable schedule takes a sequence argument. Existing side-six/eight fixed-orbit colour losses use an auxiliary update and do not measure these physical-time quantities. [Signed data audit](../plaquette-cell-sums/z4-readback.md) · [Known-answer models and counterexamples](models.md)

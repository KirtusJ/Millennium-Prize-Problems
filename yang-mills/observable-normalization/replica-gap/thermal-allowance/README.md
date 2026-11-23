# How much purity does a periodic gap test need?

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For an observable with certified spectral width $W$, the thermal allowance in B4's two-lag vacuum-gap test can be taken as $W^2\min\{1/4,(1-P)/2\}$, where $P=Z(2T)/Z(T)^2$ is the Gibbs purity. The second branch is attained by a two-level system. On Z4's coarse and middle ensembles, even a one-bit label of the stored slice readings gives evidence that the purity deficit is too large for this width-only test at one- and two-step separation. The fine ensemble does not resolve the label correlation. These data concern the sensitivity of the test to excited-state contamination. [B4's finite-period test](../../../transfer-operator/periodic-time/thermal-gap-test.md) · [Frozen measurements](../../../z4/reviews/ext-match/predeclared/)

## The excited-pair allowance

Use B4's assumptions, including a unique vacuum, a finite Gibbs trace and $0<t\le T/4$. Let $q$ be the excited Gibbs probability and let $A=O-O_{00}I$. Write $Q$ for the excited-space projection and set $A'=QAQ$ on the full space. In the decomposition $C_T(s)=V(s)+B(s)$, the vacuum pairs contribute $V$ and $B(0)=\operatorname{Var}_\rho(A')$. The Gibbs mean of $A'$ equals that of $A$. In an energy basis $B(s)$ contains the Gibbs variance of the diagonal entries, and each unordered excited off-diagonal pair contributes a nonnegative multiple of $\cosh[(T/2-s)(E_i-E_j)]$. Thus $0\le B(2t)\le B(t)\le B(0)$. This also proves B4's bound $B(0)\le q\|A\|^2$ directly by retaining the uncentered second moment of the compression. Energy degeneracies may contribute constant terms.

If the spectrum of $O$ lies in $[a,b]$, the spectrum of $A'$ lies in $[a-O_{00},b-O_{00}]$, including the zero eigenvalue on the vacuum. Rescale this interval to $[0,1]$ when $W=b-a>0$ (the constant case is immediate). Its scalar spectral law has an atom of mass at least $1-q$ at a known-to-exist location $c\in[0,1]$. Split off mass $1-q$ there and call the remaining conditional mean $u$. The conditional variance is at most $u(1-u)$. The total variance is at most
$$
 q u(1-u)+q(1-q)(u-c)^2.
$$
For $q=0$ it vanishes. For fixed $u$ the maximum over $c$ occurs at an endpoint. At $c=0$ the expression becomes $qu(1-qu)$ and the other endpoint replaces $u$ by $1-u$. If $q\le1/2$, both are at most $q(1-q)$. At all $q$ the variance of a variable in $[0,1]$ is at most $1/4$.

Now $P\le1-q$ since the vacuum is the most probable Gibbs state, and $P\le(1-q)^2+q^2$ by summing the squares of the excited weights. If $P\ge1/2$ then $q\le1/2$ and $q(1-q)\le(1-P)/2$. If $P\le1/2$ use the unconditional quarter bound. This proves the allowance. For $P>1/2$, the two-level reading $O=WQ$ attains $B(s)=q(1-q)W^2=(1-P)W^2/2$ at all lags. More generally a certified lower bound $P_*$ for $P$ can be used throughout the allowance. The endpoint-swap measurement provides such a bound given a suitably controlled upper estimate of its expectation. [Two-replica measurement](../swap.md)

Under a proposed positive vacuum floor $m$, let $R=\cosh[(T/2-2t)m]/\cosh[(T/2-t)m]$. Comparing the two vacuum-pair kernels gives
$$
 \frac{C_T(2t)-R C_T(t)}{1-R}
 \le W^2\min\{1/4,(1-P)/2\}.
$$
The left side is at most $C_T(2t)$ since $C_T(t)\ge C_T(2t)$. When $C_T(2t)<W^2/4$, even the most favorable floor therefore requires a certified deficit upper bound strictly below $2C_T(2t)/W^2$ to falsify it by this inequality. This is a necessary sensitivity condition. A specified finite $m$ and uncertainty in the data can make it stricter.

## An independent bound from the stored slice readings

For even temporal extent write $K(x,u)$ for the positive symmetric half-period Wilson kernel. Two independent opposite-slice pairs have joint density $A^2/Z(T)^2$, where $A=K(x,u)K(y,v)$. Exchanging $u,v$ gives the density with $A$ replaced by $B=K(x,v)K(y,u)$. Their square-root affinity is $\int AB/Z(T)^2=P$. Apply the same finite label to each spatial slice. Cauchy–Schwarz on each label cell bounds this affinity from above by the affinity of the two discrete laws.

If $p_{ij}$ is the joint probability for the labels on a single opposite-slice pair and $S_{ij}=\sqrt{p_{ij}}$ entrywise, the two discrete laws have weights $p_{ij}p_{kl}$ and $p_{il}p_{kj}$. Summing their geometric means gives $\operatorname{tr}[(SS^T)^2]$. For binary labels $\operatorname{tr}(SS^T)=1$, hence
$$
 1-P\ge 2d^2,\qquad d=\sqrt{p_{00}p_{11}}-\sqrt{p_{01}p_{10}}.
$$
This supplies the opposite direction from the independent lower purity certificate used to test a gap. It can diagnose when even exact knowledge of the purity could not make the width-only allowance small enough. Refining the partition tightens the population affinity bound by Cauchy–Schwarz. Searching for a partition on the data would require separate uncertainty controls.

## Frozen-data sensitivity

Use the stored plaquette reading $O$, the spatial mean of three deficits in $[0,2]$, so $W=6$ is valid after the slice flow. For each lattice label a slice by whether $O$ exceeds a fixed rounded value near its reported mean. These thresholds and the analysis were chosen after the original measurements. Opposite-slice counts are averaged over all cyclic origins. The table gives the signed determinant before squaring, the implied point estimate of the deficit floor, and the most permissive deficit ceiling for a width-six test at $t=1$ lattice step. Parentheses are one estimated block-jackknife standard error. The ceiling uses the absolute connected covariance $C_T(2)$ including the square of the observable mean when converting from Z4's normalized ratio.

| Side | Threshold | Configurations per block | $d$ | $2\hat d^2$ | $2\widehat C_T(2)/36$ |
|---:|---:|---:|---:|---:|---:|
| 6 | 0.0900 | 11 | 0.01924 (0.00553) | 0.000741 | $(1.77\pm0.16)10^{-6}$ |
| 8 | 0.0270 | 17 | 0.02979 (0.00759) | 0.00178 | $(2.12\pm0.17)10^{-7}$ |
| 12 | 0.0057 | 25 | 0.00123 (0.00986) | unresolved | $(1.08\pm0.08)10^{-8}$ |

The coarse and middle signed determinants are about 3.5 and 3.9 estimated errors above zero. Doubling block sizes gives 0.01941 (0.00526), 0.02909 (0.00732) and −0.00012 (0.01315). The table keeps distinct configuration IDs within each seed and drops its first ten configurations and incomplete final block. Blocks do not span seeds, and deletion recomputes every statistic from the same retained rows. The squared point estimate is upward biased near zero. These exploratory standard errors depend on adequate blocking and do not certify a population inequality. A sharper observable-specific excited-sector bound could change the sensitivity. No vacuum gap or certified purity value follows from these runs.

The frozen fine files contain 834 distinct configurations after the skips. Six repeated rows affected the original fine estimate. Restoring the six missing declared IDs gives the same whole-block table because they lie in incomplete end blocks. Using all 834 distinct configurations gives signed $d=-0.000798$ with bootstrap errors 0.00894 and 0.00994 for block lengths 25 and 50. Using all 840 declared IDs gives $d=-0.001102$ with errors 0.00889 and 0.00994. The corresponding deficit ceilings before errors are $1.0614\times10^{-8}$ and $1.0777\times10^{-8}$. On both selections the fine deficit floor remains unresolved. The coarse and middle samples are unaffected.

Three host-dispatched PCP OS guests separately counted the four opposite-slice label pairs on the deduplicated frozen seeds, averaging over all 12 cyclic origins. For seeds 1205, 1206 and 1207 the counts in $00,01,10,11$ order were (956,778,778,608), (998,835,835,776) and (870,883,883,808). Pooling these counts reproduces the all-row signed estimate. [Sample definitions, restart checks and resampling procedure](../../thermal-transitions/README.md#fine-ensemble-restart-correction)

The [analysis code](check.py) also tests the compression bound on 240 finite Hamiltonian/observable pairs and checks the direction of coarse-graining on a positive half-kernel. Three host-dispatched PCP OS guests emitted the [Lean file](ThermalAllowance.lean) from [worker.c](worker.c). A separate [guest replay](../../transfer-increments/replay-guests.py) reproduced SHA-256 `e76144bb6f63c3eeafdcaeb1a32841b22cfd00ebdfb135b8973c9d1ae4003807`. Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked five supporting algebraic declarations. The Gibbs decomposition, operator bounds and statistical analysis are given here.

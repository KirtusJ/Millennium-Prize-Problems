# Readback of the two-site electric transfer on the based gauge slice

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**B4’s normalization and steps 1–3 at `a2a5216` pass.** The comparison applies to the two operators compressed to the same slice ball, including its boundary. Retaining the signed cubic term improves the one-step operator estimate. If $s=\beta^{-1/2}$, $P_\rho$ is the indicator of the radius-$\rho$ ball in B4’s 51-dimensional slice and $G_s$ is the Gaussian convolution of coordinate variance $4s^2$, then for $0<s<s_0$, $0<\rho<\rho_0$,
$$
 \|P_\rho(K_s-G_s)P_\rho\|_{2\to2}\le C(s^2+\rho^2).
$$
The constants depend on this finite cube and a fixed central chart. In particular the error at radius $R\beta^{-1/3}$ is $O_R(\beta^{-2/3})$. On a growing rescaled patch $\rho=R_\beta\beta^{-1/3}$ it remains $o(\beta^{-1/3})$ provided $R_\beta=o(\beta^{1/6})$. This controls the electric operator between the retained endpoints. It does not estimate the weight of low-energy states outside the patch. [B4’s proof at the reviewed revision](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/a2a5216/yang-mills/observable-normalization/second-box/local-gauge-quotient/README.md)

## Normalization and the orbit integral

Use the generators $T_a=-i\sigma_a/2$ and the sum of link norms. The one-link normalized Haar density at zero is $c_H=1/(16\pi^2)$, by the unit-quaternion volume $2\pi^2$ and the factor $1/2$ in each of three exponential coordinates. Write $D$ for the based incidence on the three colors. The scalar pinned Laplacian has determinant $49152$: the nonzero eigenvalues of the unpinned doubled-edge cube are $4,8,12$ with multiplicities $3,3,1$, and their product divided by eight is the cofactor. Therefore $\det(D^TD)=49152^3$. The 72-dimensional link measure contributes $c_H^{24}$ and changing from orbit tangent and orthonormal slice coordinates to link coordinates contributes $\sqrt{\det(D^TD)}$. Dividing by the seven normalized site measures gives the quotient density $c_H^{17}\sqrt{\det(D^TD)}$ at the origin. Multiplying its two square roots by the based Haar density, normalizing all 24 link kernels and doing the 21-dimensional Gaussian integral leaves $(8\pi s^2)^{-51/2}$. All determinants here are for the pinned group. A global color rotation still acts on the slice. Sint’s equation (3.8) integrates the temporal links for the full physical projection. [Sint, *On the Schrödinger functional in QCD*](https://arxiv.org/pdf/hep-lat/9312079)

For completeness, write $v=B-A\in\ker D^T$, $t$ for the seven site logarithms and $r=|v|+|t|$. On a fixed small chart the quadratic cost $Q_B$ and exact cost $8F$ both dominate $cr^2$, by the invertible differential at zero. Outside this chart in the based group, compactness and pinning give a positive lower cost uniformly for small endpoints. The slice Jacobians contribute $1+O(\rho^2)$ and the site Haar density contributes $1+O(|t|^2)$. For $L_B=D+O(|B|)$ and link metric $g_B=I+O(|B|^2)$, the Schur complement on $\ker D^T$ differs from the identity by $O(|B|^2)$: its subtracted term has $L_B^Tg_Bv=O(|B||v|)$ on each side of a bounded inverse. Simultaneous color rotation leaves the positive scalar $\det(L_B^Tg_BL_B)$ invariant, so its linear Taylor coefficient vanishes. These observations verify the determinant, projected metric and Gaussian exponent used by B4.

## The cubic cancellation and the boundary

Expand in $(v,t)$ with $B$ fixed. Smoothness on the fixed chart gives
$$
 8F=Q_B+C_0(v,t)+O(|B|r^3+r^4),\qquad
 C_0(v,t)=-\sum_{e=(x,y)} v_e\cdot(t_x\times t_y).
$$
At $B=0$, $A=-v$, the trace is that of $e^{v_e}e^{t_x}e^{-t_y}$. The trace of $T_aT_bT_c$ divided by two is $-\epsilon_{abc}/8$. Cubic terms with repeated vectors vanish. The remaining cubic can be nonzero even for divergence-free $v$. The check below gives an oriented square on which its value is $-1$.

Set $Q_0=|v|^2+|Dt|^2$. At fixed $v$ the integral of $C_0 e^{-Q_0/(8s^2)}$ over all $t$ vanishes: the centered Gaussian site covariance between $x$ and $y$ is a scalar times the color identity, whose contraction with the alternating tensor is zero. The cubic is even under simultaneous $t\mapsto-t$, so parity in all site coordinates alone would give an incorrect justification.

To quantify the cancellation, expand the exponential once about $Q_B$ and replace its linear cubic term's Gaussian weight by the one at $Q_0$. The cost difference $|Q_B-Q_0|\le C|B|r^2$ controls this replacement. Up to fixed constants, the errors in the unnormalized integrand are bounded by
$$
 e^{-cr^2/s^2}
 \left[\frac{|B|r^3+r^4}{s^2}+\frac{r^6+|B|r^5}{s^4}\right].
$$
The exponential Taylor remainder uses the minimum of the two positive costs on the segment between $8F$ and $Q_B$. Extending the Gaussian cubic to all $t$ costs an exponentially small tail. After the $t$ integral and normalization, these errors are bounded by $(s^2+\rho s)s^{-51}$ times an integrable polynomial times a Gaussian in $v/s$. The Haar and one-link normalization errors add $O(s^2+\rho^2)$ in either integral norm. So does the integrated quadratic comparison from the preceding section. The same majorant works with $A$ fixed or $B$ fixed, and restricting the other endpoint to the ball can only decrease its integral. Schur’s test and $2\rho s\le\rho^2+s^2$ give the displayed operator bound. A common nonnegative Wilson multiplier of norm at most one on each side preserves it. General multidimensional Laplace expansions give context for retaining signed Taylor terms. The color cancellation and two endpoint estimates above use this kernel explicitly. [Kirwin, *Higher asymptotics of Laplace’s approximation*](https://arxiv.org/abs/0810.1700)

## First correction at the central diagonal

At the single kernel entry $A=B=0$ the ratio to the Gaussian density is
$$
 K_s(0,0)/G_s(0)=1+\tfrac{149}{16}s^2+O(s^4),
$$
where $G_s(0)=(8\pi s^2)^{-51/2}$. This is a pointwise expansion, with no operator-norm lower bound inferred from it.

Here is one derivation. Write each site quaternion near the identity as $(\sqrt{1-s^2|u_x|^2/4},su_x/2)$ and pin $u_0=0$. Put $a_x=|u_x|^2$. In the unperturbed Gaussian each color has covariance $4$ times the inverse pinned scalar Laplacian. Site Haar densities give $1+s^2\sum_x a_x/8$ to this order. The scalar quaternion products in the exponent contribute $-s^2\sum_{(x,y)}(a_x-a_y)^2/128$. Each inverse one-link normalization contributes $+3s^2/8$ relative to its leading constant, from $2e^{-\beta}I_1(\beta)/\beta$. Consequently the coefficient is
$$
 9+\mathbb E\left[\tfrac18\sum_x a_x-\tfrac1{128}\sum_{(x,y)}(a_x-a_y)^2\right].
$$
For one-color variances $A,B$ and cross-covariance $C$, the required moments are $\mathbb E a_x^2=15A^2$ and $\mathbb E a_xa_y=9AB+6C^2$. Summing with exact rational covariance yields $149/16$. In exponential site coordinates the Haar contribution is instead $-\sum_x a_x/12$ and the quartic trace changes with it. Both charts yield the same rational coefficient for every choice of pinned site. The expansion has an $O(s^4)$ remainder by the smooth nondegenerate Laplace expansion at the unique pinned minimum, with exponentially small complement. [NIST DLMF, modified Bessel asymptotics](https://dlmf.nist.gov/10.40) · [Both chart calculations and the cubic control](check.py)

## Executed checks

B4’s three-level PCP OS replay was rerun on the reviewed sources. The root, child and grandchild closed as Finished after post-exit readback. The regenerated Lean file had SHA-256 `c4346ff754c69096c70c67e04320ddf8d0fc44dc82f49d76bbdd0200818df033`. Lean accepted three finite arithmetic statements. One invalid worker request and three altered declarations were rejected. The two-link cycle reproduced relative errors $0.0062238286$ at $\beta=125$ and $0.00016924508$ at $\beta=64000$. These replays check B4’s own controls. Independently, running `python check.py` here with SymPy and mpmath verifies the pinned cofactor, both fourth-order calculations and the signed cubic directly from Wilson matrices. The uniform operator estimate is the analytic argument above. Independent director readback of the improvement is pending.

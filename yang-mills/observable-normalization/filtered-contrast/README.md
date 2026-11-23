# A local plaquette contrast with eleventh-power edge weight

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

B4's opposite-face contrast sees the lightest scalar band with weight proportional to the seventh power of the momentum radius. A further symmetric difference of three adjacent cube readings cancels its quadratic overlap amplitude. The first surviving amplitude is quartic. In a dense momentum grid or the spatial bulk the weight is proportional to the **eleventh power**, with a positive coefficient. This uses the volume-uniform amplitude estimate in [B4's orientation calculation](../../transfer-operator/girth-shell/orientation-contrast/) and the [strong-coupling vacuum band](../uniform-band/). The lattice spacing is fixed throughout.

Let $f_{y,i}$ denote the centered unnormalized fundamental plaquette trace at $y$ with normal $i$. Define $C_{y,i}=(f_{y,i}+f_{y+\hat e_i,i})/2$. For a real unit vector $h$ with $\sum_i h_i=0$ form the local observable
$$
 F_y=\sum_i h_i\left[\tfrac43 C_{y,i}-
             \tfrac16(C_{y+\hat e_i,i}+C_{y-\hat e_i,i})\right].
$$
Work in the isotropic four-dimensional SU(2) Wilson vacuum on even periodic spatial cubes of side $L\ge8$, or in their thermodynamic limit. Set $D=7/768$, fix $e>0$, $R=\sqrt{e/D}$, and measure the absolute connected spectral weight in the interval $I=[\Delta,\Delta+e\beta^4r^2]$ in lattice energy. In the joint limit $r\to0$, $\beta=o(r^2)$, with $Lr\to\infty$ or in the bulk,
$$
 \mu_F(I)\sim \frac{331}{26943840}\,\frac{R^{11}r^{11}}{6\pi^2}.
$$
The stronger coupling-to-radius hierarchy resolves the quartic amplitude against the inherited uniform $O(\beta^2)$ uncertainty in the interacting overlap.

## Checking the moving orientation

Write $c_i=\cos(k_i/2)$ and $x_i=1-c_i^2$. Up to a scalar diagonal and positive scale, the orientation matrix is $cc^T-\operatorname{diag}(c_i^2)$. Its top eigenvalue $l$ is simple near zero and tends to two. The normalized real eigenvector is proportional to $c_i/(l+c_i^2)$, with common normalization $N=\sqrt3+O(|k|^2)$. The eigenvalue solves
$$
 1=\sum_i(1-x_i)/(a-x_i),\qquad a=l+1=3-\tfrac23\sum_i x_i+O(|k|^4).
$$
The expansion follows by differentiating the displayed equation at $x=0$, where the derivative in $a$ is $-1/3$. The common phase coming from the cube center drops out of the norm. Opposite-face averaging contributes one more $c_i$. The unfiltered cube amplitudes are therefore $N(1-x_i)/(a-x_i)$. At $a=3$ the coefficient of $x_i$ in that quotient is $-2/9$. Terms independent of $i$ cancel. Thus the cube contrast has amplitude $-\sum_i h_i k_i^2/(6\sqrt3)+O(|k|^4+\beta^2)$, confirming B4's result by the secular equation. The uniform-ball average of its leading squared amplitude on the unit ball is $1/1890$.

The new local difference multiplies the $i$th amplitude by $1+(1-\cos k_i)/3=1+2x_i/3$. Its orientation-dependent factor becomes
$$
 H_i=\frac{(1+2x_i/3)(1-x_i)}{a-x_i}.
$$
Subtract two such quotients before expanding. The numerator of $3(H_i-H_j)(a-x_i)(a-x_j)$ is exactly
$$
 (x_i-x_j)\,[3-a-2a(x_i+x_j)+2x_ix_j].
$$
The constant part in the bracket vanishes at zero. Substituting the expansion of $a$, using $x_i=k_i^2/4+O(|k|^4)$, and restoring the normalization gives the compact-regulator amplitude, up to common phase,
$$
 H_h^{(4)}(k)+O(|k|^6+\beta^2),\qquad
 H_h^{(4)}(k)=\frac{|k|^2\sum_i h_i k_i^2-9\sum_i h_i k_i^4}{216\sqrt3}.
$$
Here the bounded local multipliers preserve B4's uniform $O(\beta^2)$ amplitude error. The secular calculation itself concerns the limiting orientation matrix. This distinction matters when the leading amplitude is small.

## Integration and long-lag check

After setting $p=k/r$, the rescaled amplitude converges uniformly on bounded $p$ to $H_h^{(4)}(p)$. B4's energy estimates squeeze the accepted top-branch momenta between balls with radii tending to $R$ and exclude the other branches. For $Lr\to\infty$ the local Fourier sum, divided by $r^3$, has measure element $d^3p/(2\pi)^3$. The boundary sphere has zero volume. For the bulk, take the torus limit at each fixed coupling and radius, squeezing the spectral projection between slightly enlarged and shrunken intervals. The uniform $O(\beta^6)$ error in the spectral edge shifts the rescaled energy boundaries by $O(\beta^2/r^2)$, which tends to zero.

The unit-ball average of $|H_h^{(4)}|^2$ is a permutation-invariant quadratic form in $h$. Its diagonal entries coincide and its off-diagonal entries coincide, so its value on all zero-sum unit contrasts is the same. Take $h=(1,-1,0)/\sqrt2$. Writing $p=(X,Y,Z)$, the numerator before division by $216\sqrt6$ is $-8X^4+8Y^4+X^2Z^2-Y^2Z^2$. The normalized ball moment of a monomial with even powers $b_i$ of total degree $b$ is $3\prod_i(b_i-1)!!/[(b+3)(b+1)!!]$, by spherical integration or the normalized moments of a rotationally invariant Gaussian. Squaring the four-term polynomial yields $331/26943840$. The ball volume and Fourier normalization give the coefficient in the statement.

There is a corresponding check using exact connected vacuum lags, $q_j=\langle F_0\Omega,S^j F_0\Omega\rangle$. Use G4's $t=(\beta/4)^4$ and quartic top center $b_*$. Write $v=j\beta^4$. In bulk or with $L/\sqrt v\to\infty$, assume $v\to\infty$ and $\beta v\to0$. Then
$$
 \frac{q_j}{(tb_*)^j}\sim
 v^{-11/2}(4\pi D)^{-3/2}\,
 \frac{3465}{16D^4}\,\frac{331}{26943840}.
$$
Indeed on the scale $p=\sqrt v\,k$, multiplication by $v^2$ extracts the quartic amplitude and $v^2\beta^2\to0$. Also $j\beta^6=v\beta^2\to0$, as required for the simple-branch power to converge to $e^{-D|p|^2}$. On a fixed small neighborhood the rescaled squared amplitude is bounded by $C(1+|p|^8)$; the Gaussian envelope controls its tails. The other upper branches there, and all momenta outside the neighborhood, contribute exponentially little in $v$, using bounded equal-time norm and the uniform separation. The dense-grid Gaussian sum then converges by truncation. In the limiting normalized Gaussian the radial eighth moment is $945/(16D^4)$, and conversion from unit-ball to unit-sphere angular average multiplies the degree-eight moment by $11/3$. These are fixed-mesh strong-coupling asymptotics. The continuum physical mass gap remains open. [G4's Gaussian envelope and volume passage](../../g4/local-scalar-edge/lags.md)

## Verification

The [exact-moment and numerical check](check.py) integrates a directly diagonalized symbol on shrinking balls. At radius 0.05 the scaled cube and filtered averages are 0.000529072 and 0.0000122811. B4's supplied control also passed on its separately determined energy boundary. Three host-dispatched [PCP OS guests](worker.c) tested the factored difference and the two ball moments before emitting the [Lean source](FilteredContrast.lean). A separate [three-guest replay](../transfer-increments/replay-guests.py) reproduced SHA-256 `b7226b9d60876941dfbbe56ba9adeb68e36a258974436985ef7fd30877c124db`. Eight-node product Gauss–Hermite quadrature independently reproduced the radial conversion. Lean 4.19.0 with pinned Mathlib checked the four supporting declarations with standard axioms. They cover the orientation identity, the contrast polynomial and its two moment constants. The spectral and joint-limit arguments use the stated analytic inputs.

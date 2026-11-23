# Two bounds on the actual Wilson transfer

Let $L\ge2$ be even. Write $V=L^3$, $E=P=3V$ for the numbers of sites, oriented positive spatial links and plaquettes. In units of one time step, put $A(U)=\sum_p\operatorname{Tr}(U_p)/2$. Each link has probability Haar measure on $SU(2)$. The temporal convolution has one-link density $e^{\beta\operatorname{Tr}(u)/2}/z(\beta)$, where $z(b)=2I_1(b)/b$, $z(0)=1$. Denote its product by $K$. The isotropic symmetric transfer is $T=D K D$, $D=e^{\beta(A-P)/2}$. Its restriction to vertex-gauge-invariant functions fixed by all three spatial center cuts has eigenvalues $\lambda_0>\lambda_1>0$. We seek $m=-\log(\lambda_1/\lambda_0)$. Positivity of every spin coefficient gives positivity of the operator. Its continuous strictly positive kernel on the compact orbit space makes the leading eigenvalue simple. [Lüscher, transfer matrix](https://bib-pubdb1.desy.de/record/396349)

## The cost of a one-step global contraction

Write $J(x,y)$ for the gauge- and center-averaged unnormalized temporal numerator. Its integrand is the exponential of $\beta$ times the sum of the unit-quaternion inner products between $x_e$ and $\epsilon_e g_v y_e g_{v+\hat i}^{-1}$. Independently integrate the site spins $g_v$ and average the eight seam choices $\epsilon$. Each edge connects distinct sites. Its inner product has Haar mean zero, so Jensen gives $1\le J\le e^{\beta E}$. The spatial half weights and the vacuum Doob transform multiply rows and columns by positive functions.

The projective diameter is the supremum of $\log[J(x,y)J(x',y')/(J(x,y')J(x',y))]$. The Hilbert-metric contraction factor is $\tau=\tanh(\Delta/4)$. The cross-ratio formula applies to the continuous kernel since orbit Haar measure has full support, so positive functions can concentrate on any pair of small neighborhoods. Linearizing at the strictly positive vacuum in an eigenfunction direction gives $\lambda_1/\lambda_0\le\tau$. Thus $m\ge-\log\tanh(\beta E/2)>0$ at finite $\beta>0$. [Birkhoff](https://www.ams.org/tran/1957-085-01/S0002-9947-1957-0087058-6/S0002-9947-1957-0087058-6.pdf) · [Bushell, projective contraction ratio](https://doi.org/10.1112/jlms/s2-6.2.256)

The obstruction can be measured on the original compact group. Compare $x_e=1$ and $y_i(v)=(-1)^{\sum_{j<i} v_j}1$. Every spatial plaquette of $y$ is $-1$, even after a cut. Both diagonal entries of $J$ equal the same ferromagnetic spin integral because $y$ is central. Put $R=J(x,x)/J(x,y)$. The two configurations give the projective minor $R^2$ for $J$ and for $T$.

For each seam twist the mixed action in unit spins $s_v\in S^3$ is $\frac12\sum_{a=1}^4\langle s^a,Bs^a\rangle$, where $B=\sum_i(S_i+S_i^*)$ and $S_i$ is the forward signed shift. Signs consist of the alternating factor in $y$ and a possible seam sign depending only on $v_i$. Interchanging different signed shifts, including a shift with another's inverse, introduces one minus sign. This follows by going around the intervening plaquette in either orientation. Even $L$ preserves the alternating signs at a wrap. Each shift is orthogonal, hence $B^2=\sum_i(S_i+S_i^*)^2\preceq12I$. The mixed maximum is at most $\sqrt3 V$, since $\sum_a\|s^a\|^2=V$.

For the untwisted two-cell let $H$ be the signed adjacency from its four even vertices to its four odd vertices, counting each cube edge once. Its three nonzero entries per row have magnitude one, and $HH^\mathsf{T}=H^\mathsf{T}H=3I$. Distinct rows sharing neighbors cancel by the negative plaquette sign. Give odd site $j$ the unit vector $e_j$ in $\mathbb R^4$ and even site $i$ the unit vector $H_{i,*}/\sqrt3$. Every signed cube bond then contributes $1/\sqrt3$. Repeating these spins with period two attains $\sqrt3 V$ on every even torus. The doubled bonds at $L=2$ are both present. Aligned spins attain $3V$ on the untwisted diagonal. [Lean cube identities](TwoSite.lean)

These maxima give a volume-uniform Laplace estimate. If each spin is within chordal distance $\eta\le1$ of its maximizing value, every bond changes by at most $2\eta$. A Haar cap has mass at least $c\eta^3$ by the $S^3$ polar measure. Retain the maximizing twist, with weight $1/8$. For either integral, with maximum $M$, this gives
$$
 \beta M-6\beta V\eta+V\log(c\eta^3)-\log8
 \ \le\ \log J\ \le\ \beta M .
$$
Taking $\eta=1/\beta$ yields
$$
 \frac{\log R}{\beta V}=3-\sqrt3+O((1+\log\beta)/\beta)
$$
uniformly in even $L$ as $\beta\to\infty$. In particular the **best** bound $-\log\tau$ from this one-step global diameter is at most $\log[(R+1)/(R-1)]$ when $R>1$. For sufficiently large $\beta$ it decays exponentially in $\beta L^3$. Such a bound supplies no physical gap uniformly in growing boxes at fixed cutoff. The same calculation gives no upper bound on the physical spectral gap. It singles out the loss incurred by demanding contraction for every pair of configurations, including very high magnetic energy endpoints.

## A spectral check independent of the projective minor

Let $u=I_2(\beta)/I_1(\beta)$. The largest nonvacuum eigenvalue of $K$ in the physical neutral sector is precisely $\kappa=u^4$. Peter–Weyl assigns spin $j$ the scalar $I_{2j+1}/I_1$ on each link. At a vertex with a single occupied link there is no invariant tensor. A nonempty occupied subgraph with fewer than four links and minimum degree two on the bipartite spatial graph must consist of two parallel edges. Three parallel edges never occur. The pair exists only at $L=2$ and winds once. Its two equal representations must have integer spin in the neutral sector. Their product is at most $(I_3/I_1)^2<u^4$ by the Bessel Turán inequality. The same inequality and $I_2/I_1<1$ imply successively decreasing one-link eigenvalues. Four or more occupied links give at most $u^4$, attained by tracing a fundamental contractible plaquette. [Baricz and Ponnusamy, Bessel inequalities](https://arxiv.org/abs/1010.3346)

Drop the common scalar $e^{-\beta P}$. The nonzero spectrum agrees with that of $K^{1/2} e^{\beta A} K^{1/2}$. Write $Z=\int e^{\beta A}dU$. Min–max gives $\lambda'_1\le\kappa e^{\beta P}$ and $\lambda'_0\ge Z$. Choose two different elementary plaquette traces as a two-dimensional trial space. They are orthogonal because some link occurs only once in their product. Both are odd under the central configuration $U\mapsto yU$ above. For each unit vector $f$ in their span, $\int A|f|^2=0$ and $\int e^{\beta A}|f|^2\ge1$. Hence $\lambda'_1\ge\kappa$. Finally $K$ is the constant projection plus a positive remainder of norm $\kappa$. In $e^{\beta A/2}K e^{\beta A/2}$ the rank-one term has norm $Z$, so $\lambda'_0\le\min(e^{\beta P},Z+\kappa e^{\beta P})$. This encloses the vacuum-subtracted excitation itself:
$$
 -\log\kappa+\log Z-\beta P\ \le m\le\
 -\log\kappa+\log \min(e^{\beta P},Z+\kappa e^{\beta P}).
$$

For an elementary numerical enclosure use $1+P\beta^2/8\le Z\le z(4\beta)^{P/4}$. For the lower bound, the same central transformation makes the law of $A$ symmetric, and distinct plaquette traces are orthogonal with single-plaquette second moment $1/4$ in our half-trace convention. For the upper bound, integrate one link at a time with Hölder exponent four for its four incident factors. After eliminating a link, each surviving factor is the fourth root of the integral of its fourth power over that link and all previously eliminated incident links. Completing this operation gives the product of the fourth norms, each $z(4\beta)^{1/4}$. The bound checks $m+4\log(\beta/4)\to0$ at fixed box as $\beta\downarrow0$. Neither estimate controls the weak-coupling, growing-volume spectral gap.

## Exact compact-group integration on the two-cell

At $L=2$ a negative center seam cancels the forward and wrapped terms on its direction. A subset of $k$ active axes leaves a signed or unsigned cube with **doubled** active edges. Permuting axes changes the chosen flux signs by a site gauge transformation on the cube with the same face fluxes. Integrating its four even spins gives
$$
 \mathbb E_{\rm odd}\prod_{a=1}^4 z(2\beta\sqrt{t_a}),\qquad
 t_a=\left|\sum_{j\sim a}\sigma_{aj}s_j\right|^2,\quad 0\le t_a\le k^2 .
$$
Average these quantities with weights $\binom3k/8$. The series of each factor is $\sum_{n\ge0}\beta^{2n}t_a^n/[n!(n+1)!]$. Every coefficient of the product after integration is nonnegative. To integrate the Gram monomials exactly, pair one occurrence of a chosen spin with each of its remaining occurrences. The uniform sphere moment of even degree $d$ divides this pairing sum by $d+2$ at each reduction in dimension four. Repeated arguments have their actual multiplicities. This follows by writing a standard four-dimensional Gaussian in polar coordinates and expanding its generating function.

[Exact coefficients through degree 36](coefficients.csv) begin with diagonal $1+3\beta^2+49\beta^4/8$ and mixed $1+3\beta^2+43\beta^4/8$. For a separate bound on the omitted coefficients replace every $t_a$ by $k^2$. Beyond the last majorant coefficient explicitly summed, the even coefficients are bounded by $(8k)^{2n}/(2n)!$ from the bounded total action of four independent even-site spins. A geometric bound on the factorial tail uses rational arithmetic throughout. Outward rounding gives:

| $\beta$ | Lower $R$ | Upper $R$ |
|---:|---:|---:|
| 1/8 | 1.0001871769 | 1.0001871770 |
| 1/4 | 1.0031940150 | 1.0031940151 |
| 1/2 | 1.0650411052 | 1.0650411053 |
| 3/4 | 1.4857870993 | 1.4858182415 |
| 1 | 3.2208559549 | 3.9742782161 |

The last bracket records the loss of precision at the chosen order. These are bounds on the square root of a projective minor. [Exact replay](cube.py)

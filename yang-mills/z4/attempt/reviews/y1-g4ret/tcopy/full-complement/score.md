# Readback of the spectator innovation estimates

Both auditors' proposed floors are below a bound we can derive directly for the original skeleton, all three spatial orientations and $\beta\ge1$. The first auditor's conservative value $1/1536$ follows. The second auditor's $4.479\times10^{-5}$ therefore holds as a weaker numerical inequality; the pasted summary did not include that vector-score derivation. Further numerical optimization is secondary to mixing of the full complement. The spectators' notes were supplied by the Principal, and are distinct from their previously posted GitHub comments. PR #25 was open at one auditor's cutoff and merged at ae3a0ac at the other's.

As in [the two-link proof](../coarse-plaquette-floor/score.md), write $Y=u^TOv$ with $O$ orthogonal and $u,v$ on the unit round three-sphere. The conditional log density $h$ is $\beta(Y+a\cdot u+b\cdot v)$ plus a constant, with five other incident faces per link. Write $p=\nabla_uY$, $q=\nabla_vY$, $A=\nabla_u\nabla_vY$. In either factor the weighted Hodge identity, integrated against $e^h$, gives
$$
 \|\operatorname{div}_h b\|^2+\|d b^\flat\|^2
 =\|\nabla b\|^2+\mathbb E[(\operatorname{Ric}-\nabla^2h)(b,b)]
 \le\|\nabla b\|^2+k\|b\|^2,\quad k=2+6\beta .
$$
The exterior derivative norm uses the usual antisymmetric-form inner product. Ricci equals $2g$, and the covariant Hessian of each half-trace in one factor is its negative times the metric. The estimate applies also to spectator tensor indices from the other factor, by conditioning and taking an orthonormal frame there. [Weighted Weitzenböck formula, Theorem 2.2](https://orbilu.uni.lu/bitstream/10993/53332/1/Covariant-RT.pdf)

The singular values of $A=P_uOP_v$ between the tangent planes are $1,1,|Y|$. Indeed the two hyperplanes have two common directions after the orthogonal identification, and the remaining principal cosine has magnitude $|u^TOv|$. Also $\nabla_u A=-g_u\otimes q$, $\nabla_v A=-p\otimes g_v$ and $\nabla_u\nabla_v A=Yg_u\otimes g_v$. Put $B=\operatorname{div}_{h,u}A$. Differentiation in the other factor gives $\nabla_vB=C+D$ with $C=\operatorname{div}_{h,u}(\nabla_vA)$ and $D=\beta A^TA$, since only the common face has a mixed log-density Hessian. With $m=\mathbb EY^2$ the one-factor inequality gives
$$\|B\|^2\le3(1-m)+k(2+m),\quad
 \|C\|^2\le9m+3k(1-m),\quad \|D\|^2\le3\beta^2.$$
For $Z=\operatorname{div}_{h,v}B$, the same inequality gives $\|Z\|^2\le k\|B\|^2+\|C+D\|^2$. The sum $k\|B\|^2+\|C\|^2$ is bounded by $2k^2+6k+(k-3)^2m\le3k^2+9\le201\beta^2$. Also $\|C\|^2\le3k\le24\beta^2$. Hence $\|Z\|^2\le(204+12\sqrt2)\beta^2<256\beta^2$. The two adjoints pair with the full measured sum with modulus $\beta|c_p|\mathbb E(2+Y^2)$. The conditional variance is at least $|c_p|^2/64$. Averaging 24 colours gives $1/1536$; all square-integrable coarse-measurable coefficient and joint coarse-addition quantifiers of PR #25 are preserved. The beta restriction matters: at beta zero the unscaled test is $9Y$.

In the two-link control with zero external staples, $Z=9Y+\beta(7Y^2-4)-\beta^2Y(1-Y^2)$ and $Y$ has density proportional to $e^{\beta y}\sqrt{1-y^2}$ on $[-1,1]$. Changing to $s=\beta(1-y)$ makes quadrature stable at large $\beta$. The program recomputes the six ratios in the supplied table, checks $\mathbb EZ=0$ and $\mathbb E[(Y-1)Z]=2+\mathbb EY^2$, and checks the limiting approach to $\sqrt6$. This tests one conditional model. The uniform statement uses the analytic inequality. [Independent quadrature and matrix controls](checks.py)

# A thin SU(2) Wilson loop can retain unit variance and lose even its next-slice correlation

Director A4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Consider the isotropic Wilson measure on a periodic four-dimensional lattice with each side at least three and normalized probability proportional to $\exp[(\beta/2)\sum_f\operatorname{ReTr}U_f]$ relative to product Haar measure, $\beta\ge0$. Let $F=\operatorname{Tr}W$ for a deterministic closed spatial contour using $L$ distinct unoriented edges exactly once. Put $\epsilon=\exp[-L/(19(4\beta+1))]$. The following estimates are uniform in volume:

$$|\mathbb EF|\le2\epsilon,\qquad |\mathbb E F^2-1|\le3\epsilon,\qquad
|\operatorname{Cov}(F,G)|\le2\epsilon\sqrt{\operatorname{Var}G}.$$

The last estimate holds for every square-integrable real observable on a different time slice. More generally, it holds when $G$ uses none of the selected contour links specified below. It controls the covariance even if the second observable varies with the cutoff.

A perimeter upper bound for Wilson loop expectations is a classical theorem of Simon and Yaffe. Conditional link integration also underlies the lattice multihit method. We use these established ideas to test whether a thin spatial loop can provide the finite, nonzero, time-separated observable required by this research program. The explicit coupling dependence, adjoint estimate and conditioning are needed for that inference. [Simon and Yaffe (1982)](https://doi.org/10.1016/0370-2693(82)90815-2) · [Application of link integration to non-cofacial links](https://cds.cern.ch/record/268170/files/arXiv%3Ahep-lat_9409005.pdf)

## Conditional law and explicit rate

One link enters six plaquettes. With the other links fixed its normalized-trace action is an inner product of its unit quaternion with a sum of six unit staple quaternions, multiplied by $\beta$. Change variables by the fixed direction of that sum so its density becomes proportional to $e^{hx}$ with $0\le h\le6\beta$ and $x$ the scalar part. Zero staple gives Haar. The density of $x$ is proportional to $e^{hx}\sqrt{1-x^2}$ on $(-1,1)$. The two matrix means in the defining and adjoint representations of the rotated link are scalar by conjugation invariance. Their scalars are respectively

$$r=\mathbb E_h x,\qquad s=\mathbb E_h(4x^2-1)/3.$$

Restoring the staple direction multiplies each mean by its unitary representation matrix. An inverse traversal takes the adjoint, preserving its norm. For $h>0$, integrating the derivatives of $e^{hx}(1-x^2)^{3/2}$ and $xe^{hx}(1-x^2)^{3/2}$ gives

$$3r=h\mathbb E_h(1-x^2),\qquad 3s=h\mathbb E_h[x(1-x^2)].$$

The endpoints vanish and both derivatives are integrable. Pairing $x$ and $-x$ gives $0\le s\le r$; both vanish at $h=0$. Since $1-x^2\le2(1-x)$, we get $r\le2h/(2h+3)\le q:=1-1/(4\beta+1)$. Numerically integrating the conditional density and comparing with $I_2(h)/I_1(h)$ and $I_3(h)/I_1(h)$ checks the fundamental and adjoint normalizations separately.

## Condition on the other links

In the graph of contour edges join two distinct edges whenever a plaquette contains both. Each edge belongs to six squares with three other edges apiece. A greedy independent set has size $k\ge L/19$. Condition on the complement of these $k$ selected links. The selected links are conditionally independent because no action face uses two of them. All staples in their conditional densities are fixed by this conditioning.

In the ordered product for $W$, replace each selected link matrix by its conditional mean in the same position. Independence and single occurrence justify the replacement entry by entry, regardless of matrix commutation. The remaining factors have norm one. In the two representations the conditional character bounds are $2q^k$ and $3q^k$, each bounded by its dimension times $\epsilon$. For SU(2), $F^2=1+\operatorname{Tr}_{\rm adj} W$. This proves the first two estimates and $1-3\epsilon-4\epsilon^2\le\operatorname{Var} F\le1+3\epsilon$. For an exterior $G$, use the covariance with $\mathbb E[F\mid\text{complement}]$, whose variance is at most $4\epsilon^2$. Backtracking illustrates why edge visits cannot be counted as independent factors: at $\beta=0$, $UU^{-1}$ has trace two even though the link mean is zero.

## Consequence along a regulator trajectory

Whenever $L/(1+\beta)\to\infty$, the thin loop has variance tending to one, while its centered covariance with any uniformly bounded-variance observation on another slice tends to zero. This includes a single temporal lattice step and any distinct slice approximating a fixed positive physical separation. For a contour with $Lh\to\ell>0$ as spatial spacing $h\to0$, the sufficient condition is $h(1+\beta)\to0$. This is a conditional statement about the chosen scale-setting map.

Multiplying the centered loop by a cutoff-dependent scalar while keeping its equal-time variance bounded cannot rescue such a time-separated covariance: its unscaled variance tends to one, forcing the multiplier to remain bounded. This rules out **this** finite-norm witness, including a unit-variance normalization. It allows observables with spatial or temporal smearing and renormalization schemes with divergent equal-time norm. It provides no mass-gap bound.

If a separate zero-temperature transfer construction gives the positive spectral representation of the same centered loop, then after unit normalization $C(a)=\int e^{-aE}\,d\mu(E)\to0$ for a probability measure at each cutoff. Consequently $\mu\{aE\le R\}\le e^R C(a)\to0$ for each fixed $R$. In this specific sense the loop’s spectral weight escapes even beyond energy scales of order $1/a$. The finite time-circle covariance proof above does not require a vacuum spectral representation.

## A different obstruction for an elementary plaquette

For a single unnormalized plaquette $F_0$ on a slice, the two-link proof of the [equal-time lower bound](../wilson-variance/) works with the exterior links fixed. With $b_\beta=(4/99)e^{-15/4}\sin^4(1/(4\sqrt{1+\beta}))$ the conditional variance is at least $b_\beta$; one could omit the previous coloring loss for this single face. Hence every predictor using only the remaining links has mean squared error at least $b_\beta$. Choosing the same plaquette on the next time slice gives $2D=\mathbb E(F_1-F_0)^2\ge b_\beta$. Since $0<V=\operatorname{Var} F_0\le4$, the normalized one-step loss satisfies $D/(aV)\ge b_\beta/(8a)$. On any trajectory with $a(1+\beta)^2\to0$ it diverges. Thus a bounded one-step defect per unit physical time fails for this observable under that hypothesis.

Here divergence of the first scaled defect alone does **not** establish that the time-separated correlation vanishes. For instance a spectral law with mass $1-\sqrt a$ at energy one and $\sqrt a$ at energy $a^{-2}$ has a divergent scaled defect and a limiting correlator $e^{-t}$ for $t>0$. The stronger decorrelation statement for long thin contours comes from conditioning on many distinct links.

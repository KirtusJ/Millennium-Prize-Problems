# A regulator transfer bound for two coupled sectors

Director B4 · 22 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

A lower bound on the transfer defect in each of two orthogonal sectors can disappear when the sectors couple. This note gives an exact determinant test for the comparison form, a family of positive transfer operators that loses its physical gap, and an explicit lower bound in the parent program’s one-link SU(2) model. The Wilson-lattice estimates needed to apply the test in four dimensions remain open. [Lean declarations](TwoSector.lean) · [Execution record](execution.md) · [Jaffe–Witten, §4](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## What the regulator must supply

Let $a>0$ be one step of physical time. On the gauge-invariant Hilbert space at a fixed cutoff and volume, let $T$ be a positive self-adjoint contraction fixing the normalized vacuum. Write $D=I-T$. Split every vector orthogonal to the vacuum as $p+q$ in two fixed orthogonal subspaces. Suppose the following estimates hold for **all** such $p,q$:

$$
\begin{aligned}
\operatorname{Re}\langle p,Dp\rangle&\ge a u\|p\|^2,\\
\operatorname{Re}\langle q,Dq\rangle&\ge a v\|q\|^2,\\
\operatorname{Re}\big(\langle p,Dq\rangle+\langle q,Dp\rangle\big)&\ge-2ac\|p\|\|q\| .
\end{aligned}
$$

Take $c\ge0$. If $m>0$, $u>m$ and $c^2\le(u-m)(v-m)$, the full defect is at least $am\|p+q\|^2$. To see where the threshold comes from, put $x=\|p\|$, $y=\|q\|$ and complete the square:

$$
(u-m)\big[ux^2-2cxy+vy^2-m(x^2+y^2)\big]
=\big((u-m)x-cy\big)^2+\big((u-m)(v-m)-c^2\big)y^2.
$$

The test is exact for this scalar form when $u>m$. Necessity follows by setting $(x,y)=(c,u-m)$. These are admissible nonnegative norms. A particular operator may enjoy better estimates than those three constants express. The Lean file proves the scalar equivalence and the complex inner-product bound after recombining the two sectors. The pivot boundary $u=m$ is outside the equivalence as stated.

For a positive spectral value $r$ of $T$ on the excited space, the form bound gives $r\le 1-am$ by the spectral theorem. Thus $-\log(r)/a\ge m$ by $\log r\le r-1$. The scalar logarithmic implication is checked in Lean. The spectral theorem application is the analytic interface here, including when the spectrum is continuous. To pass a positive mass to the reconstructed theory, the **same** $m$ must work along the intended joint trajectory in volume, lattice spacing and coupling, in the time normalization used for the limiting correlators. [D4’s continuum lane and A4’s nontriviality lane](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1)

## A positive family that loses the gap

Use a separate one-dimensional vacuum on which $T_a=1$. On the two-dimensional excited space set

$$D_a=a\begin{pmatrix}1&-(1-a)\\-(1-a)&1\end{pmatrix},\qquad T_a=I-D_a,\qquad 0<a\le\tfrac12.$$

The two diagonal sectors each have defect $a$ per unit vector. The symmetric direction has transfer eigenvalue $1-a^2$, and the antisymmetric direction has eigenvalue $(1-a)^2$. Both are strictly between zero and one. The vacuum is unique at each cutoff. Nevertheless the lowest physical energy satisfies

$$0<-\frac{\log(1-a^2)}{a}\le 2a.$$

This excludes every uniform positive floor. It also explains why two positive block measurements cannot settle the question without an estimate on their coupling. The adverse family is a finite-dimensional transfer model. Its matrix action is explicit above. Lean checks the two directional forms, the ordering and positivity of the two scalar transfer values, and the failure of a uniform lower bound.

## A quantitative test on the parent program’s SU(2) model

For the central convolution of E2 §1, the first excited transfer value is $r=I_2(g)/I_1(g)$ and the scaled energy is $-g\log r$, where $g>0$. E2 orders the higher modes by their Bessel ratios. Its semigroup parameter is dimensionless. Here one can bound the gap at every $g$ without a large-$g$ expansion. [Pinned E2 source, §§1 and 8](https://github.com/KirtusJ/From-Prephysical-Hypotheses-to-Physical-Models/blob/aca29276aa180af3c81ccc9f3aa06b4e2ae4d404/edition/PAPERS/E2_Compact_Group_Transfer_Spectra_and_Ultraviolet_Operator_Limits/source/01_editable_Compact_Group_Transfer_Operators.md)

Give $t\in[-1,1]$ the probability density proportional to $e^{gt}\sqrt{1-t^2}$. Differentiating the integral representation of $I_1(g)/g$ and using $I_1'=I_2+I_1/g$ gives $\mathbb E[t]=r>0$. Differentiation under the integral is justified on each compact $g$-interval by bounded $t$ and an integrable weight. Put $s=\mathbb E[t^2]$. The derivative of $e^{gt}(1-t^2)^{3/2}$ integrates to zero because both endpoint values vanish. Consequently $g(1-s)=3r$, while $s\ge r^2$ by nonnegative variance. [DLMF 10.32.2](https://dlmf.nist.gov/10.32.E2) · [DLMF 10.29](https://dlmf.nist.gov/10.29)

It follows that $3r\le g(1-r^2)\le 2g(1-r)$, and therefore

$$-g\log r\ \ge\ g(1-r)\ \ge\ \frac{3g}{2g+3}.$$

For $g\ge 1$ this gives a uniform floor of $3/5$. The bound tends to $3/2$, which agrees with E2’s first excited limiting energy. Lean checks the implication from the moment hypotheses. The integral representation, its link to the spectrum and integration by parts are justified in prose above. This calculation uses one compact group variable. It provides no control of spatial plaquettes, the infinite-volume spectrum or the physical clock of four-dimensional gauge theory.

## What would advance the Yang–Mills claim

Fix the Wilson action, the transfer operator in its gauge-invariant vacuum representation, and a trajectory of bare couplings with a physically normalized time spacing. Pick explicit projections that exhaust the excited space. A substantive next bound would control the off-diagonal defect $P(I-T)Q/a$ along that trajectory while independently bounding both diagonal forms. The determinant test then identifies exactly how large the coupling estimate can be. If the resulting $m$ tends to zero as the spatial volume grows, this route fails to certify a mass gap even when every finite lattice passes.

The November 10 assessment of the October 28 construction reports a Wightman scaling limit and explicitly leaves the mass gap open. The assessors list later submissions as under examination. Their October finding does not identify the required uniform Wilson transfer estimate. No continuum mass gap or Millennium solution is claimed here. [Dated assessment, §1](https://alexisdpc.github.io/yang-mills/references/assessment-1-2026-11-10.pdf) · [Submission register](https://github.com/yang-mills-group/YM)


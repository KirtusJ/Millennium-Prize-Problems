# Measuring scalar mixing in a conserved energy density

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

In a positive-energy, Poincaré-invariant vacuum theory, three nonzero spatial momenta suffice to separate the tensor, scalar and real cross contributions to the connected covariance of $O=T^{00}+S$. Here $T$ is a symmetric conserved tensor, $S$ a Lorentz scalar, and their unknown normalization factors have been absorbed into the fields. The inputs are positive-time autocorrelations of **one** observable. A positive integral of each measured curve brings the three energy dispersions to a common momentum before taking differences. A version with smooth spatial tests of fixed physical size avoids exact plane-wave measurements. [Wave packets](packets.md) · [Finite readings and error bounds](transport.md)

The assumptions concern an infinite-volume covariant limit with the usual joint spectral disintegration and finite correlators at every strictly positive time for the chosen momenta or packets. Vacuum contributions at four-momentum zero are excluded. Application to the original four-dimensional Wilson histories requires control of these limits for the same fields, normalizations and clocks. No signal floor, continuum construction or mass gap on that trajectory follows from the separation formula.

## What changes with a boost

Set $u=|\mathbf p|^2>0$, let $s\ge0$ be invariant mass squared, and write
$$
 f_s(u,t)=\frac{e^{-t\sqrt{s+u}}}{2\sqrt{s+u}} .
$$
There are positive measures $A,B$ and a real signed cross measure $X$ such that
$$
 C_O(u,t)=\int f_s(u,t)\,[u^2\,dA(s)+2u\,dX(s)+dB(s)] .
$$
The $2\times2$ matrix measure with diagonal $A,B$ and off-diagonal $X$ is positive. For timelike $s$ take the momentum along axis three. In its rest frame conservation makes the time row of $T$ vanish on the vacuum spectral fiber. After the boost, $T^{00}$ contributes $u/s$ times the rest-frame $T^{33}$ amplitude; the scalar amplitude stays fixed. The invariant shell measure supplies the factor $1/(2\sqrt{s+u})$. Rotations allow the same measures at every direction. On the open null cone, start at a reference momentum $(1,0,0,1)$. Conservation and symmetry give equal $00,03,33$ amplitudes. A longitudinal boost multiplies the $00$ amplitude by $u$ and preserves the scalar amplitude. Thus the three powers also apply at $s=0$. The real Gram measure of the two amplitudes proves positivity and permits a negative cross term. The tensor coefficient can include the trace sector of the conserved tensor. [Single-field shell derivation](../lorentz-test/shells.md)

## Recovering the three contributions

Take $u_i=u+ih$ for $i=0,1,2$, with $u,h>0$. For a time curve $C$ define the positive operator
$$
 K C(t)=\frac12\int_t^\infty x C(x)\,dx,\qquad
 P_a C(t)=\sum_{n\ge0}\frac{a^n}{n!}K^n C(t).
$$
It changes $f_s(u_i,t)$ into $f_s(u_i-a,t)$ for $0\le a<u_i$. It leaves each spectral coefficient multiplying the shell unchanged. In particular
$$
 Y_i=P_{ih}C_O(u_i,\cdot)(t)=u_i^2 A_t+2u_i X_t+B_t,\quad
 (A_t,X_t,B_t)=\int f_s(u,t)\,(dA,dX,dB).
$$
All three $Y_i$ are computable from positive inputs even when $X$ is negative. With $\Delta=Y_1-Y_0$ they give
$$
 A_t=\frac{Y_2-2Y_1+Y_0}{2h^2},\qquad
 X_t=\frac{\Delta-(2uh+h^2)A_t}{2h},\qquad
 B_t=Y_0-u^2 A_t-2uX_t .
$$
A fourth shifted reading must lie on the same quadratic. The recovered entries must satisfy $A_t,B_t\ge0$ and $X_t^2\le A_t B_t$. Since $f_s(u,t)>0$, a vanishing scalar diagonal at one such time implies zero excited scalar measure and hence zero cross measure. A positive scalar diagonal detects a scalar component in the proposed decomposition. The recovered entries include the fields' squared normalizations and the real interference. An arbitrary rescaling of a component and its coefficient cannot be identified separately.

Two momenta are in general insufficient, even with exact readings at every time. On one invariant shell start from the identity Gram and perturb its quadratic by $\epsilon(v-u_0)(v-u_1)$. A sufficiently small nonzero $\epsilon$ preserves positive definiteness, changes the constant coefficient, and preserves both entire curves. The two-clock identification in [free Maxwell theory](../maxwell-benchmark/) uses its independently known spectral shapes and zero cross measure.

For a pure conserved energy, $J(u,t)=C_O(u,t)/u^2$ obeys $\partial_u\partial_t J=tJ/2$. A derivative-free check is that the rectangular increment $J(u_2,t_2)-J(u_2,t_1)-J(u_1,t_2)+J(u_1,t_1)$ equals the integral of $tJ(u,t)/2$ over that rectangle. Since $J$ decreases in both coordinates, the increment lies between the two opposite-corner readings multiplied by $(u_2-u_1)(t_2^2-t_1^2)/4$. This check can reject a proposed identification using separated times alone.

## Testing invariant mass after separation

Let $G(t)$ be the recovered matrix with entries $A_t,X_t,B_t$ and let $G_{<}(t)$ restrict its positive matrix measure to $s<m^2$ for a trial $m>0$. For any $\tau>0$ set $d=e^{-\tau\sqrt{u+m^2}}$ and $z=e^{-\tau\sqrt u}$. Splitting the measure gives the matrix inequality
$$
 (z-d)\,G_{<}(t)\succeq G(t+\tau)-d\,G(t).
$$
It suffices to apply the scalar integral inequality to each quadratic form. A positive direction on the right certifies a quantitative amount of subthreshold weight in that direction. Both diagonal tests can fail to detect it when the cross correlator selects a low-energy linear combination. For the packet version replace $u$ by the lower edge $l$, since every energy is $\sqrt{v+s}$ with $v\ge l$.

At fixed $u$, the gap $s\ge m^2$ in **these two fields' excited measures** is equivalent to $G(t+\tau)\preceq dG(t)$ along the entire grid $t=t_0+n\tau$. Necessity follows on each shell. For sufficiency iterate on the trace. Weight in any compact subinterval below $m^2$ would give a strictly slower exponential than the iterated upper bound. Positivity of the matrix measure then removes the cross measure there as well. The packet criterion has the same converse if $l$ is the actual lower edge of the profile support: every neighborhood immediately above $l$ must have positive packet weight. Finite readings can contradict a proposed gap. An upper decay bound along the whole grid is an additional dynamical requirement. [Formal coverage and independent controls](execution.md)

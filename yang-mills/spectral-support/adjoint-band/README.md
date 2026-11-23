# A positive-energy band for the adjoint plaquette

Director D4 · November 22, 2026 · B.C. Pacific Time (UTC−07:00)

At fixed spatial mesh, the adjoint plaquette of the interacting $SU(2)$ Hamiltonian has spectral weight at energies at least $\kappa/576$, for every finite magnetic coupling and every periodic cubic box of side at least three. The upper endpoint and guaranteed weight are explicit and independent of the box. The observable is measurable on one $SO(3)$ plaquette at a single time. Its correlators therefore also describe the exact quotient pushforward of this cover theory. [C4’s adjoint observable](../../central-quotients/local-response/adjoint-weight.md) · [A4’s Hamiltonian and kinetic estimate](../../observable-normalization/hamiltonian-variance/)

Use the unit-round product metric on the links and $H=-(\kappa/4)\Delta+\lambda\sum_q(1-x_q)$ with $\kappa>0$, $\lambda\ge0$, and $x_q=\operatorname{Tr}(U_q)/2$. Let $\Omega$ be the normalized positive vacuum, $Q=H-E_0$, $x=x_p$, $F=2x$, and $F_A=4x^2-1$. For a real observable $O$, let $\nu_O$ be the $Q$-spectral measure of $(O-\langle O\rangle)\Omega$, with $M_{j,O}=\int E^j\,d\nu_O$. Define

$$
g=\lambda/\kappa,\quad B=\min(g,17\sqrt g/8+3/16),\quad
A=\frac{4\kappa}{(1+\sqrt B)^2},\qquad
D=\kappa^2\min\{(24+16\sqrt B)^2,(4\sqrt{86401}+8)^2\}.
$$

Then
$$
L=\max\{A/16,\kappa/576\},\qquad U=2D/A,\qquad
\nu_{F_A}([L,U])\ge w=\frac{A^2}{2D}.
$$

The bounds concern a component of this particular observable. The rest of its spectrum can reach arbitrarily close to zero as the box grows. On spatial refinement the guaranteed mass can decay and the upper endpoint can diverge. Existence and a common lower mass gap for four-dimensional continuum Yang–Mills remain open. [Jaffe and Witten’s problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## First moment from a one-link identity

With the other links fixed, the plaquette holonomy is an isometric coordinate on the selected link. The normalized real trace $x$ is the first coordinate of the unit three-sphere, so $|\nabla_e x|^2=1-x^2$ and $\Delta_e x=-3x$. On this link put $W=x(1-4x^2/3)\nabla_e x$. Direct differentiation gives
$$
\operatorname{div}_e W=1-8x^2(1-x^2),\qquad |W|^2\le x^2(1-x^2).
$$
Write $J=\langle x^2(1-x^2)\rangle$. Integration by parts with the density $\Omega^2$ and $\|\nabla_e\Omega\|^2\le4B$ imply $1\le8J+4\sqrt{BJ}$. Since $\sqrt J\le1/2$, the right side is at most $4(1+\sqrt B)\sqrt J$. The ground-state Dirichlet identity gives $M_{1,O}=(\kappa/4)\langle|\nabla O|^2\rangle$. Summing the four links therefore yields $M_{1,F_A}=64\kappa J\ge A$. In particular this lower bound requires only local kinetic control.

There is an exact cross-check using both character channels. Set $S=\langle1-x^2\rangle$ and $Z=\langle(1-x^2)^2\rangle$. Then $M_{0,F_A}=16(Z-S^2)$, $J=S-Z$, and $M_{1,F}=4\kappa S$. Consequently
$$
 M_{0,F_A}+\frac{M_{1,F_A}}{4\kappa}
 =16S(1-S)=4\frac{M_{1,F}}{\kappa}-\left(\frac{M_{1,F}}{\kappa}\right)^2.
$$
The adjoint variance is at most $4$ by its range $[-1,3]$, and at most $16S$ by this identity. For $g\le1$, $S(1+B)\le2$. For $g\ge1$, the potential-energy trial bound gives $gS\le2B$, and $B\le5\sqrt g/2$, $1+B\le7\sqrt g/2$ imply $S(1+B)\le35/2$. Thus $M_{0,F_A}\le K=\min(4,576/(1+\sqrt B)^2)$, using $(1+\sqrt B)^2\le2(1+B)$. At $g=0$, product Haar measure gives $(M_0,M_1,M_2)=(1,8\kappa,64\kappa^2)$. [A4’s trial and moment estimates](../../observable-normalization/hamiltonian-variance/excited-band/third-moment/)

## Second moment and band extraction

Let $f=F-\langle F\rangle$, $f_A=F_A-\langle F_A\rangle$, and $\gamma=\kappa/4$. The product rule on the smooth compact-group domain gives
$$
 Q(f_A\Omega)=2FQ(f\Omega)-2\gamma|\nabla F|^2\Omega.
$$
The potential commutes with multiplication by $F$. Since $|F|\le2$ and $|\nabla F|^2=16(1-x^2)$, the triangle inequality yields $\sqrt{M_{2,F_A}}\le4\sqrt{M_{2,F}}+8\kappa$. A4’s fundamental estimate is $M_{2,F}\le86401\kappa^2$. Independently, on the four incident links, $\Delta F_A=-32 F_A$, $|\nabla F_A|\le8$, and $\|\nabla_{\!p}\Omega\|\le4\sqrt B$. Applying the product rule directly gives $\sqrt{M_{2,F_A}}\le\kappa(24+16\sqrt B)$. Taking both bounds gives $D$. [Fundamental second moment](../../observable-normalization/hamiltonian-variance/excited-band/third-moment/)

For any finite positive measure with moments $M_0\le K$, $M_1\ge A>0$, $M_2\le D$, Cauchy–Schwarz gives $A^2\le KD$. Take $L=A/(4K)$ and $U=2D/A$. These satisfy $0<L<U$. On all real energies,
$$
 (E-L)(U-E)\le \frac{U^2}{4}\mathbf 1_{[L,U]}(E).
$$
The expectation of the left side is $(U+L)M_1-M_2-LU M_0\ge 2D-D-D/2=D/2$. Dividing gives the stated $w$. For the adjoint cap above, $A/(4K)=\max(A/16,\kappa/576)$. Using just the range bound $K=4$ already halves the earlier upper endpoint and quadruples the guaranteed mass in A4’s fundamental-observable estimate with its own $A,D$. [Fundamental interval](../../observable-normalization/hamiltonian-variance/excited-band/) · [Machine-checked measure inequalities](AdjointBand.lean)

For $C(t)=\int e^{-tE}\,d\nu_{F_A}$, $t\ge0$, and $s>0$, the band bounds the second time difference below by $w e^{-tU}(1-e^{-sL})^2$. Every zero-energy state contributes exactly zero to this difference. At fixed couplings, $M_2\le D$ gives tightness, and the closed-set Portmanteau inequality passes the band floor to every weak spatial-volume limit. At large $g$ and fixed $\kappa$, the guaranteed lower endpoint stays of order $\kappa$, the upper endpoint grows of order $\kappa\sqrt g$, and $w$ falls of order $1/g$. [Fixed-time difference](../positive-time/vacuum/) · [Wilson time and spatial-volume limits](wilson-limit.md)

The energy-weighted local adjoint probability $P_A^{(1)}(dE)=E\,d\nu_{F_A}/M_{1,F_A}$ consequently obeys $P_A^{(1)}([0,E_*])\le144E_*/\kappa$, since $M_{0,F_A}/M_{1,F_A}\le K/A\le144/\kappa$. Also $\int e^{-tE}\,dP_A^{(1)}\le144/(e\kappa t)$ for $t>0$. These estimates apply under any multiplicative rescaling of the observable. As the electric coefficient diverges in physical units, the energy-weighted law loses all mass below every fixed physical energy. The fraction of *raw, variance-normalized* weight at those energies remains undetermined. C4 reports a corresponding $1024 E_* N_c/\kappa$ bound for interfering adjoint plaquettes, where $N_c=\|c\|_1^2/\|c\|_2^2$. [C4’s multiple-plaquette calculation](../../central-quotients/momentum/adjoint-refinement.md) · [A4’s corresponding fundamental-smearing result](../../observable-normalization/smeared-plaquettes/moment-bounds/refinement.md)

[Peer calculations and controls](review.md) · [Native generation and Lean replay](execution.md)

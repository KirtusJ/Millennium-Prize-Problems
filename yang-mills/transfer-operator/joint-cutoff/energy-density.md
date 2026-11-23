# Testing finite-energy weight of the smeared total energy in Wilson boxes

Director B4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

A4's smeared total energy combines an unbounded electric term with a bounded magnetic term. Its uniform first spectral moment on a bare refinement allows two failure modes: weight can escape to arbitrarily high energies, or accumulate near zero. **Three positive-time readings with bounded Wilson transfer insertions test whether any of the first-moment weight survives in a compact interval of positive physical energies.** The time spacing and the electric representation cutoff can both be chosen from the parameters of each box, at arbitrary finite magnetic coupling. The test gives an equivalence and an error estimate. The sign of its limiting signal on the weak bare-coupling trajectory remains undetermined. [A4's energy density](../../observable-normalization/energy-density/README.md) · [Spatial limit and moment budget](../../observable-normalization/energy-density/spatial-limit.md)

The [uncapped Wilson construction](../periodic-time/) now implements the full electric insertion with ordinary functions of links and gives explicit finite-period and integration errors. The [stress-tensor check](../periodic-time/stress-test-review.md) uses the same physical clock across dyadic resolutions and covers unequal electric and magnetic normalizations.

## Three positive times

In a finite spatial box let $H=H_0+W$, $Q=H-E_0$, $\Omega$ its unit vacuum and $v=O\Omega$ for the weighted total-energy insertion $O$. Let $C(u)=\langle v,e^{-uQ}v\rangle$. For any fixed physical $t>0$,
$$
D(t)=C(t)-2C(2t)+C(3t)=\langle v,X(I-X)^2v\rangle,\qquad X=e^{-tQ}.
$$
Centering gives the same answer because the polynomial vanishes at one. If $\nu$ is the raw spectral measure and $\mu(dE)=E\nu(dE)$ its first-moment measure, then $D(t)=\int f_t\,d\mu$ with $f_t(E)=e^{-tE}(1-e^{-tE})^2/E$ for $E>0$ and $f_t(0)=0$. The function is positive on $(0,\infty)$ and vanishes at both endpoints. If $\mu([0,\infty))\le C_*$, then for $0<l<R$,
$$
D(t)\le t^2l C_*+t\,\mu([l,R])+e^{-tR}C_*/R,\qquad
D(t)\ge \min_{[l,R]} f_t\,\mu([l,R]).
$$
The estimates follow from $1-e^{-tE}\le\min(1,tE)$. A persistent lower bound $D(t)\ge\delta>0$ thus forces persistent first-moment mass on a common band: choose $l,R$ with the two tails adding to at most $\delta/2$, and the band carries at least $\delta/(2t)$. Conversely a persistent band gives a persistent reading. The same criterion holds on any specified subsequence. Two readings $C(t)-C(2t)$ alone can miss the low-energy failure: $\nu_n=n\delta_{1/n}$ has unit first moment and its two-reading difference tends to $t$ while $D_n(t)\to0$. [A4's uniform energy budget and D4's time-difference filter](../../observable-normalization/energy-density/spatial-limit.md)

## Capping an electric insertion

On the unit-round SU(2) product let $h_e=\gamma(-\Delta_e)$, $H_0=\sum_e h_e$ and $W=\lambda\sum_p(1-\phi_p)$ with $\phi_p=\operatorname{Tr}U_p/2$. Here $\gamma=\kappa_A/4=1/(2\kappa_B)$ in the two directors' conventions. Put $N=3L^3$, the number of edges and also of faces, and $B=2\lambda N$. In a finite box $0\le E_0,W\le B$ and $H_0\Omega=(E_0-W)\Omega$. The product rule on the smooth vacuum gives
$$
H_0^2\Omega=(E_0-W)^2\Omega-(H_0W)\Omega+2\gamma\nabla W\cdot\nabla\Omega .
$$
On one face each of its four link Casimirs acts on $\phi_p$ by 3. Each edge belongs to four faces and $|\nabla_e\phi_p|\le1$. Thus $\|H_0W\|_\infty\le12\gamma\lambda N$, $\|\nabla W\|_\infty\le4\lambda\sqrt N$, and $\|\nabla\Omega\|_2\le\sqrt{B/\gamma}$. In particular
$$
\|H_0\Omega\|\le B,\qquad
\|H_0^2\Omega\|\le J_0:=B^2+12\gamma\lambda N+8\lambda\sqrt{\gamma N B}.
$$

For the energy probe $O=\sum_e w_e h_e+\sum_p w_p\lambda(1-\phi_p)$ put $A_w=\sum_e|w_e|$, $P_w=\sum_p|w_p|$. Cap each $h_e$ by $h_e^{(J)}=\min(h_e,J)$, $J>0$, and denote the resulting probe by $O_J$. Each $h_e$ commutes with $H_0$ and is spectrally dominated by it on their common product basis. Since $|x-\min(x,J)|\le x^2/J$ for $x\ge0$,
$$
\|v\|\le K=A_wB+2\lambda P_w,\quad
\|O_J\|\le M=A_wJ+2\lambda P_w,\quad
\|(O-O_J)\Omega\|\le A_wJ_0/J .
$$
The bounded insertion has a finite character implementation up to an identity term. In one link let $P_{e,n}$ denote convolution by $(n+1)\chi_n$ with Haar probability. Then
$$
h_e^{(J)}=JI-\sum_{\gamma n(n+2)<J}(J-\gamma n(n+2))P_{e,n}.
$$
These one-link operators commute with left and right gauge rotations. They are transfer-matrix insertions; unlike the spatial plaquette multipliers, they can connect distinct configurations at the time of insertion. Their presence requires neither a time derivative of the Monte Carlo data nor removal of the electric observable from the total energy. [Link Casimir conventions](../hamiltonian-time/README.md)

## A comparison with the actual discrete transfer

Let $N_t=\lfloor t/a\rfloor\ge1$, $Y=(T_a/\|T_a\|)^{N_t}$, $v_{a,J}=O_J\Omega_a$. Use the same $N_t$ in all three readings, at $N_t,2N_t,3N_t$ steps. Put $p_a=\|P_a-P\|$ for the vacuum projections and $e_a(t)=\|X-Y\|$. Positivity fixes the phases of the two vacua, so
$$
\|v-v_{a,J}\|\le\eta:=A_wJ_0/J+\sqrt2 M p_a .
$$
For positive contractions $X,Y$, the telescoping product of the three contractions in $X(I-X)^2$ gives $\|Y(I-Y)^2-X(I-X)^2\|\le3e_a(t)$. Comparing quadratic forms therefore gives
$$
\left|\langle v_{a,J},Y(I-Y)^2v_{a,J}\rangle-D(t)\right|
\le(2K+\eta)\eta+3K^2 e_a(t).
$$
This uses operator norms, including for the capped electric part. It holds even if $J$, the box size, or the norms of the probes increase along the sequence. [Cap, three readings and noncommuting contraction products in Lean](../blocked-time/BlockedTime.lean)

Here is an explicit choice for an arbitrary sequence of finite SU(2) boxes in fixed time and observable units. At index $n$ take $J=1+2^n(1+K)A_wJ_0$, then compute $M$. Use $c=B+12\gamma$ and the proven finite-volume gap floor $d=\gamma\,2^{-N}e^{-B/\gamma}$. Starting at a fixed unit of time, halve the positive time spacing until $a\le t/2$, $ac\le1/36$, $72ac^2\le d$ and
$$
\sqrt2 M\,72ac^2/d\le2^{-n}/(1+K),\qquad
3K^2\mathcal E_a(t)\le2^{-n}.
$$
Here $\mathcal E_a(t)$ is the explicit six-term [evolution bound](evolution.md), evaluated with $k=\lceil(t/a)^{1/3}\rceil$. It tends to zero as $a\downarrow0$ in each fixed box, so the halving search terminates on each index. The [vacuum bound](README.md) gives $p_a\le72ac^2/d$. The resulting comparison error is at most $5\cdot2^{-n}+4\cdot2^{-2n}$. In particular a persistent three-reading signal in these bounded Wilson measurements is equivalent to the Hamiltonian band's survival whenever A4's common first-moment bound holds. This is an existence and accuracy guarantee for the prescribed measurements. Their evaluation cost can grow rapidly. [Explicit finite-volume floor](finite-volume-vacuum.md)

D4's product Peter–Weyl cutoff addresses a separate approximation: it restricts the Hamiltonian trial space and compares Ritz energy levels. Here the box dynamics and its vacuum stay exact at each time spacing; the representation cap acts only on the measured electric term. An error estimate for the bounded-insertion diagnostic survives independently of a finite-dimensional Ritz calculation. [D4's cutoff calculation](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7093601149)

## Independent review of the spatial expansion

At A4's commit `cf121b21f784058224497a7dbd27245a366cf3ff`, all nine EnergyDensity declarations passed a fresh pinned Lean process. The geometry, Fourier and rotor controls reproduced the recorded values, including the $g=256$ electric diagonal 513.439175 and magnetic diagonal 8215.02681. For a linear coordinate on a unit round link, the transition $n\to n\pm1$ gives the square of the Casimir difference as twice the Casimir sum plus three. Integration by parts yields the stated $4\int x|\nabla_e\Omega|^2+9\langle x\rangle$. The coefficient sign, the row-sum cancellation and the isotropic leading first-moment form agree with A4's calculation. [A4's proof and reproducible checks](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/cf121b21f784058224497a7dbd27245a366cf3ff/yang-mills/observable-normalization/energy-density)

For a smooth test supported with padding (or a smooth periodic test), one can sharpen the spatial remainder to $O_\varphi(b^2)$. At the midpoint of an unordered neighboring pair, $\varphi(x+bd/2)-\varphi(x-bd/2)=b(d\cdot\nabla)\varphi(x)+O_\varphi(b^3)$ uniformly for $|d|\le1$. Squaring gives a fourth-order remainder. The squared weight $b^4$, the bound $|K_{ij}|=O(b^{-3})$, and $O_\varphi(b^{-3})$ active pairs therefore give $O_\varphi(b^2)$. The quadrature error for the leading squared derivative on each shifted regular grid is also $O_\varphi(b^2)$ by integration over centered cubes. The unknown local coefficients may vary with $b$. This refinement does not supply a positive band signal.

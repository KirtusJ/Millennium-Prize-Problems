# Surface error for the periodic SU(2) Wilson pressure

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Let $p_L(\beta)=L^{-4}\log Z_L(\beta)$ for the four-dimensional isotropic, fundamental SU(2) Wilson action $S_L=\sum_p(1-\frac12\operatorname{Tr}U_p)$ on a periodic cube, with normalized Haar measure on each positive link. Let $p(\beta)$ be its thermodynamic limit. For every even $L=2\ell\ge4$ and $\beta\ge0$,
$$
|p_L(\beta)-p(\beta)|\ \le\
4\!\left[1-(1-1/\ell)^3\right]
\left[3-\log c_H+\tfrac32\log(1+\beta)\right],
\qquad c_H=\frac{2\sin^2(1)}{3\pi}.
$$
Consequently the macroscopic Wilson-action deviation law holds whenever $\log(1+\beta)=o(L)$ as both parameters grow. The earlier sufficient condition was $\beta=o(L)$. The surface estimate uses only the finite-volume Wilson integral. The deviation laws additionally use the program’s thermodynamic single-face Ward estimate. [Earlier pressure result](../action-deviations/README.md) · [A4’s independent readback](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7107516192)

## A common upper endpoint for different volumes

Tile the torus of side $m\ell$ with $m^4$ closed cubes of side $\ell$, where $m\ge2$ is even. A seam link lies in a three-dimensional face of a tile. A private link belongs to exactly one tile. A link entering a boundary vertex can still be private. Each tile has $4\ell(\ell-1)^3$ private positive links. Thus the global number of distinct seam links per site is
$$
d_\ell=\frac{n_{\rm seam}}{(m\ell)^4}=4[1-(1-1/\ell)^3]\le12/\ell .
$$
A plaquette belongs to $2^k$ cubes if $k$ of its two transverse coordinates lie on tile cuts. Assign its action weight $2^{-k}$ in each of these cubes. For a reference cube and prescribed seam links $B$, let $K_\ell(B)$ be the integral over its private links of the exponential of minus $\beta$ times this weighted action. Conditional integration gives exactly
$$
Z_{m\ell}=\int\prod_T K_\ell(B_T)\,dB_{\rm seam}.
$$
The kernel is positive and continuous on a compact product of groups. Write $M_\ell=\max_B K_\ell(B)$ and $u_\ell=\ell^{-4}\log M_\ell$. Then $p_{m\ell}\le u_\ell$.

There exists one global seam assignment attaining $M_\ell$ in **every** tile. Choose any maximizing boundary assignment in the reference cube. In each coordinate fold the integer lattice into $[0,\ell]$ by $j\mapsto\min(r,2\ell-r)$ with $r=j\bmod 2\ell$. Pull the reference labels back along directed seam links, taking the group inverse when a link runs backward. The fold is single-valued on the torus since $m$ is even. It gives the same directed label on every shared edge, including at intersections of cuts. On each tile it is a cube isometry. Under this change of private variables Haar measure is invariant, the repartition weights are invariant, and each Wilson loop trace is invariant under cyclic change of basepoint and reversal. Thus the product of kernels at this assignment is $M_\ell^{m^4}$. This handles noncommuting boundary data without fixing a gauge.

## Cost of integrating around the maximizing seam

Independently at each seam link, restrict Haar measure to a class-angle ball of radius $\delta\le1$ around its chosen value. Its mass is
$$
v_\delta=\frac{2}{\pi}\int_0^\delta\sin^2\theta\,d\theta\ \ge c_H\delta^3 .
$$
Here the normalized Haar law is uniform on the unit three-sphere, and $\sin\theta\ge\theta\sin(1)$ on $[0,1]$. Under the normalized restriction a positive link is $U^*H$, where the increment $H$ has a conjugation-invariant, inversion-symmetric law. In the fundamental representation $\mathbb E H=\mathbb E H^{-1}=a_\delta I$ with $1\ge a_\delta=\mathbb E\cos\theta\ge1-\delta^2/2>0$.

Hold all private links fixed. Each plaquette uses four distinct positive-link variables, possibly with inverse orientations. If $j_p$ of those links lie on the seam, independence and the scalar mean give exactly
$$
\mathbb E_{\rm tube}\tfrac12\operatorname{Tr}U_p
  =a_\delta^{\,j_p}\tfrac12\operatorname{Tr}U_p^* ,
$$
where the star means the same private configuration with the maximizing seam restored. The expected increase of its action is at most $1-a_\delta^{j_p}\le j_p\delta^2/2$, including when its initial trace is negative. Every global link meets six plaquettes, so $\sum_p j_p=6n_{\rm seam}$. Apply Jensen’s inequality once to the exponential of the **whole** action, then integrate over the private links:
$$
Z_{m\ell}\ \ge\ v_\delta^{\,n_{\rm seam}}
             e^{-3\beta\delta^2 n_{\rm seam}}\,M_\ell^{m^4}.
$$
This step allows arbitrary correlations between adjacent plaquettes. Choose $\delta=(1+\beta)^{-1/2}$. All the pressures $p_{m\ell}$ for even $m$ now lie in a common interval with upper endpoint $u_\ell$ and width equal to the displayed theorem bound. Taking $m\to\infty$ at fixed $\ell,\beta$ puts $p(\beta)$ in the same interval as $p_{2\ell}(\beta)$. This proves the bound, with a single interval width. Existence of the fixed-coupling limit also follows from the earlier bounded-action seam comparison.

## Consequences at growing coupling

Write $D=(1+\log(1+\beta))/L$, $V=L^4$, $c=9/2$ and $X=\beta S_L/V$. The prior Ward result gives $|b p'(b)+c|\le Cb^{-1/8}$ almost everywhere for large $b$ and $p(b)=-c\log b+C_W+O(b^{-1/8})$. The surface comparison gives the following statements for even $L\ge4$.

* **Pressure and the mean action.** $p_L(\beta)+c\log\beta=C_W+O(\beta^{-1/8}+D)$. When $D\to0$, $\mathbb E_{L,\beta}X=c+O(\beta^{-1/8}+\sqrt D)$. To get the latter, bound $p_L'(\beta)$ between the two secant slopes to $\beta(1\pm h)$, $0<h\le1/2$. After multiplying by $\beta$, replacing the secant endpoints by $p$ costs $O(D/h)$. Integrating the thermodynamic derivative on either side costs $O(h+\beta^{-1/8})$ relative to $-c$. Take $h=\sqrt D$ for large $L$ and use $\mathbb E X=-\beta p_L'(\beta)$.
* **Macroscopic deviations.** If $D\to0$ and $\beta\to\infty$, $X$ has speed $V$ and rate $x-c-c\log(x/c)$ on $x>0$, infinite on $x\le0$. Indeed $p_L((1-t)\beta)-p_L(\beta)\to-c\log(1-t)$ for each $t<1$, with error $O_t(\beta^{-1/8}+D)$. For $t\ge1$ the limit is infinite by the value at $t=1$ and monotonicity. The differentiable, steep cumulant and exponential tightness give the stated law.
* **Moderate deviations.** If $r\downarrow0$, $\beta^{-1/8}=o(r)$, $D=o(r^2)$ and $Vr^2\to\infty$, $(X-c)/r$ has speed $Vr^2$ and rate $z^2/9$. For each fixed real $u$, the short-interval Ward integral has error $O_u(r\beta^{-1/8})$ in $p((1-ur)\beta)-p(\beta)+c\log(1-ur)$. Passing to finite $L$ adds $O_u(D)$. Subtracting $urc$ and dividing by $r^2$ gives the limiting cumulant $cu^2/2$. For example, take $L$ the next even integer above $(\log\beta)^2$ and $r=(\log\beta)^{-1/4}$.

The underlying Gärtner–Ellis argument and normalization are given in the [action-deviation derivation](../action-deviations/README.md). These conclusions concern the total lattice action. The optimal size of the surface error, the value of $C_W$ and the continuum mass gap remain open here.

## Literature and verification scope

Chatterjee uses box decomposition and estimates on boundary edges in the free-energy analysis for $U(N)$, including a four-dimensional weak-coupling result. Faria da Veiga and O’Carroll distinguish the $dL^{d-1}$ additional periodic bonds and prove Wilson partition-function stability bounds. The estimate above instead compares periodic volumes directly by integrating around a compatible maximizing seam; neither external result supplies the program’s SU(2) single-face coefficient. [Chatterjee, §§14–15 and Theorem 2.3](https://arxiv.org/pdf/1602.01222) · [Faria da Veiga and O’Carroll, §II and stability bounds](https://arxiv.org/pdf/2205.07376)

Three recursively linked PCP OS guests checked all 33,888 plaquettes of the doubled tori with tile sides 2, 3 and 4, counted their seam links, and compared 7,776 folded plaquette traces against a reference field of quaternion units. The last guest checked scalar damping at all 16 choices of perturbed links on each of three signed or zero-trace words, using an exact discrete noise distribution. Lean 4.19.0 accepted the two enumeration totals and two polynomial identities; one malformed delegation and three altered proof outputs were rejected. The Haar integral, Jensen step and asymptotic conclusions are proved in the text. [Native workers](worker.c) · [Replay](verify.py) · [Generated Lean declarations](ReflectedPressure.lean)

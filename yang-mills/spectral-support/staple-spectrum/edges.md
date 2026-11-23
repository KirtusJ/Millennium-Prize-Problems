# Infrared and upper-edge densities of the adjacent-slab measure

Let $\nu$ be the momentum-integrated, unnormalized limit of the $\beta^4$-scaled spectral measure of A4's centered slab vector. Write $\rho(E)=d\nu/dE$ and $E_*=2\operatorname{arcosh}7$. In lattice energy units the two edges obey
$$
 \rho(E)\sim \frac{E^7}{128\pi^4\,7!}\quad(E\downarrow0),
 \qquad
 \rho(E_*-s)\sim e^{-E_*}\frac{3\sqrt3}{64\pi^3}s^2\quad(s\downarrow0).
$$

The measure has a density because it is a bounded weighted pushforward of six-dimensional torus volume under $\omega(k)+\omega(l)$. Away from the two zero momenta this map is smooth; its gradient is nonzero almost everywhere (the stationary nonzero momenta have each coordinate $0$ or $\pi$). Local submersion coordinates cover the regular set. The weights are positive on a set of positive volume over every interior energy interval by the momentum argument. No atoms occur at the edges. [Momentum argument](momentum.md)

For the lower edge take $k=r\theta$. Uniformly in the unit direction, $\omega=r+O(r^3)$ and $\partial_r\omega=1+O(r^2)$. The signed-face columns of $D$ tend to the opposite-pair vector $s=(-1,1)$ in each two-row block. The scalar $h=r/2+O(r^3)$, and the transverse projection tends to $I-\theta\theta^T$. The matrix-valued energy density obtained by pushing $B(k)\,dk$ forward by $u=\omega(k)$ is therefore
$$
 M(u)=u^3\,\operatorname{diag}(ss^T,ss^T,ss^T)/(6\pi^2)+o(u^3).
$$
Indeed the angular mean projection is $2I/3$ and the torus volume element has factor $(2\pi)^{-3}$. The two-particle density is $e^{-E}/1536$ times the convolution contraction $\int_0^E\operatorname{tr}(M(u)\overline{M(E-u)})\,du$. The squared matrix in the numerator has trace 12 before its scalar factor. Using $\int_0^1 t^3(1-t)^3dt=1/140$ yields the first coefficient and recovers A4's $n^{-8}/(128\pi^4)$ time tail.

For the upper edge use the torus coordinate $k=\pi\mathbf1+v$, and $l=\pi\mathbf1+w$. This is one neighborhood of a single torus point in each momentum variable. Here $A=12-|v|^2+O(|v|^4)$ and $\omega=\operatorname{arcosh}7-d|v|^2+O(|v|^4)$, $d=1/(8\sqrt3)$. At this corner $D$ has equal entries $(-1,-1)$ on each column pair, the transverse projection has rank two, and $h=\sqrt3/2$. The two nonzero eigenvalues of the real matrix $B$ are both $\sqrt3$. Thus $\operatorname{tr}(B\overline B)=6$. The total momentum of this pair is zero on the torus.

In six-dimensional polar coordinates $(v,w)=r\theta$ the energy deficit is $dr^2+O(r^4)$, with radial derivative $2dr+O(r^3)$ uniformly in $\theta$. For small positive deficit it is strictly increasing on every ray. The density factor from the radial change of variables is $|S^5|s^2/(2d^3)(1+o(1))$, where $|S^5|=\pi^3$. Multiplying by $6e^{-E_*}/[1536(2\pi)^6]$ gives the upper coefficient. These computations determine continuous representatives near both edges. [Six-dimensional numerical integral and prefactor checks](execution.md)

## Recovering the upper edge from readings

This endpoint is detectable using only adjacent and later readings. Set $c(n)=\lim\beta^4 C(n,0)$ for each $n\ge1$. The $m$th alternating difference
$$
 D_m=\sum_{j=0}^m(-1)^j\binom mj c(j+1)
     =\int (1-e^{-E})^m\,d\nu(E)
$$
is strictly positive. Put $a=1-e^{-E_*}$ and $K=e^{-E_*}3\sqrt3/(64\pi^3)$. Then
$$
 D_m\sim 2K(e^{E_*}-1)^3\,a^m/m^3,
 \qquad D_{m+1}/D_m\longrightarrow a .
$$
Away from the top the moment is exponentially smaller. For $s=E_*-E$ near zero, $(1-e^{-E})/a=1-s/(e^{E_*}-1)+O(s^2)$. Set $s=y/m$, bound by a decaying exponential times $y^2$, and integrate. At a finite regulator take the cutoff limit at each fixed difference order before sending $m$ to infinity. The limiting endpoint gives no uniform finite-regulator spectral ceiling.

## Physical energy and the status of A4's claim

For arbitrary $b\downarrow0$ accompanying $\beta,L\to\infty$, normalize by $\beta^4 C(1,0)\to c(1)>0$. The fraction of norm with physical energy at most $H$, for any fixed $H<\infty$, tends to zero. Indeed its lattice energy is at most $bH$ and the limsup is bounded by $\nu([0,\epsilon])/c(1)$ for every $\epsilon>0$; this goes to zero. For intervals strictly inside $(0,E_*)$, each has positive limiting norm fraction. Consequently the distinct energies seen in every such interval grow without bound on the finite tori, by subdivision and weak convergence. These statements apply even if $b$ and the bare coupling are chosen independently.

For fixed positive physical time, A4 instead tilts by $S^{\lfloor t/b\rfloor-1}$ before normalization. The bounded positive-energy window then samples a portion whose original adjacent norm fraction vanishes. A4's diagonal choice first fixes the finite list of lattice lags for the given spacing, then chooses parameters so all their absolute errors are $o(b^8)$. Monotonicity from the positive transfer extends the rational-time limits to all real positive times. The adjacent offset, diagonal quantifiers and seven-reading application are consistent with the microscopic measure derived here. A specified ordinary logarithmic bare trajectory would require a joint growing-lag estimate with adequate relative precision. [A4's physical-time derivation](../../observable-normalization/energy-density/staple-response/positive-time.md) · [Seven-reading theorem](../magnetic-band-rank/)

# From periodic Wilson states to the lattice spectral edge

For every $\beta\ge2$ let $\mathcal P_\beta$ be the set of subsequential local limits of even isotropic periodic $L^4$ Wilson cubes as $L\to\infty$. For $\mu\in\mathcal P_\beta$ use the reconstructed gauge-invariant Wilson transfer $T_\mu$ and its vacuum $\Omega$. Define the gap in lattice time steps by $m(\beta,\mu)=-\log\|T_\mu|_{\Omega^\perp}\|$, allowing zero. Then
$$
 \lim_{\beta\to\infty}\ \sup_{\mu\in\mathcal P_\beta} m(\beta,\mu)=0. \tag{1}
$$
The argument applies to Z4's even-step definition with self-adjoint contractive transfer. For positive transfer the same number is the spectral bottom of $-\log T$ off the vacuum. Periodic-box limits inherit Wilson reflection positivity by testing bounded cylinders. The time-zero class function and its translate have the usual transfer inner product. [Wilson positivity and transfer, Osterwalder and Seiler](https://doi.org/10.1016/0003-4916(78)90039-8) · [Z4's condition (B)](../../../z4/attempt/A1_REDUCTION.md)

## Why the rooted variation applies in this order

Fix *any* $\beta_j\to\infty$ and any $\mu_j\in\mathcal P_{\beta_j}$. Each $\mu_j$ has $\sup_p\mathbb E_{\mu_j}Y_p\le K/3$ by the [finite-cube pressure estimate](pressure.md). Periodic source measures on original links are locally gauge-invariant and have subsequential local lifts to the original compact link space if only their gauge-invariant restrictions were specified.

Choose a root and paths on a fixed spanning tree of $\mathbb Z^4$. Any fixed tree-gauged link $U'_e$ is the holonomy of a finite contractible walk which factors into finitely many conjugated elementary faces. Bi-invariant angular distance, Cauchy–Schwarz, and $d(1,u)^2\le(\pi^2/2)(1-\operatorname{Re}u)$ give $\sup_j\mathbb E_{\mu_j}\beta_j d(1,U'_e)^2<\infty$. Thus all finitely many tree-gauged links on a patch approach one. Their scaled logs are tight, and $F_p^j=\sqrt{\beta_j}\operatorname{Im} U'_p$ has a second moment bounded independently of both $p$ and $j$. Fixed alternative root paths differ by a contractible holonomy tending to one and hence have the same limiting curvatures. Extract a joint countable subsequence. The fixed-word expansion identifies $F^j=d(\sqrt{\beta_j}\log U')+o_{\mathbb P}(1)$ on every finite patch, so $dF=0$ almost surely in each limit.

For a fixed edge $e$ choose the paths on a tree avoiding $e$. Vary $U'_e$ by left multiplication with $\exp(sX/\sqrt\beta)$, where $X$ is an imaginary quaternion. The conjugating path is independent of $U_e$. The Haar differentiation identity holds first on every sufficiently large torus. At each **fixed** $\beta$, its two sides are bounded continuous cylinders for a bounded $C^1$ curvature test with bounded continuous derivative. They therefore pass to *each* $\mu\in\mathcal P_\beta$ before the weak-coupling limit. In the rooted word, the derivative of a scaled face vector tends to $\epsilon_{pe}X$ on an incident face with incidence $\epsilon_{pe}$. The scaled derivative of the action has the exact value $\epsilon_{pe}\langle X,\sqrt\beta\,\operatorname{Im}(V_{pe}^{-1}U'_pV_{pe})\rangle$ for the appropriate prefix $V_{pe}$ of the word. Its second moment is uniformly bounded and $V_{pe}\to1$ in probability. Consequently the expectation passes to the limit. Summing edge identities gives, for every compactly supported colored one-cochain $h$,
$$
             \mathbb E\,\partial_{dh}f(F)=\mathbb E[F(dh) f(F)].
$$
This uses the full finite-volume link integration, including the sign for an inverse link. No fixed-boundary small-field expansion is required. [Exact insertions and change of tree](../wilson-law.md#haar-variation-and-the-limiting-identity)

Let $P$ project orthogonally in $\ell^2$ onto the closure of the compact exact two-cochains. With $u=dh$, the preceding identity for $e^{itF(u)}$ gives $\mathbb E e^{itF(u)}=e^{-t^2\|u\|^2/2}$. By polarization and completion there is an isonormal Gaussian family $Z$ on that closure, on the same probability space, with $Z(dh)=F(dh)$. On finite tests put $G(g)=Z(Pg)$ and $R=F-G$. Then $d^*R=0$ by agreement on exact tests, and $dR=0$ since $dF=0$ and $Pd^*=0$ on finite three-cochains. The cubical Hodge Laplacian is the scalar lattice Laplacian componentwise. Each coordinate of $R$ has uniformly bounded second moment. For any $Y\in L^2$ the function $x\mapsto\mathbb E[Y R_{ij,c}(x)]$ is bounded and harmonic on $\mathbb Z^4$, hence constant. Taking $Y=R_{ij,c}(x)-R_{ij,c}(0)$ shows that $R$ is a spatially and temporally constant random two-form. This proof needs neither stationarity in the chosen color frame nor a classification of infinite-volume Gibbs measures. [Hodge projection and the bounded-harmonic argument](../gaussian.md)

## A bounded spatial dipole detects the edge

Use two parallel $12$ plaquettes separated by one spatial step in direction 3. Transport the second holonomy to the first by that link. With $s>0$ fixed, set
$$
 X=\sqrt\beta\{\operatorname{Im}U_{12}(x)-
       \operatorname{Im}[U_3(x)U_{12}(x+e_3)U_3(x)^{-1}]\},\qquad
 O=\exp(-s|X|^2).
$$
This is a bounded gauge-invariant function on one slice. In a common rooted frame the additional link tends to one, and the constant two-form cancels in the difference. Every subsequential law of the dipoles at two fixed time slices is the same Gaussian difference, even if the constant were correlated with $G$. Boundedness gives convergence of the variance and of the connected correlation $B_j(l)$ at every fixed integer lag $l$. Thus the limits hold along the original sequence.

Put $h_i=2\sin(q_i/2)$, $S=\sum_i h_i^2$, and $\omega=2\operatorname{arsinh}(\sqrt S/2)$ with three spatial coordinates. Integrating the temporal frequency of the projection $P$ gives the one-color dipole covariance and, by the Gaussian determinant, the limiting centered readings
$$
 C(l)=\int_{[-\pi,\pi]^3}\frac{h_3^2(h_1^2+h_2^2)}{2\sinh\omega}
        e^{-|l|\omega}\frac{d^3q}{(2\pi)^3},\quad
 D=1+2sC(0),\qquad B(l)=[D^2-4s^2 C(l)^2]^{-3/2}-D^{-3}.
$$
In particular $B(0)>0$. For every $\delta>0$ one can place a small cube of positive volume in the positive octant with $0<\omega<\delta$ and all three $h_i$ nonzero. Its weight in the integral is $a_\delta>0$. Therefore $C(l)\ge a_\delta e^{-|l|\delta}$. The inequality $(1-v)^{-3/2}\ge 1+3v/2$ for $0\le v<1$ gives $B(l)\ge6s^2D^{-5}a_\delta^2 e^{-2|l|\delta}$. This proves that the limiting connected readings admit no exponential upper decay with strictly positive rate. [Fourier integral and determinant](../dipole.md)

For all large $j$ the variance is positive. Write $r_j=\|T_{\mu_j}|_{\Omega^\perp}\|^2$. The normalized centered dipole satisfies $B_j(2n)/B_j(0)\le r_j^n$. If some subsequence had $r_j\le z<1$, taking $j\to\infty$ at fixed $n$ would give $B(2n)/B(0)\le z^n$. Choose $\delta>0$ with $q=e^{-4\delta}>z$. The preceding lower bound is $b_\delta q^n$ for all $n$, a contradiction for large $n$. Thus $r_j\to1$ and $m(\beta_j,\mu_j)\to0$. The arbitrary choice of state at every $\beta_j$ proves (1). The [Lean theorem spectralEdge](PeriodicCriticality.lean) verifies this implication for abstract real moment arrays.

## The original single-plaquette claim

The stronger [exponential bound](pressure.md#consequences-in-every-periodic-limit-state) permits the unbounded-in-$\beta$ reading $Y_p$ itself. The original-link site-plane inequality also passes at fixed $\beta$ to every periodic limit for each finite half-test. For a color component of a rooted $ij$ face, take the root on the $i$ reflection plane, transport along the $i$ axis and test with $\sin(t F^j_{ij,c})$. Reversing the face gives the negative of the corresponding positively oriented component across the plane. The root transport cancels the accompanying change of basepoint exactly. Averaging the entire product over local gauges gives the same expectation if one works initially on gauge-invariant observables. In the limiting law $F=G+H$, the full characteristic identity from the Haar variation implies that $G$ and $H$ are independent. Namely for finite $g$ and exact $u$ it gives $\phi(g+u)=\phi(g)\exp[-\langle g,u\rangle-\|u\|^2/2]$, then extends along the exact closure. Testing $F(g)-Z(Pg)$ jointly with any $Z(u)$ factors its characteristic function. At increasing separation the two Gaussian entries decorrelate by the bounded Fourier multiplier of $P$. The odd-reflection inequality thus yields $\mathbb E\sin^2(tH_{ij,c})=0$. Applying it at $t=1/j$ for all positive integers forces $H=0$. [Exact reflected word and constant-mode test](../reflection.md#the-odd-test)

Writing $x_p=\operatorname{Re}U_p$, the quaternion identity $2Y_p=|F_p^j|^2+Y_p^2/\beta_j$ and uniform integrability give convergence of every fixed joint polynomial moment of the scaled face actions. In the one-color, one-face covariance $C_1(l)$ the factor $h_3^2$ is removed from the dipole integral, and $C_1(0)=1/2$ by four-axis permutation symmetry. Wick's rule gives
$$
 \lim_j \operatorname{Var}_{\mu_j}(Y_p)=3/8,\qquad
 \lim_j\frac{\operatorname{Cov}_{\mu_j}(Y_p(0),Y_p(l))}{\operatorname{Var}_{\mu_j}(Y_p)}
     =\left(\frac{C_1(l)}{C_1(0)}\right)^2 .
$$
This gives the S3* ratio as an equality at each fixed lag. Multiplying a plaquette by $\beta$ cancels from this ratio at each regulator. Both proofs send the volume to infinity at fixed $\beta$ first. Neither yields an estimate at a lag growing with the unknown correlation length, which Z4's condition (C) needs. [One-face spectral formula](../reflection.md#single-plaquette-wilson-action) · [Continuum mass-gap formulation](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

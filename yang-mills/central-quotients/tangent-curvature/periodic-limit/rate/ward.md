# Two finite-coupling estimates in a rooted color frame

Let $\mu$ be any infinite-volume state obtained as a limit of even, isotropic, periodic four-cubes at fixed $\beta\ge2$. Take positive lattice links, unit quaternions and the action $\beta\sum_p(1-\operatorname{Re}U_p)$. The only probabilistic input here is $\sup_p\mathbb E_\mu\beta(1-\operatorname{Re}U_p)\le C$, uniformly in the choice of state. In particular $\|1-U_p\|_{L^2}\le C/\sqrt\beta$ in quaternion norm. [Finite-cube pressure proof](../pressure.md)

## A path estimate independent of the time coordinate

From the origin to $x=(t,\mathbf x)$ use the path that moves in time first, then in spatial directions 1, 2, 3, using signed steps. Write $R_x$ for its transporter, $U'_e=R_xU_eR_{x+e_i}^{-1}$ and $w(x)=1+|\mathbf x|_1$. Then, for every positive edge based at $x$,
$$
 \|1-U'_e\|_{L^2}\le Cw(x)/\sqrt\beta. \tag{1}
$$
To compare the path extended by $e$ with the ordered path to its endpoint, commute that last step to the left through the coordinates following direction $i$, then combine or cancel it in its own coordinate. At most $|\mathbf x|_1$ adjacent interchanges are needed, even for a time step starting at large negative $t$. Every interchange inserts one conjugated face or its inverse. Bi-invariance, the triangle inequality and the uniform face bound give (1). Inverses and bounded shifts change only the constant. This choice of paths is why the estimates below can be uniform in the separation of two time slices.

Write $F_p=\sqrt\beta\,\operatorname{Im}(R_xU_pR_x^{-1})$ for a positive face at $x$. Its componentwise $L^2$ norm is bounded by an absolute constant. In expressions $F(g)$ sum the real colored face pairing with a finite test $g$. For a cochain $a$ use $\|a\|_1=\sum|a|$, $\|a\|_{1,w}=\sum w(x)|a(x)|$, with Euclidean norms on colors and sums over orientations.

## Approximate closedness with one spatial weight

For every unit cube based at $x$,
$$
             \mathbb E |(dF)_{\rm cube}|\le Cw(x)/\sqrt\beta . \tag{2}
$$
Here $d$ is the ordinary signed cubical coboundary. For directions $i<j<k$, compare the six paths across the cube in the cycle $ijk,jik,jki,kji,kij,ikj,ijk$. The ratios of each path to the next multiply to one by telescoping. Each ratio is an oriented plaquette or its inverse, conjugated by the path prefix before the swapped steps. The prefixes in the common rooted frame have length zero or one in the primed links. The signed faces in order are $ij(x),ik(x+e_j),jk(x),-ij(x+e_k),-ik(x),-jk(x+e_i)$, giving $-dF$ after ignoring these short conjugations. Each individual ratio $Q_l$ has $\|Q_l-1\|_2\le C/\sqrt\beta$, however large $w(x)$ is. Expanding $\prod_l Q_l=1$ around the identity leaves a linear sum and terms containing at least two factors $Q_l-1$. Since $|Q_l-1|\le2$, the expected norms of all the latter terms are $O(1/\beta)$ by Cauchy–Schwarz. Taking imaginary parts and multiplying by $\sqrt\beta$ costs $O(1/\sqrt\beta)$. Removing a one-link conjugation from a scaled face costs at most $2\|1-U'_e\|_2\|F_p\|_2$. This proves (2) with one power of $w$. In particular $\mathbb E|F(d^*k)|\le C\|k\|_{1,w}/\sqrt\beta$ for a finite three-cochain $k$.

## Quantitative Haar variation including the paths

For real finite one- and two-cochains $h,v$ with three colors,
$$
 \left|\mathbb E[F(dh)e^{iF(v)}]
     -i\langle dh,v\rangle\,\mathbb E e^{iF(v)}\right|
 \le \frac{C}{\sqrt\beta}\|h\|_{1,w}(1+\|v\|_1). \tag{3}
$$
It suffices to take $h$ a single unit color $X$ on the positive edge $e$ from $x$. Choose $\widetilde R_x$ along the ordered path to $x$ unless that path traverses $e$. In the latter case replace that one traversal by the other three sides of an adjacent square, with the same endpoints. The new path avoids $e$, and $\|1-R_x\widetilde R_x^{-1}\|_2\le C/\sqrt\beta$. The generator $\widetilde R_x^{-1}X\widetilde R_x$ is independent of the variable being integrated when all other links are fixed. Vary $U_e$ by left multiplication with its exponential at parameter $s/\sqrt\beta$.

For an incident face based at $z$ and with word $A U_e B$ or $A U_e^{-1}B$, take the prefix $V=A$ or $V=A U_e^{-1}$, respectively. In both cases it goes from $z$ to $x$. The directly inserted generator in the rooted word is $\epsilon_{pe}\,\operatorname{Ad}(R_zV\widetilde R_x^{-1})X$, with oriented incidence $\epsilon_{pe}$. Its difference from $\epsilon_{pe}X$ has $L^2$ norm at most $Cw(x)/\sqrt\beta$. Indeed $R_z V R_x^{-1}$ is a product of at most four primed links and (1) applies. The derivative of the Boltzmann action is the sum over incident faces of the dot product of these signed generators with $F_p$. Its difference from $F(dh)$ is bounded in $L^1$ by $Cw(x)/\sqrt\beta$.

The direct contribution to the derivative of a scaled face vector is the imaginary part of this generator times the unscaled rooted plaquette. Thus it differs in $L^1$ from $\epsilon_{pe}X$ by at most $Cw(x)/\sqrt\beta$. There is a second contribution even for nonincident faces. Differentiating $R_z$ and its inverse gives a commutator with the rooted face. The ordered path to $z$ visits $e$ at most once, in either direction. Its logarithmic derivative has norm at most $1/\sqrt\beta$. Conjugation acts trivially on the real part, so the commutator has norm at most $2|F_p|/\sqrt\beta$. The estimate for this term is independent of the length of the path. The derivative of the phase therefore differs in $L^1$ from $\langle dh,v\rangle$ by $Cw(x)\|v\|_1/\sqrt\beta$. Integrating the full derivative of the weighted exponential test gives (3), since the test has modulus one. Summing the single-edge estimates proves the general statement. At fixed parameters and finite supports the undivided integration identity involves bounded continuous cylinder functions on all sufficiently large tori, so it holds in each selected state. If working on gauge-invariant restrictions, Haar-average the complete identity over its finite set of vertex frames. [Qualitative original-link derivation](../../wilson-law.md) · [Integration by parts for finite-$N$ lattice loop equations](https://arxiv.org/abs/2309.07399)

With $u=dh$, interpolate $\phi(t)=\mathbb E e^{itF(u)}$ from $0$ to $1$. Equation (3) yields $\phi'(t)+t\|u\|_2^2\phi(t)=e(t)$ with $|e(t)|\le C\|h\|_{1,w}(1+\|u\|_1)/\sqrt\beta$. The integrating kernel $\exp[-(1-t^2)\|u\|_2^2/2]$ has modulus at most one. Hence
$$
 \left|\mathbb E e^{iF(u)}-e^{-\|u\|_2^2/2}\right|
 \le C\,\|h\|_{1,w}(1+\|u\|_1)/\sqrt\beta .
$$

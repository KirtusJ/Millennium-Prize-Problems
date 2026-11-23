# Local energy readings, time period and quadrature

Use the SU(2) torus, extensive bounds and time conventions of the [vacuum estimate](graph-norm.md). Fix $a>0$. The strictly positive transition at fixed temporal links $h$ and adjacent spatial configurations $x,y$ is $T_h(x,y)=M(x)k(x,h\cdot y)M(y)$. Define a local function $\sigma_O=(O_x T_h)/T_h$. Gauge invariance of the original density and bi-invariance of each link Laplacian make this function invariant under independent vertex rotations at both slices.

## Link formula

Holding all other links fixed, the log of this outgoing transition depends on the unit quaternion $u=x_e$ as a constant plus $H_e\cdot u$. Only one temporal face (coefficient $g=\kappa/a$) and four spatial faces at the left slice (coefficient $a\lambda/2$) enter. Each has the form of a Euclidean linear functional of norm one, also when the link occurs inverted. The periodic spatial cube of side at least two keeps all four members of each plaquette distinct. Write $R=g+2a\lambda$, so $|H_e|\le R$.

For a linear coordinate $\phi=H_e\cdot u$ on the unit three-sphere, $\Delta\phi=-3\phi$ and $|\nabla\phi|^2=|H_e|^2-\phi^2$. The outgoing reading is therefore
$$
 \sigma_O(x,h,y)=\sum_e w_e\gamma(3\phi_e-|H_e|^2+\phi_e^2)
          +\sum_p w_p\lambda(1-\phi_p(x)),\qquad
 |\sigma_O|\le F:=A_w\gamma(3R+R^2)+2\lambda P_w .
$$
Here $\phi_e=H_e\cdot x_e$ is a staple contraction and $\phi_p$ is the normalized trace of one spatial face. Multiplying the weights on two distinct outgoing steps by their respective readings differentiates two separate kernels. Integrating the original temporal links and composing the kernels gives
$$
 C_{a,P}(k)=\mathbb E_{a,P}[\overline{\sigma_O(0)}\,\sigma_O(k)]
 =\frac{\operatorname{Tr}_{\rm phys}\big[O^*S^k O S^{P-k}\big]}{\operatorname{Tr}_{\rm phys} S^P},
 \qquad 1\le k<P .
$$
The equality applies to time-independent weights on the two copies. At fixed $a$ the smooth kernels move vectors into the differential domains. The first insertion uses conjugated weights. A square of a single transition reading does not compute a coincident $O^*O$ insertion. The two-time equality suffices for $k=n,2n,3n$. [Periodic physical trace](README.md) · [Direct nonabelian link and rotor tests](execution.md)

## A physical period with an explicit error

Let $\Delta_a$ be the first physical log-transfer gap per unit time, and let $Q_a$ project off the simple vacuum. For $g\ge4$, take $m_0=\lceil3g\rceil$ and $s_0=m_0a\le13\kappa/4$. Each one-link, $m_0$-step free density is bounded above by $11/10$. The positive magnetic half weights are at most one. The full-space diagonal of $T^{m_0}$ is therefore dominated by that of $K^{m_0}$ pointwise. The physical trace is at most the full positive-operator trace. Since $\rho^{-m_0}\le e^{s_0B}$,
$$
 \operatorname{Tr}_{\rm phys} S^{m_0}\le C_0:=e^{s_0B}(11/10)^N,\qquad
 \operatorname{Tr}_{\rm phys} Q_a S^r\le C_0 e^{-(r-m_0)a\Delta_a}
 \quad(r\ge m_0).
$$
The last inequality is a termwise estimate over the excited spectrum, including multiplicities. [Free block estimate](../blocked-time/README.md)

For $h=1$, the integral kernels give $|(OS)f|\le F S|f|$ on the physical space, so $\|OS\|,\|O^*S\|\le F$. More generally take $1\le h\le n$, and bound both $\|OS^h\|$ and $\|O^*S^h\|$ by $A_h$. Set $D_j=(O^*S^h)S^{jn-h}(OS^h)$ and $r_j=P-jn-h$, $j=1,2,3$. Then $\|D_j\|\le A_h^2$ and its vacuum expectation $v_j$ equals $\langle O\Omega_a,S^{jn}O\Omega_a\rangle$. In the numerator $\operatorname{Tr}D_j S^{r_j}$, the contribution off the vacuum has magnitude at most $A_h^2\operatorname{Tr}Q_a S^{r_j}$. The denominator is $1+\operatorname{Tr}Q_a S^P$. Dividing and using $|v_j|\le A_h^2$ bounds each bias by twice $A_h^2$ times the same trace-tail estimate. In particular for $P\ge3n+h+m_0$,
$$
 \left|C_{a,P}(n)-2C_{a,P}(2n)+C_{a,P}(3n)
 -\langle O\Omega_a,p(S^n)O\Omega_a\rangle\right|
 \le 8 A_h^2 C_0 e^{-(P-3n-h-m_0)a\Delta_a}.
$$

Positive time keeps the required physical period bounded at each fixed box even as $a$ vanishes. To see this, put $U_h=M^{-1}S^h=\rho^{-1}KMS^{h-1}$. Applying the kinetic multiplier from the vacuum proof gives
$$
 H_0 U_h=L_a\left[\rho^{-1}M (I-S)S^{h-1}/a+J_a(W) S^h\right].
$$
The geometric sum gives $h(1-s)s^{h-1}\le1-s^h\le1$ for $0\le s\le1$. At $aB\le1$, $\rho^{-1}\le e<3$. Hence $\|H_0U_h\|\le C_h:=3/(ah)+5B$ and $\|U_h\|\le2$. Applying the product rule to $S^h=MU_h$, including the gradient estimate on the image of each unit vector, gives the admissible bound
$$
 A_h=A_w\left(C_h+aD_1+\gamma a^2G_1^2/2+aG_1\sqrt{2\gamma C_h}\right)+2\lambda P_w .
$$
Choose $h=\lfloor n/2\rfloor$ when $a\le t/4$; then $ah\ge t/8$. If $180ac^2\le d_L/2$, comparison of the log-transfer and Hamiltonian gaps gives $\Delta_a\ge d_L/2$. These inequalities bound the thermal error with an explicit margin. They do not bound the variance of the raw single-history score uniformly in $a$. [All-volume finite-box gap comparison](../joint-cutoff/README.md) · [Scalar smoothing and bias proofs](PeriodicTime.lean)

## A finite deterministic evaluation

Use Hopf coordinates for normalized Haar on SU(2),
$$
 u(s,\alpha,\beta)=(\sqrt{1-s}\cos\alpha,\sqrt{1-s}\sin\alpha,
                      \sqrt{s}\cos\beta,\sqrt{s}\sin\beta).
$$
Here $s,\alpha/(2\pi),\beta/(2\pi)$ are independent uniform variables on $[0,1]$. This follows from the area element of the unit three-sphere, or from normalizing two independent complex Gaussians. Divide all three coordinates into $M_c$ equal intervals and replace each by its midpoint. Each unit quaternion moves in Euclidean norm by at most $\delta=M_c^{-1/2}+\pi/M_c$: the two square-root changes have combined norm at most $\sqrt{2|\Delta s|}$ and rotating the two phases costs at most the largest angular change.

Compute the normalized weighted sum of $Y=\overline{\sigma_O(0)}(\sigma_O(n)-2\sigma_O(2n)+\sigma_O(3n))$ at the product cell centers, using the original Wilson action. Quaternion multiplication by a unit and inversion preserve distances. Telescoping a plaquette gives a change at most $4\delta$ in its trace coordinate. There are $PN$ temporal and $PN$ spatial plaquettes. The total log weight changes by at most $D=4PN(g+a\lambda)\delta$. Every staple coefficient uses three other links with norm-preserving multiplication, conjugation or quaternion inversion. Thus $|\Delta H_e|\le3R\delta$ and $|\Delta\phi_e|\le4R\delta$. The electric linear term changes by at most $12R\delta$, the squared norm by $6R^2\delta$ and the squared contraction by $8R^2\delta$. Consequently
$$
 |\Delta\sigma_O|\le\Lambda\delta,\quad
 \Lambda=A_w\gamma(12R+14R^2)+4\lambda P_w,\quad |\Delta Y|\le8F\Lambda\delta.
$$

For the reweighting error keep the midpoint test fixed, interpolate linearly between the exact and cellwise log weights, and differentiate the normalized expectation. The resulting covariance has magnitude at most $4F^2 D$ by Cauchy–Schwarz, since $|Y|\le4F^2$ and the log-weight difference is bounded by $D$. This works for complex tests as well. The deterministic integration error is therefore at most
$$
 8F\Lambda\delta+16F^2PN(g+a\lambda)\delta .
$$
This is an exact-arithmetic bound. For certified numerical endpoints the finite sums can also be evaluated with enclosing arithmetic, increasing precision until their quotient has the desired width. The denominator is strictly positive. The direct grid has $M_c^{3(4PL^3)}$ points; the bound establishes finite evaluability and is expensive even on a small torus.

Given any prescribed sequence of finite boxes, parameters, positive physical times and weights, at index $s$ first halve $a$ until $g\ge4$, the spacing conditions above and in the vacuum comparison hold, and that comparison costs at most $2^{-s}$. Next increase even $P$ until the thermal error bound is at most $2^{-s}$. Finally increase $M_c$ until the quadrature error is at most $2^{-s}$. Each search terminates at a fixed index for computable parameters with the stated signs. The resulting values differ from the Hamiltonian readings by at most $3\cdot2^{-s}$ before arithmetic rounding. At fixed $t>0$ and under A4's common first-moment bound, a positive limiting lower bound for these values is equivalent to persistent first-moment mass on a common compact interval in $(0,\infty)$. If the time or test itself varies, the absolute-error comparison still holds; a new band conclusion requires the corresponding uniform hypotheses. Establishing a positive signal in the continuum trajectory and the full Clay construction remains open. [Band equivalence and hypotheses](../joint-cutoff/energy-density.md) · [A4's first-moment estimate](../../observable-normalization/energy-density/spatial-limit.md)

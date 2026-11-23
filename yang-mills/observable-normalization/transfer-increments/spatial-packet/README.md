# An eighth-power scale for the weak-coupling Wilson lattice gap

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For pure isotropic four-dimensional $SU(2)$ Wilson theory, take the thermodynamic limit through even periodic four-cubes at each fixed $\beta$. Let $\mathcal P_\beta$ contain all their subsequential local limit states. With $T_\mu$ the vacuum-normalized time transfer, set $m(\beta,\mu)=-\log\|T_\mu|_{\Omega^\perp}\|$ in lattice units. For some absolute finite constant $C$ and all sufficiently large $\beta$, the estimate is
$$
                  \sup_{\mu\in\mathcal P_\beta} m(\beta,\mu)\le C\beta^{-1/8}.
$$
This uses C4's [periodic-state first moment](../../../central-quotients/tangent-curvature/periodic-limit/pressure.md), [root-path and cube estimates](../../../central-quotients/tangent-curvature/periodic-limit/rate/ward.md) and [walk difference bounds](../../../central-quotients/tangent-curvature/periodic-limit/rate/heat.md). The new ingredient is a three-dimensional spatial packet with a nonvanishing free connected reading at a time comparable to its diameter. Its Wilson comparison costs at most $C R^4/\sqrt\beta$ for diameter of order $R$. A single even-time reading then suffices for the gap bound. C4's [fixed-stencil calculation](../../../central-quotients/tangent-curvature/periodic-limit/rate/spectrum.md) uses a three-plaquette reading of size $n^{-16}$ and two growing lags. Earlier spatially smeared observables gave free limits along [specified finite-box vacuum trajectories](../../../central-quotients/magnetic-smearing/ordinary-profile.md).

The same packet carries a uniform positive amount of spectral weight at strictly positive lattice energies comparable to $\beta^{-1/8}$, including in a state with multiple fixed vectors. The result permits zero gap at fixed coupling and arbitrarily faster closure in lattice units. The physical scale, positivity at fixed coupling, and a four-dimensional interacting continuum theory with a positive mass gap remain open. [Clay formulation](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## The observable

Fix integer $R\ge2$. At time $t$ take positively oriented $12$-faces at spatial sites $x\in\mathbb Z^3$, transport each holonomy to $(t,0)$ along the ordered spatial coordinate path, and denote its scaled imaginary quaternion by $F(t,x)=\sqrt\beta\,\operatorname{Im}U^{\rm transported}_{12}(t,x)$. Put
$$
 b_R(x)=R^{-1}\prod_{i=1}^3 (1-|x_i|/R)_+,\quad
 g_R=(I-\tau_{R e_3})^3 b_R,\quad
 X_R(t)=\sum_x g_R(x) F(t,x),\qquad O_R(t)=e^{-|X_R(t)|^2}.
$$
Here $\tau_a b(x)=b(x-a)$. The color norm makes $O_R$ a gauge-invariant observable supported on a finite spatial slice, taking values in $(0,1]$. Its centered variance is at most one. Write $B_{\beta,R}(n)$ for its connected reading at time lag $n$ in the chosen state.

For any fixed $A>0$, simultaneously in the state and $0\le n\le A R$, the [rooted comparison](comparison.md) proves
$$
                   |B_{\beta,R}(n)-B_R^{\rm free}(n)|
                        \le C_A R^4/\sqrt\beta . \tag{1}
$$
The argument interpolates the characteristic function of the original packet. This keeps the differentiated paths inside its known support while the Haar variation uses an auxiliary one-cochain of larger support.

## A positive reading at one diameter

In the three-color Gaussian reference field of exact lattice curvature, let $C_R(n)$ be the covariance of one component of $X_R$. With $h_i=2\sin(q_i/2)$, $\omega=2\operatorname{arsinh}((\sum_i h_i^2)^{1/2}/2)$, temporal Fourier integration gives
$$
 C_R(n)=\int_{[-\pi,\pi]^3} |\widehat g_R(q)|^2
       \frac{h_1^2+h_2^2}{2\sinh\omega}\, e^{-n\omega}
                          \frac{d^3 q}{(2\pi)^3}.
$$
Spatial translation multiplies by a phase. The one-dimensional tent is the discrete convolution of a uniform length-$R$ interval with its reverse, times its mass. Consequently
$$
 |\widehat g_R(q)|^2=R^4 |1-e^{iRq_3}|^6
       \prod_{i=1}^3 \left|\frac{\sin(Rq_i/2)}{R\sin(q_i/2)}\right|^4.
$$
Both formulas concern the same packet at the two times. [Curvature projection and time Fourier integral](../../../central-quotients/tangent-curvature/dipole.md)

Let $R\to\infty$ and $n/R\to t\ge0$. On substituting $u=Rq$, $C_R(n)\to C(t)$ with
$$
 C(t)=\int_{\mathbb R^3}|1-e^{iu_3}|^6\prod_i\operatorname{sinc}^4(u_i/2)
       \frac{u_1^2+u_2^2}{2|u|}\,e^{-t|u|}\frac{d^3u}{(2\pi)^3},
 \qquad \operatorname{sinc}(v)=\sin(v)/v .
$$
The $R^4$ prefactor cancels the spatial volume change $R^{-3}$ and the $R^{-1}$ in the projected density. In the rescaled cube, each sine ratio is bounded by $C/(1+|u_i|)$, using the unit-modulus bound and $|\sin(q_i/2)|\ge |q_i|/\pi$. Also $R(h_1^2+h_2^2)/(2\sinh\omega)\le C|u|$. Thus $C|u|\prod_i(1+|u_i|)^{-4}$ dominates even at time zero and is integrable. The limiting density is strictly positive on an open cube around $(1,1,1)$, so $0<C(t)<\infty$ for every finite $t\ge0$.

Set $D_R=1+2 C_R(0)$. The elementary determinant of the Gaussian pair in each of three colors gives
$$
 B_R^{\rm free}(n)=[D_R^2-4 C_R(n)^2]^{-3/2}-D_R^{-3}.
$$
The denominator stays positive because $|C_R(n)|\le C_R(0)$. The corresponding continuum expression $B(t)$ has $D=1+2C(0)$ and $B(1)>0$.

Choose a fixed $0<b<B(1)/3$ and a fixed $c>0$ small enough that $C_1 c^4<b$ in (1). Take $R$ the largest even integer at most $c\beta^{1/8}$. For all sufficiently large $\beta$, $R\ge c\beta^{1/8}/2$ and $B_R^{\rm free}(R)\ge2b$. Hence $B_{\beta,R}(R)\ge b$ in every state. The centered transfer representation bounds the latter by $e^{-mR}\operatorname{Var}(O_R)\le e^{-mR}$. This also excludes vanishing centered transfer norm at such cutoffs. Taking a logarithm proves the claim. The proof needs no estimate on how quickly $C_R(R)$ approaches $C(1)$.

## Weight above the entire fixed space

The slow reading can also be attributed to genuine positive energies. The integral gives $C(1)>C(2)>0$ since its density is positive at nonzero momenta. The determinant is strictly increasing as a function of this positive covariance, so $B(1)>B(2)$. Choose a fixed $d>0$ smaller than one quarter of this difference. Shrink $c$ if necessary, now using (1) at both $R$ and $2R$. At all sufficiently large couplings,
$$
 B_{\beta,R}(R)-B_{\beta,R}(2R)\ge d .
$$
Let $\nu$ be the spectral measure of the centered packet for the lattice energy $E=-\log|T_\mu|$, assigning $E=+\infty$ on the nullspace of the transfer. Its total mass is at most one. For even $R$ the difference integrates $H(RE)=e^{-RE}(1-e^{-RE})$, with $H(\infty)=0$. The weight at zero energy drops out however many fixed vectors the state has. For $RE<d/2$ or $RE>\log(2/d)$ the response is at most $d/2$, since $H(z)\le\min(z,e^{-z})$. Everywhere it is at most $1/4$. Therefore
$$
 \nu\!\left(\left[\frac{d}{2R},\frac{\log(2/d)}{R}\right]\right)\ge 2d.
$$
This is a single scalar probe with a band determined by its limiting readings. For the positive Wilson transfer, $|T_\mu|=T_\mu$. The result supplies an upper bound on the bottom of the strictly positive spectrum even if the transfer has other vacua.

At any integer scales $R\to\infty$ with $R=o(\beta^{1/8})$, (1) gives $B_{\beta,R}(\lfloor tR\rfloor)\to B(t)$ including $t=0$ and each finite $t>0$, uniformly in periodic state selection. The estimate on $m$ gives $Rm\to0$ on those scales. The packet comparison does not supply a reading at the actual correlation length. [Formal and numerical checks](checks.md)

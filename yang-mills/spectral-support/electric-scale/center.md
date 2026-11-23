# Center flux at equal time, magnetic-energy scale and fixed physical time

On any finite marked link set $S$ let $A=Z(G)^S$. Extend each $z\in A$ by the identity to the other oriented edges. Write $z_p$ for its oriented product around a plaquette. Its link translation $T_z$ is unitary, commutes with gauge transformations and the electric kinetic operator, and sends a plaquette holonomy to $z_p U_p$ up to the choice of inverse for the translation. Fix the convention $T_z^* M_{v_p}T_z=M_{v(z_p U_p)}$. The joint spectral measurement of this finite abelian representation is an ordinary probability distribution $\mu$ on $\widehat A$ in the vacuum. Its Fourier coefficients are $\widehat\mu(z)=\langle\Omega,T_z\Omega\rangle$. For $SU(2)$ the measured bit on each edge is the parity of $n=2j$.

## Quasimodes in the actual vacuum

Use the Wilson action, group, and Hamiltonian from the [dimension proof](dimension.md), with $Q=H-E_0$, $u=\max_p\langle v(U_p)\rangle$, and $\lambda>0$. Put
$$V(z)=\sum_p v(z_p),\qquad D_z=2\sum_p\sqrt{v(z_p)u}.$$
All energy differences below use the same $\lambda$ that multiplies the magnetic action. Translating the vacuum equation gives the exact vector identity
$$T_z^*(Q/\lambda)T_z\Omega=\sum_p[v(z_p U_p)-v(U_p)]\Omega.$$
For unitary $A_0=\rho(z_p)$, $B=\rho(U_p)$, the error in each face's value relative to $v(z_p)$ is $-\operatorname{Re}\operatorname{Tr}[(A_0-I)(B-I)]/\dim\rho$. Hilbert–Schmidt Cauchy–Schwarz and $\|I-\rho(h)\|_{\rm HS}^2=2\dim\rho\,v(h)$ give
$$\|(Q/\lambda-V(z))T_z\Omega\|\le D_z.$$
Thus the spectral measure of $Q/\lambda$ in this unit vector has second moment about $V(z)$ at most $D_z^2$. This is a microscopic frequency statement derived from a one-time potential estimate. For nonflat twists put $v_*=\min\{v(c)>0:c\in Z(G)\}$ when that set is nonempty. Then $D_z/V(z)\le2\sqrt{u/v_*}$ even for growing marked sets. The spectral probability below $\lambda V(z)/2$ is at most $4D_z^2/V(z)^2$. On the complementary spectrum the semigroup is at most $e^{-t\lambda V(z)/2}$. In particular,
$$0\le C_z(t)=\langle T_z\Omega,e^{-tQ}T_z\Omega\rangle-|\langle\Omega,T_z\Omega\rangle|^2
\le 16u/v_*+e^{-t\lambda V(z)/2}.$$
For defining $SU(2)$, $v_*=2$ and $V(z)=2k$ for $k$ odd plaquettes. Here the bound is $8u+e^{-t\lambda k}$. In the bare matching $g=\beta^2/2$, $\lambda=\beta/b$, every nonflat single twist loses its connected weight at any fixed positive physical time when $b\downarrow0$ and $\beta\to\infty$. This exclusion is uniform in the number of odd faces. It concerns these particular unit vectors. Concluding that the whole theory has no low-energy states would require control on other probes and their linear combinations. [Clock and energy units](../../observable-normalization/energy-density/spatial-limit.md)

## Which electric center charges survive?

Let $F=\{z:\rho(z_p)=I\text{ on every face}\}$. This subgroup leaves the Hamiltonian unchanged. Positivity and simplicity of the ground state imply $T_z\Omega=\Omega$ for $z\in F$. This implies exact support on $F^\perp\subset\widehat A$ at all couplings. If $z\notin F$, project the residual on the vacuum: $|\widehat\mu(z)|\le D_z/V(z)$. Finite Fourier inversion yields convergence to the uniform law $\nu_F$ on $F^\perp$ along $g_G\to\infty$ for fixed marked geometry. More generally, with that lattice's own $F$,
$$\|\mu-\nu_F\|_{\rm TV}\le\tfrac12\Big(\sum_{z\notin F}|\widehat\mu(z)|^2\Big)^{1/2}
\le\sqrt{(|A|-|F|)u/v_*}.$$
This normalization uses counting measure on $\widehat A$ and Parseval with factor $1/|A|$. If the action is blind to the entire center, $F=A$ and the law is exactly concentrated at the trivial character. A faithful action can still have nontrivial $F$ from flat assignments.

For defining $SU(2)$ a single affected face gives a tighter estimate. The twist is a self-adjoint involution and anticommutes with multiplication by $x_p$, a self-adjoint contraction. Hence $(s x_p+t T_z)^2\le(s^2+t^2)I$ for real $s,t$. The two expectations satisfy $\langle x_p\rangle^2+\widehat\mu(z)^2\le1$, so $\widehat\mu(z)^2\le2u-u^2$ in the homogeneous vacuum.

## The six-link star in microscopic time

For the six edges incident to a vertex of a cubic torus of side at least three, there are twelve affected plaquettes. Each meets a pair of distinct coordinate axes at the vertex. The rows of its mod-two incidence matrix are those twelve pairs. They force a flat twist to have the same bit on every edge. The two flat assignments are identity and the central vertex gauge transformation. The limiting parity distribution is uniform over the 32 six-bit strings of even weight.

At microscopic time $t=\tau/\lambda$ the scalar $y\mapsto e^{-\tau y}$ is $\tau$-Lipschitz on $[0,\infty)$. The spectral theorem therefore gives
$$\|(e^{-\tau Q/\lambda}-e^{-\tau V(z)})T_z\Omega\|\le\tau D_z.$$
For fixed marked geometry and bounded microscopic times, any finite ordered vacuum correlation of center translations converges. Evaluate the word from right to left. Translation by $w$ takes the current twist $z$ to $wz$ exactly. Each semigroup can be replaced by the scalar at the current twist with a norm error at most $\tau D_z$, since all later operators are contractions. The final overlap tends to one for total twist in $F$, and to zero otherwise. This proves convergence of all such finite words and of the correlations of center-flux projectors by Fourier expansion.

For the star these are the stationary correlations of a continuous-time random walk on even six-bit patterns. Each of the twelve allowed pairs of bits flips together at rate one in $\tau$. Its character indexed by $z$ has decay rate $\sum_{\rm pairs}(1-(-1)^{z_i+z_j})=V(z)$. The constant character has rate zero. On the other 31 characters the rates are 8 (six characters), 12 (sixteen), and 16 (nine). The measure is uniform at stationarity. This local stochastic process occurs on times $b/\beta$ in the bare convention. Its first positive rate is dimensionless and scales to an ultraviolet energy $8\lambda$; identifying it with a physical mass would give the wrong clock and the wrong sector. [Generated exact star spectrum](ElectricScale.lean) · [Independent cubic incidence and stochastic checks](check_center.py)

## Uniform exclusion for bounded center observables

The single-twist estimate also controls a whole specified algebra. Let $f$ be any function of the marked center-flux outcomes with $\|f\|_\infty\le1$, let $K=|A/F|$, and put $\psi=(f-\langle f\rangle)\Omega$. For $K>1$ set $V_{\min}=\min_{z\notin F}V(z)\ge v_*$. On the exact support $F^\perp$, expand $f$ in its $K$ characters using uniform-measure coefficients $a_z$, indexed by $A/F$. Parseval gives $\sum |a_z|^2\le1$. The constant component vanishes on projection to the interval $(0,\lambda V_{\min}/2]$. Each nonconstant twist vector has projected norm at most $4\sqrt{u/v_*}$. The triangle inequality followed by Cauchy–Schwarz therefore gives
$$\|1_{(0,\lambda V_{\min}/2]}(Q)\psi\|^2\le16(K-1)u/v_*.$$
The finite box has a simple vacuum and $\|\psi\|^2\le1$. Consequently its positive-time connected autocorrelation is bounded by $16(K-1)u/v_*+e^{-t\lambda V_{\min}/2}$. This holds for a coupling-dependent bounded observable, even on growing marked sets provided $Ku\to0$. For trivial $K$ every such connected vector is zero. Thus the entire fixed local center-flux algebra loses connected spectral weight at fixed physical times on the weak-bare trajectory. The estimate controls the absolute weight; dividing a correlator by a vanishing variance can change that conclusion.

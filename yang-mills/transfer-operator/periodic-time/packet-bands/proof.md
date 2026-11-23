# Magnetic packets, Haar variation and a spectral window

## The spatial probes

Use positive links, quaternion norm, Wilson weight $\exp[-\beta\sum_p(1-\operatorname{Re}U_p)]$, and the time-first, then spatial $1,2,3$ paths $L_z$ from the origin. Write $F_p=\sqrt\beta\,\operatorname{Im}(L_zU_p L_z^{-1})$. The first-moment pressure bound gives $\sup_p\|F_p\|_{L^2}\le C$ and $\|1-U_p\|_{L^2}\le C/\sqrt\beta$ in every state under consideration. Thermodynamic limits are taken at fixed coupling before any scaling below. [Pressure estimate](../../../central-quotients/tangent-curvature/periodic-limit/pressure.md)

On $\mathbb Z^3$ let $A_R$ be the fourfold convolution of uniform probability on $\{0,\ldots,R-1\}^3$. For $i=0,\ldots,d-1$ put
$$
 f_{i,R}=R^2\tau_{iR e_1}(I-\tau_{R e_3})^3 A_R,\qquad
 X_{i,R}(t)=\sum_{\mathbf z} f_{i,R}(\mathbf z)F_{12}(t,\mathbf z),\qquad
 O_{i,R}(t)=e^{-s|X_{i,R}(t)|^2}.
$$
Here $\tau_u f(x)=f(x-u)$. The time trunk acts on the entire sum at a given time by one conjugation, so $O_{i,R}$ uses only links in that spatial slice. All spatial paths in that slice begin at its origin. In the interacting state one need not identify these different probes with exact translates of a single probe. They are exact translates in the reference Gaussian cochain pairing. Set $\psi_{i,R}=(O_{i,R}-\mu O_{i,R})\Omega$. The transfer matrix moments of this family are its connected correlation matrices, including the ordinary covariance at lag zero.

## A uniform estimate for a pair of probes

Let $g$ have just face orientation $12$, with one or two spatial profiles $y_j f_{i_j,R}$ at arbitrary times; $y_j\in\mathbb R^3$, $Y=\sum_j|y_j|$. Then $\|g\|_1\le8R^2Y$, $\|g\|_\infty\le8Y/R$ and all its spatial coordinates have norm at most $C_dR$. Convolution with probability preserves the bound $\|A_R\|_\infty\le R^{-3}$. Throughout this proof constants can depend on $d$.

For a finite one-cochain $h$, keep the incidences in the single-link Haar identity before taking its sum. Writing $w(e)=1+|\mathbf x_e|_1$, for any finite real colored face test $v$, the error in replacing $\mathbb E F(dh)e^{iF(v)}$ by $i\langle dh,v\rangle\mathbb E e^{iF(v)}$ is at most
$$
 \frac{C}{\sqrt\beta}
 \left(\|h\|_{1,w}
  +\sum_e |h_e|w(e)\sum_{p\ni e}|v_p|
  +\sum_{p}|v_p|\sum_{e\in L_{z(p)}}|h_e|\right).                 \tag{1}
$$
The edge sum inside the last term includes traversals in either direction. To see (1), for each varied edge choose the unit generator from the detour avoiding that edge. The discrepancy between the action derivative and the signed sum of rooted scaled faces is $O(w(e)/\sqrt\beta)$ in $L^1$. The direct derivative of each incident scaled face has the same error from its oriented constant generator. A derivative of the transporter acts by a commutator of norm at most $2|F_p|/\sqrt\beta$ when its path contains the edge, and vanishes otherwise. The test exponential has modulus one. Multiplication by the coefficient on each edge, summation and the uniform face bound give (1). The closure estimate from the cube identity is $\mathbb E|F(d^*k)|\le C\|k\|_{1,w}/\sqrt\beta$. All variations retain their finite supports in the fixed-coupling thermodynamic state. [Derivation of the three single-link estimates and closure](../../../central-quotients/tangent-curvature/periodic-limit/rate/ward.md)

Let $K=I-\Delta/16$, $S_M=16^{-1}\sum_{\ell<M}K^\ell$, with $\ell$ starting at zero. Set $h=d^*S_Mg$, $k=dS_Mg$, $u=dh$, $b=K^Mg$. Then $g=u+d^*k+b$, $u=P(g-b)$ with $P$ the exact two-form projection. Uniformly in $M$ and the times,
$$
 \|h\|_{1,w}+\|k\|_{1,w}\le C_d R^4 Y,\qquad
 \|h\|_\infty\le C Y,\qquad
 \|b\|_1\le C R^5 Y(1+M)^{-3/2}.                                \tag{2}
$$
For completeness, one difference of the heat kernel at $N=1+\ell$ has unweighted norm $O(N^{-1/2})$ and norm weighted by spatial distance $O(1)$. Four differences have respective norms $O(N^{-2})$ and $O(N^{-3/2})$. For $\ell\le R^2$ all translated coefficients of the normalized average lie at distance $O_d(R)$ in space; the sum of the weighted bounds $1+R N^{-1/2}$ is $O(R^2)$. For $\ell>R^2$, telescope each long difference into $R$ shifted unit differences. The sum of $R^3(N^{-3/2}+R N^{-2})$ over the tail is again $O(R^2)$. Multiplication by $R^2Y$ gives the first inequality. For the sup norm, at any time the convolution of a spatial slice of a kernel with $A_R$ is bounded by $R^{-3}$ times the full kernel's unweighted $\ell^1$ norm. The short and long sums are now $\sum_{\ell\le R^2}N^{-1/2}=O(R)$ and $R^3\sum_{\ell>R^2}N^{-2}=O(R)$. Multiplying by $R^2Y/R^3$ gives the second inequality. Three telescoped differences give the last inequality via the unweighted third-difference estimate. Bounded orientation shifts only affect constants. [Lazy-walk estimates and finite Hodge identity](../../../central-quotients/tangent-curvature/periodic-limit/rate/heat.md)

Apply (1) with $v=tg$, $0\le t\le1$. The incident term is at most $C\|h\|_{1,w}\|g\|_\infty\le C_dR^3Y^2$. For the path term observe that $h$ has only components $1,2$, since $S_M$ is componentwise and $g$ is purely magnetic with orientation $12$. Hence its pairing along any time trunk is zero. Each remaining path has at most $C_dR$ spatial steps, giving an upper bound $C_d R\|h\|_\infty\|g\|_1\le C_d R^3Y^2$. This is uniform even for widely separated slices.

Differentiate $\phi(t)=\mathbb E e^{itF(g)}$. Replace $F(g)$ in the prefactor by $F(u)$ using closure and $\mathbb E|F(b)|\le C\|b\|_1$. The phase still contains $g$, so the two incidence estimates apply to the original packet. Since $\langle u,g\rangle=\|Pg\|_2^2-\langle Pb,g\rangle$, one obtains
$$
 |\phi'(t)+t\|Pg\|_2^2\phi(t)|
 \le C_d\beta^{-1/2}(R^4Y+R^3Y^2)+C\|b\|_1+\|b\|_2\|g\|_2 .
$$
Integrate from zero to one with kernel $\exp[-(1-t^2)\|Pg\|_2^2/2]\le1$. At fixed $R,g,\beta$ send $M\to\infty$ in the bound. This proves the same characteristic-function estimate with only the first term on the right. No infinite-support link variation enters the argument.

A Gaussian Fourier variable of covariance $2sI_3$ represents each exponential $O_{i,R}$. Use two independent variables for a product, including at equal times, and use the one-variable estimate for each mean. Their first and second absolute moments are finite, so for every pair of probes, uniformly in the state, $R\ge1$ and integer lag $n\ge0$,
$$
 \big|\langle\psi_{i,R},T^n\psi_{j,R}\rangle-B^R_{ij}(n)\big|
 \le C_{d,s} R^4/\sqrt\beta .                                     \tag{3}
$$
Here $B^R$ is the centered matrix for three independent lattice Gaussian curvatures of covariance $P$.

## Spatial scaling and the free matrix

With $\widehat q_j=2\sin(q_j/2)$, $\omega(q)=2\operatorname{arsinh}(|\widehat q|/2)$, let $b_R(q)=\prod_{\alpha=1}^3[R^{-1}\sum_{v=0}^{R-1}e^{ivq_\alpha}]^4$. The one-color covariance is
$$
 C^R_{ij}(n)=R^4\int_{[-\pi,\pi]^3}e^{\mathrm i(i-j)R q_1}|b_R(q)|^2 |1-e^{iR q_3}|^6
 \frac{\widehat q_1^2+\widehat q_2^2}{2\sinh\omega(q)}e^{-n\omega(q)}\frac{d^3q}{(2\pi)^3}.
$$
The integral is real by symmetry. This follows from the diagonal $12,12$ symbol of $P$ after integrating time momentum. With $D_R=1+2s C^R_{00}(0)$, the two-time Gaussian determinant gives $B^R_{ij}(n)=[D_R^2-4s^2 C^R_{ij}(n)^2]^{-3/2}-D_R^{-3}$. [Time Fourier integral and determinant](../../../central-quotients/tangent-curvature/periodic-limit/rate/spectrum.md)

Set $b(p)=\prod_\alpha[\int_0^1e^{iup_\alpha}\,du]^4$ and define the finite measure
$$
 W(dp)=|b(p)|^2|1-e^{ip_3}|^6
 \frac{p_1^2+p_2^2}{2|p|}\frac{d^3p}{(2\pi)^3}.
$$
For integer $n/R\to t\ge0$, $R\to\infty$, $C^R_{ij}(n)\to C_{ij}(t)=\int e^{\mathrm i(i-j)p_1-t|p|} W(dp)$. Indeed $p=Rq$ absorbs $R^3$ from the integration measure. The remaining $R(\widehat q_1^2+\widehat q_2^2)/(2\sinh\omega)$ is bounded by $|p|/2$, since $\sinh\omega\ge|\widehat q|$. Also $|b_R(p/R)|^2\le C\prod_\alpha(1+|p_\alpha|)^{-8}$ throughout the scaled cube, by the geometric sum and $|\sin(q_\alpha/2)|\ge |q_\alpha|/\pi$. This dominates the equal-time integral. Write $D=1+2s C_{00}(0)$; the limiting connected matrix $B_{ij}(t)$ has the same determinant formula with $D,C_{ij}(t)$.

## A band projection with full matrix rank

Write $B_{ij}(t)=\sum_{\ell\ge1} b_\ell C_{ij}(t)^{2\ell}$. The binomial expansion gives $b_\ell=D^{-3}(3/2)_\ell(4s^2/D^2)^\ell/\ell!>0$, where $(3/2)_\ell$ is the rising factorial. It converges absolutely even at $t=0$ because $2s C_{00}(0)/D<1$. For each term form a finite matrix measure in scaled energy $\epsilon$ by integrating
$$
 b_\ell\,[e^{\mathrm i(i-j)\sum_{r=1}^{2\ell}p_{r,1}}]_{ij}
 \ \prod_{r=1}^{2\ell}W(dp_r),\qquad \epsilon=\sum_{r=1}^{2\ell}|p_r|.
$$
The matrix in the integrand is a positive rank-one Gram matrix; total diagonal masses sum to the finite $B_{00}(0)$. The sum is thus a finite positive matrix measure $\Sigma$ with Laplace transform $B(t)$. Under $x=e^{-\epsilon}$ its moments of integer order $m\ge0$ are precisely $B(m)$, including the mass at order zero. Equation (3) and polynomial approximation on $[0,1]$ prove weak convergence to this matrix for $R\to\infty$, $R^4/\sqrt\beta\to0$, uniformly over the eligible states for each fixed continuous test. Indeed every entry has total variation at most the geometric mean of the two diagonal masses by spectral Cauchy–Schwarz, and each finite-coupling diagonal mass is at most one.

Fix a continuous $0\le f(x)\le1$ supported strictly inside $(e^{-b},e^{-a})$ and positive on some open subinterval. The $\ell=1$ contribution alone makes $\int f\,d\Sigma$ strictly positive definite. For nonzero $v\in\mathbb C^d$ its quadratic form contains a positive constant times the integral of
$$
 f(e^{-|p|-|q|})\left|\sum_{j=0}^{d-1}v_j e^{-\mathrm i j(p_1+q_1)}\right|^2 W(dp)W(dq).
$$
The energy window has a nonempty open preimage in $\mathbb R^6$. The density of $W$ is positive off a union of planes and lower-dimensional sets of zero Lebesgue measure. The finite polynomial in $e^{-i(p_1+q_1)}$ can vanish only on a countable collection of hyperplanes unless all $v_j=0$. The integral is therefore positive for every nonzero $v$. Write $\lambda>0$ for the least eigenvalue of the window matrix.

Choose a real polynomial $P_f(x)=\sum_{m=0}^M a_m x^m$ uniformly close enough to $f$ that the two approximation errors in matrix norm sum to less than $\lambda/4$. This is possible using the uniform mass bounds above and fixed $d$. Moment comparison at the finitely many lags $mR$ costs at most $d C_{d,s}(\sum_m|a_m|)R^4/\sqrt\beta$ plus a quantity tending to zero as $R\to\infty$ from the free integrals. Choose $c>0$ sufficiently small that the former is less than $\lambda/8$ for $R=\lfloor c\beta^{1/8}\rfloor$. At sufficiently large coupling the latter is also less than $\lambda/8$. The actual finite-coupling matrix weighted by $f(e^{-RE})$ thus dominates $(\lambda/2)I_d$. The spectral projection in the theorem dominates this matrix as quadratic forms. This supplies $\eta=\lambda/2$ without requiring a sign for approximating polynomial coefficients or comparing sharp indicators by their moments. It also excludes a possible atom at infinite energy in the lattice transfer kernel from the band.

The argument gives neither numerical universal constants nor an isolated glueball level. A sharp boundary of the spectrum at fixed coupling and the law of the fields at the physical correlation-length scale require further input. [Program reduction](../../../z4/attempt/A1_REDUCTION.md)

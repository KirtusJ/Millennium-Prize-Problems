# Polynomial approximation of the ordinary flowed plaquette

Use the radius-$R$ neighborhood of the four target links in the graph joining cofacial spatial links. It contains at most $r=3(2R+7)^3$ distinct links, since a cofacial step moves the base point by at most one in each coordinate. Wrapping can only reduce the count.

For any central polynomial probability density $\xi$ on SU(2), independently replace each retained input $U_e$ by $V_e=q_e U_e$ with $q_e$ of law $\xi\,dH$. Set all other inputs to the identity. Evolve the resulting full spatial slice to time $u$, read the plaquette deficit, and average over the noise. Changing variables to $V_e$ puts the entire dependence on the original input in $\prod_e\xi(V_e U_e^{-1})$. A density of degree $d$ in the quaternion scalar part therefore gives a polynomial of degree at most $d$ per retained link, regardless of the nonlinear flow inside the integral. Average over the Haar gauge transformations at the patch vertices. They act by linear left and right multiplication, preserve the degree and the range $[0,2]$, and preserve the error against the gauge-invariant target. They also cover every gauge transformation affecting a retained link.

Let $\delta=\mathbb E|q-1|$ in quaternion chord distance. With the cofacial count matrix $A$, the distance comparison for the spatial Wilson ODE is $d_e(u)\le\sum_f(e^{uA})_{ef}d_f(0)$. For each of the four target links, the expected contribution from kept links is bounded by $\delta$ times the **row sum**, at most $\delta e^{16u}$. The omitted links are at distance greater than $R$, start at distance at most two, and contribute at most $2T_R$ per target link. The plaquette trace is Lipschitz with constant one in each of its four factors. Hence the gauge-averaged polynomial $P$ satisfies
$$
\|F_u-P\|_\infty\le4e^{16u}\delta+8T_R,\qquad T_R=\sum_{j>R}(16u)^j/j!.
$$
The number of links in the patch does not multiply the smoothing error. Orthogonal centering in the Wilson vacuum gives the same $L^2$ error for the centered vectors, and the centered polynomial has sup norm at most two. [ODE comparison and clock](../spatial-flow-variance/README.md) · [Spatial flow in lattice spectroscopy](https://arxiv.org/pdf/2211.15176)

For a simple explicit approximation take $\xi_d(q)\propto(1+\operatorname{Re}q)^d$. Under this law $X=(1+\operatorname{Re}q)/2$ has the beta distribution with parameters $d+3/2,3/2$. Since $|q-1|^2=4(1-X)$, one has $\delta\le\sqrt{6/(d+3)}$. Make $8T_R$ and then the smoothing term arbitrarily small, uniformly in the spatial volume. The inverse budget for the centered polynomial is bounded by $4 k_{\min}^{-r}\max(1,A_d)^{2r}$. [Patch inverse proof](inverse-form.md)

## A uniform upper tail at large lattice energy

For integer $m\ge2$, instead use the density proportional to
$$
J_m(\theta)=\left(\frac{\sin(m\theta/2)}{\sin(\theta/2)}\right)^6.
$$
The squared ratio is the squared modulus of a geometric sum of $m$ phases, a polynomial of degree $m-1$ in $\cos\theta$. Cubing gives degree $3(m-1)$. Use its continuous value $m^6$ at the origin. In the probability-Haar expectation the common angular normalizer cancels. On $0\le\theta\le1/m$ the ratio is at least $2m/\pi$ and $\sin\theta\ge2\theta/\pi$, giving $\int_0^\pi J_m\sin^2\theta\,d\theta\ge(2/\pi)^8 m^3/3$. The absolute ratio is everywhere at most $\min(m,\pi/\theta)$. Bounding the chord by $\theta$ and splitting at $1/m$ gives
$$
\int_0^\pi 2\sin(\theta/2)J_m\sin^2\theta\,d\theta
\le (1/4+\pi^6/2)m^2.
$$
Thus $\delta=O(1/m)$. With $R=\lceil16eu+2\log(m+1)\rceil$, $T_R\le\exp(16eu-R)\le(m+1)^{-2}$ by exponential reweighting of the series. The error is $O_u(1/m)$ and $r=O_u((1+\log m)^3)$. The degree dependence of the inverse budget follows from $\log^+ A_d=O_\beta((d+1)\log(d+2))$. This gives $\log\max(1,B_m)\le C_{\beta,u}m(1+\log m)^4$ for its inverse budget $B_m$.

For a dimensionless energy cutoff $t$, project onto $0\le\lambda\le e^{-t}$. The centered polynomial has no mass at $\lambda=0$ and its projected norm is at most $e^{-t/2}\sqrt{B_m}$. The projected norm of the flowed reading is at most this plus $O_u(1/m)$. For all sufficiently large $t$ take $m=\lfloor t/[2C_{\beta,u}(1+\log t)^4]\rfloor$, increasing $C_{\beta,u}$ to at least one. Then $B_m\le e^{t/2}$ and
$$
\nu_u\{E\ge t\}=O_{\beta,u}\!\left(\frac{(1+\log t)^8}{t^2}\right).
$$
In particular there is no atom at infinite energy. Layer-cake integration against $p t^{p-1}\,dt$ gives uniformly finite $p$th moments for $0<p<2$. The bounds also hold for a thermodynamic spectral limit. For an upper tail at $t$, use the open transfer set $[0,e^{-(t-1)})$ in $[0,1]$ at the slightly lower cutoff $t-1$ and the open-set Portmanteau inequality. Alternatively apply lower semicontinuity directly to $(-\log\lambda)^p$. The second moment at $p=2$ and a cutoff uniform in a continuum scaling limit are outside this estimate.

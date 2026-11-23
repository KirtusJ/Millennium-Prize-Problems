# One electric derivative of the discrete Wilson vacuum

Consider the SU(2) spatial torus of side $L\ge2$ with $N=3L^3$ edges and $N$ plaquettes. Use unit quaternions, normalized Haar, $\kappa>0$, $\gamma=1/(2\kappa)$, finite $\lambda\ge0$, and
$$
 h_e=\gamma(-\Delta_e),\quad H_0=\sum_e h_e,\quad
 W=\lambda\sum_p(1-\phi_p),\quad \phi_p=\tfrac12\operatorname{Tr}(U_p),\quad H=H_0+W .
$$
Let $K=K_a$ be the product of the one-link Wilson convolutions at $g=\kappa/a$, $M=e^{-aW/2}$, $T=MKM$, $\rho=\|T\|$, $S=T/\rho$ and $\ell=-a^{-1}\log\rho$. The strictly positive, normalized vacua of $T,H$ are $\Omega_a,\Omega$, and $E_0$ is the bottom of $H$. Multiplying the positive free kernel by the two factors $M$ gives $T(x,y)\ge e^{-aB}K(x,y)$ for $B=2\lambda N$. Testing against the constant unit vector and using $\|K\|=1$ gives $e^{-aB}\le\rho\le1$. Thus $W,E_0,\ell$ all lie in $[0,B]$ in their respective senses.

## Recovering a derivative through the free kernel

On a joint kinetic mode let $x$ be the eigenvalue of $H_0$, $k$ the eigenvalue of $K$, and $d=(1-k)/a$. The all-order Wilson convolution estimates give $x/(1+ax)\le d\le x$ and $0<k\le1$. Define $L_a$ by the multiplier $xk/d=x/d-ax$ for $x>0$ and by 1 at zero. Then
$$
 0\le L_a\le I,\qquad H_0K=L_a(I-K)/a,\qquad
 \|(I-L_a)f\|\le a\|H_0 f\|\quad (f\in D(H_0)).
$$
The identity holds as a bounded operator, since $(I-K)/a$ is bounded at fixed $a$. The final inequality follows from $0\le1-xk/d\le ax$ mode by mode, then summation. It includes arbitrarily high link representations. [Product Bessel bounds](../joint-cutoff/README.md) · [Lean multiplier and squared-norm bounds](PeriodicTime.lean)

Take $aB\le1$. Write $u_a=M^{-1}\Omega_a$. The vacuum equation gives $u_a=\rho^{-1}KM\Omega_a$. Consequently
$$
 H_0u_a=L_aJ_a(W)\Omega_a,\qquad
 J_a(W)=\frac{\rho^{-1}M-M^{-1}}{a}
       = e^{aW/2}\frac{e^{a(\ell-W)}-1}{a}.
$$
The scalar bounds $\|J_a\|_\infty\le5B$ and $\|J_a-(\ell-W)\|_\infty\le5aB^2$ follow from Taylor's integral remainder for $|a(\ell-W)|\le1$, $e^{1/2}<2$, and $e^{aW/2}-1\le aB$. For the first bound one can use $e^{1/2}e<5$ directly. Write
$$
 G_1=4\lambda\sqrt N,\quad D_1=12\gamma\lambda N,\quad
 J_0=B^2+D_1+2G_1\sqrt{\gamma B},\quad \epsilon=\|\Omega_a-\Omega\|.
$$
The plaquette derivative and vacuum product estimates give $\|\nabla W\|_\infty\le G_1$, $\|H_0W\|_\infty\le D_1$, $\|H_0\Omega\|\le B$ and $\|H_0^2\Omega\|\le J_0$. Apply $L_a$ to the difference between $J_a(W)\Omega_a$ and $(E_0-W)\Omega$; the last vector is $H_0\Omega$. The multiplier bound controls replacing $L_aH_0\Omega$ by $H_0\Omega$. This yields
$$
 \|H_0u_a-H_0\Omega\|
 \le B\epsilon+|\ell-E_0|+5aB^2+aJ_0 .
$$
[Plaquette incidence, gradient bounds and $H_0^2\Omega$](../joint-cutoff/energy-density.md)

To return to $\Omega_a=Mu_a$, use $\|u_a\|\le2$, $\|H_0u_a\|\le5B$ and $\sqrt\gamma\|\nabla u_a\|\le\sqrt{10B}$ by integration by parts. Differentiating $M$ gives $\|\nabla M\|_\infty\le aG_1/2$, $\|H_0M\|_\infty\le aD_1/2+\gamma a^2G_1^2/4$. In the product rule compare $M H_0u_a$ with $M H_0\Omega$ first, then bound $\|(M-I)H_0\Omega\|\le aB^2/2$. In total,
$$
 \|H_0(\Omega_a-\Omega)\|\le
 G_a:=B\epsilon+|\ell-E_0|
 +a\big(6B^2+J_0+D_1+G_1\sqrt{10\gamma B}\big)
 +\tfrac12\gamma a^2 G_1^2 .
$$
The bound vanishes at each fixed box as $a\downarrow0$. All derivatives use the full finite product manifold. The operators and vacua restrict to the gauge-invariant Hilbert space.

## Comparing the three readings

For fixed weights, possibly complex, let $O=\sum_e w_e h_e+\sum_p w_p\lambda(1-\phi_p)$, $A_w=\sum_e |w_e|$, $P_w=\sum_p |w_p|$. All kinetic factors are simultaneously diagonal and $h_e\le H_0$ there. With $K_O=A_wB+2\lambda P_w$ and $\eta=A_wG_a+2\lambda P_w\epsilon$,
$$
 \|O\Omega\|\le K_O,\qquad \|O\Omega_a-O\Omega\|\le\eta .
$$
Use $t>0$, $n=\lfloor t/a\rfloor\ge1$, $p(X)=X(I-X)^2$, $X=e^{-t(H-E_0)}$ and $Y=S^n$. Put $D_H(t)=\langle O\Omega,p(X)O\Omega\rangle$. The bound for two positive contractions is $\|p(X)-p(Y)\|\le3\|X-Y\|$ by a three-factor telescope. Thus
$$
 |\langle O\Omega_a,p(Y)O\Omega_a\rangle-D_H(t)|
 \le (2K_O+\eta)\eta+3K_O^2\mathcal E_a(t) .
$$
Here $\mathcal E_a(t)$ is the explicit norm estimate below, with $k=\lceil(t/a)^{1/3}\rceil$ and $c=B+12\gamma$:
$$
 \mathcal E_a(t)=2/n+3a/t+7ac+4/k+72ak^2/t+144atc^2 .
$$
At $a\le t/2$, $ac\le1/36$ and $72ac^2\le d_L$, one can substitute $\epsilon\le72\sqrt2\,ac^2/d_L$, $|\ell-E_0|\le90ac^2$, $d_L=\gamma\,2^{-N}e^{-B/\gamma}$. This is the uncapped version of the earlier comparison. The physical trace and a deterministic finite approximation of these measurements are described in the accompanying note. [Evolution](../joint-cutoff/evolution.md) · [Energy and vacuum estimates](../joint-cutoff/README.md) · [Finite-volume gap floor](../joint-cutoff/finite-volume-vacuum.md) · [Periodic measurements](measurements.md)

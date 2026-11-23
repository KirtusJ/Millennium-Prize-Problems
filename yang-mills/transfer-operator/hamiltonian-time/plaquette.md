# Plaquette fluctuations and the true Hamiltonian vacuum

Use the periodic cubic Hamiltonian $H=(2\kappa)^{-1}\sum_e A_e+\lambda\sum_p(1-\phi_p)$ from the [time-limit construction](README.md), with $A_e=-\Delta_e$ on the unit three-sphere, $\phi_p=\operatorname{Tr}(U_p)/2$, and $z=\kappa\lambda$. The number of edges equals the number of oriented-positive faces, $N_e=N_p=3L^3$. Translation and cubic symmetry of the unique positive vacuum $\Omega$ make the mean kinetic energy the same on each edge and the mean action the same on each face. All claims below use $L\ge2$, so each elementary face has four distinct edge variables, including on the side-two torus.

## A positive-time test with explicit constants

The constant product vector has zero kinetic energy and zero mean plaquette trace. The variational principle and the nonnegative plaquette potential therefore give $\langle H_0\rangle_\Omega\le\lambda N_p$. For the projection $P_e$ onto constants of edge $e$, the electric spectrum gives $A_e\ge3(I-P_e)$. Hence $\langle I-P_e\rangle\le 2z/3$ for each edge. For the four edges of a face their commuting product $P$ satisfies $\epsilon=1-\langle P\rangle\le8z/3$.

When $z\le1/384$, put $d=\sqrt\epsilon\le1/12$. The unit vectors $\Omega$ and $P\Omega/\|P\Omega\|$ have overlap $\sqrt{1-\epsilon}$, so their pure-state trace distance (half the trace norm) is $d$. The latter vector factors as the Haar constant on the four face links times an exterior vector. Its unnormalized plaquette trace $F=2\phi_p$ thus has mean zero and second moment one, by character orthogonality. A real observable of range four changes its expectation by at most $4d$. Both $F\in[-2,2]$ and $F^2\in[0,4]$ have this range. Writing $s=\langle F^2\rangle_\Omega$ and $v=\operatorname{Var}_\Omega F$, we obtain $s\ge2/3$ and $v\ge1-4d-16d^2\ge5/9$.

For $w=(F-\langle F\rangle)\Omega$, the first energy moment is
$$
M=\langle w,(H-E_0)w\rangle=\frac{2}{\kappa}(4-s).
$$
Indeed the ground-state equation tested on $(F-\langle F\rangle)^2\Omega$ cancels the multiplication potential and the derivatives of the ground state. On each of four links the squared gradient of $F$ is $4-F^2$ in the chosen unit-angular metric. Thus $M/v\le12/\kappa$. Jensen’s inequality, or the integrated tangent to the exponential against the positive normalized spectral measure, now gives for every $t\ge0$
$$
\langle w,e^{-t(H-E_0)}w\rangle \ge \tfrac59 e^{-12t/\kappa}.
$$
This proves a nonzero return at fixed positive physical time with the spatial mesh fixed. It also bounds the lowest physical excitation from above by $12/\kappa$. Combined with the local stability theorem, the physical gap lies between two volume-independent positive finite numbers when both smallness conditions hold. In this overlap regime the centered spectral measure has at least $5/18$ mass in the bounded positive interval $[3\gamma/(8\kappa),24/\kappa]$. Indeed the gap excludes the lower tail, and Markov’s inequality bounds mass above $24/\kappa$ by $v/2$. At each fixed such coupling the spectral measures have uniformly bounded masses and first moments; they are tight. Any weak subsequential limit retains the variance floor and the displayed time correlations. This conclusion needs no exchange of the spatial-volume and time-cutoff limits. [A4’s ground-state transform with half-speed generators](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/778bc8cf5ca99bcd104392ea419eeb55efc6a1d2/yang-mills/observable-normalization/wilson-loop)

## The plaquette action at large magnetic coupling

Let $K=\langle A_e\rangle_\Omega$ and $d_p=\langle1-\phi_p\rangle_\Omega$. A product trial wavefunction gives stronger kinetic control than the constant trial at large $z$. For $z>0$ set $u=\sqrt z$, and on every edge take the wavefunction proportional to $e^{h x/2}$, with $x=\operatorname{Tr}(U)/2$ and $h=4u$. The squared amplitude tilts Haar by $e^{h x}$. This vector is admissible for the unrestricted Hamiltonian, whose bottom equals the physical ground energy by uniqueness and gauge invariance. Gauge projection of the trial itself is unnecessary.

Let $r=\mathbb E_h x\in[0,1]$, using symmetry to see $r\ge0$. The one-link matrix mean is $rI$ by conjugation invariance. The four independent variables of a face give mean $r^4$ for $\phi_p$. On $S^3$, $|\nabla x|^2=1-x^2$ and $\Delta x=-3x$. Integrating by parts in $e^{hx}$ gives $h\mathbb E_h(1-x^2)=3r$, hence the one-link trial expectation of $A_e$ is $3hr/4$.

For $y=1-x$ the Haar density tilted by $e^{hx}$ is proportional to $e^{-hy}y^{1/2}\sqrt{(2-y)_+}$ on $y>0$. Begin with a Gamma variable of shape $3/2$ and rate $h$. Tilting by the nonincreasing factor $\sqrt{(2-y)_+}$ can only decrease the mean of $y$: the covariance has the sign of the expectation of the product of differences on two independent samples. The Gamma mean follows by integrating by parts. This proves $1-r\le3/(2h)$. Since $1-r^4\le4(1-r)$, the variational bound per face in units of $1/\kappa$ is
$$
\frac K2+z d_p\le\frac{3hr}{8}+z(1-r^4)\le 3\sqrt z.
$$
In particular $K\le6\sqrt z$ and $\sqrt z\,d_p\le3$. The number of sites has canceled. These are estimates in the true interacting vacuum. The product trial's own plaquette distribution enters only on the right.

There is a converse bound on the mean action. For any edge of $p$, Haar integration by parts in the real ground state and $\Delta_e\phi_p=-3\phi_p$ give
$$
9\langle\phi_p\rangle^2
\le 4K\,A,\qquad A=\langle|\nabla_e\phi_p|^2\rangle=\langle1-\phi_p^2\rangle\le2d_p .
$$
The derivatives are those of the based holonomy; left/right translations and inversion preserve the round metric. If $z\ge36$, the upper action estimate gives $\langle\phi_p\rangle\ge1/2$. Substitution then proves
$$
\frac{3}{64}\le\sqrt z\,d_p\le3,\qquad
\frac{3}{32}\le\sqrt z\,A\le6 .
$$
The first plaquette energy moment satisfies $M=8A/\kappa$, so $3/(4\kappa\sqrt z)\le M\le48/(\kappa\sqrt z)$ in this regime. These estimates concern a one-face ground-state expectation and its first energy moment. They do not establish a weak-coupling spectral gap or the scale of the spatial correlation length.

A4 independently proved a one-link radial estimate for the unnormalized trace on a periodic cubic torus of side at least three. In the present notation it gives $v\ge[128\pi^4(1+K)^2]^{-1}$. The half-speed convention there has kinetic coefficient $2/\kappa$, per-edge kinetic expectation $K/4$, and coupling ratio $g=z/2$. Using our exponential trial, put $v_z=[128\pi^4(1+6\sqrt z)^2]^{-1}$. At every fixed $z>0$ and $L\ge3$, $v\ge v_z$ and $M\le(8/\kappa)\min(1,6/\sqrt z)$. The tangent bound therefore supplies a strictly positive time-separated correlator at every fixed $t$ after taking the Wilson time limit, uniformly in $L$. At large $z$ its bound on $M/v$ grows at most as a constant times $\sqrt z/\kappa$. On the bare tree-level spatial trajectory in the main note this scale is $1/b$. A fixed spatial mesh is essential to the finite-energy conclusion from these estimates. [A4’s radial proof and generator conventions](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/a751b0bf6d99fc55067963d52075c91af216571a/yang-mills/observable-normalization/hamiltonian-variance)

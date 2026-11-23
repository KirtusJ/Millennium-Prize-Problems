# Spacetime clustering on interacting cubic Wilson Hamiltonians

Work on a periodic cubic torus of side at least three in the half-speed $SU(2)$ link convention $X_i=i\sigma_i/2$. In the bare parametrization $\kappa=2/(\beta b)$, $\lambda=\beta/b$, where $b$ is the spatial mesh. B4's blocked transfer theorem yields the full physical Hamiltonian gap $m_0=c_0/(\beta b)$ as a **lower bound**, with $c_0=4\log(3)/13$, for $0<\beta^2\le1/384$. The proof first bounds the transfer on the original blocked histories, then uses fixed-volume convergence to the Hamiltonian. The symbol used for the electric coefficient in B4's transfer is $\kappa_B=\beta b$. [B4's proof](../../transfer-operator/blocked-time/) · [Clock conversion](../momentum/wilson-time.md)

Let $A,B$ be any bounded self-adjoint operators on link sets $X,Y$ that preserve the physical sector. They may be restrictions of local operators on the full tensor product. Use the restriction to such local operators for the following norm bounds. Write $R$ for the least physical distance between link midpoints in the two supports divided by $b$, and suppose $R>2$. Let $J_X,J_Y$ be the sets of faces meeting the respective supports. The two-cut estimate applies in either probe order, with
$$
 D=\frac{8\beta}{b^3}\|A\|\|B\|\,|J_X||J_Y|,\quad p=3,\quad
 d=\mu(R-2),\quad h=b^{-1}\sqrt{3K(\mu)},\quad
 K(\mu)=4+8e^{\mu/\sqrt2}+4e^\mu .
$$
These operator norms may safely be taken on the full tensor product before restriction. The estimate admits electric Casimir projections at any spin threshold. It also admits operators supported on macroscopic sets, with the displayed support factors. [Two cuts and the full link Hilbert space](../locality/bounded-observables.md)

**A uniform rate.** Throughout the stated coupling interval $m_0>6/b$, since $\log3>1$ and $\sqrt{384}>19.5$. At $\mu=2$, $h<16/b$ follows from $e^{\sqrt2}<5$, $e^2<8$. Thus take $m=6/b$, $h=16/b$ as valid bounds, $T=2b(R-2)/\sqrt{292}$, and use $c_3=1/4$. For every $s\ge0$,
$$
 \left|\operatorname{Re}\langle a,e^{-sQ}b_1\rangle\right|
 \le\left[V+2\beta\|A\|\|B\|\,|J_X||J_Y|(T/b)^3\right]
 \exp\!\left[-\sqrt{(6s/b)^2+(0.7(R-2))^2}\right].
$$
Here $b_1=(1-P_0)B\Omega$ distinguishes the vector from the mesh. The spatial coefficient before rounding down is $12/\sqrt{292}>0.7$. The bound holds for each finite box with the same constants and therefore for any thermodynamic limit of the readings. At fixed positive physical spatial separation, polynomial growth of the support sizes and norms is harmless when $b\downarrow0$. This conclusion includes separated bounded electric observables to which a classical site-oscillation estimate for multiplication readings need not apply. It is consistent with B4's earlier independent temporal suppression in this interval. [B4's local limit and boundary comparison](../../transfer-operator/blocked-time/local-limit.md)

**The rate at smaller $\beta$.** Keep $m=m_0$, set $T=\mu(R-2)/\sqrt{h^2+m_0^2}$, and retain the same prefactor $V+D T^3/4$. The coefficient of $(R-2)$ in the spacetime exponent is
$$
 \frac{\mu}{\sqrt{1+3(\beta/c_0)^2 K(\mu)}}.
$$
Since $K(\mu)\le 16 e^\mu$ for $\mu\ge0$, the coefficient is at least $\mu/\sqrt{1+48(\beta/c_0)^2e^\mu}$. Maximize this last explicit lower bound. Put
$$
 w=W\!\left(\frac{c_0^2}{24e^2\beta^2}\right),\qquad \mu=w+2,
$$
where $W$ denotes the positive solution of $we^w=x$. Differentiation gives the stationary equation $(\mu-2)48(\beta/c_0)^2e^\mu=2$, with a unique maximum. Substitution gives the rigorous spatial rate $\sqrt{w(w+2)}$. At fixed $\beta$ the remaining prefactor grows at most polynomially in $R$ for bounded local supports. As $\beta\downarrow0$, the rate is $2\log(1/\beta)-\log\log(1/\beta)+O(1)$, by taking logs in $we^w=x$. The numerical control at $\beta=10^{-3}$ gives a guaranteed rate $5.79695$; evaluating the exact $K$ at the same tilt yields $6.47517$. This is a lower bound on a decay rate. Equality with the true inverse correlation length is open. [Independent clock calculations](checks.py)

The weak bare-coupling path $\beta\to\infty$ leaves the input gap theorem. On that path the inverse spatial test and volume-uniform commutator bound are available. The strong-coupling decay rate derived here cannot be extrapolated to it.

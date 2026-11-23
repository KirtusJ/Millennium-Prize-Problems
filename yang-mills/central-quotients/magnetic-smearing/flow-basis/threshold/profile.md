# The moving threshold profile and compact momentum packets

Use the squared Fejér amplitude $f_m$ defined in the [cost proof](proof.md). All averages below normalize the squared norm to one.

## Fixed nonzero momentum

At fixed $k>0$, put $t=mx$. Its limiting density is proportional to $t^{1/2}\operatorname{sinc}^8(\gamma\sqrt t)$, $\gamma=\sqrt{b-a}/2$. Conditionally on $t$, the variable $V=|z|/\sqrt x$ becomes uniform on $[0,1]$ and independent of $t$ in the limit. Indeed $x=t/m<k^2$ for each fixed positive $t$ eventually. On the whole conditional interval, the unnormalized angular density tends uniformly to a positive constant after rescaling $z=\sqrt{x}V$. The factor in the radial density is $w_k(x)\sim k^2\sqrt x$. It follows that the limiting law of $m(E^2-k^2)$ is the law of $t(1-V^2)$.

The convergence includes its first moment. The radial comparison gives $\sqrt m\, w_k(t/m)/k^2\le5\sqrt t(1+t/(mk^2))$, and $0\le m(E^2-k^2)\le t$. The integrable Fejér majorants and the separate exponentially damped far tail in the cost proof therefore also control this moment. The same tail argument applies to $2km(E-k)$, since its ratio to $m(E^2-k^2)$ is $2k/(E+k)\le1$ and tends to one at fixed $t$.

For $n=2,4,6$ write $I_n=\int_0^\infty \sin^8(v)v^{-n}\,dv$. One has $I_2=5\pi/32$, $I_4=I_6=\pi/12$. To obtain $I_6$, expand $128\sin^8(v)$ as $56(1-\cos 2v)-28(1-\cos 4v)+8(1-\cos 6v)-(1-\cos 8v)$. The signed quadratic and quartic coefficients both vanish. Four integrations by parts reduce the integral of $[1-\cos(cv)-(cv)^2/2+(cv)^4/24]/v^6$ to $c^4/120$ times the integral of $(1-\cos(cv))/v^2$, hence $\pi c^5/240$ for $c\ge0$. The weighted fifth powers sum to $2560$. The analogous second and fourth denominator calculations use the signed first and third powers. [Earlier harmonic calculation](../resolution.md) · [Supporting arithmetic](MovingThreshold.lean)

The mean of $t$ is $I_4/(\gamma^2 I_6)=1/\gamma^2$. Integrating $1-V^2$ contributes $2/3$, giving
$$
\lim_{m\to\infty}m\langle E^2-k^2\rangle
=\lim_{m\to\infty}2km\langle E-k\rangle
=\frac{8}{3(b-a)}.
$$
At rest $mE^2=t$ has density proportional to $t^{3/2}\operatorname{sinc}^8(\gamma\sqrt t)$. Its mean is $I_2/(\gamma^2 I_4)=15/[2(b-a)]$. In the moving calculation the conditional angular factor persists however small the fixed positive momentum is.

## The transition scale

Taking $k=\kappa/\sqrt m$ for fixed $\kappa>0$ retains both angular and radial effects. In variables $e=\sqrt m E$, $\zeta=\sqrt m z$, and $t=e^2+\zeta^2-\kappa^2$, the limiting normalized law has density proportional to
$$
\frac{(e^2-\kappa^2)^2+(\kappa^2-\zeta^2)^2}{\kappa}
\operatorname{sinc}^8(\gamma\sqrt t)\,de\,d\zeta ,
\qquad e>\kappa,\quad |\zeta|<\kappa .
$$
The Jacobian and the polynomial give a common $m^{-5/2}$ before normalization. The angular density at fixed $t$ is already independent of $m$. Radial convergence with first moment follows from $w_\kappa(t)\le5\sqrt t(\kappa^2+t)$ and the same two tail bounds. This law describes the intermediate regime directly. For comparing dimensions, its shape depends on $\kappa\sqrt{b-a}$.

## Selected compact Wilson vacua

In the program's ordered weak Wilson limit, each fixed finite combination at positive physical clocks is a centered gauge-invariant spatial-slice reading. Fix a target $k$, a positive-width window, and the particular coefficients before taking limits. Use the same normalized spatial wave packet for every clock. At nonzero momentum one may combine opposite carriers into a real packet. The finite collection of clocks has a joint compact-to-Gaussian comparison. At fixed packet and fixed spatial mesh send $L=\beta$ to infinity through even sides, then refine the mesh, then increase the packet size. Positive lower clock $a$ supplies Gaussian domination even at equal time. Mixed correlations converge by polarization. Their total masses and Laplace transforms at positive integer physical times determine the limiting measures via $E\mapsto e^{-E}$. The target scalar law has no atom at $k$ or $k+\epsilon$, so window probabilities pass as well. [Compact original-link comparison](../../spatial-flow/wilson.md) · [Momentum packet and transfer representation](../../flow-momentum/spectrum.md) · [Joint-clock comparison](../wilson.md)

Consequently for any prescribed sequence of finite momenta and shrinking widths with $a\Delta_n\to0$, take the explicit filters at target fraction $(1+\eta)/2$. For each index first fix that finite filter, then choose a packet extent, mesh and even $L=\beta$ approximating its window mass within the available margin and its equal-time norm and individual norms to any prescribed relative accuracy. One can enforce $L$ much larger than the packet in lattice cells and make the relative errors tend to zero. The resulting compact vectors achieve fraction at least $\eta$ with $\log\chi\le C/(a\Delta_n)$. This is an existence construction by diagonal selection. It gives no sampling rate or compact lower bound on coefficient cost. The explicit mean constants above concern the free spectrum; transferring unbounded energy moments would require additional uniform integrability for the compact vectors.

# The untwisted packet measures a different physical-time power

Take total momentum zero in the limiting double integral. Then $l=-k$, $\overline{R(-k)}=R(k)$ and every diagonal entry of $D(k)^*\overline{D(-k)}$ equals two. The rank-two projection gives $F(k,-k)=h(k)^2/192$. For each positive integer $n$, the zero-momentum time reading is exactly
$$
 g(n)=\frac1{192}\int_{\mathbb T^3}
       e^{-2n\omega(k)}\frac{A(k)}{4+A(k)}\,dk,
 \qquad n^5g(n)\longrightarrow\frac1{2048\pi^2}.
$$
The normalized $dk$ is $d^3k/(2\pi)^3$. For the adjacent measure in $E=2\omega(k)$, near $k=0$ the radial energy derivative tends to two, $h^2\sim |k|^2/4$, and the sphere area is $4\pi$. The density is $E^4/(49152\pi^2)(1+o(1))$ at zero. Laplace integration gives the factor $4!$ in the time coefficient. The exponential away from the origin controls all other momenta. At the other edge, $E_*-E=2d|k-\pi\mathbf1|^2+O(|k-\pi\mathbf1|^4)$ and $h^2\to3/4$. The adjacent density there is asymptotic to
$$
 \frac{e^{-E_*}}{1024\pi^2(2d)^{3/2}}(E_*-E)^{1/2},
 \qquad d=1/(8\sqrt3).
$$
For this fixed momentum there are three integration variables. The integrated local reading has six, which accounts for its different edge powers. [Local density](edges.md) · [Independent time quadrature](execution.md)

To realize $g(n)$ using finite sums in the actual Wilson vacuum, take $a_M(r)=M^{-3/2}\psi(r/M)$ with a real smooth compact profile of unit $L^2$ norm. Use the same centered slab vector $v_M$ as for the alternating packet, with these untwisted coefficients. Define $C_M(n)=\langle v_M,S^{n-1}v_M\rangle$. For fixed $n$ the limits in order are
$$
 \lim_{M\to\infty}\lim_{\beta,L\to\infty}\beta^4 C_M(n)=g(n).
$$
At fixed $M$ this uses finitely many kernel translates. The squared Fourier weight is an approximate identity of mass tending to one at $Q=0$, by Poisson summation or Plancherel and rapid decay. The continuous function $I_\varphi$ for $\varphi(E)=e^{-(n-1)E}$ therefore yields its value at zero. This construction avoids any need for a finite-volume limit of a single exact momentum projector.

There also exist **common** trajectories for the point and the untwisted packet. For every prescribed $b_j\downarrow0$ one can choose $M_j,\beta_j,L_j\to\infty$, with $b_jM_j\to\infty$ and $L_j/M_j\to\infty$, so that at all fixed physical times $t>0$,
$$
 \begin{aligned}
  \beta_j^4 b_j^{-5} C_{M_j}(\lfloor t/b_j\rfloor)
     &\longrightarrow \frac{1}{2048\pi^2t^5},\\
  \beta_j^4 b_j^{-8} C(\lfloor t/b_j\rfloor,0)
     &\longrightarrow \frac{1}{128\pi^4t^8}.
 \end{aligned}
$$
Enumerate the positive rationals. At stage $j$ use all positive integer lags from the first $j$ rational times at spacing $b_j$. Choose $M_j\ge j/b_j$ so the infinite-cutoff packet values differ from $g(n)$ by at most $b_j^5/j$ on this finite list. Then choose the regulators large enough for all corresponding packet errors to be at most $b_j^5/j$ and all point errors to be at most $b_j^8/j$; impose also $L_j\ge jM_j$ and $\beta_j\ge j$. Take limits on rational times. Both centered same-vector readings are nonincreasing at positive integer lag by transfer positivity, so nearby rational times squeeze each real time. No prescribed growth rate for the bare coupling follows.

At fixed positive time $t_0$ tilt each measure by its own propagation factor and normalize by its own reading. The limiting Laplace transforms are $(t_0/(t_0+s))^5$ and $(t_0/(t_0+s))^8$ for the packet and the point. Rounding the integer times changes the sum of the two lags by at most one step and is absorbed by the same squeeze. Uniqueness and continuity of the Laplace transforms give gamma probability laws with shapes five and eight and common rate $t_0$. The two shapes describe different Wilson probes at the same cutoffs. Positive physical energy intervals carry weight for each, including intervals arbitrarily close to zero. Existence of these selected trajectories supplies no interacting continuum mass-gap construction.

## Normalization of the displaced continuum reading

D4 reported a continuum polarization polynomial for the displaced insertion. It can be checked directly from the lattice form factor. Take $Q=bP$ and $k=bK$ in the *limiting microscopic measure*, with physical energy $e=E/b$ and $q=|P|$. Per unit normalized lattice momentum $dQ$, divide the measure by $b^5$. On bounded physical energy intervals it converges against continuous compactly supported tests to the pushforward under $e=u+v$ of
$$
 \frac{u v(1+\cos^2\theta)}{1536}\frac{d^3K}{(2\pi)^3},
 \qquad u=|K|,\quad v=|P-K|,\quad \theta=\angle(K,P-K).
$$
Indeed the two transverse projections have trace product $1+\cos^2\theta$, the diagonal staggered factor tends to $2I$, and $h(bK)/b\to u/2$. The origin and the coincident soft momentum are null sets. The lattice dispersion bounds $|k|$ by a constant times $\omega(k)$ on the centered Brillouin cube. The compact physical energy test thus confines $K$ to a fixed ball, where the rescaled weights have a uniform integrable bound. With $dQ=b^3dP$ the joint scaling is $b^8$. This is a calculation after the microscopic Wilson limit. Its direct application to a prescribed simultaneous trajectory requires separate error estimates.

For $q>0$, integrate in polar coordinates about $P$. The volume factor becomes $uv\,du\,dv/(4\pi^2 q)$, with $|u-v|\le q\le u+v$. At fixed $e>q$, put $s=2u-e$, so $-q<s<q$. The angular polynomial times $(uv)^2$ is
$$
 \frac{(e^2-s^2)^2+(2q^2-e^2-s^2)^2}{16}.
$$
The uniform averages of $s^2,s^4$ are $q^2/3,q^4/5$. The density relative to $de\,d^3P/(2\pi)^3$ is therefore
$$
 \frac{(e^2-q^2)^2+8q^4/15}{49152\pi^2}\,\mathbf1_{e>q}.
$$
At $q=0$ this agrees with the independently computed coefficient $1/(49152\pi^2)$. Integrating over the momentum ball of radius $e$ gives $e^7/(128\pi^4\,7!)$, using $\int_0^1 t^2[(1-t^2)^2+8t^4/15]dt=16/105$. These two normalizations independently check D4's stated shape and A4's point coefficient. [D4's reported expression](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7096665906) · [Lean identities and shell quadrature](execution.md)

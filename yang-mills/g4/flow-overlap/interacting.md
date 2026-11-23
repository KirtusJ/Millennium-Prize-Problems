# A finite-coupling lower bound for the unpredictable part of the flowed plaquette

Let $G=F_p\circ\Phi_u$ on time slice zero, with the conventions of the [Haar proof](README.md). Set

$$H_\beta=\frac{e^{-32u}}{6(4+6\beta)}.$$

If $(4/3)T_R\le H_\beta/2$, then for every square-integrable predictor $Y$ measurable outside the spatial edges of $Q_R$,

$$\mathbb E_\beta(G-Y)^2\ \ge\ \frac{3H_\beta^2}{16(1+4\beta)N},\quad N=|Q_R|.$$

The exterior contains all links at all other times. This bounds the **mean** prediction error in the lattice law. Its proof uses spatial symmetry after averaging. The result is uniform in spatial volume at fixed $u,\beta$.

## The local integration-by-parts witness

Differentiate only the spatial links in the selected slice. On product Haar tilted by $e^{-\beta S_4}$, the integration-by-parts operator is $\mathcal L=\Delta-\beta\langle\nabla S_4,\nabla\,\cdot\,\rangle$. For each spatial face put

$$W_q=-\mathcal L F_q/12=F_q-1+(\beta/12)\langle\nabla S_4,\nabla F_q\rangle.$$

Then $12\mathbb E_\beta[BW_q]=\mathbb E_\beta\langle\nabla B,\nabla F_q\rangle$ for every smooth test $B$. Integrating just its four links shows $W_q$ has conditional mean zero given their exterior. This remains true with arbitrary exterior predictors in $L^2$ by conditioning. The witness itself uses temporal staples. The measure convention is $e^{-\beta S_4}$ throughout. [Lüscher, weighted group integration by parts, Eqs. (4.6)–(4.8)](https://arxiv.org/pdf/0907.5491)

Autonomy of the flow and spatial symmetry give $12\sum_q\mathbb E_\beta[GW_q]=\mathbb E_\beta\|\nabla S(\Phi_u)\|^2/N_p$, exactly as for the unweighted identity with the new witness. The Hessian estimate still supplies $e^{-32u}$ times the initial force energy. To bound that initial energy, fix a spatial link $e$, and fix all links except a spatial link $f\ne e$ belonging to exactly one of its four adjacent spatial plaquettes. Such an $f$ exists on each of the tori under consideration. In the left-trivialized force at $e$, only one oriented face varies. The force has the form $C+\operatorname{Im}(OQ)$ with $Q=U_f$ and $O$ orthogonal on $\mathbb R^4$ (left and right unit-quaternion factors and possibly inversion). The conditional law of $Q$ has density proportional to $\exp(\kappa n\cdot Q)$ against Haar for some unit $n$ and $0\le\kappa\le6\beta$. Each of the at most six incident spacetime faces is linear in the four coordinates. [Creutz, SU(2) one-link heat bath](https://doi.org/10.1103/PhysRevD.21.2308)

Write $x=n\cdot Q$ and $b(\kappa)=\mathbb E_\kappa x$. For $\kappa>0$, sphere integration by parts gives $3b=\kappa\mathbb E_\kappa(1-x^2)$ using $\Delta x=-3x$ and $|\nabla x|^2=1-x^2$. Each transverse component therefore has variance $b/\kappa$. The imaginary three-plane meets $(On)^\perp$ in at least two dimensions. In two orthogonal directions in this intersection the centered components of $OQ$ have that transverse variance, even for a tilted pole pointing wholly into the imaginary plane. Adding $C$ cannot reduce the uncentered second moment below this sum of variances.

For an explicit lower bound, differentiation under the integral gives $b'=\operatorname{Var}(x)=1-b^2-3b/\kappa$. The function $g=\kappa/(4+\kappa)$ has residual $1-g^2-3g/\kappa-g'=5\kappa/(4+\kappa)^2\ge0$. The difference $b-g$ satisfies a first-order linear equation with this right-hand side and integrating factor $\kappa^3\exp(\int_0^\kappa(b+g))$. Its product with $b-g$ tends to zero at the origin. Thus $b/\kappa\ge1/(4+\kappa)$, also by continuity at zero where the transverse variance is $1/4$. Conditional on all except $f$ we have

$$\mathbb E_\beta |\nabla_e S|^2\ge 2/(4+6\beta).$$

There are $N_p$ links, giving the claimed total overlap $\sum_q\mathbb E_\beta GW_q\ge H_\beta$. The integration-by-parts identity for each $q$ and the same deterministic differential influence estimate as for Haar imply that the omitted absolute sum is at most $(4/3)T_R$. The overlap with $W_R=\sum_{q\in Q_R}W_q$ is therefore at least $H_\beta/2$.

## Size of the witness

Put $S_R=\sum_{q\in Q_R}F_q$. Let $d_e$ count its faces incident to $e$. Then $d_e\le4$, $\sum_e d_e=4N$ and $\sum_e d_e^2\le16N$. We have $|\nabla_e S_R|\le d_e$, $|\nabla_e S_4|\le6$, and $\|\operatorname{Hess} S_4\|\le24$ as an operator on the selected slice links. This last bound counts at most six faces per link and at most four unit Hessian blocks per face. The Hessian of $S_R$ has block row sums at most $4d_e$. Differentiating the scalar product in $W_R$ gives

$$
\nabla W_R=\nabla S_R+(\beta/12)
(\operatorname{Hess} S_4\,\nabla S_R+\operatorname{Hess} S_R\,\nabla S_4).
$$

The first Hessian term has norm at most $96\sqrt N$. For the second, each link component has norm at most $24d_e$, again giving $96\sqrt N$. Hence $\|\nabla W_R\|\le(4+16\beta)\sqrt N$. Apply integration by parts with $B=W_R$ to obtain $\mathbb E W_R^2\le(4/3)(1+4\beta)N$. Since $\mathbb E YW_R=0$, Cauchy–Schwarz applied to $(G-Y)W_R$ proves the prediction bound. The temporal links in $W_R$ pose no problem for this centered-conditional argument. The transfer representation below uses the original one-slice reading $G$.

## A weak-coupling bound in the scaled normalization

Write $v$ for the largest expectation of any spatial or temporal plaquette deficit touching the slice. Suppose $v\le K/(1+\beta)$ with $K\ge1$. Then at fixed $u$ the radius can be chosen **independently of $\beta$**. A spatially symmetric law has $\mathbb E F_p(\Phi_u)\le v$ because $S$ decreases pointwise and all spatial faces have the same flowed expectation. The incident gradient length of a deficit is $\sqrt{F_q(2-F_q)}\le\sqrt{2F_q}$. The derivative influence estimate for $F_p\circ\Phi_u$ therefore retains a factor $\sqrt{2F_p(\Phi_u)}$ at the output. After multiplication by $\sqrt{2F_q}$ and Cauchy–Schwarz in probability, the omitted absolute overlap is at most $(8/3)vT_R$. Choosing $T_R\le e^{-32u}/(192K)$ suffices for a loss of at most $H_\beta/2$.

In mean-square norm, the link gradients of $S_R$ and $S_4$ obey $\|\nabla_e S_R\|_{L^2}\le d_e\sqrt{2v}$ and $\|\nabla_e S_4\|_{L^2}\le6\sqrt{2v}$. Use the same deterministic Hessian block bounds, summing linkwise $L^2$ norms by Minkowski before summing their squares. This gives $\|\nabla W_R\|_{L^2}\le(4+16\beta)\sqrt{2vN}$ and $\mathbb E W_R^2\le(8/3)(1+4\beta)vN$. Consequently

$$
(1+\beta)^2\mathbb E(G-Y)^2\ge
\frac{3(1+\beta)^2 H_\beta^2}{32(1+4\beta)vN}
\ge\frac{e^{-64u}}{55296\,K N}=:D .
$$

The last comparison uses $1+4\beta\le4(1+\beta)$ and $4+6\beta\le6(1+\beta)$. Under the second-moment input $\sup_q\|(1+\beta)F_q\|_2\le K_2$, the scaled flowed reading has second moment at most $M=e^{64u}K_2^2$. Indeed put $b_q=\sqrt{F_q}=|U_q-I|/\sqrt2$. The upper right time derivative is bounded by $\sum_{e\in q}\sum_{q'\ni e} b_{q'}$, also when $b_q=0$, by the link speed and triangle inequality. The face incidence matrix has row sums 16. Iterating the integral bound and using Minkowski in $L^4$ gives $\|b_q(u)\|_4\le e^{16u}\sup_{q'}\|b_{q'}(0)\|_4$. Squaring gives the asserted $L^2$ bound for the deficit.

C4's written exponential-moment estimate supplies $K,K_2$ for all sufficiently large $\beta$ in the **infinite-time Wilson vacuum**, uniformly over the spatial sides here, for all orientations. In particular a bound on $\mathbb E\exp(\beta F_q/8)$ bounds the first two moments of $\beta F_q$ by expanding the exponential. It is this vacuum version of the input that enters the spectral consequence. [C4's estimate, reflected copying and order of limits](../../central-quotients/tangent-curvature/moments.md)

Let $C(k)$ denote the connected correlation of the **scaled** reading. The vacuum slice process is stationary and reversible with transfer $T$ on the gauge-invariant slice space. The best predictor from slice $-k$ has squared centered norm $C(2k)$, since it is $T^k$ applied to the centered reading. That slice lies in the admissible exterior for $k\ge1$. Hence $C(0)-C(2k)\ge D$. In lattice energy $e=-\log\lambda$, $C(0)-C(2)=\int(1-e^{-2e})\,d\nu$. Set $d=-\log(1-D/(2M))/2$; the established bounds imply $0<D\le M$. Below $d$ the integrand is at most $D/(2M)$, so $\nu([d,\infty])\ge D/2$. This is an ultraviolet statement upon refinement, since physical energy is $e/a$. It gives neither an upper endpoint for that weight nor an exclusion of low energies. The bounds deteriorate when $u=s/a^2$ grows at fixed physical diffusion time. [Vacuum slice process](../../central-quotients/magnetic-smearing/connector/fluctuations.md) · [Wilson transfer construction](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf)

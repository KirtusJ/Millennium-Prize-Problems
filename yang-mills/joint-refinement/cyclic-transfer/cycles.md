# Comparing coarse transfer norms with cyclic endpoint integrals

Fix a periodic spatial regulator and a positive physical lag $t$ that is an integer number of lattice steps on both lattices. Work in the time vacuum. On the fine lattice observe the full straight two-link coarse orbit at the two endpoints. On the coarse lattice observe its full physical slice orbit. If center neutrality is imposed, quotient also by the independent spatial center transformations at each observed endpoint. This realizes the invariant test space. These observations have stationary one-endpoint laws $\nu_f,\nu_c$ and symmetric two-endpoint laws. The Hilbert spaces may have different measures. On each, the stationary transition at this one lag is a positive contraction: on the fine side it is the compression $A_f=U^* S_t U$ by the isometric observation pullback, and on the coarse side $A_c=S^{\rm coarse}_t$ on the stated sector. The centered norms are denoted by $\lambda_f,\lambda_c$. The additive error required in [the refinement criterion](../rare-coarse-fields/inheritance.md) is exactly $(\lambda_f-\lambda_c)_+$. [Wilson transfer construction](https://doi.org/10.1007/BF01614090)

Take reference Haar pushed forward to the respective orbit spaces, write it as $dh$, and write $v(x)$ and $j(x,y)$ for the marginal and joint densities with respect to this reference and its square. At finite regulator, positive vacuum boundary factors on a slab and bounded Wilson weights give positive upper and lower density bounds. Integration of the unseen coordinates preserves such bounds, also on the orbit quotient. Thus the endpoint kernel $k(x,y)=j(x,y)/(v(x)v(y))$ relative to $\nu$ is bounded and Hilbert–Schmidt. For each integer $p\ge2$ the following trace is finite:
$$
M(p)=\operatorname{Tr}(A^p)-1
=\int\prod_{i=1}^{p}\frac{j(x_i,x_{i+1})}{v(x_i)}\,\prod_i dh(x_i)-1,
\qquad x_{p+1}=x_1 .
$$
Compose the integral kernels relative to $\nu$, using the Hilbert–Schmidt inner product for the last two factors; each endpoint marginal occurs once in the remaining denominator. The constant mode contributes exactly one. The two lattices each use their own marginal. The formula also holds for the sweep's positive round-trip kernel. [Qin, Hobert and Khare, power-sum bounds and integral representations](https://arxiv.org/abs/1704.00850)

On each centered space $M(p)=\sum_j\lambda_j^p$ counting multiplicity. Hence
$$L(p)=M(p+1)/M(p)\ \le\ \lambda\ \le\ U(p)=\min(1,M(p)^{1/p}).$$
Use zero for both bounds if $M(p)=0$. Both tend to the centered norm at fixed regulator. In particular
$$\boxed{\quad\varepsilon\le [U_f(p)-L_c(q)]_+,\qquad
\varepsilon\ge [L_f(p)-U_c(q)]_+ .\quad}$$
Any certified centered trial Rayleigh quotient on the coarse side can replace $L_c$ in the upper bound. A finite partition or finite list of probes on the fine side only gives a lower bound on $\lambda_f$. In particular the [four-bin Wilson experiment](measurements.md) cannot furnish $U_f$ for the full orbit. These inequalities transfer a scalar norm and require no identification of the two vacuum measures. They give a four-dimensional comparison criterion, with no numerical claim about the full Wilson error until quantitative full-orbit moment bounds are available.

**What goes wrong with cheaper replacements.** Repeating the compressed kernel takes a new conditional fine representative at each join. Using the fine transfer at a single lag $2t$ instead gives
$$
\operatorname{Tr}(U^*S_{2t}U)-\operatorname{Tr}[(U^*S_tU)^2]
=\|(I-UU^*)S_tU\|_{\rm HS}^2 .
$$
This follows by inserting $I=UU^*+(I-UU^*)$ between the two factors. At finite regulator the terms are finite. For example two independent stationary binary spins of nonzero mean $b$, each with centered multiplier $a\in(0,1)$, observed through their product, have centered compression $w a+(1-w)a^2$ with $w=2b^2/(1+b^2)$. The unbroken lag has centered multiplier $w a^2+(1-w)a^4$. Their trace difference is $w(1-w)(a-a^2)^2>0$. Omitting the marginal factors also fails even for independent endpoints: a nonuniform stationary vector produces a spurious contribution $(\sum v_i^2)^p$ on counting measure.

An arbitrarily small two-endpoint total-variation discrepancy can hide a slow mode. With stationary probabilities $(1-h,h)$ take $A=\rho I+(1-\rho)\mathbf1\otimes\nu$. Its joint law is at distance $2\rho h(1-h)$ from independent endpoints, while its centered norm is $\rho$ and $M(p)=\rho^p$. Thus a fit concentrated on typical bins cannot bound the missing spectral contribution. The [controls](checks.py) compute all three failures. At fixed power there is also a multiplicity cost: for a reset on $D$ states with centered multiplier $\rho$, $M(p)=(D-1)\rho^p$. A uniform moment-order bound requires spectral-tail control. A different [finite-partition upper bound](partition.md) controls the unresolved modes using the actual Wilson action. A uniform positive limiting deficit still requires the weighted sum of the cross-lattice and exceptional-return errors to stay below the initial deficit.

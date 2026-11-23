# A lower bound in the isotropic Wilson measure

Fix periodic space of side $N\ge 2$, isotropic spacing $a=\ell/N$ and finite bare $\beta>0$. Every temporal and spatial plaquette has the Wilson coupling. Write $T$ for the one-step transfer, $\lambda_0$ for its vacuum eigenvalue, and $M_N$ for the gap above the vacuum in the gauge-invariant sector even under all three electric-center flips. Write $z(b)=\int_{SU(2)}\exp(b\,\mathrm{Tr}(g)/2)\,dg=2I_1(b)/b$ for normalized Haar measure. Then

$$
 U_N=z(6\beta)^{N^3/2},\qquad
 \ell M_N\ \ge -N\log(1-U_N^{-1})\ \ge N/U_N .
$$

The inequality holds for the full physical vacuum complement, so it also holds after imposing center neutrality. The transfer is positive, compact and self-adjoint with a simple, strictly positive vacuum. These finite-lattice facts follow from the Wilson transfer construction and the continuous, strictly positive kernel. [Lüscher, 1977](https://doi.org/10.1007/BF01614090)

### Gauge integration and row comparison

Let $x,y$ be spatial link fields. The temporal kernel after projecting vertex gauges can be written, up to an overall constant, as
$$
 k(x,y)=\int\prod_{e=(v,w)} \exp\!\left(\beta\,{\tfrac12}\mathrm{Tr}(x_e h_w y_e^{-1} h_v^{-1})\right)\prod_v dh_v.
$$
Every edge has two distinct endpoints. Its twisted SU(2) element is Haar when the endpoint frames are integrated, even for repeated edges between a pair of sites. Its trace therefore has mean zero. Jensen gives $k\ge1$. Apply product-space Hölder with exponent six to every link factor. Each vertex variable enters six factors, so the reciprocal exponents sum to one at every vertex. The sixth moment of each factor is $z(6\beta)$. With $3N^3$ edges this gives $k\le U_N$, including odd $N$. Equivalently, integrate one frame at a time, apply six-factor Hölder, and carry each edge's conditional sixth moment to its other endpoint. A one-site graph violates the distinct-endpoint hypothesis. Setting every $x_e=1$ and every $y_e=-1$ there gives $k=e^{-3\beta}$. [Finner, generalized Hölder inequality](https://doi.org/10.1214/aop/1176989534)

The spatial plaquettes contribute positive endpoint multipliers $w(x)w(y)$. Let $\phi>0$ be the leading eigenfunction of $T$. After dividing by $\lambda_0$ and conjugating by $\phi$, each row of the Markov kernel is
$$
 P(x,dy)=\frac{k(x,y)w(y)\phi(y)\,dy}{\int k(x,z)w(z)\phi(z)\,dz}
 \ \ge\ U_N^{-1}\frac{w(y)\phi(y)\,dy}{\int w(z)\phi(z)\,dz}.
$$
Thus $P$ is a convex combination of a common row of mass $U_N^{-1}$ and a Markov kernel of mass $1-U_N^{-1}$. Applied to a bounded real function, the oscillation contracts by at least this common-row fraction, i.e. $\operatorname{osc}(Pf)\le(1-U_N^{-1})\operatorname{osc}(f)$. Each nonzero eigenfunction of the continuous kernel is continuous; dividing by $\phi$ preserves boundedness on the compact configuration space. A nonconstant eigenfunction now gives $|\lambda|/\lambda_0\le 1-U_N^{-1}$. Compactness exhausts the nonzero spectrum. The physical clock multiplies the one-step log bound by $N$.

### Loss under refinement

| $N$ | Tuned $\beta$ | $\log_{10}(N/U_N)$ |
| ---: | ---: | ---: |
| 5 | 3.196581051 | −392.96 |
| 6 | 3.276133577 | −700.14 |
| 7 | 3.342724170 | −1139.73 |
| 8 | 3.399810242 | −1736.94 |
| 10 | 3.493705679 | −3506.80 |

For any continuation eventually bounded below by $\beta_*>0$, $\log z(6\beta_*)>0$ and both lower expressions tend to zero. This proves loss of the estimate. The actual eigenvalue could stay uniformly separated in physical units. As an implementation control, direct orbit enumeration on a $2^2$ spatial $\mathbb Z_2$ gauge lattice with its spatial Wilson factor includes two independent center projections. At $\beta=0.6$ the neutral ratio is 0.10521939 and the corresponding degree-four contraction bound is 0.96761623. This smaller group checks the projection and the direction of the comparison. [SU(2) values](electric.py) · [Finite orbit control](transfer-control.py)

### What would transport a physical lower bound

Fix physical time $\ell$. Set $S_N=(T_N/\lambda_{0,N})^N$ on the physical, center-neutral vacuum complement. To compare two cutoffs, assume an isometric identification $J$ of the coarse complement into the fine complement. Write $P=JJ^*$ and $Q=1-P$. Suppose on this fine space
$$
 PS_{\rm fine}P\preceq aP,\qquad QS_{\rm fine}Q\preceq bQ,\qquad
 \|PS_{\rm fine}Q\|\le\eta .
$$
For $x=\|Pv\|$, $y=\|Qv\|$ the quadratic form is bounded above by $ax^2+2\eta xy+by^2$. A target $q<1$ works when $q>a$, $q\ge b$ and $\eta^2\le(q-a)(q-b)$. Completing the square gives the bound. At $a=q$ one needs $\eta=0$ and $b\le q$. The simpler conditions $a+\eta,b+\eta\le q$ also suffice. Uniform certificates yield $\ell M_N\ge-\log q$. A compressed coarse-transfer comparison can bound $a$ if it includes a quantitative error and the correct vacuum subtraction. Exact agreement on inherited states alone leaves $b$ unrestricted. The electric control below attains this failure even with $\eta=0$. In the isotropic theory the vacuum changes with the cutoff and a spatial blocking can generate extra interactions. The required isometries and estimates across the infinite tail remain open. [Lean algebra](Refinement.lean) · [Refinement counterexample](electric.md) · [G4’s earlier transfer comparisons](../blocking/README.md)

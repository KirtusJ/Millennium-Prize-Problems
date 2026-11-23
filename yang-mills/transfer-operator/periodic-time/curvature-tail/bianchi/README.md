# The first nonzero Bianchi defect of one Wilson cube

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Z4's L4(b) proves that the signed sum of six scaled log plaquettes tends to zero. With the six connectors and the order in Z4's exact cube word, its first rescaling has a nonzero limit. In the Gaussian curvature limit identified by L4, D and the reflection argument, any one colour coordinate of that limit is the sum of two independent, centred Laplace variables with strictly positive scales. Thus the root-mean-square size of the original signed sum is exactly of order $\beta^{-1/2}$. This measures the error of *additive* closure. The ordered multiplicative Bianchi identity holds exactly at every coupling. [Z4, Proposition L4(b)](../../../../z4/attempt/paper/sec_proof.tex) · [Gaussian specification and removal of the background](../review.md)

Borisenko, Voloshin and Faber use explicitly connected non-Abelian cube identities for the low-temperature expansion in three-dimensional lattice gauge models. Their analysis motivates retaining the connectors here. The four-dimensional probability law below uses the program's tangent covariance and Z4's particular word. [Plaquette representation for 3D lattice gauge models, part I](https://arxiv.org/abs/hep-lat/0508003)

## Quadratic term and a uniform error bound

Fix one elementary three-cube inside the four-dimensional lattice and put the root at its lower corner. Write the following faces in order: lower 23, upper 13, lower 12, upper 23, lower 13, upper 12. Use signs $-,-,-,+,+,+$. Transport each upper face back along the single edge from the root to its base. Let $Y_i^\beta$ be its signed, transported principal log vector multiplied by $\sqrt\beta$ (with the same definition for lower faces). Use $\exp(i\sigma\cdot v)$ and the usual orientation of the Pauli matrices. Then

$$
\prod_{i=1}^6\exp(i\epsilon\sigma\cdot Y_i^\beta)=I,
\qquad \epsilon=\beta^{-1/2}.
$$

Define $D_\beta=\sum_iY_i^\beta$, $Q(Y)=\sum_{i<j}Y_i\times Y_j$ and $S=\sum_i|Y_i^\beta|$. Deterministically,

$$
\left|\sqrt\beta D_\beta-Q(Y^\beta)\right|\le \frac{S^3}{6\sqrt\beta}.
$$

To see the sign, expand the product with variable $s$ at zero and evaluate at $s=\epsilon$. Its Pauli-vector part, the coefficient of $i\sigma$, is $s\sum_iY_i-s^2\sum_{i<j}Y_i\times Y_j$ through order two. This follows from $(\sigma\cdot x)(\sigma\cdot y)=(x\cdot y)I+i\sigma\cdot(x\times y)$. The third derivative of the product has operator norm at most $S^3$ at every real $s$ by the product rule and unitarity. Taking the vector part contracts the norm on real quaternion matrices. Taylor's integral remainder gives the displayed inequality, including large face angles. The zero-probability choice of logarithm at the central cut point can equally be handled by choosing any exponent giving the corresponding factor.

The one-face action tail bounds all fixed moments of $S$ uniformly. The error above is therefore $O(\beta^{-1/2})$ in every fixed finite $L^p$, $p\ge1$. At leading order the fixed six-face vector converges to the signed Gaussian tangent vector $Y$. The continuous mapping theorem and the error bound give $\sqrt\beta D_\beta\Rightarrow Q(Y)$ jointly with $Y^\beta\Rightarrow Y$, with convergence of all polynomial moments by uniform integrability. This argument requires no rate of convergence for $Y^\beta$ itself. The path-independence estimate of L4(a) is first-order only. Replacing the six connectors independently could change the rescaled defect.

## Exact one-colour law

Let $C$ be the $6\times6$ one-colour tangent covariance of the ordered, signed faces, the indicated restriction of the projection onto the closure of compactly supported curls. It is positive definite on $H=\{y:\sum_i y_i=0\}$ and has kernel spanned by the all-ones vector. Indeed, the curl map on the twelve links of a cube has kernel equal to the seven-dimensional vertex gradients (the boundary of the cube is simply connected). Its image on the six signed faces therefore has dimension five and equals $H$. Any assignment of the twelve link values extends by zero to a finitely supported lattice one-form. Thus a test on the six faces is orthogonal to all compact curls precisely when it annihilates $H$, which proves the covariance claim.

Let $J_{ij}=1$ for $i<j$, $J_{ij}=-1$ for $i>j$, with zero diagonal. Then $Q_3=X^T J Z$, where $X$ and $Z$ are the first and second colour columns, independent $N(0,C)$. In the basis $e_i-e_6$, $1\le i\le5$, the restricted skew form has entries $J_{ij}$ again. Its leading four-dimensional Pfaffian is $1-1+1=1$. Since a skew form on a five-dimensional space has rank at most four, $C^{1/2}JC^{1/2}$ has exactly two positive singular-value pairs, with scales $s_1,s_2$ counting one per pair.

Conditioning on one of the two standard Gaussian factors in the whitened bilinear form and integrating over the other gives
$$
\mathbb E e^{it Q_3}=\frac{1}{(1+s_1^2t^2)(1+s_2^2t^2)} .
$$
These are the characteristic functions of independent centred Laplace variables in convolution. Colour rotation gives the same marginal in any unit colour direction. In particular $\lim_{\beta\to\infty}\beta\mathbb E[D_{\beta,3}^2]=2(s_1^2+s_2^2)>0$ and the fourth cumulant of the limiting coordinate is $12(s_1^4+s_2^4)>0$. The result is conditional on the program's tangent identification. It concerns one fixed cube and has no continuum gap implication.

## Numerical and native checks

A deterministic SU(2) link sample checks the exact product and the sign of the quadratic remainder. Halving the link amplitude from 0.01 to 0.005 to 0.0025 gives residual norms 0.6573, 0.3261 and 0.1624. Independently, the checker builds the covariance on periodic four-tori using the Fourier curl multiplier divided by the square root of the scalar Laplacian symbol, with the zero mode omitted. The multiplier is bounded and continuous away from that single point, so the sums tend to the infinite-lattice integrals. The table gives finite-mesh values without a certified quadrature error. [Python checker](check.py)

| Torus side | Larger scale | Smaller scale | One-colour variance |
|---:|---:|---:|---:|
| 8 | 0.98492468 | 0.37335163 | 2.21893615 |
| 16 | 0.98529388 | 0.37336525 | 2.22041127 |
| 32 | 0.98531832 | 0.37336542 | 2.22050784 |
| 48 | 0.98531964 | 0.37336542 | 2.22051305 |

The PCP OS parent freely reduced the cube word in twelve distinct edge generators. Its child checked the restricted skew form and its nonzero minor. The grandchild used Gaussian quadrature to check the variance and fourth moment of a single unit-scale block. The host relayed each child request to a new boot of the pinned kernel. All three guests exited zero with 47 recorded events each. [Guest source](worker.c) · [Expected output](checks.txt) · [Replay driver](../../../../observable-normalization/transfer-increments/replay-guests.py)

| Guest | Executable SHA-256 | Register head |
|---|---|---|
| Parent | 044655071c06b2b5e56813908d91970e295dded3c9bd735152e4e02b472c449a | 10ee51ce733208e2af56283643df4e8e32e5b2c915247df6cbf2ee16f9b68625 |
| Child | 66c74638359aae862f81e413828788db42a12807dda0f573e19b588471b65907 | 1649ff55de8508bac0d2cd00d69302a4df67b35ddbb71e738c27b7bad7661893 |
| Grandchild | 7b6025f0cfe20a2724e749cb2708e4fe22628e2182b1fef484d6cb36879f57d1 | 5771d9edcb4a56aea580c4d9da82d365d165362b0245c15c8710bd23921a6312 |

```sh
python check.py
python ../../../../observable-normalization/transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof checks.txt
```

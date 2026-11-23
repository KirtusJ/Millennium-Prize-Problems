# A volume-independent magnetic derivative on the whole straight coarse space

Director A4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

At the electric SU(2) Wilson regulator, the first magnetic derivative from **any** straight coarse orbit reading to fine detail has a volume-independent upper bound. At fixed positive electric time, after rescaling the magnetic coupling, the bound decays as $\sqrt\ell\,e^{-4\ell\tau}$ with mesh spacing $\ell$. G4’s family of bends of a single coarse square attains this order. The result controls the derivative at zero spatial coupling. A remainder uniform in the volume and a contraction at nonzero isotropic coupling are still needed for the gap construction. [G4’s transfer and vacuum derivative](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/660fe73/yang-mills/g4/full-attempt/blocking/README.md) · [Optimal response for a single square](../bends/README.md)

Use an even cubic spatial torus, $\ell\mid L$, $\ell\ge2$, $L/\ell\ge4$, temporal coupling $g>0$, integer lag $n\ge1$. Let $K_b$ be the stationary physical transfer at magnetic coupling $b$ and $P_b$ the conditional expectation onto the orbit algebra of straight coarse segments in its vacuum law $\pi_b$. Write $K=K_0$, $q=I_2(g)/I_1(g)$ and $\lambda=q^4$. Define $J_\ell$ as the supremum over nonzero centered coarse $F$ and fine $h$ with $P_0h=0$ of the absolute derivative at zero of

$$\langle h-P_bh,K_b^n(F-\pi_bF)\rangle_{\pi_b},$$

divided by $\langle F,(I-K^n)F\rangle_0^{1/2}\langle h,(I-K^n)h\rangle_0^{1/2}$. Equivalently take bounded spin-network sums first and extend the derivative form by density. The finite-volume estimate is

$$
J_\ell\le \frac{4\sqrt\ell}{q^{-4\ell n}-1}
\left(\frac1{1-q^4}+n\right). \tag{1}
$$

No upper cutoff on spin, loop perimeter, spatial volume or the number of coarse insertions enters (1).

## Recovering orthogonality after inserting a magnetic face

A coarse spin network pulled back to straight fine links has the same irreducible representation on each link of a given segment. Group the coarse space by the full assignment of edge representations and allow all admissible vertex tensors in each group. Electric transfer acts as one scalar $r$ on each group. If $E$ fine links carry a nontrivial label, then $r\le q^E$. Every nonconstant gauge-invariant group has $E\ge4\ell$. Its occupied coarse graph has no degree-one vertex and contains a cycle. The shortest cycle has at least four edges under the period restriction, which includes winding cycles. [Physical electric basis](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/660fe73/yang-mills/g4/full-attempt/electric.md) · [Baez, *Spin Network States in Gauge Theory*](https://arxiv.org/abs/gr-qc/9411007)

Let $A_p$ be multiplication by half the fundamental trace around a unit spatial face. Its operator norm is at most one. For $F$ in a fixed label group, the contribution of $p$ to $(K_b^n)'_0F$ is $D_n(K) A_p F$, where

$$
D_n(t)=\frac{t-\lambda r}{1-\lambda}
\sum_{j=0}^{n-1}t^jr^{n-1-j}.
$$

Indeed $K'_0F=\sum_p(KA_p F-\lambda A_p K F)/(1-\lambda)$. The coarse algebra reduces $K$. Subtract $K^nF$ from the second slot of the differentiated pairing at every $b$, as the moving first slot annihilates every coarse reading. The remaining second slot vanishes at zero, so derivatives of the moving measure and projection contribute zero. This works for superpositions of distinct electric eigenvalues.

Three geometrical facts give the operator bound.

1. If the face has no occupied edge, all four magnetic edges are new fundamentals and every nonzero component of $A_pF$ has eigenvalue $\lambda r$. It cancels. At most $4E$ faces remain since each occupied spatial edge has four incident faces.
2. A fine square contains at most one coarse-skeleton edge of each of its two directions. The two parallel candidates differ by one transverse lattice unit and cannot both lie on the mesh. At most two occupied links can lose a representation. At least two links outside the skeleton acquire fundamental representations. Thus every output component still has at least $E$ occupied fine links and eigenvalue $0\le t\le q^E$.
3. Distinct faces have orthogonal output spaces. On links outside the coarse skeleton a center flip has sign minus precisely on the outside edges of the inserted face. These edges include one in each of two perpendicular directions and uniquely determine the face, including across a periodic seam. For a fixed face, different input assignments also have orthogonal outputs. At least one fine edge in **every** coarse segment is untouched, since a face uses at most one edge of that segment and $\ell\ge2$. Its representation recovers the original coarse label. Both distinguishing properties are preserved by every function of $K$, including the defect normalization. Tensors within a single assignment need no orthogonality after multiplication because $\|A_p\|\le1$.

In particular the derivative takes values in fine detail. On an even straight mesh its image is already orthogonal to the entire spacing-two algebra. The input only uses that finer skeleton and each inserted face has a private edge outside it.

## Bounding the derivative in the two defect norms

Put $x=q^E$ for the input group. Since $r,t\in[0,x]$, telescoping gives

$$
D_n(t)=\frac{t^n-r^n}{1-\lambda}
+r\sum_{j=0}^{n-1}t^jr^{n-1-j},
\qquad |D_n(t)|\le x^n\left(\frac1{1-\lambda}+n\right).
$$

This includes $t=r$. Both defects on these inputs and outputs are at least $1-x^n$. On multiplying the derivative on each side by the inverse square root of the corresponding defect, each face contribution therefore has norm at most $(1/(1-\lambda)+n)x^n/(1-x^n)$. Sum the squared norms over the at most $4E$ orthogonal faces, then use orthogonality across input assignments. This bounds $J_\ell$ by the supremum of $2\sqrt E(1/(1-\lambda)+n)/(q^{-En}-1)$ over $E\ge4\ell$. For $s=-n\log q>0$, the function $\sqrt E/(e^{sE}-1)$ decreases since $1-e^{-sE}<sE$. This proves (1).

## Electric time and spatial scale

Let $g\to\infty$, $-n\log q\to\tau>0$, with fixed mesh and any sequence of allowed volumes. Write $\delta=1-q$ and $k=4\ell$. The derivative with respect to $\eta$ in $b=\delta\eta$ is $\delta$ times the bare derivative. Equation (1) supplies the right-hand bound and G4’s coherent positive-side singlet supplies the left-hand bound:

$$
\frac{\sqrt{k}\,e^{-k\tau}(1-e^{-2\tau})}
{16\sqrt{(1-e^{-k\tau})(1-e^{-(k+2)\tau})}}
\ \le\ \liminf \delta J_\ell
\ \le\ \limsup \delta J_\ell
\ \le\ \frac{2\sqrt{k}(\tau+1/4)}{e^{k\tau}-1}.
$$

Here $\delta/(1-q^4)\to1/4$ and $n\delta\to\tau$. At large mesh spacing these bounds have the same exponential and square-root dependence; their constants need not coincide. The upper estimates are summable over dyadic meshes, uniformly once the electric time lies in a compact subset of $(0,\infty)$ and $g$ is large. The time here is calibrated by the electric one-link multiplier. Controlling all first derivatives at this point leaves the size of higher orders in spatial coupling and the independently calibrated physical clock open. [C4’s electric-time lower bound](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/15#issuecomment-7106683964)

## Exact sign symmetry for coarse histories

For even $\ell$, the joint law of straight coarse readings at **any finite list of times** is identical at $b$ and $-b$ in the finite-volume vacuum chain. Multiply the link at $x$ along axis $i$ by the central sign $(-I)^{\sum_{j<i}x_j}$, using the same transformation at every time. Every spatial face changes trace sign. Electric convolution commutes with the transformation, so the symmetrized transfers and their unique positive vacua are conjugate. The normalized stationary chains are consequently conjugate too. Along a straight segment the sign is constant, and its $\ell$th power is one. The conjugacy therefore fixes each recorded coarse reading pathwise. In particular the coarse pair law has vanishing odd derivatives wherever analytic. The mixed coarse-to-fine derivative above is visible because its fine test can detect an individual sign. [B4’s transfer conjugacy and prior work on sign reversal](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/7293650/yang-mills/transfer-operator/blocked-time/magnetic-curvature/spatial-momentum.md) · [Lean and finite controls](checks.md)

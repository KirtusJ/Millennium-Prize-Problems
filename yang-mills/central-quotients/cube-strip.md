# Shared edge signs on a strip of cubes

Director C4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For the fundamental SU(2) Wilson regulator on the faces of an open $n\times1\times1$ strip, **no global normalization makes independent face-sign averaging uniformly accurate in the strip length at fixed $\beta>0$**. This extends D4’s two-cube read-back of C4’s single-cube calculation. The norm tested here is pointwise relative error of regulator densities. A bound on connected local correlators would require a separate argument. [D4’s two-cube result](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7090933094) · [Single-cube formula](README.md)

## Exactly which surfaces survive?

Give every face of the strip weight one in the Wilson action, including each internal shared face once. Use its full two-skeleton with open boundary conditions. Let $R_n$ denote the exact center-averaged density divided by the product of the facewise coshes at the identity edge configuration. Set $h=\tanh\beta$.

Every closed mod-two set of faces is the boundary of a unique subset of the $n$ cubes. Indeed, filling in the cubes gives a three-ball, so its second and third homology over $\mathbb F_2$ vanish. Exactness at the two-chains gives existence, and injectivity of the boundary map on three-chains gives uniqueness. If the subset $S$ has $k$ cubes and $j$ neighboring selected pairs, its boundary has $6k-2j$ faces. The identity-configuration formula is therefore

$$R_n=\sum_{S\subseteq\{1,\ldots,n\}} h^{6|S|-2j(S)}.$$

In particular $R_1=1+h^6$ and $R_2=1+2h^6+h^{10}$. The two-cube correction in excess of $R_1^2$ is $h^{10}(1-h^2)$. For $0<h<1$ every summand is at least $h^{6|S|}$, so $R_n\ge(1+h^6)^n$, with strict inequality for $n\ge2$.

There is also an exact recurrence. Let $u_n,v_n$ be the contributions from subsets whose last cube is absent or present. Starting at $(u_0,v_0)=(1,0)$, appending one cube gives $u_{n+1}=u_n+v_n$ and $v_{n+1}=h^6u_n+h^4v_n$. The exponent four accounts for cancellation of the common face. Consequently

$$R_{n+2}=(1+h^4)R_{n+1}-(h^4-h^6)R_n,\qquad R_0=1.$$

## Why the normalization cannot fix this

Take the long axis of the strip to be $x$. Set all $x$-directed links with $y=z=1$ equal to the unit quaternion $i$, and all remaining links to the identity. Each cube has its own exterior face at $y=1$ with trace zero. If the cube belongs to a selected subset, this face belongs to its boundary regardless of its neighbors. Thus every nonempty surface term vanishes and the exact-to-product ratio is one at this configuration.

At the identity it is $R_n$. Multiplying the exact density by any positive number $c_n$ gives a relative error against the independent-face density at least

$$
\max\{|c_n-1|,|c_nR_n-1|\}\;\ge\;\frac{R_n-1}{R_n+1}
\;\ge\;\frac{(1+h^6)^n-1}{(1+h^6)^n+1}.
$$

The first lower bound follows by minimizing the maximum of the two endpoint errors. It tends to one. The same bound holds for the essential supremum because the ratio is continuous and quotient product Haar has full support. This rules out a volume-uniform small multiplicative error on these strips, even allowing the normalization to vary with $n$. It leaves open whether normalized expectations of specified local observables converge to each other on a four-dimensional trajectory.

## Direct edge-sign check

At $\beta=\log 2$, an independent enumeration used integer grid vertices and the edges of the actual square faces. Starting with one all-positive pattern, each edge doubles the count by retaining the existing pattern and adding one with all its incident face bits toggled. For each resulting six-, eleven- or sixteen-bit pattern with $k$ negative faces out of $P$, its weight is $2^{P-2k}$. Divide the weighted sum by $2^{|E|}$ and then by $(5/4)^P$. The results agree as exact rationals with the recurrence. The same edge enumeration gave ratio one for the second configuration at every length tested. [Exact checker](check_strip.py)

| Cubes | Edges | Faces | Attainable face-sign patterns | Exact ratio |
|---:|---:|---:|---:|---:|
| 1 | 12 | 6 | 32 | $16354/15625$ |
| 2 | 20 | 11 | 512 | $10735924/9765625$ |
| 3 | 28 | 16 | 8192 | $7049692744/6103515625$ |

The arbitrary-length argument above is analytic. The [nine PCP-generated Lean declarations](CentralQuotient.lean) check the single-cube identities and the finite holonomy results.

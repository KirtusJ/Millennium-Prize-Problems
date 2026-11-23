# How far a center sign travels along a Wilson cube strip

At fixed quotient links, the influence of one transverse plaquette sign on a transverse sign \(d\) cells away is at most \(\tanh^{4d}\beta\) on an open \(d\times1\times1\) strip. This holds at every finite \(\beta\ge0\), uniformly in the strip length and in the \(SO(3)\) link configuration. The exponential rate is sharp even for the connected correlation of two nonzero fundamental Wilson traces conditioned on the quotient links. This gives a local estimate in exactly the geometry where the global density ratio can grow exponentially. [Global density comparison](../cube-strip.md)

## Exact sign chain

Use the fundamental \(SU(2)\) Wilson weight \(\exp(\beta\sum_p t_p)\), where \(t_p=\tfrac12\operatorname{Tr}(U_{\partial p})\). Fix a lift of every quotient link. Under product Haar measure the remaining link signs are independent unbiased bits. Their face products give a uniform distribution on coboundaries because the edge-to-face map is linear over \(\mathbb F_2\) with equal-size fibres. The strip is contractible. Thus its face coboundaries are exactly the assignments with product \(+1\) around each cube. Equivalently, choose all \(n+1\) transverse signs and three lateral signs in each of the \(n\) cubes freely. The cube constraint fixes each fourth lateral sign.

Write \(b_i\in\{-1,1\}\) for the transverse signs and \(x_p=\beta t_p\) for the signed face fields of the fixed lift. Conditional on \(b_{i-1},b_i\), the product of the four lateral signs in cube \(i\) is \(b_{i-1}b_i\). Expanding the four factors \(\cosh x_p(1+s_p\tanh x_p)\) and averaging over the three free signs retains just the empty product and the product of all four. Put \(J_i=\prod_{p\text{ lateral in }i}\tanh x_p\). The exact conditional partition weight on the quotient configuration is

\[
 W=\left(\prod_{p\text{ lateral}}\cosh x_p\right)2^{-(n+1)}
 \sum_{b_0,\ldots,b_n} e^{\sum_i x_i b_i}
             \prod_{i=1}^{n}(1+J_i b_{i-1}b_i).
\]

Here \(x_i\) is the transverse field at slice \(i\). Normalizing the summand gives the conditional sign law under the interacting Wilson measure. Each bond obeys \(|J_i|\le q=\tanh^4\beta<1\).

## A bound uniform in all the other fields

At step \(k\), sum over all spins strictly to its right. Including the field \(x_k\), write the two positive weights at \(b_k=\pm1\) as a common factor times \(1\pm m_k\). For preceding sign \(s\), the next conditional mean and its signed half-difference are
\[
 E[b_k\mid b_{k-1}=s]=\frac{m_k+sJ_k}{1+sJ_km_k},
 \qquad \rho_k=\frac{J_k(1-m_k^2)}{1-J_k^2m_k^2}.
\]
Since \(0\le1-m_k^2\le1-J_k^2m_k^2\), \(|\rho_k|\le |J_k|\). A function of a binary spin is affine in that spin. Iterating conditional expectation therefore gives, for \(i<j\),
\[
 \operatorname{Cov}(b_i,b_j\mid\bar U)
   =\operatorname{Var}(b_i\mid\bar U)\prod_{k=i+1}^j\rho_k .
\]
In particular the absolute covariance is at most \(\prod|J_k|\le q^{j-i}\). The total variation distance between the two laws of \(b_j\) obtained by fixing \(b_i=+1\) or \(-1\) is exactly \(|\prod\rho_k|\). For a binary endpoint, total variation is half the absolute difference of the two means. With independent transverse fields as source parameters, \(\partial_{x_i}\partial_{x_j}\log W\) also equals this conditional covariance.

The physical normalized fundamental trace is \(T_i=t_i b_i\). Its conditional covariance gains the factor \(t_i t_j\). Changing a reference lift may change the sign assigned to \(b_i\) and \(t_i\) separately. The product and its conditional covariance are independent of that choice.

## Sharpness with nonzero Wilson traces

Take all longitudinal links equal to the identity. On each transverse square mark its positively oriented \(y\)-edge at \(z=0\), and set every unmarked link to the identity. If every marked edge is the unit quaternion \(\mathbf i\), all transverse fields vanish and all lateral plaquettes have identity holonomy. Each \(\rho_k=q\) and the endpoint sign covariance is \(q^d\). The fundamental endpoint traces in that example vanish.

For \(d\ge2\), replace only the two endpoint marked edges by \(u=(1+\mathbf i+\mathbf j+\mathbf k)/2\). Both endpoint traces now equal \(1/2\) before the sign average. In each end cube one lateral plaquette has trace \(1/2\), since \(\operatorname{Re}(u\mathbf i^{-1})=1/2\). Every other lateral trace is one. Put \(h=\tanh\beta\), \(m=\tanh(\beta/2)\), \(J_*=h^3m\) and \(K=J_*^2q^{d-2}\). Summing the zero-field interior spins replaces two successive bonds \(A,B\) by \(AB\), from \(\frac12\sum_r(1+Asr)(1+Brt)=1+ABst\). The remaining endpoint law is proportional to \(e^{\beta(s+t)/2}(1+Kst)\). Its two means equal \(m(1+K)/(1+Km^2)\) and its product mean equals \((m^2+K)/(1+Km^2)\). Hence

\[
 \operatorname{Cov}(T_0,T_d\mid\bar U)
   =\frac{K(1-m^2)^2}{4(1+Km^2)^2}.
\]

For each fixed \(\beta>0\), dividing by \(q^d\) gives the positive limit \(J_*^2(1-m^2)^2/(4q^2)\). A smaller exponential base with any finite prefactor independent of length fails on these actual quotient configurations.

## Checks and physical scope

At \(\beta=\log4\), direct multiplication of the oriented quaternion links and full enumeration of attainable faces from the edge signs give the following exact results. Flipping the reference lift on one endpoint reverses the corresponding sign covariance and preserves the physical covariance. The enumeration uses the original Boltzmann weights. [Exact arithmetic](check.py)

| Cells | Face patterns | Physical endpoint covariance |
|---:|---:|---:|
| 2 | 512 | \(2533865443344/164016610768609\) |
| 3 | 8192 | \(10713818144485170090000/1092785674092291848518369\) |

The full covariance also contains \(\operatorname{Cov}_{\bar U}(E[T_i\mid\bar U],E[T_j\mid\bar U])\), which this bound leaves open. The strip restricts the transverse geometry. Its rate in lattice units obeys \(-\log q\sim 8e^{-2\beta}\) as \(\beta\to\infty\). A four-dimensional continuum mass gap requires physical time, a nontrivial continuum theory and uniform estimates on its vacuum complement. The separate transfer calculation identifies one obstacle to reading a single-slice projection as the quotient dynamics. [Transfer calculation](transfer.md) · [Generated Lean and replay coverage](execution.md)

## Finite spatial graphs

Complete quotient histories recover the cover states fixed by the center symmetries of the potential. On a simply connected open spatial box with fundamental Wilson action this recovers the full physical Hamiltonian spectrum for \(SU(N)\). The argument works on any fixed positive time mesh. [Smooth \(SU(2)\) theorem](finite-graph.md) · [Analytic potentials for all compact connected groups](analytic-groups.md)

A4's radial estimate also gives an explicit volume-uniform positive-time correlation floor for a single adjoint quotient plaquette at fixed Hamiltonian coefficients. [Adjoint plaquette estimate](adjoint-weight.md)

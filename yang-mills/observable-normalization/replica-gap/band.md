# Second magnetic derivative of the full SU(2) gap

On every finite periodic cubic spatial lattice with $L\ge5$, the sign of the initial magnetic response of the **full** Wilson transfer gap depends on the temporal coupling. It is positive at $\gamma=1$, negative at $\gamma=2$, and vanishes at least once between **1.30638009 and 1.30638010**. The same coefficient holds at every such spatial volume. The remainder below is at fixed volume and temporal coupling.

Use the [electric model's](electric.md) $u=I_2(\gamma)/I_1(\gamma)$, $v=I_3(\gamma)/I_1(\gamma)$, $r=u^4$, and $d=3L^3$. Define

$$
 f(k)=\frac{r+k}{r-k},\qquad c=f(r^2)=\frac{1+r}{1-r},
 \qquad g=\tfrac14 f(u^6)+\tfrac34 f(u^6v),\qquad h=f(v^4).
$$

Each square has $D=12$ distinct neighbors sharing an edge. For the dimensionless gap $\Delta_{\sigma,L}$ at spatial coupling $\sigma$,

$$
 \Delta_{\sigma,L}=-\log r+\frac{\sigma^2}{2}\,\kappa(\gamma)
                     +O_{L,\gamma}(|\sigma|^3),\qquad
 \boxed{\kappa(\gamma)=\frac{2c-h-2D(g-c)}4.}
$$

In particular equal electric gaps for all these volumes persist through the second magnetic derivative. No common positive radius or volume-uniform bound on higher derivatives follows from the calculation.

## Resolving the whole degenerate multiplet

Let $W=\tfrac12\sum_p\chi_p$, where $\chi_p=\operatorname{Tr}U_p$ is the full fundamental character. After removing a scalar per time step use $S_\sigma=K^{1/2}e^{\sigma W}K^{1/2}$. It has the same nonzero spectrum as the symmetric Wilson transfer with split spatial half-weights. The vacuum of $K$ is the constant function, and its first band consists precisely of the $\chi_p$. At fixed box $W$ is bounded. Both spectral groups are isolated and the compact self-adjoint family is norm analytic. Riesz projections therefore reduce their perturbation to finite-dimensional self-adjoint matrices.

Let $P$ project onto any of these groups with eigenvalue $s>0$. In both cases $PWP=0$. For the first group this follows because a product of three elementary characters has a face with an odd private edge. For the vacuum it follows from Haar. The first eigenvalue derivatives vanish. On the group, the second derivatives of $\log\lambda$ are the eigenvalues of

$$
 P W Q\,\frac{s+K}{s-K}\,Q W P,\qquad Q=1-P .
$$

Indeed $S'_0=K^{1/2}WK^{1/2}$ and $S''_0=K^{1/2}W^2K^{1/2}$. Eliminate the first-order complementary component of an eigenvector using $(s-K)^{-1}Q$. The second derivative before division by $s$ is $PS''_0P+2PS'_0Q(s-K)^{-1}QS'_0P$. This gives the displayed formula, with no complementary inverse applied to a band vector. For the vacuum, $W1$ lies entirely in the $r$-band and has squared norm $d/4$. The vacuum log curvature is $dc/4$.

For the first band one must evaluate $W\chi_p=\tfrac12\sum_q\chi_q\chi_p$. The function $f(K)$ preserves the parity of the spin on every edge because the electric transfer commutes with independent center changes. In a product involving four squares, an odd face has four edges and at most three other odd faces, each sharing at most one. Thus a matrix element between products in distinct edge-parity sectors vanishes. Only two equal pairs or a single face appearing four times can contribute.

| Pair within $W\chi_p$ | Electric spectral weights in $\chi_p\chi_q$ |
|---|---|
| $q=p$ | $\chi_p^2=1+\chi_{\rm adj,p}$ has squared weight one at each of $1,v^4$. For two different squared faces only the vacuum overlaps. |
| Distinct, without a shared edge | All eight edges have fundamental spin, giving squared weight one at $r^2$. A common vertex alone does not alter the transfer eigenvalue. |
| Distinct, sharing an edge | Six exterior edges have fundamental spin. The shared edge has spin zero or one, giving squared weights $1/4,3/4$ at $u^6,u^6v$. |

For the last line the full squared norm is one by private Haar integrations. Projection to spin zero on the shared link is Haar averaging on that link. The two remaining three-edge products $A,B$ are independent Haar. Up to inversion and a cyclic change of variables the average is $\int\chi(tA)\chi(tB)\,dt=\tfrac12\chi(A^{-1}B)$. Its squared norm is $1/4$. This fixes the remaining squared norm by orthogonality. On the squared face the adjoint component has norm one by character orthogonality. The inequality $v<u^2$ ensures that all the displayed nonvacuum intermediate energies correspond to eigenvalues below $r$.

Let $\mathcal A_{pq}=1$ when distinct squares share an edge and zero otherwise. For a diagonal matrix element, summing the three rows of the table gives $[-c+h+(d-1-D)c+Dg]/4$, since $f(1)=-c$. For $p\ne q$, the two surviving terms are the overlap of the two squared faces and the common mixed product. These cancel for nonneighbors and give $(g-c)/4$ for neighbors. After subtracting the vacuum curvature, the excited log-curvature matrix becomes

$$
 \tfrac14\big[(h-2c)I+(g-c)(D I+\mathcal A)\big].
$$

To determine the bottom mass one must select its **largest** eigenvalue. For a single increment, let $z=\tfrac12\operatorname{Tr}U$ under the normalized $e^{\gamma z}$ Haar law. Then $\mathbb Ez=u$ and $\mathbb Ez^2=(1+3v)/4>u^2$, from the adjoint character and strict positive variance. The weighted mean of $u^6$ and $u^6v$ thus exceeds $r^2$. The function $f$ is strictly increasing and convex below $r$, so $g>c$. The regular graph has largest adjacency eigenvalue $D$ with constant eigenvector, by $2ab\le a^2+b^2$. This proves the stated $\kappa$ with every vector in the first multiplet accounted for. At each fixed box compact spectral separation keeps higher groups above it for small enough $|\sigma|$.

## Spatial dispersion at the same order

Let $B$ be unsigned edge-square incidence. Then $B^*B=4I+\mathcal A$. In face-centered Fourier coordinates the column $ij$ has entries $2\cos(k_j/2)$ in row $i$ and $2\cos(k_i/2)$ in row $j$. At $k=0$ the squared singular values are $16,4,4$. The normalized left and right top singular vectors are constant. Expanding the six nonzero entries gives top singular value $4-|k|^2/6+O(|k|^4)$. Thus the second-order coefficient of $E_\sigma(k)-E_\sigma(0)$, with the factor $\sigma^2$ removed, is $(g-c)|k|^2/6+O(|k|^4)$. The Fourier symbol is evaluated at the allowed momenta of each box. Its Taylor expansion describes the coefficient function as momenta approach zero. Uniformity of the full dispersion at fixed nonzero coupling is a separate question.

## Signs and comparison with earlier expansions

As $\gamma\downarrow0$, $u\sim\gamma/4$, $v\sim\gamma^2/24$, and $\kappa\to1/4$. As $\gamma\to\infty$, $u=1-3/(2\gamma)+O(\gamma^{-2})$ and $v=1-4/\gamma+O(\gamma^{-2})$. The ratios $c/\gamma,h/\gamma,g/\gamma$ tend to $1/3,1/5,8/21$, respectively. Therefore $\kappa/\gamma\to-71/420$. Finite rational upper and lower bounds on the positive Bessel series at the endpoints certify the much narrower sign change quoted above. Continuity supplies a zero there. Uniqueness has not been established. [Rational sign check](check_sign.py) · [Large-argument Bessel expansion, DLMF §10.40](https://dlmf.nist.gov/10.40)

Münster derived a momentum-dependent effective glueball transfer on the **isotropic** strong-coupling trajectory. Equation (28) starts the mass at $-4\log u+2u^2$. The $\gamma\downarrow0$ limit of our $\sigma^2$ coefficient is $1/8$, compatible with $2u^2\sim\gamma^2/8$ on that diagonal. The fixed-$\gamma$ remainder here does not justify interchanging the two expansions. Münster's higher-order isotropic terms include contributions from higher orders in $\sigma$. The theta-graph control below tests the anisotropic dependence by a separate SU(2) spin-network matrix construction. [Münster, effective transfer matrix, Eqs. (26)–(28)](https://www-library.desy.de/preparch/desy/postpr/1985/desy85-007.pdf) · [Two-square recoupling and finite differences](check_band.py)

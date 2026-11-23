# Resolving individual Wilson transfer levels from periodic histories

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

The spectrum of the full gauge-invariant transfer admits two-sided thermal bounds at every fixed level. With three copies one can test whether the first excited state is isolated from the second. On the open spatial $SU(2)$ Wilson cube at $\beta_s=1,\ \beta_t=0.01$, the three-copy test at period 400 certifies $\lambda_2/\lambda_1<0.990$. The input is a rigorous enclosure of what the thermal reading would give in this finite box. Direct measurement of its integrated slab kernels is a separate numerical task. [Cube calibration](#the-second-excitation-on-the-wilson-cube) · [Exact verifier](check.py)

## Ordered levels without interpolating operators

Use a positive compact self-adjoint transfer $T$ with a simple vacuum and at least $k+1$ positive eigenvalues, in the [physical periodic trace convention](../../../transfer-operator/periodic-time/). Assume $T^N$ is trace class, and order eigenvalues $\lambda_0\ge\lambda_1\ge\cdots$ with multiplicity. Put $P_k=\lambda_0\cdots\lambda_{k-1}$ and

$$
 E_k(N)=\sum_{i_1<\cdots<i_k}(\lambda_{i_1}\cdots\lambda_{i_k})^N,\qquad E_0(N)=P_0=1 .
$$

These are traces on antisymmetric tensor powers. Squaring the largest term bounds it by the sum of squares; multiplying every term by the largest bounds the sum of squares from above. Thus
$$
 L_k=E_k(2N)/E_k(N)\le P_k^N\le U_k=\sqrt{E_k(2N)}.
$$
It follows that $(\lambda_k/\lambda_{k-1})^N$ lies between $L_{k+1}L_{k-1}/U_k^2$ and $U_{k+1}U_{k-1}/L_k^2$, with the upper bound capped at one. The choice $k=1$ recovers the vacuum gap, while $k=2$ tests splitting inside an excited cluster. A scalar normalization of $T$ cancels. If $d_j$ products attain $P_j$, then $L_j/P_j^N\to1$ and $U_j/P_j^N\to\sqrt{d_j}$ as $N\to\infty$ at fixed regulator. This follows by dominated convergence on the summable positive products divided by their maximum. The bounds after taking energy logarithms therefore converge even at a degenerate level.

Only ordinary partitions $Z_{jN}$ and $Z_{2jN}$ for $1\le j\le k+1$ enter through Newton's identities. In particular $6E_3(N)=Z_N^3-3Z_NZ_{2N}+2Z_{3N}$. At long periods this formula can entail severe cancellation.

## Positive readings on independent histories

Take $m$ independent periodic Wilson histories of period $N=2n$. Record the two opposite spatial endpoints $(x_i,y_i)$ on each history. Write $A_{ij}=K_n(x_i,y_j)$ for the real symmetric, strictly positive, gauge-projected half-period kernel. All internal links and endpoint half-weights are included. The following reading has mean $E_m(N)/Z_N^m$ and takes values in $[0,1]$:

$$
 H_m=\frac{\det(A)^2}{m!\operatorname{perm}(A^{\circ2})}.
$$

The square in $A^{\circ2}$ is entrywise. Signed Cauchy–Schwarz on the $m!$ permutation products gives the upper bound. The determinant square is invariant under relabeling the $y$ endpoints, as is the permanent. Thus under integration the independent-history density $\prod_i A_{ii}^2/Z_N^m$ can be replaced by $\operatorname{perm}(A^{\circ2})/(m!Z_N^m)$. The squared determinant integral is $(m!)^2E_m(2n)$: the antisymmetric projection of the tensor-product kernel has kernel $\det A/m!$, and its squared Hilbert–Schmidt norm sums the squared eigenvalue products. This also follows by expanding the two determinants and integrating. The factor $(m!)^2$ is essential. When working entirely with expectations, recover $E_m(2N)/Z_N^{2m}$ by multiplying the period-$2N$ reading by $(Z_{2N}/Z_N^2)^m$.

Relative variance stays bounded for each fixed $m$ and finite box as $N\to\infty$ when the one-step kernel is continuous on compact configuration space with strictly positive vacuum. Normalize $\lambda_0=1$. The kernel of the $n$-step antisymmetric transfer divided by $P_m^n$ converges uniformly to the projection kernel for its top product eigenspace. To see this, factor one step of the exterior transfer off either end; the resulting uniform row-norm bound multiplies the complementary spectral radius to power $n-2$. The single-copy kernel tends uniformly to the strictly positive vacuum product. Hence the denominator of $H_m$ is eventually bounded below uniformly on the endpoint space, and $H_m/P_m^{2n}$ is uniformly bounded. Its mean after the same rescaling tends to $d_m>0$. Constants can depend on the box and copy number. Substituting noisy kernel estimates into a squared determinant or its denominator requires a separate bias analysis.

## The second excitation on the Wilson cube

Use [B4's six-state rational enclosure](../../../transfer-operator/girth-shell/enclosures.md) and the [all-spin tail estimate](../thermal-count/). Normalize $\lambda_0=1$, put $a=\lambda_1^N$, and divide excited weights by $a$. The first is now one. The remaining weights have sum bounded by $s=5h+T$ and squared sum bounded by $v=5h^2+T^2$, where $h=(0.8883/0.8993)^N$ and $T$ bounds the total normalized tail above the six-state cluster. We can take $T<10^{-15}$ and $a<10^{-16}$ at every tabulated period.

Expanding positive products, and writing $E_j'=E_j(2N)$, gives
$$
\begin{aligned}
 E_1'&\le 1+a^2(1+v),\qquad E_2'\ge a^2,\\
 E_2(N)&\le a[1+s+a(s+s^2/2)],\\
 E_3'&\le a^4[v+v^2/2+a^2(v^2/2+v^3/6)].
\end{aligned}
$$
For instance, the terms of $E_3'$ containing the vacuum use two excited factors. They sum to at most $a^4(v+v^2/2)$. The remaining terms use three excited factors. Inserting these estimates into $\sqrt{E_1'E_3'}[E_2(N)/E_2']^2$ cancels every external power of $a$. Squaring and comparing exact positive rationals gives the bounds below.

| $N$ | Upper bound for $\lambda_2/\lambda_1$ from the three-copy test |
|---:|---:|
| 200 | 0.9960 |
| 400 | 0.9900 |
| 600 | 0.9892 |

The original eigenvalue enclosures already yield a tighter direct bound of $0.8883/0.8993$. Here they calibrate a different measurement: finite-temperature partition data alone would distinguish the first two excited levels at the stated resolution. The bounds give neither a continuum spacing nor a volume-uniform spectral splitting.

## Verification

The [exact rational control](check.py) reruns the source cube certificate. It also independently enumerates binary gauge histories after gauge reduction on two squares sharing an edge. The two fundamental cycles have length four and their sum has length six. The kinetic character ratio per edge is $1/2$, and the spatial coupling is $\log2$. Summing determinants against the actual ordered endpoint probabilities at periods two and four, for two, three and four copies, gives exactly the Newton expressions computed from ordinary transfer powers.

Two three-generation PCP OS deployments emitted identical [Lean source](ExteriorTrace.lean). Host Lean checks the finite second and third Newton identities, the signed permutation-square bound and the upper-ratio implication. The written arguments supply the exterior spectral theorem, endpoint integration, uniform kernel limit and all-spin enclosure. Use the [pinned kernel and replay settings](../execution.md), with ../../transfer-increments/replay-guests.py and this directory's source.

[Sampling cost](sampling.md) gives a long-slab information lower bound and an explicit positive short-step Wilson estimator with coupling-uniform relative variance at the electric endpoint. Two further Lean declarations check the bounded-reading second-moment inequality and the full-support obstruction for finite nonnegative estimators.

~~~text
w0.elf 416043b425e3ceae1a19728a4fe1c7e0ab597b33a5a21c962d77dfd6a4f94de5 kernel register: 47 events, head cd38f6d7f6a26e6bc854ecb6ae1de7e728c87eca598c58154667e71582ecc41f
w1.elf c7d55073971026a2b0e6303a6ea40cfaf57e13a15a3ac71a8a8549daa10d0f41 kernel register: 47 events, head b93fc10cec117d6a1a1a545b00c550ab6dfe742325c87b8070692ddaadca0566
w2.elf 3c6bf4997abb0316002733552987bcdb9be502b7c6561ce56c61f00200503fc6 kernel register: 47 events, head d589036d09820f2471a1660cfc951766bce4a0f0de6df5870cad621bb31a7fbb
generated source SHA-256 f3c84a19cc7545128719e23a12f75295f903687a5c130c3eca1a57bbc8c1c38d
~~~

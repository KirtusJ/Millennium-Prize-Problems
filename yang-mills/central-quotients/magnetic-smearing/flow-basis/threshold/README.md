# Resolving the two-gluon threshold at moving momentum

Director C4, 23 November 2026, B.C. Pacific Time (PCT, UTC−07:00).

At spatial momentum magnitude $k$, the free magnetic energy has a continuous two-gluon threshold at $E=k$. Suppose every reading flows both magnetic fields for the same spatial time, chosen in a fixed physical interval $[a,b]$, $0<a<b$. How much cancellation among readings is needed to place a fixed fraction of the spectral weight in $[k,k+\epsilon]$?

Let $g_s$ denote one such reading and $f=\sum_j c_jg_{s_j}\ne0$ a finite signed combination. Define $\chi=\sum_j |c_j|\|g_{s_j}\|/\|f\|$, and let $\chi_{\min}$ be its infimum when the window carries at least a fraction $0<\eta<1$ of the squared norm. Write $\Delta=(k+\epsilon)^2-k^2$. There are $c,C,h_0>0$ depending only on $\eta$ and $b/a$ such that, for every $k\ge0$ and $0<a\Delta<h_0$,

$$
\frac{c}{a\Delta}\le\log\chi_{\min}(k,\epsilon,\eta)\le\frac{C}{a\Delta}.
$$

A finite family with $O(1/(a\Delta))$ clock values attains the upper order. The constants specify the order of growth only. Individual readings are normalized in the definition of $\chi$.

| Resolution requested | Order of $\log\chi_{\min}$ |
| --- | --- |
| At rest, $0<E\le\epsilon$ | $1/(a\epsilon^2)$ |
| At fixed $k>0$ and $\epsilon\downarrow0$ | $1/(ak\epsilon)$ |
| Invariant mass $\sqrt{E^2-k^2}\le\mu$ | $1/(a\mu^2)$, uniformly in $k$ |

The common variable is the squared invariant-mass width. For energy width $\epsilon$, the crossover occurs when $k$ is comparable to $\epsilon$. For coefficients of one sign the captured fraction instead vanishes as $\Theta(\epsilon(k+\epsilon)^4)$, uniformly on bounded momentum intervals in fixed units. The theorem concerns the shared spatial-flow clock and the scalar magnetic tensor contraction. Independent clocks on the two field factors generate a larger space. [Proof and one-sign estimate](proof.md) · [Two-clock comparison](../../transfer-clock/free.md)

## A measurable difference between rest and motion

For the explicit finite filter with $2m-1$ available clock values, the limiting mean squared invariant mass changes when the two limits are taken in different orders. At fixed $k>0$,
$$
m\left\langle E^2-k^2\right\rangle\longrightarrow \frac{8}{3(b-a)}.
$$
At $k=0$ the limit is $15/[2(b-a)]$. The conditional angular distribution accounts for the difference. For $[a,b]=[1,4]$ and $m=4096$ the corresponding finite results are $0.88829250$ at $k=1$ and $2.45636059$ at rest. The analytic limits are $8/9$ and $5/2$. [Limit laws and integration checks](profile.md)

For selected compact SU(2) Wilson vacua the constructive upper result transfers with momentum packets, physical energies and a growing variational basis. The continuum comparison gives no lower bound on the cost in arbitrary compact vacua. Establishing a continuum theory with a separately calibrated interacting scale and a physical mass gap remains open. [Order of limits](profile.md#selected-compact-wilson-vacua) · [Clay problem](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

The free starting measure comes from the two transverse magnetic polarizations. Meyer's leading-order stress-tensor calculation provides a finite-momentum comparison with different operators. Sakai and Sasaki use spatial flow for glueball measurements. Blossier and collaborators analyze variational correlator matrices in lattice field theory. The coefficient cost here refers to the stated free family and normalization. [Meyer](https://arxiv.org/abs/0806.3914) · [Sakai and Sasaki](https://arxiv.org/abs/2211.15176) · [Blossier et al.](https://arxiv.org/abs/0902.1265)

## Verification

Three native PCP OS guests formed a parent, child and grandchild. The parent chose a valid uniform fiber-bound constant, the child convolved the order-four Fejér coefficients, and the grandchild reconstructed the fifth harmonic sum from Pascal's row. Their supervisor read back each completed child result. Hosted Lean 4.19.0 checked ten supporting declarations and rejected three intentional mathematical changes. The guest also rejected an invalid child request. The integral estimates and full cost theorem are written proofs. [Lean declarations](MovingThreshold.lean) · [Guest program](worker.c) · [Execution records](receipts.zip)

The separate Python calculation compares two integration coordinates in eight cases, tests the density and conditional bounds, and checks the integral constants with a trigonometric tail estimate. The archived table distinguishes finite filter orders from their limits. Run from this directory with the [pinned PCP OS kernel and Lean toolchain](../../../clustering/execution.md).

```sh
OPENBLAS_NUM_THREADS=1 python check.py
python verify.py --pcp-os "$PCP_OS" --kernel "$KERNEL" --desk "$DESK" \
  --delegate "$DELEGATE" --qemu "$QEMU" --firmware "$FIRMWARE" \
  --lake "$LAKE" --mathlib "$MATHLIB" --out "$FRESH_OUT"
```

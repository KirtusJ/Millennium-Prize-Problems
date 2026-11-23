# Resolving an interior magnetic energy with two spatial flow times

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

In the free magnetic channel at any fixed momentum $k>0$, one can build a positive autocorrelator whose effective energy stays as close as desired to any chosen $E_0>k$ for an arbitrarily long time. The entire spectral measure is absolutely continuous and its support extends down to $k$. The observable uses only spatially flowed fields on the measurement slice. This gives a control for interpreting a positive plateau in a variational glueball measurement. [Construction and crossover proof](plateau.md) · [Spatial flow in glueball spectroscopy, Sakai and Sasaki](https://arxiv.org/abs/2211.15176)

| Choice of spatial flow times on the two fields | Fraction attainable in $[E_0-\epsilon,E_0+\epsilon]$ as $\epsilon\downarrow0$ |
| --- | --- |
| One common time, arbitrary signed mixtures | At most $O(\sqrt\epsilon)$. [Conditional angular distribution](../../flow-basis/moving.md) |
| Independent times in $[a,b]$, all pair coefficients of one sign | $\Theta(\epsilon)$ uniformly over the mixtures. |
| Independent times in $[a,b]$, signed pair coefficients | Any prescribed fraction $0<\eta<1$, at optimal log coefficient cost $\Theta(\epsilon^{-2})$. A single squared field filter attains this order. [Cost definition and proof](cost.md) |

Here $0<a<b$, $k$ and the interior target are fixed. A shifted Fejér filter of order $m$ has mean squared energy error asymptotic to $210/[151(b-a)m]$. At any fixed time step the first crossing of a fixed level strictly between $k$ and $E_0$ occurs at a time of order $\log m$. These statements concern a continuum of free two-gluon energies. In selected compact $SU(2)$ Wilson vacua the constructive upper bound and prescribed finite time readings pass to spatial packets. A regulator-independent lower cost and the interacting continuum mass gap remain open. [Compact comparison](plateau.md#what-passes-to-a-compact-wilson-packet) · [Clay formulation](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## Numerical and formal checks

For $a=1$, $b=4$, $k=1$, $E_0=2$, the band below has half-width $1/\sqrt m$. The crossing uses time step one and level $1.5$. Composite Gauss rules in $(p,q)$ and $(E,z)$ used a momentum cutoff of seven on each field. Both coordinates were checked for the norm, second moment, band fraction and crossing. The numbers are finite-cutoff numerical checks of the written proofs.

| Filter order $m$ | $m\,\langle(E-2)^2\rangle$ | Fraction in band | First crossing time |
| ---: | ---: | ---: | ---: |
| 8 | 0.418456 | 0.877901 | 8.61156 |
| 32 | 0.451385 | 0.862475 | 19.47115 |
| 128 | 0.462713 | 0.857462 | 24.60262 |
| 512 | 0.463018 | 0.857344 | 29.67691 |

The limiting second-moment constant here is $70/151=0.463576\ldots$. Gauss–Laguerre integration of 21 individual coefficients and complex-contour evaluation of their derivatives agreed to within $10^{-15}$ at one interior parameter choice. [Numerical checks](check.py) · [Full output and native receipts](receipts.zip)

Two fresh PCP OS runs each used a parent, child and grandchild and returned identical Lean source. The guests checked an energy-window width, squared the coefficients of the order-four shifted field polynomial and reconstructed the seventh harmonic sum. Hosted Lean 4.19.0 checked eleven supporting declarations, including the integrated finite-sum bound used in the Laguerre projection argument. Each replay rejected an invalid guest request and three altered Lean conclusions. The Laguerre tail, asymptotic profile, logarithmic crossing and compact comparison have written analytic proofs. [Lean source](InteriorClock.lean) · [Native worker](worker.c) · [Replay](verify.py) · [Pinned toolchain](../../../clustering/execution.md)

~~~sh
OPENBLAS_NUM_THREADS=1 python check.py
python verify.py --pcp-os "$PCP_OS" --kernel "$KERNEL" --desk "$DESK" \
  --delegate "$DELEGATE" --qemu "$QEMU" --firmware "$FIRMWARE" \
  --lake "$LAKE" --mathlib "$MATHLIB" --out "$FRESH_OUT"
~~~

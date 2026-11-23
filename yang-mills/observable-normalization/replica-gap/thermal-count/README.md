# How many states does the thermal trace resolve on a Wilson cube?

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

On one open spatial cube with periodic time, take the original $SU(2)$ Wilson couplings $\beta_s=1,\ \beta_t=1/100$. Define $p_N=Z_{2N}/Z_N^2$ and the dimensionless reading $H_N=(1-p_N)^2/[2(1-p_{2N})]$. It uses only the three ordinary gauge-projected partitions at $N,2N,4N$. The following strict bounds include every spin representation.

| Temporal period $N$ | Lower bound for $H_N$ | Upper bound |
|---:|---:|---:|
| 8 | 5.95 | 6.000001 |
| 600 | 1.000007 | 1.0063 |

At the shorter period all six low states contribute appreciably. The longer period resolves the single lowest excitation. Fractional readings describe a weighted count. These are exact-arithmetic predictions at fixed regulator. Resolving the deficits by direct numerical subtraction at the long period would require thousands of digits. [Positive endpoint estimator](../swap.md) · [B4's finite-coupling certificate](../../../transfer-operator/girth-shell/enclosures.md)

## Removing the vacuum

Let $r_i=\lambda_i/\lambda_0$ in decreasing order for $i\ge1$, $s=\sum r_i^N$, $t=\sum r_i^{2N}$. Then $1-p_N=(2s+s^2-t)/(1+s)^2$ lies between $2s/(1+s)^2$ and $2s$, since $0<t\le s^2$. Applying both inequalities to the two periods bounds $H_N/(s^2/t)$ between $(1+s)^{-4}$ and $(1+t)^2$. The quantity $s^2/t$ is the effective number of excited states. At fixed box with isolated first eigenvalue of finite multiplicity it tends to that multiplicity, since after division by $r_1^N$ only equal largest weights survive. Finite trace at an initial period dominates the tail.

## Summing the infinitely many smaller states

Set $u=I_2(\beta_t)/I_1(\beta_t)\le1/400$. B4 bounds $r_1/u^4$ between 0.8993 and 0.9040 and the next five between 0.8836 and 0.8883. An operator norm bound on all higher states alone would leave their total multiplicity unrestricted. For the trace, use the *ordered* min–max comparison $r_i\le729 k_i$, where $k_i$ are the descending eigenvalues of the electric transfer. Indeed the squared spatial multiplier divided by its Haar mean is bounded by 729, and the normalized vacuum Rayleigh bound for the leading eigenvalue is at least one in B4's convention. Compare on the kinetic square-root side. The first seven electric states including the vacuum exhaust all networks below total twice-spin degree six. The cube is bipartite, and a degree-five invariant network is excluded by center parity (odd-labeled edges form an even-length union of cycles).

For $y_i=(r_i/r_1)^N$ write $T=\sum_{i\ge7}y_i$. Each of the twelve links of twice-spin $m$ has full representation dimension $(m+1)^2$ and kinetic eigenvalue at most $u^m$. The physical projection can only decrease multiplicities. At $z=1/10$, summing the generating function over all edges and using $u^N<z$ gives

$$
 T\le z^{-6}\left[\frac{1+z}{(1-z)^3}\right]^{12}
           \left[\frac{729}{400^2\cdot0.8993}\right]^N .
$$

Indeed each omitted weight of degree $j\ge6$ obeys $(u^N)^j\le(u^N/z)^6 z^j$. This bounds the entire tail after division by the certified lower bound on $r_1^N$. At both periods $T<10^{-10}$ and $s<10^{-80}$.

Put $l=(0.8836/0.9040)^N,\ h=(0.8883/0.8993)^N$. The leading six weights are one and five numbers between $l$ and $h$. With their sum $A$ and squared sum $B$, the exact loss $6B-A^2$ is the sum of the fifteen squared pair differences. It is at most $5(1-l)^2+10(h-l)^2$, with $B\ge1+5l^2$. Including the tail reduces this rank lower bound by at most a factor $1+T^2$. Upper bounds are $6(1+T)^2$ by Cauchy–Schwarz on the six, and $(1+5h+T)^2$ by retaining just the first term in the denominator. Combining these inequalities and the vacuum factors gives the table. No large-volume or physical time-step limit has been taken.

[Exact rational verifier](check.py) reruns B4's input certificate. Run it with Python from this directory. [Lean source](ThermalCount.lean) checks the deficit identity, its two inequalities and the algebraic rank loss implication. The spin enumeration, min–max application and infinite trace estimate are written arguments. Root, child and grandchild PCP OS guests emitted the source and a second deployment reproduced it. Use the [parent replay settings](../execution.md) with ../../transfer-increments/replay-guests.py and this source. Host Lean used the pinned Mathlib checkout.

The state-count majorant uses the finite-graph spin-network decomposition. [Baez, Spin Network States in Gauge Theory](https://arxiv.org/abs/gr-qc/9411007)

~~~text
w0.elf 339e800d10369277dff565cfd80d0eb3092dac7f98ec08e4088cbf741cb02a27 kernel register: 47 events, head ef0ba9ce7ec9032bb4e3a694e5c8206af52e9f22aacb17482e470d5ec1570884
w1.elf 536482af22f98a96f7f7273783db110615d5ed0296c6de0664ce3f7992ef4de9 kernel register: 47 events, head 2382673c4f5472857ca6ed58682bfce18f8215aa7a98b10a0fb596894e83b65d
w2.elf db59ec623ff161b4aec9c3c12c4a001278e31f9d181936741bcdc419232574e6 kernel register: 47 events, head 0d31da24e2fa2b56c7207118258d9287cd5eb593a7d261e1aac2b07cf24beca8
generated source SHA-256 404901db41d23a68163da87af2178f0dbfaa7e257e7a1314d7ca8eb304341280
~~~

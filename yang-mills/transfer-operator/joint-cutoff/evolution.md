# Positive-time evolution on a simultaneous sequence

Use the operators and energy units of the [gap estimate](README.md). Fix $t>0$ and assume $ac\le1/36$ and $a\le t/2$. Set $N=\lfloor t/a\rfloor$ and choose any positive integer $k$. On the whole physical Hilbert space at this volume,
$$
\left\| (T_a/\|T_a\|)^N-e^{-t(H-E_0)}\right\|
\le \frac2N+\frac{3a}{t}+7ac+\frac4k+\frac{72ak^2}{t}+144atc^2.
$$
Both operators include their vacuum channels. In a sequence of different Hilbert spaces each norm compares the two operators in the same box. For fixed $t$, take $k=\lceil(t/a)^{1/3}\rceil$. All terms vanish if $a(1+c)^2\to0$. No hypothesis on the size of the first gap enters this statement.

## Moving the origin of energy

Write $F_a=B_a-\mu_0$ and $F=H-E_0$. Set $e_*=\min(\mu_0,E_0)\le c$, and first shift both operators by this common value. To move from $B_a+c,H+c$ to $B_a-e_*+\eta,H-e_*+\eta$ for $\eta>0$, add the scalar $-(c+e_*-\eta)I$ in the common-potential resolvent identity. Both new inverses have norm at most $1/\eta$. The two outer factors have norm at most $1+|c+e_*-\eta|/\eta\le 2+2c/\eta$. Then move the larger ground energy to its own origin. That final change costs at most $|E_0-\mu_0|/\eta^2$. In total,
$$
\|(F_a+\eta)^{-1}-(F+\eta)^{-1}\|
\le 9a(2+2c/\eta)^2+72ac^2/\eta^2 .
$$

## Implicit and explicit time steps

For $x\ge0$, the scalar implicit Euler approximation satisfies
$$
0\le(1+x/k)^{-k}-e^{-x}\le2/k.
$$
For $y=x/k\le1$, use $\log(1+y)\ge y-y^2/2$ and $\log(1+y)\ge y/2$ to bound the difference by $(ky^2/2)e^{-ky/2}\le8e^{-2}/k$. For $y\ge1$ the difference is bounded by $2^{-k}$. Apply this estimate at $x=tF_a$ and $x=tF$ by the spectral theorem. The two middle $k$th powers of $(I+tF_a/k)^{-1},(I+tF/k)^{-1}$ differ by at most $k$ times the norm difference of their bases, which are contractions. With $\eta=k/t$, each base is $\eta$ times its corresponding resolvent. The shift estimate and $(2+2s)^2\le8(1+s^2)$ give
$$
\|e^{-tF_a}-e^{-tF}\|\le4/k+72ak^2/t+144atc^2 .
$$

For the actual normalized Wilson step, put $h=a/(1-a\mu_0)$. Then $T_a/\|T_a\|=I-hF_a$ and its spectrum lies in $[0,1]$. On $0\le y\le1$ we have $0\le e^{-Ny}-(1-y)^N\le2/N$. For $y\le1/2$, $-\log(1-y)-y\le y^2$ and the difference is at most $Ny^2e^{-Ny}\le4e^{-2}/N$. For $y>1/2$ use $e^{-N/2}\le2/N$. Consequently $\|(T_a/\|T_a\|)^N-e^{-NhF_a}\|\le2/N$.

Finally $\min(t,Nh)\ge t/2$, $a\mu_0\le1/12$ and $|Nh-t|\le(a+t a\mu_0)/(1-a\mu_0)$. The exponential derivative at $s>0$ is bounded in norm by $1/s$. This gives $\|e^{-NhF_a}-e^{-tF_a}\|\le 3a/t+7ac$, using $\mu_0\le3c$. Adding the three differences proves the stated bound.

## Vacuum correlations and a choice of spacing

For a list of bounded time-slice insertions $O_1,\dots,O_m$ at positive time separations $t_i$, form both correlations with the same operators and with their respective normalized vacua. Use $\lfloor t_i/a\rfloor$ transfer steps in each interval. Writing $d_i$ for the displayed evolution error and $v=\|\Omega_a-\Omega\|$, telescoping gives
$$
|C_a-C_H|\le \left(2v+\sum_i d_i\right)\prod_j\|O_j\|.
$$
For vanishing time separations one may combine adjacent insertions. If times are rounded individually to time-slice positions, each step count differs from the stated one by at most one. The scalar time-change estimate then applies with that actual count and the corresponding rounding error. For uniformly bounded insertions and gaps bounded below, $a(1+c)^2\to0$ suffices for convergence. A sequence of growing insertion norms can instead use the displayed product and a faster time refinement.

At fixed spatial mesh and in the uniform-gap Hamiltonian regime, a normalized bare plaquette is an example with bounded norm. For a growing smeared sum take the actual operator norm or the bound by the sum of the coefficient magnitudes times the maximum individual plaquette norm. A lower bound on weight in a finite Hamiltonian energy band need not pass through a discontinuous spectral cutoff at an atom. Fixed positive-time moments pass by the estimate above. Spectral interval conclusions require test functions supported in a slightly enlarged interval or continuity of the limiting measure at the endpoints. [Hamiltonian plaquette estimates](../hamiltonian-time/README.md)

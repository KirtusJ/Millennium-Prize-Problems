# Which energy a large Wilson rectangle sees after vacuum subtraction

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00) · Millennium Prize Problems, Yang–Mills

For two identical parallel rectangular Wilson loops, subtracting the vacuum changes the strong-coupling surface at long times. Almost all of each rectangle is capped. One plaquette is left open in each cap, and the four sides of that plaquette propagate across the time separation. Any of the $nm$ plaquettes can carry this tube, including those at edges and corners.

Use the original isotropic four-dimensional $SU(2)$ Wilson measure with normalized real fundamental trace in the action. Let $W$ be the **unnormalized** fundamental trace around a spatial $n\times m$ rectangle, $A=nm$, $P=2(n+m)$, and translate it by $k$ time steps without spatial displacement. Put $w=\mathbb EW$ and $C_k=\mathbb E[W_0W_k]-w^2$. Take the infinite-volume Wilson vacuum in its strong-coupling uniqueness region. For $n,m,k\ge2$, with $z=\beta/4$, the first nonzero term is
$$
 C_k=B_k z^{D_k}+O_{n,m,k}(\beta^{D_k+1}),\qquad
 D_k=\min(Pk,\,2(A-1)+4k),\qquad
 B_k=\mathbf1_{Pk=D_k}+A\mathbf1_{2(A-1)+4k=D_k}.
$$
The coefficient at equality is $A+1$. After propagation in the late regime, the centered rectangle vector agrees in relative Hilbert norm with $z^{A-1}$ times the sum of its $A$ centered elementary-plaquette vectors propagated by the same time. [Vector overlap](overlap.md) A lower bound from requiring temporal plaquettes to transmit a gauge-invariant signal is essential here. Center parity alone permits two disconnected disks of area $2A$. [Why the disks cancel and which connected surfaces remain](surfaces.md)

For a simultaneous regulator limit let $nb\to X>0$, $mb\to Y>0$, and $kb\to T>0$. If $|\log\beta|\, b^2\to\infty$, the first term gives $C_k=B_k z^{D_k}(1+o(1))$ **with these growing loop sizes and lags**. The same improvement gives $w=2z^A(1+o(1))$. The estimates follow from a volume-uniform analytic disk of explicit radius $1/1024$. For example, above the connected crossover,
$$
       C_k/w^2\sim (A/4)z^{4k-2}.
$$
The long-time coefficient and power survive division by an exponentially small squared mean. The bound with its finite-parameter error is in the [analytic estimate](analyticity.md).

At the earlier equality $Pk=2A$, the propagated vector including its vacuum component has asymptotic weights $4/5$ at vacuum energy and $1/5$ at the perimeter excitation, whose lattice energy differs from $P\log(4/\beta)$ by a quantity tending to zero in probability. At sufficiently late lags the centered vector instead sees lattice energy $4\log(4/\beta)+o_{\mathbb P}(1)$. For an even square the first equality is an integer lag. For an odd square the **connected** equality is an integer lag, and the unit-plaquette contribution outnumbers the perimeter contribution by $A$ to one. [Spectral weights and time scales](spectrum.md)

There is a separate fixed-coupling result about the whole gauge-invariant vacuum sector. On a periodic spatial torus of side $L\ge2$ the strong-coupling mass in lattice units satisfies
$$
 -\log\|S_{\mathrm{vac}^{\perp}}\|
      =\min(4,L)|\log\beta|+O(1)
       \qquad(\beta\downarrow0),
$$
uniformly in $L$. In the infinite-volume Wilson vacuum the coefficient is four. The short periodic directions at $L=2,3$ permit winding excitations. The contributing elementary plaquette tube and the leading four-log glueball mass are classical. The proof here obtains a uniform spectral ceiling from factorization on a forest and a complex-coupling bound for arbitrary bounded spatial probes. It also treats growing ordinary rectangles, their competing coefficients and the short periodic boxes. In infinite volume $m^2/\sigma_Q=16|\log\beta|+O(1)$ uniformly in rectangular tension estimates. The ratio is independent of the chosen physical spacing. This regime does not construct Yang–Mills theory at a finite nonzero renormalized interaction scale. [Proof and comparison with Münster’s series](gap.md) · [Lean and execution evidence](execution.md)

Gross and Ooguri already depict a lattice-spacing tube connecting separated large loops and describe the resulting glueball scale. The calculation here determines which integer rectangle and separation select it, its coefficient at the crossover, and its overlap with a sum of elementary-plaquette vectors. [Gross and Ooguri, Fig. 6 and accompanying text](https://arxiv.org/pdf/hep-th/9805129)

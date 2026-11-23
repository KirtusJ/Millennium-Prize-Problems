# Positive-energy bands seen by finitely many magnetic probes

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Fix an integer $d\ge1$, an energy interval $0<a<b<\infty$, and $s>0$. In any thermodynamic limit of the even isotropic periodic four-dimensional pure SU(2) Wilson cubes at fixed inverse coupling $\beta$, let $T$ be the positive time-step transfer contraction, normalized to fix the vacuum. Write $E=-\log T$, allowing $+\infty$ on the kernel. There exist $c,\eta>0$, depending on these three choices, such that for all sufficiently large $\beta$, at the integer scale $R=\lfloor c\beta^{1/8}\rfloor$, the centered vectors of $d$ explicit bounded spatial observables satisfy
$$
  \Big[\langle\psi_{i,R},\mathbf 1_{(a/R,b/R)}(E)\psi_{j,R}\rangle\Big]_{i,j=0}^{d-1}
  \succeq \eta I_d .
$$
The constants and the starting coupling work for every choice of these periodic limit states. The projection has rank at least $d$ and excludes the whole fixed space of the transfer, even in a mixed state. Its rank counts linearly independent projected vectors and permits continuous spectrum or a degenerate energy. In particular the infimum of the strictly positive lattice energies is at most $C\beta^{-1/8}$, with the same upper bound for the gap on the orthogonal complement of the selected vacuum.

At every $R\to\infty$ with $R^4/\sqrt\beta\to0$, the entire finite matrix of spectral measures in $x=e^{-RE}\in[0,1]$ converges weakly to the explicit free packet matrix below, including its equal-time mass. At $R=\lfloor c\beta^{1/8}\rfloor$ the conclusion is a positive lower bound on the weight of the prescribed band. Different choices of $d,a,b$ can require different $c,\eta$. The spatial supports grow with $R$. The positivity of a gap at fixed coupling, an interacting continuum limit and a nonzero local reading at one full correlation length are open. [Proof and observables](proof.md) · [Jaffe and Witten, problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## Review of the fixed-stencil estimate

C4's argument at commit a4601bd gives the stated $O(\beta^{-1/32}\log(2+\beta)^{1/16})$ lattice upper bound. In the Haar variation the detour removes dependence of the generator on the varied link. The derivative of the test's transporter still contributes, including for nonincident plaquettes. The spatial weight is invariant under either time shift. In the two-lag argument the same centered observable enters both moments. Independent replay gave maximum error $7.64\times10^{-11}$ for the five varied-link controls. Omitting the path term changed a derivative by 1.47. The 144 cube cycles and 36 finite Hodge decompositions also passed. [C4's derivation](../../../central-quotients/tangent-curvature/periodic-limit/rate/README.md)

A4 independently obtains the eighth-root upper bound and positive weight in one band using a scalar tent packet. The present matrix argument allows any preassigned band and any fixed number of displaced probes. The common spatial root gives a uniform estimate at all time separations because the auxiliary magnetic variation has zero temporal component. [A4’s scalar result at ce17173](../../../observable-normalization/transfer-increments/spatial-packet/README.md)

Faria da Veiga and O’Carroll develop Wilson stability and plaquette generating-function bounds. Abdelghani and Nissim derive compact-group integration identities at finite $N$. Osterwalder and Seiler establish lattice physical positivity. Blossier et al. discuss extracting energies from correlation matrices. The band claim here uses a lower bound on a matrix of spectral projections and permits arbitrary spectral type. [Stability](https://arxiv.org/abs/2205.07376) · [Haar variation](https://arxiv.org/abs/2309.07399) · [Transfer positivity](https://www.sciencedirect.com/science/article/pii/0003491678900398) · [Correlation matrices](https://arxiv.org/abs/0902.1265)

[Independent numerical controls](check.py) · [Native worker controls](worker.c) · [Execution record](execution.md)

For the fourfold packet conditioned on a large normal momentum, the two transverse momenta have an explicit joint limit on their original block scale. [Conditional transverse law](normal-extremes/README.md)

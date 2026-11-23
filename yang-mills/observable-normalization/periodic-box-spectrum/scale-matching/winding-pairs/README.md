# Can a pair of winding flux tubes explain the small-box tensor energies?

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

In the $12^3\times16$ SU(2) Wilson box at $\beta=2.427$, twice the measured energy of a single winding tube is $1.1608(76)$. The lowest reported energy in the cubic $E^+$ tensor channel is $1.220(9)$. If the latter is the lower edge of a two-level Hamiltonian, **no choice of its mixing amplitude can put a pair diagonal at 1.1608**. The discrepancy of 0.0592 lattice energy units also sets a quantitative test for missing low-energy spectral weight. It concerns a finite-volume tensor channel. The [scalar mass comparison](../physical-scalar/README.md) and the infinite-volume vacuum gap are distinct questions. [Athenodorou and Teper, Table 17](https://arxiv.org/pdf/2106.00364#page=69)

## A necessary condition independent of the mixing strength

Write $F$ for the single-tube energy in lattice units and $d$ for the diagonal expectation of the Hamiltonian in a normalized, specified pair state. A winding tube is also called a torelon. A pair with zero total center charge can mix with a glueball. For a Hermitian two-level model with energies $e_-\le e_+$, every diagonal belongs to $[e_-,e_+]$, since it is a convex combination of the two energies. Thus the shift from the noninteracting pair value must satisfy $d-2F\ge e_--2F$. This bound is sharp if the normalized pair state is the lower eigenstate. The argument allows any glueball diagonal. Meyer’s finite-volume Hamiltonian includes both an intrinsic shift and a mixing term. He already observed that mixing alone could overpredict the tensor splitting in SU(3). [Meyer, §§2–3, especially Eqs. 4–10](https://arxiv.org/pdf/hep-lat/0412021#page=6)

| Gauge group and spatial side | Lowest reported tensor energy | $2F$ | $e_--2F$ |
|---|---:|---:|---:|
| SU(2), 12 | 1.220 | 1.1608 | +0.0592 |
| SU(2), 14 | 1.254 | 1.4280 | −0.1740 |
| SU(3), 8 | 0.519 | 0.4214 | +0.0976 |
| SU(3), 9 | 0.583 | 0.5052 | +0.0778 |
| SU(3), 10 | 0.670 | 0.6114 | +0.0586 |
| SU(3), 11 | 0.883 | 0.6970 | +0.1860 |
| SU(3), 12 | 0.910 | 0.8070 | +0.1030 |
| SU(3), 16 | 1.060 | 1.3562 | −0.2962 |

SU(3) provides an independent check in $E^{++}$ with a variational basis that explicitly included winding pairs. Its lattice units are specific to that study. At SU(2) side 12 the residual has statistical standard error 0.0118 if the two estimates are independent and at most 0.0166 for any covariance consistent with their printed errors. Moving each input by three printed errors in the adverse direction leaves +0.0094. This rectangle has no assigned coverage probability. In SU(2), the entries are variational effective energies at $t=2a$ or fits to plateaux starting there. Energy extraction and operator coverage remain systematic uncertainties. [SU(2) measurement convention and state assignments](https://arxiv.org/pdf/2106.00364#page=23) · [SU(3) data, Table 1](https://arxiv.org/pdf/hep-lat/0412021#page=15)

## How much weight below the reported level would suffice?

Let $b>0$ denote the reported lower energy used as a threshold. In a positive vacuum-subtracted Hamiltonian let $w$ be the spectral weight of a normalized pair state in $[0,b)$. Its Rayleigh expectation $d$ obeys $d\ge (1-w)b$, since energies above the threshold cost at least $b$. Thus

$$ (d-2F)+bw\ \ge\ b-2F. $$

The alternatives have a common quantitative scale. At SU(2) side 12, setting $d=2F$ requires **at least 4.85%** of this pair state's spectral weight below 1.220. Conversely, placing all its weight at or above 1.220 requires a diagonal shift of at least 0.0592.

A one-step transfer measurement gives a different test. For a normalized vacuum-sector probe state $D$, set $r=\langle D,e^{-H}D\rangle$ and $q=e^{-b}$ in lattice units. Positivity gives $r\le w+(1-w)q$. If one assumes the one-step moment factorizes as $r=e^{-2F}$, the necessary weight is $w\ge(e^{-2F}-q)/(1-q)$, or **2.55%**. Across the adverse three-error rectangle the two conditional lower percentages are 0.787% and 0.411%, respectively. Neither hypothesis is a measured property of a pair state in Table 17. These weight inequalities apply to a Hamiltonian spectral measure in a state. In a periodic thermal trace the effective slope can also contain transitions between excited states. [Blossier et al., correlation matrices and state extraction](https://arxiv.org/abs/0902.1265) · [Finite-period analysis](../../../../spectral-support/finite-readings/periodic-vacuum/README.md)

A third correlation time makes the weight test more discriminating. For three consecutive vacuum autocorrelator readings from the **same fixed pair operator**, put $m=C_1/C_0$, $z=C_2/C_0$ and $q=e^{-b}$. If $m>q$, the one-sided variance inequality gives $w\ge (m-q)^2/[z-m^2+(m-q)^2]$ for the state weighted at the base time. Thus $z/m^2-1\le (1-q/m)^2$ suffices for at least half the correlator weight to lie below $b$. At the stipulated $m=e^{-1.1608}$ and the central $b=1.220$, the allowed relative curvature is **0.003304**, or 0.3304%. The two-point distribution saturating the bound there has transfer values $q$ and $2m-q<1$, so the half-weight threshold is sharp for those moments. Table 17 does not provide this triplet. A test requires joint uncertainties and a vacuum reading or a certified thermal correction. [Three-reading derivation and finite-period counterexample](../../../../spectral-support/finite-readings/three-readings/README.md)

## A two-volume model and a third-volume check

For disproof, assume within this SU(2) window that the glueball diagonal $g$, the magnitude of the mixing $h$, and the shift $s$ in the pair diagonal $2F+s$ are constant across sizes. At sides 12 and 14 the first two reported energies are $(a,b)=(1.220,1.317)$ and $(c,d)=(1.254,1.549)$. Equal $h^2=(g-a)(b-g)=(g-c)(d-g)$ gives $g=(cd-ab)/(c+d-a-b)=1.26205$ and $h=0.04807$. The side-12 trace then gives $s=0.11415$. The remaining algebraic check on the traces is $(c+d-a-b)-2(F_{14}-F_{12})=-0.0012$. Its illustrative independent-input statistical error is 0.0330. The traces alone constrain the sum $g+s$.

With these parameters frozen, the side-20 winding energy $F_{20}=1.0996(39)$ predicts a lower tensor level of 1.2599. The measured energy, held out of the construction, is 1.284(13). The residual is +0.0241, with first-order standard error 0.0199 under independent inputs and at most 0.0319 to that order with unknown covariance. These central values allow a shifted pair model. They do not identify a physical interaction energy without a specified pair vector and overlap information. The model also predicts pair probabilities of 43.4% and 2.7% in the lower eigenstate at sides 12 and 14. Measuring the pair/glueball correlation matrix with explicit winding-pair operators, a stated orthonormalization, and later time separations would test that prediction independently of the energy fit. Other levels can enter this subspace as the volume changes. The calculation supplies no continuum or infinite-volume lower bound. [SU(2) data](https://arxiv.org/pdf/2106.00364#page=69) · [Meyer’s operator construction](https://arxiv.org/pdf/hep-lat/0412021#page=8)

[Recompute all values](check.py) with Python 3. A [three-level native PCP OS replay](replay.py) checked the six positive residuals in integer units, the diagonal floor, the two weight inequalities, and the common-mixing identity. Lean verified the [four declarations](WindingPairs.lean). The supervisor rejected a malformed delegation and three changed declarations. [Native worker](worker.c)

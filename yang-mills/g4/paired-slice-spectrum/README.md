# Recovering the finite-volume Wilson spectrum from two spatial slices

The joint law of two complete spatial configurations half a temporal period apart determines every finite-volume Wilson excitation energy relative to the vacuum, with multiplicities. A common positive rescaling of the transfer leaves this law invariant. The following estimate quantifies how much information survives when the configurations are recorded only as cell labels. It applies at any finite magnetic coupling and positive finite temporal coupling of the ordinary $SU(2)$ Wilson action. Its input is the joint distribution of two labels measured on the **same** periodic history. Time has $N=2n$ steps; the finite spatial graph and the one-step clock stay fixed.

Let $p_{ij}$ be the probability of opposite slices in cells $i,j$. Form the matrix $B_{ij}=\sqrt{p_{ij}}$ **entry by entry**, and order its singular values $\sigma_i$ decreasingly. For each cell let $\delta_i$ bound its diameter in the gauge-orbit metric defined below. If $\lambda_i$ are the ordered physical transfer eigenvalues and $p_i^{\rm th}=\lambda_i^{2n}/\operatorname{Tr}T^{2n}$, then
$$
\sum_i |p_i^{\rm th}-\sigma_i^2|\le \ell+2d,\qquad
\sum_{i>D}p_i^{\rm th}\le\ell
$$
for $D$ non-null cells. Here $h_{ij}=\operatorname{sech}[\beta_t(\delta_i+\delta_j)/2]$, $\ell=\sum_{ij}p_{ij}(1-h_{ij}^2)$ and $d^2=\sum_{ij}p_{ij}(1-h_{ij})^2$. A common diameter $\delta$ gives total variation at most $(\beta_t\delta)^2$. All multiplicities are retained, including in sectors invisible to a single plaquette reading. The cost in the number of full-slice cells can grow rapidly with volume.

The vacuum probability satisfies the direct bracket
$$\|h\circ B\|_{\rm op}^2\ \le\ p_1^{\rm th}\ \le\ \|B\|_{\rm op}^2.$$
Thus diameter control supplies the **lower** probability needed to bound thermal contamination in B4's two-lag test. The entire histogram also gives an interval for $\Delta=-\log(\lambda_2/\lambda_1)$. A certified lower bound requires the first and second probability intervals to separate. [Derivation and statistical errors](spectrum.md) · [B4’s finite-period test](../../transfer-operator/periodic-time/thermal-gap-test.md) · [A4’s replica method](../../observable-normalization/replica-gap/swap.md)

| Tested system | Input | Result |
| --- | --- | --- |
| Compact $SU(2)$ class rotor, $\beta_t=2$, two time steps | 32 opposite-slice angle bins, interval Haar integration | Vacuum probability in $[0.798044,0.859976]$; one-step excitation ratio in $[0.403514,0.503054]$. The independent character values are about $0.828814$ and $0.433127$. |
| Frozen four-dimensional matched ensembles | Flowed spatial plaquette averages at several times | These summaries have no established fine full-orbit cell diameter. A center twist can leave every recorded flow time unchanged. A numerical four-dimensional vacuum probability or mass does not follow from the rotor control. |

The estimate covers the interacting finite Wilson regulator. A continuum conclusion would need controlled full-slice probabilities, spatial-volume and mesh limits, a physical time scale and nontrivial reconstruction on the same trajectory. [Rotor computation and frozen-data audit](controls.md) · [Lean and execution record](execution.md) · [Lüscher’s transfer construction](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf) · [Clay problem](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)

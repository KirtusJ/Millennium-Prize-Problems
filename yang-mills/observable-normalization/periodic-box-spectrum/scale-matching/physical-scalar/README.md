# Does the SU(2) scalar energy survive refinement in flow units?

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

The scalar glueball energy agrees, within the quoted statistical errors, at two lattice spacings that differ by 27% in gradient-flow units. The physical box sides differ by 2.8%. A separate fixed-coupling volume comparison strongly disfavors a pure inverse-side law for the measured scalar effective energy. The remaining question is how far these finite measurements constrain the bottom of the spectrum.

## Two direct matches in bare coupling

Athenodorou and Teper give the lightest scalar mass $aM$ for four-dimensional pure SU(2) Wilson gauge theory. Hirakida, Itou and Kouno independently measure $t=t_0/a^2$ on $32^4$ lattices using the flow reference $t_0^2\langle E(t_0)\rangle=0.10$. Both studies use the same Wilson bare-coupling convention. Define $\tau=\sqrt{8t_0}$, $Y=M\tau=(aM)\sqrt{8t}$ and $\ell=L/\tau=N/\sqrt{8t}$. The two couplings below occur in both tables, so each product uses a measured reference scale. [Spectroscopy, Table 1](https://arxiv.org/pdf/2106.00364#page=62) · [Flow scale, §4.2 and Table 1](https://inspirehep.net/files/c7ecc1004678dd8f9b85a50c7ee9cdd5#page=9)

| $\beta$ | Spectroscopy box | $aM$ | $t_0/a^2$ | $L/\tau$ | $M\tau$ |
|---|---|---|---|---|---|
| 2.60 | $30^4$ | 0.5001(41) | 3.522(10) | 5.6517 | 2.6546(221) |
| 2.70 | $40^4$ | 0.3652(35) | 6.628(36) | 5.4932 | 2.6593(265) |

The difference, fine minus coarse, is $0.0047\pm0.0345$ using first-order propagation and independent statistical inputs. Changing the flow reference to 0.08, 0.09 or 0.12 puts the fine/coarse central ratio between 0.9983 and 1.0032 across all four conventions. These checks reuse the same spectroscopy. Finite flow volume, periodic time extent, and state extraction remain systematic uncertainties. [Alternative flow scales, Table B1](https://inspirehep.net/files/c7ecc1004678dd8f9b85a50c7ee9cdd5#page=19)

## Changing volume at fixed cutoff

At $\beta=2.427$ and temporal extent $16a$, the lowest reported scalar $A_1^+$ effective energies from $t=2a$ are 0.840(11), 0.854(8), and 0.847(8) in lattice units at spatial sides $12a,14a,20a$. A pure $C/L$ law anchored at $12a$ predicts 0.504 at $20a$. The observed residual is 0.343, with statistical standard error 0.0104 for independent estimates and at most 0.0146 under arbitrary correlation given the quoted marginal errors. In the same table the winding flux-tube energy increases from 0.5804(38) to 1.0996(39). The probe and channel matter. A scalar effective energy at one Euclidean time cannot exclude a lighter level with small overlap. [Spectroscopy, Table 17](https://arxiv.org/pdf/2106.00364#page=69) · [Blossier et al., spectral extraction from correlation matrices](https://arxiv.org/abs/0902.1265)

## What would suffice to control the cutoff limit?

Write $x=a^2/t_0$, with measured central coordinates $c=0.283930$ and $f=0.150875$. Suppose the same scalar energy branch $Y(x,\ell)$ exists down to $x=0$ at the fine-box size $\ell_f$. Treat coordinates as exact initially. Let $e_c,e_f$ bound the absolute differences between the reported energies and that branch at the two measured boxes, including spectral and finite-time systematics. Assume

$$|Y(c,\ell_c)-Y(c,\ell_f)|\le B|\ell_c-\ell_f|,\qquad |\partial_x^2Y(x,\ell_f)|\le K\quad (0\le x\le c).$$

Set $w=f/(c-f)$ and $I=(1+w)Y_f-wY_c$, where $Y_i$ are the reported products. The affine extrapolant has intercept $I$ before errors and volume correction. The interpolation remainder at zero is $cf\,\partial_x^2Y(\xi,\ell_f)/2$ for some $0<\xi<c$. The triangle inequality gives

$$Y(0,\ell_f)\ge I-wB|\ell_c-\ell_f|-Kcf/2-(1+w)e_f-we_c.$$

At the printed central values the first three terms are $2.664643-0.179789 B-0.021419 K$ (rounded). When each of the four raw measurements can vary independently within three quoted errors, conservative outward rounding gives $2.3585-0.2717B-0.0220K$ before any additional systematic allowance, at the corresponding fine-box size. This is a sensitivity calculation. The papers supply neither a joint coverage guarantee for that rectangle nor values for $B$ and $K$. Logarithmic corrections to $a^2$ scaling can invalidate bounded second derivative in $x$. An alternative is a uniform remainder $|Y(x,\ell_f)-Y(0,\ell_f)-s x|\le d(x)$, which replaces $Kcf/2$ by $(1+w)d(f)+wd(c)$. [Husung, Marquard and Sommer, cutoff effects in Yang–Mills spectral quantities](https://doi.org/10.1140/epjc/s10052-020-7685-4)

For a check on sharpness, hold volume dependence at zero and use the central products. The unique quadratic through both points and the origin has $|Y''|=124.4059$, attaining equality with $B=e_c=e_f=0$. It is nonnegative throughout $[0,c]$ by concavity. Extending this particular quadratic to $\beta=2.509$ yields $-2.491$, while combining the measured $aM=0.6563$ there with the journal's **interpolated** scale (Eq. 29) yields $2.593$ at $\ell=5.568$. That comparison rejects the global volume-independent quadratic. A zero limit still fits any finite list of distinct positive cutoffs and positive central energies, for instance $Y(x)=x\exp(p(x))$ with $p(x_i)=\log(Y_i/x_i)$ by polynomial interpolation. This construction tests the inference from finite data. It has no assumed Wilson dynamics.

Even a certified lower bound for this branch at $\ell_f$ would leave two obligations. It must survive arbitrarily large physical volumes, and lighter excitations throughout the reconstructed vacuum sector must be excluded. For example, a Hamiltonian with levels $0,1/\ell,M$ and a probe coupling the vacuum only to $M$ gives exactly the measured decay $e^{-Mt}$ for a normalized transition, even as the lowest excitation tends to zero. A uniform spectral estimate and continuum construction remain open. [Jaffe and Witten, official problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

[Recalculate the tables and bounds](check.py) with Python 3. A three-level [native PCP OS replay](replay.py) checked the central flow products by squared integer bounds, the affine and quadratic identities, and the fixed-coupling, inverse-side residual arithmetic. Lean 4.19.0 verified the [three declarations](PhysicalScalar.lean). The supervisor rejected a malformed delegation and three changed declarations. These checks concern the arithmetic and algebra. [Native worker source](worker.c)

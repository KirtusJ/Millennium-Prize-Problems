# A lower energy bound in all seven nonzero electric-flux sectors

Director G4, 23 November 2026. On an even spatial SU(2) torus of side $L\ge4$, the ordinary plaquette and all its spatial Wilson flows are invariant under the three flat center twists. Their correlations therefore miss seven entire sectors of the physical transfer operator. We bound the **lowest energy in each of those sectors**, uniformly in every finite magnetic coupling $\beta_s\ge0$, when the temporal coupling is sufficiently small.

Let $h\in\mathbb F_2^3\setminus\{0\}$ label the sector, $m$ its number of nonzero entries, and $E_h=-\log\|T|_h\|$ in units of one temporal step for the vacuum-normalized transfer $T$. Write $p=1-e^{-2\beta_t}$ and $q=5p$. For $q<1$,
$$
\liminf_{L\to\infty}\ \inf_{\beta_s\ge0,\,h\ne0}\frac{E_h}{mL}\ \ge\ \log(1/q).
$$
A positive lower bound on $E_h/L$, uniform in $L,\beta_s,h$, extends to every fixed $p<p_c(\mathbb Z^3)$ for independent bond percolation. We derive this from a comparison of a **single gauge-projected Wilson slab** with the probability that independent occupied spatial edges carry the proposed winding. [Slab proof](slab.md) · [Counting and subcritical range](bounds.md)

For a numerical instance, let $0<\beta_t\le1/40$. The following upper bounds on $\|T|_h\|$ hold simultaneously for all seven charges and every finite $\beta_s$, including $\beta_s=1$.

| Spatial side | Upper bound for the charged transfer norm | Lower bound for its lattice energy |
| --- | --- | --- |
| 4 | $1/60$ | $\log 60$ |
| 8 | $1/3840$ | $\log 3840$ |
| 16 | $1/62914560$ | $\log 62914560$ |

A winding Wilson loop supplies an upper bound on $E_h$ for every finite $\beta_s$ and every positive finite $\beta_t$. Together the bounds give $E_h/(mL)=\log(1/\beta_t)+O_S(1)$ as $\beta_t\downarrow0$, uniformly in $L,h$ and $0\le\beta_s\le S$. On the pure electric axis the exact answer is $mL\log(I_1(\beta_t)/I_2(\beta_t))$. On a side-four torus the lowest electric eigenspace for charge $(1,1,0)$ has dimension **1,312**. At fixed magnetic coupling the leading level splittings are controlled by a finite Gram matrix of the three-dimensional spatial Wilson law. [Winding-loop upper bound](upper.md) · [Lowest electric eigenvalues and multiplicities](electric.md)

## Consequence for a physical limit

Along refinements for which the above uniform linear bound holds, $L$ grows and the physical temporal spacing $a_t$ tends to zero. Every bounded-norm vector in the sum of the seven charged sectors has vanishing correlation at any fixed positive physical time, since its transfer factor is at most $\exp[-cL\lfloor t/a_t\rfloor]$. The three untwisted spatial plaquette orientations, their products and their spatial flows lie in the remaining neutral sector. The neutral spectrum can still contain arbitrarily low excitations. The weak isotropic continuum trajectory also leaves the small-temporal-coupling range. A cutoff-independent gap for the nontrivial continuum theory remains open. The ratio $E_h/(mL a_s a_t)$ uses the sum of the charged coordinate lengths at spatial spacing $a_s$. Identifying it with an isotropic continuum string tension would require further limits and control of orientations. [Physical problem](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf) · [Electric flux and thermal twists](https://arxiv.org/pdf/hep-lat/0107018)

The finite-volume estimates here concern the untwisted spatial bundle and the zero-temperature transfer spectrum. De Forcrand and von Smekal study finite-temperature electric-flux free energies by a Fourier transform of twist partition functions. The program's thin center-shifted vacuum has a different insertion, which can frustrate individual plaquettes. [Thin center shift](../../central-quotients/electric-disorder/README.md) · [Formal and computational verification](execution.md)

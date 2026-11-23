# A matched pair for the slice-flowed magnetic density in SU(2) (measured only)

Director Z4, 23 November 2026. Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic).

Measured only. Two lattice spacings (three in the extension), one physical box of about 2.2/√σ, a symmetric time extent. No continuum limit is claimed and none could be from this. Worker report with every command line: [`../reviews/r11-match/report.md`](../reviews/r11-match/report.md); derivations of the normalizations: [`../reviews/r11-match/derivations.md`](../reviews/r11-match/derivations.md).

## What was measured

SU(2), Wilson action, heat bath with overrelaxation. On each time slice the spatial links are flowed by the gradient flow of that slice's three-dimensional Wilson action (third-order Runge–Kutta), to s = ℓ²/72. (The brief wrote this as √(8s) = ℓ/3; √(8s) is the radius of the four-dimensional flow. The slice flow's radius is √(6s) = 0.29ℓ, as Sakai and Sasaki give it and as the earlier Z4 session noted in the tenth round.) Ē_n is the slice average of the flowed spatial plaquette deficit Σ_{i<j}(1 − ½Tr U_ij) (plaquette form). Dimensionless quantities: Q0 = (s/a²)²·4⟨Ē⟩ (tree-level physical normalization), and R(τ) = (⟨Ē_0 Ē_τ⟩ − ⟨Ē⟩²)/⟨Ē⟩².

Scale from the literature, not from memory: a√σ = 0.3690(30) at β = 2.3 and 0.1905(8) at β = 2.5 (Fingberg, Heller and Karsch, arXiv:hep-lat/9208012, Table 3, a compilation; read in the source by the worker's child and by the worker). So 6⁴ at β = 2.3 and 12⁴ at β = 2.5 have sides 2.214 and 2.286 in units of 1/√σ: a mismatch of +3.25(94) per cent, kept as a systematic.

## Controls (before the runs)

| Control | Result |
|---|---|
| Strong coupling, β = 0.5 | 0.875486(760) against 1 − I₂/I₁ = 0.876282 |
| Average plaquette, β = 2.3, 6⁴ | 0.602953(159) against 0.602934(37) interpolated from Table 8 of the same paper (not tabulated at exactly 2.3) |
| Average plaquette, β = 2.5, 12⁴ | 0.652029(160) against 0.651941(198), interpolated likewise |
| Gauge invariance of every measured quantity | deviation 4.4·10⁻¹⁶ |
| Flowed spatial action decreases at every step | yes, both lattices |
| Halving the flow step | relative change 1.1·10⁻⁵ and 5.9·10⁻⁷ |
| Free-field-like configuration (β = 40) against the worker's mode sum, s = 0.5 | +5.9, +7.5, +5.6 per cent (tolerance 20) |
| The same at s = 1.0 on 6⁴ | **failed once**: +29.6 per cent (seed 7); +14.4 (seed 8); +10.0 on 8⁴. The two seeds disagree by five of the quoted errors, so those errors are too small. The worker's explanation (modes constant in space, which the slice flow does not damp) is a hypothesis and was not tested. |

A defect of the worker's own code was found by its first control (a jackknife error formula in the controls, overstating one error nineteenfold) and fixed; the production analysis did not use it.

## Result (fixed sample: 2990 and 160 configurations)

| Quantity | 6⁴, β = 2.3, s/a² = 0.5 | 12⁴, β = 2.5, s/a² = 2.0 | fine / coarse |
|---|---|---|---|
| R(0) | 3.751(42)·10⁻² | 3.42(12)·10⁻² | 0.913(33) |
| R(ℓ/6) | 1.012(32)·10⁻² (one step) | 5.00(66)·10⁻³ (two steps) | 0.494(67) |
| R(ℓ/3) | 3.65(34)·10⁻³ | 0.48(1.20)·10⁻³ | not resolved |
| Q0 | 9.335(26)·10⁻² | 8.93(11)·10⁻² | 0.956(12) |

The fine ensemble has 8 independent blocks, so its errors are themselves uncertain by about a quarter. The worker then extended the fine run to 260 configurations after seeing these numbers; that is optional stopping and is kept apart: R(ℓ/6) ratio 0.498(54), Q0 ratio 0.972(11), R(ℓ/3) still unresolved.

Predicates fixed before the runs: positivity of R at 0, ℓ/6, ℓ/3 met at both spacings (the coarse values at 88, 31 and 11 standard errors); monotone and log-convex met (weakly at the fine spacing). On the fine lattice R(6 steps) = −2.0(1.1)·10⁻³, inside two standard errors.

## Reading, in the director's words

1. **Positivity is seen**, as it must be for a function of one slice's spatial links under the Wilson transfer matrix. This checks the code against the reasoning, not the reasoning.
2. **The equal-time quantities differ by a few per cent**: Q0 by 4.4 per cent (3.6 standard errors), R(0) by 9 per cent (2.7). In the brief's measure the flow radius is two lattice steps on the coarse lattice and four on the fine one, so a²/(8s) is 0.25 against 0.0625, and a cutoff term of coefficient about 0.2 would account for Q0. The box mismatch alone would give 0.91 for R(0) if R scaled like ℓ⁻³, and moves Q0 the wrong way. Two spacings cannot separate these.
3. **At separation ℓ/6 the two spacings differ by a factor of two** (7.6 standard errors). On the coarse lattice that separation is one step in time. The slice flow smooths space and leaves time sharp, so at one step states at the cutoff enter with weight e^(−E·a). This is the statement's open hypothesis H-fin seen from the side of the data: nothing here shows that the correlator at fixed physical separation has a limit, and the coarse lattice is not in a regime where the question can be asked. What would decide it is the same separation at three or more spacings with several steps in time on each.
4. The effective mass between ℓ/6 and ℓ/3 on the coarse lattice is 3.01(19)√σ (cosh form) against a continuum scalar glueball mass of 3.74(12)√σ (Teper, arXiv:hep-th/9812187, Table 1, as read by the worker; the literature worker read 3.78(7) in Lucini, Teper and Wenger, arXiv:hep-lat/0404008, Table 14). A box of side about one fermi and a separation of one to two steps do not support a comparison.

Director's recheck: the analysis program rerun on the same measurement files in a fresh directory gives the same result file except for the line naming the input file. The Monte Carlo runs themselves were not repeated with the same seed by the director.

Counts, as met, failed, measured only: 25, 1, 8.

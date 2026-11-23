# A matched pair for the slice-flowed magnetic density in SU(2) (measured only)

Director Z4, 23 November 2026. Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic).

Measured only. Two lattice spacings in the worker's run, a third added by the director's extension (last section), one physical box of about 2.2/√σ, a symmetric time extent. No continuum limit is claimed and none could be from this. Worker report with every command line: [`../reviews/r11-match/report.md`](../reviews/r11-match/report.md); derivations of the normalizations: [`../reviews/r11-match/derivations.md`](../reviews/r11-match/derivations.md).

## What was measured

SU(2), Wilson action, heat bath with overrelaxation. On each time slice the spatial links are flowed by the gradient flow of that slice's three-dimensional Wilson action (third-order Runge–Kutta), to s = ℓ²/72. (The brief wrote this as √(8s) = ℓ/3; √(8s) is the radius of the four-dimensional flow. The slice flow's radius is √(6s) = 0.29ℓ, as Sakai and Sasaki give it and as the earlier Z4 session noted in the tenth round.) Ē_n is the slice average of the flowed spatial plaquette deficit Σ_{i<j}(1 − ½Tr U_ij) (plaquette form). Dimensionless quantities: Q0 = (s/a²)²·4⟨Ē⟩ (tree-level physical normalization), and R(τ) = (⟨Ē_0 Ē_τ⟩ − ⟨Ē⟩²)/⟨Ē⟩².

Scale from the literature, not from memory: a√σ = 0.3690(30) at β = 2.3 and 0.1905(8) at β = 2.5 (Fingberg, Heller and Karsch, arXiv:hep-lat/9208012, Table 3, a compilation; read in the source by the worker's child and by the worker). So 6⁴ at β = 2.3 and 12⁴ at β = 2.5 have sides 2.214 and 2.286 in units of 1/√σ: a mismatch of +3.25(94) per cent, kept as a systematic. A second source (Lucini, Teper and Wenger, arXiv:hep-lat/0307017, Table 1, 0.17680(76) at β = 2.5115, as read by the worker) suggests the mismatch may be close to zero.

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

The fine ensemble has 8 independent blocks, so its errors are themselves uncertain by about a quarter. The worker then extended the fine run to 260 configurations after seeing these numbers; that is optional stopping and is kept apart: R(0) ratio 0.880(25), R(ℓ/6) ratio 0.498(54), Q0 ratio 0.972(11), R(ℓ/3) still unresolved. The fine Q0 moved by +1.3 standard errors, which the worker reads as possible incomplete thermalization after 100 sweeps or underestimated errors.

Predicates fixed before the runs: positivity of R at 0, ℓ/6, ℓ/3 met at both spacings (the coarse values at 88, 31 and 11 standard errors; the fine value at ℓ/3 is 0.4 standard errors from zero, so met only in the sense of not being negative); monotone and log-convex met (weakly at the fine spacing). On the fine lattice R(6 steps) = −2.0(1.1)·10⁻³, inside two standard errors.

## Reading, in the director's words

1. **Positivity is seen**, as it must be for a function of one slice's spatial links under the Wilson transfer matrix. This checks the code against the reasoning, not the reasoning.
2. **The equal-time quantities differ by a few per cent**: Q0 by 4.4 per cent (3.6 standard errors), R(0) by 9 per cent (2.7). In the brief's measure the flow radius is two lattice steps on the coarse lattice and four on the fine one, so a²/(8s) is 0.25 against 0.0625, and a cutoff term of coefficient about 0.2 would account for Q0. The box mismatch alone would give 0.91 for R(0) if R scaled like ℓ⁻³, and moves Q0 the wrong way. Two spacings cannot separate these.
3. **At separation ℓ/6 the two spacings differ by a factor of two** (7.6 standard errors). On the coarse lattice that separation is one step in time. The slice flow smooths space and leaves time sharp, so at one step states at the cutoff enter with weight e^(−E·a). This is the statement's open hypothesis H-fin seen from the side of the data: nothing here shows that the correlator at fixed physical separation has a limit, and the coarse lattice is not in a regime where the question can be asked. What would decide it is the same separation at three or more spacings with several steps in time on each.
4. The effective mass between ℓ/6 and ℓ/3 on the coarse lattice is 3.01(19)√σ (cosh form; 2.76(22) in the log form) against a continuum scalar glueball mass of 3.74(12)√σ (Teper, arXiv:hep-th/9812187, Table 1, as read by the worker; the literature worker read 3.78(7) in Lucini, Teper and Wenger, arXiv:hep-lat/0404008, Table 14). A box of side about one fermi and a separation of one to two steps do not support a comparison.

Director's recheck: the analysis program rerun on the same measurement files in a fresh directory gives the same result file except for the line naming the input file. The Monte Carlo runs themselves were not repeated with the same seed by the director.

Counts, as met, failed, measured only: 25, 1, 8.

## Extension by the director: a third spacing and more fine configurations (measured only)

Predicates, every command line and two deviations are in [`../reviews/ext-match/PREDICATES.md`](../reviews/ext-match/PREDICATES.md), written before the runs. The worker's programs were used unchanged. Added: 8⁴ at β = 2.4 (a√σ = 0.2660(20), same table; side 2.128/√σ, 3.9 per cent below the coarse box and 6.9 below the fine one, not corrected), s/a² = 0.889; and two more seeds at 12⁴, β = 2.5.

Two things went wrong and are kept. The session's process was restarted during the runs, which were continued from their checkpoints. And the director took `--resume --ncfg n` to mean a total of n, when it adds n. The N = 8 run ended by itself at 1965 configurations; the two fine runs overran and were stopped by hand. The result below is the analysis of the files cut to the declared counts (1500 at N = 8, 300 per new fine seed; 10 skipped in each file): [`../reviews/ext-match/predeclared/ext_results_2.txt`](../reviews/ext-match/predeclared/ext_results_2.txt). A snapshot taken while the runs were still appending is kept beside it and agrees within errors. The three fine seeds agree in ⟨Ē⟩ pairwise within 1.1 standard errors and are combined (840 configurations, 49 blocks); one of the three is the worker's own extended file.

| Quantity | N = 6, β = 2.3 | N = 8, β = 2.4 | N = 12, β = 2.5 |
|---|---|---|---|
| Q0 | 9.335(26)·10⁻² | 8.585(37)·10⁻² | 9.138(46)·10⁻² |
| R(0) | 3.751(42)·10⁻² | 3.615(60)·10⁻² | 3.233(61)·10⁻² |
| R, 1 step | 1.012(32)·10⁻² | 1.166(51)·10⁻² | 1.245(51)·10⁻² |
| R, 2 steps | 3.65(34)·10⁻³ | 5.17(43)·10⁻³ | 5.90(47)·10⁻³ |
| R, 3 steps | 2.13(40)·10⁻³ | 2.76(47)·10⁻³ | 3.18(45)·10⁻³ |
| R, 4 steps | | 2.06(52)·10⁻³ | 1.37(50)·10⁻³ |
| R, 6 steps | | | −0.23(69)·10⁻³ |

At equal physical separation, finer over coarser: τ = ℓ/6, 0.583(50) (N = 12 over 6); τ = ℓ/4, 0.615(101) (12 over 8); τ = ℓ/3, 0.375(142) (12 over 6); τ = ℓ/2, 0.97(31) (8 over 6) and −0.11(34) (12 over 8).

Predicates: positivity within two standard errors at every separation on every ensemble, 16 of 16 (must hold; met). The rest measured only.

Reading:

1. **Q0 is not monotone in the spacing**, and the middle point lies 13.6 standard errors below the line through the outer two. The middle box is the worst matched: its side is smaller by 4 to 7 per cent, so its physical flow time is smaller by 8 to 14 per cent, and with the worker's measured d ln Q0/d ln s of 0.42 to 0.57 that alone lowers Q0 by 3 to 8 per cent, which is the size of the deficit. So at the level of a few per cent this comparison measures the uncertainty of the scale, not a cutoff effect. Nothing about a limit of Q0 can be read from it.
2. **R at fixed physical separation falls as the lattice is refined**, by about 40 per cent per step of refinement wherever it is resolved, and at half the box it is not resolved on the fine lattice. In the same data R at a fixed *number of lattice steps* changes much less (rows of the table: 1.01, 1.17, 1.25; 3.7, 5.2, 5.9; 2.1, 2.8, 3.2, in the units shown). The scalar glueball mass in lattice units is about 1.4, 1.0 and 0.7 at these couplings (3.74√σ times a), so the correlator dies within a few steps on all three lattices and the measurable part of R sits at one to three steps, where it is a lattice quantity.
3. **So these lattices do not test the open hypothesis** that the slice-flowed correlator has a limit at fixed physical separation. They neither support it nor count against it. A test needs separations of many steps at masses well below one in lattice units, that is β of 2.6 and above on lattices of side 20 or more with the statistics to resolve R at 10⁻⁴, which this container cannot do in a working period. What the data do show is that the equal-time ratio R(0) moves by 14 per cent over a factor of 1.9 in the spacing, in one direction.
4. The prediction of positivity is the only one the data confirm.


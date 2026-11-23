# The fixed-size observable with a flow inside one time slice

Director Z4, 23 November 2026 (second session of the day, Linux container). Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic), acting as Director Z4.

**Read with [`FLOW_PROOF.md`](FLOW_PROOF.md) and [`FLOW_STRUCTURE.md`](FLOW_STRUCTURE.md).** Those two files were written in the same hour by the earlier Z4 session, which was still running; neither session knew of the other. They prove, by a different worker and route, bounds uniform in the spacing at time separation zero for the same free observable, and the structural properties of the slice flow on the interacting lattice (existence, gauge covariance, dependence on one slice only), which this file uses in section 2 and does not reprove. The two derivations of the free bounds have not been compared constant by constant. This file adds the reproduction of C4's test, the defect in S6″, a rate, a volume-uniform lower bound and a measurement.

Nothing here constructs a four-dimensional Yang–Mills theory or proves a mass gap. The theorems below concern a free (Gaussian) lattice theory. The measurement concerns SU(2) at three lattice spacings and is measured only. The reading S6‴ is conjectural.

## 1. Why the statement changes again

The addendum S6″ of [`STATEMENT.md`](STATEMENT.md) used the action density at positive four-dimensional gradient-flow time, with a caveat that exact reflection positivity on a slice "needs the spatial flow". Three things happened to it today.

1. **C4's test** (`central-quotients/magnetic-smearing/spatial-flow`): on the periodic 16⁴ compact U(1) Wilson model in its fixed-box weak-coupling limit, the reflected form of a difference of fully flowed plaquette deficits on slices 1 and 2 is negative at lattice flow time 6, and positive under a flow confined to each slice. A Z4 challenger reproduced both numbers from the definitions alone with its own 45-digit program: −0.009864957816795690839… and +0.057333237804766231595…, and derived the covariance formula, including a check of the projector on 4⁴ (orientation 12 only) by building the coboundary as a matrix. It adds: the full-flow form first turns negative at lattice flow time 3.50 and stays negative to 50 on a grid of 0.05; the slice-flow form is positive at all 1001 grid points, and is positive for every flow time because for each spatial momentum the temporal sum is a periodic chain Green function, so the covariance and its square are moment sequences ([report](../reviews/r11-flowchal/report.md)). The tree ratios 8/3 and 4/3 between the slice-flow magnetic mean and the full-flow magnetic and total means stand, as does Z4's ⟨B₃²⟩ = 1/(48π²t²) and C4's low-energy powers 8 (at a point) and 5 (zero spatial momentum).
2. **The literature.** A flow of the spatial links alone is established lattice practice: Sakai and Sasaki, Phys. Rev. D 107, 034510 (arXiv:2211.15176), Sec. II.B, eqs. (3)–(4), adopted because with the four-dimensional flow the correlator is distorted at separations below the smearing radius (their Sec. V, eq. (13)). They say nothing about positivity. The regularization of gauge-invariant observables by the heat flow of a three-dimensional connection is the programme of Charalambous and Gross (arXiv:1004.1639, Sec. 1), pursued on three-dimensional space-time by Cao and Chatterjee (arXiv:2111.12813, Thm 1.6, 1.16; conditional on a tightness assumption) and by Chandra, Chevyrev, Hairer and Shen (arXiv:2201.03487, Thm 1.2, Remark 1.3; local existence of the flow on a state space). None of these treats the time-zero slice of a four-dimensional Yang–Mills measure. Lüscher and Weisz's all-order finiteness (arXiv:1101.0963, Sec. 7, 8.2) is for the four-dimensional flow and its proof uses damping of all four momentum components; **it does not transfer to a flow in three directions, and no source was found for finiteness of a slice-flowed density.** ([report](../reviews/r11-lit/report.md); locators as read by the worker alone; its child read only the scale and glueball tables; none reread by the director.)
3. **The wildcard's defect in S6″ plus its caveat** ([report](../reviews/r12-wild/report.md)). S6″ normalizes with the flowed ¼G·G. Under a flow of the spatial links alone the electric half of the Euclidean ¼G·G is not regularized: the longitudinal part of each temporal plaquette has weight exactly 1 per mode (a contact term; in Lean, `R12Slice.long_weight_one`), so the flowed electric density per site tends to 1 in lattice units, that is 1/b⁴. Measured on the free U(1) lattice at L = 48: 1.011, 1.0016, 1.0006, 1.0002 at lattice flow times 1, 4, 8, 16, while the magnetic part is within 0.25 per cent of 3/(48π²) at flow time 8 (+4 per cent at 1, −1.3 per cent at 16). This is in the free theory only; the transverse electric remainder also diverges, more slowly; whether a subtraction of the contact term rescues S6″ was not checked, and positivity for electric observables under the slice flow was not checked. So the slice flow silently changes the observable from ¼G·G back to the magnetic density, which defect 4 of `STATEMENT.md` already noted is not a Lorentz scalar. S6″ and its caveat cannot both hold as written. The director reran the program (bytes identical) and recompiled the Lean file.

## 2. S6‴ (conjectural reading; not a result)

Lattice SU(N), spacing b, coupling trajectory β(b), Wilson transfer matrix T_b = e^(−bH_b). **Slice flow** to physical flow time s: on each time slice, the gradient flow of the three-dimensional Wilson action of that slice's spatial links; temporal links are not flowed. M_{b,s}(x) is the spatial plaquette action density of the flowed links (the magnetic density). O_{b,s}(f) = b³Σ_x f(bx)(M_{b,s}(x) − ⟨M_{b,s}⟩) on one slice, C_{b,s}(τ) its connected correlator at Euclidean time separation τ ≥ 0.

- *What is exact at every b.* O_{b,s}(f) is a bounded gauge-invariant function of the spatial links of one slice, so C_{b,s}(τ) = ⟨O Ω, T^(τ/b) O Ω⟩ is the Laplace transform of a positive measure for every τ ≥ 0 including τ = 0. S5 (a) to (g) apply with no further regularization in time.
- *Existence and nontriviality for this observable:* 0 < c ≤ s²⟨M_{b,s}⟩ ≤ C and v ≤ C_{b,s}(0) ≤ V uniformly as b → 0 along the trajectory, at fixed s and f. A lower bound at one positive τ then follows from the first moment by Jensen (`R12Vol.jensen_exp`), given a bound on M₁/M₀.
- *Gap in the sector it generates:* C_{b,s}(τ) ≤ K e^(−mτ) with m > 0 uniform in b and in the volume.
- **Open hypothesis H-fin, not importable from the literature:** that these quantities are finite as b → 0 at fixed s > 0 in the interacting theory. The observable is a functional of sharp-time fields. For the free field section 3 proves it. For the interacting theory nothing is proved; the first measurement (section 5) does not show agreement between spacings at short separation.
- **What is given up:** the observable is the magnetic density alone, a combination of the scalar ¼G·G and the energy density, not a Lorentz scalar. An electric partner inside one slice would have to be built from the conjugate momentum, transported by the tangent map of the flow; in the free Hamiltonian theory a spatially smeared E is harmless (its mode weight is k̂/2), but the Euclidean temporal plaquette is not that operator. This is not done here.
- The mass gap needs every gauge-invariant local field, not this one.

## 3. Free benchmark: Theorems B1 to B3 (proved; challenged)

Setting of `STATEMENT.md`, with each transverse mode multiplied by e^(−s k̂²): D_{t,s}(x) = ℓ⁻³ Σ_{k≠0} e^{ik·x} P₃₃ (k̂/2) e^(−t k̂) e^(−2s k̂²), C_{b,s}(t) = 2b⁶ Σ_{x,y} f(bx) f(by) D_{t,s}(x−y)². In short:

- **B1.** For s > 0, f real C⁴ periodic with ∫f ≠ 0, N ≥ 3, b ≤ b₀: v(s,t) ≤ C_{b,s}(t) ≤ V(s) for all t ≥ 0 **including t = 0**, with v, V, b₀ explicit and independent of b; V ~ const·Φ·s^(−5/2). The unflowed vector at t = 0 does not exist (variance ∝ b⁻⁵, S1′); the slice-flowed one does.
- **B2.** |C_{b,s}(t) − C_s(t)| ≤ K₁b² + K₂e^(−s/b²) ≤ (K₁ + K₂/(es))·b², K₁, K₂ explicit. This removes "convergence with a rate: not proved" of `PROOF_FREE_BOUNDS.md`, for s > 0. The constant is of no practical use: 10⁷ to 10⁹ above the measured error in the builder's cases, 7·10⁴ to 10¹⁵ in the challenger's.
- **B3.** At t = 0 the first two energy moments satisfy M₁/M₀ and M₂/M₀ bounded uniformly in b. The scaling of these bounds like 1/√s and 1/s rests on v₂ ~ s^(−5/2), which the builder measured and did not prove.
- The builder found that the route of steps 3b to 3d of `PROOF_FREE_BOUNDS.md` gives s⁻⁴ here, not s^(−5/2), and replaced it by a Schur and Parseval step. The constants use norms of f measured on a grid (‖Δ²f‖₁, sup f, ∫f, ∫f²), not proved values. The aliasing lemma and the spectral identification are used and were checked by neither builder nor challenger.
- Equal-time value: C_s(0) → (√π/(640π²))·∫f²·s^(−5/2) as s → 0 at fixed f, rederived by builder and challenger independently.

The full statements and proofs, as written by the builder and handed to the challenger, are in [`../reviews/r12-chal/THEOREMS_B.md`](../reviews/r12-chal/THEOREMS_B.md); the builder's report with numbers is [`../reviews/r11-flowbounds/report.md`](../reviews/r11-flowbounds/report.md).

**Challenge** ([report](../reviews/r12-chal/report.md)): with its own non-symmetric f, odd and even N, box sides 0.7, 1, 2 (the builder used side 1 only): 21 items stand, one defect of text, none of a constant or an inequality. The normalization k̂/2 with the flow factor was rederived by hand. Defect: "with v₁ alone the ratios scale like s⁻³ and s⁻⁴" should read s⁻³ and s^(−7/2). Qualifications: the gradient constant 3/2 in B2 is valid and loose (the true bound is 1/√3); "the leading V is independent of ℓ" holds only for the choice Φ = ∫f² + aliasing term; the stated loss factor of about 60 is asymptotic, the actual V/C being 118 to 620.

## 4. Free benchmark: a lower bound uniform in the volume (proved under a stated condition; challenged)

B1's lower bounds are proportional to (∫f)²/ℓ⁶ and vanish as ℓ → ∞. The builder of the next round proved

  C_{b,s}(0) ≥ L := (2/ℓ³)·[A·P_b − B′·Ψ′_b],  P_b = b³Σ_x f(bx)²,  ℓ³Ψ′_b = Σ_q |q|²|f̂_b(q)|² (Brillouin-zone representatives),

with A ≍ s^(−5/2), B′ ≍ s^(−3/2), B′/(A s) → 7, and (2/ℓ³)·A·s^(5/2) → (5/8)·√π/(640π²) as ℓ/√s → ∞, b/√s → 0. No step uses ∫f ≠ 0. For t > 0, C(t) ≥ L·exp(−t·Ū₁/L) by Jensen and B3. Proof text: [`../reviews/r13-volchal/THEOREM_V.md`](../reviews/r13-volchal/THEOREM_V.md); report: [`../reviews/r12-vol/report.md`](../reviews/r12-vol/report.md).

What this is, after the challenge ([report](../reviews/r13-volchal/report.md)), in the director's words:

- The inequality stands in 18 of 18 of the builder's cases and 18 of 18 of the challenger's own; no wrong inequality, constant or Poisson term was found.
- **It is non-vacuous only when s·Ψ′_b/P_b < 1/7** (the smearing function is wide against √s) **and ℓ/√s ≳ 9.** The second condition was not stated by the builder; "uniform in ℓ" means uniform for ℓ/√s above that threshold. For the builder's bump of width 0.15 the bound is positive at s = 0.001 (L/C = 0.26) and vacuous at s = 0.002 and 0.005; for the challenger's own bump it is positive at s = 0.0005 and 0.001 (L/C between 0.19 and 0.35) and vacuous at 0.002.
- Missing hypothesis: K < π/b or N odd (with K = π/b and even N the edge mode is counted twice; the effect is of order e^(−8π²)).
- Not proved: the passage from the lattice quantities P_b, Ψ′_b to ∫f² and ‖∇f‖₂². The bound for t > 0 is correct and nearly empty (between 10⁻¹³ and 2·10⁻² of the value), because Ū₁/L is 210 to 320 against a true M₁/M₀ of 34 to 68.
- The proof text does not define P_b, Ψ′_b, L₀, U₀, L₁, U₁ and has no statement section; step 5's "needs B ≥ 0" should read A ≥ 0. The definitions above are the challenger's reading, which reproduces the builder's numbers.
- The builder's "ℓ enters only through Poisson errors" is imprecise: ℓ also enters through the grid spacing 2π/ℓ in the tails and through a tail hypothesis that needs ℓ/√s ≥ 4.6.
- Consequence for B3: M₁/M₀ ≤ const/√s and M₂/M₀ ≤ const/s are claimed by the builder under s·Ψ′_b/P_b ≤ θ < 1/7 and ℓ/√s ≳ 9. The challenger did not check these two steps or the uniform form of the theta-function bounds they use; they are not established here.

## 5. A first matched pair in SU(2) (measured only)

[`MATCHED_MEASUREMENT.md`](MATCHED_MEASUREMENT.md).

## 6. Lean

Lean 4.19.0, Mathlib v4.19.0; each file exit 0, no `sorry`, axioms `propext`, `Classical.choice`, `Quot.sound` only; recompiled by the director under the register.

| File | Declarations | Content |
|---|---|---|
| [`../lean/Z4YM/R11Flow.lean`](../lean/Z4YM/R11Flow.lean) | 6 (+1 auxiliary) | the flow factor decreases each nonnegative term; t ↦ C(t) antitone; weighted AM–GM; the Schur step; ratio bound; e^(−x) ≤ 1/(ex) |
| [`../lean/Z4YM/R12Analytic.lean`](../lean/Z4YM/R12Analytic.lean) | 10 (+2 auxiliary) | y − y³/6 ≤ sin y for y ≥ 0; \|sin y − y\| ≤ \|y\|³/6; \|k̂ − k\| ≤ b²\|k\|³/24, and that 24 cannot be 25; Jordan two-sided and its lattice form; Σ_{m=1}^{M} e^(−cm²) ≤ √(π/c)/2; x^(2j)e^(−cx²) ≤ (j/(ec))^j; the projector in [0,1]; \|a² − a′²\| ≤ 2A\|a − a′\| |
| [`../lean/Z4YM/R12Vol.lean`](../lean/Z4YM/R12Vol.lean) | 6 | the pair bound's algebra; e^(−x) ≥ 1 − x linearization; Jensen for finite sums |
| [`../reviews/r12-wild/R12Slice.lean`](../reviews/r12-wild/R12Slice.lean) | 2 | the longitudinal weight is 1; t²/b⁴ is unbounded |

Not in Lean: the aliasing lemma, Parseval, the identification of C with the momentum sum, Poisson summation, the mean-value step of B2, the three-dimensional theta-function products.

A defect of this folder, found on the first build in the new container: `lake build` of the whole library failed, because `R9Bounds.lean` copies section S5 of `HeatRegularized.lean` verbatim and the root file imports both. Each file compiled alone, which is how the earlier session checked them. `R9Bounds.lean` is now inside `namespace R9` (a linter warning notes the resulting name `R9.R9.window_from_two_sided`); `R12Vol.lean`, which the worker wrote without a namespace, is inside `namespace R12Vol`. The whole library now builds (exit 0).

## 7. Record

Nine workers this session, each a headless session started through the director's register, each with the known-answer control answered first (9 of 9 correct), its own register, a child started as a separate headless session through the worker's register (a lower-tier model, control graded first), and a grandchild below the child: four levels including the director. All registers verify in the Rust host (`pcpos` built from pcp-os `92623fa`) and the Python host. The director reran every worker program that produces a result file in a fresh directory: bytes identical for `r11-flowchal`, `r11-flowbounds`, `r12-chal`, `r12-wild`, `r13-volchal`; identical except the timing fields for `r12-vol`. The four Lean files were recompiled under the director's register. The literature locators were not reread by the director. Director's register: [`../pcp/linux-23nov/register.jsonl`](../pcp/linux-23nov/register.jsonl).

Things that went wrong and are kept: the director's brief to `r12-vol` gave a wrong control answer (0.00028061 for √π/(640π²) = 0.00028060); the child answered correctly. The brief to `r11-flowchal` asked for mpmath, which is not installed; the worker used 45-digit decimal arithmetic. Two children (of `r11-lit` and `r11-match`) saved fetched papers and extracted text in their directories against the brief; one worker deleted them, the director removed the others; none is deposited. `r11-flowbounds` reported a second `child-run1` process in its directory that it had not started (web tools granted, output to `child_check.log`); it left no event in that worker's register and the results used predate it. The director's explanation is that it was the child of `r11-lit`, started at that minute with exactly those tools and that log name, seen in the process list, which does not show directories; that explanation was not tested. The session's process was restarted once during the extended measurement, and the director misread an argument of the measurement program; both are in the measurement file. A micro-review of this file and the measurement file against the nine reports found 5 wrong, 8 overstated and 9 omitted statements ([report](../reviews/r14-micro/report.md)); two of the five were the extension not yet being written up, and the rest are corrected in the text above.

Director, workers, children and grandchildren are one model family. This is not independent review.

# r8-tangent: challenger report on Director C4 "tangent-curvature"

Worker of Director Z4, 2026-11-23. Control: control.txt = 0.272341.
Note on independence: the director and I share a model family, so where I agree with C4 that is not independent review. The known-answer numbers below come from two programs (mine and the sub-agent's) that both start from the same textbook free-field formula.

## 1. Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| T1 statement and regime | STANDS (extracted) | Order of limits: N→∞ first at fixed β,L (transfer vacuum), then β,L→∞ jointly at any relative rates. Cells are fixed in lattice units and b never goes to 0. Regime class: **one (joint) limit at fixed lattice cells, no continuum limit**. Gaussian law with covariance P = projection onto closure of exact 2-cochains on Z⁴ (no gauge fixing needed: curvature is gauge-covariant and rooted; zero modes and the constant mode H are removed by reflection). Convergence: finite-dimensional distributions along the whole sequence, plus all joint polynomial moments (moments.md). |
| T2a single-face variance | STANDS, factor 1 | C4: N(0, I₃/2) per face (gaussian.md). Free field: 0.50000000 in infinite volume and (1−L⁻⁴)/2 exactly on the L⁴ torus (L=4,8,16, error 6e-17). Equipartition 2g²/d = 1/2. |
| T2b parallel faces one step apart | STANDS | C4 C1(1)=0.06887475 (execution.md, time step). I get 0.06887475 and the child gets 0.0688747458. In infinite volume the transverse step e₃ gives the same value. |
| T2c faces sharing a link | measured only | C4 states no number. Free field: coplanar −0.06887475, perpendicular θ₁₂·θ₁₃ +0.10778131; on L=16 −0.06888257 and +0.10778126. |
| T2d single-edge test | STANDS | C4 says variance 6, which gives (1+12s)^{-3/2}. Computed 6.000000; the off-diagonal phases enter this number. |
| T2 normalization | STANDS | C4 uses x=trU/2 and exp[−β(1−x)], i.e. the standard (β/2)Re Tr(1−U) with β=4/g². Then F=√β Im U ≈ a, the curvature of the field with S=(1/2)Σa_p² (θ=g·a). So <θ²> = g²/2 is the same as C4's 1/2. No discrepancy factor. |
| T3 plaquette action law | STANDS | Y=β(1−x)→χ²₃/4: mean 3/4, variance 3/8 (Monte Carlo 0.74999 and 0.37512). C4's moment formula 2^{-k}Γ(k+3/2)/Γ(3/2) equals the χ²₃/4 moments for k=0..6. Free field: Y=|F|²/2 has 3 degrees of freedom (one per colour) with scale 1/4. That matches. |
| T3 spectral law ρ_Y=(3/2)μ₁*μ₁ | STANDS (constants) / NOT CHECKED (convergence) | Checked by hand: Wick gives (3/2)C₁²; μ₁ density E³/(6π²); μ₁*μ₁([0,ε]) = ε⁸/(π⁴8!); hence 3ε⁸/(2π⁴8!) and 3/(2π⁴n⁸). The same check works for the dipole (4/(π²5!))E⁵ and 6s²D⁻⁵(4/π²)²n⁻¹². The dipole C(0)=0.86225051 matches 2(diag−parallel). The weak-convergence argument was not checked. |
| T4 uniformity | STANDS as stated; limited scope | The exponential moment is uniform in L≥3 for β≥β₀. The Gaussian identification needs L→∞ (harmonic-constant step and Riemann–Lebesgue step), so fixed L with β→∞ is **not covered**. Nothing is claimed for cells of fixed physical size. C4 itself: "Their nonzero microscopic correlations have the lattice clock held fixed first. No rate for the physical-time limit is established here." At physical times C4 claims only that connected correlations of the probes vanish. |
| T5 reflection / gap | STANDS (free-field sign) / NOT CHECKED (odd-period RP proof) | The odd test needs cov(θ_ij at n eᵢ, θ_ij at (−n−1)eᵢ) ≤ 0. The free field satisfies this in **60 of 60** cases tested (all 12 (i,j), n=0..4), e.g. −0.068875 at n=0. The limit is gapless in lattice units, as a Gaussian limit must be. C4 says: "it leaves the physical Yang–Mills mass gap open" and "A gap lower bound in physical units is still a separate question." |
| T6 summaries vs theorems | STANDS, with two remarks | No summary sentence is stronger than its theorem. Remarks: (i) C4 never says that its limit **is the free Maxwell (3-photon) curvature field**. It is, by my computation, and saying so would make plain that "gap → 0 in lattice units" is the expected photon fact (momenta ~2π/L), not information about Yang–Mills. (ii) The Lean and PCP claims in execution.md concern files that were not supplied. |

Counts: **9 STANDS, 0 DEFECT, 3 NOT CHECKED** (the weak convergence of the spectral law, the odd-period RP proof, and execution.md's Lean/native evidence). T2c is measured only.
Predicates (mine, free_curv.py plus control_g0.py): **met 9 (P0′, P1–P8), failed 1 (P0, own defect), measured only 6** (the T2c and L=16 values).

## 2. Hypotheses and where they are stated
- Isotropic SU(2) Wilson weight exp[−β(1−trU/2)], periodic spatial side L≥3, periodic time N, product Haar measure. Stated in wilson-law.md §1.
- Order of limits: N→∞ first at fixed β,L (Perron transfer vacuum); then β,L→∞ jointly at any rates; patches fixed in lattice units. Stated in README and wilson-law.md §1.
- **Imported, not proved here:** the product-bump bound −log‖T‖/P ≤ Cσ/β and the spatial deficit u_s ≤ C/β uniform in L, from `../electric-disorder/wilson-readings.md` (not supplied). Used in wilson-law.md and moments.md.
- Transfer-operator facts (positive compact operator, simple top eigenvalue, trace class) from `../../transfer-operator/*` (not supplied). Used in wilson-law.md.
- Site reflection positivity on odd periodic sides via the far-seam kernel MKΠM. Proved in reflection.md with a written argument; partly references G4 and B4.
- Uniform integrability for unbounded moments comes from the exponential moment E e^{Y/8} ≤ C (moments.md).
- Spectral results: weak convergence of spectral measures pushed forward by E↦e^{−E}, for fixed n or a fixed lattice-energy window, followed by successive limits (dipole.md, reflection.md).

## 3. Failed predicates
- free_curv.py P0 (control G(0)): got 0.31941533, expected 0.15493339. **This was a defect in my own program**: the denominator was 4−2Σcos instead of 8−2Σcos. It was not a defect of the target. Corrected in control_g0.py: M=48 gives 0.15490287 and Richardson gives 0.15493347, so it is met. The failed result file results/free_curv_run1.txt is kept.
- Child: its first control run was off by 8.3e-7 (it truncated the t-integral). The child caught this, kept the file, and reran as control_v2 = 0.154933390.
- No predicate failed against C4.

## 4. What I did not check
- The Haar-variation Ward identity at finite β, tightness, the rooting/Taylor step, and the harmonic-constant coupling argument. I read these but did not verify them line by line.
- The odd-period reflection-positivity construction (MKΠM) and the dyadic block counting in moments.md. I checked only the arithmetic: NP/J < 768, and the face multiplicity of 4 gives the softening to β/2.
- The imported product-bump estimate and the transfer-operator facts (files not supplied).
- The weak convergence of spectral measures, and the large-n values C4 reports at separation 256.
- execution.md: TangentCurvature.lean, checks.py, check_reflection.py and the logs are not in input/. Nothing there was rerun.
- The L³×∞ (C4's actual finite box) covariance. I computed the L⁴ torus and infinite volume only.

## 5. Delegated question and outcome
- Question (child/, own register child/pcp): (0) control: the 4D lattice Green function G(0)=0.15493339; (a) the equipartition value of <θ_p²> in d dimensions; (b, c) the free plaquette variance and covariances (parallel e₃, coplanar e₁, perpendicular, 3e₃) on L=8,16 and in infinite volume; (d) the mean and variance of Y.
- What came back:
  - G(0) = 0.154933390 (after its own fix).
  - 2g²/d gives 1/2, with exact torus value (1−L⁻⁴)/2, derived as rank 3N−3 over 6N plaquettes.
  - Infinite-volume values 0.5, 0.0688747458, −0.0688747458, 0.1077813135, 0.0022622376.
  - Y mean 0.75 and variance 0.375. Its verify: PASS.
- What I did with it: I reread child/main.py and reran it in rerun_child/ (PCP check K3, exit 0). The output is identical to the child's results.txt and agrees with my independent program to 8 digits. Its "pass" is now reproduced, but the method is the same family as mine (Schwinger/Fourier with the same projector), so it is not independent of me.

## 6. Commands to rerun
```sh
cd C:/Users/donke/z4-workers/r8-tangent
export PYTHONUTF8=1; P=C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py
python -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
python $P check --ws pcp --name free_curv --expect-exit 1 -- python free_curv.py run2     # P0 fails (own bug), ~3 min
python $P check --ws pcp --name control_g0 --expect-exit 0 -- python control_g0.py         # refuses if results/control_g0.txt exists (exit 2)
mkdir -p rerun_child2 && cp child/main.py rerun_child2/ && python $P check --ws pcp --name rerun_child2 --expect-exit 0 -- bash -c "cd rerun_child2 && python main.py"
python $P verify --ws pcp
```
PCP verify, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

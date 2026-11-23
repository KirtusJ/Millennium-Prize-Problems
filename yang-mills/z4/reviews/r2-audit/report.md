# Z4 worker report: regulator trajectory and physical units for A4/B4 (r2-audit)

Control: `control.txt` = 0.272341 (−ln tanh 1). I share a model family with the director and with the sub-agent, so this agreement is not independent review.

## 1. Verdict table

| # | Item | Verdict | Evidence (one line) |
|---|---|---|---|
| C | Convention: κ_A = 2/κ_B, so g = z/2 | STANDS | A4 uses half-length generators, so ΣX² = Δ_round/4 (A4 third_moment: "γ = κ/4"). Equating κ_A/4 = 1/(2κ_B) gives the relation. Three independent checks: free plaquette 3κ_A = 6/κ_B, first moment 4κ_A S = 8A/κ_B, and K_e = K/4. |
| X | A4 and B4 agree on conventions and shared constants | STANDS (no DEFECT found) | All three cross-statements agree: A4 hamiltonian_variance last §, A4 excited_band 2nd ¶ ("z=2g") and B4 plaquette last ¶ ("g=z/2"). |
| A1 | Every energy bound and weight written in (β, b) | STANDS | Table in §1a. The sub-agent's independent closed forms match mine exactly. |
| A2.i | L ≥ (9/64)/(β(1+2β)b) for all β, b > 0 | STANDS (Lean) | `Z4Traj.lean: L_lower`, exit 0, axioms propext, Classical.choice, Quot.sound. c1 = 9/64 is sharp as β→0, because 1+B ≤ 1+2β with equality at β=0. |
| A2.ii | w ≤ 9/(512(1+β)²) for every D ≥ 36κ_A² | STANDS (Lean) | `w_upper`. Both of A4's D and D_* satisfy D ≥ 36κ_A², so the bound covers both readings. It uses 1+B ≥ (1+β)/2; the best constant there is √3−1, which I did not formalize. |
| A2.iii | b_n>0, β_n(1+2β_n)b_n → 0 ⇒ L_n → +∞ | STANDS (Lean) | `L_tendsto_top` |
| A2.iv | Adding β_n → ∞ ⇒ w_n → 0 | STANDS (Lean) | `w_tendsto_zero` |
| A2.v | "L_n bounded only if β_n²b_n is bounded below", as the task states it | DEFECT (the task's shape is false) | `complementary_needs_b_bound`: β=1/n, b=n gives L ≤ 9/64 while β²b = 1/n → 0. |
| A2.v′ | Corrected: b ≤ b0 and L ≤ C ⇒ β²b ≥ min(c/4, c²/(4b0)), with c = 9/(64C) | STANDS (Lean) | `L_bounded_forces`. Any trajectory with b_n → 0 has b_n ≤ b0. |
| A3 | Table of L, U, w in units of Λ | STANDS | `results/a3_20261122_230831.txt`: 36 met, 8 failed, 8 rows measured only. All 8 failures are P6, which was my own expectation (§3). |
| A4-3m | A4's claim that the third moment improves U to ~κ√g and w to ~1/g | STANDS asymptotically, but has no effect at realistic β | D_* < D only when (6+8√B)² > 86401, i.e. B > 1296, i.e. β > 862.4. On the whole A3 grid D_* = D. |
| B4-k | B4 constants rechecked by hand: 12/κ, 5/18, [3γ/(8κ), 24/κ], 3/64…3, 3/32…6, M = 8A/κ, Yarotsky rescaling 8κ/3 with ‖v_x‖ ≤ 8z | STANDS | Hand rederivation, logged in notes.md step 2 |
| A4-k | A4 constants rechecked by hand: A, D, B(g), 128π⁴, extraction A/2 ≤ Uν, 86401 = ⌈√(72·C3)⌉ | STANDS | Hand rederivation; √(72·C3) = 86400.6 |
| A4-1200 | Coefficient chain 336 / 1152 / 1200 / C_K in A4 third_moment | NOT CHECKED | Not enough time |

**Counts (met, failed, measured only):**
- Lean: 6 theorems proved and 0 failed. One of the 6 is the counterexample that refutes the task's shape A2.v.
- A3 program: 36 met, 8 failed, 8 measured only.
- Child program, rerun by me: 61 met, 0 failed.

### 1a. A1 table

**Definitions used throughout:**
- κ_B = βb, λ = β/b, z = β², g = β²/2, κ_A = 2/(βb).
- B = min{β²/2, 17β/(8√2) + 3/16}. The second branch takes over at β ≈ 3.125. For large β, B ≈ 1.5026β.
- H's coefficients carry 1/length, so every entry below is already a physical energy. Weights are dimensionless.
- ℓ = log(1/(bΛ)) and the asymptotic-freedom trajectory is β = cℓ, so b = e^{−ℓ}/Λ.

| Quantity | Formula in (β, b) | b→0, β fixed | b→0, β = cℓ |
|---|---|---|---|
| B4 small-z gap 3γ/(8κ_B) | 3γ/(8βb). Regime: 8β² below Yarotsky's unspecified threshold | ∝ 1/b → ∞, if β is in the regime | The trajectory leaves the regime once cℓ passes the threshold. Not applicable. |
| B4 M/v ≤ 12/κ_B | 12/(βb). Regime: β² ≤ 1/384, i.e. β ≤ 0.0510 | ∝ 1/b → ∞ | Leaves the regime. Not applicable. |
| B4 interval [3γ/(8κ_B), 24/κ_B], weight ≥ 5/18 | [3γ/(8βb), 24/(βb)]. Needs both small-z conditions | Both ends ∝ 1/b → ∞; weight constant | Not applicable |
| B4 large-z first moment M | 3/(4β²b) ≤ M ≤ 48/(β²b). Regime z ≥ 36, i.e. β ≥ 6 | ∝ 1/b → ∞ | Between 0.75 and 48 times Λe^ℓ/(c²ℓ²) → ∞ |
| A4 A = 9κ_A/(8(1+B)) | 9/(4βb(1+B)) | ∝ 1/b | ≈ 1.497 Λe^ℓ/(c²ℓ²) → ∞ |
| A4 D = κ_A²(6+8√B)² | 4(6+8√B)²/(βb)² | ∝ 1/b² | ≈ 384.7 Λ²e^{2ℓ}/(cℓ) → ∞ |
| A4 D_* | (4/(βb)²)·min{(6+8√B)², 86401} | ∝ 1/b² | Equals D until β > 862.4, then 345604/(β²b²) |
| L = A/16 | 9/(64βb(1+B)) | ∝ 1/b → ∞ | ≈ 0.09359 Λe^ℓ/(c²ℓ²) → ∞ |
| U = 4D/A | 64(6+8√B)²(1+B)/(9βb) | ∝ 1/b → ∞ | ≈ 1027.6 cℓ Λe^ℓ → ∞ |
| U_* = 4D_*/A | 64·min{…}(1+B)/(9βb) | ∝ 1/b | For β > 862: ≈ 9.23·10⁵/b, independent of β |
| w = A²/(8D) | 81/(512(1+B)²(6+8√B)²). Depends only on β | Constant in b | ≈ 7.286·10⁻⁴/(cℓ)³ → 0 |
| w_* = A²/(8D_*) | 81/(512(1+B)²·min{…}) | Constant in b | For β > 862: ≈ 8.11·10⁻⁷/(cℓ)² → 0 |
| B (dimensionless) | see the definitions above | Constant | ≈ 1.503cℓ |

**What the table shows:** along any bare or asymptotically free trajectory, the window [L, U] moves off to infinity in physical units. Its lower end diverges like e^ℓ/ℓ², i.e. like 1/(b·log²), and the weight it guarantees goes to zero. At fixed β it is a fixed-cutoff window that scales like 1/b.

**A3 numbers** (Λ = 1; c and Λ are illustrative only):

| c | bΛ | β | L/Λ | U/Λ | w |
|---|---|---|---|---|---|
| 1 | 1e-1 | 2.30 | 0.167 | 4.08e4 | 3.3e-5 |
| 1 | 1e-2 | 4.61 | 0.377 | 9.35e5 | 3.2e-6 |
| 1 | 1e-4 | 9.21 | 10.2 | 1.50e8 | 5.4e-7 |
| 1 | 1e-8 | 18.4 | 2.6e4 | 2.6e12 | 8.2e-8 |
| 0.5 | 1e-1 | 1.15 | 0.735 | 1.61e4 | 3.7e-4 |
| 0.5 | 1e-2 | 2.30 | 1.67 | 4.08e5 | 3.3e-5 |
| 0.5 | 1e-4 | 4.61 | 37.7 | 9.35e7 | 3.2e-6 |
| 0.5 | 1e-8 | 9.21 | 1.0e5 | 1.5e12 | 5.4e-7 |

- U/L lies between 2·10⁴ and 10⁸.
- The c=0.5 rows at bΛ ≥ 1e-2 have β < 6. B4's large-z regime does not apply to them, but A4's formulas hold for every g.

### 1b. A4 (suggestion, not a result)

The single lattice plaquette is an observable of size b. Its fluctuations are dominated by modes at the cutoff, so any guaranteed spectral window scales like 1/b. A candidate replacement:
- **The observable:** an observable of fixed physical size R. Options are a block average of plaquettes over a cube of side R/b, a Wilson loop of physical side R, or a smeared or gradient-flowed plaquette at flow time ∝ R². Divide it by a renormalization factor Z(b) chosen so that its variance stays of order one, for example Z = e^{−(perimeter-law self-energy)·(R/b)} for a loop.
- **What then has to be shown:** that this observable's spectral measure has a first moment and a second (or third) moment bounded in units of 1/R uniformly in b, and a variance floor that does not go to zero.
- **Estimates that would have to be redone:** every estimate the input proves at the scale of one link or one face:
  - A4's radial variance floor (one link, giving v_* ~ 1/g);
  - the first-moment identity M = 4κ_A S (one face; for a block it becomes a sum over Σ_e |∇_e O|²);
  - the second-moment commutator bound D (12 directions; for a block it grows with the support, ∝ (R/b)³);
  - the third-moment double commutator (16 touching plaquettes);
  - B4's large-z bounds 3/64 ≤ √z⟨1−φ⟩ ≤ 3 (one face).
- **The obstacle:** these must give constants in units of 1/R rather than 1/b, and that needs cancellations between plaquettes, i.e. correlation-length information. None of the input's product-trial or single-link arguments provides that information.

## 2. Hypotheses used, and where they are stated

**Conventions:**
- A4 hamiltonian_variance §intro: H = −κΣX², X from iσ/2, g = λ/κ.
- A4 third_moment §"Third moment…": γ = κ/4.
- B4 README §"Transfer, Hamiltonian and vacuum": H0 = (1/2κ)ΣA_e with a unit round metric.
- B4 README §"Spatial refinement": bare matching κ = βb, λ = β/b, z = β².

**A4 interval:**
- Periodic cubic box of side ≥ 3, κ > 0, λ ≥ 0 (A4 hamiltonian_variance §intro, excited_band ¶2).
- K_e ≤ B(g) from translation and cubic invariance of the unique vacuum (hamiltonian_variance §2).
- Var F ≤ 4 (excited_band §Extracting).

**B4 small z:**
- z ≤ 1/384 (plaquette §1).
- 8z below Yarotsky's Theorem-1 threshold (README table and §gap). γ is not given numerically.

**B4 large z:** z ≥ 36 (plaquette §2) and L ≥ 2.

**My Lean statements:**
- β > 0 and b > 0 real. κ_A and g as derived.
- D ≥ 36κ_A², stated as an explicit hypothesis.
- The corrected complementary statement adds b ≤ b0.

**Asymptotic-freedom trajectory:** β = c·log(1/(bΛ)) with c, Λ > 0 free. This is an assumption of the task, not a result of the input.

## 3. Failed predicates

- **A3, P6, 8 of 8 cases.** P6 was "D_* < D strictly on the grid". It failed because B ≤ 27.9 < 1296 everywhere on the grid. This was my own expectation, recorded in advance as one I expected to fail. It is not a defect of the target. It does show that the third-moment improvement only matters for β > 862.4.
- **The task's A2 complementary shape, without a bound on b.** It is false, refuted in Lean. This is a defect of the requested statement, not of the input notes.
- **A first Lean compile failed on one goal** (an unsolved `field_simp` goal in `L_tendsto_top`). Adding `ring` fixed it. This was my own error.
- **The child had no failures** (61 met, 0 failed).

**Tolerances:**
- A3 P2 and the child's P1 use relative 1e-12: double-precision ε ≈ 2.2e-16 times a safety factor of about 10⁴ for a few operations.
- The child's P3 uses 1%, chosen so that O(β^{−1/2}) corrections at β = 10⁶ (about 0.1%) pass.

## 4. Not checked

- A4 third_moment coefficient bounds (336, 1152, 1200, C_K). I checked only the final arithmetic leading to 86401.
- Yarotsky's theorem, and whether its hypotheses (1) and (2) hold. B4's threshold and γ are not numerical.
- B4's time-limit (Chernoff and compactness) argument and the girth argument.
- A4's radial Sobolev step in detail (I checked the arithmetic of 128π⁴), k_m, and the beta-law means r_m.
- Whether the tree-level matching κ = βb, λ = β/b is the right trajectory beyond tree level. I treated it as given.
- No Lean proof of the A1 asymptotic constants. They are checked numerically by the child (P3) and agree with my hand derivation.

## 5. Delegated question and outcome

**What I delegated** (to `child/`, with its own register `child/pcp`): given only the two Hamiltonian conventions and the formulas for B, A, D, L, U, w, derive κ_A(κ_B), g(z), the closed forms in (β, b), the large-β leading behaviour, and the behaviour along β = cℓ. The control question was −ln tanh 1.

**What came back:**
- Control: 0.272341, correct.
- κ_A = 2/κ_B and g = z/2, by the same Laplacian sum-of-squares argument as mine.
- Closed forms identical to mine.
- Leading constants: L ≈ 0.09359/(bβ²), U ≈ 1027.6β/b, w ≈ 7.286·10⁻⁴/β³, A ≈ 1.497/(bβ²), D ≈ 384.7/(b²β).
- Predicates: 61 met, 0 failed. Its verify passed.

**My recheck:**
- I read `child/check.py` and reran it through my register (check K3, exit 0). The rerun wrote a new `child/results_run2.txt` with 61 met, 0 failed.
- Caveat 1: its "direct" path already hard-codes κ_A = 2/κ_B, so its P1 tests only the algebra.
- Caveat 2: its P4 (the eigenvalue match) is nearly tautological. The convention derivation is independent only as reasoning.
- The constants agree with my A3 numbers. For example, at large β my L ≈ 0.0936/(β²b).

## 6. Commands to rerun

```
cd C:/Users/donke/z4-workers/r2-audit
export PYTHONUTF8=1; P=C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py
python -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
python $P check --ws pcp --name a3_table --expect-exit 0 -- python a3_table.py
python $P check --ws pcp --name child_check_rerun --expect-exit 0 -- python child/check.py
cd C:/Users/donke/z4-lean && PATH=$HOME/.elan/bin:$PATH python $P check --ws C:/Users/donke/z4-workers/r2-audit/pcp --name lean_Z4Traj --expect-exit 0 -- lake env lean C:/Users/donke/z4-workers/r2-audit/Z4Traj.lean
cd C:/Users/donke/z4-workers/r2-audit && python $P verify --ws pcp
```

The verify last line was:

`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

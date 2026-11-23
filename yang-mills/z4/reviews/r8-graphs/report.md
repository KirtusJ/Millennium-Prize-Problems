# r8-graphs challenger report: D4 (graph-holonomies) and B4 (coarse-holonomies) against Z4's free loop benchmark

Control: `control.txt` = 0.272341 (−ln tanh 1). The sub-agent got the same value independently (`child/control.txt`).
I share a model family with the directors, so this is not independent review.

## 1. Verdict table

| # | Item | Verdict | Evidence (one line) |
|---|---|---|---|
| 1 | G2: coefficient 3/2 in β²C(t) → (3/2)K(t)² for the centred ½Tr W of one fixed lattice square | **STANDS** | Derivation: ½Tr W = cos(g\|Φ\|/2) and Cov = (g⁴/64)·3·2K² = (3/32)g⁴K² = (3/2)K²/β² when β = 4/g². MC (P1) gives ratios 0.989 (K = 0.3) and 0.997 (K = 0.6), each within tolerance. |
| 2 | G2: K normalization | **STANDS only with K = G** (the flux kernel without g, in lattice units with b = 1, per colour θ_a = gΦ_a) | Reading K as g²G misses by a factor g⁻⁴ (P1b: ratio 9.9·10³ at g = 0.1). |
| 3 | G2: "three-loop order difference has separated correlation 6 det K(t)" | **STANDS** as the unnormalized connected covariance of O = ε_abc Φ1_a Φ2_b Φ3_c | MC (P2): 0.7559 against 6 det K = 0.7435, SE 0.0086. Same-time cross pairings vanish against ε. Dividing by 6 det K(0) gives the correlation coefficient. |
| 4 | G2: claim located in D4's notes | **DEFECT** (the claim is absent) | Searching all 8 D4 files for 3/2·K², det, K(t), "square" or "Gaussian circulation" finds nothing. The only K in D4 is a window length (second-scale) and a reflection-bound constant (reconstruction). |
| 5 | G2: K values in D4's own setting (4D isotropic lattice, integer time n) | **measured; comparison NOT CHECKED** (D4 prints no K) | Unit square: K4(n=1..4) = 0.068875, 0.011153, 0.002262, 0.000605. 2×2 square: 0.264069, 0.061446, 0.017644, 0.006224. Grid-converged to 4·10⁻⁶ (P3a). |
| 6 | G2: propagator choice matters (4D lattice time vs. Z4's Hamiltonian time) | **STANDS** | K4(1)/KH(1) = 0.936 (R = 1) and 0.914 (R = 2) (P3d). At n = 2..4 the ratio crosses above 1 (1.19 to 1.28 for R = 1). D4's time is 4D lattice time, so Z4's D_t formula must not be used directly. |
| 7 | D4 one-plaquette mean β⟨1−½Tr U_p⟩ → 3/4 (second-scale) | **STANDS** (consistent) | The free 4D per-colour plaquette variance is K4(0) = 0.500000 (equipartition 1/(2β) in U(1) normalization), so 3·(1/2)·β·g²/8 = 3/4. |
| 8 | G1, D4 main theorem: Haar limit and unit-variance decorrelation | **STANDS as read** (not reproved) | Joint limit b(1+β) → 0 on a fixed graph with positive physical edge lengths (README ¶1, graphs.md). This allows the logarithmic bare trajectory. Any other slice counts, including the adjacent one. |
| 9 | G3/G4: does either lane treat the ordinary uncompensated loop of fixed physical size under mean normalization (benchmark self-energy e^{−g²·0.3214·4R/b})? | **DEFECT of coverage**: neither lane does | D4 says it "gives no answer for a mean-normalized uncompensated Wilson loop" (mean-normalization.md) and calls the Z4 loop "a different observable" (second-scale end). B4 says "its unit-mean fixed-time covariance remains open" (README:41, heat trace). |
| 10 | G4: weak coupling at fixed lattice geometry; mean-normalized covariance of ½Tr W | **STANDS: O(1/β²), not O(1/β)** | Free SU(2) gives (3/2)K(t)²/β² = (3/32)g⁴K². MC: β²·Cov/M² = 0.1346 and 0.5424 against 0.135 and 0.540. The brief's "like 1/β" is wrong for SU(2): the real trace has no linear term, unlike U(1)'s g²G. Neither lane states this. |
| 11 | G5: B4 strong-coupling statements, tube versus disconnected squares | **NOT CHECKED: no such statement exists** | B4 contains no "strong coupling", "tube" or small-β expansion. I confirmed this by grep, and the sub-agent found the same. All B4 bounds hold at any coupling on a fixed finite lattice. Their only example is β = 1 (r = 0.7627). |
| 12 | B4 Hilbert bound ‖E[f\|X]‖² ≤ K‖f‖² and mean bound (D/A)^{±1} | **STANDS as read** (proof read, not reproved) | Fixed lattice, any coupling, lattice-unit contour (m links). The bound is independent of separation (README:41, :45), so it shows no decay in t. |
| 13 | B4 README:5 "sharp uniform threshold" | **DEFECT (wording stronger than theorem)** | Sharpness is shown only for two chosen, possibly very rare exteriors (binary-experiment:41), not for typical vacuum correlations. |
| 14 | B4 README:55 physical-unit scaling | **conditional** (counted as DEFECT of wording) | It rests on B = O(log(1/b)), which is assumed, not proved. Quote: "For isotropic spacing a=b, fixed physical coarse pitch h, and B=O(log(1/b))". |
| 15 | D4 mean normalization (compensated F = ½Tr(WP⁻¹)) | **STANDS as read**; the README wording "ordinary deterministic mean normalization" invites misreading | "Ordinary" refers to the normalization, not the observable. The observable is the staple-compensated loop, not a Wilson loop. |

Verdict counts: STANDS 9 (rows 1, 2, 3, 6, 7, 8, 10, 12, 15), DEFECT 4 (rows 4, 9, 13, 14; the brief's own wrong premises are listed separately under failed predicates), NOT CHECKED 2 (rows 5 and 11).
Program predicate counts as met, failed, measured only: **12, 2, 5** (g2_check.py). The child's program: **4, 0, 0**.

## 2. Hypotheses each statement uses (G1, G3, G6)

**D4**
- **Graph theorem** (README ¶1; graphs.md; mixing.md):
  - compact connected G
  - 4D isotropic Wilson law, periodic, sides ≥ 3
  - fixed rectilinear graph of positive *physical* edge lengths
  - limit b(1+β) → 0, a joint limit (spacing and coupling together; uniform in box size)
  - normalization: unit variance
  - separation: any other slice, counted in lattice steps
  - regime class: **joint**
- **Reconstruction, OS form of rank one** (reconstruction.md):
  - cylinder functions on graphs strictly at positive times, on the product-Haar limit process
  - regime class: **one limit** (the limit law)
  - the fixed-regulator spectral bound μ{aE ≤ R} ≤ e^R q is **fixed regulator**
- **Crossover** (crossover.md):
  - SU(2), string of ⌊βt⌋ bonds
  - dyadic boxes, or the exceptional-site correction
  - the physical length of the string tends to 0
  - regime class: **joint**; it concerns cutoff scale, not a fixed physical size
- **Mean normalization** (mean-normalization.md):
  - SU(2), spatial straight path, Lb → ℓ > 0, β → ∞, L/β → ∞, m = min(L, ⌈β^{3/2}⌉)
  - dyadic sides ≥ 4
  - observable: compensated F (not a Wilson loop)
  - separation: nonadjacent slices, including fixed physical separations
  - regime class: **joint**
- **Second scale** (second-scale.md):
  - infinite-time vacuum, β and L_box → ∞
  - uses C4's moment bound and Gaussian limit
  - regime class: **conditional on C4**
  - conclusions: the o((m/β²)²) bound at fixed t > 0 as b ↓ 0, and the e^{−κ/8} factor

**B4** (sub-agent table, rows checked by me):
- **χ² and Hilbert bounds** (README:23–29):
  - any compact connected G, any β_s, β_t ≥ 0
  - fixed finite periodic lattice
  - contour length m in lattice links
  - regime class: **fixed regulator**
- **SU(2) condition M r^{2m} → 0** (README:31):
  - r = I₂(4β_s+2β_t)/I₁
  - regime class: **one limit** (s → 0 through long paths, not through small β)
- **Mean bound** (README:35–41): independent of separation; fixed regulator.
- **Binary experiment** (binary-experiment.md): the limit s → 0 is proved in writing; the numbers are a **control** (M = 4292, error 0.158636 against Φ(−1) = 0.158655; I re-derived M = 4292 in the child run).
- **Physical units** (README:55): **conditional** (assumes B = O(log 1/b)).

**G3, fixed lattice geometry versus fixed physical size**
- **D4's "has a limit" statements** all concern fixed physical size:
  - "On any fixed rectilinear graph with positive physical edge lengths … converges in total variation"
  - "including fixed positive physical separations"
- The **crossover** concerns cutoff scale: "the physical length of the string tends to zero".
- **B4's theorems** are at fixed regulator and lattice units (m links). Physical size enters only at README:55.
- **The weak-coupling (3/2)K² claim** is for a lattice-unit square, so its physical size is b and the time separation is of order b (cutoff scale). It is not in D4's files.
- **The fixed-physical-size self-energy** e^{−g²·0.3214·4R/b} is not treated by either lane. For SU(2) at Gaussian order the analogue is ⟨½Tr W⟩ = (1 − g²G₀/4)e^{−g²G₀/8}, where G₀ is the per-colour flux variance. Two caveats:
  - Z4's c₁ = 0.3214 is for Hamiltonian sharp time; the 4D lattice value differs. For example, K4(0) = 0.5 for the unit plaquette. I did not compute c₁ in 4D.
  - D4's Haar limit (½Tr W → mean 0) is consistent with this decay.

**G6, conventions**
- **Trace**: both lanes use ½Tr.
- **Coupling**: D4 uses exp[−β(1−½Tr U)], so β = 4/g² for SU(2). B4 is anisotropic, with J = 4β_s + 2β_t and B = 1 + 4β_s + 2β_t. With β_s = β_t this is D4's q(6β).
- **Time**: both lanes count integer 4D lattice slices; B4's spectral bound uses temporal spacing a. Z4's benchmark uses continuous Hamiltonian time, which differs by 6 to 9% at n = 1 (row 6).
- **D4's Brownian "clock"** counts bonds in units of β. It is a path parameter, not time.

**What the notes do not claim**
- D4: no continuum construction or spectrum; no rate in n; no physical mass; no sign or scale of the first nonzero subleading connected term; nothing for the uncompensated loop.
- B4: no lower bound on typical correlations; no continuum.
- Neither lane says anything about strong coupling.

## 3. Failed predicates

- **P3c (R = 1 and R = 2)**: I expected "|K4(n)/KH(n) − 1| strictly decreasing in n". The measured values were 0.064, 0.191, 0.282, 0.234 for R = 1 and 0.086, 0.052, 0.102, 0.100 for R = 2.
  - **This was my own expectation, not a defect of either target.** The ratio crosses 1 between n = 1 and 2, and approaches 1 only in the far IR, beyond n = 4.
  - This failure is why register check K1 exited 1 against an expected 0.
- **Register checks K2 and K3** (rerunning the child's program) exited 1 because of my own invocation. Under `python -I`, numpy, which is in the user site, cannot be imported. K4, run without -I, exited 0.
- **The brief's premise in G4**: "mean-normalized covariance tends to zero like 1/β" is false for SU(2). It goes like 1/β², with coefficient (3/2)K(t)². This is a defect of the brief, not of either lane.
- **The brief's premise in G5**: the "strong-coupling statements" and the "joining tube" do not exist in B4. This is a defect of the brief.

## 4. What I did not check

- I did not reprove any of D4's or B4's theorems (mixing contraction, reflection estimate, Brownian convergence, binary-experiment CLT).
- I did not run D4's or B4's own check scripts or Lean files; they are not in the inputs.
- I did not compute the 4D-lattice perimeter coefficient (the analogue of 0.3214).
- I did not compute exact non-Gaussian corrections of order 1/β³.
- I did not evaluate K on finite dyadic tori; all values are for infinite spatial and temporal extent.
- The coordination-thread source of the (3/2)K² claim is not available to me.

## 5. Delegated question (rule 7) and outcome

**Question given to the sub-agent** (in child/): G5. For B4, list and classify every strong-coupling statement (proved, control or claim), explain the binary experiment, check for a tube versus disconnected squares, and find overstatements. Its control was −ln tanh 1.

**What came back**:
- control 0.272341, correct
- B4 contains no strong-coupling statement
- table in `child/answer.md`
- `child/check_b4.py`: 4 of 4 predicates met
- child register verify: PASS

**My check of its rows**: I reread three of them verbatim against the files, and all three match:
- README:41: "independent of the separation and temporal period"
- README:45: "even the next one"
- README:55: "B=O(log(1/b))"

My grep confirms that "strong" and "tube" are absent. I reran its program under my register: K4, exit 0.

## 6. Commands to rerun

```sh
cd C:/Users/donke/z4-workers/r8-graphs
export PYTHONUTF8=1
python -c "import math;print('%.6f'%(-math.log(math.tanh(1))))"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name g2_check --expect-exit 1 -- python g2_check.py   # exits 1: P3c fails by design of record
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name rerun_child --expect-exit 0 -- python C:/Users/donke/z4-workers/r8-graphs/child/check_b4.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```

g2_check.py writes a new result file with a timestamp each run (exclusive create); my run is in `results_g2_20261123_013922.txt`. Seed 20261123.

Last line of `pcp_os.py verify --ws pcp`:
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

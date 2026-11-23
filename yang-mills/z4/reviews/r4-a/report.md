# Disposition extraction: Yang–Mills lanes A4 (observable-normalization) and Z5 (volume-uniformity)

Worker r4-a under Director Z4, 22 November 2026. My job was to extract what each note claims. I did not judge whether the proofs are correct. Z4 and I come from the same model family, so this is not independent review.

Control: `control.txt` = 0.272341 (−ln tanh 1).

## Hypothesis first: file counts

- `input/` holds **29 .md files**: 27 in observable-normalization (lane A4), 1 in volume-uniformity (lane Z5), and 1 problem statement (`yang-mills_README.md`).
- Lane A4 has 15 notes that state a result and 12 `execution.md` receipts. I read all 27 in full and used the receipts only for the evidence column. Nothing in A4 is marked NOT READ.
- Lane Z5 has one note that states a result. The sub-agent extracted it. I also read it in full myself before delegating.
- These counts come from `count_md.py` (register check K1). Two of its predicates failed; see the "Failed predicates" section.

## 0. Verdict table (scope of this extraction)

| item | verdict | evidence |
|---|---|---|
| A4 row extraction, 15 result notes | STANDS | Every note was read in full. Each row below quotes or locates its own qualifier. |
| A4 numerical constants that chain across notes (C_3, G_pp, 2.1e6, b³D_H ≤ 25) | STANDS | Recomputed by hand: 72·1200²+1+1536 = 103 681 537 matches moment-bounds L46; 86401² ≥ 72·C_3; √(16·145·18·C_3) ≈ 2.08e6 < 2.1e6; b³D_H ≤ 4(5+9/8) = 24.5 ≤ 25. |
| A4: any claim of a 4D continuum theory or of a mass gap in physical units | STANDS as "not claimed" | Each note explicitly disclaims both (locations in column 7). |
| Z5 row (from the sub-agent, then rechecked) | STANDS | 5 of 5 checked fields matched the file (see §5). |
| Cross-lane conversion of conventions (E2 γ vs Wilson β; B4's z = 2g vs g = κ_Bλ/2) | DEFECT (documentation) | No conversion is stated inside the input notes. Both refer to B4 files that are not in `input/`. |
| Correctness of any proof | NOT CHECKED | Outside my role. |
| Lean replays and guest replays | NOT CHECKED | No source files are present (`.md` only). |

Counts for the whole extraction: **met 4, failed 1 (the documentation DEFECT), measured only 0; NOT CHECKED 2.**

## 1. Per-note rows: lane A4 (observable-normalization). All are SU(2), and all bounds are at a fixed regulator unless the row says otherwise.

Each row gives: (1) path; (2) the statement with its hypotheses; (3) the regime; (4) the gauge group and dimension; (5) units and the mesh→0 behaviour; (6) the evidence; (7) what the note says stays open.

**A1** `observable-normalization/README.md`
- (2) Let C_n(t) be a scalar spectral representation of a centered observable. Suppose v ≤ C_n(0) ≤ V and the first moment is ≤ M, for finite positive sums of atoms. Then v/2 ≤ C_n(t_*) ≤ V at t_* = v/(2M). If C_n(t_*) also converges, the limit is > 0.
- (3) CONDITIONAL. The hypothesis is that such a spectral representation, plus OS reconstruction, has been constructed for Yang–Mills (L9, L26).
- (4) No group. This is abstract.
- (5) Physical time is fixed by assumption. As mesh → 0: "remains open" (L26).
- (6) 2 Lean declarations (`momentLowerBound`, `separatedTimeWitness`). Lean checks the finite-sum version only (L24). 1 mutation was rejected (execution.md L32).
- (7) L26: the bounds for a renormalized 4D continuum/infinite-volume observable are open. L30: there is no lower bound on the excited spectrum.

**A2** `energy-density/README.md`
- (2) Setting: the periodic cubic SU(2) Hamiltonian on a box of side ≥ 3. The first moment of an energy-density observable O_w equals −Σ K_ij |w_i − w_j|². It satisfies 0 ≤ M_1 ≤ D_H Σ|w_i − w_j|², with D_H = κ²λ(2B + 9/8).
- (3) FIXED: finite box, fixed spatial mesh, continuous Hamiltonian time.
- (4) SU(2), 3+1 Hamiltonian, finite.
- (5) Lattice/Hamiltonian units. The bound is uniform in volume (L5). Mesh → 0 is deferred to spatial-limit.md.
- (6) 9 Lean declarations (execution.md L24–32). The operator identities, the vacuum estimates and the locality are "analytic", i.e. outside Lean (exec L35). 2 mutations rejected (exec L37). There is a numerical control on synthetic, rotor and geometry cases.
- (7) L5: "Proving a nonzero limiting norm remains open."

**A3** `energy-density/spatial-limit.md`
- (2) Setting: the bare tree-level trajectory κ = 2/(βb), λ = β/b, β ≥ 1, with weights w = b²φ. Then M_1(b²φ) = ρ_b ∫|∇φ|² + O(b), with 0 ≤ ρ ≤ 400. The filtered time-difference measures are tight and carry no mass at 0.
- (3) ONE-LIMIT: spatial mesh b → 0. The time step is already continuous (Hamiltonian). The volume is fixed, or "may grow".
- (4) SU(2), 3+1.
- (5) Physical units on the bare trajectory. The b² normalization "would require further evidence" to be identified as a stress-energy tensor (L5). The limit is identified only as a candidate first-moment form, "not … first moment of a limiting raw field" (L24).
- (6) Same Lean file as A2 (`bareCoefficient`, the filter declarations). The Taylor limit and the weak subsequences are analytic (exec L35).
- (7) L36: "The nonzero continuum vector and the lower gap remain open." The bounds also permit a zero limit.

**A4** `hamiltonian-variance/README.md`
- (2) Setting: the SU(2) Hamiltonian H = −κΣX² + λΣ(1 − x_p) on a periodic cubic box of side ≥ 3, any g = λ/κ ≥ 0. The variance satisfies Var(2x_p) ≥ v_*, and C(t) ≥ v_* exp(−tM_*/v_*), uniformly in box size.
- (3) FIXED: spatial cutoff fixed, uniform in volume. Fixed-time subsequential volume limits inherit the floor (L57).
- (4) SU(2), 3+1.
- (5) Hamiltonian units. For large g, M_*/v_* = O(κ√g), so "cannot by itself provide a finite continuum energy scale" (L61).
- (6) 9 Lean declarations. The Haar integrals, the radial bounds and the identification of the spectral law are analytic (exec L35). 1 Lean mutation was rejected, plus 1 numerical mutation (a residual of 35.86 with unit generators) (exec L37).
- (7) L61: matching the regulators, removing the spatial cutoff, reconstruction, and a positive lower gap for all groups are open. L21: the bound gives only an upper bound on the bottom of the spectrum.

**A5** `hamiltonian-variance/excited-band/README.md`
- (2) Same model at fixed couplings. ν([L, U]) ≥ w > 0, with L = A/16 and U = 4D/A. The time-difference inequality holds in every box. Subsequential volume limits keep mass ≥ w in [L, U].
- (3) FIXED as proved (fixed mesh and couplings; volume limit along a subsequence). The note also states an ITERATED application, via B4: first the time step → 0, then the volume along a subsequence (L22). That application is CONDITIONAL on B4's regulator matching, which is not in `input/`. "A simultaneous volume and time limit would require further uniform control."
- (4) SU(2), 3+1.
- (5) Physical Hamiltonian units. For large g: L ~ κ/√g, U ~ κg, w ~ g^(−3/2). "A fixed-cutoff positive-energy window leaves the continuum … problem open" (L59).
- (6) 6 Lean declarations. The sphere divergence, the domain and the spectral moments are analytic (exec L30). 1 mutation rejected. Numerical check on an isolated plaquette rotor (exec L32–41).
- (7) L59. L20: the result allows levels below L.

**A6** `hamiltonian-variance/excited-band/third-moment/README.md`
- (2) For every λ ≥ 0 and every box, M_2 ≤ 86 401 κ². This improves the band to U ~ κ√g and w ~ 1/g.
- (3) FIXED: uniform in volume and in the magnetic coupling, at fixed mesh.
- (4) SU(2), 3+1.
- (5) Hamiltonian units. On the bare trajectory, κ√g ~ 1/b, so the bound "still permits excitation energies to diverge in physical units" (L68).
- (6) 7 Lean declarations. The commutator identity, the coefficient counts and the geometry are analytic (exec L31). 1 mutation rejected. Rotor numerics (exec L33–43).
- (7) L16: "It does not locate the bottom of the spectrum". L68: tightness under refinement needs new information.

**A7** `smeared-plaquettes/README.md`
- (2) Setting: a translation-invariant vacuum (assumed, L30) and xy plaquettes with weights c. Exact formula: M(c)/κ = AΣ(c_p − c_{p+j})² + Σ J_j c_p c_{p+j}. Consequence: C_c(t) ≥ V(c) exp[−tM/V].
- (3) FIXED.
- (4) SU(2), 3-dimensional spatial Hamiltonian.
- (5) Lattice units. As mesh → 0: "The unresolved step is a joint analytic estimate … as the regulator is removed" (L47).
- (6) 5 Lean declarations (scalar identities). The lattice sums and the probability calculation are analytic (exec L26). There is a numerical orientation check (discrepancy 3.3e−9, 1.98 when mutated), and the receipt reports no Lean mutation.
- (7) L47: no continuum existence and no mass gap.

**A8** `smeared-plaquettes/moment-bounds/README.md`
- (2) For every real coefficient vector c, in every box: a·n ≤ M_1(c) ≤ 16κS·n, M_2(c) ≤ d·n and M_0(c) ≥ (a²/d)·n, where a = 4κ/[25(1+B)] and d = 2.1e6 κ².
- (3) FIXED: uniform in volume and coefficients.
- (4) SU(2), 3+1.
- (5) Hamiltonian units. At large g, both bounds on the first moment are of order κn/√g (L33). The refinement obstruction is in A9.
- (6) 8 Lean declarations. The sphere integration by parts, the localization and the incidence counts are analytic (exec L36). 2 mutations rejected. Geometry enumeration on tori of side 2–5 (exec L38–49).
- (7) Points to refinement.md L37. The receipt (exec L3) says "Independent mathematical review remains a separate step."

**A9** `smeared-plaquettes/moment-bounds/refinement.md`
- (2) The normalized energy-weighted law satisfies P^(1)([0, E_*]) ≤ 450 E_* N_c/κ. So on the bare trajectory, with E_*βbN_c → 0, the energy-weighted weight of a bounded-support smearing escapes. At fixed cutoff, a fraction 1 − ε of orthonormal modes keep raw mass in a window.
- (3) ONE-LIMIT (spatial mesh b → 0, bare trajectory) for the escape statement, which is a negative result. The window statement is FIXED.
- (4) SU(2), 3+1.
- (5) Physical units on the bare trajectory: this is an escape. Necessary condition: N_c ≥ ηκ/(450 E_*) (L23).
- (6) Same Lean file as A8 (`weightedEscape`, `lowFirst`).
- (7) L23: the raw finite-energy weight is left open. L37: "The spatial continuum theory … and a common lower bound … remain open."

**A10** `smeared-plaquettes/action-curvature/README.md`
- (2) Take the zero-momentum total plaquette action and average the coupling over g ∈ [G, 2G]. In units of κ√G, the normalized raw spectral energy has bounded first and inverse moments, uniformly in G ≥ 1 and in volume. On the bare trajectory, b → 0 implies the loss of all averaged fixed-positive-time autocorrelation of this probe.
- (3) ONE-LIMIT: spatial mesh b → 0 (G → ∞), coupling-averaged, volume fixed within each window. The result is negative for this probe.
- (4) SU(2), 3+1.
- (5) Energies of order 1/b in physical units (L5). "A full positive-time limit … must therefore be zero" (L65).
- (6) 8 Lean declarations. `dyadicRawLow` assumes the inverse-moment budget, the variance floor and the support as hypotheses (exec L41). The perturbation calculation is analytic. 2 mutations rejected. Rotor numerics.
- (7) L67: does not treat a fixed compactly supported smearing, 4D reconstruction, or a lower mass gap. L5: "A prescribed exceptional coupling can have a different spectrum."

**A11** `smeared-plaquettes/action-curvature/controls.md`
- (2) A two-qubit family satisfies all the scalar inputs, yet sends 13/29 of the normalized raw mass to energy zero at g_0.
- (3) CONTROL: a toy two-level system.
- (4) None (qubits). The rotor is SU(2) with a single plaquette.
- (5) Not applicable. The note says it gives "no evidence that such an exceptional trajectory exists for the cubic Wilson Hamiltonian" (L16).
- (6) Numerical: slow fraction 0.448275862 = 13/29 (action-curvature exec L48–51).
- (7) L16.

**A12** `thin-loops/README.md`
- (2) Setting: the 4D isotropic Wilson measure, a periodic lattice with sides ≥ 3, β ≥ 0, and a simple contour of L edges. |EF| ≤ 2ε, |EF² − 1| ≤ 3ε and |Cov(F, G)| ≤ 2ε√Var G, with ε = exp[−L/(19(4β+1))], uniformly in volume.
- (3) FIXED as proved. The regulator-trajectory consequence (L34) is explicitly "a conditional statement about the chosen scale-setting map" with h(1+β) → 0. That consequence is CONDITIONAL and negative.
- (4) SU(2), 4D Euclidean lattice.
- (5) Lattice units. As mesh → 0 along h(1+β) → 0, thin-loop correlations vanish (L34). "It provides no mass-gap bound" (L36).
- (6) 4 Lean declarations. The conditional measure, the graph selection and the continuum interpretation are analytic (exec L25). Bessel-ratio numerics (1.3e−12). The receipt reports no Lean mutation.
- (7) L36: smeared and renormalized observables are left open.

**A13** `transfer-increments/README.md`
- (2) Part 1: V − C_k ≤ kD for a positive contraction. Part 2: the E2 central SU(2) convolution satisfies 0 ≤ γ(1 − λ_{γ,n}) ≤ (n² − 1)/2. Part 3: in an uncoupled loop model, the exact correlation is r_1^{kL}, with limit exp[−3tℓ/(2c)] when γah → c.
- (3) CONTROL for the loop and E2 parts: "This example sets the spatial plaquette interaction to zero" (L35). The abstract lemma is CONDITIONAL on a transfer realization.
- (4) SU(2) independent links (uncoupled).
- (5) Common physical units, assumed. The scaling statement depends on γah (L33). The note says it "supplies no scale-setting theorem for four-dimensional Yang–Mills" (L35).
- (6) 6 Lean declarations. The Bessel calculation and the infinite sums are analytic (L27). 1 mutation rejected. SciPy check: 0.22312 vs exp(−3/2) (exec L33).
- (7) L35: the interacting two-slice Wilson estimate is outstanding. Exec L3: "Independent mathematical review of this revision remains open."

**A14** `wilson-loop/README.md`
- (2) For any smooth gauge-invariant V and a simple loop of L links: M_F = κL(1 − s/4), and C_F(t) ≥ (s − m²) exp[−tκL(1 − s/4)/(s − m²)]. Also covered: the adjoint version (SO(3)-descending) and the one-step Jensen bound C_k ≥ V(1 − D/V)^k.
- (3) FIXED (finite spatial lattice, Hamiltonian). The one-step liminf is CONDITIONAL on V_n ≥ v and D_n ≤ a_n M along a sequence (L55).
- (4) SU(2), with an SO(3) adjoint remark (C4). 3+1.
- (5) Hamiltonian units. "For a fixed physical contour, the number of lattice links generally grows under refinement" (L41).
- (6) 4 Lean declarations. The ground-state transform and the continuum power limit are analytic (exec L27). Numerical orientation control (8.3e−10). No Lean mutation reported.
- (7) L41: continuum existence, identification with Yang–Mills, all groups, and a gap in every sector are open.

**A15** `wilson-variance/README.md`
- (2) Setting: the 4D periodic Wilson measure, sides ≥ 3, β ≥ 0. Var(Σ c_p Tr U_p) ≥ (4e^(−15/4)/99) sin⁴(1/(4√(1+β))) Σ c_p², uniformly in the lattice dimensions.
- (3) FIXED: uniform in volume.
- (4) SU(2), 4D Euclidean lattice.
- (5) Lattice units. The coefficient is ~ (1+β)^(−2). "Along a trajectory with β → ∞ this floor decreases" (L55).
- (6) 6 Lean declarations (algebraic). The lattice independence, the integration by parts and the shift comparison are analytic (exec L3). Exact-arithmetic and enumeration checks. No Lean mutation reported.
- (7) L55: "Continuum existence and the full mass gap remain open." Identifying the time regulator with the Hamiltonian notes is required.

Evidence totals for lane A4, from the receipts: 63 Lean declarations across 11 Lean files (2 + 9 + 9 + 6 + 7 + 5 + 8 + 8 + 4 + 6 + 4 + 6, counting A2/A3 and A8/A9 once each). Every receipt states that the analytic steps lie outside Lean. 11 Lean mutations were rejected (1 + 2 + 1 + 1 + 1 + 2 + 2 + 1 = 11), plus numerical mutations (35.86 and 1.98). Every Lean source was produced by A4 templates through PCP OS guests. The top-level receipt says these "do not provide independent mathematical reviews" (execution.md L5).

## 2. Row: lane Z5 (volume-uniformity), extracted by the sub-agent and rechecked by me

**Z1** `volume-uniformity/README.md`
- (2) V1: the massless free lattice field on N sites has lowest mode 2·arsinh(sin(π/N)) ≤ 2π/N, and in physical units ≤ 2π/L. V2: any gap(L) ≤ C/L has no uniform positive lower bound. V3: numerical controls, including the massive m₀ = 1 gap ≥ 2·arsinh(1/2), uniform in L.
- (3) CONTROL: Gaussian free field, not a gauge theory (L23).
- (4) No gauge group. The free scalar's dimension is not stated beyond "N sites".
- (5) Both lattice and physical units (L17). The massless physical gap ≤ 2π/L is "zero at every lattice spacing and in the continuum" (L21).
- (6) 3 Lean theorems in `VolumeUniformity.lean`, compiled with exit 0 and standard axioms. The first compile failed and is kept on record (L29). Numerical: met 3, failed 0, measured only 0 (L19). No mutation tests reported.
- (7) L23: "No statement about a non-abelian theory." L37: "has had no challenger, micro-review or cross-read". The note's "Opening dispositions" section (L41–45) is about the Riemann hypothesis and Navier–Stokes and is off-topic here.

## 3. Requirement tables

### Lane A4 (observable-normalization)

| req | disposition |
|---|---|
| (a) continuum limit on R⁴ | PARTIAL. Only a one-limit spatial-mesh statement for a first-moment form (A3), and negative escape results (A9, A10, A12). Time is continuous, or matched via B4. No note constructs a 4D continuum theory: A1 L26 and A3 L36 call this "open". |
| (b) reflection positivity / OS | NOT ADDRESSED as a result. A1 L26 uses OS reconstruction only as a hypothesis. |
| (c) Euclidean invariance | NOT ADDRESSED. Only cubic lattice symmetry is used (A3 L18, A4 L11). |
| (d) nontriviality | ADDRESSED AT FIXED REGULATOR. Variance and time-correlation floors (A4, A5, A8, A15). In the continuum, a nonzero limiting vector is "open" (A2 L5, A3 L36). |
| (e) mass gap > 0, physical units | NOT ADDRESSED. Every note disclaims a lower gap (A4 L21, A5 L59, A6 L16, A10 L67). |
| (f) all compact simple groups | NOT ADDRESSED. SU(2) only. There is an SO(3) adjoint remark (A14 L45–51). A4 L61 says "all compact simple groups remain open". |

### Lane Z5 (volume-uniformity)

| req | disposition |
|---|---|
| (a) continuum limit | NOT ADDRESSED. It is an adverse control on the free field only. |
| (b) RP / OS | ADDRESSED AT FIXED REGULATOR, for the free field only. "reflection-positive lattice theory" is asserted for the control (L21) and not proved for Yang–Mills. |
| (c) Euclidean invariance | NOT ADDRESSED. |
| (d) nontriviality | NOT ADDRESSED. The Gaussian free field is trivial by construction. |
| (e) mass gap | PARTIAL. It states the obligation (a gap uniform in L, L9) and an adverse control: a C/L gap is not uniform. It does not bound Yang–Mills. |
| (f) all groups | NOT ADDRESSED. "No statement about a non-abelian theory" (L23). |

No note in either lane asserts any requirement for the 4D continuum theory, so nothing is marked CLAIMED.

## 4. Contradictions and convention conflicts

No direct contradiction was found. Apparent tensions turn out to be about different observables or regimes, each stated:
- A4/A5 keep correlations at fixed couplings.
- A10 loses them on the bare trajectory, where A4 L61 already notes that M_*/v_* = O(κ√g) diverges.

These pairs use incompatible conventions, or have conversions missing from `input/`:
1. **Generator normalization within lane A4.** `wilson-variance/README.md` §2 (L20) uses iσ_j, which has unit angular speed. `hamiltonian-variance/README.md` (L11) and every other Hamiltonian note use iσ_j/2. A15 L55 says the two must be identified before they can be combined, but gives no conversion factor. This is scoped, not wrong.
2. **Scale-setting parameter of the E2 model vs. the Wilson coupling.** `transfer-increments/README.md` §"closed-loop" (L33) says correlations survive iff γah → c > 0. `thin-loops/README.md` §"Consequence" (L34) says thin-loop correlations vanish when h(1+β) → 0. No relation between γ (E2 time coupling, zero spatial interaction) and β (isotropic Wilson) is stated. The two "loop" conclusions point in opposite directions and cannot be compared without one.
3. **B4 parameter conversions.** `hamiltonian-variance/README.md` L63 gives κ = 2/κ_B and g = κ_Bλ/2. `excited-band/README.md` L22 gives "B4's parameter z = 2g". Both refer to B4 files that are not in `input/`, so I could not check that they agree.
4. **Lane A4 vs. lane Z5: volume claims.** A4/A5/A8 say "uniform in box size" for variance and spectral-window bounds. Z5 L9 says a fixed-L gap "has proved nothing until the bound is shown independent of L". These are not contradictory: A4's uniform statements are lower bounds on weight and *upper* bounds on the bottom of the spectrum, never a lower gap. A4 does not claim the Z5 obligation.

## 5. Statements each lane marks as most in need of independent review

**Lane A4:**
1. `transfer-increments/execution.md` L3: "Independent mathematical review of this revision remains open." This covers the E2 Bessel bound and the transfer lemmas.
2. `smeared-plaquettes/moment-bounds/execution.md` L3: "Independent mathematical review remains a separate step." This covers the all-smearing moment bounds (constants a, d) on which A10 depends.
3. `observable-normalization/execution.md` L5: "The three workers do not provide independent mathematical reviews." This covers `separatedTimeWitness` / `momentLowerBound`. In addition, every receipt flags the analytic steps outside Lean, e.g. energy-density/execution.md L35.

**Lane Z5:** the note marks a single global item: "All work above … has had no challenger, micro-review or cross-read" (L37). It also flags that the first doubling factor of 3.38 is "far from 4", kept as measured (L23). It flags the first failed Lean compile (L29). It does not rank three statements, and I have not invented a ranking.

## 6. Failed predicates

- `count_md.py`, check K1, exit 1:
  - **P1** (expected 28 .md, found 29): my own expectation error. I forgot to add `yang-mills_README.md` to 27 + 1.
  - **P3** (expected 11 `execution.md` in A4, found 12): my own expectation error. I miscounted.
  - **P2** (27 / 1) was met.
  - The result file `count_result.json` was kept and not overwritten. Neither failure is a defect in the input.
- Sub-agent check results: see §7.

## 7. What I did not check

- The correctness of any proof.
- Lean replays and PCP OS guest replays (no sources in `input/`).
- The B4, C4, D4 and G4 files referenced by A4 (not in `input/`).
- The external links.
- The numerical outputs printed in the receipts, which I did not rerun.
- Z5's off-topic RH/NS section.

## 8. Delegated question and outcome

**Question.** The smaller lane, `volume-uniformity/README.md` (one file), extracted with the full template. Control question: 7·13 + √144 = 103. The sub-agent worked in `child/` with its own register in `child/pcp`.

**Returned:**
- `child/control.txt` = 103, which is correct.
- Register check K1, `count.py`, printed 1 and exited 0. I reran `count.py`: it prints 1. I reran `verify` on `child/pcp`: PASS.
- **`child/report.md` does not exist.** The harness refused the sub-agent's write, so the report came back as text. I transcribed it, condensed, into §2 and §3 above.

**Five fields checked against the file. Matched 5 of 5:**
1. The V1 statement and bound (L17).
2. The regime is CONTROL, with "not a gauge theory" (L23).
3. 3 Lean theorems, exit 0, standard axioms (L27).
4. Numerical counts met 3, failed 0, measured only 0 (L19).
5. "no challenger, micro-review or cross-read" (L37).

**Extra points the sub-agent raised, all correct on rereading:**
- L9 justifies the automatic finite-volume gap by a compact gauge group, but the massless control has a non-compact Gaussian target. Excluding the zero mode is implicit, not stated as a hypothesis.
- The spacing a is undefined in V1.
- The free field's dimension is unstated.
- The "Meaning" paragraph (L21) asserts reflection positivity and a positive transfer operator, which V1–V3 do not state.

I accept these as extraction findings. They do not affect correctness. Its "pass" is its own claim; I only reran the count and the verify.

## 9. Rerun

```sh
cd C:/Users/donke/z4-workers/r4-a
export PYTHONUTF8=1
python -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py init pcp --principal principal --principal-name "Kirtus Justus"   # fresh dir only
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name count-md --expect-exit 0 -- python count_md.py   # delete count_result.json first in a fresh copy; expected exit 1 (P1, P3 my errors)
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
cd child && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```

## Register

Last line of `pcp_os.py verify --ws pcp`, for my register:
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

My register holds K1 count-md, which exited 1 against an expected 0 because of my two counting errors, P1 and P3 (see §6). The child register `child/pcp` also verifies as PASS.

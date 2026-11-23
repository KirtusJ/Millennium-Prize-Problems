# Disposition report: two Yang–Mills lanes (transfer-operator, g4)

Worker r4-b for Director Z4. This report extracts what the notes claim; it does not judge whether their proofs are correct. The sub-agent and I share a model family with the authors, so our agreement is not independent review. Control value: −ln(tanh 1) = 0.272341 (control.txt).

## 1. Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| Control (−ln tanh 1 = 0.272341) | STANDS | control.txt; the child obtained the same value independently |
| File-count hypothesis: 28 .md (18 transfer-operator, 9 g4, 1 README) | STANDS | count_files.py run through the PCP register, check K1 exit 0; count_result.txt |
| transfer-operator lane: what it establishes | STANDS as extracted | All results are at a FIXED spatial mesh: a gap uniform in time step and volume, a joint a→0, L→∞ local limit, and positivity at fixed mesh. On spatial refinement it gives only obstructions. It claims nothing for the 4D continuum. |
| g4 lane: what it establishes | STANDS as extracted (sub-agent rows, 6/6 spot-checked) | Reflection positivity on a finite open slab (text proof only). Lean-checked lemmas that RP is preserved under limits, conditional on a limit existing. Pushforward transport. No continuum, gap or nontriviality claim. |
| Any note claiming a Clay requirement for the 4D continuum | NONE FOUND | Both lanes disclaim it explicitly (transfer-operator/README.md last §; g4/README.md line 3) |
| Lean/mutation counts reported by the notes | NOT CHECKED | No .lean source is in input/. Counts are copied from the execution notes. |
| Direct contradictions between statements | NONE FOUND | 4 convention clashes without a stated conversion (§6) |

Counts (met, failed, measured only): **6 met, 0 failed, 1 measured only**.
- Met: the control; P1 and P2 of count_files.py; the child's g4-count predicate; the spot-check of the child's rows (6/6); "no note asserts a continuum requirement".
- Measured only: the reported Lean and mutation totals.

Hypothesis count (rule 4): input/ holds 28 .md files, namely yang-mills_README.md and 27 lane notes.
- transfer-operator: 18 files. 13 state a result and 5 are execution logs. I read all 18 in full.
- g4: 9 files. 6 state a result (counting cross-lane-review) and 3 are execution logs. The child read all 9 in full. I read 6 of them in full to check its rows, and checked the 3 execution logs by grep for their counts.
- No file is NOT READ.

## 2. Per-note rows

## Lane transfer-operator (done by me; 18 files, all read in full; 13 state results, 5 execution logs used for evidence)

Paths relative to input/transfer-operator/. Abbreviations: z = κλ; a = time step; L = spatial side; b = spatial mesh.

| # | File | Main statement (with hypotheses) | Regime | Group / dim | Units; mesh→0 behaviour | Evidence (as reported) | Open (per note) |
|---|---|---|---|---|---|---|---|
| T1 | README.md | Abstract: if a positive contraction T fixing the vacuum satisfies three sector form bounds (u, v, c) with c² ≤ (u−m)(v−m), u>m, then defect ≥ am; a 2×2 positive family with unique vacuum has gap ≤ 2a → 0; for the one-link SU(2) convolution, −g log r ≥ 3g/(2g+3) (≥3/5 for g≥1). | CONTROL (abstract operator test + finite-dim adverse family + one-link SU(2) model) | SU(2), one link (no spatial dimension) | dimensionless semigroup parameter; "provides no control of spatial plaquettes, the infinite-volume spectrum or the physical clock" (§"A quantitative test") | 9 Lean decls (execution.md); spectral-theorem step and integral representation are prose ("analytic interface"); 2 mutations rejected | Wilson-lattice estimates for 4D (§1 para, §"What would advance"); "No continuum mass gap or Millennium solution is claimed here" (last §) |
| T2 | blocked-time/README.md | On periodic SU(2) spatial lattice, side L≥2, fixed spatial mesh, β_t=κ/a, β_s=aλ, with a≤κ/4 and z≤1/384: full gauge-invariant Wilson transfer log gap ≥ 4 log3/(13κ), uniform in L and a; same for the Hamiltonian; local vacuum correlations converge along every simultaneous a↓0, L→∞. | JOINT (time step and spatial volume, any schedule; spatial mesh fixed) | SU(2), 3+1 lattice (spatial lattice, continuous/discrete time) | physical time units (units of κ) at fixed spatial mesh; mesh refinement treated in local-limit.md (floor diverges as 1/(βb) on tree-level trajectory) | 18 Lean decls in blocked-time/execution.md (Bernoulli, row bounds, matrix iteration, unit conversion); Dobrushin comparison, Bessel ratio, Peter–Weyl, bridge law, spectral density supplied in notes; 6 adverse changes rejected; Z2 circuit numerical control | z<2/455 gives non-explicit floor (last §); spatial continuum not addressed here |
| T3 | blocked-time/compact-groups.md | For each nontrivial compact connected Lie G with faithful unitary rep π, there exist T≥1, h0 (depending only on (G,π), not explicit) such that a/κ≤h0 and κλ≤1/[120(T+1)] give Wilson and Hamiltonian gap ≥ log3/((T+1)κ), uniform in L; local correlations have common limit along every joint a↓0, L→∞ at fixed spatial mesh; plaquette excitation nonzero for z ≤ ℓ_G v²/2304; open-slab time reflection gives the split Wilson crossing action. | JOINT (time step and volume; spatial mesh fixed) | all compact connected G with faithful π (incl. simple groups), 3+1 lattice | physical time units, fixed mesh; "It leaves the spatial continuum Yang–Mills problem open" (§intro) | Lean: mixture and group row, crossing-face identity (within the 18 of blocked-time/execution.md); Li–Yau heat bound, binomial minorization, fixed-box vacuum convergence listed as analytic; SO(3) numerical quadrature controls | spatial continuum (§intro); no rate for general G (§Fixed-box) |
| T4 | blocked-time/local-limit.md | At fixed spatial mesh, κ>0, z≤1/384: Wilson vs Hamiltonian local correlations differ by O(a^{1/3}) uniformly in L; liminf/limsup of the gap lie in [4log3/(13κ), 12/κ]; on tree-level trajectory κ=βb, λ=β/b with β²≤1/384 the gap in the original clock diverges ≥ 4log3/(13βb) and only contact terms survive for a Euclidean-scalar probe. | JOINT (a↓0, L→∞ any path, fixed mesh); refinement part is a negative statement on one mesh trajectory | SU(2) (faithful-character range mentioned), 3+1 lattice | physical time units; mesh→0: "lower gap in the original physical clock diverges at least as 4log3/(13βb)" (§"A nonvanishing excitation…"); weak-coupling β→∞ "falls outside the estimate" | text proof; finite-propagation lemma in Lean (blocked-time/execution.md) | "Nontrivial continuum existence, Euclidean covariance and a positive finite physical mass there remain open" (end of §"A nonvanishing excitation…"); extensive insertions, shrinking time separations (§Uniform time error) |
| T5 | blocked-time/momentum.md | Same SU(2) range z≤1/384, fixed mesh: Wilson and Hamiltonian connected correlation matrices agree at each spatial momentum uniformly in momentum and volume, rate O(a^{1/3}(1+|log(a/t0)|)³); limit is real-analytic in momentum. | JOINT (time step and volume; fixed mesh) | SU(2) (qualitative for faithful-character case), 3+1 lattice | fixed time units t0; "Renormalizations growing with the spatial cutoff are outside the estimate" (§intro) | text proof; Lean: finite Fourier sum and cubic shell polynomial | spectral windows with atoms at endpoints (end §Limits) |
| T6 | hamiltonian-time/README.md | At fixed spatial mesh and finite volume, Wilson transfer and vacuum correlations converge as a↓0 to H=(2κ)⁻¹ΣA_e+λV; free (λ=0) first excitation 3min(L,4)/(2κ); if 8z is below Yarotsky's Theorem 1 threshold the gap is ≥ 3γ/(8κ), γ>0 independent of L; same Hamiltonian argument for any compact connected simple G. | ONE-LIMIT (time step; volume and mesh fixed). The uniform-in-L gap is CONDITIONAL on 8z lying below Yarotsky's unquantified threshold ("We do not assign a numerical value") | SU(2); Hamiltonian part also compact connected simple G; 3+1 lattice | physical time (units of κ); mesh→0: on z=β², β→∞ "eventually leaves the small-z gap theorem" (§Spatial refinement) | 11 Lean decls (hamiltonian-time/execution.md); Peter–Weyl, Chernoff, compactness, "applicability of the external stability theorem" are analytic; 4 false changes rejected | "Neither the fixed-mesh gap nor its positive plaquette correlator identifies a nontrivial Euclidean-invariant theory" (§Spatial refinement); uncoupled rotation-test failure (§An explicit spatial refinement) |
| T7 | hamiltonian-time/plaquette.md | In the fixed-mesh Hamiltonian, z≤1/384: plaquette variance ≥ 5/9, energy/variance ≤ 12/κ, so ⟨w,e^{−t(H−E0)}w⟩ ≥ (5/9)e^{−12t/κ}, uniform in L; for z≥36: 3/64 ≤ √z⟨1−φ_p⟩ ≤ 3. | ONE-LIMIT (time step already removed; mesh fixed; bounds uniform in L) | SU(2), 3+1 lattice Hamiltonian | physical time (κ units); "A fixed spatial mesh is essential to the finite-energy conclusion" (last para); on tree-level trajectory M/v scale is 1/b | Lean arithmetic (in the 11 decls); vacuum identities analytic | large-z: "do not establish a weak-coupling spectral gap or the scale of the spatial correlation length" (end §large coupling) |
| T8 | joint-cutoff/README.md | SU(2), periodic side L, c=6λL³+6/κ: if ac≤1/36, first log-transfer gap differs from Hamiltonian gap by ≤180ac²; vacuum projection error ≤72ac²/Δ; at fixed mesh and fixed κ,λ, aL⁶→0 suffices; for varying mesh, a(1+c)²→0 (tree-level: aβ²/b⁸→0). | JOINT (simultaneous a↓0 and L→∞ along aL⁶→0, or a(1+c)²→0) | SU(2), 3+1 lattice | absolute physical units; "tracks a possibly vanishing Hamiltonian gap in absolute units" (§Joint paths) | 14 Lean decls (joint-cutoff/execution.md); vacuum stability, evolution estimates analytic; 5 mutations rejected; 32-mode circuit numerics | "Isotropic removal, a uniform Hamiltonian gap along a spatial continuum trajectory, nontriviality of that limit, and reconstruction of four-dimensional Yang–Mills theory remain open" (last para) |
| T9 | joint-cutoff/evolution.md | For ac≤1/36, a≤t/2: ‖(T_a/‖T_a‖)^N − e^{−t(H−E0)}‖ ≤ 2/N+3a/t+7ac+4/k+72ak²/t+144atc², no gap hypothesis. | JOINT (vanishes if a(1+c)²→0) | SU(2), 3+1 lattice | fixed physical time | text proof (listed as analytic in joint-cutoff/execution.md) | spectral interval conclusions need enlarged windows (last para) |
| T10 | joint-cutoff/finite-volume-vacuum.md | Hamiltonian gap Δ ≥ e^{−sB}/(s2^N), s=2κ, N=3L³; explicit schedule a_n gives relative gap error ≤180·2^{−n−8}; compact-group extension for the Hamiltonian floor. | JOINT (explicit schedule a_n along any box sequence) | SU(2); floor also any compact connected G | physical time; "At fixed nonzero κ the displayed floor tends to zero as L grows. A positive continuum mass gap remains open." (§intro) | Lean finite-row/oscillation (in 14 decls); 9-state numerical control | "existence, Euclidean covariance and nontriviality of a spatial continuum limit, and a positive lower bound on its physical mass, require further estimates" (last para) |
| T11 | joint-cutoff/energy-density.md | Three-reading combination D(t)=C(t)−2C(2t)+C(3t) detects first-moment spectral mass on a compact positive band; capped electric Wilson insertions approximate it with explicit error; "a persistent three-reading signal … is equivalent to the Hamiltonian band's survival whenever A4's common first-moment bound holds". | CONDITIONAL (hypothesis: A4's uniform first-moment bound, from another lane) | SU(2), 3+1 lattice | γ=κ_A/4=1/(2κ_B) conversion stated (§Capping); "The sign of its limiting signal on the weak bare-coupling trajectory remains undetermined" (§intro) | Lean: cap, three readings, noncommuting products (blocked-time Lean); rotor numerics (blocked-time/execution.md) | sign of limiting signal (§intro); "This refinement does not supply a positive band signal" (end) |
| T12 | spatial-plaquette/README.md | On even L, V=Σ(1−½ReTr U_p) attains 0 and 2N_p; hence inf_c‖I−cB_κ‖=(1−b)/(1+b), b=e^{−κN_p}, which → 1 with volume: the spatial factor is not a small global perturbation. | FIXED (finite even L; obstruction) | SU(2), 3D spatial slice | κ here is the SPATIAL action coefficient; mesh→0 not stated | 1 universal Lean theorem; 1 mutation rejected; norm formula analytic | no conclusion about the normalized transfer gap (§Consequence) |
| T13 | strong-coupling/README.md | 4D Wilson measure, spatial torus L≥2: if tanh β_s, tanh β_t ≤ 1/20, centered transfer norm ≤ 1/3 (sharpened (22−3√35)/13), uniform in L; at fixed physical time all connected matrix elements of bounded-norm vectors vanish as a↓0; for isotropic β≥2/15 the one-link Dobrushin criterion fails. | FIXED (all lattice parameters fixed; uniform in L; open time ends removed) | SU(2), 4D lattice | LATTICE units per step; "The finite-volume energy bound in that clock is (log3)/a" (§From bounded…); "A nontrivial Yang–Mills scaling limit with finite-energy excitations therefore requires a different trajectory" (§intro) | 14 Lean decls (strong-coupling/execution.md); conditional laws, comparison theorem, Haar integrals, density analytic; 5 mutations rejected; incidence enumeration | "nonzero continuum correlations, ultraviolet construction, physical normalization and quantifier over compact simple groups remain open" (§From bounded…); interval between sufficient and obstructed regimes unresolved (end §lower bound) |

Execution logs (no row; used above): execution.md, blocked-time/execution.md, hamiltonian-time/execution.md, joint-cutoff/execution.md, strong-coupling/execution.md.
Lean declarations reported across lane: 9+18+11+14+14 = 66 + 1 (spatial-plaquette) = 67 claimed; NONE re-run by me (the .lean files are not in input/).
Mutations reported rejected: 2+6+4+5+5+1 = 23.

## Lane g4 (delegated to the sub-agent; rows condensed from child/g4_disposition.md, which carries the full quotes)

Paths are relative to input/g4/.

| # | File | Main statement (with hypotheses) | Regime | Group / dim | Units; mesh→0 | Evidence (as reported) | Open (per note) |
|---|---|---|---|---|---|---|---|
| G1 | README.md | Suppose real kernels K_n → K entrywise on a common label set, and each finite test is nonnegative (or eventually nonnegative) at every n. Then K is nonnegative on every finite test. "Neither theorem assumes or establishes a common convergence rate or existence of a convergent regulator trajectory." | CONDITIONAL (hypothesis: a convergent regulator sequence, positive at each cutoff). The 1/(1+s+t) no-gap kernel is a CONTROL. | none (abstract) | dimensionless; not stated | execution.md: 8 thm + 3 def, 11 axiom reports; 1 mutation rejected; no-gap control is text only | §Shared construction contract, items 1–5 |
| G2 | cross-lane-review.md | RP passes to the exact pushforward q_*μ when q is equivariant and preserves the test class. Independent enumeration of C4's cube: 32 patterns ×128, mean weight 8177/2048 vs 15625/4096. | CONDITIONAL (needs μ to be RP upstairs). The arithmetic check is FIXED. | cube sign model; quaternion lifts | lattice; not stated | numerical exact-rational enumeration; identity is text only; D4 covered by source review only | "It establishes neither nontriviality nor a uniform gap" (§C4) |
| G3 | complex/README.md | The complex analogue of G1: "Im Q = 0 and Re Q ≥ 0" is preserved under entrywise limits. Also a finite reflected expansion and an exact finite pushforward. | CONDITIONAL ("Existence of the limit and positivity of the chosen interacting regulator remain separate inputs") | none; finite configuration spaces | dimensionless; not stated | complex/execution.md: 24 thm + 9 def, 33 reports; 4 mutations rejected | §What this does not construct |
| G4 | integral/README.md | Integral version of G1/G3. Wilson normalization on G^E (Z finite and > 0). Finite Gram identity. If the tested Wilson density is a Gram expression, the reflected integral is ≥ 0. | CONDITIONAL (Gram identification; an explicit premise of `reflectedIntegral_wilson_of_gram`) | compact second-countable G, finite E | lattice, dimensionless; "Strict positivity of a fixed-regulator transfer operator does not give a uniform continuum mass gap" | integral/execution.md: 28 thm + 3 def, 31 reports; 5 mutations rejected; matrix-feature expansion and tail bound NOT in Lean | §Coordination, last para: remaining OS axioms, continuum, nontriviality, gap |
| G5 | integral/wilson-kernel.md | Assume X compact, β_p ≥ 0, c_p > 0, and a split kernel Σβ_p c_p ReTr(A_p(x)*A_p(y)). Then ν is a probability and ∫ conj(F(x))F(y)dν ≥ 0 for every continuous F. | FIXED. Applying it to a given lattice is CONDITIONAL on identifying the geometry. | compact G, finite-dim unitary rep | "a finite-regulator result and supplies neither spatial continuum convergence nor a spectral gap" (last para) | text proof only; "not an additional Lean-checked theorem" | §Boundary variables: geometry identification, OS reconstruction |
| G6 | integral/open-slab.md | Finite open temporal chain with free ends, Haar on links, nonnegative temporal coefficients, reflected gauge-invariant end weights. Under these hypotheses the actual Wilson measure is RP for strictly half-supported tests. | FIXED | compact G; spatial graph arbitrary (dim not stated) | "Neither continuum reconstruction, spatial-cutoff convergence, nor a mass gap follows from finite-slab RP alone" | text proof only; a ±1 counterexample forced a hypothesis correction | periodic time excluded; blocked comparisons need a pull-back (§Splitting) |

Totals as reported. g4: 75 Lean declaration reports, 10 mutations rejected. transfer-operator: 67 declarations, 23 mutations rejected. None was re-run by me.

## 3. Lane tables against the requirements

## Lane table: transfer-operator vs. the problem requirements

| Req. | Disposition | Evidence (location) |
|---|---|---|
| (a) continuum limit on R⁴ | PARTIAL: only the time cutoff and spatial volume are removed, at a FIXED spatial mesh (blocked-time/README.md; joint-cutoff/README.md). Spatial refinement gives only obstructions | "Isotropic removal … and reconstruction of four-dimensional Yang–Mills theory remain open" (joint-cutoff/README.md, last para); local-limit.md: on κ=βb with β²≤1/384 the gap diverges and only contact terms survive |
| (b) reflection positivity / OS | ADDRESSED AT FIXED REGULATOR | open-slab time reflection gives the split crossing action (compact-groups.md §"Open time reflection"); positive transfer at fixed L (hamiltonian-time/README.md §Transfer). No other OS axiom is addressed |
| (c) Euclidean invariance | NOT ADDRESSED (negative tests only) | rotation-test failure in the uncoupled model (hamiltonian-time/README.md §"An explicit spatial refinement"); "Euclidean covariance … remain open" (local-limit.md) |
| (d) nontriviality | ADDRESSED AT FIXED REGULATOR | plaquette connected correlation ≥ (5/9)e^{−12t/κ} at fixed mesh (plaquette.md; local-limit.md); "A fixed spatial mesh is essential" (plaquette.md last para) |
| (e) mass gap > 0, physical units | ADDRESSED AT FIXED REGULATOR (fixed spatial mesh; uniform in L and a, in physical *time* units κ) | gap ≥ 4log3/(13κ) (blocked-time/README.md); on the tree-level spatial trajectory it diverges as 1/(βb) (local-limit.md); finite-volume floor → 0 as L grows (finite-volume-vacuum.md). README.md: "No continuum mass gap or Millennium solution is claimed here." |
| (f) all compact simple groups | PARTIAL: every compact connected G with a faithful rep, fixed mesh, non-explicit (G,π)-dependent T, h0 (compact-groups.md); Hamiltonian gap via Yarotsky for compact simple G (hamiltonian-time/README.md); explicit constants only for SU(2) | strong-coupling/README.md: "quantifier over compact simple groups remain[s] open" |

No requirement is CLAIMED for the 4D continuum theory anywhere in the lane.

### g4 vs. requirements (from the sub-agent; checked by me against the files I read)

| Req. | Disposition | Evidence |
|---|---|---|
| (a) continuum limit on R⁴ | NOT ADDRESSED | There is only a preservation lemma that applies once a limit exists. README §Shared contract item 3 lists convergence as an obligation. |
| (b) RP / OS | ADDRESSED AT FIXED REGULATOR (RP only) | RP on the finite open slab (open-slab.md, wilson-kernel.md; analytic). PARTIAL: Lean-checked closure under limits, conditional on the limit existing. The other OS axioms "remain open" (integral/README §Coordination). |
| (c) Euclidean invariance | NOT ADDRESSED | no statement in the lane |
| (d) nontriviality | NOT ADDRESSED | "positive forms may still give a trivial limit" (integral/README) |
| (e) mass gap, physical units | NOT ADDRESSED | Only a control showing that RP plus clustering does not force a gap: K = 1/(1+s+t) (README §Controls) |
| (f) all compact simple groups | PARTIAL | RP at fixed regulator for any compact second-countable G (analytic); group scope is assigned to C4 |

CLAIMED in either lane: none.

## 4. Hypotheses each statement uses, and where they are stated

- **T1:** three sector form bounds with c² ≤ (u−m)(v−m) and u > m (README.md §"What the regulator must supply"). The spectral theorem is "the analytic interface".
- **T2, T4, T5:** SU(2); spatial mesh fixed; L ≥ 2; a ≤ κ/4; z ≤ 1/384; β_t = κ/a, β_s = aλ (blocked-time/README.md ¶1). The Dobrushin comparison is cited, not formalized (blocked-time/execution.md table).
- **T3:** G compact connected with faithful π; a/κ ≤ h0 and κλ ≤ 1/[120(T+1)], where T and h0 exist but are not explicit (compact-groups.md ¶2). Uses the Li–Yau heat bound.
- **T6:** fixed spatial mesh and finite volume for a → 0. The gap needs 8z below Yarotsky's Theorem 1 threshold, to which the note says "We do not assign a numerical value" (hamiltonian-time/README.md §"A volume-independent gap").
- **T7:** z ≤ 1/384 or z ≥ 36; L ≥ 2 (plaquette.md).
- **T8–T10:** ac ≤ 1/36, a ≤ t/2, c = 6λL³ + 6/κ (joint-cutoff/README.md ¶1; evolution.md ¶1). No gap hypothesis.
- **T11:** A4's common first-moment bound, which comes from another lane (energy-density.md §"A comparison", last para).
- **T12:** L even (spatial-plaquette/README.md ¶1).
- **T13:** tanh β_s and tanh β_t ≤ 1/20; open time slabs (strong-coupling/README.md ¶1).
- **G1–G6:** as in the rows above. child/g4_disposition.md quotes each location.

## 5. Failed predicates

None of my predicates failed (P1 and P2 in count_files.py), and the child's g4-count predicate passed.

The lanes record their own failures:
- **transfer-operator:** rejected mutations; the tilt-4 row 2311/1920 > 1 (blocked-time/execution.md); the R = 4 tilt is infeasible (strong-coupling/README.md). These are limits of the authors' own estimates.
- **g4:** the first draft failed elaboration; a CRLF parser bug; a diagnostic-matcher failure (g4/execution.md; integral/execution.md). These were defects of the tooling, not of the statements.
- **g4, open-slab.md §Adverse:** an audit found that end weights must be gauge invariant. This was a defect of the stated theorem, and the note was corrected.

## 6. Contradictions or incompatible conventions without a stated conversion

No outright contradiction was found. These conventions clash with no stated conversion:

1. **κ has two meanings.**
   - transfer-operator/spatial-plaquette/README.md §"Consequence for a transfer estimate": κ is the *spatial* action coefficient, in the multiplier exp(−κV/2).
   - transfer-operator/hamiltonian-time/README.md ¶1, and the rest of the lane: κ is the electric parameter, with β_t = κ/a and β_s = aλ.
   - Read with the lane's usual κ, the spatial-plaquette b = e^{−κN_p} is misread.
2. **γ has two meanings.**
   - hamiltonian-time/README.md §"A volume-independent gap": γ is the Yarotsky gap constant (gap ≥ 3γ/(8κ)).
   - joint-cutoff/energy-density.md §"Capping": γ = 1/(2κ) is the kinetic coefficient.
   - energy-density gives its own conversion to A4's convention but does not address this clash.
3. **The cross-lane coupling normalization differs.**
   - transfer-operator uses exp(β ReTr U_p/2) for SU(2) (strong-coupling/README.md §1) and ReTr π/dim π (compact-groups.md ¶2).
   - g4 uses β_p c_p ReTr with c_p > 0 never fixed (g4/integral/wilson-kernel.md §Statement; open-slab.md §Splitting).
   - No conversion between the β conventions is given. The sign conventions agree: both use exp(+β ReTr), and g4 states its conversion to exp(−S).
4. **The cross-lane time units differ.**
   - transfer-operator states gaps in physical time units of κ (blocked-time/README.md).
   - g4 uses dimensionless slice labels and never relates them to a or to physical time (g4/integral/README.md §Coordination, B4 bullet).
   - The child also lists clashes inside g4: c_p is never fixed, and the weight form behind β = log 2 is not stated (child/g4_disposition.md §Contradictions).

**Points where the lanes agree:**
- transfer-operator/blocked-time/compact-groups.md §"Open time reflection" says it verifies G4's split-action hypothesis for the open slab. This matches g4/integral/open-slab.md.
- Both lanes warn that observables built from blocked or auxiliary-seed variables must be pulled back from Wilson histories.

## 7. Three statements per lane that the lane's own text marks for review

**transfer-operator:**
1. The time-slice-to-spectrum step: the spectral theorem plus density of centered multipliers in the vacuum complement. README.md §1 calls it "the analytic interface"; strong-coupling/README.md §Verification lists it as analytic.
2. The Dobrushin comparison on the lifted bridge measure, together with the open-time limit. These carry the uniform gap; blocked-time/execution.md lists them as "Analytic steps supplied in the notes".
3. Whether Yarotsky's theorem applies, since its threshold is not quantified (hamiltonian-time/execution.md: "applicability of the external stability theorem … analytic"). The Li–Yau minorization behind the general-group extension is in the same position (compact-groups.md).

**g4** (from the child; I checked these against integral/execution.md and open-slab.md):
1. The matrix-feature expansion and uniform tail bound in wilson-kernel.md, which are "not Lean formalized" (integral/execution.md §Corrections).
2. The open-slab identification. It is analytic, and its first audit already found a missing hypothesis.
3. The pushforward RP identity and the conditional reviews of B4 and D4, which are not replays (cross-lane-review.md; complex/README.md §Connection).

## 8. What I did not check

- Whether any proof is correct. This was out of scope.
- Any Lean file. None is in input/, so all Lean and mutation counts are as the notes report them.
- Any external link: the rendezvous issue, the A4/C4/D4 sources, Yarotsky, Lüscher.
- The full text of the 3 g4 execution logs. I grep-checked them for counts only.
- The Python scripts and replays the notes cite.

## 9. Delegated question and outcome

**Question delegated (rule 7):** apply the same extraction template to the smaller lane, input/g4 (9 files). The child was to answer a control question first (−ln tanh 1), work in child/, and keep its own register at child/pcp.

**What came back:** child/g4_disposition.md, with 6 result rows, a requirements table, conventions, and review targets. Its control value was 0.272341, which is correct.

**My checks of the result:**
- I reran child/count_files.py: exit 0, 9 files.
- I reran the child's register verify: "result: PASS (…)".
- I checked 6 rows against the files, one more than the 5 required: README, cross-lane-review, complex/README, integral/README, wilson-kernel and open-slab. **6 of 6 matched**: statements, regime classes, quotes, and the counts (8+3 thm/def with 1 mutation; 24+9 with 4; 28+3 with 5; C4 arithmetic 4096/32/128/8177/2048 and 46/35×6).

**Differences:** none material. The child classed G1, G3 and G4 as CONDITIONAL, which is the stricter reading, and I kept it.

## 10. Commands to rerun

```sh
cd C:/Users/donke/z4-workers/r4-b
export PYTHONUTF8=1
python -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name file-count --expect-exit 0 -- python count_files.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
cd child && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name g4-count --expect-exit 0 -- python count_files.py && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```

The register was created with `pcp_os.py init pcp --principal principal --principal-name "Kirtus Justus"`. The method was reported as not pinned, which is expected. count_result.txt is written only if it is absent, so the result file is never overwritten.

Last line of my `pcp_os.py verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

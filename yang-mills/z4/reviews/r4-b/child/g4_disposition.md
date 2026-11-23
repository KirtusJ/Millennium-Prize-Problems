# G4 lane disposition (extraction only, no correctness judgement)

Inputs read in full: all 9 `.md` files under `input/g4/` (recursive) and `input/yang-mills_README.md`. NOT READ: none. The `.lean`, `.py`, `.json` and evidence files these notes cite are not in the input set. Lean and mutation counts below are what the execution notes say, not what I checked.

Files: `README.md`, `execution.md`, `cross-lane-review.md`, `complex/README.md`, `complex/execution.md`, `integral/README.md`, `integral/execution.md`, `integral/open-slab.md`, `integral/wilson-kernel.md`.
Execution logs (used for evidence only, no rows of their own): `execution.md`, `complex/execution.md`, `integral/execution.md`.

Requirement reference (`yang-mills_README.md`): "a nontrivial quantum Yang–Mills theory on four-dimensional Euclidean space for each compact simple gauge group and prove a strictly positive mass gap."

---

## Per-file rows

### 1. `input/g4/README.md` ("Reflection positivity under a common limit")
- **Main statement:** Take a common label set I and real kernels K_n → K entrywise, for each fixed pair of labels. If every regulator kernel has Q_{K_n}(i,c) = Σ c_a c_b K_n(i_a,i_b) ≥ 0 for every finite test (finite J, map i: J→I, real c), then the limit kernel K has Q ≥ 0 for every finite test. A variant needs each fixed test to be only *eventually* nonnegative, with a threshold that may depend on the test. The note says: "Neither theorem assumes or establishes a common convergence rate or existence of a convergent regulator trajectory" (§Exact question and result).
- **Regime class:** CONDITIONAL. The hypothesis not established in the lane is a regulator sequence whose kernels converge entrywise on a common label set and are positive at each cutoff. The limit index n is abstract and is not identified with time step, volume or mesh. Secondary items: two CONTROL items in §Controls. One is the zero kernel and [[1,2],[2,1]]. The other is the analytic time kernel K(s,t) = 1/(1+s+t), which is RP with normalized correlator 1/(1+t) and no spectral gap: "a time-kernel example, not a Yang–Mills theory or counterexample to the Clay problem."
- **Gauge group / dimension:** None (abstract real kernels). Four dimensions appear only as an outstanding obligation (§Shared construction contract, item 1).
- **Units / mesh → 0:** Dimensionless labels, no units. Mesh → 0: not stated. §Shared contract item 5 requires "uniform positive decay or spectral estimate in physical units" as an obligation.
- **Evidence:** Lean, per `execution.md` §Verified mathematical artifact: "accepted all eight theorems and three definitions". There are 11 dependency reports, using only propext, Classical.choice and Quot.sound, with no accepted sorryAx. The note does not say any analytic step is a hypothesis inside Lean; the elementary statement itself is formalized. Mutation tests: 1 rejected (conclusion changed to strictly negative). The two finite controls "are represented in the Lean source". The 1/(1+s+t) control is text only: "This analytic control is not yet formalized here." The draft came from a hosted model worker, "not an independent reviewer" (`execution.md` §Actual hosted PCP workers).
- **Open (location):** §Controls last paragraph: "Identification of the actual continuum positive-time test algebra and the remaining reconstruction hypotheses stays open." §Shared construction contract items 1–5: build the 4D gauge-invariant regulator, prove RP at each cutoff, find a common continuum test algebra with convergence on one limit, prove the other axioms and the null-space quotient, prove nontriviality and a uniform physical-units gap, and cover C4's group scope. §Shared contract last paragraph: "it does not discharge those limiting requirements."

### 2. `input/g4/cross-lane-review.md`
- **Main statement:** The pushforward transports reflection positivity. Suppose q maps the cover configuration space to the quotient, μ is RP upstairs, ν = q_*μ, q commutes with the specified reflections, and pullback by q preserves the positive-time test class. Then for every admissible complex F whose reflected product is integrable, ∫ conj(F(θ̄y)) F(y) dν = ∫ conj((F∘q)(θx)) (F∘q)(x) dμ ≥ 0 (§C4). The note limits this: "Replacing the shared-edge average by the product of face averages is not justified by this argument."
- **Regime class:** CONDITIONAL. It needs μ RP upstairs, an equivariant q, and preservation of the test class. Secondary items:
  - FIXED: the independent arithmetic check of C4's cube. It enumerates 4,096 edge-sign assignments and finds 32 even face patterns with multiplicity 128. At identity and beta = log 2 the mean weight is 8177/2048, against 15625/4096 for independent faces. It also enumerates quaternion four-tuples: 46 admit commuting lifts, and 35 nonzero patterns occur ×6 each.
  - CONDITIONAL: the source review of D4's spectral criterion. Order: "cutoff limit is taken at each fixed time before the unbounded time sequence" (§D4).
- **Gauge group / dimension:** The C4 check uses edge signs on a cube graph with 8 vertices and 12 edges, plus Hamilton quaternion products over 256 four-tuples. The note says: "The obstruction concerns simultaneous flat periodic lifts, not ... a continuum construction on R4." The pushforward identity is for a general measure space. No continuum dimension is stated.
- **Units / mesh → 0:** Lattice, dimensionless (beta = log 2). The D4 part reports D4's physical-clock convention: "time <= N*a, so a ceiling provides the upper envelope when a > 0. Convergence along rounded physical times remains a separate input" (§D4). Mesh → 0: not stated.
- **Evidence:** Numerical check, an independent Python exact-rational enumeration that "does not call C4's face-incidence implementation". The pushforward identity is text proof only: "an analytic argument here; it is not one of G4's real-kernel Lean theorems". D4 is covered by source review only: "G4 has not replayed D4's Lean file or independently recomputed the six-reading inverse matrix". No mutation tests are reported.
- **Open (location):** §C4 end: "It establishes neither nontriviality nor a uniform gap." §D4 end: "It does not produce D4's uniform decay estimate, spectral identity, or density. A4's nonzero-observable estimates must concern the same regulator, observables, time units and limit."

### 3. `input/g4/complex/README.md` ("Complex reflection positivity on a common test family")
- **Main statement:** The setting is complex kernels K_n → K entrywise on a common label set I, with sesquilinear forms B_K(i;c,d) = Σ conj(c_a) d_b K(i_a,i_b) and Q = B(c,c). If each fixed finite test eventually satisfies "Im Q = 0 and Re Q ≥ 0", with a cutoff allowed to depend on the test, then the limit satisfies it. The note also states three further results: a finite reflected-pairing expansion identity on finite X with arbitrary complex weights and arbitrary θ; exact finite pushforward transport when q∘θ_X = θ_Y∘q, which needs neither injectivity nor surjectivity; and the sesquilinear laws.
- **Regime class:** CONDITIONAL. From §Reflected observables: "Existence of the limit and positivity of the chosen interacting regulator remain separate inputs." The pushforward and expansion identities are FIXED (finite X). The B4 strong-coupling review is CONDITIONAL "on the stated compact, positive self-adjoint physical transfer operator, simple leading eigenvalue and boundary overlaps". The order it records: endpoints first at fixed spatial volume and insertion times, then late insertion times (§Connection).
- **Gauge group / dimension:** None formally (finite configuration spaces). The note says: "Compact SU(2) link configuration spaces are not finite sets" and need a separate integral proof (§Reflected observables). No dimension is stated.
- **Units / mesh → 0:** Dimensionless. Mesh → 0: not stated. "Uniformity in volume belongs to the resulting transfer bound, not to an interchange of these limits" (§Connection). D4's route needs "a common physical transfer variable"; "The new G4 result supplies neither that convergence nor the physical clock."
- **Evidence:** Lean, per `complex/execution.md` §Observed checks: "accepted 24 theorems and nine definitions". There are 33 axiom reports, using only propext, Classical.choice and Quot.sound. Mutation tests: 4 rejected (removed conjugation, discarded reality requirement, removed θ, flipped the −2 witness to +2). Text only:
  - the diagonal-defect example ("not an additional Lean theorem here");
  - the reduction of repeated real labels ("an analytic observation, not a separate formal aggregation theorem");
  - the B4 review ("not a G4 Lean replay or an independent verification").
  The model reviewers are "same provider family, not independent-party mathematical review" (`complex/execution.md` §Recursive PCP workers).
- **Open (location):** §What this does not construct lists: a common continuum positive-time test algebra and its regulator representations, convergence to Schwinger functions, the other reconstruction hypotheses, the null-space quotient and completion, nontriviality, and a uniform physical spectral estimate. §Reflected observables: "The continuum pushforward/integration result and inherited transfer dynamics are not formalized by this finite identity." §Subsequent extension: "does not ... establish inherited quotient dynamics".

### 4. `input/g4/integral/README.md` ("Integral reflection positivity for compact Wilson regulators")
- **Main statement:** The reflected integral pairing is B_{μ,θ}(F,G) = ∫ conj(F(θx)) G(x) dμ. The note gives:
  - a finite-test expansion that assumes every pairwise reflected product is integrable;
  - a kernel-limit preservation result, with the same CONDITIONAL caveats as the complex note: "Neither a common convergence rate nor existence of the desired limit is supplied";
  - exact transport under `Measure.map q μ` for measurable equivariant q;
  - the Wilson law on G^E (compact second-countable G, finite link set E, product normalized Haar, continuous real S), for which Z = ∫ e^{S} dμ₀ is finite and > 0 and the tilted law is a probability;
  - a finite Gram identity, ∫∫ Σ a_r conj(u_r(x)) u_r(y) = Σ a_r |∫u_r|²;
  - a conditional theorem `reflectedIntegral_wilson_of_gram`. If the tested Wilson density on a split configuration is identified with a Gram expression with nonnegative weights, then the normalized reflected integral is real and ≥ 0. The note says: "It is a sufficient criterion, not an assertion that every continuous action has it."
- **Regime class:** CONDITIONAL. The unestablished hypothesis is Gram identification of the tested Wilson density. Wilson normalization is FIXED (finite E).
- **Gauge group / dimension:** Any compact second-countable group G, finite link set E. No spacetime dimension is fixed. The cited Lüscher source is for SU(N).
- **Units / mesh → 0:** Lattice, dimensionless couplings β_p. Mesh → 0: not stated. §Coordination, B4 bullet: "Fixed spatial mesh and volume, the time-continuum limit, the thermodynamic limit and spatial refinement remain distinct operations." §Wilson character: "Strict positivity of a fixed-regulator transfer operator does not give a uniform continuum mass gap."
- **Evidence:** Lean, per `integral/execution.md` §Verification contract: "28 theorems and three definitions", 31 declaration reports passed, allowed axioms only. Mutation tests: 5 rejected (missing conjugation, false zero normalization, omitted partition denominator, reversed Gram signs, false nonintegrable-tilt identity). 2 unused-premise warnings are reported. Analytic steps are explicitly hypotheses in Lean: the Gram identification is an explicit premise of `reflectedIntegral_wilson_of_gram`. "The matrix-entry feature identity, uniform exponential-tail bound and identification with specified lattice crossing plaquettes are not Lean formalized" (`integral/execution.md` §Corrections). The conditioning on boundary variables is "not formalized in this file". The Lüscher representation theory "ha[s] not been formalized here".
- **Open (location):** §Coordination: "The remaining OS axioms, continuum identification, null-space quotient and completion, nontriviality, and a positive mass gap in the same physical units remain open." The D4/Z4 bullet: "supplies neither a physical clock, a coherent cutoff spectral measure, a positive-time decay envelope, nor control of the full vacuum complement." The A4 bullet: "positive forms may still give a trivial limit."

### 5. `input/g4/integral/wilson-kernel.md` ("Wilson holonomy kernels: a direct integral positivity proof")
- **Main statement:** The hypotheses are:
  - X is compact Hausdorff, μ is a nonzero finite positive Borel measure, s is continuous and real, and P is finite;
  - A_p: X → U(d_p) are continuous, with β_p ≥ 0 and c_p > 0;
  - H(x,y) = Σ β_p c_p ReTr(A_p(x)* A_p(y)), W = exp(s(x)+s(y)+H), ν = W(μ⊗μ)/Z, θ(x,y) = (y,x).

  Then 0 < Z < ∞, ν is a probability, and ∫ conj(F(x)) F(y) dν ∈ [0,∞) for every continuous complex F. For X = G^E with product Haar this gives "sufficient for RP of the resulting Wilson measure. Necessity is not asserted."
- **Regime class:** FIXED (finite P, finite half-link set E, compact X). Applying it to a given lattice is CONDITIONAL on geometry identification (§Boundary variables).
- **Gauge group / dimension:** Compact second-countable G with continuous finite-dimensional unitary representations. Explicit example: U(1), ρ(u) = u. No spacetime dimension.
- **Units / mesh → 0:** Lattice, dimensionless β_p, with an unspecified "positive trace normalization c_p". Mesh → 0: final paragraph: "This is a finite-regulator result and supplies neither spatial continuum convergence nor a spectral gap."
- **Evidence:** Text proof only (analytic), reviewed by same-family model workers with one corrected rerun (`integral/execution.md` §Actual PCP worker hierarchy). Line 1: "not an additional Lean-checked theorem". `integral/README.md` §Finite Gram: "The matrix feature expansion and convergence estimate are not yet Lean formalized." No numerics. No mutations specific to this note.
- **Open (location):** §Boundary variables: "exhibit its actual reflection, half-links, treatment of reflection-plane links, shared boundary variables, reflected plaquette orientation, and Haar-preserving coordinate/gauge changes ... This geometry identification and the full OS reconstruction are still separate obligations." Also: "More general disintegrations require their own proof."

### 6. `input/g4/integral/open-slab.md` ("Open temporal slabs: identifying the actual Wilson measure")
- **Main statement:** The hypotheses are:
  - a finite spatial graph and a finite open temporal chain invariant under t ↦ 1−t, with free ends and no periodic identification;
  - compact second-countable G and a continuous finite-dimensional unitary π;
  - normalized Haar on all links;
  - density exp(S)/Z, with S reflection invariant, nonnegative temporal-plaquette trace coefficients, spatial plaquettes and extra end weights in identical reflected pairs, and any end actions bounded, continuous, real, half-supported and gauge invariant;
  - reflection through the bonds between slices 0 and 1;
  - observables that are continuous, gauge invariant and strictly half-supported.

  Under these hypotheses, anchored temporal gauge preserves product spatial Haar at fixed temporal links. The crossing plaquettes become the split matrix-feature kernel of `wilson-kernel.md`. Every admissible positive-half test then has a real nonnegative reflected expectation under the original normalized Wilson measure. In the note's words: "This establishes the finite open-slab integral reflection-positivity application for these hypotheses, analytically."
- **Regime class:** FIXED (finite spatial graph and finite open temporal chain; all cutoffs fixed).
- **Gauge group / dimension:** Compact second-countable G. The spatial graph is finite and arbitrary, so the dimension is not specified (not stated as 4D). The adverse control uses G = {±1} with one spatial edge and two slices.
- **Units / mesh → 0:** Lattice, dimensionless. Mesh → 0: §Splitting, last paragraph: "Neither continuum reconstruction, spatial-cutoff convergence, nor a mass gap follows from finite-slab RP alone."
- **Evidence:** Text proof only: "It is not an additional Lean theorem." There were PCP model audits of the original and corrected text. The first audit found that end weights must be gauge invariant; a "concrete ±1 partition counterexample" gave cosh(β)cosh²(λ) against cosh(β)cosh²(λ)+sinh(β)sinh²(λ), and the statement was corrected (`integral/execution.md` §Corrections; open-slab §Adverse boundary-weight control). The Lean module is unchanged.
- **Open (location):** §Splitting, last paragraph: "Periodic time leaves a residual holonomy and is outside this argument. A reflection plane with fixed links, asymmetric or constrained end data, fresh quotient averaging, a different boundary law, or auxiliary variables in a blocked comparison requires its own identification." Also: "a blocked comparison's test must be pulled back from an actual Wilson history before using this result."

### Execution logs (evidence only)
- `execution.md`: real-kernel Lean (8 theorems, 3 definitions, 1 mutation rejected); a draft model failure that was repaired; a parser CRLF failure that was retained; native QEMU readback controls (6 boots); 3 source-emission guests. It also says: "Successful byte, guard and compiler checks do not establish a Yang–Mills construction."
- `complex/execution.md`: 24 theorems, 9 definitions, 4 mutations rejected, 7 hosted registers replayed.
- `integral/execution.md`: 28 theorems, 3 definitions, 31 reports, 5 mutations rejected, 9 native observations, 15 registers. A first full run was marked failed because of a diagnostic-matcher phrase and was rerun with the source unchanged.

---

## Lane table vs requirements

| Req | Disposition | Basis |
|---|---|---|
| (a) continuum limit on R^4 | NOT ADDRESSED | Only a conditional preservation lemma exists, for the case where some common limit exists (README, complex, integral). README §Shared contract item 3 lists continuum convergence as an outstanding obligation. integral/README: "continuum identification ... remain open". |
| (b) reflection positivity / OS axioms | RP: ADDRESSED AT FIXED REGULATOR, plus PARTIAL | Fixed regulator: finite open temporal slab with free ends, compact G, analytic text proof only (open-slab; wilson-kernel). Partial: Lean-checked closure of finite-test RP (real and complex) under entrywise kernel limits on common labels, plus exact pushforward transport; both conditional on existence of the limit. The other OS axioms are NOT ADDRESSED ("The remaining OS axioms ... remain open", integral/README §Coordination). Periodic time is excluded. |
| (c) Euclidean invariance | NOT ADDRESSED | No statement in the lane. |
| (d) nontriviality | NOT ADDRESSED | Assigned to A4. Zero-kernel control: "Positivity alone supplies no nontrivial state" (complex §Adverse tests); "positive forms may still give a trivial limit" (integral/README A4 bullet). |
| (e) mass gap > 0 in physical units | NOT ADDRESSED | There is a negative control showing positivity, normalization and clustering do not force a gap: K = 1/(1+s+t), in README §Controls, text only. The lane also says "Strict positivity of a fixed-regulator transfer operator does not give a uniform continuum mass gap" (integral/README). |
| (f) all compact simple groups | PARTIAL | The fixed-regulator RP results are stated for any compact second-countable G with continuous finite-dimensional unitary representations (wilson-kernel, open-slab; analytic). Global group scope is assigned to C4 (README line 3). No continuum statement for any group. |

CLAIMED: none. No G4 note asserts any of (a)–(f) for the 4D continuum theory. The lane repeatedly disclaims this, e.g. README line 3: "It supplies no solution of the Millennium problem"; integral/README line 3: "It does not construct the four-dimensional Yang–Mills continuum theory or a mass gap."

---

## Contradictions / incompatible conventions without stated conversion

I found no direct contradiction between two statements. Convention mismatches where the text gives no explicit conversion:
1. **Plaquette coupling parametrization.** `integral/README.md` §Finite compact-group Wilson application writes S = Σ β_p φ_p, with φ_p "continuous real plaquette functions" and the real trace supplying them "analytically". `integral/wilson-kernel.md` §Statement and `integral/open-slab.md` §Splitting write β_p c_p ReTr(A*B), with a separate "positive trace normalization c_p > 0" whose value (for example 1/N, 1/d_p or 2/g²-type) is never fixed. Neither note relates β to a bare coupling g. The open slab has c_e > 0, also unspecified.
2. **C4 cube check beta.** `cross-lane-review.md` §C4 uses "beta = log 2" and "Boltzmann weights" with edge signs, but the G4 text does not state the weight's functional form or sign. That leaves the relation to the exp(+S), β ≥ 0 convention of `open-slab.md` §1 unstated.
3. **Time variable.** `cross-lane-review.md` §D4 reports D4's physical clock, "time <= N*a", with lattice spacing a. Every G4 result note works in dimensionless lattice slice labels, and no G4 note defines a or relates its slices to physical time.
4. Conventions that do have a stated conversion: the real bilinear form (README) and the complex sesquilinear form (complex/README) are related in README §Controls ¶3. The exp(S) and exp(−S_action) sign conventions are related in open-slab §1. The swap reflection θ(x,y) = (y,x) (wilson-kernel) and the reflection through the bonds between slices 0 and 1 (open-slab) are related through the temporal-gauge argument in open-slab §Haar-preserving temporal gauge and §Splitting. The [[1,2],[2,1]] control appears as an unnormalized form Q(1,−1) = −2 in README §Controls and as a normalized expectation −1/3 under uniform base measure in integral/README §Finite Gram. These are different quantities and each is labeled.

## Three statements the lane's own text marks most in need of independent review
1. **The matrix-feature expansion and uniform exponential-tail bound** in `integral/wilson-kernel.md` §Proof, on which the fixed-regulator Wilson RP rests. `integral/README.md` §Finite Gram says: "not yet Lean formalized". `integral/execution.md` §Corrections says: "The matrix-entry feature identity, uniform exponential-tail bound and identification with specified lattice crossing plaquettes are not Lean formalized." The only review was by same-provider static model workers.
2. **The open-slab identification**: temporal gauge preserving Haar, and crossing plaquettes reducing to the split kernel (`integral/open-slab.md` §Haar-preserving temporal gauge, §Splitting). The note says it "is not an additional Lean theorem". Its first audit already found a missing hypothesis, end-weight gauge invariance (`integral/execution.md` §Corrections; open-slab §Adverse boundary-weight control).
3. **The measure-theoretic pushforward RP identity and the conditional cross-lane soundness reviews.** For the identity, `cross-lane-review.md` §C4 says: "an analytic argument here; it is not one of G4's real-kernel Lean theorems". For the B4 review, `complex/README.md` §Connection says: "not a G4 Lean replay or an independent verification of the cited compact-kernel, gauge-projection and comparison theorems". For the D4 review, `cross-lane-review.md` §D4 says: "G4 has not replayed D4's Lean file".

Runner-up: the analytic no-gap control K = 1/(1+s+t), "not yet formalized here" (README §Controls). Across the lane: all model reviews are "same provider family, not independent-party" (complex/execution.md §Recursive PCP workers; integral/execution.md §Actual PCP worker hierarchy).

## Conventions used by the lane (for cross-lane comparison)
- **Action / density sign:** The density is exp(S)/Z, with S including +β·ReTr terms, β ≥ 0. The alternative is exp(−S_action) with opposite-sign trace coefficients (open-slab §1). Z = ∫ e^{S} dμ₀ (integral/README).
- **Base measure:** Normalized Haar on each link, in product form (integral/README, open-slab).
- **Coupling:** β_p ≥ 0 per plaquette times a trace normalization c_p > 0 whose value is not fixed. No relation to g² or to 2N/g² is stated. The C4 check uses beta = log 2, with weight form not stated in G4.
- **Plaquette term:** ReTr π(U h U^{-1} h^{-1}), with π a finite-dimensional unitary representation. A link from v to w transforms as g_v U g_w^{-1} (open-slab).
- **Reflection:** Through the bonds between slices 0 and 1 (t ↦ 1−t), on an open temporal chain with free ends, never periodic (open-slab). The abstract form is the swap θ(x,y) = (y,x) (wilson-kernel).
- **RP form:** ∫ conj(F(θx)) G(x) dμ. The first slot is conjugate-linear. The condition is "Im Q = 0 and Re Q ≥ 0" (complex/README).
- **Units:** Lattice and dimensionless throughout. No lattice spacing is introduced in G4 results. "Physical units" appears only as an obligation (README §Shared contract item 5; integral/README §Coordination).
- **Gap definition:** README's control uses a positive lower support gap of the spectral measure, equivalently C(t) ≤ A e^{−mt} for large t. The cited B4 route uses a simple leading transfer eigenvalue and the D4 route uses spectral-tail and moment bounds, both conditional and owned by other lanes. G4 itself proves no gap.
- **Limit order (as recorded):** Kernel-limit closure is entrywise, with a threshold that may depend on the test and no common rate. For the D4 review, the cutoff limit comes at fixed time before time → ∞. For the B4 review, slab endpoints go first at fixed spatial volume and insertion times, then late insertion times. integral/README keeps "fixed spatial mesh and volume, the time-continuum limit, the thermodynamic limit and spatial refinement" as distinct operations.

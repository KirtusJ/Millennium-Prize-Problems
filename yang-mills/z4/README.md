# The regulator trajectory and its physical units

Director Z4 · 22 November 2026 · B.C. Pacific Time. Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic), acting as Director Z4.

Nothing here constructs a four-dimensional Yang–Mills theory or proves a mass gap. This folder holds one obligation that the other lanes share, two exact controls and one adverse control.

## Lane

The rendezvous asks that the lanes "refer to the same theory, regulator trajectory, physical units and observable algebra". Z4 takes the trajectory and the units: the map from lattice spacing a to bare coupling β(a) along which the regulated theories are compared, and the conversion of a gap in lattice units, m, to a gap in physical units, m/a. A4 holds a nonzero observable, B4 the regulator transfer operator, C4 the global form of the gauge group, D4 the continuum spectral measure, G4 reflection positivity.

Possible overlap, flagged: B4 announced a positive transfer family whose physical gap collapses. The finite-group control below is such a family. Z4 keeps it as a control on the trajectory and makes no claim on B4's operator bounds.

## 1. The scaling obligation (Lean)

Let a_n be the spacings and m_n the lattice-unit gaps of a family of regulated theories. In the Lean statements a and m are arbitrary real sequences; that m is minus the logarithm of a transfer-operator norm is the reading, not a hypothesis.

- `lattice_gap_tendsto_zero`: if a_n → 0, a_n ≠ 0 and m_n / a_n → M for a real M, then m_n → 0.
- `physical_gap_tendsto_atTop`: if a_n → 0 from above and m_n ≥ c > 0 for all n, then m_n / a_n → +∞.
- `not_uniform_lattice_gap_and_finite_physical_gap`: a_n → 0 from above, m_n ≥ c > 0 for all n and m_n / a_n → M real cannot all hold.
- `twoSided_of_tendsto` ([`lean/Z4YM/TwoSided.lean`](lean/Z4YM/TwoSided.lean), from the builder's sub-agent): if a_n > 0 and m_n / a_n → M > 0, then eventually (M/2)·a_n ≤ m_n ≤ 2M·a_n. `twoSided_cluster`: conversely, bounds c·a_n ≤ m_n ≤ C·a_n confine every limit point of m_n / a_n to [c, C]; they do not give a limit.

"From above" means eventually positive. "For all n" in the second statement can be weakened to "eventually" (micro-review, `reviews/micro/Edge.lean`).

Consequence for the map, as corrected after the challenger's report (the first version of this paragraph is quoted in "Review record" with what was wrong in it):

- A lower bound on the gap in lattice units that stays uniform while the spacing tends to zero places the excited spectrum at infinite physical energy. At a coupling that is actually held fixed the spacing does not tend to zero and the theorems say nothing.
- If the physical gap of the full transfer operator converges to a positive number, then eventually (not for every n) the lattice-unit gap lies between two positive multiples of the spacing. This is `twoSided_of_tendsto`, and it is a restatement of convergence, not an independent requirement.
- The lower bound is needed only on the sector that the observable algebra reaches. The challenger's example: U(1) × Z₂ on β = N² has full gap of order 10⁻³⁵⁵⁴ at N = 64 (a vacuum that becomes two-fold), while the spectrum above that pair converges to the U(1) value 1/2. A statement about minus the logarithm of the norm on the whole complement of the vacuum is therefore stronger than a mass gap needs when the vacuum is not unique in the limit. Which sector is meant has to be said by the lane that uses the bound.
- Strong-coupling expansions bound the lattice-unit gap below at small β. The continuum trajectory has β → ∞, outside their range; that, and not the theorems above, is why they do not reach the continuum.

The statements are elementary. They are recorded because the hypothesis they exclude is the natural first one to state.

Files: [`lean/Z4YM/Scaling.lean`](lean/Z4YM/Scaling.lean), [`lean/Z4YM/TwoSided.lean`](lean/Z4YM/TwoSided.lean), checked; see "Execution" below.

## 2. Exact controls in two dimensions

On a cylinder (a circle of N links of length a = L/N, time steps of a) the Wilson transfer operator is diagonal in characters with eigenvalues c_r(β)^N, where c_r are the character coefficients of the plaquette weight. Along β = 1/(g a)² for U(1) and β = 4/(g a)² for SU(2), with g = L = 1:

| Group | Physical gap M(N) at N = 64 | Continuum value g²L·C₂/2 | Approach |
|---|---|---|---|
| U(1), charge 1 | 0.500061048820… | 1/2 | N²(M − 1/2) → 1/4; the distance of N²(M − 1/2) from 1/4 shrinks by 4.29, 4.07, 4.02, 4.00 per doubling (M − 1/2 itself by 4.19, 4.04, 4.01, 4.00) |
| SU(2), spin 1/2 | 0.375011444266… | 3/8 | M − 3/8 shrinks by 4.01, 4.00, 4.00, 4.00 per doubling |

Here the lattice-unit gap m = M·a tends to zero at exactly the rate a, as section 1 requires, and the physical gap has a positive finite limit. Two-dimensional Yang–Mills has no local degrees of freedom and its gap is proportional to the length of the circle; it is a control on units and trajectory and says nothing about four dimensions.

## 3. Control: a finite gauge group on the Lie group's trajectory

Z_n with weight exp(β cos(2πj/n)) on the U(1) trajectory β = N²:

| Group | M(2) | M(4) | M(8) | M(16) |
|---|---|---|---|---|
| Z₂ | 2.68e−3 | 4.05e−13 | 3.29e−54 | 2.24e−220 |
| Z₃ | 2.97e−2 | 1.81e−9 | 3.90e−40 | 1.31e−164 |
| Z₅ | 3.32e−1 | 3.49e−4 | 5.51e−18 | 5.32e−75 |

M(N) agrees with N² k δ e^(−N²δ), δ = 1 − cos(2π/n), k = 1 for n = 2 and 2 otherwise, to within a relative 10⁻⁶ at N = 16 (the measured relative deviation is below 10⁻⁴⁸; the tolerance is loose). The physical gap tends to zero. The same asymptote with k = 2 holds for Z₄ and Z₆ (micro-review and its sub-agent; at N = 2 the ratio for Z₆ is still 0.88). Each of these operators is positive and has a gap at every finite N.

For Z₂ the collapse is proved, not only computed ([`lean/Z4YM/FiniteGroupControl.lean`](lean/Z4YM/FiniteGroupControl.lean)): the one-plaquette eigenvalue ratio is tanh β, and for every real x > 0

- `z2_gap_pos`: −log tanh x > 0,
- `z2_physical_gap_le`: x·(−log tanh x) ≤ 1/(1 + x),
- `z2_physical_gap_tendsto_zero`: with x = (N+1)², N = 0, 1, 2, …, the physical gap tends to zero.

The identification of the eigenvalue ratio with tanh β is not formalized.

The builder proved the general case ([`lean/Z4YM/LevelsControl.lean`](lean/Z4YM/LevelsControl.lean)). For a finite set of K levels c_j with a unique maximum separated from the rest by d > 0, real weights χ_j with |χ_j| ≤ 1 and χ = 1 at the maximum, λ₀(b) = Σ e^(b c_j) and λ₁(b) = Σ e^(b c_j) χ_j: whenever b ≥ 0 and 2K e^(−bd) ≤ 1,

- `levels_gap_le`: 0 < λ₁ ≤ λ₀ and −log(λ₁/λ₀) ≤ 4K e^(−bd),
- `levels_physical_gap_tendsto_zero`: along b = (N+1)² the product b·(−log(λ₁/λ₀)) tends to zero.

Z_n is the case c_j = χ_j = cos(2πj/n), d = 1 − cos(2π/n); that identification is in the file's comment and is not formalized. The constant 4K is not sharp (12 against 3 for Z₃). A maximum attained at several levels is not covered.

What this shows, as corrected. The first version of this paragraph said that an argument which would apply word for word to a finite gauge group "proves too much". The challenger showed that inference to be wrong, and the director confirmed it: β = N² is the trajectory of U(1), not of Z_n. On a trajectory of its own, β ≈ log(2N) for Z₂ (β = 2.079, 2.773, 3.466, 4.159, 4.852 at N = 4, …, 64), the Z₂ physical gap is exactly 1/2 at every N, and for Z_n the higher charges converge to finite values as well. In two dimensions a finite gauge group does have a continuum limit with a positive gap; it is reached at a logarithmic rate in the coupling instead of a power.

What stands is narrower. The trajectory is part of the data and belongs to the group: the same spacing-coupling relation gives 1/2 for U(1) and zero for every finite group with a separated top level (`levels_physical_gap_tendsto_zero`). So an argument that takes the relation β ∝ 1/a² as given cannot be indifferent to whether the group is continuous. And any lane that compares two groups, or a group and a quotient, has to say whether they are compared on one trajectory or each on its own. The control tests the trajectory. It does not test an argument that derives its own trajectory.

## Predicates and verdicts

Fixed in the docstring of [`computation/two_dim_control.py`](computation/two_dim_control.py) before the first run.

| Predicate | Verdict |
|---|---|
| H: closed-form character coefficients equal Haar quadrature to relative 10⁻²⁵ (20 cases) | met; 5 of 5 values of N qualify for each group |
| P1: U(1) gap above 1/2 and the distance of N²(M − 1/2) from 1/4 shrinking by a factor in [3, 5] per doubling, N = 4, …, 64 | met |
| P2: SU(2) gap above 3/8 and shrinking by a factor in [3, 5] per doubling | met |
| P3: Z_n gap strictly decreasing over N = 2, 4, 8, 16 and within a relative 10⁻⁶ of the stated asymptote at N = 16 | met |

Met 4, failed 0, measured only 0. First run: register check K2, exit 0. Rerun in a fresh directory: result file byte-identical, SHA-256 `24939c8dd0ae5925e27abe30b45936a6a0d38ae9456e326f9a3ba476465a9d0f`. Command: `python -I two_dim_control.py <directory containing mpmath>`; Python 3.14.7, mpmath 1.4.1.

Not covered by a predicate of this program: the identification of the transfer eigenvalues with c_r^N, and the continuum values 1/2 and 3/8 (quoted). The identification was since checked by the challenger on actual small lattices: Z₅ with N = 3 (eigenvector residual 5·10⁻¹³) and, by its sub-agent, SU(2) with N = 2 (residual 10⁻¹⁶). Those are two lattices, not a proof.

## Execution

What ran, on the principal's Windows 11 machine:

| Item | Status |
|---|---|
| PCP OS | Python implementation at pcp-os `59f26eb`, workspace created for this subproject; register of 24 events replays (15 at the first round, 20 at the second) with every guard passing and all objects matching (`pcpos verify`: PASS). Copy in [`pcp/register.jsonl`](pcp/register.jsonl). |
| ACR method | Not pinned. The packet on this machine has fingerprint `6b6d3a680f3f`; this build requires `7ff72eed9162`. ACR is not in use; the register holds retrievals, inspections and checks only. |
| Native Rust host, kernel guests | Not available on this machine (no Rust toolchain, no QEMU). Not used. |
| PCP workers, recursive hierarchy | Run after the principal signed the `claude` program in. Three headless workers (challenger and builder on Opus, micro-review on Sonnet), each started by the director through `pcpos check` (register checks K6, K7, K8, exit 0) from [`reviews/launch.sh`](reviews/launch.sh), each with its own PCP register, and each with one sub-agent below it holding a register of its own: three levels, director, worker, sub-agent. All six worker registers replay (chain intact). Every worker answered the known-answer control correctly (key hashed before launch, `reviews/control_answer.sha256`). The first version of this folder (commit `a44dede`) was written before any worker ran. No chat, browser or app sub-agent was used by the director. |
| Lean | Lean 4.19.0 (`6caaee842e94`), Mathlib `c44e0c8ee63c` from its cache, built outside the repository. `lake env lean` exit 0 for `Scaling.lean` (register check K3) and `FiniteGroupControl.lean` (K4); `LevelsControl.lean` and `TwoSided.lean` were compiled by the builder in its register and again by the director (exit 0, no `sorry`). All reported theorems depend on `propext`, `Classical.choice`, `Quot.sound` only. Failed first drafts: the director's `FiniteGroupControl.lean` (a `ring` after `field_simp` with no goals left) and the builder's `LevelsControl.lean` (three errors, compiled outside its register). In `twoSided_cluster` the hypotheses 0 < c and c ≤ C are unused. No mutation test was run. |
| GitHub | Check-in posted on [issue 1](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7091105974) once the browser pane was signed in. |

## Review record

Reports, programs, result files and registers of the three workers and their sub-agents are under [`reviews/`](reviews/). The director reread each report, recompiled the three Lean files the workers wrote, replayed the six registers and recomputed the challenger's own-trajectory values for Z₂.

| Worker | Verdicts | Carried into this file |
|---|---|---|
| Challenger | 10 stand (4 with remarks), 3 defects, 0 not checked | The three defects were all in the director's prose and are corrected above: the "must … two-sided bounds along the trajectory" sentence, the strong-coupling sentence, and the "proves too much" inference. |
| Micro-review | 8 of 8 cases stand; two wording gaps | P1 and P3 wording in the table; the weaker hypothesis "eventually"; Z₄ and Z₆; the bound 1/(1+x) is loose by a factor of at least 1.67 and is not claimed to be tight. |
| Builder | finite-level theorem proved; two-sided statements proved by its sub-agent; one wording defect (the same sentence as the challenger's) | `LevelsControl.lean`, `TwoSided.lean`. Its paragraph on a four-dimensional analogue is a suggestion and is not adopted here. |

The first versions of the two corrected paragraphs, kept:

> Any route to a positive finite gap must control m_n from both sides at the rate a_n: two-sided bounds c·a_n ≤ m_n ≤ C·a_n along the trajectory. The strong-coupling expansions give m bounded below at small β and so cannot serve at fixed β.

> An argument for a continuum gap that uses only positivity of the transfer operator, a gap at each cutoff and the spacing-coupling relation, and that would apply word for word to a finite gauge group, proves too much.

The check-in comment on issue 1 repeats the second sentence; a correction is posted there.

Failed predicates in the workers' own programs (none through a defect of the target): the challenger's first reading of "remainder" and a logarithm that underflowed at 10⁻²²⁰; its sub-agent's quadrature agreement at 2.75·10⁻¹² against a tolerance of 10⁻¹²; the micro-review's sub-agent at 320 digits, passed at 900. All are kept in `reviews/`.

Director, workers and sub-agents are one model family. Their agreement reduces exposure and is not independent review.

## What is open

1. In four dimensions the trajectory is not known in closed form. The expected one is asymptotic freedom, a(β) ~ exp(−β/(2 b₀ N_c))·(power of β); no proof exists that the lattice-unit gap vanishes at that rate, from either side. This is the obligation of section 1 in the case that matters, and it is untouched.
2. What distinguishes the Lie group from its finite subgroups. In two dimensions it is the trajectory: a power of the spacing for the Lie group, a logarithm for a finite group, because the low levels of the weight are continuous in one case and separated in the other. Whether a four-dimensional finite-group theory has any trajectory with a continuum limit is not addressed here.
3. A4's sufficient condition (variance bounded below, first energy moment bounded above, both in physical units) can be read off in these controls for the simplest centered vector, the character χ₁ of the spatial holonomy. It is an exact eigenvector of unit norm, so its spectral measure is a unit atom at M(N) and its first moment is M(N). For U(1) and SU(2) the moment is bounded (by M(4)) and the atom converges to 1/2 or 3/8: A4's hypotheses hold and the limit has a gap. For Z_n on the U(1) trajectory the hypotheses hold as well, the moment tends to zero, and the correlator at every positive time tends to 1: the observable survives and the gap does not, so A4's condition is not by itself a condition for a gap (A4's note says the same). This is the case A4's note marks for scrutiny (moment zero, vacuum degeneracy). It follows from the table in section 3 and has no predicate of its own. The same reading for a Wilson loop of fixed physical size, which is not an eigenvector, is not yet done.

## Cross-read of A4's `observable-normalization/SeparatedTime.lean`

At blob `399a8481d5ac`, on this machine: `lake env lean` exit 0, both theorems on the three standard axioms (register check K5), same Lean and Mathlib revisions as A4's receipt. This reproduces the compilation only. Reading of the statements: `momentLowerBound` uses neither E ≥ 0 nor t ≥ 0; the note's upper bound C_n(t) ≤ V does use E ≥ 0 and t ≥ 0, and is not in the Lean file. The guest-boot provenance in A4's receipt was not examined.

All checks here were made by one model family. Agreement with the other directors' readings reduces exposure and is not independent review.

## Second round: A4's and B4's fixed-mesh bounds in physical units

Later on 22 November 2026. Three further workers (register checks K9, K10, K11), each with one sub-agent and its own register; all six registers replay. Reports, programs and results are in [`reviews/r2-b4/`](reviews/r2-b4/), [`reviews/r2-audit/`](reviews/r2-audit/), [`reviews/r2-char/`](reviews/r2-char/). The director reread each report, recompiled the two new Lean files (K12, K13, exit 0, standard axioms only, no `sorry`), reran the challenger's enumeration in a fresh directory (bytes identical) and recomputed one row of the table below by hand.

### The trajectory audit (Z4's lane applied to the other directors' results)

Conventions, derived from the two texts and found consistent: B4's H = (1/2κ_B)ΣA_e + λΣ(1 − φ_p), A4's κ_A = 2/κ_B, g = z/2. On B4's bare tree-level matching with spatial spacing b: κ_B = βb, λ = β/b, z = β², g = β²/2. The coefficients carry 1/length, so the bounds below are already physical energies.

| Quantity | In (β, b) | b → 0 at fixed β | b → 0 with β = c·log(1/(bΛ)) |
|---|---|---|---|
| B4 small-z gap bound 3γ/(8κ_B) | 3γ/(8βb), for β² below an unquantified threshold | ∝ 1/b | trajectory leaves the regime |
| B4 M/v ≤ 12/κ_B | 12/(βb), for β ≤ 0.051 | ∝ 1/b | leaves the regime |
| B4 large-z first moment | between 3/(4β²b) and 48/(β²b), β ≥ 6 | ∝ 1/b | diverges like 1/(b·log²) |
| A4 lower endpoint L = A/16 | 9/(64βb(1+B)) | ∝ 1/b | ≈ 0.0936/(β²b), diverges |
| A4 upper endpoint U = 4D/A | 64(6+8√B)²(1+B)/(9βb) | ∝ 1/b | ≈ 1028·β/b, diverges |
| A4 weight w = A²/(8D) | 81/(512(1+B)²(6+8√B)²) | constant | ≈ 7.3·10⁻⁴/β³, tends to 0 |

B = min{β²/2, 17β/(8√2) + 3/16}. With c = 1, Λ = 1 (illustrative, not a claim about the real trajectory): at bΛ = 10⁻⁴ the window is [10.2, 1.5·10⁸] with weight 5.4·10⁻⁷; at 10⁻⁸ it is [2.6·10⁴, 2.6·10¹²] with weight 8.2·10⁻⁸.

Proved in [`lean/Z4YM/TrajectoryAudit.lean`](lean/Z4YM/TrajectoryAudit.lean), for real β > 0, b > 0:

- `L_lower`: L ≥ (9/64)/(β(1+2β)b).
- `w_upper`: w ≤ 9/(512(1+β)²) for every D ≥ 36κ_A² (covers A4's D and D_*).
- `L_tendsto_top`: if β_n(1+2β_n)b_n → 0 then L_n → +∞.
- `w_tendsto_zero`: if β_n → ∞ then w_n → 0.
- `L_bounded_forces`: if b ≤ b₀ and L ≤ C then β²b ≥ min(c/4, c²/(4b₀)), c = 9/(64C).
- `complementary_needs_b_bound`: without b ≤ b₀ the last statement is false (β = 1/n, b = n).

What this shows. On every trajectory with b → 0 and β growing more slowly than b^(−1/2), in particular at fixed β and on any logarithmic (asymptotic-freedom-like) trajectory, the whole interval in which A4 locates plaquette spectral weight leaves every fixed physical window, and if β → ∞ the guaranteed weight tends to zero. B4's volume-uniform gap lives at β below a fixed threshold and is of order 1/b there. These are the bounds their authors say they are, at a fixed mesh; A4's and B4's notes both state that the scale is 1/b on this trajectory. The audit adds the lower endpoint, the weight, the exact condition β²b bounded below, and the machine check. It says nothing about the true spectrum, only about what these bounds guarantee. The single lattice plaquette is an observable of size b; a statement in a fixed physical window needs an observable of fixed physical size with a renormalization factor, and every one-link or one-face estimate redone at that size. That is a suggestion of the worker, not a result.

Not checked: A4's coefficient chain 336, 1152, 1200, C_K; whether tree-level matching is the right trajectory. The third-moment improvement D_* < D takes effect only for β > 862.

Defect of the director's own brief, kept: the brief asked for "L_n bounded only if β_n²b_n is bounded below" with no bound on b. That is false as stated; the worker refuted it in Lean and proved the corrected form.

### Challenge of B4's Hamiltonian time limit, as B4 requested

Thirteen items, none broken ([report](reviews/r2-b4/report.md)).

- Winding-cycle threshold 3·min(L,4)/(2κ): enumeration of all edge labellings n_e ∈ {0,1,2} within the threshold with the SU(2) fusion test at every vertex. L = 2: 301 enumerated, 12 nonempty admissible, minimum cost 6, attained exactly by the 12 parallel-link pairs. L = 3: 88 723 enumerated, 27 nonempty admissible, minimum 9, exactly the 27 winding triangles. L ≥ 4 by derivation only.
- Block hypotheses: fourfold cover, rescaling 8κ/3, unit block gap, ‖v_x‖ ≤ 8z and the plaquette supports checked exactly for L = 2, 3, 4. Yarotsky's hypotheses as stated in the paper admit a term acting on a block, infinite-dimensional sites and unbounded classical terms. Caveats: the worker did not check that the paper's proof holds on periodic cubes of side 2 or 3, and the threshold and γ are not quantified (B4 says so).
- Rotation control: the computation stands. Remark: the Hamiltonian is not rescaled as b → 0, only the smearing is refined, so the failure of the z↔t rotation is built in for any uncoupled anisotropic regulator; "spatial refinement" overstates it.
- plaquette.md, first section: s ≥ 2/3, v ≥ 5/9, M = (2/κ)(4 − s), M/v ≤ 12/κ stand; the one-plaquette identity was confirmed numerically to 4·10⁻¹⁵ by the sub-agent and rerun.
- B4's `HamiltonianTime.lean` recompiles (exit 0, standard axioms). It proves real-number algebra and finite sums; the trace-distance step and the energy identity are hypotheses there.

One failed predicate, the worker's own expectation (monotone Riemann error), kept. Not checked: B4's time-limit and compactness argument, the large-z section, the general-group extension.

### The character eigenvalue step, abelian case

Section 2 used, without proof, that the transfer eigenvalues are c_r^N. [`lean/Z4YM/CharTransfer.lean`](lean/Z4YM/CharTransfer.lean) proves, for any finite group G and any multiplicative ψ : G → ℂ:

- `conv_char`: convolution by w maps ψ to c_ψ·ψ, c_ψ = Σ_y w(y)ψ(y⁻¹).
- `iterate_char`: the N-fold iterate maps ψ to c_ψ^N·ψ.
- `iterate_eq_kern`: the iterate is convolution by the chain kernel Σ w(g₁)w(g₁⁻¹g₂)⋯w(g_{N−1}⁻¹x).
- `coeff_real_even`, `coeff_eq_lam1`, `coeff_one_eq_lam0`, `iterate_eq_lam1_pow`: for a real even weight and a unitary ψ the coefficient is the `lam1` of `LevelsControl.lean`, and `lam0` for ψ = 1.

Commutativity was not needed. Numerical check on Z₂×Z₄ (sub-agent, rerun, bytes identical): the 8 eigenvalues of T³ are the c_ψ³. Still not proved: that the characters exhaust the spectrum; the reduction from the lattice transfer operator to the N-fold convolution (gauge fixing, integrating the time links); anything for characters of dimension above one, so SU(2) remains a numerical check on one lattice.

Counts for the round, as met, failed, measured only. Challenger programs 24, 1, 2 and its sub-agent 49, 0, 0; audit table program 36, 8, 8 (the 8 failures are one predicate the worker expected to fail: D_* < D on the grid) and its sub-agent 61, 0, 0; formalizer numerics 5, 0, 0. Lean: 13 new theorems, first drafts of both files failed and were fixed (the failed draft of `CharTransfer.lean` is kept in `reviews/r2-char/`). No mutation test was run.

Director, workers and sub-agents are one model family; this is not independent review. Nothing here constructs a four-dimensional theory or bounds its gap.

## Third round: mutation tests, a fixed-size observable in the control, B4's joint cutoff

Later on 22 November 2026. Three workers (register checks K14, K15, K16), each with one sub-agent and its own register; all six replay. Reports and files: [`reviews/r3-chaos/`](reviews/r3-chaos/), [`reviews/r3-fixed/`](reviews/r3-fixed/), [`reviews/r3-joint/`](reviews/r3-joint/). The director reread each report, recompiled the new Lean file (K17, exit 0, standard axioms) and reran two of the challenger's programs in a fresh directory (bytes identical).

### Correction to the director's comment on issue 1

The comment summarizing the second round said that on every trajectory with β = o(b^(−1/2)), "including fixed β", the guaranteed weight vanishes. That is wrong for fixed β: there the lower endpoint diverges and the weight stays constant; the weight tends to zero only if β → ∞. A4 pointed this out on the thread. The table and the Lean statements in the section above were right; the summary sentence was not. Kept here; acknowledged on the thread.

### Mutation tests of this folder (first time)

Baseline: the six Lean files compile unchanged (6 of 6), the control program reproduces its result file byte for byte.

- Lean, 23 single mutations of theorem statements over the six files: 19 rejected; 1 accepted and true (dropping 0 < c in `twoSided_cluster`, a hypothesis already known to be unused); 3 rejected although the mutated statement is true by the worker's numerical scan or argument (`z2_physical_gap_le` with 1/(2+x); `coeff_real_even` without ‖ψ‖ = 1; `w_upper` with 8/512). No false statement compiled.
- Ten of the 19 rejections are "unknown identifier": the proof names the removed hypothesis. Such a rejection is mechanical and does not show the mutated statement false. The statements whose falsity rests on a counterexample are those with a changed constant or direction (for example 4K → 2K in `levels_gap_le`, 9/64 → 10/64 in `L_lower`).
- Statements weaker than they could be, none false: `twoSided_cluster` (unused 0 < c, c ≤ C, StrictMono φ), `z2_physical_gap_le`, `coeff_real_even`, `w_upper`.
- Control program, 7 mutations: 5 caught by the predicate expected (wrong Bessel order, β = N²+1, SU(2) coupling 2N², halved asymptote constant). **Not caught: 2**, both loosened tolerances (the H tolerance and the P3 tolerance each multiplied by 10⁶): exit 0 and a byte-identical result file. A changed digit in a copy of the result file is noticed by nothing except a rerun and byte comparison.

Defect of this folder's check design, open: the tolerances are not written into the result file and the program has no negative control, so a loosened tolerance is invisible. To be fixed by writing the tolerances into the result and adding a perturbed closed form that must fail H and a ratio 1 + 10⁻⁵ that must fail P3. Not yet done; the published result file is unchanged.

### A fixed-physical-size observable in the two-dimensional control

"What is open" item 3 asked for the Wilson-loop reading. Outcome ([report](reviews/r3-fixed/report.md)):

- The loop gives nothing new. W = (c₁/c₀)^(A·N²) exactly, so −log W/A = M₁(N) for every area: the string tension at each N is the gap of the table in section 2, by identity and not by a separate limit. 123 of 183 (N, A) cases qualify (A·N² an integer); all agree to 5·10⁻⁶¹. This confirms the table and does not test it independently. The loop formula itself is taken from the character expansion, not checked on a lattice.
- Observables that are not eigenvectors do add something. For f = (χ₁+χ₂)/√2 and for a centered heat-kernel bump of fixed width, the first and second spectral moments in physical units decrease with N over N = 4..64 and converge: U(1) (5/4, 17/8), SU(2) (11/16, 73/128) for the first; (2.9735, 14.754) for the bump on SU(2). So A4's kind of condition holds with constants of order one in physical units at fixed physical size, in contrast with the single-plaquette bounds of the second round, which scale like 1/b. Boundedness beyond N = 64 is measured, not proved.
- Why it works here and what would fail in four dimensions: on β ∝ 1/a² each c_r/c₀ → exp(−C_r g² a²/2), so a fixed combination of characters has fixed weights and convergent energies, with no renormalization factor. In four dimensions the loop has a perimeter self-energy, smeared observables need a factor Z(b), and the trajectory is logarithmic.
- `lean/Z4YM/WilsonLimit.lean`, `wilson_area_limit`: if ρ_N > 0, N²·(−log ρ_N) → σ and n_N/N² → A, then ρ_N^(n_N) → exp(−σA). ρ ≤ 1 was not needed.
- Finite groups: on β = N² the loop tends to 1 (Z₂ at N = 8, A = 1: 1 − 3.3·10⁻⁵⁴); on Z₂'s own trajectory β_N = artanh(exp(−1/(2N²))) the tension is exactly 1/2. Z₃'s own trajectory was measured only.

One failed predicate, kept: the worker's 10⁻³ tolerance on the U(1) bump's second moment at N = 64 (observed 1.02·10⁻³); its own expectation, since the correction grows like r⁴/N² with the charge.

### Challenge of B4's joint time and volume cutoff, as B4 invited

Fifteen items stand, two minor defects of wording ([report](reviews/r3-joint/report.md)).

- The bound 90·a·c² on the two lowest energies and 180·a·c² on the gap, c = 6λL³ + 6/κ, a·c ≤ 1/36: units consistent (κ a time, λ an energy), arithmetic rederived, and on an exactly solvable one-plaquette model 39 of 39 checks met, with the observed gap error at most 2.6·10⁻⁴ of the bound. The adaptation of c to one plaquette is not forced by B4's text, so that comparison is measured only.
- Units, the statement addressed to Z4: on κ = βb, λ = β/b with physical side ℓ = Lb, c = 6βℓ³/b⁴ + 6/(βb). a·c² → 0 exactly when aβ²ℓ⁶/b⁸ → 0 and a/(β²b²) → 0. "aβ²/b⁸ → 0 suffices" is true when β is bounded below and ℓ is fixed; without a lower bound on β it fails (β = b⁴, a = b). B4's note has β → ∞.
- The finite-volume gap floor d = e^(−sB)·2^(−N)/s is log d = −(12β² + 3 log 2)(ℓ/b)³ − log(2βb): at ℓ = 1 its decimal logarithm is about −219 at L = 2 and −1.7·10⁷ at L = 64. It tracks the gap; it is not a bound on the gap in physical units, as B4 says.
- Heat density in [2/3, 4/3] at s = 2κ: 0.804 to 1.202 in the note's normalization; with the other eigenvalue convention n(n+2)/4 the window fails (0.0088 to 4.55), so the constants are tied to the stated metric.
- The moving vacuum-energy shift is controlled by the same level bound and needs no separate hypothesis.
- Defects for B4, minor: "fixed physical box size L = O(1/b)" conflates the lattice side with the physical side; the individual-energy bound needs the unnormalized transfer operator, whereas the earlier note normalizes by the leading eigenvalue (the gap bound is unaffected).
- B4's `JointCutoff.lean` recompiles (exit 0, 14 declarations, standard axioms); it covers scalar and algebraic steps, and the min–max step, the kernel bounds, the heat density and the minorization are hypotheses there.

Counts for the round, as met, failed, measured only: joint-cutoff programs 59, 0, 2; fixed-size program 12, 1, 3 and its sub-agent 3, 0, 0. Mutations: 24 caught, 3 not caught, 1 accepted as true, and 3 Lean mutations rejected though true.

Director, workers and sub-agents are one model family; this is not independent review. Nothing here constructs a four-dimensional theory or bounds its gap.

## Overall disposition

Gathered on 23 November 2026 at the principal's request: [`OVERALL_DISPOSITION.md`](OVERALL_DISPOSITION.md), covering every lane of this problem and the two external claims, with the extraction reports in `reviews/r4-a`, `r4-b`, `r4-c` (register checks K18 to K20; the register now holds 27 events).

## Fourth round: an observable of fixed physical size

Direction chosen by the principal after the overall disposition. Statements, benchmark, Lean file and review record: [`fixed-size/STATEMENT.md`](fixed-size/STATEMENT.md). In short: on the free lattice Maxwell benchmark the sharp-time smeared action density has variance growing like b^-5 and no limit as a vector, while its time-regularized version converges with energy moments bounded in physical units, and shows no gap; `lean/Z4YM/HeatRegularized.lean` proves that for such vectors norm, moments and a bounded energy window follow from two values of the positive-time correlator. Six defects of the draft were found by the workers and are corrected there with the draft kept. Register checks K21 to K25; the register holds 32 events. No estimate for the interacting theory.


## Fifth round: loop normalization on the benchmark; challenges of B4's heat trace and D4's electric scale

23 November 2026. Three workers (register checks K26, K27, K28), each with a sub-agent and its own register; all six replay. The loop benchmark and its review record are in [`fixed-size/WILSON_LOOP.md`](fixed-size/WILSON_LOOP.md). Reports: [`reviews/r6-loop/`](reviews/r6-loop/), [`reviews/r6-heat/`](reviews/r6-heat/), [`reviews/r6-elec/`](reviews/r6-elec/). The director reread the three reports and reran the loop program (K29, bytes identical). The two challenges below read the other directors' notes only; their Lean files and programs were not replayed.

### B4's charged spatial heat trace (`transfer-operator/spatial-heat-trace`)

This is the first result in the repository stated on the weak-bare-coupling trajectory. Nine items stand; no mathematical defect was found in the SU(2) proofs read.

- The theorem, restated: fixed physical Dirichlet region and diffusion time s, x = s/b² → ∞, couplings with 1 + β_s + β_t = x^{o(1)}; then −log E F_s = x^{3/5 + o(1)}. One limit, b → 0 along a coupling trajectory, with bounds uniform in the enclosing volume. It is a statement about a lattice expectation; no continuum object appears.
- The upper bound, its constants and the choice m = 2⌈x^{1/5}⌉ were rederived by hand and by program (constant c = 1/132000; 3000 of 3000 random SU(2) cubes within the stated floor). The lower bound by a nearly flat cube was rederived for SU(2).
- β = c·log(1/b) satisfies the hypothesis. The convergence is slow: on β = log(1/b) the explicit upper bound says nothing for b ≥ 10⁻³, and at b = 10⁻⁵⁰ it confines the exponent only to [0.549, 0.619]. If B grows like x^γ the bounds give only a window [min(3/5, 1 − γ), (3 + 2γ)/5].
- Units: E F_s vanishes faster than any power of b. The spectral statement puts the probe's normalized weight above x^η/a for every η < 3/5, that is above s^η·b^(−(1+2η)) in physical units on the isotropic trajectory: beyond the cutoff scale by the factor x^η. It concerns this one vector sequence under every deterministic affine renormalization; it says nothing about field-dependent subtractions or other observables, and B4 says so.
- The decorrelation bound is uniform in every lattice separation, so it does cover fixed physical time; it is a bound on the correlation coefficient. See `fixed-size/WILSON_LOOP.md` for why that leaves the mean-normalized covariance undecided.
- The Hamiltonian first-moment bound is on the unnormalized weight and nothing bounds the norm of the vector from below, so it does not control a normalized fraction.
- Minor defects for B4: the summary says "compact connected simple" where the proof file uses "compact connected" and never uses simplicity; several symbols carry two meanings (F_t and F_s, U, V, κ_B and B).
- Not checked: the general-group exponent (a sketch resting on a Łojasiewicz-type argument), and everything in files outside the folder.

### D4's electric scale (`spectral-support/electric-scale`)

Four items stand, one is not checked, three summary sentences are stronger than or mixed with their theorems.

- Convention: D4's κ is 2/κ_B and its g is β²/2, as A4's; `dimension.md` uses a second ratio g_G = 4g. Consistent once stated.
- One-link dimension of order g^(d/4): on a single SU(2) rotor (a proxy, not the cubic vacuum) the number of shells needed for 90% and 99% of the weight grows like g^0.256 and g^0.261 and the full link dimension Σ(n+1)² like g^0.724 and g^0.747, against 1/4 and 3/4; the entropy offset settles at 0.166. The exponent d/4 is for the full link dimension. The lattice statement itself was read and not tested.
- Clocks: the magnetic clock is t = τb/β and the mesh clock is t = τb. Both tend to zero in physical time, at fixed β and on β = c·log(1/b). So "survives on the mesh clock" means survives at times of order b, energies of order 1/b; the class-probe floor is spectral weight at energies up to 2M/(vb). `class-probes.md` says the time vanishes; the summary in D4's README does not.
- The class-probe scale: λh² = √2/b exactly, independent of β; the exponent is dimensionless; the width s·g^(−1/4) matches the rotor width.
- The center-flux statement needs β → ∞ and a marked set fixed in lattice units (a region of physical size of order b); with those it is uniform in volume. At fixed β it does not follow, and for a set of fixed physical size nothing is proved. D4's README sentence "along bare refinement" omits both hypotheses; `center.md` states them.
- The third sentence, opening `class-probes.md`, sets a fixed-physical-time statement beside a τ-clock statement; read literally the probes survive where center flux dies, but center flux also dies at mesh times.

Counts, as met, failed, measured only: heat-trace programs 14, 1, 3; electric-scale programs 18, 1, 2; the two failures are the workers' own tolerances.

### Reading

Three lanes now have statements at weak bare coupling, and all three are of one kind: a named probe, normalized at one time, has its weight at or beyond the cutoff scale. B4's heat trace escapes above x^η/a; D4's surviving family lives at 1/b; A4's bands were audited in the second round. None is in a fixed physical window. The benchmark of this folder shows the same behaviour in a free theory for sharp-time normalization, and shows that a positive-time or mean normalization of a fixed-size observable does have a limit there. No lane has yet stated a result for such a normalization on the interacting lattice.

Director, workers and sub-agents are one model family; this is not independent review.


## Sixth round: a sharper band found by the wildcard, measure forms in Lean, the check repaired

23 November 2026. Three workers (register checks K30, K31, K32), each with a sub-agent and its own register; all six replay. Reports: [`reviews/r7-wild/`](reviews/r7-wild/), [`reviews/r7-meas/`](reviews/r7-meas/), [`reviews/r7-fix/`](reviews/r7-fix/). The director reread the three reports, rederived the wildcard's proof by hand, recompiled both new Lean files (K33, K34, exit 0, standard axioms) and reran the repaired program in a fresh directory (bytes identical, and its verify mode against the worker's result: 281 leaves, 0 differences).

### Correction to the second round, found by the wildcard worker

The second round said of A4's window: "the exact condition β²b bounded below" (this file, section "Second round", and the Z4 row of `OVERALL_DISPOSITION.md`), and the thread comment repeated it. That is exact only for A4's particular lower endpoint L = A/16. The Lean statements `L_bounded_forces` and `L_tendsto_top` are about that L and remain true; the prose presented a property of one choice of endpoint as a property of the band. Kept as written above; scoped here.

### A4's fundamental band, sharpened (favourable; for A4 to adopt or refute)

With A4's own inputs the lower endpoint can be taken at a fixed fraction of the electric scale, uniformly in the magnetic coupling.

- Var F = 4·Var x ≤ 4·E(1−x)² ≤ 8u, because 0 ≤ 1−x ≤ 2. A4's ground-energy identity gives g·u ≤ B(g). So the total mass of the spectral measure is at most K_F = min(4, 8B/g).
- A4's pointwise inequality E ≤ L + E²/U + U·1_[L,U], integrated, gives A ≤ L·K_F + D/U + U·ν([L,U]). With L′ = A/(4K_F) and U = 4D/A: ν([L′, U]) ≥ A²/(8D), the same weight as A4's.
- L′/κ = 9/(32·K_F·(1+B)) ≥ 9/(32·43) = 1/152.9 for every g > 0, since K_F(1+B) ≤ 43 ([`lean/Z4YM/KBound.lean`](lean/Z4YM/KBound.lean), `KB_bound`; the supremum on a grid is 41.6 near g = 18.9).

On the tree-level trajectory κ_A = 2/(βb), so L′ ≥ 9/(688·βb): the band's lower edge leaves every fixed physical window whenever βb → 0, a wider class of trajectories than β²b → 0. Numerically on β = b^(−0.75), L′ rises from 0.048 to 15.6 as b falls from 10⁻² to 10⁻¹², while A4's L falls to 9.4·10⁻⁸. The weight is unchanged, so when β → ∞ it still tends to zero and the window then guarantees nothing in any fixed window whichever endpoint is used. The director checked the three steps by hand and the cited line of A4's note (K_e + g·u ≤ B, each term nonnegative). A4's proofs of that bound and of A and D are taken as given.

Reading across lanes: every positive-energy band guaranteed in the repository now has its lower endpoint at a fixed fraction of the electric scale κ = 2/(βb), uniformly in the coupling ratio: D4's adjoint band at κ/576, C4's smeared adjoint band at δκ/12288, the fundamental band at κ/153. The moment method locates weight at the electric cutoff scale on every trajectory.

The wildcard also checked C4's `momentum/adjoint-refinement.md` by hand (sphere identities, first-moment bound, window algebra, constants 1024, 12288, 1728) and found no fault.

### S5 for measures

[`lean/Z4YM/MeasureHeat.lean`](lean/Z4YM/MeasureHeat.lean): every part of S5 of `fixed-size/STATEMENT.md`, with (f) and (g), for a finite Borel measure ν on ℝ with ν((−∞, 0)) = 0 and C(t) = ∫e^(−tE)dν. Eleven declarations: `M1a`, `M1b` (integrability proved, not assumed; constants 1/(eτ) and 4/(e²τ²)), `M2_tail`, `M2_window`, `M3`, `M4_gap` (no mass in (0, m) gives C(t) − P₀ ≤ e^(−m(t−s))(C(s) − P₀)), `M5_lower`, `M5_no_bound` (mass in (0, m) defeats every bound K·e^(−mt)), `M6` (log-convexity), `exists_Icc_pos`. The sub-agent proved M6 independently by a different route. Hypotheses that turned out unnecessary: E₀ > 0, m > 0, v ≤ V. Mutations: replacing e by 3 in (a) and dropping the support in (b) are rejected and false (counterexamples δ at 1/τ and δ at −1); replacing e by 2 is rejected although true. A point about Lean's integral worth knowing: without integrability the Bochner integral is 0, so a bound can hold vacuously; the statements here prove integrability as part of the conclusion.

This is the form A4, C4 and D4 use (positive measures, not finite sums). The gap criterion (`M4_gap`, `M5_no_bound`) and the two-value reduction (`M3`) are now available to them as stated.

### The check-design defect of the third round, repaired

[`computation/two_dim_control_v2.py`](computation/two_dim_control_v2.py) with its result file; the first program and its published result are unchanged. Tolerances and windows are written into the result with their sources and compared with a hashed table; four negative controls run on every execution (a perturbed closed form must fail H, a ratio 1 + 10⁻⁵ must fail P3, a wrong Bessel order must fail P1, the coupling 2N² must fail P2); a verify mode recomputes and compares an existing result number by number. The 221 numbers common to both programs are identical to the published ones. All eight mutations of the third round are now caught, including the two that passed before and the changed digit. What it still cannot catch: a consistent edit of table, hash and code within the negative-control margins, which only the verify mode against a trusted stored result detects; and an error common to a closed form and its check. The worker's own first run failed its new self-check (precision set after the constants) and is kept.

Counts, as met, failed, measured only: wildcard 6, 0, 2 and its sub-agent 2, 0, 0; measure-form Lean 4, 0, 0 on the final file with failed intermediate compiles kept; repair 11 of 13 register checks as expected (two the worker's own defect, kept).

Director, workers and sub-agents are one model family; this is not independent review.


## Seventh round: free-field known answers for A4's, C4's and D4's weak-coupling statements

23 November 2026. Three workers (register checks K35, K36, K37), each with a sub-agent and its own register; all six replay. Reports: [`reviews/r8-contact/`](reviews/r8-contact/), [`reviews/r8-graphs/`](reviews/r8-graphs/), [`reviews/r8-tangent/`](reviews/r8-tangent/). The director reread the three reports and reran the two free-propagator programs (same numbers to the printed digits). The other directors' notes were read, not replayed: their Lean files and programs were not supplied to the workers.

By now four lanes have statements at weak bare coupling on the four-dimensional Wilson lattice. Each has a leading-order free-field prediction that can be computed exactly. That is what this round supplies. Agreement with a free-field value checks constants and conventions; it is not evidence for the interacting statement beyond leading order.

Free four-dimensional lattice numbers used below (periodic lattice, zero modes removed, per colour, unit coupling): plaquette variance 1/2 exactly in infinite volume and (1 − L⁻⁴)/2 on an L⁴ torus (equipartition, 2/d); parallel plaquettes one step apart 0.06887475; plaquettes sharing a link −0.06887475 coplanar and +0.10778131 perpendicular; lattice Green function at the origin 0.15493339 as the programs' control.

### A4, removable contact variance (`observable-normalization/energy-density/wilson-contact`)

- The theorem, restated: on the isotropic SU(2) Wilson measure, for O_b = (β/b)·Σ f·(1 − x_p) on one slice, an explicit conditional link average removes at least D_b of the variance, exactly at fixed cutoff, and b⁵D_b → (1/36)∫Σ_i(Σ_{j≠i} f)², which is ‖f‖²/18 for one orientation, as β and L → ∞. It bounds the variance removed and the error of any predictor built from outside the slice; it does not give the variance. Readings at time distance two or more are unchanged; distance two is 2b in physical time.
- Conversion, unambiguous: β(1 − x_p) = Σ_a θ_a²/(2g²) + O(g²), so A4's observable is three colours at prefactor ½ of this folder's smeared B². Free total coefficient of b⁻⁵ on the four-dimensional lattice: 0.75·c₄ with c₄ = 0.56258, that is 0.4219·∫f². On the Hamiltonian lattice of this folder c_H = 1.45682: the coefficient changes by a factor 2.59 between the two regularizations, as a contact term may.
- A4's 1/18 = 0.0556 is 13% of the free total. Exact Gaussian conditioning on A4's mask removes 0.13407 = 0.05556 (radial) + 0.07851 (transverse); the radial part is 1/18 to the digits computed. So A4's coefficient is exactly the radial part of the free removable variance, and the transverse part, dropped by A4's estimate, would raise it about 2.4-fold. That is a possible strengthening for A4, not a defect.
- A4's 4⁴ run at β = 2.2 checks the variance identity (3.706 against 2.063 + 1.622, residual 0.021 ± 0.043) and nothing about the asymptotic coefficient; its two-step residual has an error bar a hundred times the signal.
- One sentence of A4's README overreaches: "interacting counterpart of the free magnetic benchmark". The benchmark has an asymptotic equality; A4 has a lower bound on a removable part of a different observable on a different lattice. It is the counterpart of "at least b⁻⁵".
- A side result for this folder: the benchmark constant 8.110·10⁻³ of `fixed-size/STATEMENT.md` equals c_H·(πσ²)^(3/2) = 8.112·10⁻³ for the Gaussian of width 0.1 used there, from an exact lattice sum by a different program: agreement to 0.03%.

### C4, tangent curvature (`central-quotients/tangent-curvature`)

Nine items stand, none broken.

- The theorem, restated: time period to infinity first at fixed β and L, then β and L to infinity jointly; cells fixed in lattice units; the rescaled curvature √β·Im U_p converges, in finite-dimensional distributions and all polynomial moments, to a Gaussian field with covariance the projection onto exact 2-cochains. b never tends to zero. Fixed L with β → ∞ is not covered.
- Known answers: C4's single-face law N(0, I₃/2) against the free value 1/2; C4's time-step covariance 0.06887475 against 0.06887475; C4's single-edge variance 6 against 6.000000; the plaquette action β(1 − x) → χ²₃/4 with mean 3/4 and variance 3/8; the spectral constants 3ε⁸/(2π⁴·8!) and the dipole coefficients rederived by hand. No factor of disagreement anywhere.
- What C4 does not say and could: its limit is the free lattice Maxwell curvature field with three colours. Saying so makes plain that the vanishing gap in lattice units is the photon's, and carries no information about the Yang–Mills gap. C4's own scope sentences are correct: the physical gap is left open and no rate for a physical-time limit is established.
- Not checked: the tightness and Ward-identity steps, the odd-period reflection-positivity construction, the weak convergence of spectral measures, and the two estimates imported from files outside the folder.

### D4 graph holonomies and B4 coarse holonomies

- D4's main theorem, as read: on a graph of fixed positive physical edge lengths, with b(1 + β) → 0, the holonomies converge to product Haar and unit-variance correlations with any other slice vanish. This is a statement at fixed physical size. Its mean-normalization result is for a staple-compensated path, not an ordinary Wilson loop; D4 says it gives no answer for the uncompensated loop.
- D4's thread statement β²C(t) → (3/2)K(t)² for the centered trace of a fixed lattice square is confirmed at leading order: ½Tr W = cos(g|Φ|/2) gives covariance (3/32)g⁴K² = (3/2)K²/β², with K the flux kernel per colour in lattice units (simulation ratios 0.989 and 0.997). The three-loop statement 6·det K(t) is confirmed as the unnormalized covariance. Neither statement was in D4's committed notes at the snapshot read. Free values of K for D4's setting, four-dimensional lattice time n = 1..4: unit square 0.068875, 0.011153, 0.002262, 0.000605; 2×2 square 0.264069, 0.061446, 0.017644, 0.006224. This folder's Hamiltonian-time kernel differs (ratio 0.94 at n = 1, above 1.19 for n ≥ 2) and must not be used for D4's lattice.
- B4's bounds hold at any coupling on a fixed finite lattice for a contour of m lattice links and are independent of the time separation, so they show no decay. Two wordings stronger than the theorems: "sharp uniform threshold" (sharpness is shown for two chosen exteriors) and the physical-unit scaling, which assumes B = O(log(1/b)).
- Coverage, both lanes: no result yet for an ordinary loop of fixed physical size under mean normalization, the object of `fixed-size/WILSON_LOOP.md`.

### Defects of the director's own briefs, kept

- The brief asked the worker to locate D4's (3/2)K² claim "in the notes"; it was on the thread only. The brief also assumed strong-coupling statements in B4's folder that were announced on the thread and not yet committed.
- The brief said the mean-normalized covariance of the SU(2) trace should vanish "like 1/β" at weak coupling. Wrong: the real trace has no linear term, so it is (3/2)K²/β², of order 1/β². The U(1) loop of `WILSON_LOOP.md` has the linear term; SU(2) does not.

Counts, as met, failed, measured only: contact 7, 0, 6 and its sub-agent 7, 0, 3; graphs 12, 2, 5 (the two failures are the brief's wrong premises above) and its sub-agent 4, 0, 0; tangent 9, 1, 6 (one failure the worker's own lattice Green function, corrected and kept).

### Reading

At leading order the four lanes are describing one object from four sides: the free lattice gauge field with three colours. C4 has its curvature law at cutoff scale; A4 has a lower bound on its contact variance; D4 has the square-loop covariance; this folder has its positive-time correlators at fixed physical size. All constants now agree where they can be compared. What none of them has is the first quantity that is not free: a correction of relative order g² to any positive-time correlator at fixed physical size, with control of its logarithm. That logarithm is where the running coupling, and so any physical scale, would first appear.

Director, workers and sub-agents are one model family; this is not independent review.

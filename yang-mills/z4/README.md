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
| PCP OS | Python implementation at pcp-os `59f26eb`, workspace created for this subproject; register of 20 events replays (15 at the first round) with every guard passing and all objects matching (`pcpos verify`: PASS). Copy in [`pcp/register.jsonl`](pcp/register.jsonl). |
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

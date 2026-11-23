# The regulator trajectory and its physical units

Director Z4 · 22 November 2026 · B.C. Pacific Time. Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic), acting as Director Z4.

Nothing here constructs a four-dimensional Yang–Mills theory or proves a mass gap. This folder holds one obligation that the other lanes share, two exact controls and one adverse control.

## Lane

The rendezvous asks that the lanes "refer to the same theory, regulator trajectory, physical units and observable algebra". Z4 takes the trajectory and the units: the map from lattice spacing a to bare coupling β(a) along which the regulated theories are compared, and the conversion of a gap in lattice units, m, to a gap in physical units, m/a. A4 holds a nonzero observable, B4 the regulator transfer operator, C4 the global form of the gauge group, D4 the continuum spectral measure, G4 reflection positivity.

Possible overlap, flagged: B4 announced a positive transfer family whose physical gap collapses. The finite-group control below is such a family. Z4 keeps it as a control on the trajectory and makes no claim on B4's operator bounds.

## 1. The scaling obligation (Lean)

Let a_n > 0 be the spacings and m_n the lattice-unit gaps of a family of regulated theories.

- `lattice_gap_tendsto_zero`: if a_n → 0, a_n ≠ 0 and m_n / a_n → M for a real M, then m_n → 0.
- `physical_gap_tendsto_atTop`: if a_n → 0 from above and m_n ≥ c > 0 for all n, then m_n / a_n → +∞.
- `not_uniform_lattice_gap_and_finite_physical_gap`: the two hypotheses together are contradictory.

Consequence for the map: a gap proved at a fixed coupling, or uniformly in the coupling in lattice units, is the wrong kind of bound. With spacing tending to zero it places the whole excited spectrum at infinite physical energy. Any route to a positive finite gap must control m_n from both sides at the rate a_n: two-sided bounds c·a_n ≤ m_n ≤ C·a_n along the trajectory. The strong-coupling expansions give m bounded below at small β and so cannot serve at fixed β.

The statements are elementary. They are recorded because the hypothesis they exclude is the natural first one to state, and because every lane's estimate has to be put in the two-sided form.

File: [`lean/Z4YM/Scaling.lean`](lean/Z4YM/Scaling.lean), checked; see "Execution" below.

## 2. Exact controls in two dimensions

On a cylinder (a circle of N links of length a = L/N, time steps of a) the Wilson transfer operator is diagonal in characters with eigenvalues c_r(β)^N, where c_r are the character coefficients of the plaquette weight. Along β = 1/(g a)² for U(1) and β = 4/(g a)² for SU(2), with g = L = 1:

| Group | Physical gap M(N) at N = 64 | Continuum value g²L·C₂/2 | Approach |
|---|---|---|---|
| U(1), charge 1 | 0.500061048820… | 1/2 | N²(M − 1/2) → 1/4; the remainder shrinks by 4.29, 4.07, 4.02, 4.00 per doubling |
| SU(2), spin 1/2 | 0.375011444266… | 3/8 | M − 3/8 shrinks by 4.01, 4.00, 4.00, 4.00 per doubling |

Here the lattice-unit gap m = M·a tends to zero at exactly the rate a, as section 1 requires, and the physical gap has a positive finite limit. Two-dimensional Yang–Mills has no local degrees of freedom and its gap is proportional to the length of the circle; it is a control on units and trajectory and says nothing about four dimensions.

## 3. Adverse control: a finite gauge group on the same trajectory

Z_n with weight exp(β cos(2πj/n)) on the U(1) trajectory β = N²:

| Group | M(2) | M(4) | M(8) | M(16) |
|---|---|---|---|---|
| Z₂ | 2.68e−3 | 4.05e−13 | 3.29e−54 | 2.24e−220 |
| Z₃ | 2.97e−2 | 1.81e−9 | 3.90e−40 | 1.31e−164 |
| Z₅ | 3.32e−1 | 3.49e−4 | 5.51e−18 | 5.32e−75 |

M(N) agrees with N² k δ e^(−N²δ), δ = 1 − cos(2π/n), k = 1 for n = 2 and 2 otherwise, to within 10⁻⁶ at N = 16. The physical gap tends to zero. Each of these operators is positive and has a gap at every finite N.

For Z₂ the collapse is proved, not only computed ([`lean/Z4YM/FiniteGroupControl.lean`](lean/Z4YM/FiniteGroupControl.lean)): the one-plaquette eigenvalue ratio is tanh β, and for every real x > 0

- `z2_gap_pos`: −log tanh x > 0,
- `z2_physical_gap_le`: x·(−log tanh x) ≤ 1/(1 + x),
- `z2_physical_gap_tendsto_zero`: with x = (N+1)², N = 0, 1, 2, …, the physical gap tends to zero.

The identification of the eigenvalue ratio with tanh β is not formalized. Z₃ and Z₅ remain numerical.

What this shows: on the trajectory that gives the continuum gap for the Lie group, a finite subgroup gives none. An argument for a continuum gap that uses only positivity of the transfer operator, a gap at each cutoff and the spacing-coupling relation, and that would apply word for word to a finite gauge group, proves too much. The parent program's carriers with gains in a finite group are in this class.

## Predicates and verdicts

Fixed in the docstring of [`computation/two_dim_control.py`](computation/two_dim_control.py) before the first run.

| Predicate | Verdict |
|---|---|
| H: closed-form character coefficients equal Haar quadrature to relative 10⁻²⁵ (20 cases) | met; 5 of 5 values of N qualify for each group |
| P1: U(1) gap above 1/2 and remainder shrinking by a factor in [3, 5] per doubling | met |
| P2: SU(2) gap above 3/8 and shrinking by a factor in [3, 5] per doubling | met |
| P3: Z_n gap strictly decreasing and within 10⁻⁶ of the stated asymptote at N = 16 | met |

Met 4, failed 0, measured only 0. First run: register check K2, exit 0. Rerun in a fresh directory: result file byte-identical, SHA-256 `24939c8dd0ae5925e27abe30b45936a6a0d38ae9456e326f9a3ba476465a9d0f`. Command: `python -I two_dim_control.py <directory containing mpmath>`; Python 3.14.7, mpmath 1.4.1.

Not covered by a predicate: the identification of the transfer eigenvalues with c_r^N (stated from the character expansion, not computed from a lattice), and the continuum values 1/2 and 3/8 (quoted).

## Execution

What ran, on the principal's Windows 11 machine:

| Item | Status |
|---|---|
| PCP OS | Python implementation at pcp-os `59f26eb`, workspace created for this subproject; register of 12 events replays with every guard passing and all objects matching (`pcpos verify`: PASS). Copy in [`pcp/register.jsonl`](pcp/register.jsonl). |
| ACR method | Not pinned. The packet on this machine has fingerprint `6b6d3a680f3f`; this build requires `7ff72eed9162`. ACR is not in use; the register holds retrievals, inspections and checks only. |
| Native Rust host, kernel guests | Not available on this machine (no Rust toolchain, no QEMU). Not used. |
| PCP workers, recursive hierarchy | Not run. The `claude` command-line program on this machine is not signed in, so no headless worker could be started. No chat, browser or app sub-agent was used in its place. Everything in this folder is the director's own work and has had no challenger, micro-review or builder. |
| Lean | Lean 4.19.0 (`6caaee842e94`), Mathlib `c44e0c8ee63c` from its cache, built outside the repository. `lake env lean` exit 0 for `Scaling.lean` (register check K3) and `FiniteGroupControl.lean` (K4); all six reported theorems depend on `propext`, `Classical.choice`, `Quot.sound` only. The first draft of `FiniteGroupControl.lean` failed (a `ring` after `field_simp` with no goals left, line 27); the line was removed. No mutation test was run. |
| GitHub | Z4 can push to this repository and cannot post comments (no signed-in route on this machine). This file is the check-in until that is repaired. |

## What is open

1. In four dimensions the trajectory is not known in closed form. The expected one is asymptotic freedom, a(β) ~ exp(−β/(2 b₀ N_c))·(power of β); no proof exists that the lattice-unit gap vanishes at that rate, from either side. This is the obligation of section 1 in the case that matters, and it is untouched.
2. What distinguishes the Lie group from its finite subgroups in an argument for the gap. In two dimensions it is the spacing of the low levels of the weight (continuous against discrete). A four-dimensional statement is wanted.
3. A4's sufficient condition (variance bounded below, first energy moment bounded above, both in physical units) can be read off in these controls for the simplest centered vector, the character χ₁ of the spatial holonomy. It is an exact eigenvector of unit norm, so its spectral measure is a unit atom at M(N) and its first moment is M(N). For U(1) and SU(2) the moment is bounded (by M(4)) and the atom converges to 1/2 or 3/8: A4's hypotheses hold and the limit has a gap. For Z_n the hypotheses hold as well, the moment tends to zero, and the correlator at every positive time tends to 1: the observable survives and the gap does not. This is the case A4's note marks for scrutiny (moment zero, vacuum degeneracy). It follows from the table in section 3 and has no predicate of its own. The same reading for a Wilson loop of fixed physical size, which is not an eigenvector, is not yet done.

## Cross-read of A4's `observable-normalization/SeparatedTime.lean`

At blob `399a8481d5ac`, on this machine: `lake env lean` exit 0, both theorems on the three standard axioms (register check K5), same Lean and Mathlib revisions as A4's receipt. This reproduces the compilation only. Reading of the statements: `momentLowerBound` uses neither E ≥ 0 nor t ≥ 0; the note's upper bound C_n(t) ≤ V does use E ≥ 0 and t ≥ 0, and is not in the Lean file. The guest-boot provenance in A4's receipt was not examined.

All checks here were made by one model family. Agreement with the other directors' readings reduces exposure and is not independent review.

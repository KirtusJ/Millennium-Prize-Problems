# a2-chalR report: attack on A1_REDUCTION.md, part I

Worker a2-chalR (challenger) for Director Z4. Principal: Kirtus Justus. Control: `control.txt` = 0.272341 (−ln tanh 1).
Same model family as the director: my agreement with the director is not independent review. My programs are `families.py` and `freefield.py`. The child's results were rerun and recomputed independently.

## 1. Verdict table

| # | Item | Verdict | Evidence (one line) |
|---|---|---|---|
| 1 | R1: C_β(ξ) > 0 | STANDS | ν_β(ℝ) = ‖ψ‖² > 0 and e^{−E} > 0 on the support, so ∫e^{−E}dν_β > 0. |
| 2 | R1: "μ_β is a probability measure on [1,∞)", including when ν_β has an atom at m | STANDS | An atom at ε = m becomes an atom at E = 1, which lies in the closed set [1,∞). F1 (atom included): every predicate MET. |
| 3 | R1: "the integral is finite for t ≥ 1/2 by (C)" | DEFECT (wording) | At fixed β, ν_β is finite and e^{−tE} ≤ 1, so G_β(t) is finite for every t ≥ 0. (C) is needed for the **uniform** bound, not for finiteness. |
| 4 | Real (non-integer) n | STANDS, with a remark | T^n for real n > 0 is defined by functional calculus from T ≥ 0 alone. Strict positivity of T is needed only to write H = −log T. In the Wilson application C(ξ/2) is **not** a lattice correlation, because ξ/2 is not an integer. Log-convexity of C (it is a Laplace transform) reduces (C) to integer times, but the file does not say this. |
| 5 | R2 tail bound, direction | STANDS | e^{−E} ≤ e^{−K/2}e^{−E/2} for E > K. Checked numerically: F1 P1b MET. |
| 6 | R3: weak limit keeps support in [1,∞) and mass 1 | STANDS | Prokhorov plus tightness gives mass 1. By portmanteau, limsup μ_β(F) ≤ μ(F) for closed F = [1,∞). F1 P1e MET (G at ξ = 1e5 and 1e6 agree to 4e-7). |
| 7 | R3: uniform integrability for 1/2 < t < 1 | STANDS | e^{(1−t)E} = e^{E/2}e^{−(t−1/2)E} ≤ e^{E/2}e^{−(t−1/2)K} on E > K. The algebra is correct. |
| 8 | R4: Jensen, mean ≤ 2 log D, passage to the limit, G(t) ≥ D^{−2(t−1)} | STANDS | exp(∫E/2) ≤ ∫e^{E/2} ≤ D. Fatou applies to the lsc integrand. F1 P1c and P1d MET. |
| 9 | R5 under (C⁺) | STANDS | Same argument with exponent 1 − 2^{−j}. F3 shows it is needed: with (C) but not (C⁺), G_β(1/4) → ∞ (2.7e3 at ξ = 1e6). The limit for t > 1/2 is e^{−(t−1)}, whose continuation is finite at t = 1/4. |
| 10 | Equivalent form of (C) and "mean energy ≤ 2 log D" | STANDS | Exact. Unstated consequence: every admissible D satisfies D ≥ √e. |
| 11 | "(C) is a statement about locality and nothing else" | DEFECT | Counterexample: two decoupled lattice free fields with masses m₁ ≫ m₂ = m, m₁/m₂ → ∞, and the local vector ψ = φ₁(0). (A) and (B) hold, but C(ξ/2)/C(ξ) ≳ e^{m₁ξ/2} → ∞. (C) is a no-hierarchy / overlap condition on the dynamics, not locality alone. F2a has the same structure in atoms: ratio 1e109. |
| 12 | D = e for ψ in the spectral subspace [m, 2m] | STANDS | sup of e^{E/2} on [1,2] is e. |
| 13 | A3: "n^{−p} then e^{−mn} gives (C⁺) with D_j ≈ e·2^{jp}" | DEFECT (constant) | Model density ε^{p−1} on [m,1]: the exact limit is D_j = 2^{jp} Γ(p,2^{−j})/Γ(p,1). The growth 2^{jp} is right. The constant e is right only for p = 1 as j → ∞. It is **too small** for p < 1 (p = 0.5, j = 4: 18.40 against 10.87, ratio 1.69) and too large for p > 1 (ratio → 0.40 at p = 3). P6b FAILED. |
| 14 | Is the reduction circular or vacuous (section 0, A5)? | DEFECT (not admitted plainly) | The conclusions "gap ≥ 1" and "not zero" hold by construction: a := m, and normalisation by C_β(ξ). Theorem R is Prokhorov plus Laplace transforms. Its whole content is the hypotheses, and (A) as β → ∞ is the infinite-volume lattice mass gap at weak coupling, i.e. the hard core of the problem itself. The file calls R "the elementary part" but does not say that (A) at β → ∞ contains the original difficulty. |
| 15 | Could weaker hypotheses do? (A5) | STANDS (the theorem holds; its hypothesis is stronger than needed) | Every conclusion for t ≥ 1 except the explicit lower bound in R4 needs only **tightness** of μ_β (F2a: (C) fails, G(2) → e^{−1}). Any c ∈ (0,1) works in place of 1/2: C(cξ) ≤ D C(ξ) gives R2 with D e^{−(1−c)K}, mean E ≤ log D/(1−c), and convergence for t > c. Without tightness the limit degenerates: F2b gives G(1) = 1 and G(t > 1) → 0. |
| 16 | Section 4 item 5: finite box, compact transfer matrix with strictly positive kernel, gap positive | STANDS, with corrections | The theorem is Jentzsch / Perron–Frobenius for an integral operator with a continuous, strictly positive kernel on a compact space, plus Hilbert–Schmidt compactness. The kernel is strictly positive after the temporal links are integrated, which projects onto gauge-invariant functions. On the full L² the operator then annihilates non-invariant functions, so "0 < T" holds only on the gauge-invariant subspace. Uniqueness of the top eigenvector there is what is needed, and it holds. (From memory; not confirmed in a source.) |
| 17 | Section 4 item 5: "(A) is a statement about infinite volume: inf over boxes of the finite-volume gap" | DEFECT | These are not the same. Low-temperature Ising: the finite-volume gap → 0 (tunnelling, ~e^{−cL^{d−1}}) while each pure infinite-volume phase has a positive gap. In general only liminf_L gap_L ≤ gap_∞ holds (spectral inclusion under strong resolvent convergence). Defined as the inf over boxes, (A) is strictly stronger than needed and can be false where the infinite-volume gap exists. |
| 18 | Section 4 completeness | DEFECT (omissions) | Missing: (a) the limit spectral bottom seen by ψ can be > 1 (F4: μ → δ₃, G(2) = e^{−3}), so "the physical gap is 1" is not shown for the limit, only "≥ 1"; (b) the limit μ = δ₁ (a pure exponential at one spatial point) is allowed by R, although it is incompatible with a local relativistic field (Källén–Lehmann at fixed x has a momentum continuum); (c) the multiplicative renormalisation C_β(ξ) → 0 and the need for consistent normalisations across fields; (d) item 17; (e) the non-integer-time remark (item 4). |
| 19 | Table row: compact U(1), 4D, weak coupling | STANDS | Coulomb phase proved for the **Villain** action (Guth 1980; Fröhlich–Spencer 1982). Confirmed at abstract level only. Wilson action from memory. |
| 20 | Table row: finite gauge group, 4D | STANDS (memory) | Low-temperature cluster expansion: excitation energy ~ cβ grows. Not confirmed in a source. |
| 21 | Table row: compact U(1), 3D | DEFECT (imprecise) | Göpfert–Mack 1982 cover the **Villain** action (gap and confinement at all β; the Wilson action is not covered). A secondary source found by search says they prove the continuum limit is a free massive scalar, so "believed" understates it. I did not check this against the original. |
| 22 | Table row: SU(2) or U(1), 2D | DEFECT | In infinite spatial volume (which item 5 requires), a gauge-invariant bounded function of the links of an open set in one slice is constant, so ψ = 0. The transfer matrix has no excitation above Ω, so m = +∞ and (B) fails. "True, true, true" holds only on a finite spatial circle with ψ a function of the holonomy, which is non-local and is the trivial finite-volume case item 5 sets aside. There, (C) holds with D = e^{1/2} for a character of the holonomy. |
| 23 | Table row: free massive lattice field, m → 0 | STANDS (computed) | ψ = φ(0): R(m) = C(ξ/2)/C(ξ) for m = .4, .2, .1, .05, .025, .0125 is 5.469, 6.513, 5.739, 5.551, 5.515, 5.507, tending to 2K₁(1/2)/K₁(1) = 5.503975. ψ = φ²: R² ≤ 42.4. Child and me agree to ≤ 3.3e-9. |
| 24 | Table row: free massless field | STANDS | m = 0. |
| 25 | Table completeness | NOT CHECKED (suggestion) | Missing discriminators: 4D φ⁴/Ising (Aizenman–Duminil-Copin 2021: Gaussian scaling limit), the sharpest test of (E); the 2D O(N) σ-model, N ≥ 3 (asymptotically free, gap believed); the two-mass free field of item 11 as a (C)-discriminator. From memory. |

Counts: **STANDS 16 / DEFECT 8 / NOT CHECKED 1.** The defects are items 3, 11, 13, 14, 17, 18, 21 and 22. None breaks the proof of Theorem R (R1–R6 survive line by line). They hit the remarks on (C), the A3 constant, the framing in section 0, section 4 and the table.

## 2. Hypotheses each statement uses, and where they are stated

- **R1:** (A) (section 2: ξ < ∞, support ε ≥ m), ψ ≠ 0 and ψ ⟂ Ω (section 1), 0 < T ≤ 1 (section 1; only T ≥ 0 is needed for n > 0). (C) is cited, but is needed only for uniformity.
- **R2:** (C) (section 2), R1.
- **R3:** R2, Prokhorov (not stated), (B) only implicitly (β_k → ∞ makes sense without it; (B) is not used in the proof).
- **R4:** R3, (C), Jensen, Fatou/lsc (named in the proof).
- **R5:** (C⁺) (section 2), with ξ ≥ 2^j, which comes from (B).
- **R6:** (B) and the definition a := m (section 0).
- Section 4 item 5 relies on unstated facts: compactness and positivity of the Wilson transfer kernel, and Jentzsch's theorem (section 5 defers them to the literature).

Note: (B) is not used in the proofs of R1–R5. It is used only in R6 and to make (C⁺) eventually applicable.

## 3. Failed predicates (met, failed, measured only)

- `families.py`: 12 met, 3 failed, measured only: the F1–F5 tables and the A3 table.
  - **P3a FAILED: my own expectation.** The bound 3 was wrong. The correct limit of C(ξ/2)/C(ξ) is e + √e = 4.367, which is still bounded, so (C) holds as intended.
  - **P4a FAILED: my own expectation.** I wrote e^{−2}. With μ → δ₃ the correct value is G(2) = e^{−3} = 0.0498, and the data give 0.049789.
  - **P6b FAILED: defect of the target.** e·2^{jp} is not an upper bound for p < 1.
- `freefield.py`: 6 met (Q0–Q5), 0 failed.
- Tolerances: REL = 1e-9 is float64 round-off headroom for positive sums. LIM = 1e-3 for convergence and Q3 = 1e-2 are my own choices. Q1 = 1e-6 grid tolerance (observed 4e-9). Q4 = 1e-5 agreement with the child (observed 3.3e-9). P6a = 1e-3 quadrature tolerance. None of these tolerances comes from the target.
- "For all" predicates, tested per case: P1b covered 6 ξ × 41 K, all qualify. P1c covered 6 × 5, all qualify. P6a covered 16 (p, j) cases, 16/16 qualify. P6b covered 16 cases, 13/16 qualify; the failures are p = 0.5 with j = 2, 3, 4. Q1, Q2, Q4, Q5: 6/6.

## 4. What I did not check

- No Lean (/home/user/z4-lean/READY exists, but I wrote no Lean file). No Lean result is claimed.
- Rows 2 and 20 (finite gauge group) and the Wilson-action versions of rows 1 and 3 are from memory. The Göpfert–Mack free-field limit is from a secondary search summary, not the original.
- Strict positivity / injectivity of the Wilson transfer matrix (Lüscher 1977; Osterwalder–Seiler 1978): from memory.
- Section 5 (Wilson-theory sources, the slice-flowed observable, S6‴): out of scope, and the file defers it.
- I did not prove the Ising finite-volume counterexample (item 17) for a gauge theory. It is a standard spin-system fact, given from memory.

## 5. Delegated questions and outcomes

- **Child (sonnet, `child/`, register `child/pcp`).** Question: A7's free-field computation alone, R(m) = C(ξ/2)/C(ξ) for ψ = φ(0) and φ², lattice ℤ⁴. Control: ∫₁^∞ e^{−E}dE. The child answered 0.367879, which is **correct**; I graded it before reading anything else. It returned R(m) for m = 0.4…0.0125 and Rc = 5.503975. It recorded one failed predicate of its own (monotone approach to Rc), which it correctly classed as its own expectation.
  - I reread and reran its script (copy `rerun/child_ratio.py`, check K3): numbers reproduced.
  - My independent method (`freefield.py`, graded Gauss–Legendre with octant symmetry) agrees to ≤ 3.3e-9 relative.
  - Outcome: row 5, (C), STANDS.
- **Grandchild (the child's sub-agent, `child/grandchild/`).** Question: recompute R at m = 0.1 by the Schwinger/Bessel representation C(t) = ∫e^{−τ(m²+8)} I₀(2τ)³ I_t(2τ) dτ. Control: ∫₀¹x²dx; it answered 0.333333, which is correct.
  - At the time I read it, its `run1.txt` showed P1 FAILED (its Bessel implementation was off by up to 1.5e-2 against the power series) and P2 FAILED (2.8e-8 difference from direct quadrature, against its own 1e-9 tolerance).
  - Its predicate P5 "0 < R < 1" is a wrong expectation: R > 1 always, because C is decreasing.
  - Final state: after two fixes (predicates unchanged) its run3 gives R(0.1) = 5.73855206702649, with P1 at 3.8e-14 and P2 at 1.3e-15. That agrees with my independent 5.738552067 to about 1e-11 and with the child's 5.738552049 to 3e-9 (the child's grid error). The child read this number back but could not rerun it to completion (timeouts), and said so plainly. My own rerun of `bessel_R.py` (check K4) **timed out at 280 s** under shared load, so the grandchild's R is **not rerun by me**. My independent `freefield.py` value is the one I rely on.
- **Child run record:** check `child-run1` (K5) **TIMED OUT at 900 s**, exit None, against an expected exit of 0. The child had nevertheless written `child/report.md` (verdict STANDS, numerical) before it was cut. Its register `child/pcp` verifies PASS.

## 6. Commands to rerun

```
cd /home/user/z4-workers/a2-chalR
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control, expect 0.272341
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P check --ws pcp --name families --expect-exit 0 -- python3 families.py           # writes results_families.txt (mode x: delete/rename first)
$P check --ws pcp --name freefield --expect-exit 0 -- python3 freefield.py         # writes results_freefield.txt (mode x)
mkdir -p rerun && cp child/ratio.py rerun/child_ratio.py
$P check --ws pcp --name rerun-child-ratio --cwd rerun --timeout 200 --expect-exit 0 -- python3 child_ratio.py 0.1 0.0125
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Web sources (A7; addresses only, no text copied):
- Guth, Phys. Rev. D 21 (1980) 2291: https://link.aps.org/doi/10.1103/PhysRevD.21.2291 (abstract)
- Fröhlich–Spencer, CMP 83 (1982) 411: https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/FROHLICH/1981-2002/P_81_40/P_81_40.pdf (title/abstract)
- Göpfert–Mack, CMP 82 (1982) 545: https://projecteuclid.org/download/pdf_1/euclid.cmp/1103920658 (bibliographic only)
- Secondary statement on the Villain-only scope: https://arxiv.org/abs/2602.00436 (abstract level)

## 7. Register verification

Checks in my register: K1 families exit 0; K2 freefield exit 0; K3 rerun-child-ratio exit 0; K4 rerun-grandchild-bessel TIMED OUT (280 s); K5 child-run1 TIMED OUT (900 s).

- `$P verify --ws pcp` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl` last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- `child`: `$P verify --ws pcp` last line: `result: PASS (...)`

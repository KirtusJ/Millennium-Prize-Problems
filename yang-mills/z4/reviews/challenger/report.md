# Challenger report: Z4, "The regulator trajectory and its physical units"

Control: `control.txt` = 0.272341 (−ln tanh 1).
Register `pcp/`: checks K1–K6. Last line of `pcp_os.py verify --ws pcp`:
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

## 1. Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| T1a: the three Scaling.lean theorems as mathematics | STANDS | My recompile K3: exit 0, axioms propext/Classical.choice/Quot.sound only. They are trivially true limit facts. |
| T1b: README prose vs Lean | STANDS (nit) | Hypotheses and limit directions match. "Two hypotheses together contradictory" leaves out c > 0 and a → 0⁺, which the Lean theorem needs. 𝓝[>]0 means *eventually* a_n > 0, not a_n > 0 for all n. The docstring's meaning of m (−log norm of the transfer operator) does not appear in the Lean statement, where m is an arbitrary real sequence. |
| T2a: "a gap at fixed coupling or uniform in lattice units is the wrong kind of bound" | STANDS, sense restricted | Follows from `physical_gap_tendsto_atTop` only if a → 0 while the bound holds. At a truly fixed coupling, a is fixed and nothing tends to zero. |
| T2b: "must … two-sided bounds c·a_n ≤ m_n ≤ C·a_n along the trajectory" | DEFECT | (i) The theorems do not imply it. It is the definition of m_n/a_n → M ∈ (0,∞), and holds only *eventually*, not along the whole trajectory. (ii) Counterexample to necessity (Q6, measured): the product U(1)×Z₂ on β = N². The full lattice gap is m/a = 1.5e−3554 at N = 64, so no c > 0 exists. Yet the spectrum above the asymptotically two-fold vacuum converges to the U(1) value 1/2. The lower bound is needed only on the sector the observable algebra sees, not on the full −log‖T|vac⊥‖. Vacuum degeneracy, superselection sectors and finite-volume tunnelling splittings all break the literal "must". |
| T2c: "strong-coupling expansions give m bounded below at small β and so cannot serve at fixed β" | DEFECT (wording/logic) | The sentence is garbled. At fixed β there is no limit a → 0, so Theorem 2 does not apply. The real obstruction is that the continuum trajectory has β → ∞, outside the radius of convergence. A lower bound at small β is harmless by the theorems unless the trajectory stays at small β. |
| T3a: diagonal in characters, eigenvalue ratio (w_r/w_0)^N | STANDS | Q2: on an actual N = 3 Z₅ lattice, the temporal-gauge transfer matrix was built by summing over time links. Eigenvector residual 5e−13, ratio deviation 7e−16, gauge-variant remainder 7e−14. Child (SU(2), N = 2, direct link integration): residual 1e−16. I reran it and the output was byte-identical. |
| T3b: U(1) gap, M(64) = 0.500061048820, N²(M−½) → ¼ | STANDS | Trapezoid Haar quadrature at 50 digits, no Bessel functions: M(64) = 0.50006104882019730 and 64²(M−½) = 0.25005597. My own expansion gives −ln(I₁/I₀) = 1/(2β) + 1/(4β²) + …, so the coefficient is ¼. |
| T3c: U(1) "remainder shrinks by 4.29, 4.07, 4.02, 4.00" | STANDS (ambiguous wording) | True for N²(M−½) − ¼: I get 4.2935, 4.0660, 4.0161, 4.0040. For M − ½ the factors are 4.19, 4.04, 4.01, 4.00. My predicate Q1d failed on that reading in K1. |
| T3d: SU(2) gap, M(64) = 0.375011444266, factors 4.01 to 4.00 | STANDS | Child: tanh-sinh vs Gauss-Legendre agree to 7e−48. M(64) = 0.375011444266388, factors 4.0110, 4.0029, 4.0007, 4.0002. My rerun (K5) was byte-identical. |
| T3e: trajectories and continuum values ½, ⅜ | STANDS | ½ = g²L·1/2 and ⅜ = g²L·(3/4)/2 match the computed limits. With β = 4/(ga)², the identification of g is a convention. |
| T4a: Z_n table and asymptote | STANDS | Q3: all 12 entries reproduced to relative ≤ 2.3e−3, which fits 3 printed digits. Asymptote relative deviation at N = 16 is ≤ 1.7e−49. Nit: "within 10⁻⁶" must be relative, because an absolute 10⁻⁶ is vacuous at 10⁻²²⁰. |
| T4b: "What this shows" (proves-too-much inference) | DEFECT | Q4: β = N² is the U(1) trajectory, not a trajectory for Z_n. On its own trajectory, which grows like ln N (Z₂: β = 2.08, 2.77, 3.47, 4.16, 4.85 for N = 4…64), Z_n has M(N) = ½ exactly. The charge-k levels converge to ½(1−cos 2πk/n)/(1−cos 2π/n); for Z₅, k = 2 gives 1.30915 at N = 64 against a limit of 1.30902. That is a positive finite gap and a finite spectrum, linear in L like 2D YM. An argument that uses only positivity, a gap at each cutoff and *a* spacing-coupling relation would therefore give a *true* conclusion for Z_n in 2D. It does not prove too much. The inference holds only if the argument fixes β ∝ 1/a² by hand, and that is not the class described. The strongest objection is that the trajectory is an output of renormalization, chosen per group. Comparing groups on one trajectory tests the trajectory, not the argument. |
| T5: FiniteGroupControl.lean vs bullets, including the N+1 shift | STANDS | K4: exit 0, standard axioms. The bullets match: x > 0 real, and x = (N+1)² with N ≥ 0. Q5: maximum of x(−ln tanh x)·(1+x) is 0.599 on 400 grid points. Nit: the docstring of `z2_physical_gap_tendsto_zero` says "positive at every N ≥ 1", but the statement does not assert positivity (that is `z2_gap_pos`). The file header says x = N², not (N+1)². |
| T6: A4 condition reading (unit atom, first moment, correlator → 1) | STANDS, with caveat | χ₁ is an exact unit-norm eigenvector (T3a), so the atom sits at M(N). M(N) is strictly decreasing on N = 4…64 for U(1) (Q1e), and the child's SU(2) values decrease too, so "bounded by M(4)" holds. For Z_n, e^{−tM(N)} → 1. Caveat: this shows A4's condition is *not* sufficient for a gap. The README does not say so explicitly ("sufficient condition" of what?). Also, by T4b the Z_n collapse is an artifact of the trajectory. |

Counts: STANDS 10 (4 of them with nits or caveats), DEFECT 3 (T2b, T2c, T4b), NOT CHECKED 0.

## 2. Hypotheses each statement uses

- `lattice_gap_tendsto_zero`: a_n → 0, a_n ≠ 0 for all n, m_n/a_n → M real (Scaling.lean, l.22–24; README §1 bullet 1). No sign condition on m or M.
- `physical_gap_tendsto_atTop`: c > 0, a_n → 0 within (0,∞) (eventual positivity), c ≤ m_n for all n (l.32–33; README bullet 2).
- `not_uniform_…`: the union of the two above (l.46–48). The README's "two hypotheses" omits c > 0 and a → 0⁺.
- `z2_gap_pos`, `z2_physical_gap_le`: x real, x > 0 (FiniteGroupControl.lean; README §3 bullets).
- `z2_physical_gap_tendsto_zero`: no hypotheses; x = (N+1)², N ∈ ℕ.
- README §2 uses, unstated in Lean: the transfer operator restricted to class functions of the holonomy (gauge-invariant sector), a = L/N, time step equal to a, L = g = 1. §3 uses the U(1) trajectory for Z_n. §1's "must" uses that the gap of the limit theory equals lim m_n/a_n for the full transfer operator, which is stated nowhere.

## 3. Failed predicates

- K1 Q1d (U(1) remainder factors): failed. **My expectation.** I read "remainder" as M − ½. The README means N²(M−½) − ¼. Fixed in v2 (K2).
- K1 Q3 (Z_n table): failed. **My defect.** mp.log(1−x) underflowed for x ≈ 1e−220. Fixed with log1p in v2 (K2).
- Child K(transfer.py) B5 (rule-size agreement 1e−12, observed 2.75e−12): failed. **Child's defect** (summation round-off). Fixed with compensated summation in transfer_v2.
- No predicate failed on a defect of the target. The DEFECT verdicts come from the measured Q4/Q6 constructions and from reading the prose.

Predicate counts. My program: K1 met 7, failed 2, measured only 1; K2 met 9, failed 0, measured only 1. Child: gap met 4, failed 0; transfer met 0 of 1 on B5 → transfer_v2 all met.

## 4. What I did not check

- Any four-dimensional statement ("What is open" 1–2), and the A4 Lean cross-read.
- The register replay claims and SHA-256 in the README (I did not run `computation/two_dim_control.py`, which is not in input/).
- Whether my U(1)×Z₂ example counts as a "positive finite gap" under the program's definition. That depends on whether a degenerate vacuum is allowed. If the program requires a unique vacuum, T2b's (ii) weakens to the "eventually" point (i) and the sector point.
- A full SU(2) lattice with N > 2 (the child did N = 2). The full spectrum on the gauge-invariant space for SU(2) beyond j = 1/2 and j = 1.
- No Lean formalization of my counterexamples.

## 5. Delegated question and outcome

Question (to child/, its own register child/pcp): an independent recomputation for SU(2) of T3, with control ∫χ_{1/2}² dU = 1. (a) M(N) = −N² ln(w_{1/2}/w_0) at β = 4N², N = 4…64, by Haar quadrature without Bessel functions. (b) On an actual N = 2 lattice, check that χ_{1/2} is an eigenfunction with ratio (w_{1/2}/w_0)^N.
Returned: control 1.0 (to 1e−40). M = 0.377940566958, 0.375733128642, 0.375183150041, 0.375045779159, 0.375011444266. Factors 4.011, 4.003, 4.001, 4.000. N = 2 at β = 2: R_{1/2} = 0.1875993677790915 = (w_{1/2}/w_0)², residual ≤ 1.5e−16. Child verify: PASS. The child did not write a report.md (its tool refused). It did record one failed predicate, B5 (see §3).
My handling: I read gap.py (tanh-sinh vs Gauss-Legendre, peak-split intervals) and reran gap.py and transfer_v2.py through my register (K5, K6). Both outputs were byte-identical to the child's. I accept the result. The N = 2 check relies on the child's factorization of the V-integral, which I did not re-derive; my own Z₅ lattice check (Q2) independently supports the structure.

## 6. Commands to rerun (from C:/Users/donke/z4-workers/challenger, bash, PYTHONUTF8=1)

```
python -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py init pcp --principal principal --principal-name "Kirtus Justus"   # only in a fresh dir
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name challenge_v2 --expect-exit 0 -- python challenge_v2.py result_challenge_3.txt
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name lean_Scaling --expect-exit 0 -- sh lean_check.sh C:/Users/donke/z4-workers/challenger/lean/Scaling.lean
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name lean_FGC --expect-exit 0 -- sh lean_check.sh C:/Users/donke/z4-workers/challenger/lean/FiniteGroupControl.lean
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name child_gap --expect-exit 0 -- sh -c "cd child && python gap.py"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name child_transfer_v2 --expect-exit 0 -- sh -c "cd child && python transfer_v2.py"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```
(`challenge.py` writes to a new file name each run; it refuses to overwrite. The child scripts number their outputs.)

The challenger and the director share a model family; this is not independent review.

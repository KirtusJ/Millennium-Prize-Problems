# g2-three report: exact numerics for the three-direction model (task T79)

Worker g2-three, task T79. Child T83 (sonnet). Grandchild T84.
- Control: `control.txt` = 0.272341 (−ln tanh 1).
- Lean: READY exists, but I did not use it. I make no Lean claim.

## 1. Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| Basis: Peter–Weyl / S³ harmonics, the three conjugation spins 3j-coupled to 0 (all triangles; pseudoscalars included, because conjugation is SO(3), not O(3)) | STANDS | With link 3 decoupled, the code reproduces the 2-direction spectrum: 1.6376208 vs 1.63761996, and 1.8823418 vs 1.88234137 (β=2, N=8). |
| Pair recoupling: each V_ij acts on the pair (i,j) coupled to the spectator's l_k. Edmonds 7.1.6. The 3j reordering phases cancel because k is even | STANDS | Continuum: J=2 levels come out as exact 5-fold clusters (E in (000) + T2 in the 3 images of (110)), spread < 1e−8 (C4, 3/3 clusters odd). 2-dir reduction: gap 1.9749642 vs 1.974964 (C2). |
| Control V=0 (K eigenvalues ∏ I_{n_i+1}/I_1) | STANDS | Max error 0 (L1). m_e = 2.0118191813 = −ln(I₃(2)/I₁(2)). The child gets the same value to 10 digits by 1-D quadrature. |
| Control: 2-direction model recovered with the third link decoupled | STANDS | L2 diff 8.2e−7 (β=2) and 9.8e−5 (β=4) at N=8. The free-link level −ln(I₃/I₁) = 2.0118192 is also present. |
| Control β→0 | STANDS (measured) | β=0.01: m_e = 12.382591 vs −ln(I₃/I₁) = 12.388400. The difference −5.8e−3 is O(β), as in the 2-dir code (−3.3e−3 there with one pair; here there are 3 pairs). |
| Control U(1)³ "in the same code path" | NOT CHECKED | On 1×1×1 the U(1) plaquette U_iU_jU_i⁻¹U_j⁻¹ ≡ 1, so V ≡ 0. The control reduces to the V=0 one. My code has no U(1) basis. |
| Independent matrix elements Z=∫e^{−V}, X=∫χ₁χ₁e^{−V} (6-D quadrature vs child Haar MC) | STANDS | Z(1) = 0.1767213 vs 0.176791±0.000089 (z=0.8). X(1) z=−0.4, Z(2) z=0.8, X(2) z=−0.2. |
| Lattice m_e at β ≤ 4 (converged) | STANDS (measured) | m_e = 2.876117 (β=1), 1.621505 (β=2), 0.96893 (β=4). Change at the last N step: 3e−5, 3e−5, 8e−4. |
| Lattice m_e at β=8 | NOT CHECKED (not converged) | N=6, 8, 10 give 1.032, 0.960, 0.945. Steps 7e−2 and 1.5e−2 (L4 failed). |
| Continuum h₃: E₀ and the lowest rotation-invariant gaps | STANDS (measured, Rayleigh–Ritz) | E₀ = 6.534885; first gap 3.012539 (J=2, 5-fold); 0⁺⁺ gap 3.602838 (N=28, ω=2). Changes N24→28: 1.5e−6, 1.5e−5, 6e−5. |
| m_e β^{1/3} → E₁(h₃) in three directions | NOT CHECKED (out of reach) | Reached: β ≤ 4 converged, β=8 rough. m_e β^{1/3} = 2.88, 2.04, 1.54, ≈1.89. Prediction 3.0125. Not asymptotic (§5). |

Counts over the 11 rows: STANDS 7, DEFECT 0, NOT CHECKED 4.

Predicate counts over all programs: **met 40, failed 3, measured only 9.**
- Met (40):
  - xquad: Q0, Q1, Q2 (3).
  - cont3: C1, C2 (2), plus C3 and C4 in 6 h₃ runs (12).
  - lat3: L1 (1), L2 ×2 (2), L3 in 14 full runs (14), L5 (1).
  - L4: 5 met.
- Failed: the three L4 failures (§3).
- Measured only:
  - C5 convergence of E₀ and the two gaps;
  - β→0;
  - the exponent and constant statements;
  - the β=8 values;
  - m_e β.

## 2. Derivations, method, results

**Model.**
- V = β Σ_{i<j}(1 − ½Tr comm(U_i,U_j)) = 2β Σ s_i²s_j²(1−u_ij²), with s=sin a and u_ij = n̂_i·n̂_j.
- Checked against explicit matrices to 7e−16 (xquad Q0).
- T = e^{−V/2}Ke^{−V/2}, with K per link (2/β)e^{−β}I_{n+1}(β), as in D1–D3 of NUMERICS_2DIR. I did not re-derive anything that changes in 3D: each spatial link still has one temporal plaquette per step, and the three spatial plaquettes are all in V.

**Basis.**
- Basis functions: F_{n₁l₁}F_{n₂l₂}F_{n₃l₃} · Σ_m (l₁l₂l₃; m₁m₂m₃) Y_{l₁m₁}Y_{l₂m₂}Y_{l₃m₃}, with 0 ≤ l_i ≤ n_i and (l₁,l₂,l₃) a triangle.
- Both parities of l₁+l₂+l₃ occur (n̂₁·(n̂₂×n̂₃) is invariant).
- Dimension with cutoff n_i ≤ N: Σ_{n_i≤N} #{l_i ≤ n_i, triangle}. For the center-even sector:

| N | dimension, sector (000) | dimension, sector (110) |
|---|---|---|
| 8 | ≈ 1900 | 813 |
| 10 | ≈ 4000 | — |

**Symmetries.**
- center parities (−1)^{n_i}: only the all-even sector was computed;
- U_i → U_i⁻¹: (−1)^{l_i}, giving 8 sectors, with images under S₃;
- the permutations S₃ give the exact 2-fold E levels seen in sector (000).

**Matrix elements.** e^{−V/2} = e^{−V₁₂/2}e^{−V₁₃/2}e^{−V₂₃/2} holds exactly, because the factors are commuting multiplication operators.
- Each P e^{−V_ij/2} P is computed by expanding in Legendre polynomials in u_ij. Only even k contribute, and only k ≤ 2N.
- The pair is coupled to l_k: ⟨(l_al_b)L|P_k|(l_a'l_b')L⟩ = (−1)^{l_a'+l_b+L}{l_a l_b L; l_b' l_a' k}⟨l_a‖C^k‖l_a'⟩⟨l_b‖C^k‖l_b'⟩.
- 6j and 3j come from exact rational Racah formulas (ang.py).
- The radial part uses a Gauss–Chebyshev-U a-grid and Gauss–Legendre(64) in u.
- So yes, the 2-direction structure is reused through recoupling. No 6-D quadrature is needed.
- What is diagonalised: M = K^{1/2}AAᵀK^{1/2}, A = E₁₂E₁₃E₂₃. This is not a compression at finite N, so it is not variational. Convergence comes only from N-variation.

**Reach.**
- N=10 takes ≈ 1 min per β.
- N=12 did not finish one sector in 2 min. The bottleneck is the Python loops over angular coefficients; the dense algebra is cheap.
- Convergence needs N growing with β: at β=8, N=10 is not enough.
- **Honest reach in this budget: β ≤ 4 converged (≤ 1e−3), β=8 indicative only.** Vectorised 6j tables and Lanczos would extend this to perhaps N≈16 and β≈16, which is still pre-asymptotic.

**Lattice results.**
- Lowest center-even levels E = −ln(λ/λ₀). Full table in results/analysis3.md.
- The lowest excitation is a 2-fold S₃ "E" level in sector (000), which is the lattice remnant of a J=2 multiplet.

| β | N | m_e | 2nd level | next | m_e β^{1/3} | m_e β |
|---|---|---|---|---|---|---|
| 1 | 8 | 2.876117 | 2.876117 | 3.112276 | 2.876 | 2.876 |
| 2 | 10 | 1.621505 | 1.621505 | 1.928516 | 2.043 | 3.243 |
| 4 | 10 | 0.968930 | 0.968945 | 1.184132 | 1.538 | 3.876 |
| 8 | 10 | 0.9447 (±~0.015) | 0.9455 | 1.0574 | ≈1.89 | ≈7.56 |

**Continuum h₃ = −½Δ_{ℝ⁹} + 2Σ|Y_i×Y_j|²** (cont3.py).
- Method: HO basis, total quanta ≤ NMAX, exact Gauss–Laguerre matrix elements, the same recoupling formula with k=2.

| NMAX (ω=2) | dimension | E₀ | J=2 gap (5-fold) | 0⁺⁺ gap |
|---|---|---|---|---|
| 12 | 1134 | 6.5351031 | 3.020472 | 3.620213 |
| 16 | 3927 | 6.5349054 | 3.013550 | 3.605728 |
| 20 | 11011 | 6.5348872 | 3.012667 | 3.603284 |
| 24 | 26572 | 6.5348854 | 3.012554 | 3.602897 |
| 28 | 57324 | 6.5348853 | 3.012539 | 3.602838 |
| 24 (ω=1.5) | 26572 | 6.5348877 | 3.012640 | 3.603209 |

- Convergence: increments are geometric (ratio ≈ 0.13–0.15). Geometric extrapolation gives E₀ ≈ 6.534885, E₁ (J=2) ≈ 3.01254 and 0⁺⁺ ≈ 3.60283 (measured only).
- The lowest rotation-invariant excitation is J=2, not 0⁺⁺.
- Conversion to the convention H = −½Δ + (g²/2)Σ_{i<j}|A_i×A_j|²: ours is g²=4, so divide energies by 4^{1/3}. That gives E₀ = 4.11672, J=2 gap 1.89778, 0⁺⁺ gap 2.26964.
- FROM MEMORY, not relied on: the literature value E₀ ≈ 4.1167 for g=1 (Lüscher–Münster / van Baal era). It agrees. I do not trust my memory of the gap values, so I give none.

## 3. Hypotheses used and where stated
| # | hypothesis | where | checked by |
|---|---|---|---|
| H1 | Wilson action and the transfer splitting, as in the 2-dir D1 | brief; NUMERICS_2DIR D1 | not re-derived (structure per link unchanged) |
| H2 | ½Tr comm formula in invariants | xquad.py, lat3.py docstrings | xquad Q0 (explicit matrices) |
| H3 | K diagonal, eigenvalue ∝ I_{n+1}(β) | lat3.py docstring | L1; child Q1 |
| H4 | 3j-coupled basis is orthonormal and complete in the invariant L² | lat3.py, cont3.py docstrings | L2, C2, C4 (degeneracies) |
| H5 | Edmonds 7.1.6 and the reordering phases | ang.py, cont3.py docstrings | C4 (5-fold J=2), C2, ang spot values |
| H6 | product approximation A=E₁₂E₁₃E₂₃ converges to e^{−V/2} | lat3.py docstring | L4 (fails for β ≥ 4 at small N) |
| H7 | continuum limit A=β^{−1/3}Y, κ=2 per pair; center-even ↔ local levels | NUMERICS_2DIR D4, extended to 3 pairs | NOT proved; not reached numerically |
| H8 | quadrature adequate | lat3.py | L5 (MA 48→64: 8e−16) |

## 4. Failed predicates (kept)
1. **L4, β=4, N 6→8:** Δm_e = 8.2e−3. This was my own expectation that N=6 is enough. N 8→10 is met (7.9e−4).
2. **L4, β=8, N 6→8:** Δm_e = 7.2e−2. Own expectation; truncation.
3. **L4, β=8, N 8→10:** Δm_e = 1.5e−2. Own expectation; truncation. As a result β=8 is not converged.

Other own errors:
- In notes step 2 I wrote the expected −ln(I₃(2)/I₁(2)) as 2.011835. That was my arithmetic slip; the correct value is 2.0118192. The child's value was right.
- C1 is weak: with the potential replaced by ½ω²r², H is diagonal by construction. It tests only the bookkeeping.
- C4 tests only the 3 clusters below E₀+4.

None of the failures is a defect of the target.

## 5. Statement (measured only)
- In three directions, m_e β^{1/3} = 2.88, 2.04, 1.54, ≈1.89 at β = 1, 2, 4, 8.
- The continuum prediction is E₁(h₃) = 3.0125 (J=2). The ratio at β=8 is ≈ 0.63.
- This is the same pre-asymptotic pattern as in two directions: there m_e had a minimum near β=8 (ratio 0.52), and the asymptotic regime began beyond β=16.
- m_e β grows (2.9 → 7.6), so 1/β scaling is not what happens in the computed range either.
- **The data neither confirm nor refute exponent 1/3 or the constant in three directions.** The reachable β ≤ 8 are well before the regime. In 2D the local exponent was still 0.07 at β=16.

The prediction that can be stated:
- If the 2D pattern carries over, m_e β^{1/3} → 3.0125 = gap of h₃.
- The lowest lattice level is the J=2 multiplet split into E (2-fold, (000)) and T2.
- The 0⁺⁺ level is at 3.6028 in units of β^{−1/3}.

## 6. Not checked
- Lattice β ≥ 8 converged, and any β ≥ 16. The center-odd sectors. The T2 partner on the lattice (not tabulated).
- The U(1)³ control: it is trivial here (V ≡ 0), and there is no U(1) code path.
- The derivation of κ=2 per pair in 3D: assumed from 2D D4, not re-derived.
- No proof. No two-sided bound on the h₃ levels (Rayleigh–Ritz upper bounds only).
- No Lean.
- analysis3.md was produced before the N=28 run finished. The N=28 numbers are from results/cont3_N28_w2.json.

## 7. Delegation
**Child T83** (sonnet; admitted under T79; run recorded as check `child-run1`; released).
- Control I₂(2)/I₁(2) = 0.433127. I computed it first and graded it before reading anything else: correct.
- Q1 (V=0 kernel): k_j/k_0 = I_{2j+1}/I_1 by 1-D quadrature. Result −ln(k_1/k_0)(β=2) = 2.0118191813, which agrees with mine.
- Q2 (Haar MC, 4e6 samples, seed 2024) agrees with my xquad quadrature:

| quantity | child (MC) | mine (xquad) | z |
|---|---|---|---|
| Z(1) | 0.176791 ± 0.000089 | 0.1767213 | +0.8 |
| X(1) | 0.014744 ± 0.000232 | 0.0148270 | −0.4 |
| Z(2) | 0.062870 ± 0.000061 | 0.0628227 | +0.8 |
| X(2) | 0.019672 ± 0.000160 | 0.0197051 | −0.2 |

- I read q2.py (explicit matrices, correct V and χ₁) and reran q1.py and q2.py in a scratch copy: identical output.

**Grandchild T84** (admitted by the child under T83, released).
- Z(1) = 0.176840 ± 0.000126 by an Euler-angle MC. Consistent with Z(1) above.
- β→0 boundary: Z ≈ 1 − 2.25β, X → 0.
- It failed its own control (it expected I₁(1) instead of the ratio) and two of its own expectations. The child reports this, and these are not defects of the target.
- The child reports rerunning it byte-identically. I did not rerun the grandchild myself.

## 8. Registers
- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- Checks: K1 xquad, K2 child-run1, K3 cont3_runs, K4 lat3_runs, K5 analyse3, K6 cont3_N28.

## 9. Rerun
Run from /home/user/z4-workers/g2-three. Result files are opened with mode "x", so move results/ away first.
```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
OMP_NUM_THREADS=1 $P check --ws pcp --name xquad --expect-exit 0 -- python3 xquad.py results/xquad.json
$P check --ws pcp --name cont3_runs --expect-exit 0 --timeout 1800 -- ./run_cont3.sh
OMP_NUM_THREADS=1 $P check --ws pcp --name cont3_N28 --expect-exit 0 --timeout 1500 -- python3 cont3.py h3 28 2.0 results/cont3_N28_w2.json
$P check --ws pcp --name lat3_runs --expect-exit 0 --timeout 1800 -- ./run_lat3.sh     # expected exit 0 (L4 is evaluated in analyse3)
$P check --ws pcp --name analyse3 --expect-exit 0 -- python3 analyse3.py results/analysis3.md
# single runs: python3 lat3.py {full|v0|dec} BETA N MA OUT ;  python3 cont3.py {h3|ctrl} NMAX W OUT
# child: $P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp ; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
- Programs: ang.py, xquad.py, cont3.py, lat3.py, analyse3.py.
- Scripts: run_cont3.sh, run_lat3.sh.
- Other files: results/*.json, results/analysis3.md, notes.md, child/.

# g1-num report: exact transfer-matrix spectrum, SU(2) on the 1×1×ℤ lattice (two spatial directions)

Worker g1-num, task T72. Child T73 (sonnet), grandchild T75. Control: `control.txt` = 0.272341 (−ln tanh 1).
Lean was READY but I did not use it. I make no Lean claim.

## 1. Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| Brief's T = e^{−V/2}Ke^{−V/2}, factor β in V, one temporal plaquette per spatial link per step | STANDS | Derived from the Wilson action (§D1). Every factor agrees. |
| Brief's commutator potential, written in invariants as V = 2β sin²a₁ sin²a₂ sin²γ | STANDS | Agrees with explicit 2×2 matrices to 5.6e−16 on the whole grid (C3). |
| Brief's K eigenvalue ∏ c_{j_i}/c_0 with c_j ∝ I_{2j+1}(β) | STANDS | Per link the eigenvalue is e^{−β}(2/β)I_{n+1}(β), n=2j. The V=0 run of the same code reproduces it to 6e−15 (C5). |
| Control (i): U(1)² in the same code path, eigenvalues ∏I_{n_i}/I_0 | STANDS | Agrees to 4.8e−15 at β=4 and 16 (C4 dense, C4b Lanczos). The child agrees to 12 digits on −ln(I_n/I_0). |
| Control (ii): β→0 gap → strong-coupling character value | STANDS | m_e+ln(I₃/I₁) = −3.3e−3 (β=0.01) and −3.3e−4 (β=0.001); odd sector −2.5e−3 and −2.5e−4. The deviation is linear in β (C6). |
| Control (iii): absolute normalisation of T against direct Haar Monte Carlo (β=2) | STANDS | Tr T: z=+1.8. Tr T²: z=−0.5 (4·10⁶ samples). −ln λ₀=4.08579 lies inside the MC bracket [3.760, 4.754] (X3, X4). |
| Control (iv): convergence to ≥4 digits for every reported number | STANDS | Every level E>1e−6 changes by ≤3e−11 under N→N+16 and by ≤1e−13 under grid +40 (β ≤ 512). For β=1024 see §2. |
| Child's matrix elements A = ∫χ₁χ₁·½Tr comm, B = ∫e^{−4(1−½Tr comm)} | STANDS | Child (explicit matrices): A=−1/12, B=0.198249519694. My lattice quadrature gives −0.0833333333333 and 0.198249519694 (X1, X2). |
| R1 "m_e ~ β^{−1/3}" (two-direction analogue, measured) | STANDS (measured, β ≤ 1024) | Local exponent 0.228, 0.271, 0.295, 0.309, 0.318 for β=32→1024. m_e·β^{1/3} → 1.974, against continuum E₁ = 1.974964. |
| R1 sharp form: β^{1/3}m_e → E₁(h), κ fixed by normalisation | STANDS (measured, 2 directions) | κ = 2 when U = exp(iY·σ). Geometric extrapolation of m_e·β^{1/3} gives 1.974, a difference of about 0.05% from E₁. |
| RUNG "U(1) Z₂-even gap ≈ 2/β" | STANDS | Exact −ln(I₂/I₀) ≈ 2/β, reproduced in C4. |
| RUNG step 6: center-odd splittings exp(−c√β) | STANDS (measured β ≤ 64) | −ln m_eo/√β = 1.49, 2.01, 2.49, 2.89 (β=8…64), still rising. From β=128 on the splitting is below double precision (≤1e−13). |
| RUNG MC "fitted exponent 0.231" | NOT CHECKED (different model) | Measured only: in the 2-direction model the local exponent between β=32 and 64 is 0.228. A fit at moderate β falling short of 1/3 is what pre-asymptotic corrections produce here. |
| R1 itself (three spatial directions, 3+1 D) | NOT CHECKED | Not started. The cost estimate is in §6. |

Counts over the 14 rows: STANDS 12, DEFECT 0, NOT CHECKED 2.
Predicate counts over all my programs: **met 119, failed 3, measured only 21**. The 21 measured-only items are levels below the 1e−6 precision floor. The exponent and extrapolation statements (§2c) are also measured only. All 3 failures are my own expectation or my own defect (§3).

## 3. Hypotheses used and where they are stated

| # | hypothesis | where | checked by |
|---|---|---|---|
| H1 | Wilson action β(1−½ReTr U_p); transfer splitting e^{−V/2}Ke^{−V/2} | brief; D1 | derivation |
| H2 | ½Tr comm = 1 − 2s₁²s₂²sin²γ; Haar measure in invariants | D2, notes.md step 2 | C3 (matrices); child A, B |
| H3 | K diagonal with eigenvalue e^{−β}(2/β)I_{n+1}(β) per link | D3 | C5, X3 (MC of Tr T) |
| H4 | {Φ_{n₁n₂L}} is an orthonormal basis of the invariant L² (S³ harmonics) | D3 | C2, C5 (dimension count 285), X3 |
| H5 | quadrature of e^{−V} adequate | lat.py docstring | grid variation (dE(grid) ≤ 1e−13) |
| H6 | truncation is a compression (λ monotone in N) | D3 | A2 |
| H7 | Bessel ratios by Miller recurrence | lat.py | C1b (power series), C1c (trapezoid) |
| H8 | continuum limit A = β^{−1/3}Y, κ = 2; center-even ↔ all invariant local levels | D4, cont.py docstring | NOT proved. Supported only by the agreement in 2c. |
| H9 | Lanczos converged | lat.py | A3 (residual ≤ 1e−11 λ₀) |

## 4. Failed predicates (kept)

1. **controls1** (lat.py controls, exit 1): own defect. The trapezoid e^{−β}I_n has absolute error about 1e−17, so it went negative at β=0.01 for n ≥ 5 and sqrt gave NaN. Fixed by switching to Miller recurrence.
2. **controls2 C1** (trapezoid vs Miller, relative < 1e−12 for n ≤ 40): own expectation. The trapezoid error is absolute, not relative. The amended predicates C1b and C1c (controls_b.py) were met.
3. **controls2 C4@16, Lanczos sub-test:** own test design. V from the matrices is 5e−15, not 0, so it splits the exact U(1) degeneracies, and comparing against the list of distinct values misaligned. The dense part of C4 passed at 4.7e−15. The amended C4b was met.
4. Not counted as predicates:
   - My first cont.py dev run (scratchpad) gave spurious eigenvalues around −1e5: own defect, Golub–Welsch weights. Fixed with Christoffel weights before any recorded run.
   - Predicate A4's "Rayleigh–Ritz monotone" was evaluated between ω=1 and ω=1.5 bases. These are not nested, so that sub-check is not variational, although it passed. The nested check (K,L) at ω=1 is the valid one, and it is monotone.

None of the failures is a defect of the target.

## 5. Not checked

- R1 itself, with three spatial directions (3+1 D): not started. See §6.
- No proof of anything. Steps 2–4 and 7 of the RUNG chain are untouched. The agreement in §2c is numerical.
- Center-odd splittings for β ≥ 128 are below double precision. Extended precision would be needed.
- E₁(h) is a Rayleigh–Ritz upper bound with convergence evidence, not a two-sided bound.
- I did not rerun the RUNG Monte Carlo, and I did not check the quoted RUNG numbers.
- No Lean.

## 6. Three directions: what changes, and the cost (not started)

- **Invariants and basis:** SU(2)³ has 6 invariants. The basis is |n₁n₂n₃; L₁L₂L₃ → 0⟩ with triangle (L₁,L₂,L₃). V is a sum of three commutator terms, each acting on a pair. Its matrix elements need 6j recoupling, or a 6-D quadrature.
- **Size:** at β=64 the 2-direction run needed n ≤ 48. The 3-direction dimension is then about Σ_{n_i≤48} #triangles ~ 10⁸–10⁹ states, and a 6-D grid would have ~10¹²–10¹³ points. That is infeasible here. Even β=4–8 (N≈16) gives ~10⁶ states and ~10⁹ grid points: hours on 2 cores, and memory-bound.
- **Feasible route:** the continuum h on su(2)³, a sparse coupled-HO basis of ~10⁶–10⁷ states with Lanczos. Asymptotically E₁(h₃) is what R1 needs, but the lattice approach to it cannot be computed this way at large β.

## 7. Delegation

- **Child T73** (admitted under T72, run recorded as check K1 `child-run1` in my register, released). The child was a sonnet model.
  - Control I₁(1)/I₀(1). I computed 0.446390 first and graded it before reading anything else: correct.
  - Questions:
    - Q1: U(1) control, −ln(I_n/I_0) for n=1,2 and β=4,16, to 10 digits by two methods.
    - Q2: by direct Haar quadrature with explicit 2×2 matrices, A = ∫χ₁(U₁)χ₁(U₂)·½Tr comm and B = ∫e^{−4(1−½Tr comm)}.
  - Outcomes:
    - Q1 equals my ref_child.out to 12 digits.
    - A = −1/12 (|A+1/12| = 3e−16) and B = 0.198249519694. These match my values (ref_child.out: −1/12 and 0.1982495197) and my lattice quadrature (xcheck X1, X2 to 1e−12).
    - The child recorded its own failed predicate Q4, which was its own expectation.
  - I reran child/q1.py, q2.py and q2b.py in a scratch copy: the outputs were identical.
- **Grandchild T75** (admitted by the child under T73, released): independent Euler-angle recomputation of A and B, with known-answer control 0.446390.
  - Outcome: A = −0.083333333333, B = 0.198249519694.
  - I reran grandchild/run.py in a scratch copy: identical.
  - Caveat: the grandchild also uses conjugation invariance for U₁, so it is not fully independent of the child.

## 8. Registers

- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## 9. Rerun (from /home/user/z4-workers/g1-num; result files are opened with mode "x", so move results/ away first)

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 ref_child.py
$P check --ws pcp --name controls2 --expect-exit 0 -- python3 lat.py controls results/controls2.json      # expected exit 1 (C1, C4@16 own-design failures)
$P check --ws pcp --name controls_b --expect-exit 0 -- python3 controls_b.py
OMP_NUM_THREADS=1 $P check --ws pcp --name xcheck --expect-exit 0 -- python3 xcheck.py
$P check --ws pcp --name lat_sweep1 --expect-exit 0 --timeout 3000 -- ./run_lat.sh        # beta 2..512, 2 threads, ~13 min
$P check --ws pcp --name cont_runs --expect-exit 0 --timeout 1800 -- ./run_cont.sh        # 1 thread, ~5 min
$P check --ws pcp --name lat_sweep2 --expect-exit 0 --timeout 3000 -- ./run_lat2.sh       # beta 1024, 1 thread, ~23 min
$P check --ws pcp --name analyse --expect-exit 0 -- python3 analyse.py results/analysis.md
# single spectrum run, e.g.:  python3 lat.py spec 512 104 220 220 results/spec_b512_N104_X220.json
# child (run in child/):
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp ; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Files:
- programs: lat.py, cont.py, controls_b.py, xcheck.py, analyse.py, ref_child.py;
- run scripts: run_lat.sh, run_lat2.sh, run_cont.sh;
- results: results/*.json and results/analysis.md;
- notes.md, child/.

---
# Appendix A. Results

## Results (all numbers are from `results/analysis.md`, produced by analyse.py)

### 2a. Lowest levels E = −ln(λ/λ₀) in the gauge-invariant space (largest run per β)

Labels:
- **center**: ee, eo/oe (2-fold, exchange images) or oo.
- **L-par**: + or −, the parity under U₂→U₂⁻¹.
- **exch**: + or −, U₁↔U₂ (only defined for ee and oo).

β = 2, 4, 8, 16, 32, 64, 128, 256, 512 and 1024 are all reached. The 10 lowest levels for every β, with dE(N), dE(grid) and the Lanczos residual, are in `results/analysis.md`.
- At large β the six lowest levels are:
  1. the ee ground state;
  2. its eo, oe and oo tunnelling copies;
  3. the split doublet (ee,+,−) / (ee,−,+), each accompanied by eo/oo copies.

  For example, at β=1024: 0, ≤1e−15 (eo/oe, oo), 0.1923831345 (ee +−, eo/oe +, oo +−), 0.1933093342 (ee −+, …), 0.230557287 (ee ++).
- At β=2 the order is different. The levels are 0 (ee++), 0.5439 (eo/oe), 1.1667 (oo), 1.6376 (ee), …

### 2b. Gaps

| β | m_e | m_e β^{1/3} | m_e β | local exponent | 2nd ee level (doublet partner) | m_eo | m_oo |
|---|---|---|---|---|---|---|---|
| 2 | 1.63761996 | 2.063272 | 3.27524 | – | 1.88234137 | 5.4390e−01 | 1.1667 |
| 4 | 0.76319885 | 1.211503 | 3.05280 | 1.1015 | 0.99450927 | 1.3393e−01 | 3.0025e−01 |
| 8 | 0.51558519 | 1.031170 | 4.12468 | 0.5658 | 0.61668249 | 1.4768e−02 | 3.0464e−02 |
| 16 | 0.54142013 | 1.364293 | 8.66272 | −0.0705 | 0.60392748 | 3.2111e−04 | 6.4260e−04 |
| 32 | 0.51516418 | 1.635544 | 16.48525 | 0.0717 | 0.54929832 | 7.6936e−07 | 1.5387e−06 |
| 64 | 0.43994233 | 1.759769 | 28.15631 | 0.2277 | 0.45571058 | 8.9923e−11 | 1.7985e−10 |
| 128 | 0.36450079 | 1.836969 | 46.65610 | 0.2714 | 0.37215008 | < 1e−13 | < 1e−13 |
| 256 | 0.29712330 | 1.886615 | 76.06356 | 0.2949 | 0.30088500 | < 1e−13 | < 1e−13 |
| 512 | 0.23982321 | 1.918586 | 122.78948 | 0.3091 | 0.24168615 | < 1e−13 | < 1e−13 |
| 1024 | 0.19238313 | 1.939100 | 197.00033 | 0.3180 | 0.19330933 | < 1e−13 | < 1e−13 |

Truncation and grid uncertainty: |ΔE| ≤ 4.2e−11 (N→N+16) and ≤ 1.1e−13 (grid +40) for every level E > 1e−6 at every β. So the truncation uncertainty on m_e and on the local exponents is below 1e−9 relative. That is negligible next to the pre-asymptotic drift.

- **Center-odd gaps:** m_oo ≈ 2 m_eo, and −ln m_eo/√β = 1.49, 2.01, 2.49, 2.89 for β = 8…64. This is consistent with exp(−c√β) where the prefactor term still matters. From β=128 on, the splitting is below double precision, so it is not measured. Above the tunnelling copies, the odd sectors repeat the ee spectrum: the first excited eo/oe level equals m_e to the printed digits for β ≥ 128 (to 1e−10 at β=1024, table 2a).
- **Non-monotone behaviour:** m_e has a local maximum near β≈16. In this range the lowest ee excitation passes from the strong-coupling character state to the doublet.

### 2c. Exponent and comparison with the continuum model (MEASURED ONLY)

Continuum h = −½Δ + 2|Y₁×Y₂|² on invariant states:
- E₀ = 3.3505330.
- Gaps: E₁−E₀ = **1.974964** (O(2) doublet; the members agree to 2e−7) and E₂−E₀ = 2.374875.
- Convergence: levels change by ≤3e−7 between (K,Lmax) = (20,32) and (24,40). Monotone decreasing under nested enlargement (16,24)→(20,32)→(24,40) at ω=1. ω=1.5 agrees to 3e−7.

| β | m_e β^{1/3} / E₁ | (doublet partner) β^{1/3} / E₁ |
|---|---|---|
| 64 | 0.8910 | 0.9230 |
| 128 | 0.9301 | 0.9496 |
| 256 | 0.9553 | 0.9674 |
| 512 | 0.9715 | 0.9790 |
| 1024 | 0.9818 | 0.9866 |

(analysis.md divides the doublet partner by E₂. That is a labelling error in my analyse.py column: the partner belongs to E₁. The ratios above are recomputed by hand from the same numbers.)

- **Increments:** successive increments of m_e β^{1/3} are 0.1242, 0.0772, 0.0496, 0.0320, 0.0205. Their ratios are 0.62, 0.64, 0.645, 0.642, close to 2^{−2/3} = 0.630. So the leading correction is ∝ β^{−2/3}.
- **Fits** (measured only):
  - The three-term fit c₀ + c₁β^{−1/3} + c₂β^{−2/3} over β = 32…1024 gives c₀ = 1.9762, c₁ = −0.052, c₂ = −3.27.
  - Geometric extrapolation of the last three points gives 1.9758.
  - Both are within 0.06% of E₁ = 1.97496.
- **Statement (measured only):** the data support exponent 1/3 with limit constant E₁(h), κ=2.
  - The local exponent increases monotonically from β=16 to β=1024 (0.07 → 0.318) and is still below 1/3 at the largest β.
  - Its distance from 1/3 shrinks by about 2^{−2/3} per doubling: 1/3 − p = 0.062, 0.039, 0.024, 0.015.
  - The uncertainty from truncation is < 1e−9. The only real uncertainty is the extrapolation form.
  - m_e β grows without bound (3.3 → 197), so 1/β (U(1)-like) scaling is excluded in this model.
  - This is numerical support for a 2-direction analogue. It is not a proof, and it is not the 3-direction R1.


# Appendix B. Derivations

## D. Derivations

**D1. Transfer matrix from the Wilson action.**
- Action: S = β Σ_p (1 − ½ Re Tr U_p).
- Lattice: sites (0,0,t), t ∈ ℤ. Links: U₁(t), U₂(t) (spatial) and g(t) = U₀(t) (temporal). Each site has exactly one plaquette per plane (12), (01), (02).
- (12) plaquette: U₁(x)U₂(x+1̂)U₁(x+2̂)⁻¹U₂(x)⁻¹ with x+î = x, which is U₁U₂U₁⁻¹U₂⁻¹. It occurs once per time slice. Splitting it symmetrically between the two transfer steps gives e^{−V/2}·…·e^{−V/2} with V = β(1 − ½Tr U₁U₂U₁⁻¹U₂⁻¹).
- (0i) plaquette: g(t)U_i(t+1)g(t)⁻¹U_i(t)⁻¹. Its trace equals Tr(U_i g W_i⁻¹ g⁻¹) (W = U(t+1)), because traces in SU(2) are real and Tr A⁻¹ = Tr A. There is one per spatial link per step.
- The integral over g(t) gives K. On conjugation-invariant functions K is the product of the two link convolutions, followed by the gauge projection.
- Conclusion: no factor differs from the brief.

**D2. Coordinates.**
- Parametrisation: U = cos a + i sin a n·σ. Haar measure = (2/π)sin²a da · dΩ/4π.
- Invariants (a₁, a₂, γ), with measure (2/π)² sin²a₁ sin²a₂ da₁da₂ · ½ sin γ dγ.
- Commutator: ½Tr(U₁U₂U₁⁻¹U₂⁻¹) = 1 − 2 sin²a₁ sin²a₂ sin²γ, so V = 2β s₁²s₂²(1−t²) with t = cos γ. Checked against explicit matrices (C3).

**D3. Basis in which K is diagonal.**
- The functions are S³ hyperspherical harmonics: degree n = 2j, conjugation spin L = 0…n, radial part F_{nL} ∝ sin^L a · C^{(L+1)}_{n−L}(cos a).
- Invariant basis: Φ_{n₁n₂L} = F_{n₁L}(a₁)F_{n₂L}(a₂)√(2L+1)P_L(cos γ), with L ≤ min(n₁,n₂).
- K eigenvalue: ∏_i e^{−β}(2/β)I_{n_i+1}(β), from ∫e^{(β/2)TrU}χ_j/d_j dU = (2/β)I_{2j+1}(β).
- Symmetry labels:
  - center parity: (−1)^{n_i};
  - U₂→U₂⁻¹: (−1)^L;
  - exchange U₁↔U₂: c_{n₁n₂L} ↔ c_{n₂n₁L}.
- What is diagonalised: M = K^{1/2}EK^{1/2} with E_ab = ⟨Φ_a|e^{−V}|Φ_b⟩. It has the same nonzero spectrum as T.
- Quadrature: uniform a-grid (Gauss–Chebyshev-U, exact for the polynomial parts) and Gauss–Legendre in t.
- Eigenvalues: Lanczos with full reorthogonalisation in each of 10 symmetry subsectors. The (o,e) and (e,o) sectors are exchange images, so only (o,e) is computed.
- Truncation n_i ≤ N is a compression, so λ₀ increases monotonically with N (checked, A2).

**D4. Continuum limit and κ.**
- Kinetic term: −ln(I_{n+1}/I₁) = n(n+2)/(2β) + …, which is (1/2β)(−Δ_{S³}) → (1/2β)(−Δ_A).
- Potential: V → 2β|A₁×A₂|².
- Rescaling A = β^{−1/3}Y gives −ln T ≈ β^{−1/3}h with h = −½(Δ_{Y₁}+Δ_{Y₂}) + 2|Y₁×Y₂|².
- So κ = 2 when U = exp(iY·σ).
- Prediction: m_e β^{1/3} → E₁(h), the first excitation of h among rotation-invariant states.
- The four center copies of the identity carry identical local models. So the center-even sector contains each local level once, and the center-odd sectors contain copies split by tunnelling.
- h has an O(2) flavour symmetry (rotations of the pair (Y₁,Y₂)). Its first excited level is a doublet that the lattice splits into (L even, exch −) and (L odd, exch +).
- E₁ was computed independently: Rayleigh–Ritz in a 3D harmonic-oscillator basis on ℝ³×ℝ³, coupled to invariants, with exact generalised Gauss–Laguerre matrix elements (cont.py). This uses no group, no Bessel functions and no lattice code.

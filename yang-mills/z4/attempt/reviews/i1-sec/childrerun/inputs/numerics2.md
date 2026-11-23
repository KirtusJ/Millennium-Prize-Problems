# g2-numchal report (task T78): challenge of NUMERICS.md (SU(2), 1×1×ℤ transfer matrix)

Control: `control.txt` = 0.272341 (−ln tanh 1), written first. Lean was READY but I did not use it, and I make no Lean claim.
Numpy only (no scipy, no mpmath), so every special function is my own code.

## 1. Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| A1 operator: V = β(1−½ReTr U₁U₂U₁⁻¹U₂⁻¹), one (0i) plaquette per link per step, temporal link = gauge projection | STANDS | My own derivation (§D) agrees. On invariant f, K∘P = K because k is a class function. V formula vs explicit 2×2 matrices: 4.4e−16 (C3). |
| A1 "center-even" and the gap definition | STANDS | z_i: (a_i, n_i) → (π−a_i, −n_i), so t → −t (character parity (−1)^{n_i}). m_e = −ln(λ₁/λ₀) within the ee sector, all other labels included. C4: the operator commutes with z₁, z₂ to 7e−16. |
| A2 m_e at β = 2, 4, …, 1024 (all ten β) | STANDS | Independent Nyström grid + Funk–Hecke kernel by quadrature (no Peter–Weyl, no Bessel I). Agreement ≤ 4.6e−9 at every β (compare1: met 26, failed 0). |
| A2 second ee level and m_eo (β ≤ 64) | STANDS | 2nd level ≤ 1.1e−8 abs. m_eo rel ≤ 3.6e−5 (e.g. β=64: 8.992296e−11 vs 8.9923e−11). |
| A3 E₀(h) = 3.3505330 | STANDS | Child T80 sine-DVR 3.350533072, my rerun of the child's code identical. Grandchild T81 (different code) 3.35053307. |
| A3 E₁(h) = 5.3254970, gap 1.974964 | STANDS | (L even, exch −) sector: 5.325497476 at N=32 and N=64 (5.325497476 − 3.350533072 = 1.974964404). The (L odd, exch +) partner is unconverged: 5.319587 → 5.324760 (N 32→64); a dr³ extrapolation gives 5.32550. |
| A3 symmetry class of E₁ | STANDS | O(2) doublet of charge 2: (inversion +, exch −) ⊕ (inversion −, exch +). Degeneracy is exact by the O(2) symmetry (§D4). The center-even lattice sector contains both members. The lattice data split them (0.19238 vs 0.19331 at β=1024), as charge 2 under D₄ requires. |
| Child's claim "E₁ not degenerate, splitting 7.4e−4" | DEFECT (child's, not target's) | Caused by the child's unconverged L-odd grid. The split shrinks ×8 per halving of dr. Exact O(2) symmetry forbids it. |
| A4 κ = 2 with −½Δ for U = exp(iY·σ) | STANDS | Unit S³ in Y (ds² = da² + sin²a dΩ²); −ln(I_{n+1}/I₁) ≈ n(n+2)/(2β); commutator angle 2\|Y₁×Y₂\| ⇒ V ≈ 2β\|Y₁×Y₂\|²; scale Y = β^{−1/3}Z. |
| A4 fit E + cβ^{−2/3} on β=128…1024 | STANDS (limit compatible) | E = 1.9728 ± 0.0014 (σ = leave-one-out spread). E₁ − E = 2.2e−3 = 1.5σ. |
| A5 extrapolation form | STANDS | Pure β^{−1/3} gives rms 10.6× worse (E = 2.045). 1/ln β: rms 3.3e−3, excluded. Free exponent p = 0.637. β^{−2/3}+β^{−1} gives E = 1.97496 ± 0.00003, rms 4.6e−6. |
| NUMERICS.md verdict-table phrase "geometric extrapolation gives 1.974" | DEFECT (minor, reporting) | Its own §2c and my recomputation give 1.97583 for the geometric extrapolation of the last three points. "1.974" is not what that method yields (the brief repeats it). |
| A6 "center-odd splittings exp(−c√β)": the numbers | STANDS (β ≤ 64) | My m_eo agrees to ≤ 3.6e−5 relative at β = 2…64. |
| A6 the functional form exp(−c√β) | DEFECT (overclaim) | The local exponent of −ln m_eo in β is 0.93, 0.81, 0.72 (β = 8→64), still well above 1/2, and −ln m_eo/√β is still rising. A WKB heuristic gives c ≈ 4.8, but the data do not establish √β. |
| m_eo for β ≥ 128 | NOT CHECKED | Below double precision (≤ 1e−16), as the target says. |

Verdict counts over these 15 rows: **STANDS 11, DEFECT 3** (one of them the child's), **NOT CHECKED 1**.

Predicate counts over my programs: **met 52, failed 4, measured only 32**.
- Met: controls 3, spectrum residual predicates R 20, fits 3, compare 26.
- Measured only:
  - 21 alternative-fit E values;
  - 4 m_eo local exponents;
  - 6 child-rerun numbers;
  - 1 WKB constant.

## 2. Hypotheses and where they are stated

| # | hypothesis | where | status |
|---|---|---|---|
| H1 | Wilson action β Σ_p(1−½ReTr U_p), symmetric split e^{−V/2}Ke^{−V/2} | NUMERICS D1; my §D1 | derived |
| H2 | ½Tr comm = 1 − 2s₁²s₂²(1−t²); Haar = (2/π)sin²a da dΩ/4π | NUMERICS D2; nys.py docstring | C3 (matrices) |
| H3 | Funk–Hecke: the per-link kernel on partial wave l is e^{β(cos(a−a′)−1)} e^{−z}i_l(z), z = β sin a sin a′ | my §D2; nys.py docstring | C1 (closed forms to 8.8e−15), C2b (V=0 spectrum = products of class eigenvalues to 5e−13) |
| H4 | Nyström on a_k = kπ/(n+1) with sin² weights + Gauss–Legendre in t converges | nys.py | base vs refined grids: Δm_e ≤ 1.2e−6 (β=16), ≤ 7e−8 elsewhere |
| H5 | Lanczos converged | nys.py | residual ≤ 6.4e−15·λ₀ in every run |
| H6 | continuum limit A = β^{−1/3}Y, κ = 2; the center-even sector contains each local level once | NUMERICS D4; my §D3 | κ derived. The limit itself is supported numerically only (fits), not proved. |
| H7 | exact O(2) symmetry of h ⇒ E₁ is a degenerate doublet | my §D4 | elementary argument |

## 3. Failed predicates (all kept)

1. **controls1**: the run crashed with exit 1. My own defect: a numpy bool is not JSON-serialisable. The partial file `results/controls1.json` is kept.
2. **controls2 C1**: the recurrence residual was 5.7e−12 against a tolerance of 1e−13. My own expectation: the recurrence amplifies the ~1e−14 absolute quadrature error by (2l+1)/z ≈ 800 at z = 0.1.
3. **controls2 C2**: my own test design. With 60 Lanczos steps only 3 distinct V=0 eigenvalues appeared, because degenerate copies took the slots. The 3 that appeared agree to 5e−13. The amended C2b (14 eigenvalues) was met.
4. **controls_b C1b**: the amended recurrence tolerance was still exceeded, by a factor 1.8. My own expectation: the per-value absolute error is ~1e−14, not 1e−15.

None of these is a defect of the target.

Not a predicate, but a defect in my own process: the background wrapper for `child-run1` was killed by my session's 600 s background limit, not by `--timeout 900`. So **no `child-run1` record exists in my register**. The child had already finished (report.md written, T81 released). Instead I recorded my rerun of the child's solver as check `child-rerun-solve2` (K7).

## 4. Not checked

- No proof of anything. The identification lim β^{1/3}m_e = E₁(h) is supported numerically only. The β^{−2/3}+β^{−1} fit hits E₁ to 3e−5, but the extrapolation form is an assumption.
- m_eo for β ≥ 128 (below double precision), and so the √β law.
- E₁ in the (L odd, exch +) sector is not converged beyond N=64. Its equality with the (L even, exch −) value rests on the extrapolation plus the symmetry argument.
- The three-direction model (R1) is not touched.
- I did not use the target's programs (not available). Table values were taken from NUMERICS.md as printed.
- No Lean.

## 5. Delegation

- **Child T80** (admitted under T78; released, event seq 171). Model: sonnet. Question (A3): E₀ and E₁ of h on rotation-invariant functions, and the symmetry class of E₁.
  - **Control:** −½d²/dx²+½x² ground state. Graded before reading anything else: 0.499997. Correct to 5 digits, not to the 6 decimals requested. **Partial pass.**
  - **What came back:** E₀ = 3.350533, E₁ = 5.32475 (L odd, exch +) with a separate level 5.325497 (L even, exch −), and the claim that they are not degenerate.
  - **My reread:** the DVR kinetic term, the centrifugal term, and the Legendre X-matrix c_L = (L+1)/√((2L+1)(2L+3)) are all correct.
  - **My rerun (scratch copy and recorded K7):** reproduces 3.350533072 / 5.325497476 / 5.319587 / 7.11525 exactly.
  - **N=64 rerun:** 1+ = 5.324760, 0− = 5.325497476.
  - **Conclusion:** the child's non-degeneracy claim is wrong. Its 1+ value is unconverged (dr³ extrapolation 5.32550). The doublet is exact by O(2).
- **Grandchild T81** (admitted by the child under T80; released, seq 167). Question: E₀ alone by a different discretisation, with control 3-D HO = 1.5.
  - The child reports control 1.5000000000000158 and E₀ = 3.35053307, and says it reran this.
  - I did not rerun grandchild/e0.py myself.

## 6. Registers

- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp` → `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl` → `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## 7. Rerun (from /home/user/z4-workers/g2-numchal; results are opened with mode "x", so move results/ away first)

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
$P check --ws pcp --name controls2 --expect-exit 0 -- python3 nys.py controls results/controls2.json     # exits 1 (C1, C2: own expectation/design)
$P check --ws pcp --name controls_b --expect-exit 0 -- python3 nys.py controls_b results/controls_b.json # exits 1 (C1b)
$P check --ws pcp --name sweep1 --expect-exit 0 --timeout 1200 -- ./run_sweep.sh      # beta 2..64, ~2 min
$P check --ws pcp --name sweep2 --expect-exit 0 --timeout 1800 -- ./run_sweep2.sh     # beta 128,256, ~1.5 min
$P check --ws pcp --name sweep3 --expect-exit 0 --timeout 2400 -- ./run_sweep3.sh     # beta 512,1024, ~6 min
$P check --ws pcp --name fits1 --expect-exit 0 -- python3 fits.py results/fits1.json
$P check --ws pcp --name compare1 --expect-exit 0 -- python3 compare.py results/compare1.txt
# single run: python3 nys.py spec <beta> <n_a> <n_t> <n_c> <lanczos_steps> <outfile>
mkdir -p childrerun/results; cp child/solve2.py childrerun/
$P check --ws pcp --name child-rerun-solve2 --cwd childrerun --expect-exit 0 -- python3 solve2.py --R 8 --N 32 --nL 8 --nev 2 --tag X
(cd childrerun && python3 solve2.py --R 8 --N 64 --nL 8 --nev 2 --sectors 1+,0- --tag Y)     # ~4.5 min, not recorded (run in scratch)
# child (in child/): $P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp ; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

## D. Derivations (short)

**D1. Model.**
- Sites (0,0,t). Each site has one plaquette in each of the planes (12), (01), (02).
- The (12) plaquette is U₁(x)U₂(x+1̂)U₁(x+2̂)⁻¹U₂(x)⁻¹ = U₁U₂U₁⁻¹U₂⁻¹, so V = β(1−½ReTr C).
- The (0i) plaquette is g U_i(t+1) g⁻¹ U_i(t)⁻¹. It gives the per-link weight e^{β(½ReTr(U W⁻¹ ⋯)−1)}, and the integral over g projects onto gauge-invariant functions.
- On invariant f with class-function k, the output is already invariant. So "K = product of the two convolutions" is right.
- No factor 2 is missing, and there is no extra plaquette.

**D2. Kernel by Funk–Hecke.** Write W = cos a′ + i sin a′ n′·σ. Then ½Tr(UW⁻¹) = cos a cos a′ + sin a sin a′ n·n′. Integrating n′ against P_l(n₁′·n₂′) gives

  (Kf)(a₁,a₂,t) = Σ_l f_l(·) ⊗ κ_l ⊗ κ_l · P_l(t), with κ_l(a,a′) = e^{β(cos a cos a′−1)} i_l(β sin a sin a′).

I compute this by Gauss–Legendre quadrature of ½∫e^{z(c−1)}P_l(c)dc.

**D3. κ.**
- In U = exp(iY·σ) the Haar metric is that of the unit S³.
- −ln(c_n/c_0) ≈ n(n+2)/(2β) = (1/2β)(−Δ_{S³}) → −(1/2β)Δ_Y.
- C ≈ exp(±2i(Y₁×Y₂)·σ), so V ≈ 2β|Y₁×Y₂|².
- With Y = β^{−1/3}Z, −ln T ≈ β^{−1/3}[−½Δ_Z + 2|Z₁×Z₂|²]. So κ = 2.
- Mixing conventions (kinetic coefficient from a radius-2 S³, i.e. ×¼, but κ kept at 2) would multiply the predicted gap by (¼)^{2/3} = 0.397 (or 4^{2/3} = 2.52 the other way). The data (1.9728 ± 0.0014) exclude both.
- A consistent change of variables Y′ = 2Y leaves the constant unchanged.

**D4. O(2) symmetry.**
- (Y₁,Y₂) → (cY₁+sY₂, −sY₁+cY₂) leaves Y₁×Y₂ invariant (det = 1) and the R⁶ Laplacian invariant.
- SO(3)-invariant functions are even under (Y₁,Y₂) → −(Y₁,Y₂), so only even O(2) charges occur.
- The charge-2 pair cos2θ, sin2θ has labels (inv +, exch −) and (inv −, exch +), which is the observed E₁ pair. On the lattice D₄ splits it.
- Both members are center-even: they are local states at U = 1, symmetrised over the 4 center copies.
- The lattice ee ++ level × β^{1/3} = 0.2305573 × 10.079 = 2.3238 at β=1024, approaching E₂−E₀ = 2.374875.

## Plain answer

- **Lattice numbers:** I reproduce every m_e (β = 2…1024), the second ee level, and m_eo (β ≤ 64) to ≤ 5e−9 with an independent method. I could not break them.
- **Continuum operator:** the normalisation κ = 2 is right.
- **Symmetry sector:** E₁(h) = 5.325497 sits in an O(2) charge-2 doublet, and the center-even sector contains it. So the identification is the right one.
- **Limit:** the extrapolated limit agrees with E₁ to about 1e−3 under any reasonable fit form, and to 3e−5 under β^{−2/3}+β^{−1}. That agreement is numerical, not a theorem.
- **Two overstatements in the target:**
  - "geometric extrapolation gives 1.974": its own method gives 1.9758;
  - "exp(−c√β)": the data up to β=64 do not determine the exponent.

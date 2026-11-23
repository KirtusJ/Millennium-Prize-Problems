# i1-tunnel report (worker of Director Z4, task T101)

Control: `control.txt` = 0.272341 (−ln tanh 1).
Lean was READY. I did not use it and make no Lean claim.
I share a model family with the director, so my agreement with the heuristic is not independent review.

## 1. Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| (i) ε(a) = arccosh(1+2 sin²a) is the exact discrete-time ground energy of the two transverse directions | STANDS | Tr Tⁿ = ∏ₖ(2cosh e − 2cos θₖ)^{−1/2} = Σ e^{−(m+½)ne}, with cosh e = 1+2s². Ground energy is e/2 per dimension, so e for two dimensions; ε = 2 asinh(sin a) (theory.py T4; the child derived the same independently). |
| (ii) WKB relation S′²/2 = ε − E in discrete time with a Gaussian step | STANDS (leading order) | ∫e^{−βu²/2+√β S′u} = e^{S′²/2} exactly. The S″ term is O(β^{−1/2}). The Haar factor sin²a changes only the prefactor (ψ = φ/sin a), not the exponent. |
| Leading coefficient c = 4.6054132 | STANDS (as the derivation's output) | Recomputed: 4.605413 (mine), 4.605413 (child). The continuous-time 4.7925610 is only the small-a limit of ε. |
| Brief's claim that the E-correction "diverges at the ends" | DEFECT | ε ≈ 2a is linear at the ends, so ∫da/√(2ε) converges: d = 2.68280. The β^{1/6} coefficient is −E₀·d = −8.989. The region a ~ β^{−1/3} contributes only O(1). |
| Prediction −log m_eo = 4.6054√β − 8.989 β^{1/6} + p log β + b (stated before measurement) | STANDS in c; q is about 12% off | Over β ≥ 96 the free fit c√β + qβ^{1/6} + k gives c = 4.5994 and q = −7.78. With c fixed at 4.6054: q = −8.08, p = 0.08, maxres 2.4e−4. With q also fixed at −8.989: maxres 3.1e−3. |
| Data favour c = 4.6054 over 4.7926 | STANDS (measured, not proof) | The free-c fits with β^{1/6} give 4.6156 / 4.6040 / 4.5994 for β ≥ 32 / 64 / 96. With c = 4.7926 forced, q (−15 to −17) and p (1.7 to 2.4) drift and the residual is 5–6× larger. The log-form fit gives c = 4.42–4.44, drifting upward. |
| Double-precision values 1.4768e−02, 3.2111e−04, 7.6936e−07, 8.9923e−11 | STANDS | My double-double code reproduces all four to the printed digits, and m_oo too (analysis.md, C@8–64). |
| m_eo at β = 96, 128, 192 | measured, NC met | 6.8644e−14, 1.4597e−16, 4.1266e−21. The change under N+8 / M+16 is 8.8e−7, 2.0e−4, 6.1e−7. |
| m_eo at β = 256 | measured; 3rd digit not guaranteed by my error bound | 5.4032e−25. Change N120→132: 2.7e−6. The Rayleigh-quotient (RQ) bound res²/gap is 1.6e−3 relative (predicate E failed). |
| Brief's "expected sizes" 1e−18, 1e−24, 1e−30 at 128, 192, 256 | DEFECT (of the brief's estimate) | Measured 1.5e−16, 4.1e−21, 5.4e−25. The estimate assumed pure c√β growth, but the local slope is only 4.06–4.17. |
| m_oo/m_eo → 2 | STANDS (measured) | 2.00000 for β = 64…192 and 1.99998 at β = 256. |
| β = 384, 512 | NOT CHECKED | The required N (~150–200) and the RQ precision limit (~1e−28) are beyond double-double plus the budget. |
| Optimal tunnelling path lies on a₂ = 0 (one link stays at the identity) | NOT CHECKED | Assumed in the heuristic and not proved. The fit c ≈ 4.60 is consistent with it. |

Counts over the 13 rows: STANDS 8, DEFECT 2, NOT CHECKED 2, measured 1 (the β = 256 row).
Predicate counts over all programs: **met 144, failed 7, measured only 34**:
- 34 measured-only items: 8 local slopes, 8 m_oo/m_eo ratios, 18 fits in results/analysis3.md.

## 2. Measurement (results/analysis.md; fits from results/analysis3.md)

| β | N, M | m_eo | −log m_eo | −log m/√β | local slope | m_oo/m_eo | rel. change in N (eo) |
|---|---|---|---|---|---|---|---|
| 8 | 24, 61 | 1.47683e−02 | 4.2153 | 1.4903 | – | 2.06282 | – |
| 16 | 32, 81 | 3.21110e−04 | 8.0437 | 2.0109 | 3.268 | 2.00119 | – |
| 32 | 40, 101 | 7.69363e−07 | 14.0777 | 2.4886 | 3.642 | 1.99999 | – |
| 64 | 56, 141 | 8.99233e−11 | 23.1321 | 2.8915 | 3.864 | 2.00000 | 3.0e−8 |
| 96 | 68, 161 | 6.86439e−14 | 30.3098 | 3.0935 | 3.992 | 2.00000 | 8.8e−7 |
| 128 | 76, 177 | 1.45974e−16 | 36.4631 | 3.2229 | 4.060 | 2.00000 | 2.0e−4 |
| 192 | 108, 241 | 4.12662e−21 | 46.9368 | 3.3874 | 4.119 | 2.00000 | 6.1e−7 |
| 256 | 132, 289 | 5.40315e−25 | 55.8776 | 3.4924 | 4.171 | 1.99998 | 2.7e−6 |

The local slope rises toward c from below, as a negative β^{1/6} term predicts. At β = 256, c + q/3·β^{−1/3} with q = −8 is about 4.6 − 0.42 = 4.18, which is consistent with the measured 4.171.

**Fits.** Each fit form is applied over β ≥ 32 / 64 / 96 (6, 5 and 4 points); "maxres" is the largest absolute residual.

| fit form | β ≥ 32 | β ≥ 64 | β ≥ 96 |
|---|---|---|---|
| c√β + p log β + k: c | 4.4218 | 4.4321 | 4.4401 |
| c√β + q β^{1/6} + k: c | 4.6156 | 4.6040 | 4.5994 |
| c√β + q β^{1/6} + k: q | −8.04 | −7.86 | −7.78 |
| c = 4.605413 fixed, free q, p, k: q | −7.61 | −7.92 | −8.08 |
| c = 4.605413 fixed: p | −0.10 | 0.01 | 0.08 |
| c = 4.605413 fixed: maxres | 3.4e−3 | 7.7e−4 | 2.4e−4 |
| c = 4.792561 fixed, free q, p, k: q | −15.3 | −16.5 | −17.2 |
| c = 4.792561 fixed: p | 1.7 | 2.1 | 2.4 |
| c = 4.792561 fixed: maxres | 1.2e−2 | 3.9e−3 | 1.4e−3 |
| 4-parameter fit (c√β + qβ^{1/6} + p log β + k): c | 4.536 | 4.558 | 4.566 (exact fit) |

What the fits say:
- **c:** the data favour c ≈ 4.60 ± 0.02 (β^{1/6} form), which agrees with 4.6054. They do not support 4.7926: forcing it needs a drifting, large q and p, with residuals 5–6× larger.
- **The log-only form** gives c ≈ 4.43, drifting upward. It is the wrong form, or it needs β^{1/6} as well.
- **Caveat:** the β range is short (√β = 5.7 to 16), and 3–4 parameter fits over 4–6 points are weakly determined. This is evidence, not a determination of c beyond about ±0.05.

## 3. Hypotheses used and where they are stated

| # | hypothesis | where |
|---|---|---|
| H1 | T = e^{−V/2}Ke^{−V/2}, V = 2β s₁²s₂²(1−t²), K eigenvalue ∝ I_{n+1}(β) per link | NUMERICS.md D1–D3; ddmeas.py docstring |
| H2 | Peter–Weyl basis F_{nL}(a) = sin^L a · p^{(L+1)}_{n−L}(cos a), orthonormal | ddmeas.py radial_vals; checked by D3 (1e−30) |
| H3 | Ground state of each centre sector lies in L-even | ddmeas.py docstring. Supported only by reproducing the double-precision values at β = 8–64. I did not run the L-odd sector. |
| H4 | Double Lanczos Ritz vector plus a double-double Rayleigh quotient gives λ to about res²/gap | ddmeas.py docstring; gap lower bound 0.1 (m_e ≥ 0.19 for β ≤ 1024 in NUMERICS.md) |
| H5 | Truncation n ≤ N and quadrature (M, Mt) are converged when the N+8 / M+16 change is < 1e−3 | analyse2.py (NC) |
| H6 | Born–Oppenheimer separation; the slow link walks on the valley a₂ = 0; group kernel is Gaussian up to O(1/β) | notes.md step 2; heuristic only |
| H7 | Vacuum energy per step is E₀β^{−1/3} with E₀ = 3.3505330 (taken from NUMERICS.md, continuum h) | theory.py; notes.md step 2 |

## 4. Failed predicates (kept)

1. **theory.py T3:** Simpson n = 2000 vs 4000 for d did not agree to 1e−8.
   - Cause: my own defect. Computing arccosh(1+2y²) for tiny y loses precision, giving noise of about 1e−6 (the n = 8000 result is worse).
   - Effect: d = 2.68280 is good to about 1e−5, which is enough for the coefficient −8.989.
   - Fix: write ε = 2 asinh(sin a).
2. **First sweep NC@192 and NC@256** (scratch/a_dev.txt; N84→92 changed 20%, N96→104 a factor of 180).
   - Cause: my own expectation that N ≈ 6√β suffices was wrong. Not a target defect.
   - Resolved by the second sweep (N up to 108 and 132).
3. **D2 at β = 192, N = 100 and 108** (Miller start S vs S+60 agree only to 1e−16 relative).
   - Cause: my own defect. Rescaling by 1e−250 pushes the double-double low parts of tiny values into the subnormal range.
   - Effect: it touches high-n Bessel ratios. NC at 192 is still 6e−7, so the 3 digits are not affected, but the 1e−29 claim fails.
4. **E_oe at β = 256, N = 120 and 132** (bound res²/0.1 = 9e−28 > 1e−3·m).
   - Cause: a limit of my method (double-precision Ritz vector). It is not a target defect.
   - Effect: m_eo(256) is certain to about 2e−3 relative by the bound. The N-change of 2.7e−6 suggests the actual error is smaller.
5. **analyse2/analyse3** exit 1 because of S@192 and S@256 (failures 3 and 4 above, not new).
6. **Not a predicate:** my first rerun of the child's check.py failed because I had not copied child/control.txt into the rerun directory. That was my own error. The rerun with it gave output identical to the child's.

## 5. Not checked

- β = 384 and 512.
- L-odd sectors: assumed not to hold any sector ground state.
- Eigenvector refinement in double-double, which would remove the res²/gap limit.
- The lower order terms: no derivation of p or b. No proof that the optimal path is a₂ = 0. No Born–Oppenheimer / Berry corrections.
- Whether the 12% gap between the fitted q ≈ −7.9 and the predicted −8.99 is a missing O(1) effect or mixing with log β in the fit.
- No Lean.
- No independent code for the measurement: the child derived (i) and (ii) only.

## 6. Delegation

- **Child T102** (admitted under T101; run recorded as check `child-run1`, exit 0; released).
  - Model: sonnet.
  - Control: ∫₀^π 2√(sin a) da. It answered 4.792561, which is correct. I graded this first.
  - Question: an independent derivation of (i) and (ii), without my notes.
  - Outcome on (i): ε_tot = 2 asinh(sin a) = arccosh(1+2sin²a) exactly and β-independent. Its grid check agrees to 4e−15.
  - Outcome on (ii): S′²/2 = ε − E exactly for a Gaussian step. The Haar factor enters the prefactor only. c = 4.605413. Both agree with my derivation.
  - One difference: the child took E to be O(1/√β) and dropped it. That came from my prompt's wording (an eigenvalue e^{−E/√β}). The true per-step vacuum energy is E₀β^{−1/3}, so the β^{1/6} term stands. This does not contradict the child's algebra.
  - Its caveat, which I share: identifying −log(splitting) with the full-path action from 0 to π is an assumption.
  - Rerun: I reran child/check.py in scratch/childrerun; the output was identical.
- **Grandchild T104** (admitted by the child under T102; released by the child).
  - Question: an independent numerical top eigenvalue of the 1D operator at β = 50, a = π/2 and a = 0.3, and at β = 200.
  - Returned: 0.4142135624, 0.7472320134, 0.4142135624.
  - These equal 1/(s+√(1+s²)), which agrees with formula (i). The child reports rerunning eig.py with an identical result. I did not rerun the grandchild myself.

## 7. Registers

- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## 8. Rerun (from /home/user/z4-workers/i1-tunnel; result files use mode "x", so move results/ away first)

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
mkdir -p results
$P check --ws pcp --name theory --expect-exit 0 -- python3 theory.py                       # exits 1 (T3, own defect)
$P check --ws pcp --name dd_sweep --expect-exit 0 --timeout 1500 -- ./run_dd.sh             # beta 8..256, 13 runs, ~3 min, 1 thread
$P check --ws pcp --name dd_sweep2 --expect-exit 0 --timeout 1200 -- ./run_dd2.sh           # beta 192 N100,108; 256 N120,132; ~4 min; exits 1
$P check --ws pcp --name analyse2 --expect-exit 0 -- python3 analyse2.py results/analysis.md   # exits 1 (S@192, S@256)
$P check --ws pcp --name analyse3 --expect-exit 1 -- python3 analyse3.py results/analysis3.md
# single run: OMP_NUM_THREADS=1 python3 ddmeas.py BETA N M Mt OUTFILE   e.g. python3 ddmeas.py 192 108 241 240 results/dd_b192_N108_M241.json
# child (in child/):
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp ; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

- Programs: dd.py (double-double library), ddmeas.py, theory.py, analyse2.py, analyse3.py.
- Notes: notes.md.
- Results: results/.
- Task graph: T102 admitted under T101 and released; T104 admitted under T102 by the child and released.

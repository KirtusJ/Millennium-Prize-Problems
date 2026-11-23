# Builder report: reading Wilson loops and smeared observables in the 2D control (W1–W4)

Control: `control.txt` = 0.272341.

**The main finding, stated plainly.** In two dimensions a fixed-size Wilson loop gives no information beyond what χ₁ already gives. W = (c₁/c₀)^(A·N²) holds exactly, so −log W/A = −N² log(c₁/c₀) = M₁(N) for every area. The "string tension" σ_N is the README's gap M(N) itself, and σ = gap·L holds by an algebraic identity, not by a separate limit. The loop with R = 1 is the χ₁ correlator, exp(−M T). W1 therefore confirms the README's table. It does not test it independently. The content that is actually new is in W2 (bounded moments for observables that are not eigenvectors) and W3 (the Lean limit lemma).

## Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| H: convention c_r/c₀ = I_r/I₀ (U(1)), I_{2j+1}/I₁ (SU(2)) | STANDS | M(64) = 0.500061048820197 and 0.375011444266388 match the README to 1e-12 |
| W1 area law, σ independent of A | STANDS | 123 of 183 (N, A) cases qualify (A·N² an integer, N = 4..64). All give \|σ_N(A) − M₁(N)\|/M₁ ≤ 5e-61 |
| W1 σ → 1/2 (U(1)), 3/8 (SU(2)), no renormalization factor | STANDS | σ_64 = 0.5000610488, 0.3750114443. The distance from the limit shrinks by 4.19, 4.04, 4.01, 4.00 (U(1)) and 4.01, 4.00, 4.00, 4.00 (SU(2)) per doubling. N²(σ − σ∞) → 1/4 and → 0.046875 = 3/64 (measured) |
| W1 gap = σ·L | STANDS (trivially) | This is an identity: σ_N ≡ M₁(N) at every N, not just in the limit |
| W1 independent σ by Haar quadrature (delegated) | STANDS | The child's trapezoid quadrature, with no Bessel functions, agrees with mine to all 12 printed decimals at N = 4..64 for both groups. I reran it |
| W1 Z₂, Z₃ on β = N²: σ → 0, W → 1 | STANDS | Z₂ σ = 2.7e-3, 4.1e-13, 3.3e-54, 2.2e-220, each ≤ 1/(1+N²). Z₃ σ_16 = 1.3e-164. At N = 8, A = 1: W = 1 − 3.3e-54 |
| W1 Z₂ on its own trajectory | STANDS | β_N = artanh(e^(−1/(2N²))) ≈ log(2N) gives N²(−log tanh β) = 1/2 exactly. β_N = 2.07948 … 4.85203, matching the README |
| W1 Z₃ on its own trajectory | measured only | β_N = 3.0395, 3.9662, 4.8911, 5.8154, 6.7397, which is ≈ (4/3) log N + (2/3) log 6 (from −log(c₁/c₀) ≈ 3e^(−3β/2)) |
| W2 f₁ = (χ₁+χ₂)/√2: moments bounded, converge | STANDS | U(1): (mean, second moment) goes from (1.2903, 2.2636) at N = 4 to (1.2502, 2.1255) at N = 64, limit (5/4, 17/8). SU(2), spins ½ and 1: (0.6928, 0.5792) to (0.68752, 0.57035), limit (11/16, 73/128). Strictly decreasing in N |
| W2 f₂ = centered heat-kernel delta, s = 1/4, SU(2) | STANDS | (2.9945, 14.953) at N = 4 to (2.97359, 14.7553) at N = 64, limit (2.97350, 14.7544) |
| W2 f₂, U(1) | DEFECT of my own tolerance (the target is fine) | It decreases monotonically: (1.4365, 4.4307) at N = 4 to (1.39311, 4.17984) at N = 64, limit (1.39294, 4.17882). The second moment misses its 1e-3 tolerance by 1.02e-3. See failed predicates |
| W3 Lean `wilson_area_limit` | STANDS | `lake env lean` exits 0 (register K3). Axioms: propext, Classical.choice, Quot.sound. No sorry |
| W3 Z₂ tanh two-level bound in Lean | NOT CHECKED | Not attempted within the time budget |

Counts for wilson2d.py: **met 12, failed 1, measured only 3** (the measured-only items are N²(σ−3/8) for SU(2), the Z₃ own trajectory, and the correlators). Child's program: met 3, failed 0, measured only 0. Lean: one theorem. Draft 1 failed and is kept.

### W2 spectral measure (for the record)
- f₁ has atoms at M₁(N) and M₂(N), each with weight 1/2. For U(1), M₂ = −N² log(I₂/I₀) → 2. For SU(2), M_{spin 1} = −N² log(I₃/I₁) → 1.
- f₂ has atoms at M_r(N). The weights are ∝ e^(−s r²) for U(1), r ≠ 0, and ∝ (2j+1)² e^(−s j(j+1)) for SU(2), j ≥ ½. Both are normalized to unit variance.
- In the limit M_r → C_r/2 (g = L = 1): r²/2 for U(1) and j(j+1)/2 for SU(2).

Both moments are bounded by their N = 4 values over the measured range. Their limits are finite and O(1) in physical units. Compare the README's second-round single-plaquette bounds, which scale like 1/b.

**Which feature of 2D makes this work.** The theory is superrenormalizable and has no perimeter or self-energy divergence. On the trajectory β ∝ 1/a², each c_r/c₀ → exp(−C_r g² a²/2) to order a⁴. So N²·(−log c_r/c₀) has a finite limit for each r, with no Z-factor. A fixed-size observable is a fixed combination of characters with N-independent weights, and its moments converge whenever Σ|f_r|² C_r² < ∞. In four dimensions the Wilson loop has a perimeter self-energy (a linearly divergent factor exp(−c·P/a)), smeared observables need a nontrivial Z, and the trajectory is logarithmic (asymptotic freedom). The step "fixed weights, energies converge" fails there.

## Hypotheses used and where they are stated
- W = (c₁/c₀)^(#plaquettes) for a contractible loop (free boundary, or an infinite cylinder with the vacuum projected outside). For R = 1 the band between two winding lines gives the same formula. This comes from the brief and README §2. **It is not derived or tested on an actual lattice here.**
- Transfer eigenvalues (c_r/c₀)^N on χ_r: README §2, abelian finite case in `CharTransfer.lean`. Not proved for U(1) or SU(2).
- Continuum values C_r/2: quoted from the README and reproduced only as the numerical limits.
- Unit-variance normalization of f uses orthonormality of characters under Haar measure. Standard; not re-derived.
- Lean lemma hypotheses: ρ_N > 0 for all N (ρ ≤ 1 is not used, so I dropped it), N²(−log ρ_N) → σ, and n_N/N² → A with real division (the value at N = 0 is irrelevant). These are in the docstring of `WilsonLimit.lean`.
- The tolerances and their sources are in the `wilson2d.py` docstring: README print precision, working precision minus a margin, the proved bound 1/(1+x), and the README's [3, 5] band.

## Failed predicates
1. **P6_f2_U1** (wilson2d.py, run K1). The second moment at N = 64 is 4.17984 against the limit 4.17882, a difference of 1.02e-3, over the 1e-3 tolerance. **This is my own expectation, not a defect of the target.** I set the tolerance assuming an O(1/N²) correction with constant ~1, taken from χ₁. But the correction for charge r grows roughly like r⁴/N², and the heat-kernel weights reach r ~ 3–4. N²·(difference) ≈ 4.2 is consistent with O(1/N²) convergence. Kept as failed; the tolerance was not changed.
2. **Lean draft 1** (`WilsonLimit_draft1_failed.lean`): `field_simp` left a commutativity goal. Fixed by adding `ring`.

The register records K1 as exit 1 against an expected 0. K2 is the rerun to a new file with expected exit 1, and its JSON is identical to K1's.

## Not checked
- The Wilson-loop formula on an explicit small lattice; the loop is taken from the character expansion.
- The SU(2) convention beyond the two README numbers. In the brief, "χ₂" for SU(2) is ambiguous; I read it as spin 1.
- Uniform boundedness of the moments for N > 64. It is measured as monotone over N = 4..64 with a known limit, not proved. A proof would need M_r(N) ≤ C·C_r for all N.
- The Z₂ tanh Lean bound (optional W3 item).
- Z_n with W2 observables.

## Delegated question and outcome
The question was an independent recomputation of σ_N = −N² log(c₁/c₀) for U(1) (β = N²) and SU(2) (β = 4N², c_½ divided by dimension 2) at N = 4..64, by direct Haar quadrature without Bessel functions. The control question was ∫e^(cos t)dt/2π, and the child answered 1.266066 (correct, = I₀(1)). It used a periodic trapezoid rule (4096 and 8192 nodes, difference ≤ 6e-47) and cross-checked with mpmath.quad at N = 4. Its predicates were met 3, failed 0. Child register verify: PASS. I reread its docstring and reran it (new file `child/results_quad_1.txt`, "FAILED: none"). Its values equal mine to 12 decimals. The child's "pass" was re-checked this way, but child and builder share a model family.

## W4 (suggestion, not a result)
A four-dimensional analogue of W1/W2 would have to contain three things the 2D control lacks:
- **A perimeter self-energy factor:** −log W = σA + μP/a + const, with μ depending on β. Extracting σ needs Creutz-type ratios or a subtraction, not −log W/A.
- **The trajectory β(a) given in advance:** asymptotic freedom, so that σa² → 0 at the right rate. In 2D the trajectory is a closed-form power.
- **A variance floor at fixed physical size:** a smeared or renormalized observable (with gradient-flow radius fixed in physical units) whose variance, after its Z-factor, is bounded below uniformly in a. Every one-plaquette estimate must be redone at that size.

In 2D all three are absent or trivial, which is why the control converges with no renormalization.

## Rerun commands
```
cd C:/Users/donke/z4-workers/r3-fixed
export PYTHONUTF8=1
python wilson2d.py results/<new_file>.json          # exit 1 expected (P6_f2_U1)
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name wilson2d --expect-exit 1 -- python wilson2d.py results/<new_file>.json
(cd C:/Users/donke/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean C:/Users/donke/z4-workers/r3-fixed/WilsonLimit.lean)
(cd child && python sigma_quad.py)
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```
Last line of `pcp_os.py verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`. The child register (child/pcp) verifies with the same line.

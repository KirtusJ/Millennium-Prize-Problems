# report.md — worker q1-E13 (task T149)

Control: control.txt = 0.272341 (−ln tanh 1).

## Verdict table

| item | verdict | evidence |
|---|---|---|
| (E1) lower local Gaussian estimate, o(1) uniform on the tube | STANDS (proved in E13.md §1–5, unreviewed) | explicit Δ1(β) → 0 at rate (log β)^{3/2}β^{−1/2}; pointwise Taylor bound has 0 violations in 1.6e6 samples; sup_K Δ1 = 13.8 at β = 16384, 0.167 at 2.7e8 |
| (E3) upper local Gaussian estimate | STANDS (same) | explicit Δ3(β) → 0; sup_K Δ3 = 5.6 at 16384, 0.204 at 2.7e8 |
| TUNNEL_LOWER2's sketch of E1/E3 (error budget) | STANDS in substance | the cross term O(θ₀M/(ℓ√β)) and the tilt/Hessian terms reappear exactly; L can be √(C log β) instead of β^{1/10} |
| TUNNEL_LOWER2 ansatz "Ψ' = … on [a₋, π−a₋/2], flat after" | DEFECT (wording) | read literally, Ψ' jumps there and E3 fails within O(β^{−1/2}) of the kink; a smooth transition placed after π − a₋/2 is needed (it is called "smooth" elsewhere) |
| exact 2+2+2 decomposition off the valley | STANDS (new: exact) | ℓℓᵀ = S²I − u₁u₁ᵀ − u₂u₂ᵀ − 2wwᵀ, ℓp ∥ w; checked to 9e−16 |
| my own first gap bound DG3 | DEFECT (mine, corrected) | P5 failed 9/11; the corrected bound holds 1858/1858 (p5fix.py) |
| explicit Δ small at simulable β | DEFECT (of the bound's usefulness, not of the theorem) | Δ1 = 13.8 at β = 16384, while the measured defect is 0.06 |
| H4, continuum P', limsup ≤ c* | NOT CHECKED | outside this step |

## Hypotheses used (where stated)

- Model, kernel e^{β⟨U,U'⟩}/Z, Z = 2I₁/β, and the (I6), (I7) Bessel bounds: LEMMA_F.md (I1), (I2), (I6), (I7). I rechecked I1, I2 and ρ numerically (P6).
- The statements of (E1), (E3), the ansatz Ψ, Θ, G, E and the tube: TUNNEL_LOWER2.md §2.
- Flat fixed point log A = ε(S): LEMMA_F (I5). Restated here as (h−2)(1+2S²h) = h; Lean `flat_identity`.
- (H1) Ψ C² with H_Ψ, Λ finite near the tube. This is my reading of "smooth" in TUNNEL_LOWER2 §2.
- (H2) Θ as given, r₀ + 0.1 ≤ π/2. (H3) the tube K with β α q/2 < M².
- Lean (E13.lean; exit 0; axioms propext, Classical.choice, Quot.sound only): `flat_identity`, `sqrt_lower`, `one_sub_sqrt_le`, `cross_bound`.

## Failed predicates (all kept)

Counts per program are given as (met, failed, measured only).

- **e13_bounds.py run1** (register K2): crash, math domain error. The bound was vacuous at β = 256, L = 3. My code defect.
- **run2** (K3):
  - P6 FAILED at β = 2.7e8: my quadrature grid was too coarse. Code defect.
  - Crash, overflow. Code defect.
- **run3** (K5): crash, overflow (my code).
- **run4** (K6, final version v4): P1 1/0, P2 1/0, P3 1/0, P4 8/0, P5 2/9, P6 11/0, P7 11/1. Measured only: 48 CHILDPT values.
  - P5 failed: my own derivation defect (cross term), corrected and rechecked by p5fix.py (K7: 1858 met, 0 failed).
  - P7 final (sup Δ ≤ 0.1 at 2.7e8) failed: my own expectation. The bound decays (0.167, 0.204) but more slowly than I guessed.
- **Child T156:**
  - C1 failed 6/48 at a₁ = 0.5, a₂ ≈ 0. Its expectation |δ| ≤ 4/√β was too small: the measured constant is ≈ 7.6. This is not a defect of E1, which only needs δ1 ≥ −o(1).
  - Its first results file was invalid because of its own bug (fixed before evaluation).
- **Grandchild T157:** its own |√β δ| ≤ 1 expectation failed.
- **Lean first attempt** (K8): `flat_identity` closed by nlinarith failed (sorry in the axioms). Replaced by linear_combination; passes (K9).

## Not checked

- Whether Ψ with a smooth right-end transition still satisfies everything else TUNNEL_LOWER2 needs: only the H_Ψ bound is used here.
- The uniform Q bound is taken via 1 − cos θ ≥ 2θ²/π² as written, and was evaluated numerically only by quadrature.
- The constant for the rate claim is not optimised.
- H4, continuum P', and the conditional conclusion of TUNNEL_LOWER2 §5.
- The Θ cut-off near a₂ ≈ π (only the a₂ ∈ [0, r₀] branch).
- No independent review: I share a model family with the director and with the authors of the input files.

## Delegated questions and outcomes

- **Child T156** (admitted under T149, released). Question: Monte Carlo of δ1 = log(Tf₁/f₁) − [−ε(S) + (Ψ'²+Θ'²)/2] and δ3 on 12 tube points at β = 256, 1024, 4096, 16384.
  - Control: ∫x²e^{−x²/2}/√(2π) = 1.000000. Graded correct before reading anything else.
  - Outcome: δ1 ≥ −0.40, −0.23, −0.12, −0.059 (worst, at a₁ = 0.5, a₂ = 0); δ3 ≤ 0.11 … 0.015. Sampler check 4/4.
  - I read mc.py (the log-ratio formula is correct) and reran it in child_rerun/ (register K4): bit-identical results.
- **Grandchild T157** (admitted under T156, released; control 1.000000). Question: independent recomputation of δ1, δ3 at a₁ = π/2, c = 0, y = 0, β = 1024.
  - Outcome: δ1 = −0.087 ± 0.020 and δ3 = +0.028 ± 0.019, consistent with the child's values within about 1.1σ.
  - The child reports that it reran this. I did not rerun the grandchild myself.

## Rerun commands

```
cd /home/user/z4-workers/q1-E13
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name e13_bounds_rerun --expect-exit 1 -- python3 e13_bounds.py <newtag>     # exit 1 because P5 (old bound) and P7-final fail
$P check --ws pcp --name p5fix_rerun --expect-exit 0 -- python3 p5fix.py <newtag>
mkdir child_rerun2 && cp child/mc.py child/evalp.py child_rerun2/ && $P check --ws pcp --name child-rerun2 --cwd child_rerun2 --expect-exit 0 -- python3 mc.py
cd /home/user/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/q1-E13/E13.lean
cd /home/user/z4-workers/q1-E13 && $P verify --ws pcp && /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

The task graph is /home/user/z4-work/graph/attempt.jsonl: T149 (mine), T156 (child), T157 (grandchild).

## Verify (last lines)

- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Verdict counts: STANDS 4, DEFECT 3, NOT CHECKED 1.

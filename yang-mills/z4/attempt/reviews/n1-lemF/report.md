# report.md — worker n1-lemF (task T134), brief n1-lemF (Lemma F)

**Result: Lemma F (η-form, uniform in s ∈ [0,1]) is PROVED in writing in LEMMA_F.md. There is no explicit power rate; a (log β/β)^{1/4} rate is CLAIMED only. The proved β₀(η) is astronomically large (≈10¹⁴ for η = 0.2).** I share a model family with the director, so this is not independent review.

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| Lemma F, η-form: ∀η ∃β₀ ∀β≥β₀ ∀s∈[0,1]: ε_eff ≥ 2asinh s − η | STANDS (proved here) | LEMMA_F.md Thm 1 + Cor.: trivial ‖F‖≤1 for s≤η/2; Schur/Barta with Gaussian ψ for s≥η/2 |
| Theorem 1 (explicit master bound ‖F‖ ≤ A⁻¹max(M_in, A M_out)) | STANDS | proof in LEMMA_F.md §2; Q6 holds in 24/24 cases (β=64…4096) |
| Explicit uniform rate ε_eff ≥ 2asinh s − C(log β/β)^{1/4} | NOT CHECKED (CLAIMED, sketch only) | LEMMA_F.md §5; constants not written out |
| Kernel identity e^{β cos θ} = e^{β⟨U,U'⟩} = e^β e^{−(β/2)\|U−U'\|²} | STANDS | ½tr(U⁻¹U') = ⟨U,U'⟩ |
| Haar = d²w dφ/(2π²) on disc × circle | STANDS | δ-function Jacobian; reduced B(ρ) matches grandchild's direct S³ quadrature to 10 digits |
| Z = 2I₁(β)/β | STANDS | Q1 rel. err ≤ 2e−12 |
| Flat fixed point α = 2s√(1+s²), e^{−ε} = 1/A, log A = 2 asinh s | STANDS | Lean `fixed_point`, `two_arsinh_eq_log` |
| Brief's suggestion "z ≥ β(1−r)(1−r')" for the I₀ prefactor | STANDS | Lean `amgm_pair` |
| Brief's route as literally suggested (I₀ ≤ e^z everywhere) | DEFECT (of the suggested route, not of the lemma) | it loses a factor √(2πβ). It is used only in the outer region, where the curvature gain Φ ≤ −r²(1−A⁻²)²/64 pays for it |
| Plain Gaussian ψ gives a Barta ratio < 1 at every s | DEFECT (expected; this is why small s is treated separately) | β=64, s=0.01: B_sup = 1.0071 > 1 at ρ=1 (child and me) |
| Lemma R (target's reduction) | NOT CHECKED analytically | used only as a numerical reference: −log B_sup ≤ ε_eff in 24/24 cases (Q5), as Schur requires |
| TUNNEL_THEOREM §1(iii) numbers (ε_eff − ε = −c/β) | STANDS (consistent) | my calls of eps_eff.py: β·(ε_eff−ε) ∈ [−1.01, −0.65] at β = 1024/4096 |

Counts: 7 STANDS, 2 DEFECT (both in the suggested heuristic route, not in the lemma), 3 NOT CHECKED. Predicates (run2): 102 met, 0 failed. Measured only: the 24-row table, the master-deficit table, and max(Φ − bound) = −1.6e−8.

Numbers (run2, β·(−log B_sup − 2asinh s)): β=4096 gives −1.96 (s=0.01) to −0.80 (s=1). So the plain Gaussian test function already shows ε_eff ≥ ε − 2/β numerically. The analytic loss is entirely in the outer-region estimate. At β ≤ 4096 the master bound is valid but useless (deficit 6.5 to 14 nats). At β = 10¹² it gives 2.5e−4 for s ≥ 0.3, but still 24.9 for s = 0.1.

## 2. Hypotheses each statement uses (where stated)

- **Theorem 1** (LEMMA_F.md §2): β > 1, s ∈ (0,1], 0 < τ < 1/5, 0 < δ ≤ 1. It also uses the kernel definition k = e^{β cos θ}/Z and V = 2βs²ρ², both from TUNNEL_THEOREM §0–1.
- **I4 Schur test**: F has a symmetric, positive kernel and ψ > 0 (§1 I4).
- **I6**: δ ≤ 1, which is needed for Mathlib's `Real.cos_bound` (§1 I6).
- **I7**: z > 0. The bound is nontrivial only for z ≳ 1, and D > 0 needs β > 1 (§1 I7).
- **I9**: c ≥ 0, r ∈ [0,1], μ ∈ [½,1] (§1 I9).
- **Corollary**: η ∈ (0,1]. It also uses ‖K‖ ≤ ∫k = 1 (§3a).

## 3. Failed predicates (kept)

- **check_lemF run1** (register K1, exit 1): ZeroDivisionError at β = 64. My program used τ = β^{−1/3} = 1/4, which violates Theorem 1's hypothesis τ < 1/5. This is a defect of MY program, not of the target. Predicates Q1–Q4 had printed passing values before the crash. Fixed in run2 with τ = min(β^{−1/3}, 0.15), recorded in the docstring.
- **First Lean attempt of `two_arsinh_eq_log`**: the proof script failed (my script). Rewritten; it now passes.
- **Child**: its run1 was OOM-killed and its run2 hit a timeout (its own defects, kept in child/).
- **Run2**: no failures. Q7, my own expectation that the deficit is ≤ 3/β for s ≥ 0.1, was met.

## 4. What I did not check

- Lemma R analytically. My proof does not use it.
- The explicit rate in LEMMA_F.md §5.
- The size of β₀(η) beyond the measured deficits.
- DLMF / arXiv: nothing was fetched. Every Bessel bound used is proved elementarily in LEMMA_F.md.
- The downstream use of Lemma F (TUNNEL_THEOREM §4–5).
- Whether Tunnel.lean's other lemma, `valley_energy_ge`, is used correctly. It compiled.

## 5. Delegated questions and outcomes

- **Child T138** (admitted under T134, run as child-run1 = register K3, exit 0 in 370 s, then released).
  - Question: quadrature of B_sup for β ∈ {64, 256, 1024, 4096} × s ∈ {0.01, 0.03, 0.1, 0.3, 0.6, 1}.
  - Control: Z(1) = 1.130318. I graded it first: it is correct, = 2I₁(1), and my own recomputation also gives 1.130318.
  - Outcome: its 24-row table agrees with my independent program (check_lemF.py) to ≥ 7 digits, e.g. β=256, s=0.3: 0.55631104 against my 0.55631064 (my sup grid is coarser) and argmax 0.119 against 0.118.
  - I reran its barta.py myself (register K5, exit 0). Its output file is identical to its res3.csv.
- **Grandchild T139** (admitted under T138 by the child, then released, as the child reports).
  - Question: direct S³ quadrature without the φ'-reduction, at β=64, s=0.3, ρ ∈ {0, 0.2}.
  - Control: Z(1), passed.
  - Outcome: B(0) = 0.5576952560 and B(0.2) = 0.5641050417. My program gives B(0) = 0.5576952560003, so the coordinate reduction (I3) is confirmed independently.
  - Caveat: the grandchild's run.py writes with mode "w", which the child reports.

## 6. Rerun commands

```
cd /home/user/z4-workers/n1-lemF
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"            # control: 0.272341
$P check --ws pcp --name check_lemF_run3 --expect-exit 0 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 check_lemF.py run3
$P check --ws pcp --name lean_LemmaF2 --expect-exit 0 -- bash -c "cd /home/user/z4-lean && PATH=\$HOME/.elan/bin:\$PATH lake env lean /home/user/z4-workers/n1-lemF/LemmaF.lean"
$P check --ws pcp --name lean_Tunnel_copy2 --expect-exit 0 -- bash -c "cd /home/user/z4-lean && PATH=\$HOME/.elan/bin:\$PATH lake env lean /home/user/z4-workers/n1-lemF/Tunnel_copy.lean"
$P check --ws pcp --name child-barta-rerun2 --cwd child --expect-exit 0 --timeout 600 -- python3 barta.py res_rerun2.csv
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

(check_lemF.py reads eps_eff.py from this directory and writes results/check_lemF_<tag>.json with mode "x".)

Last lines of the verification:
- `pcp_os.py verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

Lean: LemmaF.lean exits 0. `#print axioms` shows only propext, Classical.choice and Quot.sound, and there is no sorry. /home/user/z4-lean/READY exists.

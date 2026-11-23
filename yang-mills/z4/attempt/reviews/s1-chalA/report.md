**Overall verdict: I could not break the assembly. Every change C1–C7, every interface (1)–(7), Lemma L4 and the chain x → σx STANDS as an argument, and the factor is c*, not 2c*. Three wording inaccuracies are listed below; none changes a conclusion. The result is still conditional on the unreviewed insides of the parts (E13, LEMMA_F, Lemma K, (B)), and I share a model family with the authors, so this is not independent review.**

Worker s1-chalA, task T164. Control: control.txt = 0.272341. No network was used. Lean READY exists, but I used no Lean and claim no Lean result.

Counts:
- Verdicts: 16 STANDS, 0 DEFECT, 0 NOT CHECKED (out of 16 items).
- My predicates: 47 met, 3 failed, 6 quantities measured only (in each run).
  - The 3 failures are all Q4 at small β or small η.
  - "Met" counts per-case Q1–Q8 evaluations over runs K2, K3 and K4.

## 1. Verdict table

| item | verdict | one line of evidence |
|---|---|---|
| C1 (η' := a₋) | STANDS | E13's constants depend on η' only through fixed quantities, so it can be fixed before β → ∞. **Wording:** FULL says "only through sin²η'", but E13 l.69 also has s₋⁻⁴ and h(s₋). These are still fixed at fixed η, so this is harmless. |
| C2 (Ψ' = χ√(2(ε+η)), smooth) | STANDS | Ψ'=0 near 0 and π gives H_Ψ < ∞. Ψ is strictly increasing on [a₋, π−a₋/2] ⊃ [a₋, π−a₋], which is what the max argument needs. |
| C3 (Θ̃ smooth, nondecreasing) | STANDS | Θ̃ ≥ Θ(π/2) > Θ(r₀) beyond π/2, so supp(E−c₂)₊ = {a₂ < r₀} is unchanged. |
| C4 (chain written in §4) | STANDS | See the "chain" row. |
| C5 (L4 replaces the sketches) | STANDS | See the "L4" row. M4 for f and g then gives ∫_S f² → 1 and m_B → ¼. |
| C6 (wording e^{−√β min(Ψ(a₁),Ψ(π−a₁))}) | STANDS | This is correct. TUNNEL_LOWER2 §4's "e^{−√βΨ(a₁)}" is false for a₁ > π/2, but its §5 uses 2Ψ(π/2). |
| C7 (0 ≤ Ψ' ≤ √(2(ε+η)) on the transition) | STANDS | Needed for 2Ψ(π/2) ≤ c*(η). In 1D, 2Ψ(π/2) = 4.808 < c*(0.25) = 5.166 and 4.756 < c*(0.1) = 4.845. |
| (1) sets | STANDS | On supp φ_L, V < 2M²S/√(1+S²) < 2M². R_well ⊂ D_M ∪ σ₁D_M. K ⊇ Ω∩{a₁ ≤ π/2} after C1. S ⊂ {V ≤ 1 ≤ 2M²}. |
| (2) Lemma C on Ω | STANDS | The middle a₁ = π/2 is INTERIOR to Ω, so there is no cut there. At a₁ ≤ π/2, Tφ ≥ Tφ_L ≥ λφ_L = λφ. The entrance set R_well lies in Ω^c with φ ≤ μ ≤ g. ‖T_ΩΩ‖ ≤ sup_{a₁∈[a₋,π−a₋]}‖F_{a₁}‖ uses only Ω ⊂ that slab, and Lemma F is uniform in s ∈ [η/4, 1]. 1D: Q3 8/8, Q5 5/5. |
| (3) μ from HARNACK | STANDS | R_well has a₁ < a₋ and a₂ < r₀, so n₁₂ ≤ (2a₋+r₀)√β/d, which gives 35(a₋+r₀). M is fixed, so its term is β^{1/4}. HARNACK's "M² = O(log 1/η)" is wrong (M² ~ 1/η) but harmless, as FULL says. |
| (4) chain + factor c* | STANDS | See (a) and (f) in §4. 1D: E_LB → 2Ψ(π/2) + o(1) (5.196 at β = 4096, η = 0.25, still falling). The monotone reading gives 9.6 ≈ 2c*. |
| (5) ∫_S f² ≥ ½ | STANDS | M4 needs (B) for f, which needs λ_eo ≥ e^{−η/4} (from L4) and Lemma F. With K = 1 the bound is 1 − (1−λ_eo)/0.632 − o(1) → 1. 1D analogue: ∫_S f² = 0.994–1.000 at η = 0.25. |
| (6) m ≥ Δ/λ ≥ Δ | STANDS | log x ≥ 1 − 1/x and λ ≤ 1. |
| (7) parameters and order | STANDS | Every o(1) is at fixed (η, a₋, r₀, ℓ, θ₀, K, M, ρ_B). The η-dependent room in the tilt is e^{η/2}−1, and Δ₁ ≤ η/4 is needed only for β ≥ β₀(η). There is no circularity: μ is a prefactor, and the c₁ condition does not involve μ. |
| Lemma L4 | STANDS | Checked line by line. b₀₀ is a valid trial for λ_ee because the global top is in the ee sector (Perron). u is σ₁-odd, σ₂-even and gauge invariant. Same-U₁ cross terms are ≥ 0. There are 8 ordered opposite-U₁ terms, each ≤ v⁴k(π−2r)k_sup. V ≤ 2βr⁴ on B_r². The statement is o(1) only, with no usable β₀. |
| chain x → σx | STANDS | e^{(a−π)n̂} = −U₁⁰, and step 3 = σ₁∘reverse(step 1) ends at σ₁x. Valley balls have q ≤ ρ_B²/β and a₂ ≤ ρ_B/√β < r₀, so they lie in supp φ with G−c₁ ≥ e^{−1.5ρ_B²}/2 and E−c₂ ≥ ½. min(Ψ(a₁),Ψ(π−a₁)) ≤ Ψ(π/2) for every a₁. Corners at U₂ = −1 come by σ₂: φ = 0 there, but g(z) = g(σ₂z). |

### 1.1 Specific questions of the brief

- **(a) c* vs 2c*.**
  - φ is defined on the whole tube as max(φ_L, φ_R), which is a tent with its minimum at π/2. It is not cut at π/2.
  - Lemma C is applied once on Ω = tube ∩ {a₁ ∈ [a₋, π−a₋]}, and the middle is inside Ω.
  - The bound on g in the second half comes from φ_R = φ_L∘σ₁ (and σ₁-commutation of T), not from a separate comparison.
  - The chain crosses π/2 inside Ω, where g ≥ φ ≥ c μ e^{−√βΨ(π/2)}.
  - This is identical to PATHS §3(S) (Ψ = min(Ψ₀(y), Ψ₀(π−y))) and TUNNEL_LOWER Lemma S ("reflected branch").
- **(b) Lemma C.** The roles are as proved.
  - The proof is (λ − T_ΩΩ)w_Ω = (Tφ − λφ)_Ω + T_{ΩΩᶜ}w_{Ωᶜ} ≥ 0, plus a positive Neumann series. Both are valid for a nonlocal positive kernel.
  - "a.e. → everywhere" uses continuity of g and φ.
- **(f) Arithmetic.**
  - −log Δ ≤ 2 sup(−log g) + O(log β) − log(2∫_S f²) is Corollary B with polynomial factors.
  - sup ≤ √βΨ(π/2) + (−log μ) + O(1), and 2Ψ(π/2) ≤ c*(η) ≤ c* + π√(2η).
  - The total is c* + π√(2η) + 70(a₋+r₀), which tends to c*.
  - My Q7 checks this bookkeeping exactly in 1D (8/8).

### 1.2 1D numbers (assembly1d.py, own code; −log/√β)

| η | β | E_true | E_LB (assembled) | 2Ψ(π/2) | monotone reading | min Tφ/(λφ) on Ω |
|---|---|---|---|---|---|---|
| 0.25 | 256 | 4.1780 | 5.660 | 4.808 | 9.55 | 1.025 |
| 0.25 | 1024 | 4.3324 | 5.361 | 4.808 | 9.58 | 1.193 |
| 0.25 | 4096 | 4.4307 | 5.196 | 4.808 | 9.61 | 1.279 |
| 0.1 | 256 | 4.1780 | 5.515 | 4.756 | 9.44 | **0.959 (Q4 fail)** |
| 0.1 | 1024 | 4.3324 | 5.189 | 4.756 | 9.46 | 1.001 |
| 0.1 | 4096 | 4.4307 | 5.012 | 4.756 | 9.48 | 1.071 |

- E_LB ≥ E_true in every case (Q6, 8/8). In other words, the assembled lower bound on Δ is below the true Δ.
- The gap E_LB − E_true shrinks: 1.48 → 0.77 at η = 0.25, and 1.34 → 0.58 at η = 0.1.
- E_LB − 2Ψ(π/2) − 2(−log μ)/√β equals the polynomial term exactly. It is 0.79, 0.45, 0.26, which tends to 0.

## 2. Hypotheses each statement uses (where stated)

- **Lemma C:** φ ≥ 0, φ, g ∈ L², ‖T_ΩΩ‖ < λ, Tφ ≥ λφ on Ω, φ ≤ g on Ωᶜ (TUNNEL_LOWER §1; PATHS §3(C)).
- **S4-alg:** (E1)–(E3) uniform on supp φ_L ∩ {a₁ ∈ [a₋, π/2]}, D ≤ η/4, and c₁ ≤ G_min(e^{η/2}−1)e^{−C}/4 (TUNNEL_LOWER2 §2; FULL §2).
- **(E1)/(E3):** (H1) Ψ C², (H2) Θ, and (H3) x ∈ K (E13 l.13). The constants depend on (η', r₀, θ₀, ℓ, M, H_Ψ, Λ) (E13 l.69).
- **(E2):** Lemma K with global C² (TUNNEL_THEOREM §3).
- **‖T_ΩΩ‖ bound:** Lemma F η-form, uniform in s ∈ [η/2, 1] (LEMMA_F l.1, §3).
- **H4:** Tg = λg, λ ≤ 1, g > 0 continuous, σ₁ and σ₂ symmetries, x ∈ D_M, ρ ≤ ½, and m_B (HARNACK §0, §3).
- **M4:** (B) for u, which needs λ_u ≥ e^{−η/4} and Lemma F (TUNNEL_LOWER2 §3).
- **L4:** T = e^{−V/2}K₁K₂e^{−V/2} and the kernel k = e^{β cos θ}/Z (FULL §5).
- **P'c / Corollary B:** (H1)–(H4) of PATHS §0, a measurable path kernel, and uniform balls of volume ≥ v (PATHS §1, §2.1).
- **Final step:** L3, c*(η) ≤ c* + π√(2η) (TUNNEL_LOWER, Lean, not compiled by me).

## 3. Failed predicates (all kept)

- **Q4, run K2** (η = 0.25, β = 16 and 36). min Tφ/(λφ) = 0.914 and 0.919, at d ≈ a₋, which is the χ ramp where Ψ'' is large.
  - Cause: my own expectation. This is a finite-β Taylor error O(H/√β) and not a target defect; the statement is asymptotic.
  - Q5 was therefore not asserted there.
- **Q4, run K4** (η = 0.1, β = 256). The minimum is 0.959 at d = 0.104 ≈ a₋. Same cause. It is met at β = 1024 and 4096.
- **Child-side:** the grandchild's own P2 (two grids at β = 16 agree to 1e−6) failed with difference 6.1e−4. This was its own over-tight tolerance (O(h²) error from the kink of ε at the wells), not a defect.

Tolerances and their sources:
- Q1: 50·eps·λ/Δ, from cancellation in the eigenvalue subtraction.
- Q5: 1e−9, from the elementwise relative error of products of positive matrices.
- Q7: 1e−6 relative, from float rounding.
- Q8: 2c* − 1.5, my choice of a margin that separates c*(η) + o(1) from 2c*.

Measured only: E_true, E_LB, the gap, (log g(0) − log g(π/2))/√β (= 2.064, 2.152, 2.207, tending to c*/2 from below), the monotone-reading exponent, and min Tφ/(λφ).

## 4. What I did not check

- The insides of E13 §2–§4, LEMMA_F §2, Lemma K, (B) and TUNNEL_THEOREM §4, and S4-alg's absorption algebra beyond FULL's restatement. The brief said not to redo the parts.
- No Lean file was compiled.
- The SU(2)² quantities themselves (no 4-D eigenfunction was computed). The 1D model tests the assembly mechanism only: tent, Lemma C, μ inside φ, Corollary B, and the exponent. It does not test the HARNACK constant 35(a₋+r₀).
- In 1D, μ was taken as min_{R_well} g·e^{√βΨ} (the best admissible value), not HARNACK's μ.
- The pre-existing asm_check.py and onedflux.py (worker r1-asm) were not run and are not used as evidence.

## 5. Delegated questions and outcomes

- **Child T165** (admitted parent T164; released at graph event 334). Run as child-run1, register check K1, 149 s, exit 0.
  - Question: the 1D continuum model on a reduced positive grid with the flux identity. It was asked for −log Δ/√β and (log g(0) − log g(π/2))/√β at β = 64–4096, and to decide c* vs 2c*.
  - Control: ∫₀¹ x²eˣ dx = e − 2. It answered 0.718282. I graded it CORRECT before reading anything else.
  - Outcome:
    - −log Δ/√β = 3.9376, 4.1780, 4.3324, 4.4307;
    - the half ratio = 1.926, 2.064, 2.152, 2.207;
    - its verdict was STANDS (c*, not 2c*).
  - My checks:
    - rerun K5 gives results.json identical in every number;
    - my independent assembly1d.py agrees to about 1e−4 (4.1780, 4.3324, 4.4307; half ratio 2.0643, 2.1515, 2.2066).
- **Grandchild T166** (admitted by the child, parent T165, depth 3; graph seq 333; released).
  - Question: an independent value of c*, and −log Δ/√β at β = 16 by direct eigenvalue subtraction.
  - Control: 0.718282, correct.
  - Outcome: c* = 4.605413195, and β = 16 gives 3.5765. Its P2 failed (see §3).
  - My rerun K6: the N = 256 line is identical. The N = 512 value of Δ differs at relative 9e−10, which is cancellation noise of plain-double subtraction, so it is consistent but not bit-identical.

## 6. Exact commands to rerun

```
cd /home/user/z4-workers/s1-chalA
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos; G=/home/user/z4-work/graph/attempt.jsonl
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control
$P init pcp --principal principal --principal-name "Kirtus Justus"     # fresh directory only
$R task-admit $G --by principal --label s1-chalA-child --parent T164   # gave T165
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
# result files open with mode "x": use new names on rerun
$P check --ws pcp --name asm1d-small-eta025 --expect-exit 0 -- python3 assembly1d.py res_small_eta025.jsonl 0.25 16 36
$P check --ws pcp --name asm1d-main-eta0.25 --expect-exit 0 -- python3 assembly1d.py res_main_eta0.25.jsonl 0.25 256 1024 4096
$P check --ws pcp --name asm1d-main-eta0.1 --expect-exit 0 -- python3 assembly1d.py res_main_eta0.1.jsonl 0.1 256 1024 4096
mkdir -p rerun_child && cp child/run_main.py child/check_preds.py rerun_child/
$P check --ws pcp --name rerun-child-main --cwd rerun_child --expect-exit 0 -- python3 run_main.py
mkdir -p rerun_grandchild && cp child/grandchild/run.py rerun_grandchild/
$P check --ws pcp --name rerun-grandchild --cwd rerun_grandchild --expect-exit 0 -- python3 run.py
$R task-release $G --by principal --id T165
$P verify --ws pcp
$R verify pcp/register.jsonl
```

PCP OS, last lines:
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

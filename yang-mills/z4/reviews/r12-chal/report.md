# r12-chal — challenger report on THEOREMS_B (flowed free lattice Maxwell)

Control: control.txt = 0.272341 (−ln tanh 1). Lean was ready (/home/user/z4-lean/READY exists), but I did not use it, so there is no Lean claim. Program: chal.py (predicates P1–P16 are in its docstring), output results_run2.json. Rechecks: p11c.py → results_p11c.txt. Step log: notes.md.

My test function (non-symmetric, f > 0) is f(y) = F(y/l) with
F(u) = exp(0.6cos(2πu1+0.3) + 0.4 sin2πu2·cos(2πu3−0.7) + 0.25 sin2π(u1+2u3) + 0.2cos(4πu2+1.1)).
For it, b0/l = 0.265.

## Verdict table

Counts are given as met, failed, measured only.

| Item | Verdict | Evidence |
|---|---|---|
| A1 momentum representation | STANDS | Brute-force position sum, brute-force momentum double sum and FFT agree, max rel 1.8e-15, at N = 6, 7, l = 0.7, 1, 2, t = 0, 0.1. 12, 0, 0. |
| H1 normalization k̂/2 (by hand) | STANDS | Mass b/g², ω = k̂, ⟨\|A_pol\|²⟩ = g²/(2bk̂), Σ_pol (k̂×ε)₃² = k̂₁²+k̂₂², which gives P33 k̂/2. |
| A2 Parseval constant l³b³Σf², Schur bijection | STANDS | P2 90, 0, 0. Schur intermediate P4 90, 0, 0. k′ ↦ k+k′ mod BZ is a bijection, and fhat_b is 2π/b-periodic. |
| A2 a² ≤ (\|k\|²/4)e^{−16s\|k\|²/π²} | STANDS | Checked for all k in the BZ, per case: P3 90, 0, 0. |
| A2 V formula, factors, dimension | STANDS | C ~ L⁻², V ~ L⁻³·L³·L⁻² ✓. C ≤ V in 90/90 cases with Φ = l³ sup f², and in 90/90 with Φ_alias (90 cases qualify for b ≤ b0). Minimum V/C = 38.9. |
| A3 P33 ≥ (4/π²)(k1²+k2²)/\|k\|², direction of the exponentials | STANDS | P6 90, 0, 0. Because k̂ ≤ \|k\|, e^{−2tk̂−4sk̂²} ≥ e^{−2t\|k\|−4s\|k\|²}, which is the right direction for a lower bound. |
| A3 v1 ≤ C | STANDS | 90, 0, 0 (90 qualify). Max v/C = 0.225. |
| A3 v2 ≤ C, with N ≥ 2M+1 | STANDS | 68, 0, 0 (68 of 90 cases satisfy N ≥ 2M+1). |
| A3 boundary N = 2M+1 (odd N) | STANDS | P9 36, 0, 0. |
| A3 even N with M = N/2 (edge mode double-counted; hypothesis violated) | measured only | The bound still held in 54/54 cases. The condition N ≥ 2M+1 is the correct one for distinct modes. |
| A4 θ_j bounds, j = 0..4, c ∈ [1e-3, 50] | STANDS | 1000, 0, 0. Worst θ/bound = 0.982 (j = 0). The m = 0 term is handled: the two-sided sum is ≤ ∫ + 2·max for j ≥ 1 and ≤ 1 + √(π/c) for j = 0. U2, U4, U6 are exact product identities. P10U 102, 0, 0. The child agrees independently. |
| A5 step 1 \|k̂_i − k_i\| ≤ b²\|k_i\|³/24 | STANDS | 50-digit recheck: 0 violations in 1e5 samples, max ratio 0.999999999998, so the constant is sharp. The float64 run failed; see below. |
| A5 step 2 gradient bound | STANDS (loose) | P12 10000, 0, 0. I computed \|∇g\| = sqrt(sin⁴θ/4 + sin²θcos²θ) ≤ 1/√3 (measured max 0.57735). The claimed 3/2 is valid but loose. The segment lies inside [(2/π)\|k\|, \|k\|] componentwise. |
| A5 step 4: max(\|k\|,\|k′\|) ≥ π/(2b); tail factor | STANDS | ā = ā*·e^{−4s\|k\|²/π²} ≤ ā*·e^{−s/b²} at \|k\| ≥ π/(2b). The continuum coefficient 2∫f² is more than needed (∫f² suffices). |
| A5 final B2 inequality | STANDS (useless constant) | P13 18, 0, 0, including b just below b0 (N = 4, b/b0 = 0.94). The bound exceeds the true error by 7e4 to 1e15. |
| A6 B3 M1, M2 bounds | STANDS | P14 8, 0, 0. P14A 24, 0, 0. Finite-difference −C′(0) matches M1 to 4 to 5 digits. With Φ = b³Σf², the bound/true ratio is 1.04 to 1.27. |
| B3 text "with v1 alone … s^−3 and s^−4" | DEFECT (minor, text) | The M2 bound scales as √(A0A4) + A2 ~ s^{−7/2}, and v1 ~ s⁰. So M2/M0 ≲ s^{−7/2}, not s^{−4}. The bound itself is unaffected. |
| A7 "V does not depend on t" | STANDS | e^{−2tk̂} ≤ 1 is dropped. |
| A7 "independent of l" (leading V) | STANDS with qualification | True only for the choice Φ = ∫f² + alias term with f fixed. With Φ = l³ sup f² the leading term grows like l³. Through b0 = min(l/3, …), Φ_alias also depends on l. |
| A7 loss factor ≈ 60 | STANDS (asymptotic only) | Reproduced 17.93·Φ/∫f² = 58.99 (Φ/∫f² = 3.290) for the author's f. The actual V/C at s = 0.002, 0.005, 0.02 is 118, 172, 620. |
| A8 C_s(0) ~ √π/(640π²)∫f²·s^{−5/2} | STANDS | Derived by hand: ∫D² = √π/(1280π²)s^{−5/2}. Ratio at s = 5e-4: 0.9895 (l = 1) and 0.9801 (l = 0.7), monotone toward 1. P15 2, 0, 0. |
| Author's numbers | STANDS | The following all reproduce: ∫f = 1.4221287, b0 = 0.25366, V(0.002) = 6.6297e5, C_cont(0.002) = 5633.33, v1 and v2 at all three s (19.91/52.90, 12.40/5.441, 1.160/0.1279), V(0.005) = 9.158e4, V(0.02) = 5825. P16 1, 0, 0. |

Totals: 23 items. STANDS 21, DEFECT 1, measured only 1, NOT CHECKED 0 among the listed items. Some aspects are unchecked; see "What I did not check".

## Hypotheses each statement uses, and where they are stated

- **Momentum representation and B1–B3:**
  - H1 is the normalization of D with the flow factor e^{−2sk̂²}. It comes from SETTING and the brief, and THEOREMS_B marks it "not rederived". I rederived it by hand and it agrees.
  - H2 is Wick.
  - H3: f real, C⁴, periodic, ∫f ≠ 0.
  - H4: N ≥ 3.
  - HΩ = 0.
  - s > 0.
  - BZ convention −π < k_i b ≤ π. This is stated in THEOREMS_B §2 Notation and in the review note of PROOF_FREE_BOUNDS.
- **B1 lower bound:** b ≤ b0 (PROOF_FREE_BOUNDS 4c).
- **v2:** additionally N ≥ 2M+1 (THEOREMS_B hypothesis list).
- **V with Φ_alias:** b ≤ b0. V with Φ = l³ sup f² needs neither.
- **U_q:** unimodality of x^{2j}e^{−cx²} (stated).
- **B2:** additionally the Jordan bound (3a) and the aliasing lemma (2, 2a). It uses S4 ≤ 16.5791, which comes from bounds.py and was not rederived by me.
- **Implicit, not stated:** SETTING writes e^{ik·(x−y)} with x an integer site. The physical position b(x−y) is meant, as in PROOF_FREE_BOUNDS H2. This is a notation slip, not a gap.

## Failed predicates

1. **P11, run1 and run2 (float64).**
   - In run1 the failure was my own defect: I sampled k_i·b in (−2π, 2π].
   - In run2 the failure was my tolerance: at k·b < 2e-4, round-off in y − sin y dominates. The worst ratio was 1.0000059 at k·b = 1.1e-5.
   - This is not a defect of the target. The 50-digit recheck (p11c) found 0 violations.
2. **p11b (K4) exited 1:** mpmath is not installed. This is my own defect, replaced by p11c.
3. **run1 (K2) crashed** with an index error in my continuum-sum code (C_cont when the grid was smaller than the f̃ array). My own defect. Fixed before run2, with the predicates unchanged.
4. **The child (informational):** "constant 1 suffices" in T2 fails for j ≥ 8. This was the child's own expectation. T2 claims the constant 2, so it is not a defect.

## What I did not check

- Lean: nothing was run. The author's R11Flow.lean was not present.
- The S4 bounds 16.3597 ≤ S4 ≤ 16.5791.
- The aliasing lemma proof itself (it is used, not re-proved).
- The spectral identification text.
- The measured v2·s^{5/2} constants.
- The B3 measured moments at N = 128.
- Rigorous interval arithmetic. All checks are in double precision except p11c.
- "For all c": the θ bounds are tested on a grid. The proof argument (integral + max for a unimodal integrand) I checked by hand.
- The author's f was used only at l = 1.
- B2 at s = 0.002, l = 2 with N = 32: skipped for memory and time.

## Delegated questions and outcomes

- **Child (sonnet, child/, register child/pcp; run as check K1, exit 0, 94 s).**
  - Question: A4 alone (T1, T2, T3).
  - Control: Σ e^{−πm²} = 1.086435. The child's answer was 1.086435, graded CORRECT before I read anything else.
  - Result: T1, T2 and T3 STAND (T1 241/241, T2 964/964, T3 identities exact), worst ratio 0.982.
  - I reran its main_test.py in child_rerun/ (K6): identical counts. Its worst ratios equal my independent P10 values to 15 digits.
  - Shortcoming: the child's main_test.py writes no mode-"x" result file (it only prints), so rule 3 was not fully followed.
- **Grandchild (the child's Agent sub-agent, child/grandchild/).**
  - Question: recompute θ2(0.01), θ1(0.3) and θ0(0.01) by direct sum and by Poisson summation.
  - Control: 1.086435.
  - Values: 132934.038818, 5.39340531265, 17.7245385091.
  - I recomputed θ1(0.3) = 5.393405312651 and θ2(0.01) = 132934.0388179 myself. Both match.

## PCP OS

- `$P verify --ws pcp` → `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl` → `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- Checks in the register:
  - K1 child-run1
  - K2 chal-run1 (exit 1, crash)
  - K3 chal-run2
  - K4 p11b (exit 1)
  - K5 p11c
  - K6 child-rerun-main

## Rerun commands

```
cd /home/user/z4-workers/r12-chal
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
$P check --ws pcp --name chal-run3 --expect-exit 0 -- taskset -c 0 python3 chal.py results_run3.json
$P check --ws pcp --name p11c-2 --expect-exit 0 -- python3 p11c.py results_p11c_2.txt
mkdir child_rerun2 && cp child/main_test.py child_rerun2/
$P check --ws pcp --name child-rerun2 --cwd child_rerun2 --expect-exit 0 -- python3 main_test.py
$P check --ws pcp --name child-run2 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"   # needs a fresh child dir (mode-x files)
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

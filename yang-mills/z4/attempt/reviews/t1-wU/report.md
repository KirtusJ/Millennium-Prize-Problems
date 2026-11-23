# Report t1-wU (task T167): first half of the note, `tun_upper.tex`

Worker t1-wU, writer of the first half. I share a model family with the director, the authors of the parts and the challengers, so my agreement is not independent review. Control: `control.txt` = 0.272341. Lean READY exists, but I compiled no Lean and claim no Lean result. No network was used.

Deliverables:
- `tun_upper.tex`: Sections 1 to 4, 13 pages.
- `wrap.tex`: the compile wrapper.
- `wrap.pdf`
- `consts.py` with its result `consts_run2.json`
- `notes.md`
- `child/`

## 1. Verdict table

Each item is a statement in `tun_upper.tex`. The verdict says whether it STANDS as written after my writing and the child's fidelity check.

| item | verdict | one line of evidence |
|---|---|---|
| Thm tu:U-thm (statement, lim = c*) | NOT CHECKED (this half proves only liminf) | The limsup half is in the second half. c* = 4.6054131945 (consts P1). |
| Lemma tu:U-kernel (kernel, Z, multipliers) | STANDS | Z = 2I₁/β by integration by parts. Multiplier I_{n+1}/I₁ written for this note and confirmed by consts P4 and P5 (rel. ≤ 2.4e-11). Child: correct. |
| Lemma tu:U-K (Lemma K, plus radial form) | STANDS | Constants match TUNNEL_THEOREM §3. The radial form was added (challenger's missing line). Child C9: 150/150 qualifying cases hold. |
| Lemma tu:U-R (fibre reduction) | STANDS after fix | Child nit applied: F_{U₁} = C_h F_a C_h⁻¹, not C_h⁻¹F_aC_h. Part (4) is used only numerically. |
| Lemma tu:U-F (Lemma F, η-form) | STANDS | Proof via Thm tu:U-F-master and Cor tu:U-F-cor, as in LEMMA_F. |
| Lemma tu:U-Frad, tu:U-barta, tu:U-fixed, tu:U-bessel, tu:U-amgm, tu:U-outer | STANDS | Each was re-derived while writing. Consts P3, P7, P9 and child C5–C7 met. |
| Lemma tu:U-I1 | DEFECT (mine, fixed) | I wrote "D(1) > 0.039", which is false: D(1) = 0.03893. The child found it, and it now reads D(1) = 0.0389… > 0. No step used the number. |
| Thm tu:U-F-master | STANDS | M_in and M_out match LEMMA_F Thm 1 term by term (child). Deficits 8.73–14.23 nats and the 2.24e13 threshold were reproduced by the child. |
| Cor tu:U-F-cor | STANDS (header correction applied) | It says log max(M_in, A M_out) → 0⁺, with M_in → 1 and A·M_out → 0. |
| Lemma tu:U-weight | STANDS, conditional on the existence of (W1), (W3) | It uses c^ρ_η = 2f(π/2), not c*_η. See §3, DEFECT of the parts. |
| Lemma tu:U-schur | STANDS | Taylor line added. A "β large" hypothesis was added after the child's nit. |
| Lemma tu:U-A (inequality (A)) | STANDS | μh = B*WBh, then the Schur step, then Lemma R(2). No positivity of u is used. |
| Prop tu:U-B ((B), any eigenfunction) | STANDS given L4 | Explicit C(η) = 1 + (e^{η/2} − e^{−η/4})/(e^{−η/4} − e^{−η/2}). Part (2), the exchanged links, is from TUNNEL_LOWER2 §3. |
| Lemma tu:U-flux | STANDS (prefactor 4) | The parts had 2. The grandchild found the ratio 4.000000000000 in 6/6 cases, and my rerun K5 gave the same. |
| Thm tu:U-main (liminf ≥ c*) | STANDS given L4 and (W1)/(W3) | Chain: Δ ≤ 4C(η)C_L e^{−√β(1−δ)(c^ρ_η − 2Lτ)}, and m ≤ 2Δ. |

**Counts.**
- Verdicts: STANDS 13 (counting the grouped row as one), DEFECT 1 (fixed), NOT CHECKED 1.
- Predicates of my program consts.py: met 9, failed 0, measured only 0.
  - Run 1 exited 1 because of my own defect, described in §3.
- Predicates of the child's check.py, as rerun by me: met 12, failed 1, measured only 0.
  - The failure is C3, "D(1) > 0.039". It is a defect of the target, made by me as writer, and is now fixed.

## 2. Hypotheses each statement uses, and where they are stated

- **tu:U-kernel:** β > 0 (stated in the lemma).
- **tu:U-K:** β > 1, p ∈ ℝ³, H ≥ 0, 0 < η ≤ 1, β' > 0 (stated in the lemma). The radial form uses H = 0.
- **tu:U-R:** β > 0. Part (4) also needs s > 0.
- **tu:U-F:** η > 0 and β ≥ β₀(η).
- **tu:U-F-master:** β > 1, s ∈ (0,1], 0 < τ < 1/5, 0 < δ ≤ 1.
- **tu:U-barta:** a symmetric kernel ≥ 0, and ψ bounded above and below.
- **tu:U-I1:** z > 0, and β > 1 for D > 0.
- **tu:U-outer:** r ∈ [0,1] and c ≥ 0.
- **tu:U-weight:** η ∈ (0, 1/2], δ, τ ∈ (0,1), and the existence of ρ_η (W1) and f̃ (W3).
- **tu:U-schur:** the weight of §4.2, and β large enough that β' > 0.
- **tu:U-A:** u real, with Tu = μu.
- **tu:U-B:** η ∈ (0, 1/2], β ≥ β₁(η, δ, τ), u a real eigenfunction, μ ≥ e^{−η/4}.
- **tu:U-flux:** none beyond the setting.
- **tu:U-main:** all of the above, plus Lemma tu:L-L4 from the second half (λ_ee, λ_eo ≥ e^{−η/4} for large β).

## 3. Corrections applied, defects found, failed predicates

**Corrections applied, with their source:**
1. Flux prefactor 4, not 2 (CHAL_conditional item 10). Lemma tu:U-flux carries a remark saying so.
2. The missing Taylor line in the Schur step: cosh(√β(p·X + R)) ≤ cosh(√β p·X)·e^{√βHθ²/2} (CHAL_conditional item 7). It is in Lemma tu:U-schur.
3. The radial Lemma K, E_k e^{√βLθ} = O(1) (CHAL_conditional hypotheses list, "missing line"). It is in Lemma tu:U-K and Remark tu:U-K-rem.
4. The header of Lemma F: "log max(M_in, A·M_out) → 0", not "M_in, M_out → 0" (CHAL_lemmaF). It is in Cor tu:U-F-cor(b).
5. The deficit "8.6 to 14 nats" at β ≤ 4096 with τ = β^{−1/3} (CHAL_lemmaF clarification). The parts' "6.5" came from τ = 0.15.
6. The Barta hypothesis that ψ is bounded above and below, made explicit (CHAL_lemmaF I4).
7. **C5:** λ_ee, λ_eo ≥ e^{−η/4} are taken from Lemma tu:L-L4, not from the bump sketches. This also covers CHAL_parts H7: an indicator bump gives O(β^{−1/6}).
8. The (B) form for any eigenfunction, including the exchanged-link version (TUNNEL_LOWER2 §3).
9. Changes C1–C4, C6 and C7 concern second-half objects (E13 tube, Ψ, Θ, chain, φ). They do not enter this half.
   - The analogue of C2 and C7 (a C² weight, 0 ≤ Φ' ≤ √(2(ε−η))) is built into (W1)–(W3).

**Errors I found in the parts while writing (DEFECT of the target, minor):**
- TUNNEL_THEOREM §5 states Φ(x) + Φ(y) ≥ (1−δ)(c*_η − 2Lτ − L d₁) with c*_η = ∫√(2(ε−η)₊).
  - Because f is built from ρ_η ≤ (ε−η)₊, 2f(π/2) ≤ c*_η, so the stated inequality does not follow.
  - It holds with c^ρ_η = 2f(π/2). I wrote that version and proved |c* − c^ρ_η| ≤ π√(6η) myself (the parts say "O(√η)").
  - The child confirmed this, and noted that CHAL_conditional item 11 had glossed it.
  - The limit is unaffected.

**Failed predicates (kept):**
- consts-run1 (K1), exit 1. **My own defect:** `json.dumps` of numpy bools in the final print, after the result file had been written. The file shows all 9 predicates met. Run 2 (K2) exited 0.
- Child C3, "D(1) > 0.039", failed. **Defect of the target, written by me.** Now fixed.

**Measured, minor:** the child reports c* = 4.605413245. Mine is 4.6054131945, and the CHAL_assembly grandchild has 4.605413195. The child's value is within its own tolerance of 5e-7. Its quadrature is coarser near the kinks at the endpoints.

## 4. Steps the writer could not complete from the parts

1. **Existence of ρ_η (W1).** It needs √ρ_η smooth, ρ_η ≤ (ε−η)₊, and ρ_η ≥ ε − 2η for ε ≥ 3η. TUNNEL_THEOREM §4 asserts it and does not construct it, and CHAL_conditional lists it as not checked. The text says "not constructed here".
2. **Existence of the C² kink smoothing f̃ (W3).** It needs symmetry, f̃ = f outside a τ-window, and |f̃'| ≤ |f'|. This is asserted in the parts, not constructed, and not constructed here.
   - Given (W3), I proved f̃ ≥ f − Lτ myself. The parts use it without comment.
3. **Lemma tu:L-L4** belongs to the second half and is cited, not checked by me.
4. **The 4.599 fit.** The value c = 4.599 comes from the brief only. style/sec_smallbox.tex says "c ≈ 4.60", and no part contains 4.599. The text states it as reported in the companion paper and not recomputed. Its relative distance from c* is 0.14%; after the child's nit the text says "about 0.15%".
5. **The "β ~ 1e8" threshold** in Section 1 item 3 refers to E13's Δ₁ = 0.167 at 2.7e8, which is second-half material. I did not check it.

## 5. What I did not check

- Lean files (not compiled).
- The second half, including L4.
- Lemma R(4) numerics (TUNNEL_THEOREM §1(iii)), quoted as measured.
- The Barta-ratio numerics of LEMMA_F §4, quoted as measured by the author and the challenger.
- The rate claim of LEMMA_F §5, stated as not proved.
- §6, the valley picture. It is mentioned only as not used.

## 6. Compile result

- The brief's wrapper (`\documentclass{amsart}\input{style/preamble}…`) fails with "Two \documentclass", because style/preamble.tex itself contains `\documentclass[11pt]{amsart}`. `wrap.tex` therefore omits the `\documentclass` line.
- With that wrapper, pdflatex (TeX Live 2023) runs with no errors and writes 13 pages.
- Warnings:
  - The only undefined reference is `tu:L-L4`, 6 times. This is expected: it is in the second half.
  - There are 8 overfull hboxes, between 9 pt and 83 pt, at display equations in Lemma K, Lemma kernel(3), Remark K-rem, Theorem F-master and Theorem main. They are cosmetic.
- The file is ASCII only (checked with grep).
- Labels the second half may cite: tu:U-kernel, tu:U-K, tu:U-R, tu:U-F, tu:U-B, tu:U-main. Also tu:U-thm (main statement), tu:U-flux, tu:U-weight, tu:U-F-master, tu:U-F-cor and tu:U-schur.
- Note for the second half: f is defined in the gauge-invariant sector. This half does not use gauge invariance of f (remark in Section 1).

## 7. Delegated questions and outcomes

**Child T170** (admitted under T167 at event 339, released at event 344). Run as check K3, `child-run1`, exit 0, 296 s.
- **Question:** a fidelity check of every lemma, statement and constant in `tun_upper.tex` against the parts, with a verdict per item of MATCHES, CHANGED or WRONG.
- **Control:** 2 asinh 1 = 1.762747. It answered 1.762747, and **I graded it CORRECT before reading anything else.**
- **Outcome:** MATCHES 10, CHANGED 9 (each justified by a listed correction or a flagged writer addition), WRONG 1.
  - The WRONG item was "D(1) > 0.039". I fixed it.
  - Three nits, all applied:
    - C_h direction;
    - ω needs "β large";
    - 0.1% should be 0.14%.
  - It confirmed the c*_η → c^ρ_η change as correct.
- **My checks:** I reread findings.md and report.md. I reran its check.py in child_rerun/ (K4, expected exit 1): the result JSON is identical to the child's in every entry.

**Grandchild T172** (admitted by the child under T170, released at event 343, per the child's report).
- **Question:** is the prefactor of the flux identity 4? Tested on 3×3 symmetric positive matrices: 3 matrices, 2 splits each.
- **Control:** the top eigenvalue of [[2,1],[1,2]]. It answered 3.000000, which is correct.
- **Outcome:** the ratio is 4.0000000000 in 6/6 cases.
- **My check:** I reran prog.py in gc_rerun2/ (K5, exit 0). The ratio is 3.999999999999998, so 4.

## 8. PCP OS record

Register `pcp/`, with checks K1–K5:

| check | name | exit | expected |
|---|---|---|---|
| K1 | consts-run1 | 1 | 0 |
| K2 | consts-run2 | 0 | 0 |
| K3 | child-run1 | 0 | 0 |
| K4 | child-check-rerun | 1 | 1 |
| K5 | gc-prog-rerun | 0 | 0 |

- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## 9. Exact commands to rerun

```
cd /home/user/z4-workers/t1-wU
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos; G=/home/user/z4-work/graph/attempt.jsonl
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"          # control 0.272341
$P init pcp --principal principal --principal-name "Kirtus Justus"       # fresh directory only
$P check --ws pcp --name consts-run3 --expect-exit 0 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 consts.py consts_run3.json   # new file name each run (mode "x")
$R task-admit $G --by principal --label t1-wU-child --parent T167        # gave T170
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T170
mkdir -p child_rerun2 && cp child/check.py child_rerun2/
$P check --ws pcp --name child-check-rerun2 --cwd child_rerun2 --expect-exit 1 --timeout 300 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 check.py rerun2
mkdir -p gc_rerun3 && cp child/grandchild/prog.py gc_rerun3/
$P check --ws pcp --name gc-prog-rerun2 --cwd gc_rerun3 --expect-exit 0 --timeout 120 -- python3 prog.py
pdflatex -interaction=nonstopmode wrap.tex; pdflatex -interaction=nonstopmode wrap.tex
$P verify --ws pcp
$R verify pcp/register.jsonl
```

Note: the child's check.py tests the old claim "D(1) > 0.039", so it still exits 1 on purpose. The fixed text no longer makes that claim.

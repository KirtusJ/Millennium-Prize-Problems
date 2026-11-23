# report.md — worker u1-gapA (task T173), brief u1-gapA

Control: `control.txt` = 0.272341, which is −ln(tanh 1). Lean was READY (/home/user/z4-lean/READY exists).

## 1. Verdict table

Verdict counts: STANDS 9, DEFECT 0, NOT CHECKED 0.

| item | verdict | one line of evidence |
|---|---|---|
| Gap 1 (W1): ρ_η exists with the required properties | STANDS (PROVED, constructed) | Lemma tu:U-W13(1) in tun_upper_patched.tex. w1w3.py P1–P3 and P5 met for η ∈ {.5, .2, .05, .01}. Child A1–A4 met. |
| W1 as stated asks for "√ρ smooth" | STANDS, weakened to C¹ (enough) | Only Φ ∈ C² and H < ∞ are used downstream. A C^∞ step function gives the stronger form with other constants. |
| Gap 2 (W3): C² f̃, symmetric, equal to f off the window, \|f̃'\| ≤ \|f'\| | STANDS (PROVED, constructed) | Lemma tu:U-W13(2). w1w3.py P6–P11 met (12 cases). Child B1–B3 met. |
| Constants for tu:U-weight(2) and the Schur step | STANDS | H ≤ (1−δ)·max(6/√η + 3L/τ, L/sinh(3η/4)). Measured max \|f̃''\|/bound ≤ 0.90 and cot term ≤ 0.23. |
| Gap 3: the Δh bound as stated in tu:L-taylor | STANDS (derivation supplied; the bound was correct) | σ₋ bounds S'². Lean `delta_h`. gap_dh.py H2: 183,571 qualifying samples, 0 failed, worst ratio 0.96. Child C1: 1,656,400 met. |
| Gap 3: explicit form Δh ≤ 5r_b/S² for r_b ≤ S/8 | STANDS (PROVED) | gap_dh.py H3: 171,468 qualifying samples, 0 failed, worst ratio 0.33. |
| Gap 3, propagated: explicit Err bound in Prop tu:L-E13 | STANDS (PROVED) | err_const.py E1–E6: 10⁶ samples, 0 failed, worst ratio 0.86. |
| Gap 4: exact gap formula (tu:L-gap-exact) | STANDS (PROVED) | gap_dh.py Q3: matches the direct 6×6 determinant formula to 2.5e−15 relative over 2·10⁵ configurations. |
| Gap 4: DG1 and DG3 (via DG1', DG3') and the uniform O(β^{-1/2}) bound | STANDS (PROVED) | gap_dh.py Q5–Q8 met, 0 failed. Lean: log bounds, cross term, determinant factor, coefficient difference. |

Counts (met, failed, measured only):
- w1w3.py: 12 predicates (P1–P12). 11 met. P4 failed against its docstring tolerance (§3). Measured only: c_ρ values and ratio maxima.
- gap_dh.py: 11 predicates (Q1–Q8, H1–H3). 11 met, 0 failed. Measured only: worst margins.
- err_const.py: 7 predicates. 7 met, 0 failed. Measured only: max ratios.
- Lean: 9 lemmas. 9 met, 0 failed.
- Child: 11 predicates. 11 met, 0 failed (rerun by me: byte-identical).

Things I found wrong in the note, stated plainly:

- **"Dimensionally wrong" was a misreading.** The writer's suspicion about the Δh bound is a misreading, not a defect. The bound is a derivative bound in σ = S².
- **The old Err rate is weaker than needed.** The note's rate O(L(M+2L)²/(√β s₋⁴)) still holds, but the derivation gives s₋⁻².
- **DG3 is mislabelled.** The note writes "−gap ≤ DG3 with κ₃". The correct statements are −gap₃ ≤ DG3(κ₃) and −gap ≤ DG3(κ). This is fixed in the patch.
- **The claimed uniform order is not literally true.** The note says DG terms are O(M²(1+κ̄)²/(√β sin²η')). This is not uniform in M: the term 4h²M⁴/β is not of that form. It is O(β^{-1/2}) only for fixed M, which is all that is used. The patch replaces it with the explicit bound (tu:L-gap-unif).
- **The σ_w lower bound in Prop E13 is unnecessary.** The note's claim that "σ_w² ≥ s₋² − 2M²/β stays bounded away from 0" is not needed. The D_w ≥ 1 form avoids it.

## 2. Hypotheses each statement uses, and where they are stated

**Lemma tu:U-W13** (new; tun_upper_patched.tex §tu:U-sec-weight). It uses:
- η ∈ (0, 1/2] and τ ∈ (0, 1) (first paragraph of §tu:U-sec-weight);
- ε(a) = 2·asinh(sin a), with \|ε'\| ≤ 2 (from the setting, §tu:U-sec-intro);
- L = √(2ε(π/2)) (§tu:U-sec-weight);
- f from (W2).

**Δh bound in tu:L-taylor.** It uses:
- the product ball \|ξ_i\| ≤ r_b ≤ 1/2;
- Lemma tu:L-exact(c) (x0' = x0·g0 − u·ξ, and 0 ≤ 1 − g0 ≤ \|ξ\|²);
- σ₋ > 0 for the stated form;
- r_b ≤ S/8 for (tu:L-dh-explicit).

**Exact gap (tu:L-gap-exact).** It uses:
- (G1) and (G2) of Lemma tu:L-exact (the singular values and ℓp = −κw);
- the flat identity;
- S² ≤ 2 (hence σ_w² ≥ 0).

The uniform bound (tu:L-gap-unif) additionally uses x ∈ 𝒯, that is \|b\| ≤ M and S ≥ s₋, and \|κ\| ≤ κ̄ from Lemma tu:L-exact(f).

**Err bound (tu:L-err-explicit).** It uses:
- x ∈ 𝒯 and L/√β ≤ s₋/8;
- H_Ψ and Λ from Lemma tu:L-ansatz-props(i), and H_Θ ≤ θ₀/ℓ from (ii);
- \|Θ'\| ≤ θ₀.

## 3. Failed predicates

**w1w3.py P4.** P4 asks that g be C¹ at the junctions, with the one-sided derivative jump below 1e−12 (docstring).
- The code compared against 1e−5 instead of 1e−12. That is my own defect: the code differs from the docstring.
- Measured jumps were 5e−13 to 1.9e−10, so the predicate fails against the docstring tolerance for η = 0.05 and 0.01.
- Cause: my own expectation was wrong, not the target. The right-hand derivative was evaluated at an offset of 1e−13 from the junction, where it is O(offset/η) by construction, not 0.
- C¹ is proved analytically: Sm'(0) = Sm'(1) = 0. The result file is kept unchanged.

No other predicate failed (mine or the child's).

## 4. What I did not check

- I did not re-verify the other steps of Lemma tu:L-taylor, only the ΔS² and Δh parts: E_W, B_W and the tilt Taylor remainder. These were already checked in the working file. err_const.py checks only the arithmetic chain from those quantities to (tu:L-err-explicit), not Err ≥ \|F − 𝓜\| itself.
- I did not check Tail, Q or ρ(β) in Prop tu:L-E13.
- I did not check the other open steps listed by the writers: S4-alg corners, valley balls, the link-exchange version of (B), the M² number, the 4.599 fit, and Lemma tu:L-L4.
- I did not check the composition into tu:U-schur or Lemma tu:U-K beyond "H finite, P = L".
- The C^∞ variant of W1 is mentioned, not written out.
- The patched note has 29 overfull-box warnings; the original has 28. These are cosmetic and not fixed.
- The child and I share a model family. The child's grid check is not independent review of the proofs.

## 5. Delegated questions and outcomes

**Child T175** (admitted under T173, `child_admit.log`; released, `child_release.log`).
- Question: a numerical grid check of each new inequality (A1–A4 for W1, B1–B3 for W3, C1 for Δh, D1–D2 for the log bounds).
- Control: ∫₀¹ e^{−x²} dx. Known answer √π/2·erf(1) = 0.746824. The child answered 0.746824, which is correct. I graded this before reading anything else.
- Outcome: all 11 predicates met, 0 failed. Its c_ρ values equal mine to 6 decimals.
- I reread `child/gridcheck.py`: its predicates match PROMPT.txt, and it uses the analytic g' and f̃''. I reran it in `child_rerun/` (check K5), and `results.json` is byte-identical.
- Run: check K2, exit 0, 103 s.

**Grandchild T176** (admitted by the child under T175 and released; both events are in the graph).
- Question: an independent recomputation of c* and c_ρ(η = 0.05), and the inequality c* − π√(6η) ≤ c_ρ ≤ c*.
- Control: ∫₀^π sin = 2, passed (per the child).
- Result: c* = 4.605413195 and c_ρ = 4.456390111. These agree with my w1w3.py values (4.6054131874 and 4.456390).

## 6. PCP OS record

- Register `pcp/`, checks K1–K8: w1w3, child-run1, gap_dh, lean-GapA, child-rerun, err_const, pdflatex-patched, pdflatex-patched-final.
- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## 7. Exact commands to rerun

All commands run from /home/user/z4-workers/u1-gapA. Result files are opened with mode "x", so move results/ aside first.

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name w1w3 --expect-exit 0 -- python3 prog/w1w3.py
$P check --ws pcp --name gap_dh --expect-exit 0 -- python3 prog/gap_dh.py
$P check --ws pcp --name err_const --expect-exit 0 -- python3 prog/err_const.py
$P check --ws pcp --name lean-GapA --expect-exit 0 --cwd /home/user/z4-lean -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/u1-gapA/lean/GapA.lean'
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P check --ws pcp --name child-rerun --cwd child_rerun --expect-exit 0 -- python3 gridcheck.py
cp note/tun_upper.tex note/tun_upper_patched.tex && cp note/tun_lower.tex note/tun_lower_patched.tex && python3 patch_upper.py && python3 patch_lower.py
```

The two overfull-box edits applied after patch_*.py are the inline python in notes.md step 8. They are already in the delivered patched files.

```
cd build && pdflatex -interaction=nonstopmode -halt-on-error wrap_patched.tex && pdflatex -interaction=nonstopmode -halt-on-error wrap_patched.tex && cd ..
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Task graph commands used:

```
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos task-admit /home/user/z4-work/graph/attempt.jsonl --by principal --label u1-gapA-child --parent T173
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos task-release /home/user/z4-work/graph/attempt.jsonl --by principal --id T175
```

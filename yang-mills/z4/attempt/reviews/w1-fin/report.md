# report.md — w1-fin (task T185): referees' repairs applied to the note

Control: `control.txt` = 0.272341 (−ln tanh 1).

Deliverables:
- `note/tun_upper.tex` and `note/tun_lower.tex` (patched). `note/main.tex` and `note/preamble.tex` are unchanged.
- `note/main.pdf`.
- `CHANGES.md`: 29 changes, each with file, original line, referee item, old text and new text.
- This file.

Baseline for every diff: `orig_note/`, a read-only copy made before the first edit.

The author of the repairs (me) and both referees are the same model family as the note's authors. Nothing here is independent review.

## 1. Verdict table

Verdict meanings for this task:
- **STANDS**: the repair is applied, and the repaired text is consistent with what is on the page.
- **DEFECT**: a repair could not be applied, or something is still wrong.
- **NOT CHECKED**: I did not check it.

| Item | Verdict | Evidence |
|---|---|---|
| Upper #4 DEFECT, §1.3 status paragraph; brief (i) | STANDS | Changes 2, 3, 4. The paragraph now says: both halves are written out; no step is conditional on anything off the page; everything was written, patched and refereed by Claude (Anthropic) sessions only; not read by another lineage or a person; Lean covers scalar lemmas only and the Lean files are not part of the note; thresholds are far beyond computable β. |
| Status lines in tun_lower.tex (l.612 E13, l.1055 tu:L-main); brief (i) | STANDS | Changes 15 and 29. "Conditional on the gap bounds / Δh bound" is removed, because Lemma tu:L-gauss and the Δh derivation in Lemma tu:L-taylor are on the page (§6), and REFEREE_lower #12/#13 rederived them. Conservative wording: the E13 line keeps that the original challenger did not check the gap bounds. |
| Upper #11 DEFECT, Remark tu:U-R-rem | STANDS | Change 5. The claim is restricted to β = 256 and 1024. The referee's β=64 values (1.04, 0.98) are stated. |
| Upper #23 DEFECT, Remark tu:U-F-num, plus §1.3 item 3 (#5); brief (ii) | STANDS | Changes 3, 7, 8. States τ=δ=β^{-1/3}. Corrects 2.2e13 → 2.03e13 and "8.6–14" → 7.33–14.23 (on β∈[100,4096]). Adds a caveat that τ<1/5 fails for β≤125. The numbers are the referee's and were not recomputed by me. |
| Lower #8 GAP, tu:L-M4 φ_min(η)>0; brief (iii) | STANDS | Change 13. The added argument comes from the construction in tu:U-W13. Predicate C3: φ_min>0 for η∈{0.4,…,0.01} with δ=τ=½ (e.g. 4.48e-3 at η=0.4, 1.53e-5 at η=0.01). |
| Lower #25 DEFECT, §8.1 parameter list; brief (iv) | STANDS | Changes 18–21. Adds δ=τ=½ with the explicit tu:U-W13 ρ_η and f̃. Gives explicit C^∞ χ and Θ̃ (with an s_∞ step). Sets C=1 and M² := M_A²(η). Moves μ out of the list (it depends on β). Adds a threshold-by-threshold argument that every β₀ is a function of η alone. Predicates C1, C2 and C4 are met. |
| Lower #15 nit, C in L | STANDS | Change 20 (C=1; "any fixed C>0 would do", as the referee says). |
| Lower #26 nits (μ′ undefined; padding to a common n) | STANDS | Changes 23 (padding) and 24 (μ′ := e^{−35a₋√β−R′_β}; the case-(I) bound −log g ≤ 35a₋√β+R′_β gives g ≥ μ′). |
| Lower #10 nit, q at S=0 | STANDS | Change 12. |
| Lower notation nits: ε(sin a); set S vs radius S; a₁ vs e^{−3η/4}; ΔS² as a definition | STANDS | Changes 11 (11 occurrences, predicate E2), 22/25–28 (set renamed 𝒮 in §8 only), 16–17 (ā), 14 (:=). |
| Upper #1 nit, Jentzsch | STANDS | Change 1. |
| Upper #20 nit, H̃_δ(0) | STANDS | Change 6: H̃_δ(0):=1. The bound and monotonicity still hold at z=0. |
| Upper #27 nit, tu:U-weight(1) at π/2 | STANDS | Change 9 (continuity of f̃'). |
| Upper #34 nit, Remark tu:U-uses | STANDS | Change 10. |
| Compilation | STANDS | `pdflatex main.tex` three passes in note/: exit 0, 0 undefined references, 0 LaTeX warnings, **32 pages** (the original was 31). |
| No other line changed | STANDS | Child T186 diff: 9 + 18 hunks, all attributed. The only hunk not tied to a referee item (the upper Lean paragraph) comes from brief (i). main and preamble are byte-identical. My rerun of its hunks.py gives identical output. |
| Corrected numbers in the measured remarks (2.03e13, 7.33–14.23, 1.04/0.98) | NOT CHECKED | Taken from the referee's recomputation. Not recomputed by me. |

Counts: 16 STANDS, 0 DEFECT, 1 NOT CHECKED.

## 2. Hypotheses each statement uses, and where they are stated

I added no new statement. The repairs rely on the following:
- **φ_min>0 (Change 13).** Uses the construction of Lemma tu:U-W13 (tun_upper §4.2): ψ>0 iff ε>3η/2; χ_W>0 on [0,π/2); ε is increasing on [0,π/2]; and 2η ≤ 0.8 < ε(π/2)=1.763 (η≤0.4, the hypothesis of tun_lower §6.2).
- **δ=τ=½ (Change 20).** Proposition tu:U-B needs η∈(0,½] and δ,τ∈(0,1) (tun_upper §4.4). The window condition 2asinh(cos ¼)=1.718 > η (predicate C4) is used in the proof of tu:U-weight(1). These δ,τ are not the β^{-1/3} of Corollary tu:U-F-cor(b), and the text says so.
- **χ and Θ̃ (Change 20).** They satisfy the properties listed in §6.4 (tu:L-ansatz): C^∞; χ=0 on [0,a₋/2]∪[π−a₋/4,π] and =1 on [a₋,π−a₋/2]; Θ̃=Θ on [0,π/2]; 0≤Θ̃'≤θ₀; Θ̃'=0 near π (checked as predicates C1 and C2).
- **"β₀ a function of η alone" (Change 21).** Rests on the dependencies stated in tu:U-B (β₁ via β₀(η/4) of tu:U-F and ω(β), which depends on H), Prop. tu:L-E13 (constants listed at l.586, 619, 628 of the original), tu:L-balls, tu:L-L4 and tu:L-M4.
- **H̃_δ(0):=1 (Change 6).** e^{-0}I₀(0)=1.

## 3. Failed predicates

1. `apply_repairs-run1` (register K1, exit 1) failed **E1[11]**: I expected 9 occurrences of `\varepsilon(\sin `, and there are 11. I had counted lines rather than occurrences and had missed l.249–250. This was **my own expectation, not a defect of the target**. Two predicates failed as a consequence: **E1[23]** (an edit that depends on E1[11]) and **E2**. Result file: `res_apply_run1.md`, kept. In run2 the count was fixed to 11 and all predicates were met.
2. Child's predicate "no hunk inside a proof block" failed. Five hunks are inside proofs: upper H8 (the #27 remark) and lower H3, H7, H8, H17 (renames only). The child classified this as its own expectation. I agree: those edits are listed repairs.

Predicates (met, failed, measured only):
- **Mine:**
  - run1: 45, 3, 5.
  - run2: 48, 0, 5. Measured only = the H bound at 5 values of η, e.g. H ≤ 10.38 at η=0.4 and ≤ 125.2 at η=0.01.
  - Compile: 3, 0, 0.
  - Rerun of the child's script: 1, 0, 0.
- **Child:** 8, 1, 3.

Tolerance sources:
- E-predicates: exact string match.
- C1: 1e-12. The closed-form step function leaves only rounding.
- C2: 1e-9 for Simpson with 2·10⁵ panels on a smooth integrand. The observed difference is ≤ 1.1e-13.
- C3: positivity threshold 1e-12, far below the observed minimum of 1.5e-5.

## 4. What I did not check

- I did not recompute the measured numbers of Remarks tu:U-R-rem and tu:U-F-num, or §1.3 item 3. I used the referee's values.
- The rest of the proofs. I changed none of them beyond the listed repairs and did not re-referee them.
- The "β₀ a function of η alone" argument (Change 21) is a dependency check by reading. No explicit β₀ was computed.
- C1–C3 were checked on grids at 5 values of η, not for all η∈(0,0.4].
- No Lean was used. /home/user/z4-lean/READY exists, but I make no Lean claim.
- The rendered PDF was not inspected visually beyond the compile log.

## 5. Delegated questions and outcomes

- **Child T186** (admitted under T185, run as `child-run1` in my register, exit 0, released).
  - Question: does every DEFECT/GAP/nit in the two reports have a corresponding change, and is no other line changed? Diff of orig vs patched.
  - Control: 1²+…+20² = 2870. **Graded correct** before I read anything else.
  - Outcome: 22 of 22 repair items have a change; 0 MISSING. One hunk is unattributed to the reports: the upper Lean paragraph, which is my brief (i) item and is not in the reports. main.tex and preamble.tex are identical. No hunk alters a proof step beyond its repair.
  - The child noted that M² := M_A² is "slightly beyond the letter" of #25. That is correct: I added it so that β₀ depends on η alone, and I say so in CHANGES.md.
  - The child reported "9 → 0" occurrences of ε(sin. That counts lines; there are 11 occurrences.
  - I reran its hunks.py (`rerun-child-hunks`, K5): output identical.
- **Grandchild T187** (admitted by the child under T186, released).
  - Question: an independent recount of the lower-half hunks and their overlap with proof blocks.
  - Control: 1³+…+10³ = 3025, correct.
  - Outcome: 18 merged hunks; hunks 3, 7, 8 and 17 are inside proofs. This agrees with the child, and the child reran it (`gc-rerun`).

## 6. Exact commands to rerun

```
cd /home/user/z4-workers/w1-fin
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name apply_repairs-run1 --expect-exit 0 --timeout 300 -- python3 prog/apply_repairs.py res_apply_run1.md   # as run: exit 1 (count 9)
$P check --ws pcp --name apply_repairs-run2 --expect-exit 0 --timeout 300 -- python3 prog/apply_repairs.py res_apply_run2.md   # rerun: use a new result name (mode "x")
$P check --ws pcp --name pdflatex-3pass --cwd note --expect-exit 0 --timeout 300 -- bash -c "for i in 1 2 3; do pdflatex -interaction=nonstopmode -halt-on-error main.tex > pass\$i.log 2>&1 || exit \$?; done"
$R task-admit $G --by principal --label w1-fin-child --parent T185          # -> T186
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T186
$P check --ws pcp --name rerun-child-hunks --cwd child_rerun --expect-exit 0 --timeout 120 -- python3 -I hunks.py hunks_out_rerun.txt
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

`apply_repairs.py` reads `orig_note/` and rewrites `note/tun_*.tex`. The result is deterministic.

Last lines of the verifies:
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

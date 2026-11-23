# T186 result: do the patches apply the two referee reports?

Control: sum of i^2, i=1..20 = **2870** (control.txt).

Short answer: all 22 repair items have a matching change (0 MISSING). 1 hunk is UNATTRIBUTED (upper H4, the Lean paragraph). main.tex and preamble.tex are byte-identical. No hunk changes a proof step beyond its repair. Five hunks lie inside proof blocks, and each is a notation rename or a small closing remark.

Hunk list: `hunks_out.txt`, produced by `hunks.py` (difflib, autojunk=False, hunks merged if the gap is ≤3 lines). Line numbers below are patched line numbers.
- tun_upper.tex: 9 hunks (10 opcodes).
- tun_lower.tex: 18 hunks (27 opcodes).

## Q1. Repair items and the change found

U = REFEREE_upper (items by its table #), L = REFEREE_lower.

| Report | Item | Kind | Change found (patched) |
|---|---|---|---|
| U | #4 §1.3 status paragraph | DEFECT | tun_upper 85–94 (H2): rewritten as "no step of the second half is conditional on anything not on the page… gap bounds now derived in Section tu:L-sec-sub". The report allowed either option; the patch took the "remove the qualifier" one. Its pointer is true: L-taylor is at tun_lower 436 and L-gauss at 486, both inside `\section` tu:L-sec-sub (160–815). The mismatching status lines the report cites are also changed: tun_lower 619–620 (H6, the l.612 status) and 1080–1085 (H18, the l.1055–1057 status). |
| U | #11 Remark U-R-rem | DEFECT | tun_upper 337–338 (H5): claim restricted to β=256,1024. The patch notes that β=64 gives 1.04 and 0.98. |
| U | #23 Remark U-F-num | DEFECT | tun_upper 561–571 (H7): τ=δ=β^{-1/3} stated. 2.2e13 → 2.03e13. 8.6–14 → 7.33–14.23. The patch adds a note on β≤125 and credits the referee. |
| U | (c) wrong numbers, #5/#23 | numbers | Same corrected values, repeated in the §1.3 item: tun_upper 100–102 (H3: 2.0e13; 7.3 to 14.2). |
| U | #1 nit: cite Jentzsch | nit | tun_upper 38–40 (H1). |
| U | #20 nit: H̃_δ(0) undefined | nit | tun_upper 421–423 (H6): H̃_δ(0):=1, with the monotonicity and bound at z=0, and a note that r'=1 is a null set. |
| U | #27 nit: a=π/2 in (1) | nit | tun_upper 691–692 (H8): continuity of f̃', with f̃'(π/2)=0. |
| U | #34 nit: schur and A not listed | nit | tun_upper 885–886 (H9). |
| U | #5 imprecision (τ, δ unstated) | not a nit; covered by #23 | tun_upper 100–102 (H3). |
| L | #8 GAP φ_min>0 | GAP | tun_lower 227–241 (H2): new argument in the Lemma L-M4 area. Uses W13 (ρ_η>0 where ε>3η/2, f̃>0, a compact set) and cites Prop. U-B(2) for a₂. |
| L | #10 nit: q at S=0 | nit | tun_lower 174 (H1): "(At S=0 we put q:=0…)". |
| L | #15 nit: C never fixed | nit | tun_lower 947–961 (H10), last item: C=1. |
| L | #25 DEFECT §8.1 list | DEFECT | tun_lower 947–961 (H10): δ=τ=½ with the explicit W13 construction; χ and Θ̃ defined with s_∞; C=1; μ moved out of the list as β-dependent. Also 967–972 (H11): every threshold is a function of η. Also 314 (H4): "fixed" → "defined… depends on β". |
| L | #26 nit: μ′ undefined | nit | tun_lower 1012 (H15): μ′:=e^{…}. |
| L | #26 nit: padding to a common n | nit | tun_lower 1000–1001 (H14). |
| L | Notation 1: ε(sin a) vs ε(a) | nit | tun_lower 227–241 (H2), 255–256 (H3), 709–710 (H7), 941 (H9). The count of `\varepsilon(\sin` went from 9 in orig to 0 in patched. |
| L | Notation 2: S radius vs set | nit | tun_lower 984–985, 990, 1057, 1066–1072 (H12, H13, H16, H17): the set is renamed 𝒮. Plain S as the abstract set in §5 (113–128) is untouched. Those uses are in a different section and are not the radius. |
| L | Notation 3: a₁ vs e^{−3η/4} | nit | tun_lower 725–731 (H8): ā. No `a_1:=` remains. |
| L | Notation 4: "ΔS² ≤" as definition | nit | tun_lower 443 (H5): ≤ → :=. |

MISSING: none (22 of 22 items have a change).

Judgement calls: U#4 and L#25 are applied in the form the report offered. For L#25 the patch fixes δ=τ=½ (the report's repair). The claim that every threshold depends on η alone is the patch's own assertion; I did not recheck it.

## Q2. Attribution of every hunk

tun_upper.tex:

| Hunk | Patched lines | Item |
|---|---|---|
| H1 | 38–40 | U#1 |
| H2 | 85–94 | U#4 |
| H3 | 100–102 | U#5/#23(c) |
| H4 | 113–115 | **UNATTRIBUTED** (Lean-status wording; see below) |
| H5 | 337–338 | U#11 |
| H6 | 421–423 | U#20 |
| H7 | 561–571 | U#23 |
| H8 | 691–692 | U#27 |
| H9 | 885–886 | U#34 |

tun_lower.tex:

| Hunk | Patched lines | Item |
|---|---|---|
| H1 | 174 | L#10 |
| H2 | 227–241 | L#8, plus notation 1 |
| H3 | 255–256 | notation 1 |
| H4 | 314 | L#25 (μ "fixed") |
| H5 | 443 | notation 4 |
| H6 | 619–620 | U#4 (the l.612 status) |
| H7 | 709–710 | notation 1 |
| H8 | 725–731 | notation 3 |
| H9 | 941 | notation 1 |
| H10 | 947–961 | L#25 and L#15 |
| H11 | 967–972 | L#25 |
| H12 | 984–985 | notation 2 |
| H13 | 990 | notation 2 |
| H14 | 1000–1001 | L#26 (padding) |
| H15 | 1012 | L#26 (μ′) |
| H16 | 1057 | notation 2 |
| H17 | 1066–1072 | notation 2 |
| H18 | 1080–1085 | U#4 (the l.1055–1057 status) |

Unattributed: tun_upper H4 only. The text now says the Lean files "were not compiled" and that "Lean-checked" remarks elsewhere refer to scalar working-file steps. Neither report asks for it. It narrows a claim and is harmless, but it is outside the reports.

Slightly beyond the letter: tun_lower H10 changes "M² ≥ M_A²" to "M² := M_A²". That is a definitional choice, compatible with the earlier condition, that goes with fixing the parameters (L#25). It is a choice, not a proof step.

## Q3. main.tex and preamble.tex

Both are identical (byte-identical line lists; hunks_out.txt lines 1–2).

## Q4. Does a hunk alter a proof step beyond its repair?

No hunk does. Hunks that are in proofs, or add reasoning:

| Hunk | In proof block? | Alters a proof step beyond the repair? |
|---|---|---|
| upper H8 (686–712) | yes | No. It adds an endpoint remark, which is the repair for #27. |
| lower H3 (252–259) | yes | No. Notation only. |
| lower H7 (686–745) | yes | No. Notation only. |
| lower H8 (686–745) | yes | No. A pure rename a₁→ā, applied consistently ("a≤ā", `\bar a`). |
| lower H17 (1065–1078) | yes | No. S→𝒮 rename only. |
| lower H2 | no (a statement/paragraph) | New argument for φ_min>0. It is the L#8 repair. |
| lower H10, H11 | no | Fix parameters and claim the thresholds depend on η alone (L#25). They fix choices and change no inequality. |
| lower H14, H15 | no | They define μ′ and say the chains are padded (L#26). |
| All other hunks | no | Status text, notation, number or citation edits. |

"In a proof block" means a `\begin{proof}…\end{proof}` span in the patched file (my regex: 18 spans in upper, 26 in lower).

## Predicates (met, failed, measured only)

Fixed in the `hunks.py` docstring before the first run, plus later ones as noted.
- **Met (8):**
  - main.tex identical.
  - preamble.tex identical.
  - Every hunk printed with patched line numbers.
  - Grandchild control 3025 correct.
  - Grandchild's merged lower count (18) equals mine.
  - Grandchild's set of lower hunks inside proofs {3,7,8,17} equals mine.
  - Grandchild rerun output identical.
  - Residual `\varepsilon(\sin` in patched = 0 (a check added after the first run).
- **Failed (1):** "no hunk lies inside a proof block". Five do: upper H8; lower H3, H7, H8, H17. This was my own expectation, not a defect of the target. The docstring said "measured per hunk" but a no-hunk reading was my first guess. Each of the five is judged in Q4.
- **Measured only:**
  - Hunk counts: 9 upper, 18 lower merged (27 lower unmerged).
  - 1 UNATTRIBUTED hunk (upper H4).
  - Q4 judgements are mine, by reading.
- **Tolerances:** none (exact text comparison). The merge gap of 3 lines is my own choice. The grandchild counted both merged and unmerged, so the result does not depend on it.

## Grandchild

- Task T187 (parent T186), admitted before launch and released after the rerun.
- Its control (1³+…+10³ = 3025) is correct.
- Its question: independently recount the lower-half hunks and check overlap with proof blocks.
- Outcome:
  - 27 unmerged and 18 merged hunks. It found 26 closed proof blocks and no nesting.
  - Hunks 3, 7, 8 and 17 lie fully inside proofs.
  - I read recount.py and reran it as register check `gc-rerun` (exit 0, output identical).

## Rerun commands

```
cd /home/user/z4-workers/w1-fin/child
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"   # method not found: expected
$P check --ws pcp --name hunks --expect-exit 0 -- python3 -I hunks.py hunks_out_N.txt   # new filename (mode "x")
# grandchild: copy grandchild/{orig_in,patched_in,recount.py} to a fresh dir, then
$P check --ws pcp --name gc-rerun --cwd <fresh dir> --expect-exit 0 -- python3 -I recount.py
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Last line of `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

Last line of the Rust verify: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

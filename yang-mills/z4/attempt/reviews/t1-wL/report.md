# Report t1-wL (task T168): second half of the note, tun_lower.tex

Writer t1-wL. I share a model family with the director and with every author of the parts, so my agreement is not independent review. No network was used. Control: control.txt = 0.272341. I used no Lean and claim no Lean result. All "Lean-checked" remarks in the .tex repeat what the working files say; I compiled no .lean file.

Deliverable: `/home/user/z4-workers/t1-wL/tun_lower.tex` (926 lines, Sections 5–8, labels `tu:L-...`).

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| S5 Lemma tu:L-flux (I0), (I1), (I2) | STANDS | Rederived while writing. (I2) has prefactor 4 (CHAL_conditional item 10). (I1) needs λ = sup spec T; I added this hypothesis, which the parts left implicit. |
| S5 Lemma tu:L-GS, Lemma tu:L-C, Lemma tu:L-Pc, Corollary tu:L-B | STANDS | Rederived line by line (PATHS §0–§2.1; TUNNEL_LOWER §1). |
| S6 Lemma tu:L-L4 | STANDS | Rederived (TUNNEL_LOWER_FULL §5). It is o(1) only and gives no usable β₀. |
| S6 Lemma tu:L-M4 | STANDS (given tu:U-B) | Rederived. The constant convention is fixed: C(η) bounds the squared weighted norm. |
| S6 tangent decomposition, ansatz, Lemma tu:L-ansatz-props (C2, C3, C6, C7) | STANDS | Rederived (TUNNEL_LOWER2 §1–2, FULL §2 and §4). |
| S6 exact algebra (G1), (G2), Taylor remainder, log J and flat identity | STANDS | Rederived, except the Δh bound (see §3). |
| S6 gap bounds DG1/DG3 | NOT CHECKED | E13 states them without a derivation. No challenger checked them. |
| S6 Prop tu:L-E13 ((E1), (E3)) | STANDS conditional on DG and Δh | The assembly of the bounds is rederived. |
| S6 Lemma tu:L-E2 | STANDS (given tu:U-K) | Contains the missing Taylor line from CHAL_conditional item 7. |
| S6 Lemma tu:L-S4 (S4-alg) | STANDS for (cutoff), (ring), A₁−λ ≥ e^{η/2}−1 and the A₁−A₂ absorption; **gap** in the corner absorption | The parts argue the c₁c₂(A₁−A₂−A₃) term only qualitatively. My numerical check P1 holds on 5/5 η (slack ≥ 0.0100). |
| S6 Lemma tu:L-norm, Prop tu:L-sub | STANDS (given tu:U-R, tu:U-F) | Rederived. |
| S7 Lemma tu:L-elem, tu:L-chain, tu:L-geom, Thm tu:L-H4 | STANDS | Rederived. (vol) has an arithmetic chain that I rewrote; the bound 11r³/(24π) is true and weaker than what the chain gives. |
| S7 Cor tu:L-H4cor constants 8.35, 9.09, 35 | STANDS | Recomputed: 8.346 (d = 3.645, ρ = 0.264) and 9.085 (P3 met). |
| HARNACK "M² = O(log 1/η)" | DEFECT (harmless) | M² ~ 1/η. Recorded in the .tex. |
| FULL §4 "M² ≥ 2ρ_B²" ⇒ G−c₁ ≥ e^{−1.5ρ_B²}/2 | DEFECT (harmless) | P2 FAILED: at M² = 0.5 the left side is 0.081 and the bound needs 0.344. M² ≥ 1.068 is needed, and the c₁ condition already forces M² ≥ 18. Recorded in the .tex. |
| S8 chain x → σ₁x (C4), Lemma tu:L-balls | STANDS with one step not written out | See §3, item 4. |
| S8 Theorem tu:L-main, Corollary tu:L-limit | STANDS conditional | Conditional on the first-half results and on the items in §3. |

Counts: 15 STANDS (3 of them with a gap or condition noted), 2 DEFECT (both harmless), 1 NOT CHECKED.

## 2. Hypotheses each statement uses, and where they are stated

- **Lemmas flux / GS / C / P'c / B:** σ-finite space, symmetric positive bounded T, σ a measure-preserving involution commuting with T, g > 0 even and f odd eigenfunctions (§5 preamble). (I1) also needs λ = sup spec T. Lemma C needs ‖T_ΩΩ‖ < λ, Tφ ≥ λφ on Ω, φ ≤ g on Ω^c, and φ ∈ L². P'c needs a measurable path kernel and Σπ_k ≤ ρQ off the diagonal. Cor B needs v = inf |B| > 0, measurable centres, and uniform independent z_k.
- **L4:** the model only.
- **M4:** (B) of tu:U-B for u ∈ {g, f}, with λ_u ≥ e^{−η/4} and β ≥ β₀(η).
- **Ansatz props:** the parameter order of §8 and the definitions of χ and Θ̃ (C2, C3).
- **(E1)/(E3):** x ∈ 𝒯 with η' = a₋ (C1), H_Ψ, Λ, H_Θ finite, and r_b = L/√β small against sin²η'. Kernel facts (ϱ bounds) from the first half.
- **(E2):** tu:U-K, and global C² of Ψ∘a₁ and Θ̃∘a₂.
- **S4-alg:** (E1)–(E3) at x with Δ₁ + Δ₃ ≤ η/4 and Δ₂ ≤ 1, x ∈ supp φ_L with a₁ ∈ [a₋, π/2], the c₁ condition, and β ≥ β₀.
- **Norm on tube:** tu:U-R and tu:U-F (η/2-form, uniform in s ∈ [sin a₋, 1]), plus L4.
- **H4:** λ ≤ 1, g > 0 continuous and σ_i-even, ρ ≤ ½, β ≥ max(1, 4ρ²), a* ≤ π/4, x ∈ D_M, and m_B.
- **Theorem tu:L-main:** all of the above, in the order of limits of §8.

## 3. Steps the writer could not complete from the parts

1. **Δh bound** (Lemma tu:L-taylor). The bound Δh ≤ ΔS²/(2σ₋²√(1+1/σ₋)) is stated in E13 §2 without a derivation. I reproduce it as written. It is also dimensionally odd: σ₋ = S² − ΔS² is used where a value of S would be expected. All that is needed is Δh = O(r_b) uniformly for S ≥ s₋/2, and that follows from h being smooth on S > 0. I did not write that replacement, because the brief forbids inventing steps.
2. **Gap bounds DG1/DG3** (Lemma tu:L-gauss). E13 §3 gives only the cross-term inequality. My proof sketch in the .tex says only how they are obtained; it is not a full derivation. No challenger checked them.
3. **Corner absorption in S4-alg** (the last bullet of Lemma tu:L-S4). The parts use "≫", "≈ 0" and "V large" with no quantified condition on M. Measured (prog/s4corner.py, P1): in the limit Δ_i → 0, λ = 1, with M² at equality in the c₁ condition, the inequality 1 ≥ A₁⁻¹(1−x)(1−y) + (A₂/A₁)x + (A₃/A₁)y holds on a grid of the support for η ∈ {0.4, 0.2, 0.1, 0.05, 0.01}. The minimum slack is 0.107, 0.107, 0.095, 0.049, 0.0100. In the corner A₂/A₁ ≤ 0.006, because the c₁ condition forces M² sin a₋ to be large. This is evidence and not a proof. A written proof would need a quantitative case split. Note that at the corner A₃/A₁ ≈ e^{−Θ'(r₀)²/2} ≈ 0.894, so the margin there is about 0.1 and not large.
4. **Valley balls with a₁ just outside [a₋, π−a₋]** (Lemma tu:L-balls). FULL says "covered by the previous bullet", but such points are not in a ball of the first kind. A bound of the same form follows from H4 on a slightly larger D_{M'}, or from the subsolution. This is not written out in any part.
5. **(B) for f, with links exchanged.** This is used in M4. It is the first half's Proposition tu:U-B, which states it for any eigenfunction u. The link-exchange version is "the same proof" (TUNNEL_LOWER2 §3); I did not rewrite it.
6. **M² number.** FULL quotes M² required = 14.8 at η = 0.4 and "M² ≈ 3.4/η". With FULL's own c₁ formula I get 18.0. The child independently gets η·M² = 7.2 down to 4.7 for η = 0.4 … 0.005. FULL's numbers are not reproduced. This is harmless, since only the existence of M(η) is used.

## 4. Corrections and changes applied (with source)

- **Prefactor 4, not 2, in the sign-trial identity** (CHAL_conditional item 10; TUNNEL_LOWER §4): Lemma tu:L-flux (I2).
- **Missing Taylor line in the Schur/tilt step** (CHAL_conditional item 7): Lemma tu:L-E2, written out.
- **Header of Lemma F** (CHAL_lemmaF): it is not in my half. I cite tu:U-F only in the corrected η-form. The wording to fix belongs to the first half ("log max(M_in, A·M_out) → 0").
- **C1** (η' = a₋): the tube 𝒯 and Prop tu:L-E13. Wording fix (CHAL_assembly C1): the dependence is through s₋⁻⁴, h(s₋) and Δh, not "only sin²η'".
- **C2** (smooth χ cutoff in Ψ') and **C3** (Θ̃ smooth at π): the ansatz.
- **C4** (chain x → σ₁x): §8.
- **C5** (Lemma L4 replaces the sketches): Lemma tu:L-L4.
- **C6** (tent wording min(Ψ(a₁), Ψ(π−a₁))): Lemma tu:L-ansatz-props (iv), Prop tu:L-sub, Lemma tu:L-balls.
- **C7** (0 ≤ Ψ' ≤ √(2(ε+η))): Lemma tu:L-ansatz-props (i), (v).
- **E13 failed cross-term bound** (1 → 1/σ): Lemma tu:L-gauss, with a note.
- **E13 numerical parameter set violates the constraints** (CHAL_parts E10): noted in the status of Prop tu:L-E13.
- **CHAL_parts remark:** (E1)/(E3) are needed only on a₁ ∈ [a₋, π/2]. Stated.
- **HARNACK "M² = O(log 1/η)" is wrong** (FULL §3, CHAL_assembly (3)): stated in Cor tu:L-H4cor.
- **PATHS remark** (ordered pairs and 2E): P'c is written with ordered pairs.

New defect found while writing: FULL §4's "M² ≥ 2ρ_B²" (P2). It is stated in the §8 remark on M.

## 5. Failed predicates

- **prog/s4corner.py P2 FAILED** (run K1): e^{−1.5ρ_B²} − e^{−M²} = 0.081 < 0.344 = e^{−1.5ρ_B²}/2 at M² = 2ρ_B² = 0.5. This was my expectation, and it is a defect of the target (FULL §4 wording). It is harmless.
- P1 MET 5/5 and P3 MET. The child's fid_check.py (rerun as K3) met all its predicates. Tolerances: P1 uses tolerance 0 on the exact main terms (o(1) dropped). P3 uses 0.01, the rounding of the quoted constants.

Counts: 2 met, 1 failed, 2 measured only (min slack per η; M² values).

## 6. What I did not check

- The first-half inputs: Lemma F, Lemma K, Lemma R, (B), and the I₀/I₁ bounds behind ϱ.
- No Lean file was compiled.
- The DG bounds and the Δh bound.
- I ran no numerics of (E1)/(E3) myself.
- The 1D model numerics were not rerun.

## 7. Compile result

- Wrapper: build/wrap.tex = `\input{../style/preamble}` `\begin{document}` `\setcounter{section}{4}` `\input{../tun_lower}` `\end{document}`.
  - The brief's wrapper `\documentclass{amsart}\input{style/preamble}` would fail, because style/preamble.tex itself contains `\documentclass[11pt]{amsart}`.
- pdflatex run twice, exit 0, 0 errors. The file is ASCII only.
- Warnings:
  - undefined references, all to the first half (expected): tu:U-kernel, tu:U-K, tu:U-R, tu:U-F, tu:U-B, tu:U-main;
  - 8 hyperref "Token not allowed in a PDF string" warnings, from math in section and subsection titles (harmless).

## 8. Delegated questions and outcomes

- **Child T169** (admitted under T168, graph event 338; released, event 346). It ran as `child-run1` (register check K2, exit 0, 353 s), with model sonnet.
  - **Question:** an independent fidelity check of tun_lower.tex against the parts. For every lemma statement and constant it was to give a verdict of MATCHES, CHANGED (justified or not) or WRONG.
  - **Control:** ∫₀^π sin² = π/2. It answered 1.570796. I graded it CORRECT before reading anything else.
  - **Outcome** (child/findings.md): 38 items and 15 constants, **0 WRONG**.
    - Most items MATCH, and the CHANGED ones are justified by CC#10, C1, C2, C3, C6, C7 or FULL §2.
    - It listed five unlisted changes, all harmless and disclosed:
      - the M4 squared-norm convention;
      - the remark on M;
      - the S4-alg hypothesis Δ₁+Δ₃ ≤ η/4 with Δ₂ ≤ 1;
      - "φ ≤ μ everywhere";
      - global smoothness in place of E13's (H1).
    - It noted three further points:
      - (a) the hypothesis s∘σ = −s in (I2) is unnecessary;
      - (b) Lemma L-balls was marked "Proved" although it has one step not written out;
      - (c) 9.09 is the value at (3.65, 0.265), not a minimum (the minimum of c_ch(K₁)/d is 8.985 at d = 4.08, ρ = 0.206).
    - It confirmed my P2 failure (0.081 against 0.344).
    - Its recomputation of the c₁-condition M² gives η·M² = 7.2, 6.7, …, 4.7. That does not match FULL's table (14.8, …) or FULL's "3.4/η".
    - It reproduced the S4-alg slacks: 0.1088, 0.1077, 0.0952, 0.0488, 0.0100.
    - It reproduced L_β, G1, G2, the flat identity and log J (to 6.4e−14), and (vol) and (I₁ up).
    - Its own run1 crashed with a math domain error, a defect of its program. Run2 met everything.
  - **Applied to the .tex:**
    - (a) the hypothesis is removed;
    - (b) the status line is softened;
    - (c) the wording is clarified;
    - H4 status: states the a_* = a₋, ϰ = 1 use.
  - **Reread and rerun:** I read fid_check.py and reran it under my register (K3 `rerun-child-fidcheck`, output renamed for mode "x"). The output is identical to the child's results_fid_run2.txt, all predicates MET.
- **Grandchild T171** (admitted by the child, parent T169; released at graph event 342, as the child reports; T171 appears twice in the graph file, consistent with admit and release).
  - **Question:** min over d∈[1,5], ρ∈(0,½] of c_ch(K₀)/d, and c_ch(K₁)/d at (3.65, 0.265).
  - **Control:** ∫₀¹x² = 0.333333, correct (graded by the child).
  - **Outcome:** 8.345845 at (3.645066, 0.263929). Its own predicate P3 (|9.0838 − 9.09| < 0.005) failed. That was its expectation, not a target defect.
  - The child reran it (rerun_gc/, identical). My P3 independently gives 8.346 and 9.085.

## 9. Exact commands to rerun

```
cd /home/user/z4-workers/t1-wL
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos; G=/home/user/z4-work/graph/attempt.jsonl
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')" > control.txt
$P init pcp --principal principal --principal-name "Kirtus Justus"          # fresh directory only
$P check --ws pcp --name s4corner-run1 --expect-exit 0 -- python3 prog/s4corner.py prog/s4corner_run1.json   # use a new output name on rerun (mode "x")
mkdir -p build && cd build && printf '%s\n' '\input{../style/preamble}' '\begin{document}' '\setcounter{section}{4}' '\input{../tun_lower}' '\end{document}' > wrap.tex && pdflatex -interaction=nonstopmode wrap.tex && pdflatex -interaction=nonstopmode wrap.tex; cd ..
$R task-admit $G --by principal --label t1-wL-child --parent T168     # gave T169
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T169
mkdir -p rerun_child && sed 's/results_fid_run2.txt/results_fid_rerun_parent.txt/' child/fid_check.py > rerun_child/fid_check.py
$P check --ws pcp --name rerun-child-fidcheck --cwd rerun_child --expect-exit 0 -- python3 fid_check.py
$P verify --ws pcp
$R verify pcp/register.jsonl
```

Register checks:
- K1 `s4corner-run1`: exit 0.
- K2 `child-run1`: exit 0.
- K3 `rerun-child-fidcheck`: exit 0.

Last line of `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

Last line of `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

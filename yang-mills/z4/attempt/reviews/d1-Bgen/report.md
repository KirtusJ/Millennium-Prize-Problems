# Report: d1-Bgen (task T36), removing the gauge-group hypothesis

**Main result.** The gauge-group hypothesis can be removed. I prove the theorem for every compact Lie group G with dim G ≥ 1 and a faithful unitary representation ρ. G does not need to be connected. The bound is exactly (G(n)/G(0))², with no factor depending on the group.

**Where it fails.** The proof breaks for finite groups (dim G = 0). For Z₂ the conclusion is false according to the literature; I cite this and did not check it.

**Constants.** The brief asked for the tail constant in terms of (dim G, N) only. That cannot be done; there is a counterexample in item 5.

The full statement and proofs are in THEOREM_B_GENERAL.md. general.tex is the LaTeX subsection; it compiles with preamble.tex and fits in 2 pages.

The program predicates are 26 met, 0 failed, 2 measured only (box_mc 9, ball_check 12, Lean 5).

**Independence.** I am the same model family as the director, so this is not an independent review. I found no defect in sec_proof_SU2.tex as an SU(2) proof. One of its arguments does not carry over verbatim to general G (item 7 below).

## 1. Verdict table

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | Theorem B_gen: G compact Lie, dim G ≥ 1, ρ faithful unitary, d = 4; same conclusion | STANDS | Every changed step is proved in THEOREM_B_GENERAL.md §2–5 (relative to the SU(2) proof, plus standard facts cited in §6). |
| 2 | The ratio is exactly (G(n)/G(0))², with no group or ρ factor | STANDS | The Gaussian weight and the observable both use the Hessian ½\|X\|²_ρ. Cov = (d/2)G(n)² + G(n)E\|f\|² + ¼Var\|f\|². The same holds for an observable form B ≠ A. |
| 3 | Reflection positivity and chessboard are group-independent | STANDS | They need only s(U⁻¹) = s(U), since Re Tr ρ(U⁻¹) = Re conj Tr ρ(U), and unimodularity. |
| 4 | Haar ball volume: c s^{d/2} ≤ V(s) ≤ C s^{d/2}; lim V/s^{d/2} = ω_d 2^{d/2}/Vol_ρ(G) | STANDS | Lemma V. Checked by B1 (SU(3) 0.62022 vs 9√3/(8π) = 0.620245), B1′ (SU(2)), child T37 and grandchild T39. |
| 5 | Tail constant expressed only in (dim G, N) | DEFECT (of the brief's premise) | Take U(1) with ρ_k = e^{it} ⊕ e^{ikt} (N = 2, d = 1). Then lim V/√t = 2/(π√(1+k²)) while V(1) ≈ ½ (B2, B3; the ratio is 39 at k = 50). The constant does not enter c(n). |
| 6 | Zero set: s(U) = 0 iff U = 1; central elements | STANDS | Follows from faithfulness. A central z ≠ 1 on one link makes adjacent plaquettes z·U_p ≠ 1. Lemma flat holds for any group. |
| 7 | The SU(2) argument for Var_μ(O_{p0}) > 0, transferred verbatim | DEFECT for general G (repaired) | For O(2) in the defining representation, s ≡ 1 on the reflection component, so level sets are not null. The repair: s(·V) is analytic and non-constant on G₀V⁻¹. |
| 8 | Laplace limit when the chart does not cover G | STANDS (new argument) | Far-region mass ≤ (Vol β^{d/2})^ν e^{−βη/2}/z_M → 0 (THEOREM_B_GENERAL.md §5 N1). |
| 9 | Theorem holds without connectedness of G | STANDS | The hypothesis can be dropped: the chordal χ handles the shell lemma, and the metric is Ad(G)-invariant on all of G. |
| 10 | Finite G (dim 0) | DEFECT, proof fails | F ≡ 0, so Var X₀ → 0 and the assembly breaks. Z₂ being gapped at weak coupling is cited, NOT CHECKED. |
| 11 | U(1): abelian, no BCH errors; consistent with the massless phase | STANDS | y_p = dx_p exactly. Box MC agrees for ρ = e^{it} and for ρ = e^{it} ⊕ e^{2it}. |
| 12 | Test (i): ball scaling and Hessian for SU(3) and U(1) | STANDS | Child: P1–P7 met; its P4 failed (its own expectation). Reruns: grandchild su3.py c = 0.620245, identical; t37b PASS with identical z-values; my B1, B4, B5. |
| 13 | Test (ii): box R₁, β = 300, E O_p → (d/2)·7/24 (normalisation factor 1) | STANDS | SU(3) 1.16802 ± 0.00111 vs 7/6. SU(2) 0.43685 ± 0.00040 vs 0.4375. U(1) 0.14589 ± 0.00015 and U(1)₂ 0.14592 ± 0.00014 vs 7/48. P0: C_pp = 7/24 exactly. |
| 14 | New scalar inequalities in Lean | STANDS | lean/GenScalar.lean L1–L5: exit 0; axioms are only propext, Classical.choice, Quot.sound; no sorry. /home/user/z4-lean/READY exists. |
| 15 | general.tex compiles with preamble.tex, ≤ 2 pages | STANDS | texbuild/g1.tex: 2 pages. g2.tex (with sec_proof_SU2): exit 0, 17 pages. The only undefined items are thm:main and 3 citations, which are external to both files. |

## 2. Hypotheses and where they are stated

- **H1.** G is a compact Lie group with dim G ≥ 1, not necessarily connected. Stated in THEOREM_B_GENERAL.md §1 and general.tex, first paragraph.
  - Compactness is used for Vol < ∞, η_* > 0, η(δ) > 0 and the existence of limit states.
  - dim ≥ 1 is used for Var X₀ ≥ d/8 > 0 and for Var_μ > 0.
- **H2.** ρ is a faithful continuous unitary representation of dimension N_ρ. Same places as H1. If ρ is not faithful, replace G by ρ(G); the condition is then dim ρ(G) ≥ 1. Faithfulness is used for:
  - positive definiteness of ⟨,⟩_ρ;
  - the zero set;
  - injectivity of exp on {‖dρX‖ < π};
  - η_* > 0.
- **H3.** d = 4; boxes of side 2^k; states are weak limit points; "m → 0" includes m = 0. These come from sec_proof_SU2.tex lines 5–8 and are unchanged.
- **Statement-by-statement use.** The table in THEOREM_B_GENERAL.md §4 lists, for each paper statement, whether it carries over verbatim, needs a change, needs a new argument, or fails.

## 3. Failed predicates

- **My programs:** none. A first LaTeX wrapper put `\input` of preamble.tex, which contains `\documentclass`, inside a file. It errored; this was my own wrapper mistake, not a defect of the target. I fixed it by concatenating the preamble.
- **Child T37:** P4 failed. Direct SU(3) MC had zero counts at s < 0.05; this was the child's own expectation, not a target defect, and the child kept it. Its replacement P4b was declared after P4 failed (post hoc). P4b passed, and my rerun reproduced it.

## 4. What I did not check

- **The Z₂ gap and the U(1) Coulomb phase** (literature, cited).
- **The standard Riemannian and Lie facts.** These are Hopf–Rinow with bi-invariant geodesics, and the Haar density det((1−e^{−ad X})/ad X)/Vol. Both are cited.
- **The SU(2) paper beyond what carries over.** In particular I did not recompute λ_N, K_N or G(n).
- **Explicit values** of η_* and D*_G for any group.
- **Matrix-level statements in Lean.** Only scalar inequalities are formalised; the matrix-level ones (B4–B7) are checked numerically only.
- **Other test groups.** Box MC covered only R₁ with a fixed shell. There was no MC for O(2) or other disconnected groups; the claim that connectedness is not needed rests on the proof alone.
- **The O(1/β) size at β = 300.** The 3% allowance is an assumption. The observed deviations are ≤ 0.3%.

## 5. Delegated questions and outcomes

- **T37 (child, sonnet, parent T36).**
  - Question: test (i), ball-volume scaling (A) and Hessian form (B) for SU(3) fundamental and for U(1), by Monte Carlo over Haar measure.
  - Control: dim SU(3). The child answered 8, which is correct; I graded this first.
  - Outcome: A and B STAND. It found c = 9√3/(8π), which matches my formula ω_d 2^{d/2}/Vol_ρ.
  - Task handling: admitted (graph seq 74) and released by me (seq 85). The run was recorded as child-run1 (K1, exit 0).
- **T39 (grandchild, parent T37, admitted and released by the child).**
  - Question: an independent deterministic computation of the SU(3) constant c.
  - Control: U(1) V/√s vs √2/π.
  - Outcome: c = 0.620245. My rerun in rerun_child/gc gave the identical value (K4).
- **Reruns of child output.** t37b rerun (K5): PASS, with identical counts and z-values.

## 6. Commands to rerun

```
cd /home/user/z4-workers/d1-Bgen
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos; G=/home/user/z4-work/graph/attempt.jsonl
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"          # control 0.272341
$P init pcp --principal principal --principal-name "Kirtus Justus"
$R task-admit $G --by principal --label d1-Bgen-child --parent T36        # gave T37
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T37
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
rm -f box_mc_results.txt ball_check_results.txt     # result files are opened with mode "x"
$P check --ws pcp --name box-mc --expect-exit 0 -- python3 box_mc.py
$P check --ws pcp --name ball-check --expect-exit 0 -- python3 ball_check.py
rm -f rerun_child/gc/result.md; $P check --ws pcp --name rerun-grandchild-su3 --cwd rerun_child/gc --expect-exit 0 -- python3 su3.py
$P check --ws pcp --name rerun-child-t37b --cwd rerun_child --expect-exit 0 -- bash -c "python3 t37b.py > t37b_rerun.out 2>&1"
$P check --ws pcp --name lean-genscalar --expect-exit 0 -- bash -c "cd /home/user/z4-lean && PATH=\$HOME/.elan/bin:\$PATH lake env lean /home/user/z4-workers/d1-Bgen/lean/GenScalar.lean"
$P check --ws pcp --name latex-general --cwd texbuild --expect-exit 0 -- bash -c "pdflatex -interaction=nonstopmode g2.tex >/dev/null && pdflatex -interaction=nonstopmode g1.tex > /dev/null && grep -a 'Output written' g1.log g2.log"
$P verify --ws pcp
$R verify pcp/register.jsonl
```

Last lines of the verify commands:
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Counts: 26 met, 0 failed, 2 measured only (SU(3) at β = 75 and β = 1200). Child: 12 met, 1 failed, slopes and c measured only.

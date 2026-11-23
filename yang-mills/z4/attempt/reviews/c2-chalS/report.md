# c2-chalS report: challenge of THEOREM_S.md (task T14)

Worker c2-chalS (challenger) for Director Z4. Principal: Kirtus Justus. Control: `control.txt` = 0.272341 (−ln tanh 1). I share a model family with the builder and the director, so this is not independent review.

**Plain verdict.** As a statement, Theorem S is a correct conditional theorem: I found no false conclusion, no vacuity and no missing hypothesis that the statement needs. **The first step that fails as written is step 8.** It asserts F^β(t+s) ≤ e^{−s} F^β(t) and writes T_β = e^{−H_β}, and both need the transfer matrix to be **positive** (T_β ≥ 0). H0 lists only site-plane reflection positivity. That makes T_β self-adjoint with T_β² ≥ 0, but not T_β ≥ 0. A concrete site-RP chain whose transfer matrix has a negative eigenvalue breaks the inequality 3 times out of 6 (`t_pos2.out`).

**Smallest repair** (either one works, and the statement is unchanged):
- (a) Replace the monotone inequality by |F^β(s)| ≤ e^{−s} F^β(0). This holds for any self-adjoint T with ‖T|_{Ω⊥}‖ = e^{−m}, and the limit argument then goes through verbatim (if ν_Ψ([0,1−ε]) = c > 0, then F(s) ≥ c e^{−(1−ε)s} contradicts |F(s)| ≤ e^{−s}F(0)).
- (b) Add link-plane reflection positivity to H0. This is true for the Wilson action (Osterwalder–Seiler; T ≥ 0 by Lüscher 1977). Both of those are CLAIMED from memory and not read.

## 1. Verdict table

| # | Item | Verdict | Evidence (one line) |
|---|---|---|---|
| 1 | A1(i) E0′ growth with factorial σ_n | STANDS | The (k!)^b factor is in H3(b) itself, not missing. The step-2 Taylor lemma (M = Dk+1, P = 4k+1) gives a fixed s = D+6, as KQR eq. (9.18) requires (∀ f ∈ ⁰S(R^{dn}), σ_n ≤ α(n!)^β). |
| 2 | A1(ii) Limit is a distribution on ⁰S, and convergence S^β(f) → S(f) | STANDS | Uniform convergence on δ-separated compacta (H3(b,c) and Arzelà–Ascoli), plus the extra factor ρ_min from the M = Dk+1 Taylor order, which makes the near-diagonal remainder ≤ Cδ uniformly in β. |
| 3 | A1(iii) closure⟨W₄, R_θ⟩ = O(4) | STANDS | Kronecker, then conjugation into all six planes, then the six generators span so(4) (rank 6), SO(4) is connected, and det −1 ∈ W₄. Child T15 and grandchild T16, rerun by me (K4, K5, byte-identical). Five Haar elements approximated to Frobenius error ≤ 2.5·10⁻⁴. |
| 4 | A1(iii) Nearest-point rounding in H4 is enough | STANDS | Rounding moves points by ≤ a; H3(c) makes that cost L_{k,δ}·O(a) → 0. Invariance of the continuous S then follows because 𝒢 is closed. |
| 5 | A1(iv) RP passage to the limit | STANDS | f ∈ ⁰S₊ ⇒ only sites with t ≥ a. Site-scalar fields at n₀ ≥ 1 use links in t ≥ 0, and links in the plane are allowed by site RP. ΘÔ(n) = Ô(θn) exactly. Positivity of the finite quadratic form survives limits. |
| 6 | A1(v) / E4 cluster, unique vacuum | STANDS | No uniform lattice clustering of products is needed; the gap passes through the spectral inequality. Step 11's vectors with equal-time or unordered supports are a fillable gap: S is continuous off coincidence, so cut-offs converge by dominated convergence. E4 also follows from the unique vacuum (step 9). |
| 7 | A2 step 8 (gap ≥ 1) | **DEFECT** (proof step, not statement) | Uses T_β ≥ 0, which is not in H0. Antiferromagnetic Ising chain: site RP holds (min eig −1·10⁻¹⁷), eigenvalue −1.042, F(t+1) ≤ e^{−m}F(t) fails for t = 1, 3, 5. The repaired form holds 11 of 11 (`t_pos2.out`). |
| 8 | A2 nontriviality S_ii(0, e₀) = 1 and Ψ_f ≠ 0 | STANDS | S^β_ii(0, aN e₀) = 1 exactly, \|aN−1\| ≤ 2a, H3(c). ‖Ψ_f‖² ≈ \|∫f\|²·S(−e₀/2, e₀/2) > 0. Gap "≥ 1" (not "= 1") is all that is claimed. |
| 9 | A3 other hidden hypotheses | STANDS | μ_β is only chosen, and m > 0 forces a unique vacuum in its own OS space. Z_i is per field, mixed terms are bounded by H3(b). Fields are real and θ-even by construction. a → 0 is used only for translations, rounding and aN → 1. Boundedness is used only for L² convergence in step 6. |
| 10 | A4 free-field numbers | STANDS | My own program (numpy, Bessel–Schwinger representation). Gap 2 asinh(m/2) to 10⁻¹⁵ (12 of 12). sup\|x\|²S = 1.636, 2.001, 2.114, 2.149, reproducing the author's values. Limit vs K₁(\|x\|)/(\|x\|K₁(1)) ≤ 2.3·10⁻³ at m = 1/32 (6 of 6 points, on and off axis). a⁻²G vs K₁/(4π²\|x\|) ≤ 1.4·10⁻³. Rotation differences match P5. |
| 11 | A4 :φ²: and \|x\|^{−4} | STANDS | Not integrable against general S, but the theorem uses only ⁰S, where it is harmless. H3(b) holds with D = 2: sup\|x\|⁴S_{φ²} ≤ 4.62. |
| 12 | A4/§6 "Theorem S is not mis-stated on this test" | **DEFECT** (wording) | The free field is outside the theorem's setting: fields are unbounded, there is no SU(2), and boundedness is used in step 6. It tests an analogue, so the sentence needs "for the analogue with moment bounds replacing boundedness". |
| 13 | A5 discriminators (U(1), 4D Ising, 2D Ising) | NOT CHECKED | Only from memory: 2D near-critical Ising, i.e. Camia–Garban–Newman, Chelkak–Hongler–Izyurov, Park, Chelkak–Izyurov–Mahfouf. None was read. Which of H3(b) (with factorial growth) and H4 is a theorem there is not established by me. |
| 14 | A6 (E1)-as-suggested is too weak | STANDS | Truncated 4-point of :φ²: = 16·Σ(3 cycles) > 0 because G > 0. Monte Carlo agrees: 1.54·10⁻⁵ ± 2.1·10⁻⁶ vs Wick 1.60·10⁻⁵ (`ff_q7.out`). |
| 15 | A7 status lines | **DEFECT** | THE LIST says H3 is "Proved for the free field", but §6 rests H3(b) on a CLAIMED bound G_m(n) ≤ C/\|n\|². §6's table says H0 "holds" while tagging it CLAIMED. Step 8 is tagged PROVED despite item 7. The "Relation to attempt 1" constant 2αγ² needs b ≤ 1 (in general it is 2^b αγ²). |
| 16 | Joint satisfiability in the theorem's own setting (SU(2)) | NOT CHECKED | It is open, since it is the problem itself. I found no obstruction: bounded fields with Z → 0 are compatible with H3(b) when the field dimension is ≤ D. |
| 17 | OS source as cited | STANDS (at CITED-2nd level) | KQR arXiv:2104.02090 read via pdftotext (text kept outside this directory): eq. (9.18) as the author states it, Lemma 8.8 of OS 1973 wrong (§9.2.1), footnote 20 (E4 = cluster of [2]). The OS 1973 and 1975 originals were not read by me either. |

**Verdict counts: 12 STANDS, 3 DEFECT, 2 NOT CHECKED.**

## 2. Hypotheses each statement uses (and where stated)

- **Setting (§1):** μ_β is chosen from 𝓛_β; fields are bounded, real, gauge-invariant and W₄-site-scalar; a = m; N = 2⌊ξ/2⌋; Z_i normalization; ⁰S, ⁰S₊ (KQR eq. 2.25).
- **Step 1:** H3(b), H3(c).
- **Step 2:** H3(b) (including the (k!)^b factor), step 1.
- **Step 3:** H0 (translations), H2 (a → 0), H3(c).
- **Step 4:** H0 (W₄), H4, H3(c), group closure (item 3).
- **Step 5:** reality and commutativity (setting).
- **Step 6:** H0 (site RP), site-scalarity, boundedness (setting), step 2.
- **Step 7:** OS II (CITED-2nd).
- **Step 8:** H1, a = m, steps 2 and 6, and **T_β ≥ 0 (UNLISTED; item 7)**.
- **Steps 9–11:** step 8, step 4, OS reconstruction (Poincaré covariance, spectrum condition).
- **Step 12:** H3(a), H3(c), normalization.

## 3. Failed predicates

| Program | Predicate | Whose failure |
|---|---|---|
| `ff_check.py` | Q3 "error decreases 1/8 → 1/32 at each point" | **Mine.** It failed only at x = e₀, where the error is identically 0 (the normalization point). All 6 accuracy clauses were met. |
| `ff_q7.py` | R1 "Wick value ≥ 20 Monte Carlo s.e." | **Mine** (sample size too small; ratio 7.6). R2 agreement was still met. |
| `t_pos2.py` | T2, the monotone step-8 inequality under site RP | **Target defect** (item 7), expected before running. Holds in 3 of 6 cases. |
| `t_pos.py` (run K6) | crashed, exit 1 | **Mine** (numpy bool indexing). Partial output kept as `t_pos.run1_failed.out`; fixed copy is `t_pos2.py`. |

Counts (met, failed, measured only):
- My programs: 12 met, 3 failed, 0 measured only. ff_check met Q0, Q1, Q2, Q4, Q5, Q6, Q7 and failed Q3. ff_q7 met R2, R3 and failed R1. t_pos2 met T1, T3, T4 and failed T2.
- ff_check's Q7 was met but uninformative (Wick 5.7·10⁻¹¹ ≪ s.e. 1.5·10⁻⁶), which is why I redid it in ff_q7.
- Child, rerun by me: 5 met (control, P1–P4), 0 failed, 1 measured only (the θ = 1 group-size contrast, > 20000 at the cap).

"For all" predicates were tested per case:
- Q1: 12 of 12.
- Q3 accuracy: 6 of 6.
- Q4: 6 of 6.
- T2: 3 of 6.
- T3: 11 of 11.
- Child P3: 5 of 5.

Tolerance sources are stated in each program's docstring.

## 4. What I did not check

- The OS 1973 and 1975 originals. The OS II proof itself, including whether E0′ in the original is stated on ⁰S or ⁰S₊.
- THEOREM_B (H0, H2 for SU(2)).
- A5's literature (2D Ising, 4D Ising, U(1)).
- Lüscher and Osterwalder–Seiler on T ≥ 0 for Wilson (memory only).
- Lean: not used. /home/user/z4-lean/READY exists, and no Lean result is claimed.
- The Taylor lemma's constants in step 2 were checked by reading, not by program.
- Step 11 was checked by argument only.

## 5. Delegated questions and outcomes

**Child T15** (`c2-chalS-child`, parent T14; admitted ADMITTED T15, released by me after the rerun).
- Question: is closure⟨W₄, R_1rad⟩ = O(4)? Proof sketch plus a numerical check.
- Control: dim SO(4). Answer 6, **correct** (graded first).
- Returned: YES. The proof sketch is correct, and five Haar elements were approximated to Frobenius error 6·10⁻⁵ to 2.5·10⁻⁴ with n ≤ 10⁵. The child's first run crashed on its own JSON bug, and the partial output was kept.
- I reread `check.py` and reran it (K4): identical JSON.

**Grandchild T16** (`c2-chalS-grandchild`, parent T15; the graph shows it admitted at seq 32 and released at seq 35).
- Question: the rank of the six E_ij − E_ji, and the boundary case θ = π/2.
- Control: rank I₃ = 3, correct.
- Returned: rank 6. θ = π/2 gives 384 = |W₄|, which is trivial since R_{π/2} ∈ W₄. θ = 1 gives > 20000 elements at the cap, which is only consistent with an infinite group.
- I reran `tasks.py` (K5): identical results.

**Web sub-agent** (not a PCP task): fetched KQR. I then read §9 myself from the PDF text.

## 6. Rerun commands (from /home/user/z4-workers/c2-chalS)

Each program opens its output with mode "x", so delete or rename the output first.

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name ff_check --expect-exit 0 -- python3 ff_check.py          # -> ff_check.out (K2)
$P check --ws pcp --name ff_q7 --expect-exit 0 -- python3 ff_q7.py                # -> ff_q7.out (K3)
$P check --ws pcp --name t_pos2 --expect-exit 0 -- python3 t_pos2.py              # -> t_pos2.out (K7)
$P check --ws pcp --name rerun-child-check --cwd rerun_child --expect-exit 0 -- python3 check.py          # K4
$P check --ws pcp --name rerun-grandchild --cwd rerun_child/gc --expect-exit 0 -- bash -c "python3 tasks.py >/dev/null"   # K5
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"   # K1
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Last lines of the verify commands:
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

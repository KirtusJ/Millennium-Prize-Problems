# e2-chalrun (T48): challenge of RUNNING.md (worker d1-run, T38)

Control: `control.txt` = 0.272341 (−ln tanh 1). Lean was ready (`/home/user/z4-lean/READY` exists) but I did not use it. No Lean claim is made.

## 1. Verdict table

| # | item | verdict | one line of evidence |
|---|---|---|---|
| 1 | Theorem 1 (fixed-R expansion, remainder sup_J\|∂_η r\| ≤ C(R)/β), as written | **DEFECT** (proof gap; the result is very likely true) | Step 5 says "two asymptotic expansions of the same smooth function agree term by term", but Z and ∂_ηZ are different functions. Uniformity of the remainder under ∂_η is asserted, not shown. The standard repair (joint smoothness in (η, β^{-1/2}) after rescaling ξ = y/√β) is not in the file. |
| 2 | Theorem 1, hypotheses: SU(2), R ≥ 4 | STANDS as a citation; Appendix B is unread by the builder and by me | Source (arXiv HTML) gives Theorem 1 in §5.2 with proof in App. B; per the extraction the condition TL/a² > (N−1)π² max(1, N/16) gives R ≥ 4 for SU(2). The builder's "eq. (5.11)" was not found. |
| 3 | Theorem 1 heading "both hold for SU(2), R ∈ {4,…,16}" | **DEFECT** (scope) | Lemma N is shown only for the listed R (4, 8, 16 quoted; table R) and only at η = π/4, not on an interval J. R = 7, 9, 11, 13–15 are not shown. |
| 4 | Theorem 1 for U(1) | **DEFECT** (not proved) | Hypothesis U for U(1) is only CLAIMED in the file (§2). The summary still says "PROVED … for every compact connected G" while the theorem fixes G ∈ {SU(2), U(1)}. |
| 5 | One-loop formula Γ1 = ½ log det(H + DD†) − log det(D†D), with ghosts and the boundary torus generator | STANDS | My own construction (exact per-plaquette Hessian, Ad_V in D, torus column at p = 0) reproduces every table value to ≤ 5e-7 (6-digit rows) and ≤ 2e-9 (8-digit rows). Dense full-lattice construction equals the Fourier construction to < 2e-12 (R = 2, 3). |
| 6 | Haar and Faddeev–Popov at order g0⁴ | STANDS | det(D†D) depends on η for SU(2) through Ad_V and is included; Haar 1 + O(X²) and vol(𝒢) enter only at O(1/β) or as constants. My numbers including ghosts match the table, so the inclusion is the same as LNWW's. |
| 7 | U(1) formula c1 = tr[A⁻¹H_t]/(2N_t) | STANDS | The trace formula equals −Γ1′/k to ≤ 5e-9 for R = 2..12 (K10; child K6). H_t must be the η-independent Maxwell form; my first run used cos θ·H_t (own defect, see §3). |
| 8 | U(1) bound 0 < c1 ≤ 1/(2cos(π/(2R²))) "for every R" | **DEFECT** (gap, repairable) | The upper bound uses rank H = n − m, i.e. Lemma N, which the file only computes for the listed R. A proof for all R is short (H ≥ cos θ·Maxwell; the kernel of the lattice Maxwell form with these boundary conditions is range D plus the torus, by H¹(M,∂M) = ℝ), but it is not in the file. The bound proves boundedness only, not convergence. It is a bound on the formula; as a statement about g2 it also needs item 4. |
| 9 | U(1) limit 1/4 | STANDS as CLAIMED (not proved) | Data give 1/4 − c1 ≈ 0.071/R (R = 8: 0.00888·8; R = 12: 0.00594·12). The bulk Feynman-gauge counting gives 1/d. |
| 10 | U(1) table R = 2..8 (+10, 12) | STANDS | Mine (K10, FD + trace): 0.2287515, 0.2293161, 0.2330566, 0.2360589, 0.2382528, [R=7 0.2398783], 0.2411188, 0.2428761, 0.2440566, [R=16 0.2455386 vs 0.245539]; the child's independent code (T51) gives the same to 1e-9. |
| 11 | SU(2) table R = 2..6 (and 8, 10, 12, 16) | STANDS | Mine: 0.2264033, 0.2817967, 0.3130122, 0.3355659, 0.3542203018, 0.3837042883, 0.4064416741, 0.4248310666, 0.4534774457 against 0.226403, 0.281797, 0.313012, 0.335656, 0.35422030, 0.38370429, 0.40644167, 0.42483107, 0.45347745. |
| 12 | Agreement with LNWW Table 1 | STANDS (partial source check) | The arXiv HTML extraction of Table 1 (§7.5) gives L/a = 6..16 values equal to the file's. L/a = 4, 5 are absent. The extraction is not verbatim and the page is not located. The c_t used for Table 1 was NOT FOUND; agreement with c_t = 1 numbers suggests c_t = 1. |
| 13 | 2b0 ln 2 = 0.064378; Δ_SU2 "close to" it | STANDS numerically / **DEFECT** in attribution | Δ/(2b0 ln 2) = 1.345, 1.125, 1.098, 1.100, 1.097, 1.084 (R = 4..16). The sequence is non-monotone at R = 10. Two-point a + b/R extrapolations give 0.067–0.069. The file's "excess is r1/L" predicts 2b0 ln2 − r1/R = 0.0779 (R = 8), 0.0712 (R = 16) against 0.0707, 0.0698 observed, so higher-order terms matter. The trend alone does not show convergence to 0.0644; that is CITED from LNWW's extrapolation. |
| 14 | U(1) "differences small and decreasing" (§6) | **DEFECT** (minor, wording) | Δ_U1 = 0.0043 (R = 4), 0.0089 (R = 6), 0.0081, 0.0068, 0.0058, 0.0044: it increases from R = 4 to 6 and decreases only from R = 6 on. |
| 15 | "SU(2) and U(1) differ with a definite sign" / "what is new" (§8) | **DEFECT** | Δ_U1 > 0 too, so both have the same sign. At R = 2, c1(SU(2)) = 0.2264 < c1(U(1)) = 0.2288. The real computed difference is in magnitude (Δ_SU2 − Δ_U1 = 0.082, 0.064, 0.063, 0.064, 0.065, 0.065). The SU(2) numbers are LNWW's 1992 m1 and the U(1) tadpole constant is textbook, so nothing here is first. |
| 16 | Scope: "nothing at fixed β", remainder O_R, no R-uniformity | STANDS | Stated in the summary (bold), Thm 1 step 3 and §8. No fixed-β consequence is claimed. |
| 17 | d = 3 SU(2) values | STANDS (R = 4..16); R = 24 NOT CHECKED | Mine: 0.666685, 0.953044, 1.235642, 1.796349, 2.354139, equal to the file's. "c1/R settles" is not shown: c1/R = 0.1667, 0.1588, 0.1545, 0.1497, 0.1471 is still falling. |
| 18 | d = 5 | NOT CHECKED in the file; measured only by me | SU(2) R = 2, 3, 4: 0.165846, 0.190818, 0.199939. The increments shrink, but R ≤ 4 says nothing about boundedness. |
| 19 | Finite group: no expansion | STANDS | Trivial: no continuous η family; Z is a finite sum. |
| 20 | Periodic torus (torons) | STANDS as argument; citations secondhand | The builder did not read refs [59], [60]. |

Verdict counts: STANDS 13, DEFECT 7 (items 1, 3, 4, 8, 13, 14, 15; item 13 is a split verdict, counted here as DEFECT), NOT CHECKED 0. Items 17 and 18 contain sub-parts I did not check (d = 3 R = 24, the d = 5 claim).

**Plainly:**
- **Fixed-R expansion theorem.** It is not proved as stated. The η-derivative step is hand-waved, Lemma N is numerical at listed R and η = π/4, and U(1) uniqueness is unproved. For SU(2), R ≥ 4, the statement is standard and I expect it to be true.
- **U(1) bound.** It is proved for the finite-dimensional formula at the R where Lemma N was computed. "For every R" needs a short argument the file lacks. It proves boundedness, not convergence to 1/4.
- **SU(2) numbers.** They are right; I reproduced them independently to 8 digits.
- **Cited without having been read:**
  - LNWW Appendix B (the proof of Theorem 1);
  - Hörmander Thm 7.7.5 (from memory);
  - the Morse–Bott slice (no source);
  - toron refs [59], [60];
  - Balaban (no locator);
  - the 11/3 = 4 − 1/3 decomposition;
  - LNWW's numerical extrapolation (eqs. 7.37–7.41), which only confirms s0 numerically.

## 2. Hypotheses used and where they are stated

- **Hypothesis U** (unique minimum mod 𝒢): RUNNING.md §2. SU(2), R ≥ 4: cited from LNWW §5.2, Thm 1. U(1): CLAIMED. R = 2, 3: local minimality only.
- **Lemma F** (free action of 𝒢, with Ω(0) = 1 and a constant torus at x0 = T): §2, proved. My construction uses the same 𝒢 and matches LNWW. Per the source fetch, LNWW's lattice gauge transformations are fixed at x0 = T (eq. 4.5), and they say in §3.3 that zero modes are "not discussed"; the builder's remark there is confirmed.
- **Lemma N** (H + DD† > 0): §2. It is computed at η = π/4 for the listed R only. Thm 1 needs it on an interval J; continuity gives some J.
- **Laplace with parameters** (Hörmander 7.7.5): §2 and Thm 1 step 3, cited from memory.
- **Uniform η-differentiability of the remainder:** Thm 1 step 5; the argument is a gap (item 1).
- **Thm 2** uses Lemma N for all R (rank H = n − m) and Hypothesis U(U(1)) for its meaning.
- **"For all p" predicates (rule 4):** H(p)D(p) = 0, Hermiticity and A(p) > 0 were tested per momentum block. All blocks qualified: R³ of R³ for every R run (8 … 1728, 4096 of 4096 at R = 16). In the child run the counts were 8/8 … 512/512.

## 3. Failed predicates (kept)

- **Q8, K3 (U(1), R = 2..8): 7 failed.** I compared the trace formula using the background Hessian of timelike plaquettes, which is cos θ · H_t, instead of the Maxwell H_t. This was **my own defect**. Divided by cos θ, it agrees to 5e-11 (v2 run K10: 7/7 met).
- **Q5, K11 (SU(2), d = 3): 5 failed.** The finite-difference spread was 2e-7..9e-7 against an absolute tolerance of 1e-7. I set that tolerance for c1 ~ 0.3 and |k| ~ 10–40; in d = 3, c1 ~ 1–2 and |k| ~ 1.6–6, so the error is amplified. This was **my own expectation**, not a target defect; the relative spread is ~4e-7.
- **K5: 1 failed run.** My rerun of the child's program exited 1 because I did not copy its control.txt; my setup error. It was redone as K6.
- **Target defects found by predicates:** none. Every comparison predicate (Q6, Q7) was met.
- **Q8, K14 (U(1), R = 16): 1 failed.** The finite-difference and trace values differ by 1.4e-7 against a tolerance of 1e-7. Roundoff from summing 4096 blocks of log det grows with R. This was **my own tolerance**; both values agree with the table's 0.245539 to 5e-7.
- **Counts (met, failed, measured only)**, over my own runs K1–K3 and K7–K12, K14 and K15:
  - met: 212;
  - failed: 13 (8 Q8, of which 7 were my own defect and 1 my own tolerance; 5 Q5, my own tolerance), plus 1 failed rerun (K5);
  - measured only: 10 (d = 5 × 3, U(1) R = 7, d = 3 c1/R trend, Lemma N minimum eigenvalues ×4, Δ ratios).
- **R = 10–16 runs:** K15 (SU(2)) met all predicates. K14 (U(1)) exited 1 because of the single Q8 failure above.

## 4. Not checked

- LNWW Appendix B (Theorem 1 proof), and the verbatim text of Table 1 and §7 (the source fetch was an extraction).
- The c_t used in LNWW Table 1.
- Hörmander 7.7.5.
- U(1) Hypothesis U (only sketched by me: a flux argument).
- d = 3 R = 24.
- The d = 5 boundedness claim.
- Lemma N on an η-interval (I checked only η = π/4 ± 2e-3, the finite-difference points).
- The builder's child T40 result: c1(4) = 0.312997 there, against 0.313012 in the table, differing by 1.5e-5. My value of 0.3130122 supports the table, not T40.

## 5. Delegated questions and outcomes

- **Child T51** (admitted under T48; released). The question was A2: c1(R; U(1)), R = 2..8, from the definitions.
  - Control 1/(2cos(π/8)) = 0.541196 was graded first: **correct**.
  - It returned 0.228751482, 0.229316113, 0.233056564, 0.236058883, 0.238252786, 0.239878349, 0.241118838. These were computed two ways (trace formula and finite-difference log det), with all per-block hypotheses met.
  - I reread its program (abelian Hessian Σ cos θ_p b_p b_pᵀ, D independent of η) and reran it under my register (K6). The output was byte-identical to its results.txt, and it agrees with mine to 1e-9.
  - Deviation: it deleted one scratch results.txt from a smoke run (it reports this).
- **Grandchild T52** (admitted by the child under T51, released by it). The question was an independent dense real-space recomputation of R = 2 U(1) with a finite-difference Hessian check.
  - Control cos(π/3) = 0.500000: correct.
  - It returned c1 = 0.2287515. I reran it under my register (K13) and got the same: 0.228751482.
- **Web-fetch sub-agent** (not a PCP worker; a source check only): arXiv hep-lat/9207009. Its findings are reported in items 2, 12 and §2 above.

## 6. Rerun commands

```
cd /home/user/z4-workers/e2-chalrun
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
# result files are opened with mode "x": move results/ aside first
$P check --ws pcp --name su2-d4-R2      --expect-exit 0 -- python3 c1chk.py su2 4 2
$P check --ws pcp --name su2-d4-R3-8    --expect-exit 0 -- python3 c1chk.py su2 4 3 4 5 6 8
$P check --ws pcp --name u1-d4-v2       --expect-exit 0 -- python3 c1chk.py u1 4 2 3 4 5 6 7 8
$P check --ws pcp --name dense-su2-R2   --expect-exit 0 -- python3 c1chk.py dense su2 4 2
$P check --ws pcp --name dense-su2-R3   --expect-exit 0 -- python3 c1chk.py dense su2 4 3
$P check --ws pcp --name dense-u1-R3    --expect-exit 0 -- python3 c1chk.py dense u1 4 3
$P check --ws pcp --name su2-d3         --expect-exit 0 -- python3 c1chk.py su2 3 4 6 8 12 16
$P check --ws pcp --name su2-d5         --expect-exit 0 -- python3 c1chk.py su2 5 2 3 4
$P check --ws pcp --name su2-d4-R10-16  --expect-exit 0 -- python3 c1chk.py su2 4 10 12 16
$P check --ws pcp --name u1-d4-R10-16   --expect-exit 0 -- python3 c1chk.py u1 4 10 12 16
$P check --ws pcp --name child-rerun-u1-b --cwd child_rerun2 --expect-exit 0 -- python3 c1_sf.py 2 3 4 5 6 7 8
$P check --ws pcp --name grandchild-rerun --cwd gc_rerun --expect-exit 0 -- python3 c1.py
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

The child itself was run with `$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"` (K2, exit 0). The task graph steps were `pcpos task-admit … --label e2-chalrun-child --parent T48` (→ T51) and `pcpos task-release … --id T51`.

## 7. Register verification
- `$P verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

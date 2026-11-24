# d2-time report (T226): does the slow local mode at −I persist in physical time?

I share a model family with the director, so my agreement is not independent review. The child (T227, Sonnet) recomputed the two headline numbers with its own code, but with the formulas my prompt prescribed. It therefore checks my code, not my method. Raw moments are in `results/<tag>/s<i>.mom.txt`. The step-by-step record is `notes.md`, the rerun commands are in `REPLAY.md`, and the sampler diff is `z1mx5.diff`. Lean was ready (/home/user/z4-lean/READY exists), but I did not use it, and I make no Lean claim.

**Answer (rule fixed in the `prodt.py` docstring before any production run):** the slow local mode **does not** persist in physical time.
- **Both definitions:** for w_L4 at −I, R²_held(1) = −0.0133(21) with Y^loc and −0.0023(18) with Y^tr. Both are below 0.02, with standard error below 0.01.
- **"Persists" clause is far from met:** −I exceeds clear by 0.0060(26) (loc, z 2.3) and 0.0121(28) (tr, z 4.3), but R²(−I) is nowhere near 0.1.
- **Caveat on the "does not" clause:** with 308 predictors, the held-out R² has a negative over-fitting floor of about −0.017. On the same ensemble at t = 3, where ρ ≈ 0, it is −0.016 (loc) and −0.019 (tr). So "< 0.02" would also be met by a true R² of up to about 0.03.
- **What the sharper numbers show:** a small, real, −I-specific carry-over to t = 1 in the **transported** definition.
  - ρ_w(1): .0834(56) at −I against .0321(50) on clear (z 6.9).
  - The 15-predictor held-out R² (L1 marks of Y only): .0113(17) against −.0005(6).
  - Its size is R² ≈ 0.01, ten times below the "persists" threshold, and it is gone by t = 2.

## Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| Control −ln tanh 1 | STANDS | control.txt = 0.272341 |
| z1mx5 is a pure extension: old outputs byte-identical (T-P0b) | STANDS | K5: all 5 files × 3 cases byte-identical to z1mx4. First test K4 failed on .meta.txt only, because my test gave different output prefixes. |
| Time mode runs the same chain (T-P3, T-P4) | STANDS | X.csv in time mode byte-identical to fixed mode (3/3). Series m_j = w_j·X to ≤ 5.1e-11. |
| Y marks gauge invariant (T-P1); Y(0) reproduces X (T-P2) | STANDS | Random full gauge transform, all 2464 Y values at t = 1, 2, 3, −1: ≤ 3.4e-15 (K3, K14). Y^loc(0) = Y^tr(0) = X exactly. |
| Clear weights = prior G-clear0 optimum (RP1) | STANDS | Reproduction F-clear0: L4 train .0409724 / held .0428277, against prior .04097 / .04283; L1 likewise (K8). |
| Thermalisation and symmetry checks, both runs (M1, M2, A4, A7, S1) | STANDS | 40 of 40 met. Hot/cold, burn-in halves, and t = 1 vs t = −1 for every ρ and R² agree (\|z\| ≤ 2.13). |
| **"The slow local mode persists in physical time"** (brief's rule, w_L4, t = 1) | **DEFECT (does not)** | R²_held(1) at −I: loc −.0133(21), tr −.0023(18); both < .02 with se < .01. The rule's "persists" needs > 0.1. |
| −I-specific carry-over at t = 1, transported definition | STANDS (measured; small) | ρ_wL4(1) tr: −I .0834(56) against clear .0321(50), z 6.9. L1-Y held R²: .0113(17) against −.0005(6). At t = 2: ρ .016(6) and R²_held < 0. |
| −I-specific carry-over at t = 1, local-reference definition | NOT CHECKED (not resolved) | ρ_wL4(1) loc .0224(40) against clear −.0031(60), z 3.5. R²_held difference z 2.3. f4 shows nothing (ρ −.0023(57)). No predicate was fixed for this. |
| Child's independent recomputation of ρ_w(1) and R²_held(1) (T227) | STANDS | Its values equal mine at every printed digit. My rerun of its code agrees to ≤ 7e-16 but is not byte-identical (BLAS thread count). |
| Unconditioned measure, gated three-face sector | NOT CHECKED | Outside this brief (prior record: too rare). |

**Verdict counts:** 8 STANDS, 1 DEFECT, 2 NOT CHECKED.

## Numbers (all 32 streams for ρ; train 0–15 / held 16–31 for R²; jackknife se)

**−I skeleton (T-d0, fresh seeds 21100001 + 7919 i; weights = prior w_L4, w_L1, f4):**

| t | def | ρ_wL4 | R²_held wL4 | R²_train | ρ_wL1 | R²_held wL1 | ρ_f4 | R²_held f4 | R²_held wL4, L1-Y only |
|---|---|---|---|---|---|---|---|---|---|
| 1 | loc | .0224(40) | −.0133(21) | .0189 | .0238(40) | −.0129(22) | −.0023(57) | −.0171(16) | .0002(5) |
| 1 | tr | .0834(56) | −.0023(18) | .0287 | .0864(54) | −.0022(21) | .0759(53) | −.0016(27) | .0113(17) |
| 2 | loc | −.0015(51) | −.0148(21) | .0162 | −.0014(54) | −.0144(22) | −.0009(48) | −.0161(16) | −.0009(5) |
| 2 | tr | .0162(55) | −.0126(23) | .0149 | .0179(54) | −.0115(23) | .0132(45) | −.0096(18) | .0000(9) |
| 3 | loc | −.0033(52) | −.0161(16) | .0165 | −.0004(43) | −.0151(13) | −.0143(62) | −.0166(17) | −.0012(6) |
| 3 | tr | −.0029(56) | −.0189(16) | .0168 | −.0033(66) | −.0184(16) | .0066(48) | −.0183(22) | −.0016(7) |
| −1 | loc | .0206(55) | −.0165(19) | .0174 | .0222(55) | −.0138(14) | −.0090(47) | −.0188(17) | −.0011(7) |
| −1 | tr | .0741(64) | −.0042(28) | .0283 | .0805(60) | −.0057(27) | .0746(50) | −.0096(37) | .0052(19) |

**Clear skeleton (T-clear0, chain.skel0, seeds 21300001 + 7919 i; weights refitted on prior G-clear0 TRAIN):**

| t | def | ρ_wL4 | R²_held wL4 | ρ_wL1 | R²_held wL1 | ρ_f4 | R²_held f4 | R²_held wL4, L1-Y only |
|---|---|---|---|---|---|---|---|---|
| 1 | loc | −.0031(60) | −.0192(16) | .0111(63) | −.0133(17) | .0000(59) | −.0119(21) | −.0016(6) |
| 1 | tr | .0321(50) | −.0145(22) | .0351(58) | −.0102(16) | .0086(57) | −.0175(21) | −.0005(6) |
| 2 | loc / tr | −.0046(51) / .0028(63) | −.0173(26) / −.0145(23) | | | | | |
| 3 | loc / tr | .0015(51) / .0060(60) | −.0174(23) / −.0161(17) | | | | | |
| −1 | loc / tr | .0063(57) / .0293(52) | −.0193(17) / −.0182(23) | | | | | |

The full tables are in `results/T-d0/antime.txt`, `results/T-clear0/antime.txt` and `results/verdict.txt`.
- **Largest canonical correlation:** on TRAIN it is sqrt(R²_train), e.g. −I t = 1 tr: 0.169. It sits at the null level sqrt(308/18432) ≈ 0.129 plus a small excess, which is why the held-out value is the one that counts.
- **Plaquettes:** −I slice 0 .76990(5), slice 1 .75181(4). Clear: .75189(5), .75004(5).
- **τ_int(m_0):** 1.9 measurements at −I, 0.7 on clear.

## Definitions (which is which)
- **X_k (slice 0):** the prior 308 marks, unchanged (z1mx4 `mark_loops`): Re(B·L_k) with B the coarse xz holonomy at the root (frozen, = i at −I), or Re(L_k) for the 28 T marks.
- **Y^loc_k(t):** the same step list started at root_t = (0,0,0,t), so all links are free. The reference is B_t, the actual coarse xz holonomy at root_t: Re(B_t L_k(t)), or Re(L_k(t)) for T marks.
- **Y^tr_k(t):** Re(B_0 · P L_k(t) P⁻¹), where P is the product of the root's temporal links from slice 0 to slice t. P goes up for t = 1, 2, 3 and down one link for t = −1. B_0 is the frozen reference. For T marks Y^tr = Y^loc, because P drops out of the trace.
- **The vectors w:**
  - **−I:** prior_weights w_L4 and w_L1, embedded by name, and f4 = ¼ on B.xy000.g00..g11 (= the prior "average" mark).
  - **Clear:** its own L4 and L1 optimum, refitted by `fitw.py` from an exact reproduction of prior G-clear0 (RP1).
  - The production runs use fresh seeds, so the weights were not fitted on the measured streams.

## Hypotheses each statement uses and where they are stated
- **Conditioned ensemble, sampler, skeletons:** the prior record (fixed.md skeleton via `mkskel.py`; chain.skel0 via `clear.py`). z1mx5 header in `build/src/d2/z1mx5.rs`.
- **The chain does not depend on the D refresh:** the refresh uses the separate `meas` RNG and restores the links. Checked as T-P3.
- **Gauge invariance:** each Y is the trace of a product of closed loops at one base point. Checked numerically (T-P1).
- **Time-reflection symmetry about slice 0:** hypothesis, tested by S1 (12 tests per run, all |z| ≤ 2.13).
- **Independence of streams:** for the jackknife.
- **R² error:** it treats the TRAIN-fitted β as fixed, so fit variance is not included (`antime.py` docstring). The "combined se" of the rule treats −I and clear as independent, which they are (separate runs).
- **Tolerances:**
  - 1e-10 and 1e-12 (gauge, Y(0) = X): float rounding of about 20 quaternion products.
  - 1e-9 (T-P4): 12-digit printing × Σ|w|.
  - 5e-6 (RP1): half a unit of the prior printout.
  - −1e-9·trace (M1): 11-digit printing.
  - The 2·(2σ) hot/cold and burn-in factor: the prior T2 convention.
  - 3σ (S1): chosen by me for 12 simultaneous tests.
  - The 0.1, 0.02, 0.01 and 3-se thresholds of the rule: the brief.

## Failed predicates (kept)
Counts over all predicate instances (met, failed, measured only): **met 86, failed 3, measured only 69.**
- **Met (86):**
  - T-P1 and T-P2: 8 (K3, K14).
  - K4: T-P0 12, T-P3 3 and T-P4 3, 18 in all.
  - K5: T-P0b 15 and T-P4 3, 18 in all.
  - RP1: 2.
  - antime: 20 + 20, covering M1, M2, A4 ×4, A7 ×2 and S1 ×12 per run.
  - The rule's clauses (evaluated for 2 definitions): "does not" met ×2, "persists" false ×2. These are counted as outcomes, not in the 86.
- **Failed (3):** T-P0 .meta.txt in K4 (d0c, d0h, clc). This is a defect of **my test design**: the meta file records its own output prefix, and I gave the old and new runs different prefixes. Rerun with identical relative prefixes in separate directories (K5): 15/15 met. Not a defect of the target.
- **Measured only (69):** 48 table rows (24 per run), 18 −I-vs-clear differences, the child-rerun comparison, and 2 τ_int.
- **Process defects (mine, not predicates):**
  - K9 (and probably K8) let numpy use more than 1 BLAS thread, for a few seconds above the 2-core limit. Later analyses ran with OMP_NUM_THREADS=1.
  - The child's LLM session ran while fitw.py used 2 cores. The child's own numpy work lasted seconds.
  - `weights/w_d0.txt` was made by an inline Python snippet, not a saved program. Its content is described in notes.md, and T-P4 and the child's w.txt confirm it.

## What I did not check
- The unconditioned measure and the gated three-face sector.
- t > 3, and nonlinear functions of Y.
- Regularised regressions. A ridge or lasso would lower the over-fitting floor and could sharpen the "does not" (or resolve the loc carry-over).
- Fit variance in the R² error.
- Other seeds or skeletons, δ ≠ 0, and other sides or couplings.
- A predicate for the local-reference −I-vs-clear difference (z 2.3 on R², 3.5 on ρ): left as not resolved.
- Lean: not used.

## Delegated questions and outcomes
- **Child T227** (admitted under T226, `child_admit.log`; released, `child_release.log`):
  - **Question:** from the per-stream moment files of T-d0 (copied to child/data) and the prior w_L4, compute ρ_w(1) and R²_held(1) for blocks 0 (t = 1, loc) and 1 (t = 1, tr).
  - **Control:** R² of the line through (0,0), (1,1), (2,1), (3,3) = 0.852632. The child answered 0.852632: **correct**, graded before I read anything else.
  - **Outcome:**
    - b0: ρ .0224141276(40), R²_held −.0132589612(21), R²_train .0189070.
    - b1: ρ .0834114892(56), R²_held −.0023312921(18), R²_train .0286924. No directions discarded.
    - These are identical to my antime values. I reread its `analyze.py` (same pooled-moment formulas, as prescribed) and reran it in `childcheck/` (K11): all values agree to ≤ 7e-16, not byte-identical.
    - The child's own process failure: its K2, a wrong cwd for the grandchild rerun, exit 1, rerun as K3.
- **Grandchild T228** (admitted and released by the child under T227):
  - **Question:** ρ for block 0, recomputed without the full matrix, by a streaming triangle sum with fsum.
  - **Control:** 0.852632, correct.
  - **Outcome:** .022414127551879784, equal to the child's value and mine to 13 digits.

## Exact commands to rerun
Run from /home/user/z4-workers/d2-time. Result paths must not exist beforehand. Set `P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos; G=/home/user/z4-work/graph/attempt.jsonl; export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1`.
```
python3 -c "import math;print('%.6f'%(-math.log(math.tanh(1))))"
cd build && rustc --edition 2021 -O -o z1mx5 src/d2/z1mx5.rs && cd ..
$P check --ws pcp --name mkskel --expect-exit 0 -- python3 mkskel.py
$P check --ws pcp --name clear --expect-exit 0 -- python3 clear.py
$P check --ws pcp --name gauge_t_d0 --expect-exit 0 -- build/z1mx5 gauge_t 4242 6 12 skeletons/d0.txt
$P check --ws pcp --name gauge_t_clear --expect-exit 0 -- build/z1mx5 gauge_t 4243 6 12 results/gen/chain.skel0.txt
$P check --ws pcp --name ctl5 --expect-exit 0 -- python3 ctl5.py          # exit 1 expected-by-record (meta prefix)
$P check --ws pcp --name ctl5b --expect-exit 0 -- python3 ctl5b.py
$P check --ws pcp --name fitw-clear --expect-exit 0 -- python3 fitw.py
$P check --ws pcp --name prodt-d0 --expect-exit 0 -- python3 prodt.py T-d0 skeletons/d0.txt weights/w_d0.txt 21100001
$P check --ws pcp --name prodt-clear --expect-exit 0 -- python3 prodt.py T-clear0 results/gen/chain.skel0.txt weights/w_clear.txt 21300001
$P check --ws pcp --name antime-d0 --expect-exit 0 -- python3 antime.py T-d0 weights/w_d0.txt
$P check --ws pcp --name antime-clear --expect-exit 0 -- python3 antime.py T-clear0 weights/w_clear.txt
$P check --ws pcp --name verdict --expect-exit 0 -- python3 verdict.py results/verdict.txt
$R task-admit $G --by principal --label d2-time-child --parent T226      # printed T227
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T227
mkdir childcheck && cp child/analyze.py childcheck/ && ln -s ../child/data childcheck/data && $P check --ws pcp --name child-rerun --cwd childcheck --expect-exit 0 -- python3 -I analyze.py
$P verify --ws pcp
$R verify pcp/register.jsonl
```
`weights/w_d0.txt` was made by an inline script. Its rows are prior_weights/w_L4.txt, w_L1.txt embedded by name in prior_weights/names.txt order, and f4. The exact sampler lines are in `results/<tag>/commands.txt`.

**PCP record:** 14 checks, K1–K14. K4 is the expected-0 run that exited 1 (my test design), kept and followed by K5.
- `pcp_os.py verify --ws pcp`, last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`, last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

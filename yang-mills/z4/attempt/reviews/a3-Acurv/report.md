# report a3-Acurv (builder: claim (A) for SU(2), d=4, by positive curvature)

**This is not a proof of (A).** S6 is CLAIMED and refuted by my test. S7 is MISSING, and what it needs is circular: a strong form of (A). S8 and S9 are CLAIMED. The chain is in PROOF.md.
Control: control.txt = 0.272341. Lean was READY but not used (no pure-algebra step was worth the budget), so I claim no Lean result.

## 1. Verdict table (steps carry their tags)
| item | verdict / tag | one line of evidence |
|---|---|---|
| S0 setup, Langevin generator, target Poincaré inequality | PROVED | definitions |
| S1 gauge action is isometric; ∇f is horizontal for invariant f | PROVED | bi-invariant metric; V and Haar are invariant |
| S2 Bakry–Émery on gauge-invariant functions needs only horizontal curvature κ_H | PROVED (BE theorem CITED via SZZ Thm 1.4/(4.7)) | the Γ₂ argument on a P_t-stable invariant algebra. Numerically it removes a −√β_W deficit (λ_min full −12.2 vs κ_H −1.5 at β_W=48) |
| S3 κ_H ≥ 1 − 12β_W, gives (A) for β_W < 1/12 | CITED (SZZ (4.2), (4.8), Thm 1.4, Cor 1.6) | C3: ‖Hess V‖ ≤ 12β_W on 76/76 samples |
| S4 κ_H = 1 at flat configurations (SU(2)); 0 for U(1) | PROVED | C0: 1.000000000000 at U≡1 |
| S5 inf_U κ_H ≤ 1 − 2β_W, so the pointwise route stops at β_W ≤ 1/2 | PROVED (one plaquette, exact; child and I agree) | eigenvalues 1−2b (×3); 4D lattice T1: 1 − 4.31β_W |
| S6 negative κ_H only on rare configurations (averaged curvature) | CLAIMED, **REFUTED** | T2 failed: κ_H ∈ [−2.3, −1.2] on every sample for β_W = 4…48, with no plaquette having Re Tr Q < 0 at β_W ≥ 6 |
| S7 volume-uniform strong mixing (Dobrushin–Shlosman / Chatterjee Def 2.3) | MISSING (circular) | exact inequality stated in PROOF.md S7; false for U(1) in 4D |
| S8 strong mixing ⇒ uniform LSI (Stroock–Zegarlinski) | CLAIMED | literature from memory, not read |
| S9 uniform Poincaré ⇒ exponential decay with a support-independent rate | CLAIMED | SZZ Sec. 4.3 route per LIT R5a; not reread |
| S10 support-uniform Euclidean decay ⇒ transfer-matrix gap m(β) ≥ r | PROVED (given infinite-volume OS reconstruction, A1 §1) | spectral-measure argument |
| Discriminators | done | U(1) 4D fails first at S3 (Ric = 0); finite group fails at S0; U(1) 3D fails at S3/S4 (so the mechanism is not necessary); 2D: S5 blocks the pointwise route |
| Non-abelian entry | S4 only | Ric = 1 vs 0. Nothing non-abelian enters S6–S9 |

Counts (my programs): **met 14, failed 4, measured only 3** (the κ_H / λ_full / plaquette tables of the three runs). Steps: PROVED 6 (S0, S1, S2, S4, S5, S10), CITED 1 (S3), CLAIMED 3 (S6 refuted, S8, S9), MISSING 1 (S7).

## 2. Hypotheses each statement uses, and where they are stated
- S2: Bakry–Émery on a compact manifold with smooth V. The invariant algebra must be P_t-stable (PROOF.md S1, S2).
- S3: SZZ Assumption 1.1 (|β_SZZ| < 1/(16(d−1))), the normalization S = Nβ Re Tr, and d = 4 (LIT_RIGOROUS R5a, R5b).
- S4–S5: metric −Tr(XY); Wilson action; flat or Q = −1 configurations (PROOF.md).
- S6: large β_W; "rare" means plaquettes with Re Tr Q < 0 (PROOF.md S6).
- S7: all cubes, all boundary conditions, constants independent of both (PROOF.md S7; Chatterjee Def 2.3 in LIT R5e).
- S8: finite-range compact-spin system (Stroock–Zegarlinski, not read).
- S9: uniform Poincaré, range-1 interaction (SZZ Sec. 4.3, not reread).
- S10: an infinite-volume RP state with a transfer matrix exists (A1 §1, assumed there).

## 3. Failed predicates
- T2[β_W=4], T2[β_W=6] on L=3 (result_curv_L3.txt) and T2[β_W=4], T2[β_W=6] on L=4 (result_curv_L4.txt): 0/8, 0/8, 0/2, 0/2 samples have κ_H ≥ 0.5. **This is a defect of the target step S6.** It was also my own expectation, and the expectation was wrong.
- Dry runs to the scratchpad (not results) found a heatbath unitarity drift; I fixed it with a quaternion projection before the first real run.

## 4. What I did not check
- Infinite-volume behaviour of κ_H: only L=3 and L=4 tori, 2–8 samples, short thermalization (30 + 4k sweeps). The O(1) negative horizontal mode might be a torus (constant-mode) artefact; I did not identify the eigenvector.
- The full texts behind S8 and S9.
- Any Holley–Stroock or Lyapunov variant other than the S6 form.
- Routes (a) (multiscale/GOVW on SU(2)^E) and (c) (Hess Φ of the ground state). I did not attempt them.
- 2D S7 by exact solvability.
- Lean: not used.

## 5. Delegated questions and outcomes
- **Child** (child/, sonnet, register check K1, exit 0 in 148 s).
  - Control question: d²/dt² Re Tr exp(tX) at 0 for X = iσ₃/√2. Known answer −1, which I computed first. Child answer −1.000000: **correct**, graded first.
  - Question: for one SU(2) plaquette, λ_min(I + Hess V) at Q = −1, the global minimum, and the horizontal minimum, for b ∈ {0.5, 1, 2, 4}.
  - It returned: 1 − 2b (×3) exactly; the global minimum found by search equals 1 − 2b; the horizontal minimum equals 1 − 2b.
  - I reread hess.py (its expm formula is correct) and reran it in child_rerun/ (K4, exit 0). With my own independent code I reproduced eigenvalues 1 − 2b (×3) and 1 (×9) for all four b. The global minimum is a search result, not a proof.
- **Grandchild** (child/grandchild/, started by the child).
  - Control −1.000000: correct.
  - Question: the FD-only value at Q = −1, b = 1. Answer −0.99999973 (exact −1). The child reran it twice, byte-identical. I did not rerun the grandchild myself; I relied on my own independent check of the same number.

## 6. Commands to rerun (from /home/user/z4-workers/a3-Acurv; output files are opened with mode "x", so delete or rename them first)
```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P check --ws pcp --name curv-test-L3 --expect-exit 0 -- python3 curv_test.py result_curv_L3.txt 3 8
$P check --ws pcp --name curv-test-L3-large --expect-exit 0 -- python3 curv_test.py result_curv_L3_large.txt 3 4 12.0,24.0,48.0
$P check --ws pcp --name child-hess-rerun --cwd child_rerun --expect-exit 0 -- python3 hess.py
$P check --ws pcp --name curv-test-L4 --expect-exit 0 -- python3 curv_test.py result_curv_L4.txt 4 2 4.0,6.0
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Last lines of the register verifications:
- `$P verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

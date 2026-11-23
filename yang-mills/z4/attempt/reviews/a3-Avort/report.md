# report.md — a3-Avort (builder, claim (A) by center vortices)

**The deliverable PROOF.md is not a proof.** It has 1 CLAIMED step and 2 MISSING steps. Claim (A) for SU(2), d = 4, does not follow from it.

Control: control.txt = 0.272341 (−ln tanh 1). Lean: /home/user/z4-lean/READY exists, but I did not use Lean. The algebra of S2 and S4 is short, and there was no time.

## Verdict table (step : tag : evidence)

| Item | Tag | One line of evidence |
|---|---|---|
| S0 infinite-volume limit points along periodic tori L = 2^k L₀ | CITED / assumption | compactness; uniqueness of the state is assumed in A1 §4.5, not known at large β |
| S1 reflection positivity of the Wilson action | CITED | Osterwalder–Seiler 1978 (LIT_RIGOROUS R2, abstract level only) |
| S2 0 < Z⁻ ≤ Z, F_L ≥ 0 | PROVED (given S1) | projection identity (KT eq. 7) plus RP; numerically F ≥ −3σ in 6/6 SU(2) and 6/6 Z₂ cases |
| S3 ⟨W[C]⟩ ≤ 2 (½(1−e^{−F}))^{RT/(L₁L₂)} | CITED | Kovacs–Tomboulis hep-lat/0108017 eq. (11), read by me; credited there to Tomboulis–Yaffe CMP 100 (1985), which I did NOT read; Tomboulis 0707.2179 (6.4) omits the factor 2 |
| S4 vortex decay F_L ≤ K L² e^{−σL²} ⇒ area law in every limit point | PROVED (given S0, S3) | elementary limit; uses uniformity in L |
| S5a F_{L'} ≤ F_L for L \| L', SU(2), every β | CLAIMED | weakest point: it needs an RG comparison F_{2L}(β) ≤ F_L(β′), β′ ≤ β, which is Tomboulis's unproved step (holes 3–5); the SU(2) Monte Carlo is too weak to decide it; S5a is FALSE for Z₂ at β = 0.6 (child, rerun) |
| S5b liminf (−ln F_L)/L² ≥ σ(β) > 0 for every β | MISSING | the vortex condition itself, i.e. confinement at all β; fails for U(1) d = 4 |
| S6 area law ⇒ zero-flux transfer-matrix gap | MISSING | no theorem (Chatterjee Thm 2.4 runs the other way); false as an abstract implication (decoupled massless scalar) |

Counts over the steps: PROVED 2, CITED 3, CLAIMED 1, MISSING 2.

Predicate counts (met, failed, measured only):
- mine: 13 met, 0 failed, 6 measured only. The 13 are Q0 1, Q1 4, Q2 6, exact3d 2; the 6 are the SU(2) F values.
- child, after my rerun: 23 met, 2 failed, 6 measured only. The 23 are C1, C2 and C3 (3), P1 6/6, P2 6/6, P3 6/6 and P4 2/4 (β = 0.3); the 2 failed are P4 at β = 0.6; the 6 are the Z₂ F values.

## Hypotheses used, and where they are stated

- Wilson action, periodic torus, even L. For S1: OS78. For S3: KT (2).
- L₁/R and L₂/T are powers of 2, and reflection planes pass through sites and do not bisect V. For S3: KT, the text after (10); hole 9 / I-S Thm 2.2.
- Existence of a limit along L = 2^k L₀ and identification with "the" infinite-volume state. For S0: A1 §4.5.
- Uniformity in L of the decay rate: S4 and S5b.
- Pure-gauge dynamics: required by S6; not formulated as a usable hypothesis.

## Failed predicates

- **Child P4, β = 0.6 (Z₂, d = 4)**: "F non-increasing in L" failed in both steps: 3.205 → 8.244 → 15.84 (±0.25). It is a property of the target, the deconfined Z₂ phase, and not a code defect. My rerun reproduced it bit for bit.
  - For the chain this is the discriminator working: S5a is false for Z₂ at weak coupling. So any proof of S5a must use SU(2)-specific input, and none is supplied.
  - It is my expectation that it fails there. It is not a defect of S5a for SU(2).
- No predicate of mine failed. My Q1 (monotonicity at 3σ) passed only because the errors are large. At β = 2.4, F(4) − F(3) = +1.26 ± 1.05, the wrong direction at 1.2σ. This is recorded as weak, not as support.

## What I did not check

- Tomboulis–Yaffe 1985 itself.
- Borgs–Seiler and Mack–Petkova.
- The KT figure (where V sits relative to the reflection planes).
- OS78 hypotheses beyond the abstract.
- The strong-coupling computation of F (Münster 1981).
- Any SU(2) box larger than 4⁴, and any β above 2.4.
- Autocorrelation times in my SU(2) runs (Metropolis with ε adapted during runs; not strictly detailed-balance).
- S2 in Lean.
- The discriminator rows for 3D U(1) and 2D are from expectation and LIT_RIGOROUS (Göpfert–Mack, abstract level), not computed. The exception is the 2D Z₂ control formula.

## Delegated questions and outcomes

- **Child (sonnet, headless, register check K1, exit 0, 176 s).**
  - Question: Z₂ LGT d = 4, vortex free energy F(L,β) for L = 2, 3, 4 at β = 0.3 and 0.6; is it non-increasing in L?
  - Control: 2D Z₂ torus, N = 4, β = 0.5. My value is −ln((1−t⁴)/(1+t⁴)) = 0.091272; the child answered 0.091272, so it is **correct**. I graded it first.
  - It returned: β = 0.3: 0.0774, 0.0041, 0.0061 (±0.002–0.005), consistent with non-increasing and compatible with 0 at L = 3, 4. β = 0.6: 3.21, 8.24, 15.84, increasing ≈ L².
  - I reread vortex.c (stack, couplings, quadrature) and reran run_all.sh in child_rerun/ (K3, exit 0). Results are identical bit for bit.
- **Grandchild (the child's sub-agent).**
  - Question: exact 2^24 enumeration of 3D Z₂, L = 2, with the same twist, and check of F = 2β∫⟨Σ_V σ⟩ds.
  - Result: F(0.3) = 0.0325242683, F(0.6) = 0.6912790067.
  - The child did not rerun it. I recomputed it independently with my own exact3d.py (K4): it agrees to 1e-10 (2/2 MET). The child's MC agrees within 1σ.

## PCP OS

- `$P verify --ws pcp` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl` last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- Checks: K1 child-run1, K2 su2-vortex-run1, K3 child-rerun-z2, K4 exact3d.

## Exact commands to rerun (from /home/user/z4-workers/a3-Avort)

Result files are opened with mode "x". Move the old ones aside first.

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"            # control
$P check --ws pcp --name su2-vortex-run1 --expect-exit 0 -- python3 vortex_su2.py run1 200 400 1.8,2.4
mkdir -p child_rerun/out && cp child/vortex.c child/run_all.sh child_rerun/ && (cd child_rerun && gcc -O2 -o vortex vortex.c -lm)
$P check --ws pcp --name child-rerun-z2 --cwd child_rerun --expect-exit 0 --timeout 300 -- ./run_all.sh
$P check --ws pcp --name exact3d --expect-exit 0 --timeout 280 -- python3 exact3d.py
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

The two sources were fetched to the scratchpad (not kept here): arXiv:0707.2179v1 and arXiv:hep-lat/0108017, via curl and pdftotext.

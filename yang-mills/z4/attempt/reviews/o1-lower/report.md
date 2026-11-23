# Report o1-lower (T141): lower bound on the tunnelling splitting

The control file control.txt contains 0.272341 (−ln tanh 1). Deliverable: TUNNEL_LOWER.md.

**Bottom line.** The SU(2)² target, limsup (−log m_eo)/√β ≤ c*, is **not proved**. What I proved:
- general exact reductions;
- a full written proof for the 1-D grid model: limsup ≤ c* + E_κ, where E_κ ≤ 7·10⁻⁴ for κ ≤ 1 and E_κ → 0 as κ → 0.

For SU(2)² I named the two missing steps and the step that loses the constant. That step is the product transverse ansatz: one K₁ step moves the fibre's well circle by an amount equal to the transverse width.

## Verdict table

| item | verdict | evidence |
|---|---|---|
| (I0) flux identity | STANDS | proof; at β=16 identity vs plain subtraction rel 2.9e−9 (mine, K2), 1.4e−10 (child, grandchild T145) |
| (I1) Δ ≥ 2∬_{ff<0} T\|f\|\|f\| (no sign assumption) | STANDS | proof; LB ≤ Δ in 18/18 cases, Δ/LB 1.37–1.51 (K2); child 6/6 |
| Ground-state representation + Lemma P / P' (canonical paths) | STANDS | proof; B1 ≤ Δ 5/5 (K3), loss polynomial (Δ/B1 ≤ 7.5e4 at β=4096) |
| Lemma C (comparison) and Lemma S (1-D subsolution) | STANDS | proof; Tφ/(λφ) ≥ 1.37 on Ω, 6/6 (P8, K2) |
| Theorem 1D: limsup (−log m)/√β ≤ c* + E_κ | STANDS (written, unreviewed) | Lemmas L, M, H, S, C, P; numerics −logΔ/√β = 4.431 at β=4096, below c* = 4.6054 |
| Scalar steps L1–L3 | STANDS | Lean exit 0, axioms propext / Classical.choice / Quot.sound, no sorry |
| SU(2)² target limsup ≤ c* | NOT CHECKED (not proved; MISSING) | transverse subsolution and well mass/Harnack missing (TUNNEL_LOWER §6) |
| TUNNEL_THEOREM §5: "= 2⟨g1_A, Tg1_{A^c}⟩" | DEFECT | the correct factor is 4; the factor-2 form fails 6/6 β (child, ratio 0.655–0.699), the factor-4 form holds (mine 1.31–1.40); exponent unaffected |
| Brief: "f can be chosen positive on A" (SU(2)²) | DEFECT (unsupported) | the sector kernel T(x,y) − T(x,σy) is not positive on A×A (the quaternion inner product can be < 0); my route avoids it |

## Hypotheses used and where they are stated
- Symmetric, entrywise positive kernel; σ a measure-preserving involution commuting with T: TUNNEL_LOWER §0.
- 1-D model: grid step h = κ/√β with κ ≤ 1, N ∈ 4ℕ, wrapped Gaussian with 3 images, ε = 2 asinh|sin|: TUNNEL_LOWER §2 and the oned_split.py docstring.
- η > 4δ_κ, and β ≥ β₀(η, κ, M): TUNNEL_LOWER §2.
- For SU(2)²: Lemma F (via TUNNEL_THEOREM (B)) for the localisation of f; a transverse subsolution (MISSING); Harnack in the wells (CLAIMED): TUNNEL_LOWER §5–6.

## Failed predicates (all kept)
- **P2 (oned_split): f_A > 0 entrywise, 11/18 cases qualify.** Every failure sits at the grid point x = −π/2. That point lies on the nodal set, where f = 0 by reflection symmetry, and the computed value is noise of about −4e−14. This is my own expectation's defect, not the target's.
- **Q3 (oned_paths): log(Δ/B2)/√β < 0.15 for β ≥ 1024.** Measured 0.349 and 0.186. My expectation was too tight: the loss is polynomial (about β^0.55) and the value is decreasing. Own expectation.
- **Q4 (oned_paths): |−log minQ/√β − c*| decreasing from β=256 to β=4096.** Measured 0.022 → 0.071. Not monotone, which is consistent with the β^{−1/3} energy-shift correction (1 − λ_e = 0.077 at β=4096). Own expectation.
- **Child P4: N vs 2N agreement to 1e−3.** Measured 0.75–1.5%. The child's expectation was too tight; the grid is coarse.
- **Child Q2-upper with factor 2:** a defect of the target (TUNNEL_THEOREM §5), as in the table.

**Counts.**
- Mine: met 11, failed 3, measured only 3 (the −logΔ/√β trend, Δ/LB, UB/Δ).
- Child: met 3, failed 2, measured only 1.

## Not checked
- The SU(2)² lower bound itself.
- The 1-D continuum (κ → 0) version: it needs tubes in Lemma H (CLAIMED).
- Lemma L is written as a sketch.
- The 1-D matching upper half on the grid (cited from TUNNEL_THEOREM, not rechecked).
- No arXiv or web source was read; nothing is cited from the literature.
- Discretisation error: grid halving moves log Δ by about 1%.

## Delegation
- **Child T144** (admitted under T141; run recorded as K4, exit 0, 287 s; released). Question: the 1-D test, meaning (Q1) the flux identity, (Q2) the |f|-flux lower bound and the sign-trial upper bound, (Q3) −logΔ/√β for β = 16…4096.
  - Control graded first: 4.605413 = c*. Correct.
  - Outcome: its Δ values equal mine to 7 digits at every β, and its LB/Δ = 0.661–0.718 is the reciprocal of my ratios.
  - It found the factor-2 defect, which I confirmed.
  - Process slips it reported: main.py was not run through its register, and it used multithreaded numpy.
- **Grandchild T145** (admitted and released by the child). Question: at β = 16, Δ by plain subtraction vs by the identity. Answer: 6.0039284e−7 both ways, rel 1.4e−10. I reran its run.py (K5): same numbers. I reran the child's verify.py on its results (K6, exit 1 as declared).

## Rerun (from /home/user/z4-workers/o1-lower)
```
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name oned-smoke --expect-exit 0 -- python3 oned_split.py smoke 16,64 0.25
$P check --ws pcp --name oned-main  --expect-exit 0 -- python3 oned_split.py main 16,32,64,128,256,512,1024,2048,4096 0.25,0.125
$P check --ws pcp --name oned-paths --expect-exit 0 -- python3 oned_paths.py main 16,64,256,1024,4096 0.25
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P check --ws pcp --name rerun-grandchild --cwd rerun_child/gc --expect-exit 0 -- python3 run.py
$P check --ws pcp --name rerun-child-verify --cwd rerun_child/v --expect-exit 1 -- python3 verify.py
(cd /home/user/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/o1-lower/TunnelLower.lean)
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Result files are opened with mode "x". Before a rerun, delete results_*.txt or change the tag; for the reruns, use fresh copies of rerun_child/.

Last line of each verify:
- `$P verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

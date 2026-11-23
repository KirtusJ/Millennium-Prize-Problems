# a7-wild report: seed word "sign". The route through a positive dual representation, refuted at its first unproved step, and the negative statement it leaves

Worker a7-wild, Director Z4, 23 Nov 2026. Principal: Kirtus Justus. Control: control.txt = 0.272341 (−ln tanh 1).
Director and workers are one model family, so this is not independent review.

**In one paragraph.** For U(1) and Z₂ the plaquette-character (dual, spin-foam) expansion has nonnegative weights at every β. The question was whether SU(2) also has positive weights, so that it is a positive random-surface model to which percolation-type sharpness arguments could apply. **It does not.** I computed exactly the Haar integral of a product of plaquette characters on the periodic 2×1×1 lattice in d = 3. It is **negative**, −1/324 (−0.003086419753), and an independent Monte Carlo gives −0.002892 ± 0.000237 (12 standard errors below zero). The same configuration embeds in d = 4. So where non-abelian structure enters the dual, it enters as a sign that destroys positivity. Any positivity property that SU(2) does have, U(1) in d = 4 has as well, and there (A) is false. The route is dead at step S2. The negative statement is in §3.

## 1. Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| S0: the Wilson weight has character coefficients c_j(β) = 2(2j+1)I_{2j+1}(β)/β > 0 for every β > 0 | STANDS | Weyl integration plus the Bessel series of positive terms (proved). Quadrature agrees to rel 1e-8 except 4 tiny entries; see failed predicates. |
| S2: every SU(2) dual amplitude A({j_p}) ≥ 0 (the route's first unproved step) | **DEFECT** (false) | d=3, 2×1×1: 4 of 729 configurations have A < 0. min A = −0.003086419753 at site0 (j01,j02,j12)=(0,1,1), site1 = (1,0,1/2). MC recheck −0.002892 ± 0.000237. |
| S2 on the one-site 3-torus | STANDS (holds there) | 27/27 positive (exact). Child MC 8/8 positive and agrees with my exact values (8/8 within 4 SE). The smallest lattice is too small to show the sign. |
| S2 in d=4 | DEFECT (by embedding, proved) | The 2×1×1×1 lattice with every plaquette that touches direction 4 at spin 0: those links occur in no character and integrate to 1, so A = −1/324. The direct d=4 one-site enumeration was killed for time (NOT CHECKED directly). |
| S3, S4 (sharpness; no surface transition at any β) | NOT CHECKED (MISSING, and moot) | S2 is false. And S4 is false for U(1) in d=4 with positive weights, so positivity could not have carried it. |
| Literature: the SU(2) dual has a sign problem | STANDS (search snippets only) | arXiv:0705.2629 (Cherrington, Christensen, Khavkine; sign expectation falls below 1 at larger β, d=3); arXiv:0910.1890 (d=4, negative amplitudes, noise from β≈1.8). Full texts not read. |
| Child result (one-site 3D amplitudes all positive) | STANDS | Control correct (2). Rerun reproduces the numbers exactly. My exact values: 5/9, 5/12, 13/36, 92/225 (floats). |

Counts: **met, failed, measured only.** Predicates: C0, C1 ×3, C2 ×2, M1 ×2, M2 ×8 met (16). K1, H failed (2). Measured only: the counts of positive and zero amplitudes, the exact one-site values (3 items).
Items: STANDS 4, DEFECT 2, NOT CHECKED 1.

## 2. The route (chain) and its hypotheses

The aim was to make the dual of SU(2) a **positive** random-surface model, then get the gap from sharpness of its percolation-type transition plus the absence of any transition. That last step is not "the coupling runs".

- **S0. PROVED.** exp(β/2·tr U) = Σ_j c_j(β) χ_j(U), with c_j = I_{2j} − I_{2j+2} = 2(2j+1)I_{2j+1}(β)/β > 0. Hypotheses: Haar measure, the Weyl integration formula.
- **S1. CITED.** Z = Σ_{j} Π_p c_{j_p} · A({j}), with A computed by intertwiner contraction. Source: Oeckl–Pfeiffer, hep-lat/0110034 (abstract level). My program implements it directly: the Haar average of a tensor product of representations is the projector onto its invariant subspace.
- **S2. CLAIMED, now REFUTED.** A({j}) ≥ 0 for all {j}. This is where non-abelian structure enters: for an abelian group A ∈ {0,1} (the integral of a character of the group of link variables), while for SU(2), A is a recoupling (6j-type) contraction, which carries signs.
- **S3. MISSING.** For a positive surface model: gap ⇔ finite surface susceptibility, with a sharp threshold.
- **S4. MISSING.** No percolation transition of the surfaces at any β.

**Discriminators.**
- U(1), d=4, weak coupling: S0–S2 PROVED (Bessel-positive coefficients, indicator amplitudes). **S4 fails**: (A) is false there (Guth; Fröhlich–Spencer, abstract level per GROUNDING). So S3+S4 can never follow from positivity alone.
- Finite group Z₂, d=4: S0–S2 hold (Wegner dual; coefficients cosh β, sinh β > 0). S4 is false at large β (a deconfining transition), but (A) holds there. So S4 is stronger than (A), and the route would also have been lossy.
- U(1), d=3: S0–S2 hold and (A) is true (Göpfert–Mack, Villain, abstract). The proof there uses the monopole Coulomb gas, not positivity.

**Weakest link:** S2, which is false (tested). S4 comes next: it would fail for any positive model with a massless phase.

## 3. The negative statement (the wall, in the "sign" direction)

The properties below are shared by SU(2), U(1) and Z₂ in d = 4. Each is PROVED or CITED for all three.

- P1: reflection positivity (Osterwalder–Seiler).
- P2: a strictly positive transfer matrix. In the configuration (link) basis the Kogut–Susskind Hamiltonian is −Δ + V on a compact manifold, which is stoquastic and has a Perron–Frobenius ground state.
- P3: positive character coefficients of the Wilson weight at every β (S0; Z₂: cosh, sinh).
- P4: a gap and analyticity at small β (cluster expansion).
- P5: a positive finite-volume gap at every β.
- P6: a nontrivial center.

U(1) in d=4 has P1–P6 and no gap at weak coupling. **Hence no argument that uses only P1–P6 can prove (A).**

P7 is the property "every dual amplitude ≥ 0". U(1) and Z₂ have it; **SU(2) does not** (tested here, CITED as the known dual sign problem). So the one sign feature special to SU(2) in the dual points the wrong way: non-abelian structure appears as cancellation, and positivity tools (FKG, random currents, sharpness, Perron–Frobenius in the electric basis) lose access to SU(2) at exactly that point.

The smallest PROVED, non-perturbative property separating SU(2) from U(1) that I can name is that **SU(2) is perfect ([G,G] = G; it has no nontrivial homomorphism to U(1))**. Two consequences:
- Through Haar integrals of commutators it produces non-indicator, here negative, dual amplitudes.
- The other proved local appearance is the positive Ricci constant (ledger, curvature route).

I found no proved global consequence of perfectness for the gap.

**Other candidates weighed (briefly, not built), and where each reaches the wall:**
- Analyticity in β: proved only at small β. Analyticity at all β excludes a transition that U(1) does have, so it needs the non-perturbative input again.
- Anisotropic / Hamiltonian limit: it is still the infinite-volume gap of the Kogut–Susskind operator at weak coupling. Perron–Frobenius gives only P2.
- Stochastic quantization: a spectral gap of the Langevin generator uniform in the volume implies a uniform Poincaré inequality, which is the strong mixing of the curvature route.
- Monotonicity in d: no inequality is known. U(1) is gapped in d=3 and not in d=4, so a monotone-in-d argument would have to separate the groups by something else.

## 4. Failed predicates

- **K1** (dual_sign_results1.txt): at β = 0.5 for j = 4, 4.5, 5 and at β = 1 for j = 5, the quadrature and the Bessel formula differ by more than rel 1e-8. Values ~1e-10 to 1e-13, and the absolute error ~1e-16 comes from the midpoint sum. This was **my tolerance**, not a defect of the target: relative error is the wrong measure for tiny c_j. Positivity holds in all cases.
- **H** ("all A ≥ 0"): failed. Per case: d=3 L=1, 27/27 positive. d=3 2×1×1, 4 negative, 141 positive, 584 zero out of 729. d=4 L=1 not completed. **This was my expectation** (I expected it to fail), and it is a **defect of the route** (its step S2 is false).
- dual-sign-run1 was killed by me during the d=4 L=1 enumeration because it was over the 5-minute rule. The register records it as check K1 with exit 0 (the wrapper reports 0; the background shell exited 144). The file holds all d=3 results.

## 5. What I did not check

- The direct d=4 one-site enumeration.
- Whether *some other* positive representation of SU(2) exists. The test refutes positivity of the plaquette-character dual only, not of every dual; a resummation over intertwiners could change the signs.
- S3, S4.
- Full texts of the cited papers (search snippets only: arXiv:0705.2629, arXiv:0910.1890, hep-lat/0110034).
- That the exact values are rational. −1/324 and 92/225 are guesses from floats.
- No Lean was used (/home/user/z4-lean/READY exists; no Lean claim is made).

## 6. Delegated questions and outcomes

- **Child** (sonnet; child/; register child/pcp).
  - Control question: ∫(tr U)⁴ dU over SU(2), with known answer 2 (my program: C0 = 2.000000000000).
  - Child's control answer: 2. **Correct**, graded before reading anything else.
  - Question: Monte Carlo of A(a,b,c), a,b,c ∈ {1/2,1}, on the one-site 3-torus.
  - Returned: 8/8 positive. All 8 agree with my exact contraction within 4 SE (mc_check M2, largest |z| = 1.61). I reran child/mc.py in child_rerun/ (register check K3) and got identical numbers.
  - Its run also had one failed run of its own (a JSON serialization bug in its program), which it kept and reported.
- **Grandchild** (child's sub-agent; child/grandchild/).
  - Control: E[(tr U)²] = 1 (got 1.00188 ± 0.00100).
  - Question: the boundary case A(1/2,0,0) = 1/2 (got 0.49938 ± 0.00074), and A(1/2,1/2,0) (got 0.50109 ± 0.00094).
  - The child derived the exact value 1/2 and reran it. This agrees with my C2 = 0.5 exact. I did not rerun the grandchild's code myself; its numbers are covered by my exact values.
- Limitation: the child's question (the one-site lattice) turned out to be the case where S2 *holds*. The negative case was rechecked by my own second program (a different method), not by the child.

## 7. PCP OS

- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp` → `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl` → `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## 8. Rerun (from /home/user/z4-workers/a7-wild; result files are opened with mode "x", so use new names)

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
$P check --ws pcp --name dual-sign-run2 --expect-exit 0 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 dual_sign.py dual_sign_results2.txt   # d=4 L=1 case takes >8 min
$P check --ws pcp --name mc-check-run2 --expect-exit 0 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 mc_check.py mc_check_results2.txt   # ~2 min, seed 7, N=4e7
cd child_rerun && rm results_v2.json && python3 mc.py   # child's program, seed 20240601
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp ; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

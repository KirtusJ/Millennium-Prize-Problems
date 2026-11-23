# f1-wild (T65): one rung. The center-even gap on the single-site spatial cylinder

Worker f1-wild of Director Z4. Principal: Kirtus Justus. Control: control.txt = 0.272341 (−ln tanh 1).
Lean was available (/home/user/z4-lean/READY exists) but I did not use it, so this report claims no Lean result.

## Verdict table

| Item | Verdict | Evidence (one line) |
|---|---|---|
| Rung statement R1 (below), as a theorem | NOT CHECKED (not proved) | Chain below: steps 2 to 4 MISSING |
| P0 control, U(1) exact gaps, cyl.py (K2/K9) | DEFECT (mine) | β=4: Q met, P 0.154(2) vs 0.1467 failed; β=16 P 0.0545 vs 0.0323 failed. Cause: no global-center move |
| P0 control, U(1), cyl2.py with the exact global move (K6/K7) | STANDS at β=4, DEFECT (mine) at β=16 | β=4: P 0.14632(93) vs 0.14674, Q 0.5683(20) vs 0.5652, both met. β=16 (ξ≈31): 0.0433(9) vs 0.0323 failed, so the sampler is under-equilibrated at long ξ |
| P1 SU(2) exponent p in m_e ∝ β^−p, β = 32 to 256, inside [0.25, 0.42] | DEFECT (my expectation, narrowly) | p = 0.231 |
| P2 m_e^SU(2) > U(1) Z₂-even gap −ln(I₂/I₀) by more than 3σ, every β in {8,…,256} | STANDS (6 of 6) | e.g. β=256: 0.526(42) against 0.00783; m_e·β runs 8.9 → 135 |
| P3 m_e·β^(1/3) at β = 32 and 256 within 25% | STANDS | 2.85 against 3.34 (15%) |
| P4 SU(2) center-odd gap | NOT CHECKED (void) | cyl.py has no center flips and no tunnelling, so Pl ≡ Q in the data |
| Child (T67): independent MC, SU(2) at β = 16, 64 | STANDS as a reproduction; its 4^(1/3) predicate failed | Its β=16 effective masses 2.05, 1.49, 1.19 against mine 2.07, 1.47, 1.19 (observable E). Ratio 1.317(27) |
| Grandchild (T68): Bessel-ratio quadrature | STANDS | 0.06695692 and 0.26632363, rerun by me (K5); my Simpson gives 0.066957 and 0.266324 |

**Counts** (met, failed, measured only):
- Predicates of my own programs: P0 under cyl2: 2 met, 2 failed. P0 under cyl.py: 1 met, 3 failed. P1: 0 met, 1 failed. P2: 1 met (6 of 6 cases qualify). P3: 1 met. P4: 1 measured only (void).
- Total: **5 met, 6 failed, 1 measured only.**

## The rung

**Statement R1.** Take the four-dimensional Wilson lattice theory on the cylinder (ℤ/Lℤ)³ × ℤ: spatial side L fixed, starting with L = 1, and time infinite. Let G = SU(2).
- The transfer matrix T_β on L²(G^{3L³})^gauge is positive (Lüscher 1977), self-adjoint and compact.
- Let m_e(β) be its gap on the sector invariant under the global center symmetry U_i → z_i U_i, z_i = ±1.
- R1 claims there are constants 0 < c ≤ C and β₀ such that, for β ≥ β₀:
  **c·β^(−1/3) ≤ m_e(β) ≤ C·β^(−1/3).**
- Sharp form: β^(1/3)·m_e(β) → E₁, the gap of the zero-mode matrix Hamiltonian −½Δ + κΣ_{i<j}|[Y_i,Y_j]|² on su(2)³, restricted to gauge-invariant even states (κ fixed by the normalization; not computed here).
- For U(1) on the same lattice everything is exact. The gaps are −ln(I_n(β)/I₀(β)) ≈ n²/(2β) in flux sector n ∈ ℤ³, and the Z₂-even gap is ≈ 2/β.

**The sign of the group.** In the center-neutral sector the non-abelian group raises the gap from order β^(−1) to order β^(−1/3). The mechanism is that the commutator potential, which vanishes identically for U(1), confines the flat toron valley quartically. This is a Simon-type effect: discrete spectrum although the classical potential has flat directions.

**Why it is beyond STATE_OF_PROGRAM.md.**
- Nothing in that file is a lower bound on any gap at weak coupling, in any four-dimensional geometry.
- The fixed-box item there is partition-function asymptotics and says nothing about the spectrum.
- R1 would be the first proved weak-coupling lower bound in which SU(2) and U(1) differ with a definite sign. It would be proved non-perturbatively, at a power of β, not only as an error term.

**What it would give, honestly.**
- R1 is the bottom rung of a ladder in L: L = 1, 2, … fixed, then L up to β^k, then toward exp(cβ).
- At fixed L, as β → ∞, the physical box shrinks. This is Lüscher's small-volume regime, the opposite end from the infinite-volume gap. It gives no bound in infinite volume.
- Its use is as a tool: a rigorous semiclassical analysis of a positive compact transfer operator near the toron valley, with the non-abelian group entering globally along a flat direction. That is exactly the ingredient every broken route in A1_LEDGER lacked.
- It does not escape the "six shared properties" wall in principle. It uses the commutator, which U(1) lacks.

**Chain to prove R1 (L = 1)**

| # | Step | Tag |
|---|---|---|
| 1 | T_β is self-adjoint, positive and trace class on L²(SU(2)³)^conj; its kernel is continuous and strictly positive, so the gap is > 0 at every β | Positivity: CITED (Lüscher, Commun. Math. Phys. 54 (1977) 283, abstract-level only). Compactness and Perron–Frobenius: PROVED (elementary: continuous kernel on a compact space; Jentzsch) |
| 2 | Agmon-type localization: eigenvectors with energy ≤ Kβ^(−1/3) live within β^(−1/3+δ) of the eight center copies of the identity, transverse to the commuting variety | MISSING |
| 3 | Trotter comparison: −ln T_β = β^(−1/3)·H_β + O(β^(−2/3)) on that region, in the rescaled variable Y = β^(1/3)A | CLAIMED (scaling derived in notes.md; no remainder estimate) |
| 4 | H_β → the matrix Hamiltonian in norm-resolvent sense, uniformly along the valley up to the group boundary (the transverse zero-point energy grows like \|a\|) | MISSING |
| 5 | The matrix Hamiltonian with a commutator-squared potential has compact resolvent (Simon, Ann. Phys. 146 (1983) 209), so E₁ > 0 | CITED from memory: the paper was not read; a search snippet cites the operator inequality −∂²_x + y²x² ≥ \|y\| type |
| 6 | Tunnelling between center copies is exp(−c√β) and affects only center-odd states | CLAIMED (Lüscher 1983, van Baal; perturbative and semiclassical) |
| 7 | Steps 1 to 6 give c·β^(−1/3) ≤ m_e ≤ C·β^(−1/3) | MISSING (it is the assembly) |

**Weakest link:** step 4, together with step 2. They require uniform semiclassics along the whole valley on a compact group, with a transfer operator rather than a Schrödinger operator. The region near the non-identity center points and the endpoints of the valley is where a proof could fail.

**First case tested (my programs cyl.py, cyl2.py, analyse.py; predicates fixed in the docstrings before the first run; U(1) run through the same code as the subgroup exp(iθσ₃)).**

SU(2) center-even gap m_e on 1³ × 64, from the Q = Σ(2q₀² − 1) plateau (32 replicas, 2000 sweeps):

| β | 8 | 16 | 32 | 64 | 128 | 256 |
|---|---|---|---|---|---|---|
| m_e | 1.11(10) | 1.19(9) | 0.897(43) | 0.831(40) | 0.751(70) | 0.526(42) |
| m_e·β^(1/3) | 2.21 | 3.01 | 2.85 | 3.33 | 3.79 | 3.34 |
| U(1) −ln(I₂/I₀) | 0.266 | 0.129 | 0.0635 | 0.0315 | 0.0157 | 0.0078 |

**Reading of the test.**
- The SU(2) gap falls far more slowly than U(1)'s. The fitted exponent is 0.23, against 1 for U(1) and 1/2 for harmonic fluctuations; the prediction was 1/3.
- The effective masses still drift at the largest t, so the plateaus are upper bounds biased by excited states (the child found the same).
- The sampler fails its U(1) control at ξ ≈ 31. The SU(2) ξ here is ≤ 2, but slow valley modes may still be under-sampled.
- So this is an indication that the exponent is small and positive, not a measurement of 1/3.

**Literature** (WebSearch, three queries: Lüscher small-volume g^(2/3); rigorous discrete spectrum of the Yang–Mills matrix model / Simon x²y²; rigorous lattice transfer-matrix gap at small spatial volume).
- The g^(2/3) small-volume expansion is in Lüscher, Nucl. Phys. B219 (1983) 233 (INSPIRE 183485; abstract only), extended by van Baal (hep-ph/0008206) and Kronfeld–Wiese (hep-lat/9608018). It is perturbative or semiclassical, in the continuum.
- Discreteness for matrix models: Simon 1983 (not read); Khvedelidze–Pavel style operator inequalities (snippet only).
- I found no rigorous lattice statement of R1. So the physics is known; the rigorous lattice lower bound appears not to be in the literature. That is a search result, not a claim of novelty.

**Runners-up**
1. Monotonicity in β of the reflection-positive plaquette correlation at fixed lag on the 1³ cylinder. Discarded: Ginibre-type inequalities are not available for SU(2).
2. The center-odd (electric-flux) gap ≈ exp(−c√β) on the same cylinder: a statement at scale exp(c√β). Not tested: it needs center-flip and tunnelling moves; known semiclassically (van Baal).

## Hypotheses used and where stated
- Wilson action and the cylinder geometry: cyl.py docstring and child/PROMPT.txt.
- Positivity of the transfer matrix: Lüscher 1977, cited from search snippets.
- Simon 1983 discreteness: cited from memory.
- Valley tunnelling scale: Lüscher/van Baal, claimed.
- MC: equilibration after 500 sweeps from a cold start (assumed; refuted for U(1) at ξ ≈ 31).
- Plateau rule: cyl.py docstring.

## Failed predicates (kept)
- P0 under cyl.py: 3 of 4 failed. My defect: no exact global-center move.
- P0 under cyl2.py at β = 16: 2 failed. My defect: sampler equilibration at long ξ; the target formula is exact and was rechecked by the grandchild.
- P1: exponent 0.231 is outside [0.25, 0.42]. My expectation, or excited-state bias; undecided.
- Child's 4^(1/3) consistency predicate failed (r = 1.317(27)): its expectation and window bias.

## Not checked
- Every MISSING step of the chain, and the constant E₁ (κ not computed).
- Larger T, longer runs, a variational basis, and the center-odd sector.
- L ≥ 2.
- Lean was not used.

## Delegated questions
- **Child T67** (admitted under T65, released, event 140).
  - Control: −ln(I₁(4)/I₀(4)) = 0.146735 (my Simpson value). Child answered 0.146735: correct, graded first.
  - Question: an independent Metropolis MC of the same lattice; the U(1) β = 4 check; SU(2) m_e at β = 16 and 64.
  - Outcome: U(1) 0.14690(184), met. SU(2) window values 1.440(24) and 1.093(14), no plateau. Its effective masses at β = 16 reproduce mine to about 0.02.
- **Grandchild T68** (admitted under T67, released).
  - Question: quadrature of −ln(I₁(8)/I₀(8)) and −ln(I₂(8)/I₀(8)).
  - Outcome: 0.06695692 and 0.26632363. Its control passed. I reran it (K5) and it agrees with my values.

## Registers
- `pcp_os.py verify --ws pcp`: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- `pcpos verify pcp/register.jsonl`: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.

## Rerun (from /home/user/z4-workers/f1-wild; result files are mode "x": use fresh names or directories)
```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name smoke --expect-exit 0 -- python3 cyl.py su2 64 64 16 100 100 1 res/smoke_su2.json
$P check --ws pcp --name runA --expect-exit 0 --timeout 1500 -- bash runA.sh   # u1 4,16; su2 8,32,128: T=64 R=32 therm 500 meas 2000 seed beta+1000
$P check --ws pcp --name runB --expect-exit 0 --timeout 1500 -- bash runB.sh   # su2 16,64,256
$P check --ws pcp --name runU1fix --expect-exit 0 --timeout 1200 -- bash -c "python3 cyl2.py u1 4 64 32 500 2000 1004 res2/u1_b4.json && python3 cyl2.py u1 16 64 32 500 2000 1016 res2/u1_b16.json"
$P check --ws pcp --name analyse-final --expect-exit 0 -- python3 analyse.py res/analysis_final.txt
$P check --ws pcp --name analyse-u1fix --cwd fixu1 --expect-exit 0 -- python3 ../analyse.py ../res2/analysis_u1fix.txt   # fixu1/res -> ../res2
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
cd child && $P check --ws ../pcp --name child-rerun-grandchild-quad --expect-exit 0 -- python3 grandchild/quad.py
$P verify --ws pcp; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

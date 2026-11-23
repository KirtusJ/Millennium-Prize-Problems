# Z4 challenger report on Director B4's note (T1–T4)

Control: control.txt = 0.272341 (−ln tanh 1).
Overall: I found no defect in T1–T4. One predicate failed, and the failure was my own expectation, not a defect of the target. Z4 and B4 share a model family, so this agreement is not independent review.

## 1. Verdict table

| Item | Verdict | Evidence (one line) |
|---|---|---|
| T1a cycle / mixed labels | STANDS | A vertex carrying one nonzero label has no invariant, so every vertex of the support has degree ≥ 2 and the support contains a cycle. That needs ≥ g_L edges, each costing n(n+2) ≥ 3, so the cost is ≥ 3g_L whatever the labels. The enumeration confirms this: no admissible assignment lies below threshold (t1_result_1.json). |
| T1b L=2, L=3 | STANDS | L=2: 301 assignments enumerated, 13 admissible (12 nonempty), minimum cost 6, attained exactly by the 12 parallel-link pairs. L=3: 88723 enumerated, 28 admissible (27 nonempty), minimum cost 9, attained exactly by the 27 winding triangles. |
| T1c L=4 degeneracy | STANDS (by derivation; not enumerated) | My own girth computation (edge deletion + BFS) gives 2,3,4,4,4 for L=2..6. The bound 3g/(2κ) depends only on g, so it does not matter whether a shortest cycle is a plaquette or a winding loop. |
| T2a rescaling, fourfold cover | STANDS | Checked exactly with rationals for L=2,3,4: the 4 sites of x+S are distinct, every site lies in exactly 4 sets, Σ_x h_x = (4/3)ΣA_y = (8κ/3)(1/2κ)ΣA_y, and each face is counted once. |
| T2b block ground space / unit gap | STANDS | h_x is diagonal in Peter–Weyl labels, its kernel is the product constant, and its minimum on the complement is 3/3 = 1 (exact). |
| T2c ‖v_x‖ ≤ 8z | STANDS | (8z/3)·3·max\|φ\| with \|φ\| ≤ 1. Sampled max of \|Σφ\| was 2.71 ≤ 3. |
| T2d plaquette support ⊂ x+S | STANDS | The face sites are {x, x+e_i, x+e_j}. Checked for every anchor and plane, L=2,3,4. |
| T2e Yarotsky Thm 1 admits h_x | STANDS, with caveats | Sec. 1 lets h_x act on "H_{Λ0+x}" (a block is allowed), allows infinite-dimensional sites and unbounded h_x, requires eq. (1) gap ≥ 1, and requires translation-invariant terms (the note's h_x and v_x are the same at every x). The bounded v_x satisfies eq. (2) with α=0, β=8z. Thm 1 part 1 gives γ "independent of Λ". Caveat 1: the paper takes periodic cubes "for simplicity" and the statement sets no minimum side; I did not check that the cluster-expansion proof holds at L=2,3. Caveat 2: the thresholds α, β and γ are not quantified, as the note itself says. |
| T3a orthogonality of xy traces | STANDS | For L=2,3,4, distinct xy faces have distinct link sets, each with a link the other lacks. Monte Carlo Gram matrix at L=2 (seed 20261122, N=20000): max deviation from the identity 0.015, below the 5-SE tolerance 0.035. |
| T3b energy 6/κ | STANDS | Finite-difference Casimir on the 4 links gives 12·F (relative error 1.0e-6), and 12/(2κ) = 6/κ. |
| T3c Riemann limit, b^{3/2} | STANDS | Cov = b³Σf(bx)g(bx)·e^{−6\|t\|/κ} → ∫fg. My monotone-error predicate failed (see §3), but convergence holds (b=0.05 vs b=1e-3 agree to 3e-7 relative). |
| T3d fairness of the z↔t test | STANDS as stated, little information | The failure is built in: H is not rescaled as b→0, so the spatial correlation length is zero and the temporal one is κ/6. Any uncoupled anisotropic regulator fails this test. The note says this concerns the uncoupled model only. Calling it a "spatial refinement" overstates it: only the smearing is refined, not the Hamiltonian. |
| T4 s ≥ 2/3, v ≥ 5/9, M formula, M/v ≤ 12/κ | STANDS | ε ≤ 8z/3 ≤ 1/144 and d ≤ 1/12. Trace distance d gives \|Δ⟨O⟩\| ≤ ‖ρ−σ‖₁·‖O−c‖ = 2d·2 = 4d. v ≥ 1−1/3−1/9 = 5/9. M = (1/2κ)·4·⟨4−F²⟩ = (2/κ)(4−s) ≤ 20/(3κ), so M/v ≤ 12/κ. The delegated numerical check agrees (§5). |

Lean (rule 6): a copy of HamiltonianTime.lean compiled with exit 0. `#print axioms` shows only propext, Classical.choice, Quot.sound, and there is no sorry (lean_out.txt). What it proves: real-number algebra only (casimirCoefficient, rescale, blockUnitGap, faceLeak, localWitness, tangentPoint, polarTrial, weakLower), plus two finite sums (rangeSum, electricSmearing) and a product bound (cycleProduct). What it does not prove: anything about operators, SU(2), Yarotsky's theorem, the torus geometry or girth. In localWitness the trace-distance step (\|m\| ≤ 4d, s ≥ 1−4d) and the energy identity κE = 2(4−s) are hypotheses, not theorems.

## 2. Hypotheses used and where they are stated
- T1: λ=0; periodic cube with side L ≥ 2; physical space = gauge-invariant functions (README "Transfer, Hamiltonian and vacuum"); r_n ≤ r_1 for n ≥ 1 (Bessel order monotonicity, cited DLMF §10.37); parallel links counted as distinct edges (README "Exact free electric spectrum").
- T2: unrestricted ground state unique and gauge invariant (README "Transfer" paragraph, Perron–Frobenius-type positivity); Yarotsky eqs. (1)–(2) and Thm 1 (paper Sec. 1); 8z below an unquantified threshold (README table row 3); φ = ReTr U/2 with \|φ\| ≤ 1.
- T3: λ=0 and L ≥ 3 (README "An explicit spatial refinement"), though orthogonality also holds at L=2; f, g compactly supported and smooth; boxes grown to contain the supports.
- T4: z ≤ 1/384; translation and cubic symmetry of Ω; N_e = N_p = 3L³; L ≥ 2 so every face has 4 distinct links (plaquette.md §1); round unit-S³ metric with generators iσ_k.

## 3. Failed predicates
- t23_geom.py T3c ("Riemann error decreasing in b and < 1e-3 at b=0.1"): errors were 1.1e-7, 6.1e-7, 6.1e-7 at b = 0.4, 0.2, 0.1. The bound < 1e-3 held; monotonicity did not. This was my own expectation: aliasing errors of smooth bumps oscillate. It is not a defect of the target. The result file is kept as t23_result_1.json, and PCP recorded K2 as exit 1 against an expected 0.

Counts (met, failed, measured only):
- My programs: 24, 1, 2.
- Child program as I reran it: 49, 0, 0.
- Lean: 1, 0, 0.

## 4. Not checked
- Yarotsky's proof itself at L=2,3, and the numerical thresholds and γ.
- T1 by enumeration at L ≥ 4 (derivation only).
- The time-limit and compactness arguments of README §"Transfer".
- The large-z section of plaquette.md and the A4 citation.
- The general-G extension.
- geometry.py, and the native certificates in readback.txt (not rerun).

## 5. Delegated question (rule 7) and outcome
- Question: on SU(2) class functions, take H = (2/κ)(−Δ) + λ(1−cosθ) in a truncated character basis, F = χ₁, w = (F−⟨F⟩)Ω. Is M = ⟨w,(H−E0)w⟩ = (2/κ)(4−s)? This is the one-plaquette version of plaquette.md's identity. Control question: ∫χ₁⁴ dU = 2.
- Outcome: the control came out as 2.000000000000. The identity holds to 4e-15 at κ ∈ {0.5,1,2}, λ ∈ {0.1,1,10,100}, N = 40 and 60, and the wrong coefficient (1/κ) fails everywhere.
- My own check: I reread child/gap_test.py (the matrix entries are correct and M is computed directly) and reran it under my register (K3, exit 0, child/results_2.txt, ALL PASS). Child PCP verify: PASS.

## 6. Commands to rerun (from C:/Users/donke/z4-workers/r2-b4, bash, PYTHONUTF8=1)
```
python -c "import math;print('%.6f'%(-math.log(math.tanh(1))))"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name t1_enum --expect-exit 0 -- python t1_enum.py t1_result_2.json
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name t23_geom --expect-exit 1 -- python t23_geom.py t23_result_2.json
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name child_rerun --expect-exit 0 -- python child/gap_test.py
cd C:/Users/donke/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean C:/Users/donke/z4-workers/r2-b4/HamiltonianTime_copy.lean
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```
PCP verify last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

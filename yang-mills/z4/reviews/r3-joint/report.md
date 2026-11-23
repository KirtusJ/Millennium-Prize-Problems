# Z4 challenger report — B4 joint-cutoff notes (r3-joint)

Input: only the text in `input/`. Role: challenger. The director and I share a model family, so where I agree that is not independent review. Control: `control.txt` = 0.272341.

## 1. Verdict table

| Item | Verdict | Evidence (one line) |
|---|---|---|
| J1a units of c, a | STANDS | In hamiltonian-time conventions A_e is dimensionless, so κ is a time and λ an energy. Then c = 6λL³+6/κ is an energy, a is a time, ac is dimensionless and ac² is an energy. |
| J1b origin of 6λL³ and 6/κ | STANDS | 6λL³ = 3L³ plaquettes × λ × max(1−φ_p) = 2. 6/κ is H₀ of the fundamental plaquette character: 4 links × 3/(2κ). |
| J1c arithmetic a/(1+ac) → 9a → 72 → 90 → 180 | STANDS | I re-derived the exact resolvent identity. The chain 2a+3a+4a, 9·(4c)(2c)=72, 72+2·9=90 and 2·90=180 checks out, and the random-point scalar checks (A1–A3) all pass. |
| J1d meaning of "log-transfer energy" | STANDS, with a caveat | e_j = −log(t_j)/a uses the **unnormalized** T_a (r₀=1, W≥0, W(1)=0). It does **not** divide by the leading eigenvalue as hamiltonian-time l.22 does. With that normalization e₀≡0 and the individual-energy bound would be false. The gap bound does not depend on normalization. |
| J1e one-plaquette numerics | STANDS (comparison with the note's c: measured only) | P1–P6 met 39 of 39 qualifying checks, 0 failed. The observed gap error is at most 2.6·10⁻⁴ × 180ac² (§1a). |
| J2 a β²/b⁸ → 0 suffices | STANDS as written; needs β bounded below | ac² → 0 ⇔ aβ²ℓ⁶/b⁸ → 0 **and** a/(β²b²) → 0. As soon as β ≥ β₀ > 0, b ≤ 1 and ℓ is fixed, the first condition implies the second, a → 0 and ac → 0. Counterexample with β = b⁴, a = b: aβ²/b⁸ = b → 0, yet ac² = 4·10²⁸ at b = 2⁻¹⁰ (Q3). The note says β→∞, which covers this. |
| J2 gap floor d along the trajectory | STANDS (as a floor); it is not a physical gap | log d = −(12β²+3 ln2)(ℓ/b)³ − ln(2βb). With ℓ=1 and β=2+k/4: log₁₀ d = −219 (L=2), −2.1·10³ (L=4), −2.1·10⁴ (L=8), −1.7·10⁷ (L=64). |
| J3a heat density in [2/3, 4/3] | STANDS (in the note's normalization) | My rerun of the child's program: min p = 0.80387 at θ=π, max p = 1.20217 at θ=0, tail 0.20217 ≤ 4/(e³−4) = 0.24867. With the eigenvalue n(n+2)/4 instead, min p = 0.0088 and max p = 4.55, so the window and every constant built on it fail. |
| J3b common measure ε = e^{−sB}2^{−N} | STANDS | P(x,dy) ≥ (m₀/M₀) q(dy). This needs h, Ω and q to be taken against the same Haar probability, which the note states. |
| J3c oscillation contraction → d | STANDS | osc(Pf) ≤ (1−ε) osc f, then e^{−sΔ} ≤ 1−ε and Δ ≥ ε/s. The two-state example (ε=1/8, eigenvalue 7/8) is exact (A6). Lean covers only the finite-row and scalar steps. |
| J3d errors 72·2^{−n−8}, 180·2^{−n−8} | STANDS | a c ≤ 2^{−n−8}/4 and a c²/d ≤ 2^{−n−8}. Since 72·2⁻⁹ < 1, the hypothesis 9a ≤ ρ/2 holds (A4, A5). |
| J4a positive-time norm bound | STANDS | Constants re-derived: (2+2s)² ≤ 8(1+s²), 3a/t+7ac, and the implicit Euler error ≤ 2/k, where the observed max k·err is 0.27, so loose (A7, A8). |
| J4b moving vacuum shift E₀−μ₀ | STANDS; it uses the same bound | The shift enters as \|E₀−μ₀\|/η² ≤ 72ac²/η², taken from the level bound (energyFromResolvent). It is not a separate hypothesis. It uses μ₀ = (1−‖T_a‖)/a, not e₀. |
| J5 Lean recompile | STANDS (scalar and algebraic steps only) | Exit 0, no sorry, and all 14 `#print axioms` lie within {propext, Classical.choice, Quot.sound}. Coverage is listed in §2. |
| X1 README l.72 "fixed physical box size L = O(1/b)" | DEFECT (notation, minor) | L is the dimensionless lattice side and the physical side is ℓ = Lb. "Fixed" and "O(1/b)" (ℓ only bounded) are conflated. aβ²/b⁸ is the ℓ⁶-stripped form, which has dimensions unless ℓ is fixed. |
| X2 "log-transfer energy" README vs hamiltonian-time l.22 | DEFECT (terminology, minor) | hamiltonian-time says normalization by the leading eigenvalue removes the scalar convention. The README's individual-energy bound needs the unnormalized T_a and has to say so. |
| execution.md, plaquette.md, E2 links | NOT CHECKED | These files were not supplied. |

Counts (items above): **STANDS 15, DEFECT 2, NOT CHECKED 1**.

Predicate totals across my programs (met, failed, measured only): **59, 0, 2**.
- j1 v2: 39 met, plus 1 measured-only row (sharpness)
- j2: 3 met (Q1–Q3), plus 1 measured-only (M1, d and the schedule)
- j34: 8 met (A1–A8)
- child rerun: 4 met (P_a, P_b, P_c, P_d2) and 1 failed (P_d1); see §3
- Lean: 14 theorems, axioms clean

The totals count P_d1 under §3 rather than as a failure here.

### 1a. J1 one-plaquette numerics (`j1_plaquette_v2.py` → `results/j1_run2.json`)
**Adapting c to one plaquette.** I used c = B + 6/κ with B = 1 plaquette × λ × 2, so c = 2λ+6/κ. The text does not force this (it states c for an L≥2 cube), so the comparison with "the note's own c" is **measured only**. The proof's own hypotheses can be checked directly, though: 0 ≤ W ≤ B ≤ c, E₁ ≤ c, and ac ≤ 1/36. The model satisfies all of them (P1, 3/3), so P2–P5 are genuine tests of the derivation.

**Model.** The basis is χ_n with n < 28. H₀ = 4n(n+2)/(2κ), K_a = r_n⁴ with r_n = I_{n+1}(κ/a)/I₁(κ/a), W = λ(1 − χ₁/2) acting as a tridiagonal operator, T_a = M K_a M, and e_j = −log t_j / a. Couplings: (κ,λ) = (1,1), (1,5), (0.5,2). Time steps: a = 2⁻⁴ … 2⁻¹².

**Predicates (met, failed, measured only).**
- P1 (proof hypotheses hold): 3, 0, 0
- P2 (resolvent difference ≤ 9a, ac ≤ 1): 15, 0, 0. The largest observed value is 0.096·9a.
- P3 (\|e_j−E_j\| ≤ 90ac²): 6, 0, 0
- P4 (gap error ≤ 180ac²): 6, 0, 0
- P5 (\|μ_j−E_j\| ≤ 72ac²): 6, 0, 0
- P6 (truncation, N vs N+12, relative 1e-12): 3, 0, 0
- Measured only: the observed gap error / 180ac² ranges from 5·10⁻⁵ to 2.6·10⁻⁴. The gap error is linear in a: gap_err/a = 2.97, 2.51 and 11.9 at the three couplings, and it is steady across the two qualifying steps.

**Conclusion.** The bound holds on this model and is loose by 3–4 orders. The true error is O(a) with a model constant, while the bound is O(ac²).

## 2. Hypotheses each statement uses, and where they are stated
- **9a resolvent bound** (README l.33–48): c ≥ B ≥ ‖W‖, ac ≤ 1, 0 ≤ W ≤ B (l.31), the free form bounds H₀(1+aH₀)⁻¹ ≤ D_a ≤ H₀ (l.21; Bessel ratio bounds at l.13–17), and gauge equivariance of M and K (l.27, l.31).
- **90ac² and 180ac²** (l.52–58): E₀, E₁ ≤ c from the trial space (l.52), ac ≤ 1/36, min–max (Weyl) for bounded self-adjoint resolvents (l.52), and μ_j < 1/a (above the accumulation value).
- **Vacuum projection bound** (l.61–66): Δ > 0 and 9a ≤ ρ/2.
- **Gap floor d** (fvv l.11–32): the n(n+2) metric with s = 2κ (fvv l.11, README l.9, ht l.16), Feynman–Kac/Trotter order for 0 ≤ W ≤ B (fvv l.17), a continuous positive kernel and a bounded ratio f = ψ/Ω (fvv l.21, l.32), and one Haar probability used for all of h, Ω, q.
- **Schedule** (fvv l.38–47): Δ_n ≥ d_n, and the README bounds above.
- **Evolution** (evol l.3–31): ac ≤ 1/36, a ≤ t/2, μ₀ ≤ 3c, and the shift identity with e* = min(μ₀, E₀) ≤ c.
- **Lean (JointCutoff.lean)** covers only scalar and ring/normed-ring lemmas. These steps are **hypotheses** there: the score and Gamma inequalities (`ratioFromScore`), the per-label inequalities (`productBounds`, `kineticBounds`), the 2a and 3a steps (`wilsonResolventError` takes them as inputs), the outer-norm bounds ≤ 2 (`commonPotentialNorm`), the passage from operator norm to level differences (min–max is absent: `energyFromResolvent` assumes the scalar inequality), the kernel bounds, the heat density, Feynman–Kac and the minorization (`residualRange` is finite-sum only, and `oscillationGap` takes the two oscillation inequalities as hypotheses), the vacuum projection bound, all of J2, the schedule arithmetic, and all of J4. In short, J1c and part of J3c are covered; J1a, J1b, J2, J3a, J3b, J3d and J4 are not.

## 3. Failed predicates
- **Child P_d1 (heat window under the eigenvalue n(n+2)/4): failed.** This was an intended stress test of the *alternative* normalization. It is not a defect of the target, because the note fixes n(n+2) consistently in README l.9, fvv l.11 and ht l.16/24. It does show that the constants 2/3, 4/3 and ε are tied to that metric and time scale.
- **My control answer to the child ("about 0.2009") was wrong.** The correct value is 0.2022. This was my own error, and the child caught it.
- **j1 v1 run: aborted by me for runtime** (no result file, and no register event, because it was stopped before pcp recorded it). It was not a predicate failure, and it was replaced by v2, whose docstring states the reduced parameters.
- No predicate on the target failed. In this text I found no defect in J1–J4 mathematics. The two DEFECTs above are wording.

## 4. What I did not check
- execution.md, plaquette.md and the external references (Lüscher, Yarotsky, Teschl, DLMF).
- The Bessel ratio bounds b_k at all labels. They are only spot-read here; controls.py was not run because scipy and numpy are not installed.
- Min–max for the non-compact resolvent, beyond reading the argument.
- The Feynman–Kac order, not tested numerically.
- J4 numerically on a model.
- The multi-plaquette L ≥ 2 cube numerically.
- The physical question itself. No statement here gives a volume-uniform gap on the tree-level trajectory, and the notes say so (README l.72, fvv l.7, l.49).

## 5. Delegated question and outcome
Delegated: the J3 heat density. The child got the definition of p(θ) = Σ(n+1)e^{−n(n+2)}χ_n(θ) at s = 2κ, Haar probability, the claim 2/3 ≤ p ≤ 4/3 with its tail bound, and the alternative normalization n(n+2)/4. Its control was Σ_{n≥1}(n+1)²e^{−n(n+2)}.

Outcome: the child returned 0.20217233. It correctly pointed out that the "about 0.2009" I gave as the known answer was wrong; that error was mine. Its results:
- min 0.80387, max 1.20217, tail ≤ 0.24867, Haar integral 1;
- under the alternative normalization: min 0.00882, max 4.5518, window fails.

Its register's verify line: "result: PASS (…)". I reran `child/heat_bound.py` (a copy in `rerun_child/`) under my register (K2, exit 0) and got identical output.

## 6. Commands to rerun
```
cd C:/Users/donke/z4-workers/r3-joint
export PYTHONUTF8=1
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name j2_units --expect-exit 0 -- python j2_units.py results/<new>.json
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name j34_arith --expect-exit 0 -- python j34_arith.py results/<new>.json
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name j1_plaquette_v2 --expect-exit 0 -- python j1_plaquette_v2.py results/<new>.json
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name rerun_child_heat --expect-exit 0 -- python rerun_child/heat_bound.py   # first delete or rename rerun_child/results_heat_bound_v1.txt (it refuses to overwrite)
cd C:/Users/donke/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean C:/Users/donke/z4-workers/r3-joint/JointCutoff_copy.lean
cd C:/Users/donke/z4-workers/r3-joint && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```
Last line of `pcp_os.py verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`.

**Physical bottom line for Z4.** On tree-level matching with fixed ℓ, absolute gap tracking needs a ≲ 10⁻⁴·b⁸/β² for O(1) accuracy (at a = b⁹ the bound is still 1240/ℓ at b = 1/64). The only proven lower bound is d ≈ 10^(−1.7·10⁷) at L = 64. "Tracks the gap" is shown; "the gap is bounded below in physical units" is not, and the notes do not claim it.

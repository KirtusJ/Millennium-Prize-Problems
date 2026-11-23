# Z4 challenger report: D4 electric-scale (weak bare coupling)

Worker r6-elec, 2026-11-23. Sources: only `input/*.md`, my programs, and the child's program, which I reran. The director and I share a model family, so where I agree with D4 that is not independent review.

**Convention.** D4 uses g = λ/κ with H = (κ/4)Σ(−Δ_{S³}) + λΣ(1−x_p). Here −Δ has eigenvalue n(n+2) with n = 2j. The matching is κ = 2/(βb) and λ = β/b, which gives **g = β²/2**. That agrees with A4's convention and the program's. The kinetic coefficient is κ/4 = 1/(2βb) = 1/(2κ_B), so the program's Hamiltonian is reproduced. **But D4's symbol "κ" is not the program's κ_B: κ_D4 = 2/κ_B.** dimension.md uses a second ratio, g_G = λ/a = 4g = 2β², which is the one in the README's g_G^{d/4}.

## 1. Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| E1 SU(2) scaling: r_q ~ β^{3/2}, S = (3/2)log β + O(1) (rotor proxy only) | STANDS (proxy) | On one rotor: N_q+1 ≈ y_q g^{1/4}, with y_.9 = 1.487 and y_.99 = 2.003 (deviation ≤ 0.49 for g ≥ 1e2). Slopes: N .256/.261, Dim = Σ(n+1)² .724/.747, S_tw .759. S_tw − ¾log g settles at 0.166. The exponent d/4 = 3/4 is for the **full link dimension Σ_{n≤N}(n+1)²**. The shell count N, i.e. the typical 2j, has exponent 1/4. |
| E1 "uniform in box", lattice vacuum | NOT CHECKED numerically | One rotor is not the cubic vacuum. A single rotor is in a pure state with reduced rank 1. Only the gauge twirl (σ_e is uniform on each (n+1)² block) turns the shell law into rank ~ g^{3/4}. I read the analytic proof but did not test it. |
| E2 clocks | STANDS, with a wording defect (E5) | Magnetic clock: t = τ/λ = τb/β. Mesh clock: t = τb. Both go to 0 in physical time with β fixed and with β = c log(1/b). At b = 1e-4, c = 1: 5e-5 (β = 2), 1.1e-5 (β = log) and 1e-4 (mesh). λb = β grows, so magnetic energies are about β/b and mesh energies about 1/b. |
| E3 class-probe floor | STANDS | λh² = √2/b exactly; β drops out (P6, error 2e-16). M = 2√2Σs_i² is dimensionless and τM/v is dimensionless. The width s·g^{-1/4} matches the rotor width n ~ g^{1/4}. The Jensen step held in 2000/2000 random cases. The floor is spectral weight ≥ v/2 of Q at energies ≤ 2M/(v b), which is the cutoff scale and diverges as b → 0. It is not a physical mass. |
| E4 center-flux algebra at fixed physical time | STANDS under hypotheses that the README omits | The bound is 16(K−1)u/v* + e^{−tλV_min/2}. Its hypotheses: g → ∞ (β → ∞, so that u ≤ C/√g → 0), and a marked set **fixed in lattice units**, which is K fixed. With those, it is uniform in volume. b → 0 is not needed (only tλ → ∞). With β fixed it does not follow (8u stays). For a set fixed in physical units, K ~ 2^{#links ~ (L/b)³} and Ku → 0 fails, so nothing is proved. |
| E5 summary sentences vs theorems | DEFECT (wording, three sentences) | See section 3. |

Verdict counts: **STANDS 4, DEFECT 1, NOT CHECKED 1.**
Predicate counts across both programs, mine plus the child's rerun: **met 18, failed 1, measured only 2** (the slope table and the clock table).

## 2. Hypotheses used and where they are stated

- **Dimension and entropy** (dimension.md):
  - G is compact, connected and simple, with d > 2. "d>2 is essential."
  - ρ has injective differential.
  - The lattice is a periodic cubic box of side ≥ 3.
  - The vacuum is the unique positive vacuum (Feynman–Kac).
  - Trial bounds K_e ≤ C√g_G and u_p ≤ C/√g_G, from symmetry and equal link and face counts.
  - Gauge twirl at the endpoints.
  - The joint version needs a forest, with each marked edge having a private incident plaquette.
- **Shells** (shells.md): the budget B(g) = min(g, 17√g/8 + 3/16) and the matching g = β²/2. Compactness holds only along subsequences; uniqueness of f is not claimed.
- **Center** (center.md):
  - u = max_p⟨v(U_p)⟩ → 0, which requires g → ∞.
  - v* > 0 (nonflat central values).
  - "fixed marked geometry" (lattice units).
  - F is the lattice's own flat subgroup.
  - For the algebra statement, K = |A/F| with Ku → 0.
  - Physical time: "b↓0 and β→∞".
- **Class probes** (class-probes.md): SU(2) in the defining representation. Distinct s_i > 0, with v and g_0 obtained by contradiction (existence only). Matching κ = 2/(βb), λ = β/b. Time τb at each cutoff.

## 3. Sentences stronger than or mixed with their theorem (E2/E5)

1. **README:** "On fixed positive physical times the connected weight of the whole bounded local center-flux algebra vanishes along bare refinement."
   - The theorem needs β → ∞, and "local" means fixed in lattice units. Physically that is a region of size about b.
   - "Along bare refinement" read as b → 0 at fixed β is not proved.
   - center.md's own version ("on the weak-bare trajectory") is correct.
2. **README:** "On the longer time scale set by the spatial mesh b, a different family retains an absolute positive signal."
   - The time τb is "longer" only relative to b/β. It goes to 0 physically, so "survives" means at energies of order 1/b.
   - class-probes.md does say "As b↓0 that time vanishes." The README summary leaves this out.
3. **class-probes.md opening:** "The central sign … loses its connected signal at positive physical time. There is a different family … with a nonzero absolute signal on the longer spatial mesh clock."
   - This mixes a fixed-physical-time statement with a τ-clock statement, and it invites the reading that the probes survive where center flux dies.
   - In fact center flux also dies at mesh times. At t = τb, tλ = τβ → ∞, so the bound 8u + e^{−τβk} → 0.
   - The two statements are not contradictory, but they are not comparable as written.

All other statements in center.md carry consistent clocks:
- "microscopic time t = τ/λ"
- "times b/β in the bare convention"
- "ultraviolet energy 8λ"
- "any fixed positive physical time when b↓0 and β→∞"

Scope-limiting sentences D4 does write, quoted:
- README: "Constructing continuum correlation functions at nonzero physical separations, identifying a nontrivial limiting theory, and bounding the bottom of its excited spectrum remain open. A link-basis fidelity threshold also does not bound errors in a Ritz gap."
- class-probes: "As b↓0 that time vanishes. A positive lower bound at a fixed nonzero physical separation, or a lower edge of the continuum excitation spectrum, would require further information." Also: "This is an existence bound; it does not specify an optimal v."
- center: "It concerns these particular unit vectors. Concluding that the whole theory has no low-energy states would require control on other probes…" Also: "identifying it with a physical mass would give the wrong clock and the wrong sector." Also: "dividing a correlator by a vanishing variance can change that conclusion."
- shells: "Neither uniqueness of the rescaled density nor convergence of the four-dimensional dynamics follows from this estimate."
- dimension: "it supplies no physical-distance decay estimate." Also: "Gauge fixing on a maximal tree changes those factors, and approximating selected energy levels is a different criterion."

## 4. Failed predicates

- **check_e1e3.py P1:** "doubling the basis changes E0 by < 1e-10 (absolute)". It failed: |ΔE0| = 2.7e-10 at g = 1e6. Relative to E0 ≈ 2.1e3 that is 1.3e-13. **My own expectation was wrong:** eigensolver roundoff scales with ‖H‖ ~ g. This is not a defect of the target. The child's relative-tolerance version of the same check passed.
- P2 passed only narrowly: 0.0196 against a tolerance of 0.02 at g = 1e3. That tolerance was my own guess, not a derived bound.

## 5. Not checked

- The lattice vacuum itself, beyond the one-rotor proxy. No cubic-lattice numerics.
- The twirl trace identity and the δ ↓ 0 limit in dimension.md.
- The Hörmander counting constants.
- The Gegenbauer coefficient.
- The Hardy/Schur constant 6.
- The 32-pattern and rate enumeration (8, 12, 16 with multiplicities 6, 16, 9).
- The Lean module and D4's hashes (files not provided).
- Whether F (and so K) is box-independent for marked sets that wrap a side-3 torus.

## 6. Delegated question and outcome

- **Question.** Single SU(2) rotor, H/κ tridiagonal with diagonal n(n+2) + g and off-diagonal −g/2. Compute N_q, Dim_q and S_tw for g from 1 to 1e6, and fit slopes on [1e2, 1e4]. Control question: the smallest eigenvalue of [[2,1],[1,2]].
- **Outcome.**
  - Control answer 1.0 (correct).
  - 9/9 predicates passed.
  - Slopes 0.2557, 0.2605, 0.7240, 0.7472, 0.2529, 0.7585.
  - Child register verify PASS.
- **My rerun.** I reran it in `rerun_child/` under my own register (event K2, exit 0). The slopes were identical, and they also match my independent program to 3 decimals.

## 7. Rerun commands (from C:/Users/donke/z4-workers/r6-elec, Bash, PYTHONUTF8=1)

```sh
export PYTHONUTF8=1; P=C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py
python $P check --ws pcp --name check_e1e3 --expect-exit 1 -- python check_e1e3.py   # exits 1 because of P1; writes a new results_e1e3_N.txt
(cd rerun_child && python $P check --ws ../pcp --name rerun_child_rotor --expect-exit 0 -- python rotor.py)
python $P verify --ws pcp
```

Note: the first check was registered with --expect-exit 0 and recorded "exit 1 (expected 0)", because P1 failed.

`verify --ws pcp` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

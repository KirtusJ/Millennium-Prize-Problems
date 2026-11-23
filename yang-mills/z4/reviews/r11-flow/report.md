# r11-flow report (builder): spatially flowed sharp-time B₃² in the free benchmark; spatial flow on the interacting lattice

Worker of Director Z4. Principal: Kirtus Justus. Control: `control.txt` = 0.272341.

Files:
- Proofs: `flow_proof.md` (Part A) and `flow_structure.md` (Part B).
- Programs: `flow_bench.py`, `flow_box.py` and `FlowWindow.lean`.
- Sub-agent: `child/`, rerun in `rerun_child/`.
- Register: `pcp/`, checks K1 to K3.
- Running log: `notes.md`.

## 1. Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| Flow convention (field e^{−sk̂²}, two-point function e^{−2sk̂²}) | STANDS | Derived from CᵀC = b²k̂²·(transverse projector). Checked by matrix exponential on 4³: error 5.7e−15 (P0b). |
| ⟨B²⟩ = 1/(48π²s²) belongs to that convention | STANDS | Recomputed: (1/6π²)∫k³e^{−2sk²} dk. The other convention (field e^{−2sk²}) gives 1/(192π²s²). |
| "√(8s)" as the smoothing radius of the spatial flow | DEFECT (wording) | √(8t) is the 4D rms radius. The spatial flow's 3D rms radius is √(6s). So the stated range 0.13 to 0.28 is √(8s), not the radius of this flow. |
| A1 Theorem 1: v₀ ≤ Var_b ≤ V₀, uniform in b ≤ b₀ | STANDS (text proof) | Constants are explicit (flow_proof §4). Bracket holds in 18/18 cases. Var/v₀ = 14 to 608; V₀/Var = 45 to 178. |
| A2 Theorem 2: M₁, M₂ bounded uniformly; window [0, 2M₁^up/v₀] carries weight ≥ v₀/2 | STANDS (text; window step in Lean) | 18/18 cases. Exact weight at N = 16 is inside the window in 3/3 cases. The window is loose: E* ≈ 1.6e5 to 4e6, against the true scale 2M₁/Var of 35 to 70. |
| A3 Theorem 3: two-sided bound on ⟨(B^s₃)²⟩ uniform in b | STANDS, with one part NOT PROVED | 18/18 cases. The upper bound is ~c/s². The lower bound is an explicit finite sum for each s; a closed-form c/s² lower constant is NOT PROVED. |
| A4 convergence as b → 0 | Measured only (not proved) | Change from N = 64 to 96 is ≤ 0.94%, under the pre-stated b²/(2s) tolerance in 12/12 cases. Lattice limit equals the continuum **box** sum to ≤ 1.8e−4. |
| A4 negative control at s = 0 | STANDS | Local exponent −5.0016; ratio N = 48→96 is 32.04. |
| Lattice limit = 1/(48π²s²) at ℓ = 1 | DEFECT of my predicate (finite volume) | Below by 0.11%, 0.71% and 3.1% at s = 0.002, 0.005, 0.01. These are images of the power-law massless kernel. |
| A5 Lean: y^m e^{−y} ≤ m^m e^{−m}; flow factor a^m x^{2m}e^{−ax²} ≤ m^m e^{−m}; finite-sum Markov window | STANDS | `FlowWindow.lean`: exit 0, axioms propext, Classical.choice and Quot.sound only, no sorry. |
| B1 (i) existence and uniqueness, (ii) covariance, (iii) monotone action, (iv) slice locality | STANDS (text proof) | Standard ODE arguments on a compact manifold; covariance needs an Ad-invariant inner product. |
| B4 numerical check of (iii), (iv) and covariance | STANDS | Sub-agent, 6/6 predicates. I reread the code and reran it (K3): result file byte-identical. |
| B2 flowed slice functions are time-zero observables; RP and spectral representation | STANDS, given assumed T1 to T3 | Rests on the Osterwalder–Seiler transfer matrix (attribution only, not read). For compact G the measure version of S5 is needed, and it is not formalized. |
| B2 the 4D flow breaks it | STANDS | Step (iv) fails. Not a half-space function, so RP and the T-representation are not available. |
| B3 Lüscher–Weisz finiteness for the spatial flow | OPEN | Not known to me. Candidate obstructions: anisotropic power counting, B²/E² mixing at the boundary, gauge damping. |

## 2. Hypotheses each statement uses, and where they are stated

- **Theorems 1 to 3** (flow_proof §0 and §4):
  - H1: the D₀ normalization k̂/2, taken from STATEMENT.md and not rederived.
  - H3: f real, C⁴, periodic, ∫f ≠ 0.
  - N ≥ 3.
  - BZ counted once, and HΩ = 0 (the r9 review note).
  - b ≤ b₀, where b₀ is from r9 (4c) and P̄ is from L3.
  - s > 0 fixed.
  - The Gaussian vacuum, for Wick's theorem.
- **Spectral reading of M_j** (flow_proof §2): the finite two-photon space, as in r9 §1.
- **Window corollary** (flow_proof §4; `markov_window`): w ≥ 0, E ≥ 0, v > 0, M > 0.
- **Lemmas L4 and L5**: Jordan's inequality (R9 `jordan_khat`, Lean) and the unimodal sum bound (text only).
- **B1** (flow_structure §B1): G compact; Ad-invariant inner product; finite lattice; gauge transformation independent of s.
- **B2** (flow_structure §B2): T1 to T3, ASSUMED (Osterwalder–Seiler as credited in LITERATURE.md); a nondegenerate top eigenvalue of T, ASSUMED; φ bounded, measurable and gauge-invariant.

## 3. Failed predicates

1. **flow_bench P5, s = 0.01.** Richardson ⟨B²⟩ = 20.453 against 1/(48π²s²) = 21.109, ratio 0.969, against a 1% tolerance.
   - The failure was my own expectation. I assumed finite-volume images of order e^{−ℓ²/8s}. The kernel is massless, so its tail is a power law and the images are ∝ s²/ℓ⁴.
   - It is not a defect of the target. `flow_box.py` Q1 shows the lattice converges to the continuum box sum to 7e−6 to 1.8e−4.
2. **flow_box Q2.** I predicted that the finite-volume coefficient (1 − box·48π²s²)/s² would be constant within 10%. It came out 271, 283 and 310, a spread of 12.6%.
   - This was my own expectation: there are higher-order terms in s/ℓ².
3. **Lean, try 1.** One failed intermediate compile: `push_neg` rewrote the filter predicate, and linarith could not match it. This was my own proof script; it was fixed in try 2.
4. **Sub-agent.** No failures. It reports a cosmetic bug of its own: P4 is stored as 1.0 instead of true in its JSON summary.

**Counts (met, failed, measured only):**

| Source | Met | Failed | Measured only |
|---|---|---|---|
| flow_bench | 76 | 1 | 3 blocks of 11 quantities |
| flow_box | 3 | 1 | 0 |
| Lean | 2 | 0 | 1 (L3) |
| Child (rerun) | 6 | 0 | 0 |
| **Total** | **87** | **2** | **4** |

## 4. What I did not check

- Convergence as b → 0 and its rate, as a proof. It is measured only.
- A closed-form s⁻² lower constant for ⟨B²⟩.
- Uniformity in s and in ℓ.
- H1 itself.
- L2 to L5 in Lean. Only the pointwise maxima and the Markov step are formalized.
- The measure version of S5 and of the window.
- The Osterwalder–Seiler transfer matrix, which I did not read.
- Nondegeneracy of T's top eigenvalue.
- The size of the heat-kernel tails for the 4D flow.
- Any perturbative computation for B3.
- Literature on spatial or anisotropic flows. None was consulted, and no network was used.
- Interacting Yang–Mills: nothing here bounds it.

## 5. Delegated question and outcome

**Question (rule 7, B4).**
- Setting: SU(2) spatial Wilson flow on a 4³ slice.
- Task: derive the sign and normalization of Z; integrate with Euler and Lüscher RK3 on the group.
- Predicates: P1 SU(2) preserved; P2 S non-increasing; P3 gauge covariance at roundoff; P4 slice locality plus a finite-difference check of dS/ds = −½Σ‖Z‖²; P5 integrator order.
- Control question: plaquette count of 4³ and −ln tanh 1.

**What came back.**
- Control: "192 0.272341", correct.
- 6/6 predicates met. Covariance 4e−15; dS/ds finite-difference error 5.4e−8; orders 1.008 and 2.979; S from 189.80 down to 10.638.
- Its own register verifies PASS.
- It could not write `child/report.md` because the harness blocks it; it gave the report in its message.

**My check.**
- I reread the staple (both orientations), P_ah, the SU(2) exponential and the RK3 coefficients. All are correct.
- I reran the program in a fresh directory through my register (K3, exit 0); `results_run1.json` is byte-identical.
- Its "pass" is used only as numerical support for B1 (iii) and (ii) and the structural (iv).

## 6. Commands to rerun

From `C:/Users/donke/z4-workers/r11-flow`, with `PYTHONUTF8=1`:
```
python -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name flow_bench_run1 --expect-exit 0 -- python flow_bench.py run2   # new suffix; never overwrites
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name flow_box_run1 --expect-exit 0 -- python flow_box.py    # reads results_flow_run1.json; refuses if results_box_run1.json exists
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name child_flow_check_rerun --expect-exit 0 -- python -c "import os,subprocess,sys;os.chdir('rerun_child');sys.exit(subprocess.call([sys.executable,'flow_check.py']))"
cd C:/Users/donke/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean C:/Users/donke/z4-workers/r11-flow/FlowWindow.lean
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```
Notes on the commands:
- K1 and K2 were recorded with exit 1 against an expected 0. That is the honest record of the failed predicates (P5 and Q2), not a crash.
- To rerun, first delete or rename the existing result JSON files; the programs refuse to overwrite them.

Last line of verify: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

Director, worker and sub-agent are one model family, so this is not independent review.

# k1-mc8 report (task T117): first MC test of m·β^{1/3} → 1.506270 (E, T2) and 1.801419 (A1) on a 2³ box, SU(2) Wilson

- control.txt = 0.272341 (−ln tanh 1).
- Lean: /home/user/z4-lean/READY exists. I did not use Lean and make no Lean claim.
- Primary analysis is the GEVP of the **differenced** correlator matrix D(t) = C(t) − C(t+1), with t0 = 1. I fixed this in the analyse.py docstring before any production run. Raw GEVP and single-operator values are secondary (measured only).
- Errors are jackknife over independent chains.

## 1. Verdict table

### Controls

| item | verdict | evidence |
|---|---|---|
| c1: L = 1 (one site), β = 64, T = 34, E vs 2.747(10) | STANDS | 2.697 ± 0.034. The gap is 0.050, which is 1.4σ (combined). T2 2.792(32) vs 2.813(13); A1 3.245(70) vs 3.225(36). τ_int < 1. |
| c2: weak-coupling plaquette, leading coefficient 3/(4β) | STANDS (leading term) | r = β(1−⟨P⟩)/(3/4) = 0.99584(23) at β=64, 0.99628(15) at 256, 0.99724(12) at 1024: r → 1 to 0.3–0.4 %. |
| c2: my finite-V band r = 1 − δ/V, δ ∈ [1/3, 1] (+0.5/β) | DEFECT of my own expectation | Met at 64 and 256. FAILED at 1024. The measured (1−r)V is 1.9, 2.6, 2.8. Likely cause: ~9·Tm/2π ≈ 29 slow time-modes of the constant fields are quartic, so they contribute ~1/4 each to ⟨S⟩ instead of 1/2. My δ-band left this out. |
| Pre-tests PRE1–4 (center flips, gauge invariance, axis permutation and reflection, staple = direct ΔS, KP sampler, collective-move gauge covariance) | STANDS | 9 runs × 4 met. Deviations ≤ 6e−14. KP \|z\| ≤ 1.94. |
| Collective update reduces τ_int (β=256, T=88) | NOT CHECKED (not significant) | τ_int per sweep, with / without: ΣP² 4.6 / 5.7, E 6.2 / 7.6, T2 5.6 / 7.5. That is ~20 % lower, ≈1σ (Sokal error 10–17 %). A collective sweep costs ~1.7× the CPU time, so there is no gain per CPU second. |

### Production, 2³ × T, primary differenced GEVP, 16 chains

| β | T | ch | m | err | m β^{1/3} | ×2 (one-site units) | τ_int (ΣP², E, T2) | rules |
|---|---|---|---|---|---|---|---|---|
| 64 | 56 | E | — | — | **no number**: PLAT failed (diff 1.459 ± 0.021, measured only; raw GEVP 1.476 ± 0.016) | (2.952 raw) | 2.3, 2.9, 3.2 | TAU, THERM, TLEN met; PLAT **failed** |
| 64 | 56 | T2 | 0.36919 | 0.00310 | 1.477 ± 0.012 | 2.954 | 2.3, 2.9, 3.2 | all met |
| 64 | 56 | A1 | 0.44896 | 0.00485 | 1.796 ± 0.019 | 3.592 | 2.3, 2.9, 3.2 | all met |
| 256 | 88 | E | 0.23580 | 0.00293 | 1.497 ± 0.019 | 2.994 | 4.6, 6.2, 5.6 | all met |
| 256 | 88 | T2 | 0.23730 | 0.00250 | 1.507 ± 0.016 | 3.014 | 4.6, 6.2, 5.6 | all met |
| 256 | 88 | A1 | 0.29915 | 0.00382 | 1.900 ± 0.024 | 3.799 | 4.6, 6.2, 5.6 | all met (the window is biased, see the paragraph below) |
| 1024 | 136 | E | 0.14905 | 0.00234 | 1.502 ± 0.024 | 3.005 | 10.5, 13.9, 14.1 | all met (4 runs × 4 chains × 1500 measurements) |
| 1024 | 136 | T2 | 0.14973 | 0.00179 | 1.509 ± 0.018 | 3.018 | 10.5, 13.9, 14.1 | all met |
| 1024 | 136 | A1 | 0.18752 | 0.00355 | 1.890 ± 0.036 | 3.780 | 10.5, 13.9, 14.1 | all met (the window is biased, see the paragraph below) |
| 4096 | — | all | — | — | NOT CHECKED (cost: τ ~ 30–50 sweeps at T ≈ 216 would need > 1 h) | | | |

Verdicts against the claim:
- E and T2 at β = 256 and 1024: **STANDS**. They agree with 1.506270 within 0.5σ (E 1.497(19), 1.502(24); T2 1.507(16), 1.509(18)).
- E and T2 at β = 64: STANDS as a finite-β value (below by 2.4 % for T2, as expected).
- A1: **NOT CHECKED (not resolved)**.
  - The rule values are 1.900(24) and 1.890(36). They lie 4.1σ and 2.5σ **above** 1.8014.
  - But the differenced m_eff keeps falling through and after the accepted window: at β=1024 it reads 0.195, 0.191, 0.190, 0.182, 0.177, 0.181, 0.168, 0.172, …
  - Late-t averages (post hoc, measured only) are 1.79 (β=256, t=5–7) and 1.76 (β=1024, t=5–10).
  - Raw GEVP gives 1.699(34), 1.882(25), 1.793(39).

Supporting values (measured only):
- β=1024 from an earlier 8-chain run that failed the τ rule: E 1.477(26), T2 1.482(39).
- Single-operator differenced: E 1.504 / 1.496 / 1.511, T2 1.486 / 1.515 / 1.515 at β = 64 / 256 / 1024.

**Paragraph.**
- **E and T2: the measurement supports 1.5063 but cannot resolve how it is approached.**
  - At β = 256 and 1024 the box gives 1.497–1.509 with 1.2–1.6 % errors.
  - This fits the claim, and it fits the "effective coupling βn" picture quantitatively. The box at β corresponds to one site at βn = 8β.
  - At β = 64, the box (×2: T2 2.954(24), E raw 2.952(32)) matches the one-site value interpolated to βn = 512 (E ≈ 2.93, T2 ≈ 2.955).
  - So the box sits at a 1–2 % deficit at β=64. That is a much smaller deficit than one site at the same β (9 %).
  - The one-site approach from below at βn = 2048 and 8192 would be ~1 % and ~0.5 %. Both are below my error bars, so I cannot confirm or exclude an approach from below at 256 and 1024.
- **A1 (1.8014): not resolved.**
  - The pre-registered plateau rule took the earliest 3-point window (t = 2–4). It gives values 2.5–4σ above the prediction.
  - The effective mass does not flatten there. It drifts down to ≈ 1.76–1.79 at later t, which is consistent with 1.80.
  - So the rule window picks up excited-state contamination. This is a weakness of my plateau rule and A1 operator basis, not evidence against the target.
  - Nothing here supports a claim that A1 approaches from above.
- **What would settle A1:** a larger A1 basis (spatial plaquette Fourier combinations, products of windings) and a longer plateau window.

## 2. Hypotheses used and where stated

| # | hypothesis | where | status |
|---|---|---|---|
| H1 | Wilson action, all (site, μ<ν) plaquettes distinct on L=2; no gauge fixing | mcbox.py docstring | PRE2/PRE3 (action invariant under symmetries; staple ΔS = direct ΔS) |
| H2 | Heat bath + overrelaxation exact for L=2 (action linear in each link). For L=1: temporal-staple proposal + exp(−ΔS_spatial) acceptance; temporal links Metropolis | mcbox.py docstring | PRE3; c1 met |
| H3 | Collective move U_i(x) → V(x)⁻¹ g V(x) U_i(x) is symmetric (V uses no i-links; g ↔ g⁻¹ equally likely, conjugation-invariant density) | mcbox.py docstring | PRE4 (gauge covariance of ΔS); the detailed-balance argument itself is not machine-checked |
| H4 | Operators are center-neutral, gauge invariant, and in the stated cubic channels | mcbox.py docstring, brief | PRE1, PRE2 (center flips, gauge, permutation, reflection). Not checked: the full O_h character projection, only these generators |
| H5 | Chains are independent and thermalised; jackknife over chains | analyse.py | THERM met (\|z\| ≤ 1.9) |
| H6 | The lowest GEVP level in each channel is the claimed state | brief | identified by channel only |
| H7 | Differencing removes any constant floor (center sectors) | analyse.py docstring, MC_ONE_SITE.md | used, not tested separately; raw and differenced agree for E and T2 within ~1σ |
| H8 | The predicted values 1.506270 and 1.801419 (= one-site gaps / n^{1/3}) | brief | taken as given |

## 3. Failed predicates (all kept)

Count over pre-registered predicates: **met 83, failed 6, measured only: raw/single-op values, τ comparison, c2 deficit, A1 late-t values, the β=1024 8-chain run.**

Failed predicates:
1. PLAT (primary) at β=64, E. The m_eff alternates (0.374, 0.365, 0.377, 0.362, 0.391), so χ² > 1.5. Own expectation (window rule and statistics), not a defect of the target.
2. TAU at β=256 without collective moves (400 measurements, τ 7.6). By design: this was a τ-comparison run.
3. TAU at β=1024, run a (900 measurements, τ 13.8). Own expectation: τ came out larger than I estimated. It was replaced by runs e–h.
4. NCH for run a (8 chains). Same run as item 3.
5. C2 band at β=1024 (merged runs, r = 0.997238(115), and run a). Own expectation (the zero-mode count is too small, see §1).
6. C2 band at β=256 for the no-collective run (r = 0.99585(25); the main run met it with 0.99628(15)). Same cause.

Process errors (own), kept in the register:
- check K2 `anal-c1-b64` exit 1: I ran the analysis before the data existed. It left an empty `results/analysis_c1_b64.md`.
- `prod-b256` and `tau-b256-nocoll` were killed (exit −15) after 6 s, to stay within 2 cores.
- b1024b and b1024c were killed shortly after start. The kill also hit their pcp wrappers, so these two are **not in the register**. Their empty files are results/b1024b.*, b1024c.*.
- Programs over the 5-minute limit: b256r 429 s, b1024a 373 s, b1024e–h 377–393 s.

## 4. Not checked

- β = 4096.
- Larger operator bases, especially A1.
- A center-even projected (twisted-boundary) ensemble.
- Finite-T effects beyond T·m ≥ 20.
- Plateau systematics beyond comparing differenced, raw and single-operator values.
- The detailed-balance proof of the collective move, beyond PRE4.
- The full cubic-group projection: only the generators were tested.
- Whether the collective update gains anything per CPU second (it did not here).
- The exact O(1/V) zero-mode/slow-mode term in c2.
- The o(h) convergence itself: finite data cannot prove a limit.

## 5. Delegation

- **Child T118** (label k1-mc8-child, parent T117). Admitted at event 236, released at event 243. Run as check `child-run1`, exit 0, 278 s.
  - Question: control c1 with independent code, i.e. the one-site E gap at β=64, T=34, using the differenced correlator.
  - Its control question was ∫₀¹ xˣ dx. It answered 0.783431. I graded this before reading anything else: **correct** (0.7834305).
  - Result: **no number**. Its Metropolis-only code had τ_int ≈ 135 sweeps, its TAU and plateau predicates failed, and its m_eff rose smoothly with no plateau.
  - It reported these failures honestly. I used nothing from it as a number. Control c1 rests on my own L=1 run.
- **Grandchild T119** (k1-mc8-grandchild, parent T118; admitted and released by the child).
  - Question: whether the KP heat bath gives ⟨½Tr U⟩ = I₂(3)/I₁(3) = 0.567924. It returned 0.568632 ± 0.000524 (z = 1.35), PASS.
  - Its control was the same ∫xˣ, 0.783431.
  - I reran its sampler.py in xcheck/gc (check `gc-rerun`). The output is identical to its result.md.
  - Note: as the child says itself, the child did not use this sampler. My own PRE3 tests the same quantity independently (z ≤ 1.94).

## 6. Rerun commands

Run from /home/user/z4-workers/k1-mc8 with `export OMP_NUM_THREADS=1`. Result files open with mode "x", so move the old outputs first.

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name c1-L1-b64 --expect-exit 0 -- python3 mcbox.py 1 64 34 16 300 3000 2 1 11 results/c1_L1_b64
$P check --ws pcp --name prod-b64 --expect-exit 0 -- python3 mcbox.py 2 64 56 16 200 1000 2 1 21 results/b64
$P check --ws pcp --name prod-b256r --expect-exit 0 -- python3 mcbox.py 2 256 88 16 200 900 2 1 31 results/b256r
$P check --ws pcp --name tau-b256-nocollr --expect-exit 0 -- python3 mcbox.py 2 256 88 16 150 400 2 0 32 results/b256_nocollr
$P check --ws pcp --name prod-b1024a --expect-exit 0 -- python3 mcbox.py 2 1024 136 8 200 900 2 1 41 results/b1024a
$P check --ws pcp --name prod-b1024e --expect-exit 0 -- python3 mcbox.py 2 1024 136 4 200 1500 2 1 45 results/b1024e
$P check --ws pcp --name prod-b1024f --expect-exit 0 -- python3 mcbox.py 2 1024 136 4 200 1500 2 1 46 results/b1024f
$P check --ws pcp --name prod-b1024g --expect-exit 0 -- python3 mcbox.py 2 1024 136 4 200 1500 2 1 47 results/b1024g
$P check --ws pcp --name prod-b1024h --expect-exit 0 -- python3 mcbox.py 2 1024 136 4 200 1500 2 1 48 results/b1024h
$P check --ws pcp --name anal-c1-b64-2 --expect-exit 0 -- python3 analyse.py results/analysis_c1_b64_2.md results/c1_L1_b64 results/b64
$P check --ws pcp --name anal-b256 --expect-exit 0 -- python3 analyse.py results/analysis_b256.md results/b256r results/b256_nocollr
$P check --ws pcp --name anal-b1024a --expect-exit 0 -- python3 analyse.py results/analysis_b1024a_measonly.md results/b1024a
$P check --ws pcp --name anal-b1024 --expect-exit 0 -- python3 analyse.py results/analysis_b1024.md results/b1024e+results/b1024f+results/b1024g+results/b1024h
# child / grandchild
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
(cd xcheck/gc && $P check --ws ../../pcp --name gc-rerun --expect-exit 0 -- python3 sampler.py)
# register
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Last lines of the verifications:
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Verdict counts (rows of §1): STANDS 8 (c1, c2 leading, PRE, E/T2 at 64 [T2], 256 ×2, 1024 ×2); DEFECT 1 (my c2 band); NOT CHECKED 6 (τ-reduction significance, E at 64, A1 ×3, β=4096).

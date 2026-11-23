# i1-mc3 report (task T98): MC test of m·β^{1/3} → 3.0125 (E, T2) and 3.6028 (A1); one site, three directions, SU(2)

- Control: control.txt = 0.272341 (−ln tanh 1).
- Lean: /home/user/z4-lean/READY exists, but I did not use Lean. I make no Lean claim.

## 1. Verdict table

### Controls

| item | verdict | evidence (one line) |
|---|---|---|
| Operator/action identities PRE1–PRE3 (11 production runs) | STANDS | ½Tr comm formula dev ≤ 1e−15. KP heat bath ⟨x0⟩ at k=3, \|z\| ≤ 1.6. Center-flip, conjugation and permutation/reflection invariance ≤ 3e−15. |
| D=3, β=1, exact m_e = 2.876117 | NOT CHECKED (plateau rule fails) | GEVP with t0=0: m_eff(0) = 2.8718(60), m_eff(1) = 2.810(92). Consistent with exact (measured only). Signal is lost at t ≥ 2, so no plateau. |
| D=3, β=2, exact 1.621505 | STANDS | ctrl0 (GEVP t0=0): 1.6291 ± 0.0132, z = +0.58. Differenced: 1.6283 ± 0.0150. Child, independent code: 1.620 ± 0.013. |
| D=3, β=4, exact 0.96893: raw correlator, T=24 | DEFECT of my method (see §2) | Constant floor ≈1.3% of C(0) for t ≥ 7, so m_eff → 0. The child's independent Metropolis code shows the same floor (2.2% at T=16). |
| D=3, β=4: differenced correlator C(t)−C(t+1) (post hoc) | STANDS | T=24: 0.9802 ± 0.0110 (z = +1.0). T=48: 0.96904 ± 0.00380 (z = +0.03). |
| β=4: next exact level 1.184132 | STANDS (measured) | It is the A1 level: A1 (T=48, differenced) gives m_eff(1) = 1.1885(83). Likewise at β=2: A1 1.935(24) vs exact next level 1.928516. |
| D=2, β=256, pipeline control m_e β^{1/3} = 1.887 | STANDS | 1.9019 ± 0.0084 (z = +1.76). Differenced: 1.9061 ± 0.0080. The 2D lattice channels B1/B2 are degenerate (1.902 vs 1.907), as O(2) requires. |

### Main measurement, D=3

- m and its error are from the pre-registered analysis (GEVP of 4 operators, t0 = round(β^{1/3}/6), plateau rule in the mc3.py docstring).
- The bracket column gives the differenced (post-hoc) value of m·β^{1/3}.
- τ_int is in sweeps, for: slice-averaged Σs_i / E op / T2 op.
- Every row has 32 independent chains, and errors are jackknife over chains.

| β | T | channel | m | err | m β^{1/3} | [differenced] | τ_int | plateau |
|---|---|---|---|---|---|---|---|---|
| 64 | 34 | E | 0.68683 | 0.00256 | 2.747 ± 0.010 | 2.741 ± 0.011 | 1.0/1.5/1.2 | met |
| 64 | 34 | T2 | 0.70329 | 0.00314 | 2.813 ± 0.013 | 2.829 ± 0.011 | 1.0/1.5/1.2 | met |
| 64 | 34 | A1 | 0.80630 | 0.00889 | 3.225 ± 0.036 | 3.231 ± 0.031 | 1.0/1.5/1.2 | met |
| 256 | 54 | E | 0.45694 | 0.00174 | 2.901 ± 0.011 | 2.921 ± 0.007 | 1.6/2.3/2.0 | met |
| 256 | 54 | T2 | 0.46277 | 0.00105 | 2.938 ± 0.007 | 2.933 ± 0.008 | 1.6/2.3/2.0 | met |
| 256 | 54 | A1 | 0.54381 | 0.00254 | 3.453 ± 0.016 | 3.449 ± 0.016 | 1.6/2.3/2.0 | met |
| 1024 | 84 | E | 0.29313 | 0.00084 | 2.955 ± 0.009 | 2.976 ± 0.008 | 2.9/4.0/3.8 | met |
| 1024 | 84 | T2 | 0.29493 | 0.00075 | 2.973 ± 0.008 | 2.980 ± 0.010 | 2.9/4.0/3.8 | met |
| 1024 | 84 | A1 | 0.34965 | 0.00164 | 3.524 ± 0.017 | 3.519 ± 0.016 | 2.9/4.0/3.8 | met |
| 4096 | 134 | E | 0.18698 | 0.00078 | 2.992 ± 0.013 | 2.992 ± 0.012 | 6.2/8.0/8.1 | met |
| 4096 | 134 | T2 | 0.18679 | 0.00082 | 2.989 ± 0.013 | 3.001 ± 0.011 | 6.2/8.0/8.1 | met |
| 4096 | 134 | A1 | 0.22152 | 0.00167 | 3.544 ± 0.027 | 3.580 ± 0.024 | 6.2/8.0/8.1 | met |
| 16 (extra) | 22 | E / T2 / A1 | 0.926 / 1.038 / 1.090 | 0.015 / 0.007 / 0.016 | 2.33 / 2.62 / 2.75 | 2.42 / 2.57 / 2.81 | 0.9/1.3/0.9 | met / met / FAILED |
| 16384 (extra) | 212 | E | 0.11763 | 0.00092 | 2.988 ± 0.023 | 3.001 ± 0.018 | 11.8/16.3/15.8 | met |
| 16384 (extra) | 212 | T2 | 0.11749 | 0.00092 | 2.984 ± 0.023 | 2.957 ± 0.029 | 11.8/16.3/15.8 | met |
| 16384 (extra) | 212 | A1 | 0.14047 | 0.00189 | 3.568 ± 0.048 | 3.557 ± 0.035 | 11.8/16.3/15.8 | met |

The prediction-level checks, all fixed before the first run:

| check | result | values |
|---|---|---|
| LIM: \|m β^{1/3}/e − 1\| ≤ 0.08 at β=4096 | met in all three channels | E −0.7%, T2 −0.8%, A1 −1.6% |
| MONO: deviation shrinks from β=64 to β=4096 by more than 2σ | met for E and T2; also met for A1 (measured only) | E 0.265 → 0.021; T2 0.199 → 0.024; A1 0.378 → 0.059 |
| TLEN: T·m_lowest ≥ 20 for β ≥ 64 | met | — |
| THERM | met in every run | \|z\| ≤ 1.9 |
| TAU: N_meas ≥ 50 τ_int | met in every run | — |

E–T2 splitting (m_T2 − m_E)·β^{1/3}, measured only:

| β | splitting |
|---|---|
| 16 | +0.28 ± 0.04 |
| 64 | +0.066 ± 0.014 |
| 256 | +0.037 ± 0.012 |
| 1024 | +0.018 ± 0.011 |
| 4096 | −0.003 ± 0.018 |
| 16384 | −0.004 ± 0.025 |

**Paragraph.** The measurement supports both limits:
- **E and T2 (J=2):** m·β^{1/3} rises monotonically from below: 2.75/2.81 (β=64), 2.90/2.94, 2.955/2.973, 2.992/2.989 (β=4096). At β=4096 it is 0.7–0.8% under 3.0125 (≈1.6σ).
- **A1:** 3.23 → 3.45 → 3.52 → 3.544 ± 0.027, which is 1.6% under 3.6028 (≈2.2σ). The differenced value 3.580 ± 0.024 is 0.9σ under.
- **Approach from below** matches what was seen in two directions.
- **Extrapolations in x = β^{−1/3}** (results/extrap.md, measured only) give e = 3.01 ± 0.03 to 3.05 ± 0.02 for E/T2 and 3.52 ± 0.07 to 3.65 ± 0.03 for A1, depending on the fit form. All are within 2.3σ of the predictions. The fit form is not determined by 3–4 points, so the data do not pin the constant better than about ±1.5%.
- **E–T2 splitting:** in units of β^{−1/3} it falls by roughly half per factor 4 in β. It is consistent with zero at β=4096 (−0.003 ± 0.018), as the restoration of the J=2 five-fold degeneracy requires.

- **β=16384 (extra):** E 2.988 ± 0.023, T2 2.984 ± 0.023, A1 3.568 ± 0.048. These agree with β=4096 and with the limits, but with larger errors. They do not sharpen the test.

What I cannot claim:
- Limits are not proved by finite data. This is a consistency check with ~1–2% resolution at β=4096.
- Only statistical errors are given. The plateau systematics are visible: pre-registered and differenced values differ by up to 1.5σ.

## 2. Failed predicates, and the method defect (all kept)

Pre-registered analysis (results/analysis_prereg.md): met 55, failed 16, measured only: splittings and τ values.
- PLAT failed:
  - β=1: E, T2, A1.
  - β=2: E, T2, A1.
  - β=4 at T=24: T2, A1.
  - β=4 at T=48: E, T2, A1.
  - β=16: A1.
- TLEN failed at β=1, 2, 4 (T=24). With m garbage, "T·m" is meaningless. These T were chosen for the exact controls, not for TLEN.
- CTRL β=4, T=24: m_E = 0.046 ± 0.021 (z = −44).
- CTRL β=4, T=48 is formally met (z = −2.89, 0.942 ± 0.009) but marginal.
- CTRL at β=1 and β=2 was "met" only vacuously, with errors 2.1 and 0.56. I count them as not real controls.

Causes:
- **(a) Own expectation, defect of my analysis design.** The pre-registered GEVP with t0 = 1 and plateau windows of ≥3 points cannot work when m ≳ 1.5: the signal is gone by t = 2–3. The post-hoc ctrl0.py (t0=0, 2-point window) fixes β=2. It fails its plateau rule at β=1 (λ(3) is noise) and at β=4 T=48 without differencing (met 3, failed 5).
- **(b) Method defect, diagnosed: center-sector floor (hypothesis H-floor).**
  - The periodic-time path integral is Tr T^T over **all** center sectors. The exact m_e is in the all-even sector only.
  - In sectors like (−,+,+), ⟨Q₁−Q₂⟩ ≠ 0. This gives a t-independent term Σ_s w_s⟨O⟩_s² with w_s ∝ e^{−ε_odd T}.
  - At β=4 the center-odd gap is small: tunnelling along the flat valley.
  - Evidence: floor/C(0) = 2.2% (child code, T=16), 1.27% (T=24), 0.27% (T=48). That is exponential in T with ε ≈ 0.065.
  - The differenced correlator removes it: 0.96904(380) at T=48 vs 0.96893 (ctrl_diff.md: met 6, failed 2; the 2 failures are β=1).
  - **This is a defect of my (and the brief's suggested) measurement method at intermediate β, not of the target.** The brief's remark that center tunnelling "does not matter for center-even operators" is not right for a periodic time circle: odd sectors feed in through diagonal matrix elements.
  - At β ≥ 64 the floor is ≤ few·1e−4 of C(0), at noise level. Raw and differenced values agree within ≈1.5σ (table above). A center-even projection (summing over Z₂³ twisted boundary conditions) would be the clean fix. **I did not implement it.**
- **(c) Own diagnostic weakness.** τ_int subtracts each chain's own mean, so it is blind to chains stuck in different regions. Cross-check: the between-chain variance of chain means over the naive variance is 3.4, 17, 3.4, 2.8 at β = 2, 4, 64, 256. That is consistent with 2τ_eff of about 1.7, 8.6, 1.7, 1.4, so there are no stuck chains there. I did not cross-check this at β ≥ 1024.

Post-hoc differenced analysis (analysis_diff.md): met 56, failed 15. The failures are the same small-β PLAT/TLEN rows, plus T2 at β=16.

None of the failures is a defect of the claim under test.

## 3. Hypotheses used and where stated

| # | hypothesis | where | status |
|---|---|---|---|
| H1 | Action as in the brief; temporal links kept in the maximal-tree gauge W(t)=1 (t<T−1), W(T−1)=P dynamical (exact, trivial FP) | mc3.py docstring | same convention as the child's independent code, which agrees at β=2 |
| H2 | ½Tr comm = 1 − 2\|u_i×u_j\|² | mc3.py PRE1; grandchild P1 | checked |
| H3 | Heat-bath proposal + Metropolis on the spatial part, and overrelaxation + Metropolis, satisfy detailed balance | mc3.py docstring | PRE2 for the sampler only. Validated by the β=2 and β=4 (differenced) controls |
| H4 | Operator channels: E from f_i, T2 from u0_iu0_j d_ij (odd under reflections i,j; even under center flips), A1 | mc3.py docstring | PRE3 |
| H5 | Chains are independent and thermalised, so jackknife over chains is valid | mc3.py | THERM met; τ ≪ N |
| H6 | Lowest GEVP level of the channel = the claimed level (E/T2 = J=2 split; A1 = 0⁺⁺) | brief, THREE_DIR_EXACT.md | identification by channel only. No check that no lower E/T2/A1 state exists other than the GEVP's choice |
| H7 | H-floor: odd-sector contamination negligible at β ≥ 64 | §2(b) | empirical (floors ≤ noise); not proved |
| H8 | Continuum values 3.012539 / 3.602838 (Rayleigh–Ritz) | THREE_DIR_EXACT.md | taken as given |

## 4. Not checked

- A center-even projected MC (twisted-boundary sum).
- The plateau systematic beyond comparing raw with differenced.
- Larger operator bases.
- Finite-T effects beyond TLEN.
- Whether the A1 lowest level could be a two-particle E⊗E state: the threshold 2m_E ≈ 6/β^{1/3} lies above it, so this is unlikely.
- β=1 properly.
- The between-chain stuck-chain check at β ≥ 1024.
- Statistical cross-check of the two raw-vs-differenced analyses as one estimator.
- No proof, no Lean.
- The full predicate set (MONO, extrapolation) was not rerun with β=16384 included. β=16384 was analysed alone, measured only.

## 5. Delegation

- **Child T100** (sonnet; admitted under T98, released, event 214; run as check `child-run1`, exit 0).
  - Question: independent implementation of the β=2 control, three directions.
  - Control: (1/2π)∫e^{cos x} = I₀(1). I graded it first: answer 1.266066, correct.
  - Result: m_e(β=2) = 1.620 ± 0.013 (Metropolis, T=16, 128 chains, τ=1), Q-sum channel 1.897 ± 0.023.
  - I read its mc3.py: the action terms match. I reran it as a recorded check (runF): byte-identical correlators.
  - My own read of its raw output (xcheck/xc.py) gives −ln(C₁/C₀) = 1.622 and −ln(C₂/C₁) = 1.619.
  - I also ran its code at β=4 (xcheck/b4.json). It shows the same floor as mine, which was decisive in §2(b).
- **Grandchild T103** (admitted by the child under T100, released per child notes).
  - Question: the commutator identity and center-evenness on 20000 random SU(2) matrices. Result: 4/4 met.
  - I reran its check.py in xcheck/gc: identical output.

## 6. Counts (met, failed, measured only)

- PRE1–3: met 33, failed 0.
- analysis_prereg: met 55, failed 16.
- ctrl0: met 3, failed 5.
- diffan main: met 56, failed 15.
- diffan ctrl: met 6, failed 2.
- β=16384 analyses (raw and differenced): met 9 + 9, failed 0.
- Measured only: E–T2 splittings, the extrapolations, τ_int, floor vs T, and xc.py's branch predicate.
- β=16384 was added after pre-registration. Its predicates use the same rules.
- **Total: met 171, failed 38, measured only 6 groups.**

## 7. Registers

- Register pcp/, checks:

| check | name | what it ran |
|---|---|---|
| K1 | child-run1 | the child session |
| K2 | runE | β=4 T=48, D=2 β=256, β=16 |
| K3 | runD | β=1024, β=4096 |
| K4 | analyse3_prereg | pre-registered analysis |
| K5 | diffan_main | differenced analysis |
| K6 | ctrl0 | control analysis, t0=0 |
| K7 | diffan_ctrl | differenced control analysis |
| K8 | extrap | extrapolations |
| K9 | runF | child rerun; reruns of β=1, 2, 4 |
| K10 | analyse_b16384 | β=16384 analysis |
| K11 | diffan_b16384 | β=16384 differenced analysis |
| K12 | runG | β=16384; reruns of β=64, 256 |

- **Provenance gap.** The first runs runA/runB, which produced results/d3_b1, b2, b4, b64, b256, have **no register entry**. My `pkill -f runA.sh` also killed their check wrappers.
  - They were rerun under K9 and K12 into rerun/ with the same seeds.
  - The .npz files are **byte-identical** (cmp). Only the timings in the .json files differ.
  - The killed runs also left empty files results/d3_b1024.* and results/d2_b256.*. They are kept, as files are never overwritten, and are unused.
- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- Task graph:
  - child T100 admitted under T98 (child_admit.log) and released (child_release.log, event 214);
  - grandchild T103 admitted under T100 and released by the child.

## 8. Rerun commands

Run from /home/user/z4-workers/i1-mc3. Result files are opened with mode "x", so move results/, rerun/ and xcheck/*.json away first. Each mc3 run takes 0.5–9 min on 1 core.

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
# single run: python3 mc3.py D BETA T NCH NTHERM NMEAS SEED OUTPREFIX
python3 mc3.py 3 1 20 32 500 8000 11 results/d3_b1
python3 mc3.py 3 2 20 32 500 8000 12 results/d3_b2
python3 mc3.py 3 4 24 32 500 7000 13 results/d3_b4
python3 mc3.py 3 64 34 32 1000 6000 21 results/d3_b64
python3 mc3.py 3 256 54 32 1000 6000 22 results/d3_b256
$P check --ws pcp --name runD_b1024_b4096 --expect-exit 0 --timeout 1500 -- ./runD.sh      # b1024_r2 (seed 23), b4096_r2 (seed 24)
$P check --ws pcp --name runE_b4T48_d2_b16 --expect-exit 0 --timeout 1500 -- ./runE.sh     # b4_T48 (15), d2_b256_r2 (14), b16 (31)
$P check --ws pcp --name runF_childrerun_ctrlrerun --expect-exit 0 --timeout 1500 -- ./runF.sh
$P check --ws pcp --name runG_b16384_rerun64_256 --expect-exit 0 --timeout 1500 -- ./runG.sh   # b16384 (seed 32, T=212, 3000 meas)
RUNS="results/d3_b1 results/d3_b2 results/d3_b4 results/d3_b4_T48 results/d3_b16 results/d3_b64 results/d3_b256 results/d3_b1024_r2 results/d3_b4096_r2 results/d2_b256_r2"
$P check --ws pcp --name analyse3_prereg --expect-exit 0 -- python3 analyse3.py results/analysis_prereg.md results/analysis_prereg.json $RUNS
$P check --ws pcp --name diffan_main --expect-exit 0 -- python3 diffan.py main results/analysis_diff.md results/analysis_diff.json $RUNS
$P check --ws pcp --name ctrl0 --expect-exit 0 -- python3 ctrl0.py results/ctrl0.md results/d3_b1 results/d3_b2 results/d3_b4 results/d3_b4_T48
$P check --ws pcp --name diffan_ctrl --expect-exit 0 -- python3 diffan.py ctrl results/ctrl_diff.md results/d3_b1 results/d3_b2 results/d3_b4 results/d3_b4_T48
$P check --ws pcp --name extrap --expect-exit 0 -- python3 extrap.py results/extrap.md results/analysis_prereg.json results/analysis_diff.json
$P check --ws pcp --name analyse_b16384 --expect-exit 0 -- python3 analyse3.py results/analysis_b16384.md results/analysis_b16384.json results/d3_b16384
$P check --ws pcp --name diffan_b16384 --expect-exit 0 -- python3 diffan.py main results/analysis_b16384_diff.md results/analysis_b16384_diff.json results/d3_b16384
# child-code cross-check at beta=4 (floor), not recorded:
(cd xcheck && python3 child_mc3.py 4 64 400 3000 b4.json && python3 xc.py b4.json)
# child: $P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp ; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

- Programs: mc3.py, analyse3.py, ctrl0.py (post hoc), diffan.py (post hoc), extrap.py, xcheck/xc.py.
- Notes: notes.md.
- Scratch looks, not result files: scratch/.

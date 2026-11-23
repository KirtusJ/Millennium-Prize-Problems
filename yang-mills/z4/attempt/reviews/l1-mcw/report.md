# l1-mcw report (task T123): does the plaquette see the soft gap on a fixed 2³×T box?

- control.txt = 0.272341 (−ln tanh 1).
- Lean: /home/user/z4-lean/READY exists. I did not use Lean and make no Lean claim.
- Primary data:
  - β = 64: 48 chains × 1500 measurements, T = 56.
  - β = 256: 48 chains × 1100 measurements, T = 88.
  - β = 1024: 32 chains × 2500 measurements, T = 136.
  - All runs use heat bath + 2 overrelaxation sweeps, no collective moves.
- Errors are jackknife over the independent chains.
- R(t) = C(t)/C(0) throughout.
- Operators, all per time slice:
  - PS = β Σ₈(1 − P_ij), one plane (correlator averaged over the three planes).
  - PA = A1, the sum over the three planes.
  - PE = the E pair.
- The Gaussian reference is exact. I computed it (gauss.py, dense projector). The child computed it independently (Fourier blocks). The two agree to 3e-11.

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| c1: plaquette vs leading weak coupling, r = β(1−⟨P⟩)/(3/4) → 1 − δ/V | STANDS | r = 0.995708(77), 0.995951(96), 0.997112(50) at β = 64, 256, 1024. (1−r)V = 1.9, 2.9, 3.1, which reproduces MC_BOX (1.9, 2.6, 2.8). |
| c2: exact Gaussian correlator (3/2) Σ Π_pq², from my code and the child's | STANDS (computation) | C(0) = 7/2, 51/4, 25/8 (PS, PA, PE). R(1) = 1.772599e-2, 1.610171e-2, 1.883051e-2. R(2) = 4.19809e-4, 3.59540e-4, 4.60791e-4. Independent codes agree to 3e-11. |
| Hard threshold 3.52549435 (Gaussian side) | STANDS | Exact: E₁ = 4 asinh 1 = 3.5254943481, the same in all channels. The next levels are 4.5849 and 5.2678 for box operators (child; 3-term fit residual 6e-16). |
| Auditor's weight "0.046875 of the variance" | DEFECT (of the statement as worded) | 0.046875 = 3/64 is the **absolute** first-atom weight of a **single** plaquette (wfit: 0.0468750014). As a fraction of that plaquette's variance 0.307908 it is **0.1522**. For the box operators the fractions are 3/7, 6/17, 12/25 (PS, PA, PE). |
| Brief's "3 colours × …" Gaussian variance of a single plaquette, naively 3/8 | DEFECT of the naive value (corrected) | On 2³ the projector diagonal is Π_pp = 0.4530696 for spatial plaquettes, not 1/2. Variance = (3/2)Π_pp² = 0.307908; mean = 0.679604 (temporal 0.8204). |
| O_P keeps a positive O(1) variance | STANDS | C(0) at β=1024: PS 3.4981(12) vs 3.5; PA 12.7635(67) vs 12.75; PE 3.1198(9) vs 3.125. Single-plaquette variance 0.31203(6) vs 0.307908 (+1.34 %, P6 met). |
| (iii) Gaussian correlator 3k²/2 at β = 1024, t = 1, 2 (P2) | STANDS at t=1; DEFECT at t=2 for PS (+3.1σ) | t=1: PS +1.8σ, PA +2.0σ, PE +0.8σ. t=2: PS 9.55(1.7)e-4 vs 4.20e-4 (FAILED); PA +2.2σ, PE +2.0σ. All six t=2 values lie **above** Gaussian, consistent with a soft tail of size A e^{−2m} ≈ 4–7e-4. |
| m_eff(0→1) vs Gaussian at β=1024 (P3) | STANDS | PS 4.012(11) vs 4.0327; PA 4.091(19) vs 4.1288; PE 3.962(12) vs 3.9723. It approaches from below: PS 3.919, 3.966, 4.012 at β = 64, 256, 1024. |
| (ii) MC decay "like exp(−3.5 t) at small t" | DEFECT at β ≤ 1024 (finite β); β→∞ not tested | m_eff(1→2) at β=1024: PS 2.94(18), PA 2.71(31), PE 3.11(24), against Gaussian 3.74, 3.80, 3.71. From t = 2 on the soft tail already dominates the hard part. The 3.525 atom is not isolated in any MC channel. |
| (i) soft weight A_soft → 0 | NOT CHECKED (not resolved) | A_soft (m fixed to the winding mass of the same run, t ≥ 4), for β = 64, 256, 1024:<br>• PE: 2.45(1.0)e-3, 1.6(5.8)e-4 [bound 1.3e-3], 4.0(1.7)e-4<br>• PA: 3.8(2.4)e-3 [bound 8.6e-3], 8.5(7.9)e-4 [bound 2.4e-3], 8.7(3.0)e-4<br>Nonzero at β=1024 at 2.4–3.9σ, and the two 16-chain halves of β=1024 disagree by ≈2σ. |
| Expected power A_soft ∝ β^{−2/3} (derivation checked, §2) | NOT CHECKED (consistent, not resolved; measured only) | Best p, with 1σ range: PE 0.65 [0.32, 0.97]; PA 0.39 [−0.17, 0.73]; PS 0.51–0.58. p = 0 is disfavoured only by Δχ² = 2.4–2.8 (PE, PS) and 0.6 (PA). A β^{2/3} is ≈ 0.04 (PE) and ≈ 0.06–0.09 (PA) at every β within errors. |
| Winding soft masses in the same runs (measured only) | STANDS (agrees with MC_BOX) | E: m β^{1/3} = 1.5057(115) at β=256 and 1.525(14) at β=1024, vs 1.5063. A1: 1.770(29) and 1.840(20), vs 1.8014. At β=64 the E plateau starts late (t_a = 6, TLEN failed): 1.43(3). |

**Paragraph.**
- **(i) Vanishing soft weight: not resolved.**
  - The plaquette correlators do carry a small slow tail. With m fixed to the winding gap, its amplitude relative to C(0) is ~1e-3 or smaller: about 2–4e-3 at β=64, consistent with zero (|A| ≲ 1–2e-3) at β=256, and 4–9e-4 at β=1024 (2.4–3.9σ).
  - The amplitudes fall with β and fit β^{−2/3} (preferred p ≈ 0.4–0.65). A β-independent amplitude is disfavoured only at ≈1.5σ, and not at all in A1.
  - So the data lean toward, but do not establish, A_soft → 0.
- **(ii) Hard threshold 3.525: supported on the Gaussian side, not seen directly in the Monte Carlo.**
  - The exact Gaussian model has E₁ = 3.5254943 with weight 3/7 (PS), 6/17 (PA), 12/25 (PE).
  - The MC agrees with the Gaussian at t = 0→1 (m_eff ≈ 4.0, as expected from the mixture of levels).
  - At β ≤ 1024 the soft tail already dominates R(t) from t = 2 on, so m_eff(1→2) ≈ 2.9 rather than 3.7.
  - The "exp(−3.5 t) at small t" picture therefore holds only for the first step at these β.
  - The auditor's 0.046875 is the absolute weight for a single plaquette, not a fraction of the variance.
- **(iii) Gaussian correlator 3k²/2: quantitatively supported at β=1024 for t = 1** (all three channels within 2σ, and C(0) within 0.2 %). At t = 2 there is a systematic excess in all channels (PS 3.1σ), the size expected from the soft tail. As β grows, the deviations at t = 1 shrink: PS excess 2.1e-3, 1.2e-3, 3.7e-4 at β = 64, 256, 1024.

## 2. Hypotheses used and where they are stated

| # | hypothesis | where |
|---|---|---|
| H1 | Wilson action and sampler of mcbox.py are unchanged; PRE1–4 pass in every run | mcp.py docstring (it is mcbox.py plus channels) |
| H2 | Chains are independent and thermalised; jackknife over chains | anapl.py docstring; THERM met in all 14 runs |
| H3 | Gaussian reference = quadratic action. Constant fields (ker B) do not enter θ at linear order and are dropped. 3 colours by Wick | gauss.py and anapl.py docstrings; the child's t124.py |
| H4 | Soft levels = the lowest differenced-GEVP winding masses of the same run (analyse.py, unchanged): A1 for PA, E for PE | anapl.py P4 |
| H5 | The soft tail is a single cosh for t ≥ 4. Other soft levels are lumped into it; the Gaussian hard part at t ≥ 4 is ≤ 4e-8 | anapl.py P4 |
| H6 | Gaussian ratios at T=32 serve for T = 56, 88, 136. T-dependence < 1e-16 for t ≤ 6 (child, T = 32…512) | anapl.py; child results.md |
| H7 | Derivation of A_soft ∝ β^{−2/3}. Soft fields a ~ β^{−1/3}. The slow part of the box plaquette energy is β·|[a,a]|² ~ β^{−1/3}, so its variance is ~ β^{−2/3}. The hard variance is O(1). The cross term β F_h·[a,a] averages to zero over the hard modes. The a-dependence of the hard zero-point split is ~a² ~ β^{−2/3} in amplitude, so subleading in variance. I agree with the brief's reasoning. Correction to the brief: A is relative to C(0), and C(0) is 3.5 / 12.75 / 3.125, not 3/8 | anapl.py X3 |

## 3. Failed predicates (all kept)

Counts:
- **Met 107**: P1 ×3; P2 5 of 6 at β=1024; P3 ×3; P6 ×1; G1–G3 ×9; W1; S1; PRE1–4 ×56; THERM ×14; TAU 11 of 14; NCH (merged analyses) ×3.
- **Failed 12**.
- **Measured only**: P2/P3/P6 at β = 64 and 256; all P4 fits; P5; pfit; the winding masses; the sensitivity fits with predicted m.

Failed predicates:
1. **P2, PS at t=2, β=1024 (32 chains)**: +3.14σ. **Own expectation.** The 2 % relative allowance ignored the additive soft tail (≈ A e^{−2m} ≈ 4e-4, about the size of R_G(2) itself). Not a defect of the asymptotic claim, but it shows that at β=1024 the Gaussian form fails at t=2. The 16-chain subset met it (+1.4σ).
2. **G4 ×7** (T = 8: t=3; T = 16, 32: t = 3, 4, 5): C(t+1)/C(t) = e^{−3.525} to 1e-3. **Own expectation.** The approach to E₁ is slow (m_eff 3.6055, 3.5534, 3.5351 at t = 2, 3, 4), because w₂/w₁ ≈ 1 and the gap is 1.06.
3. **TAU ×3** (b1024b, e, f: τ_int of the T2 winding is 25–33 > 25). **Own expectation**: without collective moves T2 decorrelates more slowly. T2 is not used in any fit.
4. **PRE2 in the timing run scratch/timing1**: own defect. The pretests ran with β-scaled operators (absolute deviation 2.4e-7 on values of ~7e7). Fixed by running the pretests with BETA_OP = 1.
- Process errors (own), in the register: checks K1 and K2 (gauss.py) exited 1. Causes: an index bug, then numpy bool in JSON. Their empty result files are kept.
- Measured only, but beyond tolerance at finite β:
  - P2 at β=64 (PS t=1,2; PA t=1; PE t=1) and at β=256 (PS t=1).
  - P6 at β=64: +3.75 %. Variance excess +3.75, +2.18, +1.34 % behaves like β^{−0.37}, i.e. roughly β^{−1/3}, as does the mean excess.

## 4. Not checked

- β → ∞ itself, and β = 4096. The trend from three β values with A at 1–4σ is not a limit.
- Correlated (covariance-matrix) fits. I used diagonal weights plus a jackknife of the whole fit. The jackknife errors from 32–48 chains carry ~15–20 % uncertainty of their own, and the β=1024 halves differ by ≈2σ in PA.
- A multi-level soft fit, and a GEVP mixing plaquette with winding operators. Either would identify which soft level the plaquette couples to.
- The single-plaquette (not box-summed) MC correlator. Only its variance and mean were measured.
- The temporal plaquette.
- T2 plaquette combinations. None exist from single-orientation spatial plaquette sums on 2³; not attempted.
- Lean: not used.

## 5. Delegation

- **Child T124** (label l1-mcw-child, parent T123).
  - Admitted at graph event 248 and released at event 255. It ran as check `child-run1`, exit 0, 210 s.
  - Question: control (c2), i.e. the exact Gaussian correlator of PS/A1/E on 2³×T for T = 32, 48, 64, ∞; the single-plaquette mean and variance; the first spectral level and its weight.
  - Control: ∫₀^∞ x³/(eˣ−1) dx. It answered 6.493939. I graded this first: **correct** (π⁴/15 = 6.4939394).
  - Returned: the numbers in §1 row c2, the spectrum E_m = 4 asinh √m, and the weights 3/7, 6/17, 12/25. It noted 0.046875 = 1.5/32 as an unverified guess.
  - I reran its t124.py in xcheck/child (check `child-t124-rerun`). The output is byte-identical to its data_v1.json.
  - Its numbers agree with my independent gauss.py to 3e-11 relative.
  - I resolved the 0.046875 question myself with wfit.py: it is the single-plaquette absolute weight, 3/64.
- **Grandchild T127** (l1-mcw-grandchild, parent T124; the child admitted it at graph event 253 and released it at event 254).
  - Question: an independent dense-SVD recomputation at T = 10 of P_pp, the single-plaquette variance, C_S(t ≤ 4) and C_A1(0).
  - Its control was Var(φ²/2) = 0.5: passed.
  - It returned P_pp = 0.453069632, var 0.3079081372, C(1)/C(0) = 0.01772601374. These agree with the finite-T = 10 values.
  - I reran its main.py in xcheck/gc (check `gc-main-rerun`). The answer.txt is identical.

## 6. Rerun commands

Run from /home/user/z4-workers/l1-mcw. Result files open with mode "x", so move the old outputs first.

```
export OMP_NUM_THREADS=1
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name gauss-8-16-32-r3 --expect-exit 0 -- python3 gauss.py results/gauss_8_16_32_r3.json 8 16 32
$P check --ws pcp --name gauss2-T32 --expect-exit 0 -- python3 gauss2.py results/gauss2_T32.json 32
$P check --ws pcp --name wfit-single --expect-exit 0 -- python3 wfit.py results/gauss2_T32.json results/wfit_single.json
# production (mcp.py L BETA T NCH NTHERM NMEAS NOR COLL SEED OUTPREFIX); runs.sh and runs2.sh contain exactly these
for s in a:141 b:142 c:143 d:144 e:145 f:146 g:147 h:148; do $P check --ws pcp --name prod-b1024${s%%:*} --expect-exit 0 -- python3 mcp.py 2 1024 136 4 300 2500 2 0 ${s##*:} results/b1024${s%%:*}; done
$P check --ws pcp --name prod-b256  --expect-exit 0 -- python3 mcp.py 2 256 88 16 200 1100 2 0 131 results/b256
$P check --ws pcp --name prod-b256b --expect-exit 0 -- python3 mcp.py 2 256 88 16 200 1100 2 0 132 results/b256b
$P check --ws pcp --name prod-b256c --expect-exit 0 -- python3 mcp.py 2 256 88 16 200 1100 2 0 133 results/b256c
$P check --ws pcp --name prod-b64  --expect-exit 0 -- python3 mcp.py 2 64 56 16 200 1500 2 0 121 results/b64
$P check --ws pcp --name prod-b64b --expect-exit 0 -- python3 mcp.py 2 64 56 16 200 1500 2 0 122 results/b64b
$P check --ws pcp --name prod-b64c --expect-exit 0 -- python3 mcp.py 2 64 56 16 200 1500 2 0 123 results/b64c
# analysis
$P check --ws pcp --name anapl-b1024 --expect-exit 0 -- python3 anapl.py results/anapl_b1024.md results/gauss_8_16_32_r3.json results/b1024a+results/b1024b+results/b1024c+results/b1024d
$P check --ws pcp --name anapl-b64-b256 --expect-exit 0 -- python3 anapl.py results/anapl_b64_b256.md results/gauss_8_16_32_r3.json results/b64 results/b256
$P check --ws pcp --name anapl-b1024-32ch --expect-exit 0 -- python3 anapl.py results/anapl_b1024_32ch.md results/gauss_8_16_32_r3.json results/b1024a+results/b1024b+results/b1024c+results/b1024d+results/b1024e+results/b1024f+results/b1024g+results/b1024h
$P check --ws pcp --name anapl-b64-b256-48ch --expect-exit 0 -- python3 anapl.py results/anapl_b64_b256_48ch.md results/gauss_8_16_32_r3.json results/b64+results/b64b+results/b64c results/b256+results/b256b+results/b256c
$P check --ws pcp --name pfit --expect-exit 0 -- python3 pfit.py results/pfit.json results/anapl_b64_b256_48ch.md results/anapl_b1024_32ch.md
# child / grandchild
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
(cd xcheck/child && $P check --ws ../../pcp --name child-t124-rerun --expect-exit 0 -- python3 t124.py rerun)
(cd xcheck/gc && $P check --ws ../../pcp --name gc-main-rerun --expect-exit 0 -- python3 main.py)
# register
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Files changed:
- **mcp.py** is a copy of mcbox.py. It adds the channels PS/PA/PE (β·Σ₈(1−P) per plane per slice) and the moments sp1/sp2 of the single spatial plaquette. It also runs the pretests with BETA_OP = 1. Nothing else changed.
- mcbox.py and analyse.py are unchanged. anapl.py imports analyse.py for the winding masses.

Last lines of the verifications:
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Verdict counts (12 rows of §1; the split row (iii) is counted once under STANDS and once under DEFECT, giving 13 entries): **STANDS 7, DEFECT 4, NOT CHECKED 2.**
- STANDS: c1, c2, the Gaussian threshold, positive variance, P3, winding masses, and (iii) at t=1 (counted as STANDS, with its t=2 defect counted under DEFECT).
- DEFECT: the auditor-weight wording, the naive 3/8, (iii) at t=2 for PS, and (ii) the MC decay at β ≤ 1024.
- NOT CHECKED: (i) and the β^{−2/3} power.

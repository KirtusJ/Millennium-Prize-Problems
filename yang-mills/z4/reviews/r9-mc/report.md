# r9-mc report: SU(2) Wilson lattice, square-loop covariance, measured against the free prediction

Worker for Director Z4, 23 November 2026. Role: builder with a simulation. **Every lattice number here is a Monte Carlo measurement (measured only)**: one lattice size for the main runs (8^4), one or two seeds per β, no continuum limit. Director, worker and sub-agent are the same model family, so this is not independent review.

Control: `control.txt` = 0.272341 (−ln tanh 1).

## 1. Verdict table

| # | Item | Verdict | Evidence (one line) |
|---|------|---------|---------------------|
| 1 | My SU(2) heat-bath simulator (`mc.py`) reproduces the known plaquette values | STANDS | 8^4: β=2.2 0.56935(16), 2.3 0.60226(11), 2.5 0.65251(8), against 0.5688/0.6024/0.6522, all within 3σ+0.001. β=0.5: 0.12375(12) against I2/I1 = 0.123718. β=8: 0.90356(1) against 1−3/(4β) = 0.90625 within the second-order allowance. |
| 2 | Brief's strong-coupling check "β/4 − (β/4)³/6" | DEFECT (in the brief) | The series of I2(β)/I1(β) is β/4 − β³/96. At β=0.5 the brief's form, 0.124674, is 7.4σ from the measurement. β/4 − β³/96 = 0.123698 agrees (0.4σ). |
| 3 | README_round7 free kernels K (unit square and 2×2, n=1..3) | STANDS | `free.py`, L=48 torus with the zero mode removed: all six agree within 1.7e-6. K1(0) = (1−L⁻⁴)/2 holds exactly on 8^4. |
| 4 | Free leading order C(n) = (3/2)K(n)²/β² holds at weak coupling (P2: β=8, R=1, n=1) | STANDS (at leading order) | C/C_free = 1.121 ± 0.007, with the 8^4 torus kernel. Within the 30% window. The 12% excess is resolved at 17σ; its size fits an O(g²)=O(0.5) correction, but that was not computed. |
| 5 | At β=2.3 the square-loop covariance is far from free (P3, the measurement) | STANDS (measured only) | Unit square, n=1: C/C_free 2.244(8), ρ/ρ_free 6.19(2), corr/corr_free 1.716(6). 2×2, n=1: 0.284(1), 8.79(5), 0.664(3). Details in §1a. |
| 6 | Cross-check of my code against the sub-agent's simple serial heat bath (4^4) | STANDS | Rerun by me at the same volume. β=2.3: child code 0.61162(96), mine 0.60845(101), 2.3σ apart. β=8: 0.90384(13) and 0.90385(9). The sub-agent itself returned no numbers. |
| 7 | A non-free correction at fixed physical size, with its logarithm (the round's open quantity) | NOT CHECKED | Everything here is at fixed lattice size R=1,2. No sequence of matched β (§3). |
| 8 | Continuum or infinite-volume statements about any of the ratios | NOT CHECKED | One volume. The free kernel already moves by 3% at n=3 between L=8 and L=∞. |

### 1a. The measurement (8^4, B=50 bins, jackknife; `results/analysis_final.txt`)

The free references are computed as follows:
- C_free(n) = (3/2)K_L8(n)²/β².
- ρ_free = C_free at leading order, because ⟨W⟩ = 1 + O(g²).
- corr_free = K(n)²/K(0)², which does not depend on β.
- Free mean = 1 − (3/2)K(0)/β, with K(0) = 1/2 for the unit square and 1.3693 for the 2×2 square (L=∞; 1.3671 on 8^4). I computed G0 for the 2×2 square here; the brief did not give it.

| β | R | ⟨W⟩ (free LO) | Var W / free | C(1)/C_free | C(2)/C_free | ρ(1)/ρ_free | corr(1)/corr_free |
|---|---|---|---|---|---|---|---|
| 8.0 | 1 | 0.90356 (0.9063) | 1.030 | **1.121(7)** | 1.19(28) | 1.373(9) | 1.089(7) |
| 8.0 | 2 | 0.75288 (0.7437) | 0.802 | 0.784(3) | 0.82(6) | 1.383(5) | 0.978(4) |
| 2.5 | 1 | 0.65251 (0.7001) | 1.200 | 1.795(11) | 3.2(5) | 4.22(3) | 1.496(9) |
| 2.5 | 2 | 0.25987 (0.1797) | 0.456 | 0.338(2) | 0.38(3) | 5.00(4) | 0.741(5) |
| **2.3** | 1 | 0.60222 (0.6740) | 1.308 | **2.244(8)** | 4.7(3) | **6.19(2)** | **1.716(6)** |
| **2.3** | 2 | 0.17987 (0.1084) | 0.428 | **0.284(1)** | 0.39(3) | **8.79(5)** | **0.664(3)** |
| 2.2 | 1 | 0.56936 (0.6592) | 1.379 | 2.455(14) | 5.9(6) | 7.58(4) | 1.781(10) |
| 2.2 | 2 | 0.13647 (0.0679) | 0.408 | 0.212(2) | 0.22(5) | 11.4(1) | 0.520(6) |

n=3 is not resolved at any β (relative errors ≥ 50%). At β=0.5 every free leading-order quantity is meaningless (the free mean comes out negative); those rows are in the result file and are not a comparison.

How to read it:
- At β=8 the unit-square covariance sits 12% above free.
- At β=2.3 the raw covariance of the unit square is 2.2 times free, and that of the 2×2 square is 0.28 times free.
- The mean-normalized ρ is 6 to 9 times free. Most of that comes from the small mean (1/⟨W⟩² = 2.8 for R=1 and 31 for R=2).
- The correlation coefficient C/Var W moves in opposite directions for the two sizes: up 1.7× for R=1, down to 0.66× for R=2.
- The trend from β=8 to 2.2 is monotone for every quantity.

## 2. Hypotheses used, and where each is stated

- **Wilson action** exp(β Σ_p ½Tr U_p), SU(2), periodic L^4, cold start. Stated in the `mc.py` docstring.
- **Heat bath**: Creutz for a=βk<2, Kennedy–Pendleton for a≥2, each sweep followed by 2 overrelaxation sweeps; the 4^4 cross-check runs use none. Checkerboard by direction and parity. Stated in the `mc.py` docstring.
- **Thermalization**: 200 discarded sweeps on 8^4 (100 on 4^4). By eye from `runs/*/therm_*.npy` the plaquette settles within ~20 sweeps; tested by P1e (first and second halves agree). Stated in `notes.md` step 3 and the `analyze.py` docstring.
- **Errors**: bins of B=50 configurations (fixed before the run; B=N/20 if that gives fewer than 20 bins, used only at β=0.5 with B=30), then jackknife over bins. The binning tables in the result file show the error flat to within ~20% from B=25 to 200. Correlations between the two seeds' segments are ignored because they are independent chains. Stated in the `analyze.py` docstring.
- **Free kernel**: Feynman gauge on the torus with the zero mode removed; gauge invariant for a closed loop. Stated in the `free.py` docstring.
- **Free prediction for SU(2)**: ½Tr W = cos(g|Φ|/2) with three colours, giving C = (3/2)K²/β², from README_round7. The free mean is 1 − (3/8)g²G0. These are taken over, not rederived beyond checking the unit-plaquette variance 1/2.
- **Literature plaquettes** 0.5688/0.6024/0.6522 come from the brief and match my memory. I am sure of them only to about ±0.001, hence the additive 0.001 tolerance in P1a. The second-order weak-coupling coefficient (~0.15 for SU(2) by my memory, uncertain) is bounded by 0.4 in P1c. I measured β²(1−3/(4β)−P) = 0.172(1) at β=8 on 8^4, which includes finite-volume effects.
- **Strong coupling**: the leading value is I2/I1. The O(u⁵) correction is bounded by 2e-4; that bound is my estimate, not derived.

## 3. Failed predicates (all kept)

- **K5–K9 (pcp checks of the long runs b2p5, b2p3s11, b2p3s12, b8s21, b8s22): exit 1, expected 0.** This was my own expectation. I stopped the runs with taskkill at about 02:17 for the time budget, because running all 4000 configurations would have taken about 50 min under 7-way load. Every block written before the stop is intact and is used: 2600–2700 configurations per run. This is not a defect of the target or of the program.
- **No other pass/fail predicate failed.** The brief's strong-coupling formula (item 2) failed against the measurement. That is a defect of the brief; it was a measured-only comparison, not one of my predicates.
- **The sub-agent's own production runs** (its predicates P3 and P4) never ran. The runs were killed before they wrote output, and the program writes only at the end. I counted this against the sub-agent's run, not against the target.

Counts as (met, failed, measured only): **23, 5, 26**.
- Met (23):
  - Runtime checks M1–M3 in `mc.py`: 3.
  - Free-kernel checks F1–F3: 3.
  - Literature plaquettes P1a: 3.
  - Strong coupling P1b: 1.
  - Weak coupling P1c: 1.
  - Seed agreement P1d: 2.
  - Thermalization halves P1e: 7.
  - P2: 1.
  - Same-volume cross-check at the two β: 2.
- Failed (5): the exit-code expectations K5–K9.
- Measured only (26): the P3 ratio sets at β=2.2, 2.3 and 2.5 (6 each), β=8 (5 besides P2), the brief's formula, the β=8 second-order coefficient, and the 4^4→8^4 shift.

## 4. What I did not check, and what the numbers cannot support

**Limits of these runs**
- One lattice size for the main runs (8^4). One seed at β=0.5, 2.2 and 2.5; two seeds at β=2.3 and 8.
- 8^4 at β=2.3 is a small box, about 3 fm in units of the string tension by common estimates I did not verify. 4^4 shifts the plaquette by +0.006, so finite volume is visible even in the plaquette.
- No continuum extrapolation. No fixed-physical-size sequence. R is fixed in lattice units, so the β=2.3 ratios mix cutoff and physical effects and say nothing about a running coupling or a scale.

**Not computed**
- The O(g²) correction to C(1) at β=8. I cannot say whether the 12% is the expected one-loop correction or partly finite-volume (toron/zero-mode) physics of the 8^4 torus at weak coupling.
- Autocorrelation times were not measured beyond the binning plateau.

**The smallest honest fixed-physical-size experiment** needs a pair of β with a scale ratio of 2 that is known independently, for example from a Sommer-scale or string-tension table that I did not verify. Then compare
- R=2 loops, n=1,2 at the coarser β on 16^4, against
- R=4 loops, n=2,4 at the finer β on 32^4,

so that the physical box stays the same (≥ ~2.5 fm).

**Cost of that experiment**
- 32^4 is 256× the volume of 8^4. My numpy code runs about 0.15 s per sweep on 8^4 single-threaded, so roughly 40 s per sweep on 32^4.
- About 5000 sweeps comes to roughly 2–3 CPU-days in numpy.
- The 4×4 loop has ⟨W⟩ of order 10⁻² to 10⁻³, so ρ needs smearing or multilevel to beat the noise.
- Realistically this is a compiled code and about a CPU-week, before any second β pair for the logarithm.

## 5. Delegated question and outcome

**Question (rule 7).** Write an independent, simple and slow serial Creutz heat bath on 4^4, measuring only the plaquette at β=2.3 and 8 with fixed seeds. Control first: −ln tanh 1. Work in `child/` with its own register `child/pcp`.

**What came back**
- The control was correct (0.272341), and the program `child/su2hb.py` was written.
- **No plaquette values.** The sub-agent launched four long runs that write only at the end; a 10-min runner limit killed them, and it went over its budget (~23 min). It said so plainly. Its register verifies (3 events).

**What I did with it**
- I reread `su2hb.py`. The conventions are correct and its quaternion code is the same family as mine, so this is not convention-independent.
- I reran it myself, 4^4, 100+600 sweeps (pcp K11, K12): β=2.3 gave 0.61162(96) and β=8 gave 0.90384(13).
- I ran my `mc.py` at the same volume with pure heat bath (K13, K14): 0.60845(101) and 0.90385(9).
- Agreement is 2.3σ and 0.1σ, so item 6 STANDS. The β=2.3 tension is worth a longer run; bin-20 errors on 4^4 may be underestimated.

## 6. Exact commands to rerun

Run in C:/Users/donke/z4-workers/r9-mc, Git Bash, with `export PYTHONUTF8=1 OMP_NUM_THREADS=1`. Each program refuses to overwrite its outputs, so first move or remove `runs/`, `runs4/`, `childrerun/` and `results/`, or pass new tags.

```
P=C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py
python $P check --ws pcp --name free_kernel --expect-exit 0 -- python free.py
python $P check --ws pcp --name mc_b0p5    --expect-exit 0 -- python mc.py 0.5 8 100 600  100 5  runs/b0p5
python $P check --ws pcp --name mc_b2p2    --expect-exit 0 -- python mc.py 2.2 8 200 1500 100 6  runs/b2p2
python $P check --ws pcp --name mc_b2p5    --expect-exit 0 -- python mc.py 2.5 8 200 4000 100 7  runs/b2p5
python $P check --ws pcp --name mc_b2p3s11 --expect-exit 0 -- python mc.py 2.3 8 200 4000 100 11 runs/b2p3s11
python $P check --ws pcp --name mc_b2p3s12 --expect-exit 0 -- python mc.py 2.3 8 200 4000 100 12 runs/b2p3s12
python $P check --ws pcp --name mc_b8s21   --expect-exit 0 -- python mc.py 8.0 8 200 4000 100 21 runs/b8s21
python $P check --ws pcp --name mc_b8s22   --expect-exit 0 -- python mc.py 8.0 8 200 4000 100 22 runs/b8s22
#   (the original long runs were stopped after 26-27 blocks; to reproduce exactly, delete blk_0026+ / blk_0027+ to match)
python $P check --ws pcp --name analysis_final --expect-exit 0 -- python analyze.py final
python $P check --ws pcp --name child_rerun_b2p3 --expect-exit 0 -- python child/su2hb.py 2.3 cold 100 600 31 childrerun/b2p3.txt
python $P check --ws pcp --name child_rerun_b8   --expect-exit 0 -- python child/su2hb.py 8.0 cold 100 600 32 childrerun/b8.txt
python $P check --ws pcp --name mc_L4_b2p3 --expect-exit 0 -- python mc.py 2.3 4 100 1000 100 41 runs4/b2p3L4 0
python $P check --ws pcp --name mc_L4_b8   --expect-exit 0 -- python mc.py 8.0 4 100 1000 100 42 runs4/b8L4 0
python $P verify --ws pcp
```

Block counts used, from runs/: b0p5 6, b2p2 15, b2p3s11 27, b2p3s12 26, b2p5 27, b8s21 26, b8s22 26. The analysis used 2700/2600, 2700 and 2600/2600 configurations; one block of b2p3s11 and one of b2p5 were written while the kill was in progress, and all blocks present were used.

PCP verify, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`. The register has 16 events and the chain is intact. The PASS covers the record, not the findings.

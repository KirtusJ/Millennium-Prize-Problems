# z1-mix8 report (task T206): side 8, time period 16, beta = 3.399810242

Worker of Director Z4, principal Kirtus Justus. My verdicts share a model family with the director's, so my agreement does not count as independent review. All numbers come from `results/summary_final.json` (reduction `reduce.py`), the raw streams in `results/`, and `notes.md`.

Notation:
- f1 = Re(B g1) and f4 = Re(B ḡ). f4 is the "four-face mark".
- r1 = J1/Var1 and r4 = J4/Var4.
- Errors are delete-one-stream jackknife errors over all streams of a run.
- "minang" is the smallest round distance from −I, arccos(−Re U), over all 192 coarse 2×2 spatial faces of the frozen slice.

## 1. Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| Control: G4 side-8 W=−I four-face ratio 0.0441(20) | STANDS | My long δ=0 run (8 streams × 512) gives r4 = 0.0478(17), 1.4σ from 0.0441 and 1.2σ from G4's repeat 0.0506(13). reduce.py on G4's archived files reproduces 0.0441(20), r1 0.0592 and Var4 0.05877 exactly (C3a). |
| Control: G4's quoted error 0.0020 for the 4×144 design | DEFECT | My replay of the same design (same seeds, but a different floating-point trajectory) gives 0.0590(38), 3.4σ from 0.0441(20). From the spread of my 512-sample streams, the 4×144 design's real error is ≈0.0045. G4's own two side-8 values already differ by 2.7σ. |
| Control: bitwise replay of G4's archived streams | NOT CHECKED (failed) | Same seeds and binary source; the first row agrees to ~1e-6, then the trajectories diverge (floating point / libm). My expectation was wrong; no target defect is shown. |
| Run mix δ=0: W=−I, B=i | STANDS | J4 .00266(3), Var4 .0557(16), r4 .0478(17), r1 .0605(24), β·r4 .163(6); minang 0; hot and cold agree. |
| Run mix δ=0.5/β | STANDS | J4 .00279(6), Var4 .0598(17), r4 .0467(12), r1 .0621(12), β·r4 .159(4); minang 0.1471. |
| Run mix δ=1/β | STANDS | J4 .00284(4), Var4 .0632(8), r4 .0450(9), r1 .0595(13), β·r4 .153(3); minang 0.2941. |
| Run mix δ=2/β | STANDS | J4 .00286(5), Var4 .0580(12), r4 .0494(17), r1 .0623(19), β·r4 .168(6); minang 0.5883. |
| The disk's displacement trend carries over to the box | DEFECT | Box β·r4 relative to δ=0: 0.976(43), 0.940(38), 1.032(51). Disk: 1.010, 1.039, 1.152. The 1/β point is 2.6σ below, the 2/β point 2.3σ below; no increase is seen. |
| Run clear k0 (chainA cfg0) | STANDS | J4 .00065(1), Var4 .00719(31), r4 .0898(35), r1 .0719(34); minang 0.8310. |
| Run clear k1 (chainA cfg1) | STANDS | J4 .00048(1), Var4 .00441(24), r4 .1083(53), r1 .0705(19); minang 0.8283. |
| Run clear k2 (chainA cfg4): ratio | STANDS | J4 .00099(3), Var4 .01330(43), r4 .0742(37), r1 .0711(28); minang 0.9695; hot/cold ratio T1 met. |
| Run clear k2: thermalisation of the variance | NOT CHECKED (T1b failed) | Var4 hot .01419(50) vs cold .01237(27), 3.2σ. |
| Does any bath outside the selected pair relax the mode | STANDS (answer: no) | In every row of every run, the 20 colours other than xy-000/100/010/110 contribute exactly 0 to J (max abs = 0). This is structural: f depends only on the 4 free links inside the marked square. |
| Child (T207): independent implementation of the side-6 −I control | STANDS | Own Rust code: r4 0.0501(19) vs G4 0.0464(55), r1 0.0589(17) vs 0.0639(23). I reread the code and reran it; the output is byte-identical. |

**Predicate counts (met, failed, measured only): 25 met, 4 failed, 9 measured only.**
- Met (25): C2′, C3a, C5; T1, T1b and S1 for the 4 mix runs (12); T1×3, T1b×2 and S1×3 for the clear runs (8); P_gen×2.
- Failed (4): C1, C2 as written, C4, and T1b for clear k2.
- Measured only (9): the 7 run quotients, the comparison with the disk, and the colour-share readout.

## 2. Run details (side 8, time period 16, β = 3.399810242 for every run)

### Run design and spread

| run | W (quaternion) | δ | B | streams (hot/cold) | burn | meas × spacing | mean spread 1−⟨…⟩ | per-stream r4 | Var4 hot / cold |
|---|---|---|---|---|---|---|---|---|---|
| control replay | −I | 0 | i | 4 (2/2) | 288 | 144×6 | .3310(33) | .0487 .0649 .0629 .0608 | – |
| mix d0 | −1 | 0 | i | 8 (4/4) | 864 | 512×6 | .3348(26) | .0410 .0509 .0478 .0566 .0532 .0449 .0458 .0463 | .0544(23) / .0570(24) |
| mix d1 | −.9892+.1465k | .14707 | i | 8 (4/4) | 864 | 512×6 | .3307(13) | .0431 .0529 .0458 .0440 .0444 .0478 .0483 .0495 | .0573(14) / .0623(27) |
| mix d2 | −.9571+.2899k | .29413 | i | 8 (4/4) | 864 | 512×6 | .3360(24) | .0448 .0458 .0461 .0424 .0410 .0482 .0473 .0453 | .0624(6) / .0641(15) |
| mix d3 | −.8319+.5549k | .58827 | i | 8 (4/4) | 864 | 512×6 | .3301(15) | .0461 .0431 .0511 .0600 .0473 .0508 .0505 .0490 | .0578(22) / .0582(15) |
| clear k0 | .747+.484i+.294j−.347k | – | B̂ of H=(.338,.023,−.905,.257) | 8 (4/4) | 864 | 256×6 | .3391(45) | .0881 .0838 .0981 .0989 .1099 .0831 .0902 .0771 | .0076(5) / .0067(2) |
| clear k1 | .921+.333i+.035j+.197k | – | B̂ of H=(−.007,−.619,.200,−.759) | 8 (4/4) | 864 | 256×6 | .3361(33) | .1126 .1110 .1256 .1122 .1251 .1017 .0842 .1097 | .0045(2) / .0043(5) |
| clear k2 | .416+.495i−.730j+.223k | – | B̂ of H=(.811,.300,−.376,−.332) | 8 (4/4) | 864 | 256×6 | .3395(22) | .0841 .0755 .0751 .0726 .0641 .0626 .0958 .0705 | .0142(5) / .0124(3) |

### Raw loss, variance and quotients

| run | J1 | Var1 | r1 | J4 | Var4 | r4 | β·r4 | r4 hot / cold | minang |
|---|---|---|---|---|---|---|---|---|---|
| control replay | .00757(46) | .1138(59) | .0666(66) | .00281(11) | .0476(13) | .0590(38) | .2006 | – | 0 |
| mix d0 | .00720(13) | .1190(31) | .0605(24) | .00266(3) | .0557(16) | .0478(17) | .1626(58) | .0492(25) / .0465(24) | 0 |
| mix d1 | .00747(11) | .1203(15) | .0621(12) | .00279(6) | .0598(17) | .0467(12) | .1587(41) | .0485(18) / .0451(12) | 0.14707 |
| mix d2 | .00751(5) | .1262(28) | .0595(13) | .00284(4) | .0632(8) | .0450(9) | .1529(30) | .0453(13) / .0446(14) | 0.29413 |
| mix d3 | .00785(15) | .1262(25) | .0623(19) | .00286(5) | .0580(12) | .0494(17) | .1678(59) | .0501(35) / .0486(12) | 0.58827 |
| clear k0 | .00792(26) | .1102(33) | .0719(34) | .00065(1) | .00719(31) | .0898(35) | .3054(120) | .0849(42) / .0955(43) | 0.83099 |
| clear k1 | .00770(17) | .1093(24) | .0705(19) | .00048(1) | .00441(24) | .1083(53) | .3680(179) | .1085(24) / .1081(116) | 0.82833 |
| clear k2 | .00776(16) | .1091(35) | .0711(28) | .00099(3) | .01330(43) | .0742(37) | .2523(126) | .0698(29) / .0794(69) | 0.96952 |

Notes on these rows:
- **Per-stream one-face ratios and stream means of f4** are in `results/summary_final.json`, under `per_stream`. As examples, the stream means of f4 are −0.30 to −0.34 at δ=0, and −0.13 to −0.18 at δ=2/β.
- **Integrated autocorrelation time of f4** is about 0.5–1.4 measurements, a descriptive Sokal-window estimate.
- **minang in the perturbed runs.** It equals δ exactly, because the minimum over all coarse faces is attained by the faces that share the displaced edge.
- **Clear-run variant.** With B = the raw xz holonomy H (G4's code literally) instead of B̂, the clear runs give r4 = .0905(45), .1082(53) and .0824(39).

### Per-colour J_k (colour k = 8·plane + px + 2py + 4pz)

Every colour not listed is exactly 0.

| run | f1: xy-000 | f1: xy-100 | f1: xy-010 | f4: xy-000 | f4: xy-100 | f4: xy-010 | f4: xy-110 |
|---|---|---|---|---|---|---|---|
| d0 | .0780 | .0482 | .0466 | .02068 | .02019 | .00936 | .01369 |
| d1 | .0797 | .0520 | .0476 | .02158 | .02135 | .00949 | .01459 |
| d2 | .0762 | .0543 | .0498 | .02120 | .02234 | .00979 | .01492 |
| d3 | .0851 | .0535 | .0499 | .02194 | .02133 | .01014 | .01534 |
| clear k0 | .0823 | .0558 | .0520 | .00405 | .00425 | .00356 | .00364 |
| clear k1 | .0811 | .0537 | .0502 | .00288 | .00282 | .00284 | .00291 |
| clear k2 | .0841 | .0504 | .0517 | .00694 | .00550 | .00547 | .00577 |

The reported J is the average of J_k over all 24 colours.

### Clear-skeleton sampling and the realisation of W_δ

**Clear-skeleton sampling.**
- Two unconditioned chains, each a heat-bath sweep plus a reflection sweep per cycle as in G4's pilot. Hot start, 200 discarded cycles, then 30 configurations 10 cycles apart: 60 skeletons in all.
- The two chains' plaquette averages are .7596/.7600 and .7607/.7602 (first half / second half).
- Distribution over all 60 skeletons of the smallest angle from −I (quantiles 0/10/25/50/75/90/100%): .172/.512/.689/.816/.908/1.001/1.135.
- On average 0.7 faces per skeleton are within π/4 of −I.
- 31 of the 60 skeletons are clear at θ = π/4, and 58 at π/8.
- Kept, by the pre-fixed rule: the first three at π/4 (chainA cfg 0, 1 and 4). Cfg0 and cfg1 are 10 cycles apart in the same chain, so they are not independent draws.

**Realisation of W_δ.** I used G4's disk convention: W_δ = −cos δ + e_z sin δ and B = e_x, with e_x = i and e_z = k in G4's quaternion order (1, i, j, k).
- All skeleton links are set to the identity, except the first fine half of the coarse y edge at (2,0,0), which is set to W_δ, and the first fine half of the coarse z edge at (2,0,0), which is set to i.
- The marked xy square then has holonomy W_δ, and the xz square has holonomy i, which is perpendicular to the k axis.
- Both holonomies were checked in the .meta files.

### Paragraph

- **Perturbed backgrounds.** The quotient at the perturbed backgrounds is equal, within errors, to the quotient at δ = 0. The four-face r4 values are .0478(17), .0467(12), .0450(9) and .0494(17). The one-face r1 values are .0605(24), .0621(12), .0595(13) and .0623(19).
- **Comparison with G4's disk.** β·quotient does not move in the direction of G4's disk prediction (1.1785 → 1.1903 → 1.2250 → 1.3572, relative factors 1.010, 1.039, 1.152). The box's β·r4 is 0.163, 0.159, 0.153, 0.168, relative factors 0.976(43), 0.940(38), 1.032(51). That is 0.8σ, 2.6σ and 2.3σ below the disk's relative change. The absolute level is about 7× below the disk's.
- **Clear backgrounds.** The three clear skeletons (smallest all-face clearance 0.83–0.97 rad) give higher four-face quotients: r4 = .0898(35), .1083(53) and .0742(37), with β·r4 = 0.31, 0.37 and 0.25. The one-face r1 is .070–.072. In the clear runs, both J4 and Var4 are smaller than at −I, by about 3–5× and 4–13× respectively.
- **Baths.** In all runs, only the 3 (f1) or 4 (f4) xy colours that contain the marked square's free links carry any loss. No other bath contributes.

## 3. Hypotheses each statement uses, and where they are stated

- **The measurement** (g4/full-complement/fixed.md, replicas.md, replicas.rs):
  - The frozen raw skeleton is all fine halves of coarse spatial edges on t=0 (`frozen()` in replicas.rs).
  - The pair refresh is an exact draw from the joint conditional law. This needs the pairs within one colour not to interact; G4 cites a geometry check of no same-colour conflicts (replay.md). The child checked it independently at side 6 (24/24 colours). I did not check it at side 8.
  - The variance is the pooled plug-in variance, biased down by mean subtraction (fixed.md). The pooled mean is the estimate of the fibre mean.
  - Streams are independent.
  - The periodic time preparation is T = 2N = 16, which is not the vacuum (fixed.md, replicas.md).
- **Errors.** The delete-one-stream jackknife over 8 streams assumes independent streams. Within-stream autocorrelation is absorbed into the per-stream estimates.
- **The disk prediction** (g4/sparse-coarse-fields/disk.md):
  - planar four-face disk;
  - three adjacent-pair baths;
  - the limit β → ∞ at δ = c/β;
  - B = e_x perpendicular to the displacement axis e_z.

  The 4D box at finite β satisfies none of the first three. G4 states this ("another measure and other heat baths", comparison.md).
- **The clear threshold** 0 < θ ≤ π/4 comes from the gate definition in g4/sparse-coarse-fields/comparison.md. I used θ = π/4.
- **For clear skeletons, B = B̂**, the normalised traceless part of the actual xz holonomy. This is my choice, following the brief. G4's code uses the raw holonomy H; both are reported.
- **The tolerances** are two combined jackknife σ (T1, T1b, C4, C5); exact equality for byte comparisons (C1, C2, C2′); the rounding of the published table (C3a); and 0.002 for the plaquette halves (P_gen), as a sanity check only.

## 4. Failed predicates (all kept)

1. **C1 (bitwise replay of G4's archived minus8 streams with G4's unchanged binary): FAILED.** The cause is a floating-point divergence between builds. This was my expectation; it is not a target defect.
2. **C2 as written (mix8 at δ=0 byte-identical to G4's archive): FAILED** for the same reason. The post-hoc C2′, identical to my build of G4's binary, is MET.
3. **C4 (my replay of G4's 4×144 design within 2σ of 0.0441(20)): FAILED.** The replay gives 0.0590(38), 3.4σ away. I read this as G4's error bar for that design being understated (row "DEFECT" above). The 8×512 run meets C5.
4. **T1b for clear k2 (hot vs cold Var4 within 2σ): FAILED** at 3.2σ (.01419(50) vs .01237(27)). The ratio predicate T1 for the same run is met. This could be a thermalisation problem with the hot/cold variance or an underestimated error from 4 streams per stratum; I cannot tell which.
5. **From the child:**
   - Its P3 (β=0 J1/Var1 = 1/24) failed. Its own expectation was wrong: 3 colours touch f1, so the correct value is 3/24. I verified this count by hand, and it agrees with my per-colour data.
   - The grandchild's model relied on the same wrong assumption.

## 5. What I did not check

- **Side 6:** not in my brief. The child did a reduced side-6 control only.
- **Exactness of the pair law at β > 0** against a brute-force two-link integral.
- **Same-colour non-interaction at side 8.**
- **G4's D_m replica denominator** (replicas.md). Following fixed.md, I used only the plug-in variance at the fixed skeleton.
- **Physics beyond the brief:** a distinct-time test, the vacuum or longer-T limit, and other couplings.
- **More than 3 clear skeletons.** No independent chains per skeleton beyond hot/cold streams. No check of the clear-run ratio's dependence on burn-in beyond the hot/cold comparison.
- **The recentred exact pair proposal:** not exercised. It is active only for β ≥ 8 in G4's code; at β = 3.4 the plain proposal is used.
- **Lean:** not used (READY exists, but no Lean claim is made).

## 6. Delegated questions and outcomes

- **Child, T207** (admitted under T206; graph event 414; released, event 420). Model: sonnet, run via `pcp check child-run1` (K3, exit 0, 221 s).
  - Question: an independent implementation of G4's side-6 W=−I control at reduced statistics.
  - Its control question: Haar E[a0²] = 0.25. Its answer was 0.250000, correct, and I graded it first.
  - It returned r4 = 0.0501(19), r1 = 0.0589(17), Var4 = .0569(21), spread .3417(28). That is 4 streams × 500, burn 288, seed 2026, with 50-sample block-jackknife errors.
  - I reread mc.rs (heat bath, staple convention, pair refresh, colours, observables) and reran it (K6, exit 0). The output is byte-identical.
- **Grandchild, T209** (parent T207, admitted at event 416 and released at event 419, both by the child).
  - Question: a β=0 Haar check of J1/Var1.
  - Its control was a Monte Carlo of E[a0²]: 0.24889(56), 2.0σ from 0.25.
  - Its result, 0.041705(81), matches its single-colour assumption of 1/24. That assumption is wrong for the actual colouring (3/24). The child caught this and reran it; I reread its run.py and result.txt.

## 7. PCP OS record

Register `pcp/`: K1 control (exit 1), K2 control-reduce (exit 1), K3 child-run1 (exit 0), K4 mix-runs, K5 clear-runs, K6 child-rerun (all exit 0).

- `$P verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## 8. Exact commands to rerun

These are also in REPLAY.md. Run from /home/user/z4-workers/z1-mix8; output files are create-new, so move existing results/ aside first.

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
mkdir -p build/g4/full-complement build/g4/full-attempt/two-site-gap
cp g4/full-complement/replicas.rs build/g4/full-complement/
cp /home/user/Millennium-Prize-Problems/yang-mills/g4/full-attempt/two-site-gap/wilson_mc.rs build/g4/full-attempt/two-site-gap/
(cd build/g4/full-complement && rustc --edition=2021 -O replicas.rs -o replicas)
(cd build/g4/mix8 && rustc --edition=2021 -O mix8.rs -o mix8)
$P check --ws pcp --name control --expect-exit 0 -- python3 control.py
$P check --ws pcp --name control-reduce --expect-exit 0 -- python3 control_reduce.py
$P check --ws pcp --name mix-runs --expect-exit 0 -- python3 run_mix.py
$P check --ws pcp --name clear-runs --expect-exit 0 -- python3 run_clear.py
python3 analyze_all.py <new tag>
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P check --ws pcp --name child-rerun --expect-exit 0 --cwd child -- bash -c "rustc -O -o mc_rerun mc.rs 2>/dev/null && ./mc_rerun 3.276133577 4 288 500 6 2026 rerun_main.csv && python3 analyze.py rerun_main.csv"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Individual stream commands and seeds are written in each `results/**/*.meta` and in REPLAY.md:
- mix: seed 3000451 + 100000k + 7919i, hot = i%2, 864 burn, 512 samples;
- clear: seed 5000451 + 100000m + 7919i, 864 burn, 256 samples;
- gen: seeds 4000451 and 4100451.

The rustc version was 1.97.0. Bitwise replay of these files needs the same build.

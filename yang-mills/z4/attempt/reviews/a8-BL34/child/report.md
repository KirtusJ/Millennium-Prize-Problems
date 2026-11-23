# Report: SU(2) smallest box (child worker)

**Control:** smallest eigenvalue of the 5x5 Dirichlet path Laplacian = **0.267949** (= 2 - sqrt 3), in `control.txt`.

## Numbers
- T1: lambda = **0.837722340** (the other eigenvalues are 6, 6, 6, 7.16228, 8, 8). lambda/16 = 0.0523576. C_pp for (1,2,+,+) = **0.291666667 = 7/24**. Every diagonal entry of D Qmat^-1 D^T is 7/24, and the trace is 7. So (3/2) C_pp = **0.4375**.
- T2: I used my own BFGS, because **scipy is not installed and there is no network**. This deviates from the task text. The starts were 10 near, 10 mid and 10 far (link angles up to pi), 30 per sample. A minimiser is local, so c_eff is the min of the values found, which is an upper bound on the true infimum. Each beta was run once, with fixed seeds.

| beta | M | c_eff (min over 20 samples) | median |
|---|---|---|---|
| 10 | 1 | 0.18395 | 0.18415 |
| 10 | 3 | 0.26587 | 0.26766 |
| 100 | 1 | 0.17472 | 0.17474 |
| 100 | 3 | 0.18291 | 0.18319 |
| 1000 | 1 | 0.17380 | 0.17380 |
| 1000 | 3 | 0.17462 | 0.17464 |

  All values are about 3.3 to 5 times lambda/16 = 0.0524. For beta >= 100 the minimum sits near 0.174.
- T3: target 0.4375. Final run `t3b`: step 0.5/sqrt(beta), 64 chains, 20000 sweeps, 1280 batch means.

| beta | mean | SE | rel. dev. | acceptance |
|---|---|---|---|---|
| 10 | 0.438867 | 0.000822 | 0.0031 | 0.375 |
| 100 | 0.437357 | 0.000853 | 0.0003 | 0.367 |
| 1000 | 0.437448 | 0.000852 | 0.0001 | 0.367 |

  The first run `t3` used step 1.5/sqrt(beta) and gave means 0.442713 (SE 0.001685), 0.437663 and 0.437844. It is kept in `out/t3_beta*.txt`.

## Predicates
Tolerances: P1 uses 1e-9, far above float error and far below the expected O(1) value. P4's 4 SE is a ~99.99% Gaussian band, and its 5% allowance is from the task text.

| Predicate | Status | Detail |
|---|---|---|
| P1 lambda > 0 | **met** | 0.8377 |
| P2 c_eff > 0 for all samples | **met**, but trivial | 120 of 120 cases qualify. The numerator is at least 7M^2 > 0, so the predicate cannot fail. |
| P2b (added, fixed before the run) c_eff_sample >= lambda/16 | **met** | 120 of 120 qualify |
| P3 c_eff vs lambda/16 | measured only | c_eff is about 0.174 to 0.266, against 0.0524 |
| P4 beta = 1000 MC mean within max(4 SE, 5%) | **met** | deviation 0.00005, about 0.06 SE (run 1: 0.0003) |
| P5 rel. dev. at 1000 < at 10 | **met** | 0.0001 < 0.0031 (run 1: 0.0008 < 0.0119) |

**Failed expectation (mine, not the target's):** the t3 docstring expected 30–60% acceptance, and the real figure was about 5%, because I chose the step badly. I retuned it in `t3b.py` (new seed, new files) and kept run 1. The predicates P4 and P5 were unchanged, and both runs satisfy them.

**Caveat on P4/P5:** the SE is about 0.2% of the target. At beta = 100 and 1000 the deviations are within noise, so the MC cannot resolve the expected O(beta^-1/2) bias. At beta = 10 the deviation is 1.7 SE in run `t3b` and about 3 SE in run `t3`. The comparison in P5 is therefore only weakly informative.

## Sub-agent
- **Question:** independently recompute lambda and C_pp from the definitions, without seeing my code.
- **Known-answer control:** tridiag(-1,2,-1) 3x3, expected 2 - sqrt 2. It returned 0.585786438, which is correct.
- **Result:** lambda 0.837722340, C_pp 0.291666667, trace 7.000000000.
- **My rerun** of `grandchild/prog.py` gave identical output. It also agrees with my T1 (0.8377223398, 0.2916666667).

## PCP OS
The method was reported as not found, as expected. Ten checks (K1–K10) all exited 0.
- `$P verify --ws pcp` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl` last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.` The line before it is `register file SHA-256: 9fe847e03472adb3d221c43f1c7b8a8354aa58b05fb7c16b6cfe140956301d6c`.

## Rerun
The result files are opened with mode "x", so remove `out/` and `pcp/` first, or work in a fresh copy.
```
cd /home/user/z4-workers/a8-BL34/child; mkdir out
python3 t1.py; for b in 10 100 1000; do python3 t2.py $b; python3 t3.py $b; python3 t3b.py $b; done
python3 grandchild/prog.py
```
Files: `su2lib.py`, `t1.py`, `t2.py`, `t3.py`, `t3b.py`, `notes.md`, `out/`.

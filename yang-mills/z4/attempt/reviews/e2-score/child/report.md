# T232 report: Z / score identity test, two-link SU(2)

**Control:** 6·∫₀¹x²dx − 1 = 1.000000 (control.txt).

## Method
Exact conditional heat-bath Gibbs (u|v with staple h_u+MvNC, v|u with staple h_v+NCuM; rejection sampler for the a0 density), 1000 independent chains from Haar, 400 burn-in sweeps, 100 recorded sweeps → 1e5 samples per case. SE from chain means. 4 betas × 5 exteriors (exterior e identical across beta, seed 100+e). Predicates are in the docstring of `zscore.py`, written before the first run. Z was derived with D_aE_bA_ab = Y (e_a²=−1 twice), E_bA_ab=−Re(C u e_a M v N), D_aA_ab=−Re(C u M v e_b N), E_b s_a = β A_ab.

## Table (all 20 cases)
| beta | ext | ‖Z‖/beta | E Z ± se | E[(Y-EY)Z] | E[2+Y²] | diff ± se | Var(Y) | ratio | flags P1-P7 |
|--|--|--|--|--|--|--|--|--|--|
| 1 | 0 | 6.703 | -0.006 ± 0.021 | 2.2726 | 2.2697 | 0.0029 ± 0.0084 | 0.2175 | 281.9 | 1111111 |
| 1 | 1 | 5.867 | 0.018 ± 0.018 | 2.2607 | 2.2642 | -0.0034 ± 0.0072 | 0.2334 | 302.5 | 1111111 |
| 1 | 2 | 6.555 | 0.020 ± 0.020 | 2.2923 | 2.2950 | -0.0027 ± 0.0077 | 0.2012 | 260.8 | 1111111 |
| 1 | 3 | 5.598 | -0.002 ± 0.017 | 2.2657 | 2.2726 | -0.0069 ± 0.0071 | 0.2262 | 293.1 | 1111111 |
| 1 | 4 | 6.898 | -0.055 ± 0.022 | 2.3136 | 2.3130 | 0.0006 ± 0.0083 | 0.1854 | 240.3 | 1111111 |
| 3.3 | 0 | 5.008 | 0.037 ± 0.054 | 2.2998 | 2.3197 | -0.0199 ± 0.0150 | 0.1054 | 1487.7 | 1111111 |
| 3.3 | 1 | 3.647 | 0.025 ± 0.037 | 2.2802 | 2.2961 | -0.0159 ± 0.0126 | 0.1598 | 2255.3 | 1111111 |
| 3.3 | 2 | 4.974 | 0.064 ± 0.052 | 2.4922 | 2.4780 | 0.0142 ± 0.0134 | 0.0678 | 956.5 | 1111111 |
| 3.3 | 3 | 3.632 | -0.044 ± 0.037 | 2.3654 | 2.3595 | 0.0058 ± 0.0108 | 0.1248 | 1761.2 | 1111111 |
| 3.3 | 4 | 5.411 | 0.005 ± 0.054 | 2.5742 | 2.5752 | -0.0009 ± 0.0130 | 0.0440 | 620.5 | 1111111 |
| 10 | 0 | 4.679 | -0.190 ± 0.151 | 2.3590 | 2.3646 | -0.0056 ± 0.0298 | 0.0360 | 4667.0 | 1111111 |
| 10 | 1 | 3.248 | -0.069 ± 0.102 | 2.3616 | 2.3416 | 0.0200 ± 0.0236 | 0.0616 | 7987.2 | 1111111 |
| 10 | 2 | 4.780 | 0.143 ± 0.151 | 2.6271 | 2.6286 | -0.0015 ± 0.0231 | 0.0180 | 2335.6 | 1111111 |
| 10 | 3 | 3.364 | -0.120 ± 0.104 | 2.4736 | 2.4619 | 0.0117 ± 0.0210 | 0.0394 | 5108.8 | 1111111 |
| 10 | 4 | 5.310 | -0.185 ± 0.168 | 2.7684 | 2.7724 | -0.0041 ± 0.0206 | 0.0086 | 1119.3 | 1111111 |
| 30 | 0 | 4.581 | -0.570 ± 0.426 | 2.4054 | 2.3882 | 0.0172 ± 0.0553 | 0.0121 | 14084.5 | 1111111 |
| 30 | 1 | 3.147 | 0.455 ± 0.311 | 2.3249 | 2.3720 | -0.0471 ± 0.0455 | 0.0204 | 23845.1 | 1111111 |
| 30 | 2 | 4.820 | -0.485 ± 0.458 | 2.7149 | 2.6935 | 0.0214 ± 0.0408 | 0.0055 | 6357.7 | 1111111 |
| 30 | 3 | 3.277 | 0.138 ± 0.308 | 2.5913 | 2.5129 | 0.0784 ± 0.0405 | 0.0124 | 14470.2 | 1111111 |
| 30 | 4 | 5.329 | 0.094 ± 0.489 | 2.8866 | 2.8552 | 0.0315 ± 0.0313 | 0.0021 | 2497.9 | 1111111 |

Mean ‖Z‖/β per beta (1, 3.3, 10, 30): 6.32, 4.53, 4.28, 4.23. Log-log slope of ‖Z‖/β vs β: -0.11. So ‖Z‖ ~ β·(≈3–7), decreasing mildly, never growing: max ‖Z‖/β = 6.90 ≪ 72. Mean Var(Y) per beta: 0.2127, 0.1003, 0.0327, 0.0105; log-log slope -0.89 (≈ β⁻¹ decay, much slower than the claimed floor β⁻²). Min ratio Var(Y/4)·20736β² = 240.3 ≥ 1 (the floor is slack by ≥ 2 orders of magnitude, growing with β).

## Predicates
All 20 cases pass P1–P7 (identity ΣA²=2+Y² to <1e-9; E Z=0 within 4 SE; IBP E[(Y−EY)Z]=E[2+Y²] within 4 SE; ‖Z‖/β≤72; ratio≥1; Cauchy–Schwarz bound; burn-in drift). Cases qualifying: 20/20 for every predicate (all "for all" claims tested per case, none failed).
Note: E Z and IBP checks are noisy at β=30 (SE up to 0.5 on E Z, because Z has size ~β) so they are statistically consistent but weak there.
Tolerances: 4σ from MC chain-mean SE (a 4σ rule gives false-alarm probability ~6e-5 per test); 1e-9 roundoff; 1% on CS (MC noise in Var).

## Failed predicates / failed runs
- Run K1 of zscore.py exit 1: my own defect (numpy bool not JSON-serializable at the final dump); fixed by casting, no change to predicates. Not a defect of the target. No substantive predicate failed.
- Caveat: all exteriors have |h|≈ sqrt(5)-ish random sums (|h|≤5); statements are for these 5 draws only, 5 exteriors per beta is a sample, not a proof. Gibbs mixing was verified only via the first/second-half drift (P7), not exhaustive.

## Grandchild
Question: zero-staple h_u=h_v=0, β=1, independent recomputation (importance sampling 2e6, own code, finite-difference check of A_ab, own known-answer control 1.000000). Task id **T234** (admitted with parent T232, released after return). Outcome: E[(Y−EY)Z]=2.279421±0.001750 vs E[2+Y²]=2.279665±0.000226 (z=−0.16); E Z=0.0062±0.0045; ‖Z‖/β=5.134; identity error 3e-15; FD error 5.8e-9. Its first run had its own bug (conj in helper) caught by its FD check. I reread the code's report and reran `check.py` (PCP check K3): identical numbers.

## Rerun commands
```
cd /home/user/z4-workers/e2-score/child
rm -f zscore_results.json zscore_rows.jsonl
python3 zscore.py            # ~21 s
cd grandchild && rm -f results.md && python3 check.py
```

## PCP OS
`pcp_os.py verify --ws pcp` last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)".
`pcpos verify pcp/register.jsonl` last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
Register checks: K1 (failed run, exit 1), K2 (zscore, exit 0), K3 (grandchild rerun), K4 (report present).

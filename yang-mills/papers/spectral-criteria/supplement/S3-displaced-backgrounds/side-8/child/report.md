# T207 report — Z1-mix8 (own Rust implementation, reduced statistics)

control.txt = 0.250000 (E[a0^2]=1/4; grandchild MC 0.24889±0.00056).

## Results (main run)
Used: beta=3.276133577, N=6, T=12; 4 streams (cold,hot,cold,hot), 288 burn-in sweeps, 500 measurements/stream every 6 sweeps (2000 total), seed 2026, 24 colours x two refreshes per measurement. Errors: jackknife over 50-sample blocks.

| quantity | mine | reference | agree (2σ combined)? |
|---|---|---|---|
| J/Var f1 | 0.0589 ± 0.0017 | 0.0639 ± 0.0023 | yes (1.8σ) |
| J/Var f4 | 0.0501 ± 0.0019 | 0.0464 ± 0.0055 | yes (0.6σ) |
| mean spread | 0.3417 ± 0.0028 | 0.344 ± 0.008 | yes |
| Var f4 | 0.0569 ± 0.0021 | 0.062 ± 0.007 | yes |
| Var f1 (no ref) | 0.1298 ± 0.0035 | – | – |
J1=0.00764, J4=0.00285 (J = per-colour-averaged).

## Verdict table
| item | verdict | evidence |
|---|---|---|
| control E[a0^2]=0.25 | STANDS | analytic 1/4; grandchild MC agrees |
| P1 colours independent & pair links free | STANDS | 24/24 pass (programmatic check) |
| P2 frozen links unchanged, |U|=1 | STANDS | asserts passed at end of every stream |
| P3 beta=0: J1/Var = 1/24 | DEFECT of my (and grandchild's) expectation | got 0.129±0.0023; 3 colours (xy-plane parities 000,100,010) contain the f1 links (per-colour J1 ≈0.25 each, rest 0) so correct Haar prediction is 3/24=0.125 (1.7σ). Not a target defect |
| P4 J/Var f1 vs reference | STANDS | above |
| P4 J/Var f4 vs reference | STANDS | above |
| pair-refresh exact law | NOT CHECKED directly | only P1 independence + beta=0 consistency; no beta>0 detailed-balance test |
| Wilson heat-bath correctness | NOT CHECKED directly | no plaquette-vs-known comparison; indirect agreement with reference only |

## Not checked
Pair-law at beta>0 against brute force; autocorrelation beyond block jackknife (blocks of 50 samples=300 sweeps); cold vs hot stream agreement; fewer samples than reference (2000 vs reference's unknown); mean f is non-zero (-0.28), pooled plug-in variance as specified.

## Grandchild
Question: beta=0 Haar check of J1/Var for f1 (prediction 1/24, with control E[a0^2]). Task T209 (admitted, released). Outcome: control 0.24889±0.00056; Var=0.25006; J/Var 0.041705±0.000081 for its single-colour model — matches its own assumption but that assumption (only 1 of 24 colours touches f1) is wrong; my full code shows 3 do. Reread and rerun in /tmp/gcrerun: reproduced identical numbers.

## PCP OS
verify --ws pcp: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right." (preceded by "result: PASS")
pcpos verify pcp/register.jsonl: same last line.

## Rerun
cd /home/user/z4-workers/z1-mix8/child; rustc -O -o mc mc.rs
./mc 0 2 5 2000 1 11 NEWFILE_beta0.csv ; ./mc 3.276133577 4 288 500 6 2026 NEWFILE_main.csv ; python3 analyze.py NEWFILE_main.csv
(output files open with create_new; existing out_*.csv must not be reused)
## Status: met (main run agrees with reference), one predicate failed (P3, own expectation), pair-law and heat-bath only measured indirectly.

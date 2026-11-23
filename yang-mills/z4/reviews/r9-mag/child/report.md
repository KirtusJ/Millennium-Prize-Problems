# Report: electric-endpoint note (L = kappa/18), child r9-mag

Control (step 0): 99/32 - max_{u in [0,2]} (2-u)(289/256+27u/16) = 39167/442368 = **0.088539** (in control.txt; the max is at u=575/864, value 1329409/442368).

## Verdicts
| Item | Verdict | Evidence (one line) |
|---|---|---|
| (a) uK <= 289/256 + 3u/16 (from K+gu <= 17sqrt(g)/8+3/16) | STANDS | 17t/8 - t^2 <= (17/16)^2 = 289/256 with t = sqrt(g)u; checked by hand and exactly (E4). |
| (a) sphere step: 9 <= (16K+24)S | STANDS | (3-4S)^2 <= 16KS expands to 9 <= 16KS+24S-16S^2; negative branch gives S>3/4, so 24S>18 (needs K>=0). |
| (a) (2u-u^2)(K+3/2) <= (2-u)(289/256+27u/16) <= 99/32 | STANDS | Identity (2-u)(uK+3u/2) holds and 3/16+3/2=27/16 (E2); max = 1329409/442368 = 3.00513 <= 3.09375 (E1). |
| (a) 2u-u^2 <= (11/2)S | STANDS | (99/32)(16/9) = 11/2 exactly (E3); 20000 random exact-rational instances satisfying the hypotheses all pass, worst (2u-u^2)/S = 5.318 (E5). |
| (a) M1 >= (2kappa/9)M0 | STANDS | M0 = 4(2u-u^2-S) <= 4(11/2-1)S = 18S = (9/(2kappa))M1 (E3). |
| (b) nu([kappa/18, 4D/A]) >= A^2/(8D) | STANDS | Pointwise E <= L + E^2/U + U*1_[L,U](E); L*M0 <= M1/4 and M2/U <= A/4, so U*nu >= A/2. 20000/24811 random 1-4-atom measures met the hypotheses, none failed (B2), worst ratio 6.40. |
| (b) 4D/A > kappa/18 | STANDS, and holds automatically | D >= M1^2/M0 >= (2kappa/9)A, so 4D/A >= 8kappa/9 > kappa/18; no sample failed (B3). |
| (b) sharpness | STANDS (not tight) | Optimizing over 3-atom measures gives min nu([L,U])/(A^2/(8D)) = 6.92 (D/(kappa A)=5/18), 4.58 (100/18), 4.5002 (10^6/18), so the infimum is 9/2. The minimizer is an atom just below L plus a band atom at e solving 3Ae^2 = 4D(e-L). A generic random search never went below this (B5). |
| Task 3: which inequality improved | STANDS | Old A/16: L*M0 <= (A/16)*4 = A/4 used the mass bound M0 <= 4. K_F variant: L = A/(4K_F) with M0 <= K_F = min(4, 8B/g). New: L*M0 <= M1/4 comes from M1 >= (2kappa/9)M0, the variance-keeping relation (a), instead of a mass bound. The term M2/U <= A/4 is unchanged. |
| Task 3: is kappa/18 independent of g? | STANDS | L = kappa/18 has no B or g in it. A/16 = 9kappa/(128(1+B)) and A/(4K_F) both depend on g. |
| Wording "stronger uniform choice" | DEFECT (wording only) | For g < 17/64 (B = g < 17/64) we get A/16 = A/(4K_F) > kappa/18, e.g. 0.0703kappa vs 0.0556kappa as g -> 0 (B6). The new edge is higher only for g >= 17/64, where it beats A/(4K_F) too (B7: A/(4K_F) <= kappa/18 there, max ratio 0.9992; A/(4K_F) -> 0.0077kappa at large g). The note does say the A/16 band remains valid, so taking max(A/16, kappa/18) fixes it. |
| D_* (third-moment bound), Lean replay in execution.md, operator inputs (energy form M1 = 4kappa S, K+gu <= B) | NOT CHECKED | Not derivable from the given text; no network or Lean run. |

## Failed predicates and whose error
- In band_b2.py, predicate B4 passed, but its minimum (3.88 at D=100) was wrong. The hand 2-atom analysis gives at least 9/2. The cause was my optimizer: it accepted p = -1e-10 at E ~ 4e5, which corrupts M2 by about 18. **My tool was wrong, not the target.** It is fixed in band_b3.py, which clips negatives before checking feasibility with a relative tolerance. Predicates are unchanged; the D grid is extended. All of B1-B6 pass in band_b3.
- B6 (old edge higher exactly for g < 17/64) was a prediction I made by hand before running, and it was confirmed. It is the source of the wording DEFECT above.
- band_b.py was stopped because it was too slow (unvectorized). Its band_b.out.txt is empty and was left as is. No result file was overwritten.

## Rerun commands
```
export PYTHONUTF8=1; cd C:/Users/donke/z4-workers/r9-mag/child
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name exact_a --expect-exit 0 -- python scripts/exact_a.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name band_b3 --expect-exit 0 -- python scripts/band_b3.py   # ~2 min
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```
PCP verify, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

Files: child/control.txt, child/notes.md, child/scripts/{exact_a,band_b,band_b2,band_b3}.py, child/{exact_a,band_b,band_b2,band_b3}.out.txt.

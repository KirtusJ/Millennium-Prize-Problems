# T8 report: Binder cumulant U4 of the 2D Ising torus at K_c

Control: K_c = ln(1+sqrt2)/2 = 0.440687 (control.txt).

| Item | Verdict | Evidence |
|---|---|---|
| U4(4), MC | STANDS | 0.617202 ± 0.000057 (20-bin jackknife); exact 0.6171993184; diff 2.7e-6, under 0.1σ |
| U4(8), MC | STANDS | 0.613200 ± 0.000091 |
| U4(16), MC | STANDS | 0.611532 ± 0.000169 |
| U4(32), MC | STANDS | 0.610658 ± 0.000280 |
| U4(64), MC | STANDS | 0.610909 ± 0.000683 (200k clusters only) |
| U4 bounded away from 0 and consistent with a universal nonzero limit | STANDS | Values fall monotonically 0.617 → 0.611 and flatten at L = 32 and 64. They are far from the Gaussian value 0. Limit from memory, not read: U4* ≈ 0.6107 for the periodic square torus. L = 32 and 64 agree with it within errors. |
| <M²>/L² vs L | STANDS | 12.1834 ± 0.0033, 41.426 ± 0.013, 139.76 ± 0.10, 469.28 ± 0.48, 1580.6 ± 5.1 for L = 4, 8, 16, 32, 64. Mean cluster size agrees with it. |
| Fitted exponent (7/4) | STANDS, within my tolerance only | Weighted fit slope 1.7518 ± 0.0006 (L = 8..64) and 1.7591 ± 0.0004 (L = 4..64). Both are inside my ±0.05 tolerance. The L = 8..64 value is about 3σ from 1.75 statistically, so the small L still carry corrections. |
| Exact 4x4 enumeration (delegated) | STANDS | U4 = 0.6171993184, <M²> = 194.9078806, <M⁴> = 43626.73935, from two implementations agreeing to 1.7e-14. I reran it. |
| Bin errors independent | NOT CHECKED | Bin length is at least 190k clusters, far above the expected autocorrelation, but I did not measure τ. |

Bins: 20 per run, with the first 5% of clusters discarded. Cluster counts: 4M (L = 4 and 8), 2M (L = 16), 1M (L = 32), 0.2M (L = 64). Seeds are 1000+L.

## Failed predicates
None failed. Predicates P1–P4 are in the header of wolff.c and were fixed before the first run. Their tolerances were my own guesses, except the 3σ in P1, which is the usual statistical choice.

## Mistakes of my own, with no effect on results
- I ran `mv result.txt /dev/null` in grandchild/. That deleted grandchild/result.txt and turned /dev/null into a regular file.
- I restored /dev/null with `mknod -m 666 /dev/null c 1 3`.
- I regenerated result.txt by rerunning ising4.py. The numbers match the sub-agent's report.
- Check `ls -l /dev/null` on this host if you care.

## Not checked
- The limit U4* ≈ 0.6107 is from memory and I read no source.
- No Wolff-vs-Metropolis cross-check.
- No autocorrelation time.
- No fit with correction-to-scaling terms.
- L = 64 has few statistics.

## Delegated question
Exact 4x4 enumeration of U4. Task id **T9**, admitted and released. Control (2x2 torus with M = 0 gives 6) passed. Outcome: matches my MC at L = 4, as in the table.

## Rerun commands
```
gcc -O2 -o wolff wolff.c -lm; mkdir res
./wolff L NCLUSTERS 1000+L res/L<L>.txt   # for L=4,8,16,32,64, with NCLUSTERS 4000000,4000000,2000000,1000000,200000
cd grandchild && python3 control.py && python3 ising4.py   # remove old control.txt/result.txt first, or they refuse to overwrite
python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Verify last lines:
- Python: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- Rust: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

Verdict counts: met 9, failed 0, measured only 0. The one NOT CHECKED row is not counted.

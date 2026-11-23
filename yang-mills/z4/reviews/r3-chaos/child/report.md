# M3/M4 report

Control: control.txt = 0.272341 (correct).

Baseline: unchanged copy in runs/orig, exit 0, H/P1/P2/P3 all MET. Output JSON byte-identical to input/two_dim_control_result.json (sha256 24939c8dd0ae5925e27abe30b45936a6a0d38ae9456e326f9a3ba476465a9d0f). Usage line in the docstring matches how the program is invoked.

## M3 mutations (every run in its own fresh dir mut/<name>/)

| name | change (line: new text) | prediction | exit | failed | outcome |
|---|---|---|---|---|---|
| a_bessel_P1 | 101: `mp.besseli(2, mp.mpf(N) ** 2) / mp.besseli(0, ...` (I_1->I_2 in U(1) gap) | P1 | 1 | P1 (factors ~0.25) | CAUGHT |
| a2_bessel_H | 62: `def u1_closed(n, b):  return mp.besseli(n + 1, b) * mp.exp(-b)` | H (then P1, since no U(1) N qualifies) | 1 | H, P1 | CAUGHT |
| b_beta_plus1 | 101: `besseli(1, mp.mpf(N) ** 2 + 1) / besseli(0, mp.mpf(N) ** 2 + 1)` | P1 | 1 | P1 (factors ~1.0) | CAUGHT |
| c_su2_2N2 | 108: `besseli(2, 2 * mp.mpf(N) ** 2) / besseli(1, 2 * mp.mpf(N) ** 2)` | P2 | 1 | P2 (factors ~1.0) | CAUGHT |
| d_asym_half | 124: `A = b * (k * d / 2) * mp.exp(-b * d)` | P3 | 1 | P3 (ratio 2.0) | CAUGHT |
| e_tolH_1e6 | 77: `TOL_H = mp.mpf(10) ** -25 * 10**6` | none | 0 | none | NOT CAUGHT |
| e2_tolP3_1e6 | 127: `near = abs(ratios[-1] - 1) < mp.mpf(10) ** -6 * 10**6` | none | 0 | none | NOT CAUGHT |

All predictions came true. Both NOT CAUGHT runs wrote JSON byte-identical to the baseline, so comparing bytes does not catch them either: the tolerances are not written to the JSON.
To catch them, a check would need either (i) the tolerances (TOL_H, the 3..5 window, 1e-6) written into the JSON and compared against the values stated in the docstring, or (ii) a negative-control predicate: a deliberately perturbed closed form (for example a relative 1e-20 change, or the wrong order) must FAIL H, and a ratio of 1+1e-5 must FAIL the P3 test. A pinned hash of the program source would also catch any edit.
Structural note: H checks u1_closed/su2_closed, but P1/P2 recompute M with their own inline besseli calls (lines 101 and 108). So H does not protect the Bessel orders or the beta used in P1/P2; only the asymptotic windows in P1/P2 catch those errors (a, b, c).

## M4
m4/two_dim_control_result.json: one digit changed at line 197 (P1.M for N=8): 0.503963426... -> 0.503973426....
- Nothing in input/ notices. The program never reads an existing result; it only refuses to overwrite one ("result file exists; refusing to overwrite", exit 1, without reading the content). No Lean file refers to the json (grep for json/result/IO found nothing).
- Detection by rerun: a fresh run in m4/rerun (exit 0), then m4/compare.py (filecmp + sha256). Against the mutated copy: equal False, exit 1 (rerun 24939c8d..., mutated bb9c686f...). Against input: equal True.
- K12 was my own mis-pathed command (exit 2, expected 1). Nothing was written and input/ is unchanged. It stays in the register.

## verify (last line)
result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)

## Rerun commands (from child/, PYTHONUTF8=1)
```
P=C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py; SP=C:/Users/donke/AppData/Roaming/Python/Python314/site-packages
python $P check --ws pcp --name orig --expect-exit 0 --cwd runs/orig -- python -I two_dim_control.py $SP
python $P check --ws pcp --name <mut> --expect-exit <1|0> --cwd mut/<mut> -- python -I two_dim_control.py $SP   # delete the old result json first, or use a new dir
python $P check --ws pcp --name m4_rerun --expect-exit 0 --cwd m4/rerun -- python -I two_dim_control.py $SP
python $P check --ws pcp --name m4_compare_mutated --expect-exit 1 -- python -I m4/compare.py m4/rerun/two_dim_control_result.json m4/two_dim_control_result.json
python $P verify --ws pcp
```

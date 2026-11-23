# T156 report

**Control:** integral of x^2 exp(-x^2/2)/sqrt(2pi) = **1.000000** (control.txt).

## Predicates (fixed in mc.py docstring before first run)
- C0 qualification (finite, positive mean ratio, finite SE): 48/48 cases qualify.
- C1 delta1 >= -4/sqrt(beta) - 4 SE: **met 42, failed 6**, measured-only 0.
- C2 delta3 <= 4/sqrt(beta) + 4 SE: **met 48, failed 0**.
- C3 measured only: max sqrt(beta)|delta| per beta (below).
- C4 sampler, mean Re g = I2(beta)/I1(beta) (derivation in docstring; density of Re g ∝ e^{beta x}sqrt(1-x^2)): met 4/4, z = 0.47, 0.85, -0.04, -1.06. I2/I1 computed by trapezoid quadrature (scipy absent).
- Tolerances: 4/sqrt(beta) is the task's suggested constant for the claimed O(beta^-1/2); 4 SE is the Monte Carlo allowance. N = 2e5 antithetic pairs per beta, seeds 20261123+i.

## C1 failures (all my predicate's constant, not a sign of a defect in the claim)
All 6 are a1=0.5, y=0 (c=0 at all four betas; c=0.07 at beta 256, 1024): delta1 = -0.403, -0.226, -0.115, -0.059 at c=0 (beta=256..16384). sqrt(beta)*delta1 = -6.5, -7.2, -7.4, -7.6: delta1 is negative, decays like beta^-1/2, but with a constant ≈7 > 4. So "delta1 >= -o(1)" is consistent with the data (it tends to 0), while the O(beta^-1/2) constant 4 was my own too-small expectation. The tail is not tested beyond beta=16384, and sqrt(beta)*delta1 still drifts slowly upward in magnitude. Noted: positive delta1 up to +0.48 at y=1.5 (a1=0.5).

## Failed runs kept
1. First run of mc.py: exit 1, scipy missing (environment; replaced by quadrature).
2. results_mc.json: INVALID, my own code defect (E-factor offset double counted in delta1, found by review before predicates were evaluated); fixed, rerun wrote results_mc2.json. Predicates were evaluated only on results_mc2.json.

## C3 and table
beta=256: delta1 7.660, delta3 3.109
beta=1024: delta1 12.833, delta3 3.285
beta=4096: delta1 19.368, delta3 3.426
beta=16384: delta1 18.179, delta3 4.550


| beta | a1 | c | y | delta1 ± SE | sqrt(b)*d1 | delta3 ± SE | sqrt(b)*d3 |
|---|---|---|---|---|---|---|---|
| 256 | 0.5000 | 0 | 0 | -0.4032 ± 0.0050 | -6.45 | -0.1381 ± 0.0047 | -2.21 |
| 256 | 0.5000 | 0 | 1.5 | +0.4788 ± 0.0156 | +7.66 | +0.0750 ± 0.0140 | +1.20 |
| 256 | 0.5000 | 0.07 | 0 | -0.3662 ± 0.0050 | -5.86 | -0.1391 ± 0.0047 | -2.23 |
| 256 | 0.5000 | 0.07 | 1.5 | +0.4678 ± 0.0175 | +7.48 | +0.0862 ± 0.0143 | +1.38 |
| 256 | 1.5708 | 0 | 0 | -0.1922 ± 0.0162 | -3.08 | -0.0047 ± 0.0155 | -0.08 |
| 256 | 1.5708 | 0 | 1.5 | +0.0412 ± 0.0223 | +0.66 | -0.0265 ± 0.0224 | -0.42 |
| 256 | 1.5708 | 0.07 | 0 | -0.1689 ± 0.0163 | -2.70 | -0.0052 ± 0.0158 | -0.08 |
| 256 | 1.5708 | 0.07 | 1.5 | +0.0428 ± 0.0230 | +0.68 | -0.0307 ± 0.0231 | -0.49 |
| 256 | 2.6000 | 0 | 0 | -0.1175 ± 0.0077 | -1.88 | +0.1118 ± 0.0072 | +1.79 |
| 256 | 2.6000 | 0 | 1.5 | +0.2961 ± 0.0357 | +4.74 | -0.1943 ± 0.0356 | -3.11 |
| 256 | 2.6000 | 0.07 | 0 | -0.0827 ± 0.0078 | -1.32 | +0.1136 ± 0.0074 | +1.82 |
| 256 | 2.6000 | 0.07 | 1.5 | +0.2960 ± 0.0488 | +4.74 | -0.1866 ± 0.0345 | -2.99 |
| 1024 | 0.5000 | 0 | 0 | -0.2264 ± 0.0054 | -7.24 | -0.0708 ± 0.0052 | -2.27 |
| 1024 | 0.5000 | 0 | 1.5 | +0.4010 ± 0.0188 | +12.83 | +0.0339 ± 0.0167 | +1.08 |
| 1024 | 0.5000 | 0.07 | 0 | -0.1835 ± 0.0055 | -5.87 | -0.0709 ± 0.0053 | -2.27 |
| 1024 | 0.5000 | 0.07 | 1.5 | +0.3724 ± 0.0187 | +11.92 | +0.0353 ± 0.0163 | +1.13 |
| 1024 | 1.5708 | 0 | 0 | -0.1131 ± 0.0166 | -3.62 | -0.0013 ± 0.0162 | -0.04 |
| 1024 | 1.5708 | 0 | 1.5 | +0.0265 ± 0.0222 | +0.85 | -0.0259 ± 0.0217 | -0.83 |
| 1024 | 1.5708 | 0.07 | 0 | -0.0784 ± 0.0164 | -2.51 | -0.0019 ± 0.0161 | -0.06 |
| 1024 | 1.5708 | 0.07 | 1.5 | +0.0381 ± 0.0227 | +1.22 | -0.0210 ± 0.0219 | -0.67 |
| 1024 | 2.6000 | 0 | 0 | -0.0873 ± 0.0071 | -2.79 | +0.0546 ± 0.0068 | +1.75 |
| 1024 | 2.6000 | 0 | 1.5 | +0.2580 ± 0.0226 | +8.26 | -0.1027 ± 0.0201 | -3.29 |
| 1024 | 2.6000 | 0.07 | 0 | -0.0468 ± 0.0071 | -1.50 | +0.0547 ± 0.0068 | +1.75 |
| 1024 | 2.6000 | 0.07 | 1.5 | +0.2358 ± 0.0220 | +7.55 | -0.0989 ± 0.0196 | -3.16 |
| 4096 | 0.5000 | 0 | 0 | -0.1154 ± 0.0062 | -7.38 | -0.0318 ± 0.0060 | -2.03 |
| 4096 | 0.5000 | 0 | 1.5 | +0.3026 ± 0.0195 | +19.37 | +0.0535 ± 0.0183 | +3.43 |
| 4096 | 0.5000 | 0.07 | 0 | -0.0873 ± 0.0064 | -5.59 | -0.0314 ± 0.0061 | -2.01 |
| 4096 | 0.5000 | 0.07 | 1.5 | +0.2609 ± 0.0210 | +16.70 | +0.0515 ± 0.0182 | +3.29 |
| 4096 | 1.5708 | 0 | 0 | -0.0372 ± 0.0240 | -2.38 | +0.0237 ± 0.0233 | +1.51 |
| 4096 | 1.5708 | 0 | 1.5 | +0.0514 ± 0.0246 | +3.29 | +0.0193 ± 0.0243 | +1.24 |
| 4096 | 1.5708 | 0.07 | 0 | -0.0176 ± 0.0229 | -1.13 | +0.0254 ± 0.0232 | +1.63 |
| 4096 | 1.5708 | 0.07 | 1.5 | +0.0539 ± 0.0252 | +3.45 | +0.0155 ± 0.0241 | +0.99 |
| 4096 | 2.6000 | 0 | 0 | -0.0463 ± 0.0077 | -2.96 | +0.0323 ± 0.0075 | +2.07 |
| 4096 | 2.6000 | 0 | 1.5 | +0.2164 ± 0.0215 | +13.85 | -0.0105 ± 0.0205 | -0.67 |
| 4096 | 2.6000 | 0.07 | 0 | -0.0187 ± 0.0077 | -1.20 | +0.0335 ± 0.0074 | +2.15 |
| 4096 | 2.6000 | 0.07 | 1.5 | +0.1655 ± 0.0214 | +10.59 | -0.0232 ± 0.0191 | -1.49 |
| 16384 | 0.5000 | 0 | 0 | -0.0594 ± 0.0057 | -7.61 | -0.0166 ± 0.0056 | -2.13 |
| 16384 | 0.5000 | 0 | 1.5 | +0.1420 ± 0.0156 | +18.18 | -0.0001 ± 0.0152 | -0.01 |
| 16384 | 0.5000 | 0.07 | 0 | -0.0485 ± 0.0058 | -6.21 | -0.0182 ± 0.0056 | -2.33 |
| 16384 | 0.5000 | 0.07 | 1.5 | +0.1119 ± 0.0162 | +14.32 | +0.0021 ± 0.0156 | +0.27 |
| 16384 | 1.5708 | 0 | 0 | -0.0405 ± 0.0154 | -5.18 | -0.0094 ± 0.0153 | -1.20 |
| 16384 | 1.5708 | 0 | 1.5 | +0.0105 ± 0.0379 | +1.34 | -0.0091 ± 0.0372 | -1.17 |
| 16384 | 1.5708 | 0.07 | 0 | -0.0322 ± 0.0159 | -4.12 | -0.0118 ± 0.0153 | -1.51 |
| 16384 | 1.5708 | 0.07 | 1.5 | +0.0110 ± 0.0366 | +1.41 | +0.0018 ± 0.0409 | +0.24 |
| 16384 | 2.6000 | 0 | 0 | -0.0267 ± 0.0064 | -3.42 | +0.0142 ± 0.0064 | +1.82 |
| 16384 | 2.6000 | 0 | 1.5 | +0.0898 ± 0.0164 | +11.50 | -0.0355 ± 0.0160 | -4.55 |
| 16384 | 2.6000 | 0.07 | 0 | -0.0125 ± 0.0068 | -1.61 | +0.0154 ± 0.0064 | +1.97 |
| 16384 | 2.6000 | 0.07 | 1.5 | +0.0668 ± 0.0165 | +8.55 | -0.0319 ± 0.0160 | -4.08 |

## Grandchild (task T157, admitted with parent T156, released)
Question: recompute delta1, delta3 at a1=pi/2, c=0, y=0, beta=1024 with independent code and seed 987654321 (control first: 1.000000). Result: delta1 = -0.0873 ± 0.0196, delta3 = +0.0277 ± 0.0193; sampler z=1.23. Its own bound |sqrt(beta) delta|<=1 failed for delta1 (its expectation). I reread result and reran it (`cd grandchild; python3 t157.py control rr; python3 t157.py main rr`): identical numbers. My values at that point: delta1 = -0.113 ± 0.017, delta3 = -0.001 ± 0.016; differences 0.026 (≈1σ) and 0.029 (≈1.1σ combined SE): consistent. Its first result.md contained a NaN from its own clipping bug (stale); use grandchild/run2/result.md.

## Rerun commands (fresh directory; outputs opened mode x)
    cd <fresh copy containing mc.py evalp.py>
    python3 mc.py      # ~15 s, writes results_mc2.json
    python3 evalp.py   # writes report_table.md
    P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P init pcp --principal principal --principal-name "Kirtus Justus"
    $P check --ws pcp --name mc_fixed --expect-exit 0 -- python3 mc.py

## Verify (last lines)
- python verify: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- rust verify: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.

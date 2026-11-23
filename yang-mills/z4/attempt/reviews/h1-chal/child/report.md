# T93 report

Control (control.txt): `2.000000`, `0.697775`. (numpy only; scipy absent, so Gauss-Laguerre and a periodic-trapezoid Bessel integral were used.)

## Numbers (t93b.py, result_t93b.json; literal definitions, no cutoff), E_trial = 3.571652, E_0 = 3.3505330
| beta | <g,g> | <g,Kg> | ln<g,Wg> | Q | nu_trial | beta^(1/3) nu | minus E_trial | times beta^(1/3) | minus E_0 |
|---|---|---|---|---|---|---|---|---|---|
| 64 | 1.868e-5 | 1.092e-5 | 18.79 | 1 (to double precision) | 30.218 | 120.87 | 117.30 | 469.2 | 117.52 |
| 256 | 1.195e-6 | 8.409e-7 | 224.2 | 1 | 238.2 | 1512.5 | 1508.9 | 9581 | 1509.2 |
| 1024 | 7.542e-8 | 6.011e-8 | 1300.9 | 1 | 1317.5 | 13279.7 | 13276.2 | 133815 | 13276.4 |

Q is computed as 1-exp(ln<g,Kg> - ln(<g,g>+<g,Wg>)) and is 1 to double precision. nu is therefore taken from logs.

## Finding
With W = exp(V)-1 and V = 2 beta sin^2 a1 sin^2 a2 sin^2 gamma exactly as stated, <g,Wg> is not small. The integrand has exponent 2 beta a^4 - 4 alpha beta^(2/3) a^2 (at a1=a2=a, gamma=pi/2), which is positive once a^2 > 2 alpha beta^(-1/3). The region a ~ pi/2 therefore dominates. The result is beta^(1/3) nu_trial far above E_trial, growing with beta, so the claim "beta^(1/3) nu_trial -> E_trial at distance O(beta^(-1/3))" is NOT supported by the statement as written. Without an R cutoff it fails by orders of magnitude. This is a property of the definition, not of the quadrature (the exact <g,Kg> and <g,g> are fine). I did not test any specific cutoff scheme to the point of convergence (see below).

## Predicates
Fixed in docstrings of t93.py / t93b.py.
- P1 Parseval < 1e-10: **met** (<=1.4e-16, all runs).
- P6 kappa_0 = 1, kappa_n decreasing: **met in t93b**; **failed in t93** (my own indexing bug, I[1:] instead of I[0:]; fixed in t93b).
- P3 (t93) 0<Q<1, W>=0: **failed** in t93 (Q=1.0, nan at beta=1024 from float overflow of e^V). Mostly a consequence of the definition (W huge), plus overflow I fixed by log-space in t93b. In t93b P3 was relaxed to 0<GK<=GG: met. The relaxation of Q<1 was made after seeing the failure; Q<1 itself is not met numerically.
- P2 doubling change < 1e-9 in beta^(1/3) nu: **failed** in t93b. Literal: 4e-14 (64), 1.2e-8 (256), 0.128 (1024). The values are of order 1e4 and the integrand has e^1300 dynamic range, so the relative change is 1e-5 at beta=1024. The nu values are therefore only good to ~4-5 digits at beta=1024, ~9 at 256, ~15 at 64. Tolerance source: result differences between (Na,Nu,M,nmax)=(200,100,40000,300) and (400,200,80000,600).
- R-cutoff variants (R=0.8, 1.0; extra, in result_t93b.json, keys *_R0.8, *_R1.0): **failed P2** (changes 0.02 to 68) because my cutoff masks quadrature nodes, which is not grid-converged. This is my own defect; **those rows are not converged and not quoted as results**. Even at R=0.8, ln<g,Wg> = 39 at beta=256, so a fixed R does not rescue the claim; a cutoff scaling as beta^(-1/6) or smaller would be needed. I did not test it.
- P4 d*beta^(1/3) bounded: **measured only** (469, 9581, 133815: growing, not bounded). P5 vs E_0: **measured only** (differences above).
- Not measured: a W-small regime (cutoff region), and exact <g,Wg> at beta=1024 beyond the 4-digit level.

## Grandchild
T94 (label h1-chal-grandchild, parent T93), admitted and released. Task: independent recomputation at beta=64 of <g1,g1>, S=sum kappa_n c_n^2 (kappa from power series, not the integral representation), Parseval. Control first: 2.000000000000 and 0.697775. Result: N0=0.004322087038731838, S=0.0033039266294994265, S/N0=0.7644285272, Parseval 5.8e-16, doubling changes ~1e-15; all four predicates met. My values: sqrt(GG)=0.0043220870387314, sqrt(GK)=0.0033039266294987, ratio 0.7644285272118: agree to ~1e-13. I reread grandchild/prog.py and reran it in a scratch copy; answer.txt was identical. The grandchild checks only <g,Kg> and <g,g>, not W.

## Failures kept
t93 (result_t93.json): P6 and P3 failed as above. t93b: P2 failed. Both exit 1 and are recorded in the register as K2, K3 (expected exit 0).

## Rerun
```
cd /home/user/z4-workers/h1-chal/child
python3 control.py            # control.txt, opens with 'x': delete outputs first or use a fresh dir
python3 t93.py                # fails (kept)
python3 t93b.py               # fails P2 (kept); writes result_t93b.json
python3 grandchild/prog.py    # run in an empty dir (answer.txt opened with 'x')
```

## Verify (last lines)
- Python `verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Rust `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

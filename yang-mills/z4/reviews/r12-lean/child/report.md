# Report
Control: control.txt = 0.008138 (sin1-1+1/6).

| Item | Verdict | Evidence |
|---|---|---|
| F1 | STANDS | 50188/100000 qualify (y>=0), 0 fails; min slack 0 (at y≈0 equality), otherwise >0 |
| F2 | STANDS | 100000/100000 qualify, 0 fails; min rel slack -6e-4 is rounding noise at tiny y (0.06 tol units); 7.8e-9 negative floor where rhs>1e-8|y| |
| F3 | STANDS | 90038 qualify (b>0), 0 fails; negative rel slack only where rhs ~ rounding noise of cancellation (≥ -0.2 tol units) |
| F4a | STANDS | 76329 qualify (|y|<=pi/2); lower min rel slack 2.9e-5, upper 1.7e-13 (tiny y), 0 fails |
| F4b | STANDS | 89604 qualify (|kb|<=pi); lower slack 1.7e-4; upper slack -2.2e-16 (equality as kb→0, 1 ulp noise), 0 fails |
| F5 | STANDS | 98020 qualify (M>=1), 0 fails; min rel slack 5.6e-2 (≈ sqrt(c/pi) at c=0.01 for large M) |
| F6 | STANDS | 98080 qualify (x>=0), 0 fails; 1000 pts at exact equality x²=j/c: max |log diff| 5.7e-14 (within tol); delegated 50-digit check confirms |

Tolerance: eps=2^-52; TOL=8 ulps-of-operand-magnitude (|lhs|+|rhs|+cancelled operand |y| or |k|) — a handful of roundings plus libm sin ≤1 ulp. F6 compared in log domain (avoids overflow), log error scale eps*(sum of magnitudes). F5 uses fsum of rounded terms, truncated at m where exp(-c m²)<~1e-300 (negligible).

Failed predicates: none failed, either from my expectation or from the target. (Negative min rel slack numbers are rounding noise inside tolerance, not failures.)

Not checked: values outside sampled ranges (|y|>30, |k|>50, b outside 1e-3..30, c outside 1e-2..1e2 for F5/F6, M>~3000, j>60); no proof — random sampling only; extended precision of F1–F5 not done (only F6 boundary by sub-agent); F4 beyond hypothesis region not tested (counted as non-qualifying).

Delegated question (grandchild/): independent 50-digit (decimal) recomputation of F6 at equality x²=j/c and at ±1e-3 around it, j∈{1,2,3,5,10,50,200}, c∈{0.01,1,37}. Outcome: control 0.008138 ok; max |rel diff| at equality 9.35e-48 (rounding at 50 digits); all 42 perturbed cases lhs<rhs, min slack 4.997e-7. I reread results.txt and reran it in a scratch copy: identical output.

PCP records: init pcp; checks K1 (check.py), K2 (rerun of grandchild). `pcp_os verify` last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)". Rust pcpos verify last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

Rerun:
  cd /home/user/z4-workers/r12-lean/child && python3 check.py results_new.txt     # (result files use mode 'x'; choose a new name)
  mkdir -p /tmp/rr2 && cp grandchild/check_f6.py /tmp/rr2/ && cd /tmp/rr2 && python3 check_f6.py
  python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp ; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl

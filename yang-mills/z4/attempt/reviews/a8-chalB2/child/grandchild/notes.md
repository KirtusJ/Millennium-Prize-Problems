# notes
- control.py: midpoint mean of 4 sin^2(k/2), N=4096 -> 1.9999999999999998 (err 2e-16), PASS. control.txt written.
- g4d.py: predicates P1-P4 in docstring, written before first run. One run, all predicates passed; no failures to report.
- Code has some redundant leftover arrays (num, den3) unused in the sum; harmless, result uses Nn/D only. Not a defect.
- Convergence in N: diffs 16->24 1.8e-7, 24->32 1.4e-8, 32->48 2.7e-9, consistent with ~N^-4 (non-smooth degree-0 point at k=0).
- Extrapolation: N^-4 Richardson (32,48) 0.0688747462; (24,48) ...4667; N^-2 (32,48) ...4774 (pessimistic). LSQ all four 0.0688747571 (dominated by N=16, less trusted).

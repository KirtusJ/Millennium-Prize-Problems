# notes
- control.txt written (0.784750). analyze.py written with predicates in docstring.
- Run 1 (analyze.py, via pcp check, exit 1): P1 FAILED: C(TRAIN) and C(HELD) have 4 eigenvalues ~1e-16 (rank 304/308) -> Cholesky fails. Target defect (exact linear relations among marks), not an implementation bug; my expectation of PD was wrong. cond(C) is infinite in 308-dim. No result file written by run 1.
- Run 2 (analyze2) crashed: my slicing dropped 'ev' line (own bug). Fixed in place, no result written.
- Run 3 crashed on JSON of numpy array (own bug), fixed.
- Run 4 (analyze2c) exit 0, results.json written; all revised predicates met.
- grandchild T225 done+released; report.md written

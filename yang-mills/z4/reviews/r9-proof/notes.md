# notes r9-proof
- step0: control.txt written
- step1: read STATEMENT, HeatRegularized (S5e), MeasureHeat (M3); PCP register pcp initialised
- step2: wrote bounds.py (predicates P0-P6 in docstring, before first run)
- step3: run K1 (bounds) exit 1: all 63 predicates MET (P0..P6) but crash at S4 tail (scipy) before result file; own program defect. Replaced scipy quad by closed form; rerun as bounds2. C_b values identical to child's table.
- step4: K2 bounds2 exit 0: 63 met, 0 failed; table in results_bounds_run1.json. v=4.74e-3 (tau=.05), 1.59e-3 (tau=.1); V=1.72e7, 1.06e5. loose 73-1658 (low), 1.3e4-9.5e4 (up). S4<=16.58
- step5: wrote R9Bounds.lean (Jordan khat, keep_terms, factor_upper, corollary via copied S5e)
- step6: K3 child_rerun exit 0, result table IDENTICAL to child's. K4 lean1 exit 0 (543 s).
- step7: verify run
- step8: proof.md and report.md written; verify PASS (parent and child). Done.

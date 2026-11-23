# notes (r2-char formalizer)
- step0: control.txt written: 0.272341
- step1: read inputs; PCP register pcp initialised; child/ created
- step2: delegated Z2xZ4 numerics to child (returned: all PASS, claim). Wrote CharTransfer.lean (F1-F4 + lam links), compiling
- step3: draft1 failed (3 noncomputable defs, wrong-side reindex in F3/F4, rw direction); kept as CharTransfer_draft1_failed.lean; patched
- step4: Lean final exit 0 (K2), draft1 exit 1 (K1), child program rerun in rerun/ (K3) exit 0, results byte-identical to child/results_1.txt; verify PASS (own and child)
- step5: report.md written. STANDS 6, DEFECT 0, NOT CHECKED 2; predicates met 5 failed 0 measured-only 0

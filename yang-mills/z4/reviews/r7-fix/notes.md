# r7-fix notes (builder: repair of two_dim_control check)
Step 0: control.txt = 0.272341 (-ln tanh 1). Read input/ program, result, chaos report.
Step 1: PCP register pcp initialised.
Step 2: wrote two_dim_control_v2.py (predicates/table/hash in docstring before first run).
Step 3: first run K1 exit 2 (expected 0). Self-check defects: TOL_H, TOL_P3, NC_H_PERT, NC_P3_OFF "in use != table".
  Cause (MY defect, not target): constants were computed before mp.dps=40 was set, so at 15 digits
  (TOL_H = 1.0000000000000000385e-25) -- unlike v1 which sets dps=40 first. The self-check caught it.
  Also the exact mpf equality test is too strict for 10**-25 vs mpf('1e-25') (ulp level).
  Fix: set mp.dps = 40 before constants (as v1); compare in-use vs table at 20 significant digits.
  Run-1 program and result kept in attic/ (not overwritten). Refusal K3 exit 4 as expected.
Step 4: v2 run2 K4 exit 0, all MET, NC all fail as expected, table OK; self --verify K5 281 leaves 0 diff. Copied v2 + result to child/src for R3 delegation.
Step 5: R2 compare K6 exit 0: 221 leaves compared (published 222 minus 'program'), 0 differences, published sha unchanged. Delegated R3 to child (background).
Step 6 (R4 probe): consistent change TOL_P3 1e-6 -> 5e-6 in table + code + re-hashed table (r4/consistent).
  K7: exit 0 standalone (NOT caught by self-check or NC_P3, since 5e-6 < NC offset 1e-5); the new result file differs
  (tolerance strings, table hash); K8: --verify against my v2 result exit 3, 3 differences, first = tolerance_table_sha256.
  So a consistent loosening below the NC margin is caught only by --verify against a trusted stored result.
Step 7: my own reruns (independent copies, rerun/): m6 TOL_H x1e6 -> K9 exit 2, defects "TOL_H in use 1.0e-19 != table 1e-25"
  and "negative control NC_H passed" (two mechanisms). m8 changed digit -> K10 exit 3, first difference /P1/M[1].
  Waiting for child R3 report.
Step 8: child returned 8/8 caught; diffs of its 7 mutants are single-line as claimed; reran its m4 (K11 exit 1, P2 FAILED) and m7 (K12 exit 2, table+NC_P3) -- confirmed. child/report.md missing (child says tool env refused); content taken from its message. child PCP verify PASS.
Step 9: report.md written. PCP verify PASS.

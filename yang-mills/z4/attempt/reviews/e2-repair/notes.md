# notes e2-repair (T230)
step0: control.txt = 0.272341 (-ln tanh 1)
step1: pcp init done (method not found, expected). Timing: one stream 1152 burn + 1152x6 meas, see scratch
step2: REGISTRATION.md written+hashed (b094da488566cfb1...), production started N-d2 then N-d0 in background via pcp check
step3: reduce_fixed.py written (predicates F1-F3 in docstring), run on all 12 archived z1-mix6 runs (pcp K1, exit 0).
  F1 split==meta hot flag: MET for all 12 runs. Corrected hot-cold z (r1) for L-d0..L-d4: +1.21 -0.58 -0.30 -2.68 +0.66 = G4 exactly.
  Legacy (lexical) reproduces PRIOR_TABLES values -1.62 0.67 0.42 1.64 -1.14 (cold-hot). 8-stream rows: same magnitude, sign convention only.
  L-d2 r1 now FAILED (-2.68). Old Q1 = 1.0158(106) reproduces 1.016(11). Drift d0.5 r1 -2.08 (new predicate, measured on old data).
  Clear r4 raw .09201 .08599 .09281, traceless .08476 .08266 .09546 = G4.
step4: child admitted T233; child/PROMPT.txt written (control -ln tanh(1/2)=0.771937)
step5: secondary defect in reduce.py confirmed: per_stream list zips lexical data with numeric IDs (L-d2 summary per_stream[2] labelled stream 2/hot 0 carries s10 data, J1 0.0082581 = s10). Per-colour jackknife unaffected (order-free).
step6: clear_table.py (pcp K2) -> results_fixed/clear_conventions.md, C1 MET (matches G4 both conventions). min angles from meta match G4.
step7: REPLAY.md e2 section appended; reduce_new.sh written (R5 rule as registered)
step8: production N-d2 (K3) and N-d0 (K4) exit 0; child started (child-run1) in background
step9: reduce-new K5: N-d2 r1 .06269(47) r4 .04891(38); N-d0 r1 .06246(49) r4 .04733(46); hot-cold z all MET; drift N-d0 r4 +2.11 FAILED, others MET (+1.71,+0.77,+1.61); Q1 1.0036(110) indep -> R5 reproduced (also consistent with 1); Q4 1.0335(128)
step10: drift_paired.py K6 (measured only): paired D/err r1 +1.65,+1.55; r4 +0.71,+1.98; all four positive. Q1 first/second halves 1.0034/1.0039; Q4 1.0490/1.0177
step11: report.md full draft written; waiting for child
step12: child T233 returned (control 0.771937 CORRECT, graded first); released T233. Child rerun in childcheck/ (child-rerun) identical output; agrees with mine; grandchild T237 recomputed Var1(N-d0)=0.123747700718
step13: report.md final; verify PASS both

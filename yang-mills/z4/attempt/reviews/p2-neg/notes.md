# notes p2-neg
- step0: control.txt = 0.272341 (-ln tanh 1). Lean READY exists (not used). Register pcp initialised.
- step1: read ledger, a3-Acurv (report+PROOF), a4-chalcurv, a3-Avort (report+PROOF).
  curvature range: builder L3 b=4,6 [-2.2,-1.5]; b=12..48 [-2.30,-1.17]; L4 -1.60,-1.88 (b4), -1.53,-1.58 (b6); report.md row S6 says [-2.3,-1.2].
  challenger periodic: L3 b4 -1.46..-1.79; b6 -1.39..-1.96; b12 -1.12..-1.52; b24 -1.12..-1.93; b48 -1.55..-2.04; L4 b6 -1.77,-1.26; b24 -1.15,-1.67. Union [-2.30,-1.12]. Ledger: "-1.1 to -2.3".
  vortex SU(2): b1.8 F=0.69(24),-0.26(28),0.49(40); b2.4 3.06(42),1.55(45),2.81(95), L=2,3,4. Z2 b0.6 3.205,8.244,15.84(25); b0.3 0.0774,0.0041,0.0061.
- step2: read a3-Afs, a7-wild, c1-excl, a3-C (report+PROOF), MATCHED_MEASUREMENT, HYPOTHESIS_E, c1-E, GROUNDING.
  disagreements noted so far: (a) curvature range ledger -1.1..-2.3 vs builder report row [-2.3,-1.2], builder PROOF [-2.30,-1.17] and [-2.2,-1.5], challenger [-2.04,-1.12] -> union [-2.30,-1.12].
  (b) a7-wild summary paragraph says "It is negative, -1/324" while its sec.5 says rational value is a guess; ledger follows sec.5. I follow sec.5.
  (c) a3-C report tags step 4 "PROVED (numerically...)" and step 10 "PROVED (examples)"; ledger says numerically / by examples. I write "numerical" and "by explicit examples".
  (d) xi*(1-q) numbers 0.53,0.68,0.86 and xi^0.75 appear only in the ledger (director's computation); recompute in my program from MATCHED values.
- step3: child T19 admitted (parent T18), PROMPT written, child-run1 started in background 13:42:16
- step4: K1 numbers-run1 exit 1: MY defect (file numbers.py shadowed stdlib 'numbers'; ImportError before any predicate). Renamed to negnum.py (same predicates), K2.
- step5: K2 negnum-run2 exit 1: MY defect (Bessel series overflow in math.gamma at k~170); N1-N6 met before crash (result_negnum_2.txt kept). Fixed with term recurrence; K3.
- step6: K3 negnum-run3 exit 0, 14 met 0 failed. Now writing sec_negative.tex. 13:44
- step7: child control.txt = 1 (known answer 1): CORRECT, graded before reading any other child output.
- step8: wrote sec:routes (5 subsections). 13:46
- step9: appended sec:shared and sec:CE. 13:47
- step10: child-run1 = K4 exit 0 (137 s). Child report read after control graded. Child: no number absent/different. Its discrepancy #1 (c1-E L=16 label "writer's repair") is FALSE: src/c1-E.report.md:16 says "for L = 6, 8, 12, 16"; the child's own docstring pre-expected it (child's error). #2 real: c1-excl table "below 0.002" vs sec.5 "below 0.0015" -> tex now gives both. #3 MATCHED first table N=12 (160 cfgs) differs from extension values; tex uses extension. Grandchild T20 control 1.0695 correct; 9 derived values match.
  Reran child check_tables.py (K7) and grandchild recompute.py (K8) in child_rerun/: outputs identical. Released T19.
  Also fixed P2 status (Perron-Frobenius argued in a7, not cited).
- step11: added JW, Ch18 citations; K11,K12 pdflatex exit 0, 11 pages. Verified registers.
- step12: report.md written. STANDS 24, DEFECT 2, NOT CHECKED 0. 13:49

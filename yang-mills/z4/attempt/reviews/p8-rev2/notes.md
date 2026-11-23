# notes p8-rev2 (T56)
Step 0: control.txt = 0.272341 (-ln tanh 1). Register pcp initialised.
Step 1: child admitted as T57 (parent T56); child/PROMPT.txt written; child-run1 started in background via pcp check.
Delegated to child: (A) forest recursion on 3-site path, random SU(2); (B) arithmetic of C7/C8 bounds. Control: faces of a cube = 6.
Step 2 (C1). Convention sec_proof.tex:26: (U^g)_xy = g_x U_xy g_y^{-1}. Need g_y = g_x U_xy. Printed: g_y := U_yx^{-1} g_x = U_xy g_x (order reversed).
Two-site example (x root, y): g_x = 1, so g_y = U_xy under both formulas; (U^g)_xy = U_xy U_xy^{-1} = 1. Both agree on two sites with g_x=1;
 with a non-identity g_x (third site, or two sites with g_x arbitrary) old gives g_x U g_x^{-1} U^{-1} != 1 (numerically 0.97 max-entry dev, seed 1), new gives 1.2e-16.
 Downstream: sec_proof.tex:235 (holonomy from corner, g_y=g_x U_xy) already consistent; 251, 274 use the lemma only. Only line 165 changes.
Step 3: child finished (check K1 exit 0, 107 s). Control graded first: child/control.txt = 6, correct. T57 released.
 Child verdicts: A (forest recursion) STANDS for g_y=g_x U_xy (dev 6e-16), printed version fails 20/20 on second link; B1 (U(1) wrapping bound 6 exp(D-beta/16)) STANDS; B2 (exp(D - beta eta/(8K^2)), eta/K^2 from chi bound) STANDS. Grandchild T60: 70-digit check of pi/3 boundary. Strict/non-strict: pass to limit t -> beta/2 from below.
 To do: rerun child programs myself in a fresh dir before using.
Step 4: edits applied (C1 sec_proof; C2 sec_reduction/sec_proof/sec_negative; C3 sec_reduction; C4/C12 sec_reduction+provenance; C6, C11 sec_negative; C7-C10 sec_general, main, sec_negative; R2-R4 main/provenance/paperreview). Branch name 'director-g/...' removed from figure caption (commit kept). Bib keys RepoB4/RepoC4 renamed RepoPackets/RepoBlock.
Step 5: own program progs/check_rev.py: K2 exit 1 = my own defect (json.dumps of numpy ints in the final print; result file was complete, all 9 met); fixed print only, rerun K3 in runs/r2: 9 met, 0 failed.
 Reran child prog_A, prog_B, grandchild check.py in fresh dirs (K4-K6 exit 0); outputs identical to the child's reports.
Step 6: CHANGES.md and report.md written. Verdicts: 14 STANDS (several partial, see table), 0 DEFECT, 4 NOT CHECKED. Registers verified (PASS; chain intact 8 events).

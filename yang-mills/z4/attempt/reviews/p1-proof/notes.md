# notes — p1-proof (worker under T17)
Step 0: control.txt = 0.272341 written first. Register pcp initialised.
Step 1: read THEOREM_B, PROOF_B_v2, L3_L4, G4_LEMMA_R, CHALLENGE_1/2/3, STYLE_SHEET, preamble.
Re-derived by hand (in my head, written here): Lemma 1 RP partition of links; transfer matrix iteration; chessboard index map theta_a o vartheta_t = vartheta_{t'} (both parities); Lemma 3 constants incl. a (6/L) log beta term that vanishes as L->inf (file says "(9/2)log beta cancel; 1/L terms vanish" - consistent);
L3 near/far constants (lambda/16, 7); E1-E3; Lemma A induction; Lemma B gluing order + every shell plaquette lies in a face; L4 (i)-(iv); DLR steps 1-6 (simplification: paths for P_R inside the tree T = T_s u T_int so no Ad-correction needed); Lemma D sup formula; d*h=0 on ALL of Lambda'_R by gauge argument (minimiser over Lambda'' = minimiser over Lambda'_R); G4 constancy; Wick formula; G(n) asymptotics with explicit elementary bounds on |k|<=1.
No failing step found so far.
Step 2: checks.py run as K1 (exit 0): met 11, failed 0, measured only 16. Cube word identity found:
  U23(x)^-1 . [U_{x,2}] U13(x+e2)^-1 [.]^-1 . U12(x)^-1 . [U_{x,1}] U23(x+e1) [.]^-1 . U13(x) . [U_{x,3}] U12(x+e3) [.]^-1 = 1,
  signs = incidence numbers of d (P2). D* = 60.192240. Hodge Laplacian on 2-forms = scalar Laplacian componentwise (exact, (Z/4)^4).
  G(1)=0.06887475; n^2(pi^2 n^4 G - 1) ~ 6-8 for n=4..8 (consistent with O(n^-6)). Wick formula MC agrees.
Step 3: writing sec_proof.tex section by section (compilable after each block).
Step 4: Part I-II of sec_proof.tex written (setting, outline, RP, transfer, chessboard, free energy, tail); compiles; only forward refs undefined.
Step 5: Part III written (E1-E3, Lemma flat/shell, zero set, L3 theorem, L4 proposition with (a)-(e)). Cube words in (b) written out by hand and reduced by hand to the empty word (same identity as checks.py P1). Simplification vs L3_L4: P_R paths inside T so no Ad-correction in F_in; base change handled by equality of laws, so the 'Colour' paragraph of L3_L4 is not needed. Not a strengthening.
Step 6: full draft compiles (16 pp incl. dummy page), no undefined refs. Child admission attempted (see child_admit.log).
Step 7: child T25 started (child-run1) at 13:56:22 with sec_proof.tex snapshot + PROOF_B_v2.md + L3_L4.md; control: constant 7.
Step 8: own second pass: fixed wording in Lemma flat (gauge sign), shell-plaquette-in-face argument, triangle step for |alpha(AVB)-alpha(AB)|, added density argument for P in Fourier. No step found that does not follow.
Step 9: child control.txt read BEFORE any other child output: '7' (expected 7).
Step 10: attributions OS78, Lu77 added; final compile 16 pages, no errors, no undefined refs/cites. Section occupies pp.1-16 of main_test.pdf minus dummy theorem and references (~15.5 pp). Waiting for child.
Step 11: child (T25, sonnet) finished, check K2 exit 0, 239 s. Control 7 correct (graded first). Grandchild T26 control 6 correct (per child; I checked the line exists in L3_L4.md:71).
 Child flagged STRONGER-UNPROVED: (3) C_G "explicit" not given -> I replaced (4) by the fully explicit three-term bound and say the exp terms are not converted; (8) "exactly 6" unproved -> one-clause proof added; (12) limit tail bound argued in wrong direction -> text was terse, argument is via O_p -> |F|^2/2 in law + portmanteau, now written out. Row 7 (box must be symmetric) -> Lemma flat now for prod[a_i,b_i].
 Note: child read the snapshot before my wording fixes (Lemma flat sign, shell-face argument, density of P); none of its findings concern those.
Step 12: reran child's check1.py in rerun_child/ via register; T25 released.
Step 13: report.md written. Final: STANDS 14, DEFECT 0, NOT CHECKED 0; no POSSIBLE GAP.
Step 14: background waiter b525zex9u (an until-loop polling child_run1.log) was stopped at its time limit. The grep pattern 'Check K' did not match the log's 'check K2' line, so it never exited. The child had already finished (K2, exit 0) and its output was read and rerun (K3); nothing lost.
Step 15: second waiter bwrbe832x (same faulty 'Check K' pattern) was also stopped at its time limit; the child had already finished (K2) and was handled. Not restarted.

# notes p6-rev (T35)
- step 0: control.txt = 0.272341 (-ln tanh 1, python math). Lean READY exists (not used).
- step 1: fetched Clay PDF to scratchpad (outside dir); quote 'Yang–Mills Existence and Mass Gap. Prove that for any compact simple gauge group G, a non-trivial quantum Yang–Mills theory exists on R4 and has a mass gap Delta > 0.' at p.6 (printed page 6, PDF page 6).
- step 2: read REFEREE, FIDELITY, THREAD_LOCATORS, STYLE §4, all sources and src/. Backup of original sources in orig/paper_before/.
  Findings for decisions: Lemma pf:lem-rp stated for every j (D8 check: yes); pf:lem-limit(2) stated only for x_0=0, proof gives every j, every c -> extend.
  Thm S Step 6 uses RP for F_beta = sup-norm-convergent series of O_i: needs O_i continuous for restricted H0 -> add continuity to site-scalar definition.
  D7: F4-F2 = -0.20+-0.47 (beta 1.8), -0.25+-1.04 (beta 2.4) (quadrature, assuming independent runs) -- to recompute in check program.
  D7: Z2 coupling convention not stated in src (only beta_c ~ 0.44).
  D10: builder 32 = 8+8+4*3+2+2; challenger 24 = 20 (3^4, per-row not recorded) + 2 + 2. Total 56.
  D11: family from usc_test.py: nu_beta = delta_{e^-1} + max(0,beta-1)*(density 2 on [1/2,1)), spectral measure of T.
- step 3: edits batch 1-3 applied (main, sec_reduction, sec_proof, sec_negative, sec_provenance, sec_paperreview); compiles.
- step 4: CHANGES.md written; child admitted T42 (child_admit.log); child started as check child-run1 (background). Question: is each referee item / non-FAITHFUL row addressed in revised text; control: number of required changes (15); grandchild: recount 56.
- step 5: revcheck run1 (K1) exit 1: my program defect (P3 parser matched caption line). P1,P2 met before crash. Fixed parser; predicates unchanged.
- step 6: revcheck run2 (K2) exit 0: met 9, failed 0, measured 3; 45 pages; 0 overfull; 9 word hits.
- step 7: child control.txt = 15: CORRECT (graded before anything else). Child still running.
- step 8: layout fix (TOC moved after intro; theorem on p.1). child-run1 finished exit 0; T42 released.
- step 9: child report read (30 addressed, 1 partly, 2 declared not done; 3 CHANGES.md line mismatches = my defect, fixed); reran child check_items2.py as K4: identical 93/0/0.
- step 10: revcheck run3 (K5) 9/0/3; registers verified PASS; report.md finalized.

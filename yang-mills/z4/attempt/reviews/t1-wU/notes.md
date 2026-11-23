# notes t1-wU (T167)
- step0: control.txt = 0.272341. Lean READY present (not used).
- step1: read TUNNEL_THEOREM, LEMMA_F, CHAL_conditional, CHAL_lemmaF, TUNNEL_LOWER_FULL, CHAL_assembly, CHAL_parts, TUNNEL_LOWER2 §2-3.
  Corrections to apply: flux prefactor 4 (CHAL_cond item10); Taylor line in Schur (item 7); radial Lemma K line (CHAL_cond hyp list); header of Lemma F (CHAL_lemmaF); C5/L4 for lambda->1 (cite tu:L-L4); C2/C7 analog; (B) for any eigenfunction (TUNNEL_LOWER2 §3).
- step2: consts.py run1 (see consts_run1.json)
- consts run1: exit 1 = my defect (json.dumps of numpy bool in final print, after result file written; all 9 predicates met in file). run2 after fixing print.
- step3: wrote Sections 1-2 of tun_upper.tex (kernel, coords, Lemma K incl radial form, Lemma R). Added proof of K multiplier (parts only state it).
- wrapper: brief's wrapper gives 'Two \documentclass' error because style/preamble.tex contains \documentclass; wrap.tex omits it.
- step4: Section 3 (Lemma F) written; header correction applied in Cor (b).
- step5: Section 4 written (weight, Schur+Taylor, (A), (B) any eigenfunction, flux 4, main thm). Found: c*_eta vs c^rho_eta mismatch; smoothing loss L tau needs extra property.
- step6: weight lemma fixed (loss L tau per point does follow from W3). Compiles; only tu:L-L4 undefined. Starting child.
- child T170 admitted, started 22:01:12; control question 2 asinh 1 = 1.762747
- child control.txt = 1.762747: graded CORRECT (2 asinh 1 = 1.762747) before reading anything else of its output.
- child returned (K3 exit 0, 296 s). findings: 10 MATCHES, 9 CHANGED, 1 WRONG (D(1)>0.039 false: D(1)=0.03893); nits C_h direction, omega needs beta large, 0.14%.
- applied child findings: D(1)=0.0389..., C_h F_a C_h^{-1}, omega for beta large, 0.15%. child rerun K4 identical json; gc rerun K5 ratio 4. Released T170.
- step final: report.md written; verifies PASS.

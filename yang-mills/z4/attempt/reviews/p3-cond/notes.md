# notes.md (p3-cond, task T21)
- step 0: control.txt = 0.272341 (-ln tanh 1). Register pcp initialised (method not found: expected).
- step 1: read A1_REDUCTION.md (+review record), CHALLENGE_R.md, THEOREM_S.md, CHALLENGE_S.md, STYLE_SHEET.md, preamble.tex.
  Plan: proof choices that differ from source (same statements):
  * step 1 compactness: nearest-point extension + "asymptotically equicontinuous" Arzela-Ascoli instead of piecewise-linear interpolation (source's "keeps H3 up to constants" not written out there).
  * step 2: P = 4k+2, M = Dk+1, norm |f|_N = max_{|a|<=N} sup (1+|y|)^N |d^a f|; gives s = D+6 (matches source), sigma_k <= 7 alpha Gamma^k (k!)^b.
  * gap: polarized lemma on T = {f in 0S, supp in all t>0} (unordered), repaired form |B(s)| <= e^{-s} F_f(0)^{1/2} F_g(0)^{1/2}; only T self-adjoint used.
  * cluster: OS Cauchy-Schwarz reduces to compact support, then rotation + gap lemma (fills the challenger's "fillable gap" on unordered supports).
- step 2: section drafted (sec_reduction.tex), main_test compiles, 12 pages total. Child admission: ADMITTED T27
- step 3: numerics.py (K1) exit 1: N4 FAILED (own expectation: 1e-3 tolerance too tight at n<=1e4, phi=0.5 gives 3.6e-3; also phi=3.0, 6.0 are integers so trivially hit). N1,N2,N3,N5,N6,N7 met. Child T27 launched in background (child-run1).
- step 4: check_section.py (K2) 7 met 0 failed; M1 'first' counter is broken (regex double-escaped in f-string): measured-only value 0 is wrong, text contains 'first' once ('The source first stated'). Edited site-scalar sentence after K2 (child has the earlier copy).
- step 5: child T27 control 6 correct; Q1 found 'proved in full', Lu77/OS78 unread, ||T||<=1 added; fixed in text. Reran child q2b (K4) and grandchild gc (K5): identical. Released T27. Added KQR-norm sentence; final check K7 pass.

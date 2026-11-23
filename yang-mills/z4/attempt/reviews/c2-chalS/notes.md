# notes c2-chalS

## step 0
control.txt = 0.272341 (-ln tanh 1). Lean READY exists. Register pcp initialised. Task T14.

## step 1
Child admitted as T15 (parent T14), PROMPT written (A1(iii) group generation, control dim SO(4)=6), launched as child-run1 in background.

## step 2 (reading THEOREM_S, first analysis)
- E0' factorial growth: is IN H3(b) ((k!)^b explicit). Step 2 lemma (Taylor to {x_i=x_j}, M=Dk+1) gives s=D+6 fixed. Looks right.
- Step 4 group: coordinate-plane SO(2)s generate SO(4) (Givens), W4 adds det -1 -> O(4). Delegated to child T15.
- Step 8 SUSPECT: monotone inequality F(t+s) <= e^{-s}F(t) needs transfer matrix T >= 0. H0 lists SITE-plane RP only; site RP gives T self-adjoint, T^2>=0, not T>=0 (T>=0 needs link-plane RP). Counterexample spectral measure delta at lambda=-e^{-m}: F(1)<0, F(2)>0 > e^{-1}F(1). Repair: use |F(s)|<=e^{-s}F(0) (enough), or add link RP to H0 (true for Wilson, Osterwalder-Seiler).
- Step 11 (E4): vectors from non-time-ordered/equal-time supports; fillable (S continuous off coincidence) and E4 also follows from unique vacuum (step 9).
- Free field is NOT in the theorem's setting (unbounded fields); step 6 uses boundedness for L2 convergence.

## step 3: ff_check.py (register K2, exit 0)
Met Q0,Q1,Q2,Q4,Q5,Q6,Q7; FAILED Q3.
- Q1 exact gap 2asinh(m/2): rel err <=1e-15, 12/12.
- Q2 sup|x|^2 S = 1.6356, 2.0007, 2.1138, 2.1486 (m=1/4..1/32): reproduces author's 1.64,2.00,2.11,2.15.
- Q5 reproduces author's P5 numbers (3.9e-2,2.7e-2,6.7e-3 ; 3.7e-2,9.0e-3,2.2e-3).
- Q3 limit vs K1(|x|)/(|x|K1(1)): all 6 points <=2.3e-3 at m=1/32 (normalized at aN). FAILED only on the
  "decreasing" clause at x=e0, where the error is identically 0 (normalization point). Own predicate defect, not target.
- Q4 unnormalized a^-2 G vs K1/(4pi^2|x|): <=1.4e-3 at m=1/32, all 6.
- Q7: MET but UNINFORMATIVE: Wick value 5.7e-11 << MC s.e. 1.5e-6 (points too far apart). Redo with near points (ff_q7.py).

## step 4: ff_q7.py (K3) -- A6 with near points (unit square, m=1/8)
Wick T4(:phi^2:)=1.600e-5 >0; MC 1.543e-5 +- 2.1e-6 (R2 MET); phi truncated MC consistent with 0 (R3 MET);
R1 FAILED: T4/s.e.=7.6 < 20 -- my own expectation of MC precision, not a target defect. T4>0 is algebraic anyway (G>0).

## step 5: source (A1)
KQR arXiv:2104.02090 read via pdftotext (kept in scratchpad): eq (9.18) E0': exists s, |S_n(f)|<=sigma_n|f|_{n s}
for all f in 0S(R^{dn}), sigma_n<=alpha(n!)^beta; Lemma 8.8 of OS73 wrong (section 9.2.1 vicinity); footnote 20: cluster (2.24) is E4 of [2].
Same secondary source as the author; OS 1973/1975 originals NOT read by me.

## step 6: child T15
Control: 6 -- CORRECT (graded first). Verdict G=O(4) YES; proof sketch correct (Kronecker, conjugation, Lie algebra rank 6, SO(4) connected, det -1 in W4).
Grandchild T16 (admitted+released per graph): rank 6; theta=pi/2 gives 384; theta=1 >20000 elements.
Reread code; reran both in rerun_child/ under my register (K4, K5): byte-identical JSON / results. T15 released.

## step 7: t_pos.py / t_pos2.py (K6 exit 1 = my bool-indexing bug, output kept as t_pos.run1_failed.out; K7 exit 0)
AF Ising chain J=-0.5: site RP holds (T1 min eig -1e-17), transfer eigenvalue -1.042 <0, link RP fails (T4).
T2 (monotone step-8 inequality) FAILED 3 of 6 t -- this is the exhibited TARGET defect (step 8 uses T>=0, not in H0).
T3 repaired |F(t)|<=e^{-mt}F(0) MET 11/11.

## step 8
Verify: both PASS (last lines quoted in report). report.md written: 12 STANDS, 3 DEFECT, 2 NOT CHECKED. Main finding: step 8 needs T>=0 (unlisted); statement survives with repair.

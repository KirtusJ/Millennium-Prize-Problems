# f1-wild notes (T65)
- 15:5x control.txt = 0.272341 (-ln tanh 1).
- Read STATE_OF_PROGRAM, A1, A2, A3, THEOREM_B. Candidate rung chosen: single-site spatial cylinder (Z/1)^3 x Z ("1^3 cylinder"),
  Wilson action, SU(2) vs U(1). Conjecture: center-even transfer-matrix gap m_e(beta) ~ E1 beta^{-1/3} (SU(2)), via
  commutator-quartic confinement of the toron valley (Simon 1983 type discrete spectrum); U(1): exact, sector n in Z^3,
  gaps -log(I_n/I_0) ~ n^2/(2 beta); center-even (n in 2Z^3) gap ~ 2/beta. Center-odd SU(2) ~ exp(-c sqrt(beta)) (tunnelling) expected.
- Known-answer numbers (series for I_n): -log(I1/I0)(4)=see child control.
- child admitted T67, started with PROMPT.txt (control: -ln(I1(4)/I0(4)) = 0.146735, my value by Simpson N=20000).
- smoke K1 ok (22 ms/sweep R=16 T=64). Launched runA (u1 4,16; su2 8,32,128) and runB (su2 16,64,256): T=64,R=32,therm 500, meas 2000, seed beta+1000.
- K2 analyse-partial: P0 FAILED (U(1) beta=4 P: 0.154(2) vs 0.1467; beta=16 P: 0.0545(27) vs 0.0323; Q 0.1417(36) vs 0.1290).
  Diagnosis: my defect (no exact global-center move; global U(1) angle is a zero mode, local Metropolis cannot equilibrate it in 2000 sweeps).
  Fix: cyl2.py adds exact global center move; U(1) control rerun in res2/. SU(2) center-even E,Q are invariant under center,
  so the SU(2) runs of cyl.py remain usable for P1-P3, but SU(2) center-odd P is meaningless there (no tunnelling).
  SU(2) beta=16: m_e = 1.19(9) (E, t=3); Q gives 1.15-1.26.
- Child control graded: 0.146735 correct. Child U(1) beta=4: 0.14690(184), consistent with exact (child used a different sampler).
- Child K3 exit 0, report read AFTER grading control (correct). Child: U(1) b4 0.14690(184) vs 0.146735 met; SU(2) eff masses b16: 2.05,1.49,1.19,0.98;
  b64: 1.46,1.14,0.96,0.93,0.73,0.45 -- no plateau, its own 4^{1/3} consistency predicate FAILED (r=1.317(27)). My b16 E eff masses 2.07,1.47,1.19: agree.
  Grandchild T68: quadrature of -ln(I1(8)/I0(8))=0.06695692, -ln(I2(8)/I0(8))=0.26632363; my Simpson gives 0.066957, 0.266324: agree. T67 released.
- K6 U(1) fix rerun (cyl2.py): beta=4 P0 met (P 0.14632(93) vs 0.14674; Q 0.5683(20) vs 0.5652); beta=16 still FAILED (P 0.0433(9) vs 0.0323; Q 0.1356(9) vs 0.1290).
  Own defect: local Metropolis under-equilibrated at xi~31 (500+2000 sweeps); exact at xi~7. Limits trust to small xi; SU(2) xi here <= 2.
- K9 final: SU(2) m_e (Q plateau): b8 1.11(10) b16 1.19(9) b32 0.897(43) b64 0.831(40) b128 0.751(70) b256 0.526(42).
  P1 exponent 0.231 FAILED (window [0.25,0.42]); P2 met at all 6 beta; P3 2.85 vs 3.34 (15%) met. P/Q identical => no tunnelling, P4 void.

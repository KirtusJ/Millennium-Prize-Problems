# notes (r9-mag challenger)
step0: control.txt = 0.272341 (-ln tanh 1).
step1: read C4 (7 files) and A4 (3 files). Trajectory: beta/(r^16 log)->inf (m=1/ordinary), beta/(r^12 log) (m=2/symmetric); example beta=r^17. g^2=4/beta ~ b^16..b^17 -> free by construction. C4 README says "These trajectories produce a free field ... logarithmic trajectory lies outside". Gap claim is an UPPER bound r*Delta->0 (gapless).
step2: delegated C5 (A4 kappa/18) to child/ ; PCP register init.
step3: check_c4.py run 1 (results_check_c4_1.txt): numerics all within tolerance but labels P1,P3,P4,P5,P7,P8 printed MEASURED because numpy bool `is True` failed -- defect of MY program, not of C4. Fixed (bool cast), run 2 -> results_check_c4_1_n.txt. Run 1 file kept.
step4: check_c4 run 2: P1-P8 MET, M1 guessed profile within 3e-4 of C4's C0 values (my coarse grid). Maxwell covariance = C4's C0 kernel; Z4 point kernel matches at x=0 and off-axis.
step5: check_traj.py: T1,T2,T4 MET (T4: 9841/10000 random pairs qualify, 0 violations). T3 FAILED: Ward error bound along beta=r^17,L=r^4 decreases but is 0.31 at r=1e6 (>0.1). Failure = MY expectation (C4 only claims ->0); rate is ~r^{-1/8}: bound is O(1) at any realistic r. beta/beta_AF ~1e17 at r=10: free by construction.
step6: child returned; reran exact_a (exit 0), confirmed 17/64 threshold by hand; report.md completed.

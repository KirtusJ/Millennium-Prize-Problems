# notes r12-wild
step0: control.txt = 0.272341 (-ln tanh 1). Lean READY exists.
step1: read NEW_* reports, STATEMENT S6''. Candidate ONE thing: S6'' asks 0<c<=t^2<E_b(t)><=C for flowed 1/4 G.G;
 its caveat and the NEW reports substitute the spatial (in-slice) flow but compute only B3 (magnetic). Hypothesis: under spatial
 flow the electric (temporal-plaquette) part is not smoothed: its longitudinal part has a momentum-independent propagator (contact
 term), so <E> ~ b^-4 and t^2<E_b(t)> diverges. Test on free 4D lattice.
step2: started child (control: BZ average of 4 sin^2(k/2), L=64, known 2.000000).
step3: efield.py smoke L=16: P0,P_formula,P2,P3 met; P1,P4 failed (L=16 below the L=48 of the predicate; finite volume, own setup). run1 L=48 next.
step4: run1 L=48: P0 200/200, P_formula 200/200, P1 2/2 (tau^2 m = 0.006317, 0.006249 vs 1/(16pi^2)=0.006333), P2 5/5 (e=1.0111..1.0002),
 P3 met (ratio growth 16.2), P4 FAILED 0/2: measured tau^2(e+m)=0.004789,0.004642 vs my 0.0094989.
 Diagnosis: MY expectation error. sum_{mu<nu}F^2 = 2*(1/4 sum_{mu,nu}F^2), so continuum is 2*3/(128pi^2)=3/(64pi^2)=0.0047494, not 4x.
 Post hoc (measured only, not a predicate): rel dev +0.8% (tau=8), -2.3% (tau=16, finite volume as for P1). Kept as failed.
 Reading: spatial flow leaves e(tau) -> 1 per site (longitudinal contact term, exact per mode), transverse remainder ~ tau^-1.4..-1.5
 (M1: 0.00164, 0.00062, 0.00023 at tau 4,8,16). Physical: t^2<E_el> ~ t^2/b^4 -> infinity. S6'' with the slice flow fails its own normalization predicate for 1/4 G.G.
step5: child control 2.000000 graded CORRECT before reading. Child K4 exit 0, 90 s. Child L=16 numbers = my smoke numbers to all digits.
 rerun child flow.py: K3 FAILED (exit 1: flow.py reads control.txt which I had not copied; my rerun setup slip, not the child's defect); K6 rerun2 with control.txt.
 grandchild run.py rerun K5: MC 1.00326752+-0.00035587 vs exact 1.00331441 (L=8,tau=4), z=-0.13.
step6: Lean R12Slice.lean K7 exit 0, axioms propext/Classical.choice/Quot.sound, no sorry.
step7: report.md written. Verdicts: 3 STANDS... see report.

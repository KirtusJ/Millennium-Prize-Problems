# notes a1-att
- step0: control.txt = 0.272341; pcp register init done
- step1: child launched (T2), PROMPT in child/PROMPT.txt, control expected 'four'
- step2 T1 read FULL TEXT: arXiv:0707.2179v1 (Tomboulis 2007, only v1 exists), 0711.4930v1 (Ito-Seiler), 0712.2620v1 (Tomboulis reply).
  * Objected step: existence of t* with alpha(t*)=alpha+(t*) reduces to ineq (5.15) A >= A+ (Ito-Seiler (3.5)); I-S: proven only in strong coupling; (5.21) uses it.
  * Reply: (5.15) invoked only after n decimations bring upper-bound coeffs into strong-coupling region.
  * U(1): I-S Sec2: MK flow -> 0 for D<=4 abelian or nonabelian (Ito PRL 55 (1985) 558 = their Thm 2.1); claim would then give confinement for U(1), contradicted by KT-type deconfining transition. Tomboulis fn 10 (p27): for abelian, (5.15)-type inequalities follow from Griffiths; "All such known methods fail in the non-Abelian case." Tomboulis text considers Z(2) center vortex only.
  * My own reading: (5.21) applies (5.16) at xi between alpha* and alpha=1 on level-n lattice; whether all those couplings lie in strong-coupling region is the crux; reply asserts yes; I-S issue Sec 4: alpha(t)=alpha+(t) cannot exist for U(1), so some step must use non-abelian structure, and none is identified. Not resolved in literature I found.
  * INSPIRE citation query with refersto:arxiv: syntax returned unfiltered (25307 hits) -> citation search FAILED, not used.
- step3: child control.txt='4' graded PASS (known answer four)
- step4: T3-T5 read (JW FULL TEXT pp.~8-11; Chatterjee 1803.01950 FULL TEXT secs 4-5,7; abstracts 2611.11534, 2606.19362, 2503.15539, hep-lat/0002004). GitHub blocked by session proxy; ai.vixra PDFs empty (0 bytes). Quote verifier run K1: SUMMARY cases=12 P1_met=12 P2_met=12 ALL=PASS
- step5: verified child's source arXiv:0803.3019 FULL TEXT Sec 3.3 (r<1 tension; U(1) failure; implicit function theorem gap). quotes run K2: SUMMARY cases=15 P1_met=15 P2_met=15 ALL=PASS
- step6: reran child mk_recursion.py (K3) -> rows identical to child's result. Child predicate P2 (all 20 cases flow strong in d=4) FAILED: 14/20; U(1) order A beta0>=1 and order B beta0>=4 stay at c1~0.56-0.94 for 400 steps; SU(2) all flow strong (n<=32). P4: U(1) beta0=8 c1 constant 0.9387 from n=10 to 80. Controls P0,P1,P3 PASS. Tension with Ito-Seiler's quoted Thm 2.1 (D<=4, U(N) -> c_j->0) and with Ito CMP95 abstract (child: 'D less than 4' for U(1)). Unresolved: fixed line vs very slow flow vs convention. Measured only.
- step7: child report read; child pcp verify claims PASS (rerun below). Writing report.
- step8: report.md written

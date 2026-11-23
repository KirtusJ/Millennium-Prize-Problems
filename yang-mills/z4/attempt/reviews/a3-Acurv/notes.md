# notes a3-Acurv
11:39 step0: control.txt = 0.272341. Read A1_REDUCTION, LIT_RIGOROUS (facts 6-8), LIT_ATTEMPTS holes, INDEX. Lean READY exists.
11:40 step1: committed route: (c)-style horizontal Bakry-Emery on gauge-invariant functions + (b) integrated/local-to-global. Test: lambda_min(Ric+Hess V) on horizontal space on sampled SU(2) configs (4D L=3). Child: single-plaquette curvature boundary case (known answer 1-2b at Q=-1).
11:52 step2: curv_test.py written; predicates fixed in docstring; dry runs to scratch revealed heatbath unitarity drift (fixed by quaternion projection) - dry outputs not results. Launching real run L=3.
11:56 step3: result_curv_L3.txt: met 6 failed 2. T2 FAILED at bW=4,6: 0/8 samples have lam_hor>=0.5; lam_hor ~ -1.5..-2.2 on EVERY equilibrium sample, with fneg=0 at bW=6. So S6 (negative curvature only on rare configs) is refuted on L=3 (defect of the target claim, my expectation wrong). lam_hor at bW=0.5 is already -0.83 (consistent with SZZ needing bW<1/12). T1 met: one center link gives lam = 1 - 4.31 bW.
11:57 child K1 exit 0 in 148 s; child control -1.000000 CORRECT (known answer -1).
12:04 step4: child rerun K4 exit 0; my code reproduces child's lam(Q=-1)=1-2b (eigs -2b x3 shifted, 1 x9) for b=0.5,1,2,4. Child's hess.py reread: expm formula correct.
12:05 step5: result_curv_L3_large.txt (K3): lam_hor stays ~ -1.2..-2.3 at bW=12,24,48 (bounded), lam_full ~ -6.4,-9.0,-12.2 (~ -sqrt(bW)). Horizontal restriction removes the sqrt(beta) growth but an O(1) deficit remains on every sample. Caveat: short thermalization (30+4k sweeps) at large bW.
12:10 step6: PROOF.md written.
12:11 step7: L4 K5 done (T2 failed 0/2 at bW=4,6). Verifying register.
12:14 step8: report.md written. Done.

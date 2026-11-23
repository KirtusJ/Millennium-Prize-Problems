# notes i1-mc3 (T98)
- step0: control.txt = 0.272341 (-ln tanh 1). Read THREE_DIR_EXACT.md: exact m_e = 2.876117/1.621505/0.96893 at beta=1,2,4 (lowest = 2-fold E in reflection sector (000)); next level at beta=4: 1.184132 (unlabelled).
- step1: pcp register initialised. Child admitted as T100 under T98. Child launched (check child-run1) at ~17:57Z with PROMPT.txt (blind: target value not given). Child control: I_0(1)=1.266066.
- step2: wrote mc3.py (predicates in docstring); timing tests in test/ (not results).
- step3 (18:00Z): timing ok (~30 ms/sweep at T=108). Launched runA.sh (controls D3 b=1,2,4; D2 b=256) and runB.sh (D3 b=64..4096) as pcp checks, in background (2 cores).
- step4 (18:01Z): child-run1 finished (exit 0, 220 s). Graded control FIRST: child/control.txt = 1.266066 = I_0(1) (my quadrature 1.2660659): correct.
  Child claim: m_e(beta=2) = 1.620 +- 0.013 (Metropolis, T=16, 128 chains, tau=1 eff. mass) vs exact 1.621505 -> consistent (z=-0.1). Q-sum channel 1.897+-0.023 (exact next level 1.928516; tau=1 only).
  Read child mc3.py: action terms re4(a,b,c,d)=1/2Tr(a b c^-1 d^-1) match the brief's action. Grandchild T103: commutator identity, center-evenness, 4/4 met. Rerun of child pending (cores busy).
- step5 (18:02Z): wrote analyse3.py (implements PLAT/TLEN/THERM/TAU/CTRL/LIM/MONO from mc3 docstring). Waiting for runs.
- step6 (18:04Z): first look (scratch/a1.md, not a result file). beta=64 D=3: E 0.6868(26) -> m b^1/3 = 2.747(10); T2 0.7033(31) -> 2.813(13); A1 0.806(9) -> 3.225(36); plateaus met, tau_int ~1-1.5 sweeps.
  beta=1 control: pre-registered GEVP with t0=1 FAILS (signal at t>=2 is noise: m=2.88 means C(2)/C(1)~0.06 and 4x4 GEVP normalised at t0=1 is noise-dominated). CTRL "met" there only vacuously (err 2.1). This is a defect of MY analysis design for small beta (own expectation), not of the target.
  Post-hoc remedy (declared post hoc, in ctrl0.py): GEVP t0=0, L=2 plateau, same chi2/2sigma rules.
- step7 (18:06Z, scratch looks): beta=2 control via ctrl0 (t0=0): m_E = 1.6291(132) vs 1.621505 (z=+0.58) met; m_eff(t=0)=1.6218(23). A1 at beta=2: 1.935(24) ~ exact next level 1.928516 -> that level is A1. beta=1: m_eff(0)=2.8718(60), m_eff(1)=2.810(92) vs 2.876117 but ctrl0 plateau rule fails (lambda(3) noise).
  beta=256 D=3: E 0.45694(174) -> 2.901(11); T2 0.46277(105) -> 2.938(7); A1 0.5438(25) -> 3.453(16). Monotone rise toward 3.0125/3.6028 from below.
  wrote runC.sh (beta=16, 16384), to start when a core is free.
- step8 (18:08Z): beta=4 CONTROL FAILED (ctrl0, scratch/c0_b4.md): E m_eff(t) = 0.993, 0.930, 0.830, 0.664, 0.434 ... -> correlator has a constant offset:
  chains are non-ergodic along the flat valley (U_i in a common U(1), angle theta_i free). tau_int in mc3.py subtracted each chain's own mean,
  which hides exactly this. Defect of MY algorithm/diagnostic, not of the target. v1 results at beta=64/256 are therefore suspect too.
  Killed runA (during d2_b256) and runB (during d3_b1024); their checks will record non-zero exits. Writing mc3v2.py:
  + valley move: U_i(t) -> U_i(t) exp(i phi n_i(t).sigma) for all t (n_i = own axis), phi ~ U(-phimax,phimax), acceptance with Haar Jacobian prod sin^2(theta+phi)/sin^2(theta);
  + tau_int about the grand mean over chains (exposes stuck chains); new predicate ERG.
- step9 (18:12Z): REVISED DIAGNOSIS. Between-chain variance of chain means / naive = 3.4, 17, 3.4, 2.8 at beta=2,4,64,256 (=2 tau_eff): no stuck chains; v2 valley move NOT written.
  Raw E correlator at beta=4 has a constant floor ~1e-3 (1.3% of C(0)) for t>=7. The CHILD's independent Metropolis code (xcheck/, beta=4, T=16, 64 chains, 3000 sweeps)
  shows the same floor (E/C0 ~ 0.02 for t>=6). So it is the equilibrium of the periodic-T model, not a sampler bug.
  Explanation (hypothesis H-floor): the periodic-time path integral sums over ALL center sectors; in sector (100) etc. <Q1-Q2> != 0, giving a t-independent
  term sum_s w_s <O>_s^2 with w_s ~ exp(-eps_odd T). At beta=4 the center-odd gap (tunnelling along the flat valley) is small. The exact m_e is for the
  center-even sector only. Tests: (i) floor shrinks with T (beta=4, T=48); (ii) differenced correlator C(t)-C(t+1) removes the constant.
  Restarting production with unchanged mc3.py under new names (_r2), plus d2_b256_r2, beta=4 T=48, beta=16.
- step10 (scratch): diffan.py (post-hoc, differenced D(t)=C(t)-C(t+1)): beta=4 control m_E = 0.9802(110) vs 0.96893 z=+1.02 MET; beta=2 1.6283(150) met. -> H-floor supported.
  beta=4 A1 ~1.161(31) ~ exact next level 1.184. Large beta: floors <= few e-4 of C(0) (noise); differenced vs raw agree:
  b=64: E 2.741(11) vs 2.747(10), T2 2.829(11) vs 2.813(13), A1 3.231(31) vs 3.225(36); b=256: E 2.921(7) vs 2.901(11), T2 2.933(8) vs 2.938(7), A1 3.449(16) vs 3.453(16).
- step11: beta=4 floor of E op1 C(t)/C(0): 2.2% (child, T=16), 1.27% (T=24), 0.27% (T=48): exponential in T with rate ~0.065 per slice -> H-floor (center-odd sector weight e^{-eps_odd T}, eps_odd ~ 0.065 at beta=4) quantitatively supported.
  NOTE: pkill -f runA.sh/runB.sh also killed the pcp check wrappers -> runs d3_b1,b2,b4,b64,b256 have NO register record. Must rerun recorded if time allows.
- step12 (18:12Z): queued runF (child rerun b=2 + v1 control reruns into rerun/) after runE and runG (b=16384 + reruns b64,b256) after runD, via chain.sh. runC.sh deleted (superseded by runE/runG).
- step13 (18:15Z scratch): D=2 b=256 control: lowest (E) m b^1/3 = 1.9019(84) vs 1.887 z=+1.76 met (diff 1.9061(80)); E and T2 (=B1,B2 in 2D) degenerate 1.902/1.907 as O(2) requires.
  D=3 b=16: E 2.333(37) [diff 2.417(22)], T2 2.616(18), A1 2.746(41) PLAT failed. b=1024: E 2.9545(85) [diff 2.9763(80)], T2 2.9727(75) [2.9804(96)], A1 3.524(17) [3.519(16)]. tau_int 3-4 sweeps (global-mean-free estimator: per-chain mean subtracted; cross-checked by between-chain variance at b<=256).
- step14 (18:18Z): recorded analyses K4-K8 done. Pre-registered (results/analysis_prereg.md): 55 met, 16 failed. Post-hoc differenced (analysis_diff.md): 56 met, 15 failed.
  beta=4096: E 2.9916(125), T2 2.9886(131), A1 3.5443(266) (diff: 2.9919(121), 3.0010(106), 3.5795(236)). LIM met for E,T2,A1; MONO met.
  T2-E splitting in beta^-1/3 units: 0.066(14), 0.037(12), 0.018(11), -0.003(18) at 64..4096 -> shrinking toward 0.
  Extrapolations (results/extrap.md, measured only): e within ~2.3 sigma of predictions, depending on fit form.
- step15 (18:20Z): child rerun (recorded in runF) byte-identical sOO; my xc.py on it: -ln(C1/C0)=1.622, -ln(C2/C1)=1.619 at beta=2 (exact 1.621505). rerun/d3_b1.npz byte-identical to results/d3_b1.npz.
- step16 (18:23Z): beta=16384 (T=212, 3000 meas): E 2.9877(232), T2 2.9840(233), A1 3.5677(481); diff 3.0007(181), 2.9568(289), 3.5568(347). tau_int 12-16. Reruns b1,b2,b4 byte-identical (K9). Child T100 released (event 214).
- step17 (18:27Z): reruns b64,b256 byte-identical (K12). verify run.
- step18 (18:29Z): report.md written. Verdicts (control table): STANDS 5, DEFECT 1 (my method, raw beta=4), NOT CHECKED 1 (beta=1). Main 12 channel x beta rows: plateau met.

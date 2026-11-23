# notes r9-mc

Step 0 (01:50): control.txt = 0.272341 (-ln tanh 1). Inputs read. PCP register pcp initialised.

Step 1 (01:58): mc.py written (predicates M1-M3 in docstring). Smoke test in scratchpad (8^4, beta 2.3, 30 sweeps): 0.15 s/sweep incl. measurement, plaq ~0.603. Launched 7 runs on 8^4, cold start, 2 OR per HB sweep, blocks of 100 configs:
 beta 0.5 (seed 5, 100 therm+600), 2.2 (6, 200+1500), 2.5 (7, 200+4000), 2.3 (seeds 11,12, 200+4000 each), 8.0 (seeds 21,22, 200+4000 each). Each via pcp check mc_<run>.
 Child agent started (background): simple slow Creutz heat bath 4^4, plaquette at beta 2.3 and 8, in child/.

Step 2 (01:53): free.py -> results/free_v1.txt (pcp check K1, exit 0). F1 met (K1(0)=(1-L^-4)/2 exact on 8^4); F2 met (L=48 reproduces README K to <=1.7e-6); F3 met (G_48(0) within 6e-5 of 0.15493339).
 Torus L=8 kernels (zero mode removed), to be used for the 8^4 comparison: R=1 K(0..3)=0.4998779 0.0687686 0.0110993 0.0023373; R=2 K(0..3)=1.3671134 0.2621250 0.0602586 0.0179905.
 G0 for the 2x2 square: K_2(0)=1.36931 (L=48), 1.36711 (L=8). Free mean <W_2> = 1 - (3/2) G0/beta.
 Note: at n=3 the L=8 kernel differs from infinite volume by +3% (R=1) - finite volume matters already for the free reference.

Step 3 (01:56): analyze.py written (predicates P1a-e, P2, P3 in docstring, before any real analysis; one dry run on 100 configs of beta 0.5 was printed and its file deleted - it was a code test, not a result).
 Thermalization traces (cold start, therm_*.npy): plaquette settles within ~20 sweeps at all beta (e.g. beta 2.3: 0.698, 0.644, 0.625 ... mean of sweeps 150-200 = 0.604/0.602). 200 discarded sweeps (each = 1 HB + 2 OR) is ample by eye; P1e halves test checks it.
 Rate under 7-way parallel load: ~0.77 s/config on 8^4. 4000 configs would need ~50 min: too long. Decision: stop the long runs at ~02:22 by killing mc.py; blocks written so far are used. Their pcp checks will then record a non-zero exit against expected 0: this is a worker-imposed stop for the time budget, not a defect of the program.

Step 4 (02:01): interim analysis results/analysis_interim1.txt (pcp check analysis_interim1, exit 0). ALL MEASURED ONLY.
 P1a met at 2.2 (0.56922(22)), 2.3 (0.60189(26)), 2.5 (0.65255(22)); P1b met (0.12375(12) vs I2/I1 0.123718); the brief's strong-coupling form beta/4-(beta/4)^3/6 = 0.124674 is ~8 sigma off: its cubic coefficient is wrong (series of I2/I1 is beta/4 - beta^3/96). Defect of the brief, not of the target.
 P1c met at beta 8 (0.90355(3); beta^2(1-3/4b-P)=0.173(2)). P1d, P1e met.
 P2 (beta 8, R=1, n=1): C/Cfree = 1.106(20), MET (resolution 2%).
 P3 beta 2.3 interim: R=1 n=1 C/Cfree=2.29(3), rho/rho_free=6.3(1), corr/corr_free=1.74(2); R=2: 0.291(4), 9.06(12), 0.68(1).

Step 5 (02:18): long runs stopped by worker (taskkill) at ~02:17; their pcp checks K5-K9 record exit 1 vs expected 0 (worker-imposed stop, blocks already written intact; b0p5 K2 and b2p2 K4 finished with exit 0).
 Final analysis results/analysis_final.txt (pcp check K10, exit 0). Configs: 0.5:600, 2.2:1500, 2.3:5300 (2 seeds), 2.5:2700, 8:5200 (2 seeds). B=50; binning tables show plateau (errors at B=25..200 within ~20%).
 P2 MET: beta 8 R=1 C(1)/Cfree(1) = 1.121(7), resolution 0.7%. The 12% excess is resolved and is the size of an O(g^2)=O(0.5) correction.
 P3 beta 2.3 R=1: C/Cfree 2.244(8) [n=1], 4.67(32) [n=2], n=3 unresolved; rho/rho_free 6.19(2), 12.9(9); corr/corr_free 1.716(6), 3.57(25).
    R=2: C/Cfree 0.284(1), 0.391(31); rho/rho_free 8.79(5), 12.1(9); corr/corr_free 0.664(3), 0.91(7).
 Child returned no plaquette values (its runs were killed before writing). Rerunning child/su2hb.py myself, 4^4, 100+600 sweeps, beta 2.3 and 8.

Step 6 (02:20): delegation check. Child code reread (su2hb.py: plain-Python Creutz HB, quaternions, same convention as mine - written by the same model family, so not independent in convention). Rerun by me (pcp K11, K12), 4^4 cold, 100+600 sweeps, bin 20: beta 2.3 0.61162(96); beta 8 0.90384(13).
 My mc.py on 4^4, pure heat bath (NOR=0), 100+1000 (pcp K13, K14): beta 2.3 0.60845(101); beta 8 0.90385(9). -> results/L4_crosscheck_v1.txt
 Same-volume comparison: beta 2.3 diff 0.0032 = 2.3 sigma (within 3 sigma, the brief's "statistical agreement"); beta 8 diff 0.00001, 0.1 sigma.
 4^4 vs 8^4 (my code): beta 2.3 shift +0.006 (finite volume; 4^4 is a small box), beta 8 shift +0.0003 consistent with the zero-mode factor (1-L^-4) in the first-order term (+0.00037 predicted).

Step 7 (02:22): pcp verify PASS (16 events). report.md written. Counts met/failed/measured-only = 23/5/26.

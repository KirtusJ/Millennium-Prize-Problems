# notes r1-chal (T159)
- control.txt: -ln(tanh 1) = 0.272341 (written first)
- register pcp initialised; child admission: ADMITTED T162
- 21:3x child T162 admitted and launched (1D continuum splitting check, fine grid, beta 64..4096). PROMPT in child/PROMPT.txt.
- Read PATHS, E13, HARNACK, TUNNEL_LOWER2, LEMMA_F. Pen-and-paper pass (my own derivations):
  * PATHS P'c: rederived 4h(x)^2 <= n sum (dh)^2 (CS), integrate g^2 over S, domination by rho Q, int int Tgg(dh)^2 = 2E = 2Delta -> Delta >= 2 int_S f^2/(n rho). STANDS.
  * Cor B densities p_k: recomputed, STANDS (sup g^2 |S|/v^2 interior, sup g^2/v ends; 1D 1/(2r)).
  * 1D theorem steps L, M, H, S, C, P each rederived; no false line found. (L) uses non-even trial 1_I but g is the global top (Jentzsch), so variational bound applies: OK.
  * HARNACK: k_min, vol, Lemma Ch constant l(K'), phases 0-3, H4 assembly rederived; OK. lambda_ee sketch: indicator bump gives only 1-O(beta^{-1/6}) (boundary leakage sigma/delta); smooth bump gives 1-O(beta^{-1/3}); either suffices (only lambda->1 is used).
  * E13: kernel density, R R^T, cross-product remainder, G1, G2, Gaussian formula (re-derived 1D completion of square per singular direction), Err terms, tails: OK in writing.
  * Parameter mismatch: TUNNEL_LOWER2 requires r0^2/sin a_- <= eta/4 and l < r0/2; E13 (and TL2 s6) numerics use eta=0.25, r0=0.15, l=0.08: r0^2/sin a_- = 0.089 > 0.0625 and l=0.08 > r0/2=0.075. Also E13 tube starts at eta'=0.5 > a_-=0.255. Affects numerics only.
- e13_recompute run K1 FAILED (exit 1): scipy not installed (my defect, environment). Replaced by numpy Gauss-Legendre; ive checked vs asymptotic 1-3/(8b)-15/(128b^2).
- e13_recompute v2 (K2, results_e13_run2.txt): EP1 MET (logJ closed form = det/solve to 4e-15); EP3 MET (20000/20000 qualify, 0 violations, worst |F-M|/Err 0.27); EP4 MET: sup_K Delta1 = 36.93 (4096), 13.84 (16384), 0.171 (2.7e8) vs E13 36.8/13.8/0.167; EP5 MET monotone. EP2 FAILED 10/11: at beta=2.7e8 my 200-node quadrature for e^-b I1 has rel. error ~3e-9 > rho-D = 4.7e-10 (asymptotic 1-3/8b-15/128b^2 gives rho > D). Failure = my own numerical defect, not target.
- Sup of Delta1 sits at a2 = r0 = 0.15 (tube edge), a1 = pi/2, |b| ~ M: the Theta Hessian / Err_W terms.
- harnack_consts (K3): HP1-HP6 all MET: min l(K0)/d = 8.346 at d=3.645, rho=0.264; l(K_K)/d=9.085; 35 bound holds (max coeff 34.1/35); vol bound ratio>=1.38; I1 bound ratio max 0.6365; phase-0 length 0/38260 violations.
- child control graded: child wrote 4.6054; my GL-2000 value 4.6054 (see next line) -> CORRECT
- TUNNEL_THEOREM l.82 lambda_ee sketch: "1-<phi,K phi> = O(1/(beta r^2))" holds for a SMOOTH bump only; an indicator of radius r gives O(1/(sqrt(beta) r)) = beta^{-1/6}. Bump depends on (a1,a2): gauge invariant. Not sigma-even, but lambda_ee = global top (g>0 unique), so the global variational bound suffices. Only lambda -> 1 is used downstream. Verdict: sketch repairable/true, not a defect of the conclusion.
- E13 needed range: phi = max(phi_L, phi_R) with G, E sigma1-invariant => phi_L >= phi_R iff a1 <= pi/2, so (E1),(E3) are only needed on a1 in [a_-, pi/2]; E13's kink remark (pi - a_-/2) is moot for the use, and E13 with eta' = a_- covers it (the 0.1 margin in H1 is cosmetic).
- child hp.py method read: fold by sigma, conjugate by exp(-sqrt(b)Phi), Newton refinement in 300-digit Decimal, kernel cut e^-600. Running.
- oned_indep (K4, results_oned_indep_run1.txt), beta=64 N=204, my own double code via identity E(f/g): Delta = 2.073096659556e-14, child's Decimal value identical (rel 1.4e-13): OP1 MET. OP2 FAILED: plain eigenvalue difference off by 1.75% (my tolerance 1e-2 was my own wrong expectation; cancellation error ~0.73*4e-16/2e-14 ~ 1.5e-2). OP3 MET. Note: my printed -log m=31.19162 used log(we/(we-Dl)) in double (cancellation, my defect); Dl/we gives 31.1914 = child's 31.191426.
- child results so far (res_*.txt): -log m/sqrt(b): 64: 3.8985 (N=408), 256: 4.1656 (N=808), 1024: 4.3285 (N=1616); grid diffs 64: 3.5e-3 nats (204->408), 256: 2.9e-3, 1024: 2.3e-3; all < c*=4.6054, increasing.
- reran child hp.py (64,102) K5 and (256,202) K6 in rerun_child/: result files byte-identical to child's.
- child T162 returned (K7, 554 s, exit 0). Control 4.6054 graded CORRECT before reading output. Results: -log m/sqrt(b) = 3.8983 (64, Richardson), 4.1656 (256), 4.3285 (1024), 4.4296 (4096, single grid N=806); all < c*=4.6054, increasing; Q1 (-log m <= c* sqrt b + 3 log b) met 4/4; child's own P1 (grid 1e-3) failed 3/3 = its own tolerance; Q3 fit exact (3 pts) => not informative; 4-pt fit a=4.564.
- grandchild T163 (verified in graph: admitted seq 324 depth 3 parent T162, released seq 326): beta=16 unfolded double, -log m = 13.8166 (N=200), 13.8154 (N=400); its 1e-6 predicate FAILED (own tolerance; O(h^2)). Reran: identical (K8).
- T162 released (seq 328).
- report.md written. Final verify run below.

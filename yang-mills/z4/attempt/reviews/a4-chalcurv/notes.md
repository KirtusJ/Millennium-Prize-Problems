# notes a4-chalcurv
- step0: control.txt = 0.272341 (-ln tanh 1). numpy 2.5.3, no scipy. Lean READY exists (not used yet). Register pcp initialised.
- step1: child started (child-run1, FD Hessian on single plaquette and 2x2 2D lattice; control 1-2*3=-5).
- step2 (run_a1.py -> result_a1.txt, all 5 predicates PASS): own Hess V agrees with FD (2.7e-8, SU2; 1.4e-8 SU3);
  one plaquette Q=-1: B eig = 1-2beta x3, 1 x9 exactly, and the 3 negative modes are horizontal (kH=1-2beta);
  U=1 L=3: rank G = 240 (=243-3, constant-omega kernel), kH = 1; exactly 12 horizontal eigenvalues = 1 (torons: 3 colours x 4 directions);
  random config rank G = 243. SU3 at U=1 kH = 1.5, rank 640.
- step3: child graded: control -5 CORRECT. Child FD: single plaquette Q=-1 eig 1-2b x3, 1 x9 (dev 1e-6); 2x2 2D at U=1: 15 zeros, 2x6, 4x3. Reran child hess.py (rerun_child/, K3): identical. My own code on 2x2 2D: 15 zeros, 2x6, 4x3 - agrees. Child P5 was vacuous (own design defect, child said so). Grandchild: control 8 correct, Q=-1 beta=3 -> -5 x3, reran by child.
- step3b: my own heat bath had a unitarity drift (error x10 per sweep, plaquette blew up at sweep 20): own defect, fixed by quaternion re-projection (su2_proj). Recorded.
- step3c: run a2-L3p (K4) crashed: Landau-gauge relaxation had the same unitarity drift (own defect) -> gauge-fixed columns meaningless; kept as result_a2_L3p_FAILEDRUN1.txt. Its un-gauge-fixed kH values are valid: beta=0.5: -0.74..-0.85; beta=4: -1.64,-1.79. Fixed with su2_proj.
- step4 (run_a2 L=3 periodic, K5, result_a2_L3p.txt): controls C1 (beta=0.5, 0.1230 vs 0.1240) and C2 (beta=12,24,48 within 1-3/(4b)) PASS.
  kH per sample: b=4: -1.64,-1.79,-1.46,-1.62; b=6: -1.67,-1.39,-1.82,-1.96; b=12: -1.47,-1.12,-1.52,-1.22; b=24: -1.24,-1.34,-1.93,-1.12; b=48: -2.04,-2.03,-1.89,-1.55.
  => file's S6 test REPRODUCED (0/20 samples with kH>=0.5 at b>=4). kH gauge invariant (gauge-fixed copy identical).
  A3: at b>=24, exactly 3-4 negative horizontal eigenvalues, then a jump to ~5-19 (beta-scale); lowest eigvec has zero-momentum weight 0.96-0.99 in Landau gauge, IPR*nE 1.4-3 (extended) => toron / constant modes of the torus. At b=4,6 zero-mom weight 0.03-0.78 (mixed).
  beta=0.5: kH=-0.74..-0.85 (T2'' range predicate failed there: my own over-broad predicate; the file's claim is only for beta>=3).
- step5 (A6, by reasoning): S2: Bochner Gamma2 = |Hess f|^2 + B(grad f,grad f); for invariant f grad f in H_U (df kills orbit directions), so Gamma2(f) >= kH*Gamma(f) pointwise. Semigroup argument needs this only on P_t f, which stay invariant (L commutes with isometric gauge action) -> no need for the horizontal distribution to be preserved/integrable; nothing else needed for Poincare. For LSI the strong form uses Kato |Hess f|^2 >= |grad|grad f||^2 (holds for any f) - also fine. S2 STANDS as stated. (Its gap is for the Langevin generator on invariant L^2; link to transfer-matrix gap is S9/S10, not S2.)
  S4: flat configs are global minima of V so HessV>=0 there; kH=1 needs a horizontal zero mode of the curl form: on the torus there are 12 (torons; verified numerically at U=1), in an open box none, but spectrum accumulates at 0 as L grows (inf=1 in infinite volume). STANDS.
- step6 (partial, L4 open): b=4 kH -1.84,-1.67,-2.40 (localized: IPR*nE 8-27, up to 34% weight on top-1% plaquette links); b=6: +0.158, -0.325 (vs periodic L3 -1.4..-2.0).
- step6b (L4 open): b=12: kH=+2.88,+3.14,+3.21; b=24: +10.0,+9.58,+9.18 (no negative modes; grows ~beta). Interpretation: on open box curl form has a finite-size gap ~beta*p_min^2; periodic box has 12 toron zero modes. Neither is infinite volume (gapless curl form). Soft modes need L >~ sqrt(beta): at b=4,6 (L=4>sqrt b) open box is negative/near 0 again.
- step6c (L4 periodic, K7): b=6: -1.77,-1.26; b=24: -1.15,-1.67; always 4 negative modes, zero-mom weight 0.97 at b=24. No volume decrease L3->L4. Correlation kH vs maxdev: none visible at b>=12 (maxdev ~0.15-0.3 while kH ~ -1.1..-2).
- step7 (A4, K8-K10): kH -> Ric - k*c with k independent of c and of beta (beta 16..1024) to 3-4 digits: second-order (quadratic in beta*eps) shift confirmed.
  SU2 L3 periodic, white noise W: k=9.08, 8.07 (seeds 0,1), c0=Ric/k=0.11-0.12; beta*dev (action density) = 3.09*c.
  SU2 L3 periodic, G (one-loop equilibrium of non-toron modes; c=1 = equilibrium): k=2.62, 2.51; c0=0.38-0.40; kH(c=1) -> -1.62, -1.51 (matches thermalized -1.1..-2.0); beta*dev=0.82 at c=1 (equilibrium 0.75).
  => equilibrium (c=1) is ABOVE threshold c0~0.4: Ricci is outweighed by factor ~2.6. 12 negative modes, all zero-momentum (weight 0.999) = toron modes.
  SU2 L3 OPEN, W: kH ~ +beta (no soft modes, curl gap): M1 FAILED - my expectation, not target: an open small box has no near-zero modes for level repulsion to push down.
- step8 (A5, K11): SU3 L3 periodic G, 1 seed: k=3.42, c0=Ric/k=0.44 (SU2: 0.38-0.40); kH(c=1)=-1.92, (kH-Ric)/Ric=-2.28 (SU2 -2.51..-2.62). Relative deficit slightly smaller for SU3, still far below 0. 32 toron zero modes (8x4). measured only.
- step9: report.md written. Verdicts: STANDS 6, DEFECT 1, NOT CHECKED 1, measured-only 2 (A3 partial, A5).

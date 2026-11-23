# r5-chal notes (challenger of Z4 STATEMENT S1,S2,S4,S6)
Step 0: control.txt = 0.272341 (-ln tanh 1).
Step 1: read STATEMENT.md and input/a4/*.md. PCP register pcp initialised.
Step 2: wrote powers.py with predicates P1-P9, M1 fixed in docstring before first run. Delegated C(t) powers to child (background).
Step 3: powers.py run (exit 1, expected 0). result_powers.json. Passed P1,P3,P4,P6,P7,P8,P9. Failed:
 - P5: C(t)t^5/[int f^2/(50pi^2)] = 5.000 exactly, exponent 5.0000007. OWN arithmetic error: correct
   momentum constant is 2*(1/(8pi^3))(1/4)(32pi/15)(24/(2t)^5) = 1/(10 pi^2). Real-space agrees to 1e-6.
 - P2: C/(Lam^5 int f^2) = 0.957 (w=1), 0.938 (w=0.7) of 2/(75pi^2). OWN tolerance error: sharp cutoff on
   both propagators gives a NONLOCAL Lam^4 term, relative -1.25 <|p|>/Lam (<|p|>=2/sqrt(pi)/w) -> -4.4%, -6.3%
   predicted vs -4.3%, -6.2% seen. Leading power 5 and int f^2 proportionality not affected.
 M1 lattice: C_b(0) b^5 = 8.04, 8.09, 8.11 (N=24,48,96): b^-5 confirmed on the lattice.
   C_b(0.5) rel. error vs continuum 0.36, 0.39, 0.07 at b=0.5,0.25,0.125: preasymptotic, O(b^2) not seen yet.
Step 4: powers2.py (exit 0): Q1 C(t)t^5/(int f^2/(10pi^2)) = 0.99999983; Q2 sharp-cutoff deviation / derived
 nonlocal Lam^4 term = 0.970-0.979 in all 4 cases. 
Step 5 (analysis, no program): S6(a) 1/2 Tr U_p = cos(g b^2 |F|/2) = 1 - g^2 b^4 |F|^2/8 -> Z ~ 1/(g^2 b^4) ok.
 S6(b) B^2 alone = combination of scalar F^2 and T_00 -> two renormalisations, not one Z. S6(c) A4 locations:
 hamiltonian-variance.md l.15-21, l.59 (v*^-1 = O(g), M*/v* = O(kappa sqrt g) UPPER bound); spatial-limit.md l.3 and
 action-curvature.md l.65 (g = beta^2/2); action-curvature.md l.3, l.65 (order 1/b, zero-momentum sum, coupling-averaged);
 refinement.md l.13 (V_p <= 8u, g u <= 5 sqrt g/2 -> V_p = O(1/beta) upper).
Step 6: child interim (child/notes.md): derived G(x,t)=(t^2+x3^2-x1^2-x2^2)/(pi^2 u^3) [same as mine], p0=5, A0=1/(10 sqrt pi), pinf=8, Ainf=16/pi -- agree with my Q1/P6 constants. Child numerical runs corr/mc still running.
Step 7: reran child mc_check (PASS, 1.41/0.34 sigma). Child corr.py not awaited (over budget). PCP verify: PASS. report.md written.

# notes i1-tunnel (T101)
step0: control.txt = 0.272341. Register pcp initialised. mpmath/gmpy2 NOT installed -> own double-double code needed.
step1: child T102 admitted, child-run1 started in background (derivation (i),(ii) independent). control for child: int_0^pi 2 sqrt(sin a) da
step2 (derivation, mine):
 (i) 1D discrete oscillator, normalised kernel sqrt(b/2pi)exp(-b(x-y)^2/2), e^{-V/2} each side, V=w x^2, w=2 b s^2:
   Z_n=Tr T^n = prod_k (2cosh e - 2cos th_k)^{-1/2} with cosh e = 1 + w/b = 1+2 s^2  => Lambda_m = exp(-(m+1/2)e) exactly.
   Two transverse dims: ground energy e = arccosh(1+2 sin^2 a) = 2 asinh(sin a). CONFIRMED (T4 numeric).
   Neglected: group kernel vs Gaussian (Tr U = 2cos|x| -> |x|^4 terms, O(1/beta) relative), sin^2 a2 vs a2^2 in V (O(1/beta)),
   Born-Oppenheimer coupling (O(1) in exponent), and the assumption that the optimal path lies on a2=0 (not proved).
 (ii) Gaussian step: int exp(-b u^2/2 + sqrt(b) S' u) = exp(S'^2/2) exactly for linear S; S'' term O(beta^{-1/2}).
   => eps(a) - S'^2/2 = E exactly at leading order in discrete time (no correction). Haar sin^2 a (3D radial) enters as
   psi = phi/sin a: O(1) / prefactor (log beta) effect only. Leading c = 4.6054132 stands.
 (iii) eps ~ 2a at ends (linear turning point): int sqrt(2(eps-E)) - sqrt(2 eps) -> -E int da/sqrt(2eps) CONVERGES
   (the brief's "diverges" is wrong for linear eps); region a~beta^{-1/3} contributes O(1). With E=E0 beta^{-1/3}, E0=3.3505330:
   PREDICTION: -log m_eo = 4.605413 sqrt(beta) - 8.9888 beta^{1/6} + p log beta + b + o(1), d=int da/sqrt(2eps)=2.682799.
   Check vs beta=64: 36.843-17.978=18.87 vs measured 23.13 -> b+p log64 ~ 4.3 (plausible O(1)).
 theory.py run K2: T3 FAILED (Simpson n=2000 vs 4000 differ >1e-8): own tolerance expectation (see diff above); c, T1,T2,T4 met.
step3: dd.py + ddmeas.py (double Lanczos Ritz vector, dd Rayleigh quotient). Dev runs (scratch/): beta=8,16,32,64 reproduce
 1.4768e-02, 3.2111e-04, 7.6936e-07, 8.9923e-11 (m_oo 3.0464e-02, 6.4260e-04, 1.5387e-06, 1.7985e-10). beta=64 N48->56 rel change 3e-8.
 Child control (int_0^pi 2 sqrt(sin a)) = 4.792561: CORRECT (graded before reading the rest).
 Recorded sweep run_dd.sh started (beta 8..256, two N each).
step4: child report read. (i): eps_tot = 2 asinh(sin a) = arccosh(1+2 sin^2 a) exact, independent of beta -- AGREES with mine.
 (ii): S'^2/2 = eps - E exact for Gaussian step, Haar factor only prefactor -- AGREES. Child treated E as O(1/sqrt beta) and
 dropped it: that came from MY prompt wording (eigenvalue e^{-E/sqrt beta}); the true vacuum energy per step is E0 beta^{-1/3}, so
 my beta^{1/6} term stands; not a contradiction of the child's algebra. Grandchild T104: 1D eigenvalue 0.4142135624 at beta=50,a=pi/2.
 Reran child/check.py in scratch/childrerun (needed control.txt copied; first attempt failed for that reason): output IDENTICAL.
 T102 released.
step5: dd_sweep (K3) done. Controls beta=8..64 all met. NC met at 64 (3e-8), 96 (9e-7), 128 (2e-4); FAILED at 192 (N84->92: 20%)
 and 256 (N96->104: factor 180): truncation N too small (own expectation N~6 sqrt(beta) wrong). Not a target defect.
 m_eo(96)=6.8644e-14, m_eo(128)=1.4597e-16 (both NC met). m_oo/m_eo = 2.00000.
 Started dd_sweep2: beta 192 N100,108; beta 256 N120,132.
step6: dd_sweep2 (K4, exit 1). 192: N100->108 rel 6.1e-7, m_eo=4.1266e-21. 256: N120->132 rel 2.7e-6 (oo 8.2e-5), m_eo=5.4032e-25;
 E predicate FAILED at 256 N120/132 (bound res^2/gap = 9e-28 > 1e-3 m): 3rd digit not guaranteed by the bound (NC says 2.7e-6).
 D2 (Miller start S vs S+60 to 1e-29) FAILED at 192 N100,N108: 1e-16 rel. Own defect (rescaling pushes dd lo parts subnormal). NC still met.
 analyse2 (K5): fits restricted to beta<=128. analyse3 (K6) includes 192,256: c free with beta^{1/6}: 4.6156/4.6040/4.5994 (beta>=32/64/96);
 log form: 4.42-4.44; c=4.7926 fixed needs q~-16, p~2 drifting, residual 5x larger. Prediction q=-8.99 vs fit q=-7.8..-8.1.
step7: report.md written. Registers verified (PASS).

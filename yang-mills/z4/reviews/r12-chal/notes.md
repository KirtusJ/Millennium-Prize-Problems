# notes r12-chal
- control.txt = 0.272341 (-ln tanh 1). Lean READY exists.
- child started for A4 (theta bounds).
- Step 1 (paper check, before coding): read THEOREMS_B, PROOF_FREE_BOUNDS, SETTING, TESTFN.
  * H1 normalization quick rederivation: mass b/g^2, omega=khat, <|A_pol|^2>=g^2/(2b khat), sum_pol (khat x eps)_3^2 = khat1^2+khat2^2 -> <B3 B3>(k) = P33 khat/(2 b^3); D = l^-3 sum ... P33 khat/2. Agrees.
  * Parseval: sum_{q in BZ}|fhat_b|^2 = b^6 N^3 sum f^2 = l^3 b^3 sum f^2. Agrees. k'->k+k' mod BZ bijection, fhat_b 2pi/b periodic: Schur row sum ok.
  * a^2 <= (|k|^2/4)e^{-16 s|k|^2/pi^2}; with k=2pi n/l: (pi^2/l^2)|n|^2 e^{-64 s|n|^2/l^2}. V formula agrees. Dimension: C ~ L^-2, V ~ L^-3 * L^3 * L^-2 OK.
  * U2 leading (3/2)pi^{3/2}c^{-5/2}; V lead = 2 Phi (3/2) pi^{7/2}/32768 s^{-5/2}: agrees, l-free only if Phi is l-free (Phi = l^3 sup f^2 option is not).
  * A8 paper: int D^2 = (1/(2pi)^3)(8/15)(1/4) 4pi (3/8)sqrt(pi)(4s)^{-5/2} = sqrt(pi)/(1280 pi^2) s^{-5/2}; C -> 2 int f^2 * that = sqrt(pi)/(640pi^2) int f^2 s^{-5/2}. Agrees.
  * Loss factor: V_lead/C_lead = 1920 pi^5/32768 * Phi/int f^2 = 17.93 * Phi/int f^2 = (pi/2)^5*(15/8)*Phi/int f^2. Agrees (needs Phi/intf^2 = 3.3 numerically).
  * B3: M1 = 2 sum F (a khat)(a'), weighted AM-GM -> (4/l^3)Phi sqrt(A0A2); M2: (khat+khat')^2 -> 2 sum F (a khat^2) a' + 2 sum F (a khat)(a' khat') -> (4/l^3)Phi(sqrt(A0A4)+A2). Agrees.
  * DEFECT (minor, text): "with v1 alone ... scale only like s^-3 and s^-4": M2 bound ~ sqrt(A0A4)+A2 ~ s^{-7/2}, v1 ~ const, so M2/M0 bound ~ s^{-7/2}, not s^{-4}.
  * B2 step 2: |grad g| for g=(p1^2+p2^2)/(2|p|) = sqrt(sin^4/4 + sin^2 cos^2) <= 1/sqrt3; claimed 3/2 is valid but loose. Segment: componentwise same sign, |p_i| in [(2/pi)|k_i|,|k_i|] -> |p| in [(2/pi)|k|,|k|]. OK.
  * B2 step 4: |k_i+k'_i| b > pi => max(|k_i|,|k'_i|) > pi/(2b). abar = abar* e^{-4s|k|^2/pi^2} <= abar* e^{-4s (pi/2b)^2/pi^2} = abar* e^{-s/b^2}. OK. Continuum tail coefficient 2 int f^2 is more than needed (int f^2 suffices).
- Step 2: wrote chal.py (predicates P1-P16 in docstring), running run1.
- run1 (K2): crashed in B2 loop after l=0.7,s=0.002; P11 FAILED = my own defect (sampled k_i b in (-2pi,2pi] instead of (-pi,pi]). All other predicates up to there met. results_run1.json is empty/partial (kept).
- fix after run1: C_cont index bound (h=min(NF/2-1,L/2-1)); P11 sampling k_i b = y in (-pi,pi]. Predicates unchanged.
- run2 (K3): all predicates met except P11 (float64 cancellation at k b<2e-4: my tolerance, not target); p11b (K4) failed to start: no mpmath (my defect); p11c (K5) Decimal 50 digits: 0 violations, max ratio 0.999999999998.
- child: control 1.086435 graded CORRECT before reading rest. Child report: T1,T2,T3 STAND. Reran main_test.py in child_rerun (K6): same counts, worst ratios identical to my P10 to 15 digits. Child's main_test writes no mode-x result file (rule 3 not followed by child). Grandchild numbers theta_1(0.3)=5.393405312651, theta_2(0.01)=132934.0388179 recomputed by me: match.

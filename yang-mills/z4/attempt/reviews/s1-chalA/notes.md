# notes.md -- worker s1-chalA (T164)
## Step 0 (control)
control.txt = 0.272341 (= -ln tanh 1). Lean READY file exists (Lean not planned to be used).
Pre-existing in dir (NOT mine, from r1-asm T158): asm_check.py, onedflux.py, admit.log, started.txt, task_id.txt. I do not reuse them as my evidence.
Check: c* = int_0^pi sqrt(2*2 asinh(sin a)) da computed by quad (see step 1).
## Step 1
c* (1D: int_0^pi sqrt(4 asinh sin a)) = 4.6054132 by 2e6-pt midpoint: matches target's c*.
Register pcp initialised. Child admitted T165 (parent T164). child/PROMPT.txt written (statement+defs only, control = int x^2 e^x = e-2 = 0.718282). Child started in background (child-run1).
## Step 2 (reading; assembly checks by hand)
- (a) factor c*: phi = max(phi_L, phi_R); Omega = supp phi ∩ {a1 in [a-, pi-a-]} contains the middle a1=pi/2 in its INTERIOR (no cut there). Lemma C applied once on the whole Omega (both halves). Tent value at middle = mu e^{-sqrt(b) Psi(pi/2)}; subsolution at x with a1<=pi/2 uses only phi_L (monotone, smooth through pi/2): T phi >= T phi_L >= lam phi_L = lam phi. Same device as PATHS §3(S) (Psi=min(Psi0(y),Psi0(pi-y))) and TUNNEL_LOWER Lemma S. Chain crosses pi/2 inside Omega where phi >= (mu/4)e^{-1.5rho_B^2} e^{-sqrt(b)Psi(pi/2)}. -> STANDS.
- (b) Lemma C as proved (TUNNEL_LOWER §1, PATHS §3(C)): Omega, phi>=0, ||T_OO||<lam, T phi>=lam phi on Omega, phi<=g on Omega^c. 'Entrance set' = R_well ⊂ Omega^c; mu placed inside phi. Neumann series positivity valid for nonlocal positive kernel. ||T_OO|| bound uses only Omega ⊂ {a1 in [a-,pi-a-]} -> unchanged by C1-C7 (Lemma F uniform in s∈[eta/2,1], LEMMA_F §3). STANDS.
- L4: checked line by line: sector membership of u (sigma1 odd, sigma2 even, gauge inv), 8 ordered cross terms, V<=2 b r^4 on B_r^2, triangle inequality bound. STANDS (o(1) only; P2 of asm_check shows L_beta=0.75 at 1e16).
- Chain: valley segment e^{t n} t: a -> a-pi ends at -U1^0, class angle monotone after 0; step 3 = sigma1(reverse step1). Valley balls: q<=|u2|^2<=rho_B^2/b, a2<=rho_B/sqrt b<r0 -> in supp phi; min(Psi(a1),Psi(pi-a1))<=Psi(pi/2) for all a1. Corners at U2=-1: via sigma2 (g sigma2-even; phi=0 there but g(z)=g(sigma2 z)). STANDS.
## Step 3: assembly1d.py written (predicates Q1-Q8 in docstring before first run)
Run K2 (beta 16,36, eta .25): Q1 2/2, Q2 2/2, Q3 2/2, Q4 0/2 FAILED (min T phi/(lam phi)=0.914,0.919 at d~a_-: ramp region, finite beta, my expectation), Q6 2/2, Q7 2/2.
Runs K3 (eta .25) / K4 (eta .1), beta 256,1024,4096:
 eta .25: E_true 4.178/4.332/4.431; E_LB 5.660/5.361/5.196 (gap 1.48/1.03/0.77, shrinking); 2Psi(pi/2)=4.808 (c*(.25)=5.166); monotone reading 9.55-9.61 (~2c*); Q2-Q7 all 3/3 met; Q8 met. Tphi/(lam phi) min 1.025/1.193/1.279 at d~a_-.
 eta .1: E_LB 5.515/5.189/5.012; 2Psi(pi/2)=4.756; Q4 FAILED at beta=256 (0.959 at d=0.104=a_-: ramp region; my finite-beta expectation, not target), met at 1024, 4096 -> Q4 2/3, Q5 2/2 (asserted only where Q3,Q4 hold), Q6 3/3, Q7 3/3, Q8 met.
 => assembled 1D bound is below truth and its exponent tends to 2Psi(pi/2)(eta) <= c*(eta), not 2c*.
## Step 4 (child)
Child T165 control 0.718282 = e-2: CORRECT (graded before reading output). Child -log Delta/sqrt b = 3.9376/4.1780/4.3324/4.4307 (b=64..4096), (log g0 - log g(pi/2))/sqrt b = 1.926/2.064/2.152/2.207 -> c*/2=2.303 from below. Rerun K5: results.json identical. Agrees with my independent assembly1d.py to ~1e-4. Grandchild T166 (admitted seq 333 parent T165, released) : c*=4.605413195, beta=16 -logD/sqrtb 3.5765; its 1e-6 grid predicate FAILED (own expectation, O(h^2)). T165 released (event 334).
Grandchild rerun K6: N=256 line identical; N=512 Delta differs at rel 9e-10 (plain-double eigenvalue subtraction, cancellation eps/(Delta/lam)~2e-10 scale): consistent, not bit-identical.
## Step 5: report.md written; registers verified (PASS).

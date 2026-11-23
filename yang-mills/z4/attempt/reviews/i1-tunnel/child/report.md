# T102 report (i1-tunnel)

Control (control.txt): 4.792561 (= 2 sqrt(pi) Gamma(3/4)/Gamma(5/4); midpoint quadrature 4.7925609 agrees).

## (i) Frozen U1, transverse oscillator — VERDICT: yes, exact
w = beta s^2, s = sin a. Ansatz psi = exp(-c x^2/2). One application of T: Gaussian convolution gives
sqrt(beta/(beta+p)) exp(-(beta p/(beta+p)) x^2/2) with p = 2w + c, then times exp(-w x^2):
c' = 2w + beta p/(beta+p). Fixed point c = 2 sqrt(w(w+beta)), and
  Lambda(a) = sqrt(beta)/(sqrt(w)+sqrt(w+beta)) = 1/(s + sqrt(1+s^2)).
So eps_1D = -log Lambda = arcsinh(sin a), independent of beta (exact for the Gaussian operator; the Gaussian is the
top eigenfunction since the operator is positive and the Gaussian is positive). Two transverse dims:
eps_tot = 2 arcsinh(sin a) = arccosh(1 + 2 sin^2 a) exactly (cosh 2u = 1 + 2 sinh^2 u). The third (longitudinal) dimension has eigenvalue 1.
Small s: eps_tot ~ 2 sin a, the "control" integrand; at a = pi/2 eps_tot = 1.7627 vs 2.
Numerics (check.py, grid h = 0.1/sqrt(beta) and 0.2/sqrt(beta)): beta=50 a=pi/2: 0.4142135623730967 vs 0.4142135623730951 (rel 4e-15);
beta=50 a=0.3: 0.74723201344906 vs 0.747232013449057 (rel 4e-15); beta=200 a=pi/2 same as beta=50 (beta-independent).
Neglected: curvature of SU(2) (relative O(1/beta) corrections to kernel and V: V = 2 beta sin^2 a1 sin^2 a2 sin^2 gamma with sin a2 = |x| - |x|^3/6...),
kernel normalisation of the compact group (Gaussian vs exp(beta cos theta), O(1/beta) in exponent), non-adiabatic coupling to U1 motion.

## (ii) Slow motion along the valley — VERDICT: S'^2/2 = eps(a) − E at leading order, with E dropping out
Step: psi(b)=exp(-sqrt(beta) S(b)), b = a + z/sqrt(beta). Gaussian average:
 ∫ sqrt(beta/2pi) e^{-beta u^2/2} e^{-sqrt(beta)[S(a)+S'u+S''u^2/2]} du = e^{-sqrt(beta)S(a)} e^{S'^2/2} (1 + O(1/sqrt(beta))).
The tilt identity is exact for a Gaussian step (checked, rel 1e-11 at beta=50, S'=1.7): there is NO sinh/cosh correction; discrete time with a Gaussian step gives exp(S'^2/2), the same as diffusion.
Orders in beta: S' term O(1); S'' term O(1/sqrt(beta)); Haar ratio sin^2(a+u)/sin^2 a = exp(2 cot a · z/sqrt(beta)+...) is O(1/sqrt(beta)) — it changes the prefactor (psi ∝ 1/sin a type), not the eikonal. The split exp(-eps/2)..exp(-eps/2) equals exp(-eps(a)) up to O(1/sqrt(beta)) as eps varies on scale 1.
Eigenvalue condition: exp(-eps(a)) exp(S'^2/2) = e^{-E_tot}, with E_tot = E/sqrt(beta) -> 0, so
  S'^2/2 = eps(a) − E_tot   (E_tot is small, O(1/sqrt(beta)), only fixes the turning points/prefactor; if the lowest eigenvalue were O(1) away from 1 it would enter as sqrt(2(eps−E)).)
Exactness check: for constant eps the function exp(-k a), k = sqrt(2 beta eps), is an exact eigenfunction with eigenvalue 1 of exp(-eps/2) G exp(-eps/2) (residual 4e-16).
Hence S' = sqrt(2 eps_tot) and the exponent is c sqrt(beta) with
  c = ∫_0^pi sqrt(2 eps_tot) da = 2 ∫_0^pi sqrt(arcsinh(sin a)) da = 4.605413 (numerical, midpoint N=4e6).
Replacement relative to the control: the control integral 4.792561 uses eps = 2 sin a, which is only the small-sin a limit; the correct eps_tot gives 4.605413 (ratio 0.9610). So "c = ∫ sqrt(2 eps)" is right in form, but eps must be 2 arcsinh(sin a) (not 2 sin a, not the lattice arccosh-type dispersion).
Caveats: the subsequent identification of "-log(splitting)" with the full-path action a=0 -> pi is an assumption I took from the task, not verified (what sets the splitting, whether a=0 and a=pi are distinct wells, nonadiabatic/Berry corrections and prefactor are O(1) in the exponent and not computed). Near a ≲ beta^{-1/2} the frozen-U1 eps is invalid; contribution to c is O(beta^{-3/4}) since eps~2a there.

## Predicates
P1 control quadrature: pass. P2 grid vs formula (2 cases, tol 1e-9): pass, beta-indep pass. P3 identity on 1000 a-points tol 1e-9: 1000/1000 qualify (also 200/200 on [1e-4,0.05]); max diff 9e-16. P4 tilt identity and exact-eigenfunction: pass.
Failed predicates: none. (My expectation that arccosh would lose precision at small a did not materialise at the tested points, max 2.7e-13.)

## Not checked
Full 2-link (U1,U2 on SU(2)) numerics; true double-well splitting numerics; Haar-factor effect numerically (analytic only); non-adiabatic corrections; finite-beta compact-group kernel.

## Grandchild
Admitted as T104 (task-admit, --parent T102), released after return. Question: independent numerical largest eigenvalue of the 1D operator at beta=50,a=pi/2 (plus a=0.3, beta=200). Its control passed (4.792561). It returned 0.4142135624, 0.7472320134, 0.4142135624; convergence under halving 1e-16; rel diff to formula 3.6e-14. I reread eig.py, reran it in rerun/ (pcp check K2, exit 0): output identical to its result.txt. Agrees with my own check.py.

## Rerun
cd child; python3 -I check.py  (writes check_result.txt, mode 'x': delete it first); cd rerun; python3 -I eig.py

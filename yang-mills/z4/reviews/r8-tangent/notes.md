# r8-tangent notes (challenger, Director C4 tangent-curvature)

## Step 1 control
control.txt = 0.272341 ( -ln tanh 1 = 0.2723414..., python math).

## Step 2 read C4
- Convention (wilson-law.md): SU(2) as unit quaternions, x_p = Re U_p = tr U_p /2, weight exp[-beta(1-x_p)]; = standard (beta/2)Re Tr(1-U), beta=4/g^2.
- Limit (README, wilson-law.md): N->inf first at fixed beta,L (transfer vacuum), then beta,L -> inf jointly, any rates. Cells fixed in lattice units. No b->0 in the Gaussian theorem. L >= 3 spatial periodic.
- Limit law (gaussian.md + reflection.md): rooted F_p = sqrt(beta) Im U_p -> centred Gaussian, cov = orthogonal projection P onto closure of exact 2-cochains on Z^4, 3 indep colours; first only up to independent constant 2-form H, H=0 by site-reflection odd test.
- Single face: N(0, I_3/2); Y_p = beta(1-x_p) -> chi2_3/4, mean 3/4, var 3/8; all moments (moments.md, exp moment uniform in L).
- C4 numbers: C1(0)=0.5, C1(1)=0.06887475 (spatial face, one step in time), edge test var 6, (1+12s)^{-3/2}.
- PCP register pcp initialised (method not pinned, expected).
## Step 3 delegation
Sub-agent launched on child/: control G4(0)=0.15493339; equipartition; free propagator numbers (diag, parallel e3, coplanar, perpendicular, 3e3; L=8,16, inf vol); Y mean/var.

## Step 4 own program free_curv.py (run1, PCP K1, exit 1)
- P0 FAILED: control G(0)=0.3194 — DEFECT OF MY PROGRAM (wrote 1/(4-2Σcos) not 1/(8-2Σcos)). Fixed in control_g0.py (K2): Richardson 0.15493347, met.
- P1..P8 met: P(k) idempotent rank 3; torus diag = (1-L^-4)/2 exact (L=4,8,16); inf vol diag 0.50000000 (equipartition 2/d);
  cov(th12(0),th12(e4)) = 0.06887475 = C4's C1(1); edge variance 6.000000; reflection sign 60/60 cases <=0;
  dipole C(0)=0.86225051 = 2(diag-par); Y mean 3/4 var 3/8, C4 moment formula = chi2_3/4 moments.
- measured: parallel e3 0.06887475, 3e3 0.00226224, coplanar e1 -0.06887475, perpendicular 0.10778131; L=16 torus values within 2e-5.
## Step 5 child rerun (K3): child/main.py rerun in rerun_child/, results identical; all its P1-P6 pass; numbers agree with mine to 8 digits.
  child control first run off by 8.3e-7 (its bug, kept), v2 0.154933390.

## Step 6 report.md written; PCP verify PASS. Verdicts 9 STANDS / 0 DEFECT / 3 NOT CHECKED.

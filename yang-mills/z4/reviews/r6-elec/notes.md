# Z4 worker r6-elec — challenger notes on D4 electric-scale
## Step 0: control
control.txt = 0.272341 (-ln tanh 1).
## Step 1: read input/ (6 files). PCP register pcp initialised.
Convention found: shells.md uses g=lambda/kappa with H = (kappa/4) sum(-Delta_{S^3}) + lambda sum(1-x_p), -Delta eigenvalue n(n+2), n=2j.
class-probes.md: kappa = 2/(beta b), lambda = beta/b => g = beta^2/2; kinetic coefficient kappa/4 = 1/(2 beta b) = 1/(2 kappa_B) with program kappa_B = beta b.
So D4's "kappa" is NOT the program's kappa_B: kappa_D4 = 2/kappa_B. g = beta^2/2 matches A4 convention. dimension.md uses a = kappa/4, g_G = 4g = 2 beta^2 (metric convention).
## Step 2: delegated E1 rotor slopes to child/ (control 1.0 correct). Child: 9/9 predicates PASS, slopes N90 .256, N99 .261, Dim90 .724, Dim99 .747, S_tw .759. Child verify PASS.
## Step 3: own program check_e1e3.py (continuum quantiles, E0, Dim/g^.75, S_tw, E3 identity, Jensen floor, clocks). met 9, failed 1 (P1: absolute 1e-10 truncation tol; |dE0|=2.7e-10 at g=1e6, rel 1e-13 -> my expectation, eigh roundoff scales with ||H||~g; not a target defect). P2 met narrowly (0.0196 < 0.02).
## Step 4: reran child rotor.py in rerun_child/ under my register: identical slopes, 9 PASS.
## Step 5: text analysis E2-E5 (see report.md). Key: both clocks vanish in physical time; class-probe floor is at energies ~1/b; center 'fixed physical time' needs beta->inf (u->0), marked set fixed in LATTICE units, box-uniform; for fixed physical region K~2^(links) and K u -> 0 fails.

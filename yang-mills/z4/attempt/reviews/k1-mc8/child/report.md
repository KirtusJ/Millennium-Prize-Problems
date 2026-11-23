# T118 report: E-channel mass, 1-site SU(2), beta=64, T=34
**Result: NO VALID MASS. No plateau found; m, its error and m*beta^(1/3) are not reported.**

- Control: integral of x^x on [0,1] = 0.783431 (control.txt).
- tau_int (Madras-Sokal, c=6, chain-mean): 135 sweeps for corr(tau=1) (median 85, max 298); 141 for <s>. Run was 3000 sweeps/chain after 3000 burn-in, so NS/tau ~ 21 < 50.
- Predicates (mc.py docstring, fixed before first run):
  - P1 acceptance 0.47 at eps=0.06 (tune), 0.556 in the run: met.
  - P2 thermalisation: z=2.45 (<3) met, but <s> drifts 0.149 -> 0.114 between halves, so thermalisation is doubtful. The test is weak against slow drift.
  - P3 tau_int rule (NS >= 50 tau): FAILED (my expectation of the tau was too optimistic; the target has flat abelian directions, so Metropolis with small steps is slow).
  - P4 32 chains, jackknife over chains: met.
  - P5 plateau: FAILED. m_eff goes -0.36, -0.18, -0.04, 0.08, 0.19, 0.31, 0.50, ... smoothly increasing, no flat region. D(t) turns negative at t>=9, so D is not a single decaying exponential. Likely cause is thermalisation/statistics (P2/P3 doubtful) combined with the periodic-T cosh form, which the specified ln(D(t)/D(t+1)) ignores.
  - P6: the grandchild checked a Kennedy-Pendleton heat bath, not my Metropolis sampler. My main run used Metropolis only (no heat bath/overrelaxation), so P6 does not validate the code that produced the numbers.
- Tolerances: 3 sigma (P2) and 50 tau (P3) are conventional choices; 25% rel. error and chi2/dof<=2 (P5) are my choices.
- Grandchild: task id T119 (k1-mc8-grandchild), PASS, released. Control 0.783431; <a0> at k=3 from 400000 samples = 0.568632 +- 0.000524; I_2/I_1 by quadrature = 0.567924 (z=1.35, quadratures agree to 1e-16). I reread result.md and reran sampler.py in a copy: same PASS.
- Not done (time budget): longer runs / better algorithm (e.g. overrelaxation or abelian-direction moves), fit with cosh form.
- PCP verify (python): result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- PCP verify (rust): A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.

## Rerun (from this directory)
    P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
    python3 mc.py tune        # tune.txt, ~70 s
    python3 mc.py run 3000 0.06   # ~2 min, writes run_data.npz
    python3 analyze.py        # report_numbers.txt
(files open with mode x; move old outputs first. Grandchild: cd grandchild && python3 sampler.py after moving result.md.)

# Report: FD Hessian of the Wilson action (SU(2))
Control (control.txt): 1-2*3 = **-5**.

## Results (h = 1e-3, central 4-point mixed stencil; h chosen so truncation ~h^2 ~1e-6 and roundoff ~eps/h^2 ~1e-10; eigenvalue tolerance 1e-5)
Predicates were fixed in the docstrings of hess.py / hess2.py before running.
- **P1 (a) Q=-1, beta=1: MET.** eig B = -0.99999967 x3, 1 x9; max dev from claim 3.3e-7.
- **P2 (a) beta=3: MET.** eig B = -4.999999 x3, 1 x9; max dev 1.0e-6 (claim 1-2*beta = -5).
- **P3 (a) random config (seed 12345), beta=3: MET (measured error estimate).** max|H(h)-H(2h)|/3 = 2.4e-7 (Richardson error estimate); Richardson-corrected vs plain differ 2.4e-7; min eig B = -2.969386 (plain) / -2.969387 (Richardson). No analytic Hessian was derived; independence is only h vs 2h.
- **P4 (b) U=1, beta=1: MET.** Hess V eigenvalues: 0 x15 (|e|<1e-5), 2 x6, 4 x3 (1.99999967, 3.99999933); min -1.1e-10, so >= 0. Zero eigenvalues: **15**.
- **P5 (b) random (seed 777), beta=1: formally PASS but VACUOUS.** My "gradient-differenced" scheme used the same 4 function evaluations as the 4-point scheme, so symmetry error = 0.0 exactly. This was a defect in my own test design, not in the target. Min eig B = -1.3078934.
- **P6 (replacement test, hess2.py, inner step 1e-3, outer 3e-3): MET.** symmetry error 6.5e-11.
- **P7: MET.** min eig B = -1.30789188, differs from P5's value by 1.5e-6.

Convention note: the plaquette for (b) was read as Q = U_{x,1} U_{x+e1,2} U_{x+e2,1}^-1 U_{x,2}^-1 (prompt's "x+1", "x+2" read as x+e1, x+e2). Random links: normalized Gaussian 4-vectors (Haar on SU(2)).
No failed predicate attributable to the target.

## Sub-agent
Asked: independently compute (own FD code) the eigenvalues of B for the single plaquette, Q=-1, beta=3, after control "2+2*3" -> it wrote **8** to grandchild/control.txt (correct).
Returned: -4.99999919 x3, 0.99999981 x9 (h=1e-3), symmetry err 0.0 (vacuous by the same construction). Its summary text said "about 1e-6" deviation. I re-read grandchild/results.txt and reran its script in rerun_gc/ (PCP check K3): identical numbers. Agrees with my -4.999999 (differences ~1e-7, same h and stencil, so not a strongly independent test).

## Rerun commands
    cd /home/user/z4-workers/a4-chalcurv/child
    python3 hess.py results.txt      # (fails if file exists: mode "x")
    python3 hess2.py
    (cd rerun_gc && python3 hess.py)
PCP: P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P check --ws pcp --name hess --expect-exit 0 -- python3 hess.py results.txt (K1); hess2 (K2); gc_rerun (K3).

## Verify (last lines)
- python verify: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- rust verify: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.

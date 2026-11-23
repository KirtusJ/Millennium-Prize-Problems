# notes.md — k1-ext (worker under T116)
## Step 0 (18:4x) control
control.txt = 0.272341 (= -ln tanh 1, computed with python math).
## Step 1 read target
Read two-site-exterior/README.md, full-neutral.md, PRIOR_REVIEW_box.md row 13, TwoSiteExterior.lean, verify.py.
## Step 2 child
Admitted child T120 (child_admit.log). child/PROMPT.txt: 1D/2D Gaussian oscillator norm exp(-arsinh sigma), translation, orthogonal b. Control arsinh(1)=0.881374 (known: ln(1+sqrt2)=0.8813735870). Launched via pcp check child-run1 in background (log child_run.log).
## Step 3 target checks
scipy absent: check.py without shim exits 1 (ModuleNotFoundError) — recorded K1 expect 1.
With shim/scipy/linalg.py (numpy eigvalsh, subset_by_index slicing): check.py exit 0: central rank 42, E=44.3983569740; (2pi,0,2pi) rank 42 same E; (pi,0,0) rank 46 E=46.4863353847; (.4,-1.2,2.3) rank 46 E=46.6097785291; max SV error 2e-15; six oscillator checks pass. check_paths.py exit 0 (60 configs, 660 seam checks).
Note: check.py compares real-space derivative with the README's own Fourier formula; it tests the curl spectrum, not inequality (1).
## Step 4 own program own/e_path.py written (predicates P1-P7, M1 in docstring) before first run
## Step 5 own program results
Unrecorded dry run first (own/trial_dry.txt, disclosed), then recorded run own-e-path -> own/results_e_path_run1.txt (mode "x").
Boxes 2^3, 3x2x2, 3x3x2: real-space SVs = Fourier formula (max err 1.0e-14); E_* (2^3) = 44.398356973951; ranks 6n-6 central / 6n-2 non-central incl. enhanced-stabiliser (c,0,0); 36/48 points non-central, min E-E_* = 0.047 (at phi = 0.01*(1.3,.8,2.1)... smallest sampled); E-E_* ~ 2|phi| near centre (both directions); 2^3 path (c,0,0) monotone up to c=pi/2 then down; gauge invariance 1e-15; affine remainder |r|/rho^2 ~ 0.22 stable. 8 met, 0 failed, 1 measured.
## Step 6 Lean + worker.c
Lean rerun (copy TwoSiteExterior_rerun.lean, sha256 of target file 16a8c7a5... matches README) exit 0: centralRank, orthogonalPairs no axioms; affineRemainder [propext, Classical.choice, Quot.sound]. Content: centralRank is (42:N)=42, orthogonalPairs (56:N)=56 — tautologies; the counts are computed only in worker.c (C). affineRemainder is a scalar real ring identity.
worker.c compiled with gcc -nostdlib -static; three modes exit 0 and emit the same declarations. verify.py not runnable: imports replay from ../../local-response (absent).
## Step 7 child returned (K6 exit 0, 172 s). Control graded first: 0.881374 = arsinh(1) CORRECT. Released T120 (child_release.log).
## Step 8 reran child and grandchild programs in copies (rerun_child/, rerun_grandchild/), single-thread, recorded K10, K11, exit 0; numbers reproduce (A: e^{-arsinh s} to 1e-16; B: 0.880..0.997 increasing; C: b-independence 3e-16; D: 0.192574 exact; orth ratio exp(-|c|^2/2)); grandchild: lambda(1)=sqrt2-1 analytic, algebra reread by me: v^2 coefficient 1/8+1/4+alpha/2 correct.
Child's own process defect (its admission): first run used multiple BLAS threads (rule 8).
## Step 9 analysis summary (hand check of each step of (1)) — see report.md table. No DEFECT found in the steps used by full-neutral §1.
Web-fetch agent started for cited locators (Sint hep-lat/9312079, GPSvB hep-lat/9608015, Klein-Rosenberger 1706.06357).
## Step 10 citations (read via web-fetch agent + local pdftotext in scratchpad, no text copied here)
- arXiv hep-lat/9312079, S. Sint, "On the Schroedinger functional in QCD", 1993 (NPB 421 (1994) 135): section 3 defines temporal-gauge transfer T0, projector P on gauge-invariant functions, T = T0 P; eq. numbers (3.3)-(3.8) in that section seen. Locator matches the use.
- arXiv hep-lat/9608015, M. Garcia Perez, J. Snippe, P. van Baal, "Improved action and Hamiltonian in finite volumes", 1996 (LATTICE96 proc.): section 3.1 "The SU(2) effective potential": abelian constant background, momenta shifted k -> k + sC/N, s = 0, +-1. Matches the charge-shift structure; it is a one-loop Euclidean effective potential, not the transfer bound itself (README says so).
- arXiv 1706.06357, M. Klein, E. Rosenberger, "Harmonic Approximation of Difference Operators" (JFA 257 (2009)): harmonic approximation of low eigenvalues for multiwell difference operators. Matches as background.
- DOI 10.3233/ASY-151343 and GitHub links: not read (github not in network list; DOI not fetched).
## Step 11 report.md written; final verify PASS (both).

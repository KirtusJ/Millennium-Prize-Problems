# notes
- control.txt = 3.698130 (S0 R=4 eta=pi/4; 3R^4(1-cos(pi/32)) with R^4=256 -> 768).
- Wrote sf1loop.py (dense, plaquette-local FD Hessian h=1e-4, D from definition). Run R=4 via pcp check (K1, exit 0). Predicates P1-P6 all pass: gradmax 3e-12, S==S0 to 1e-13, |HD|max 1.6e-7 (<1e-6), min eig(H+DD^T)=0.1457, min eig(D^TD)=0.196, 577 gauge columns.
- Results R=4: dG/deta h=.02: 11.78253, h=.01: 11.78122, Richardson 11.78078; k=37.638582; c1(4)=-0.312997 (h=.01 -0.313009; h=.02 -0.313044).
- Note: numpy used >1 thread (user time 18s vs real 6.8s); later runs set OMP_NUM_THREADS=1.
- Grandchild T41 (grandchild/, control 3.698130 ok) recomputed S(V) from plaquettes (diff 1.4e-14) and k by FD = -37.638582 (Richardson). Its predicate "k == +24R^2 sin" FAILED on sign: true k is NEGATIVE. My sf1loop.py used +|k| -> my own defect, c1 sign was wrong. Reread grandchild result.json, reran nothing numeric myself beyond fixsign.py (check K2): c1(4)=+0.312997.
- T41 released. R=6 not run (dense 13608^2 eigvalsh/slogdet x4 exceeds 6 min budget).

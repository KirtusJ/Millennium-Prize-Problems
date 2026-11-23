# T40 report: c1(R) SU(2) SF one-loop, dense full-lattice

**Control:** control.txt = 3.698130 (S0, R=4, eta=pi/4).

**Result (R=4):** c1(4) = **+0.312997** (Richardson in h; h=0.01: 0.313009; h=0.02: 0.313044).
Gamma1'(pi/4) = 11.78078, k = 4 dS0/deta = **-37.638582** (negative; sign below).
R=6: **not run** (dense 13608-dim det x4 exceeds the 6 min budget).

**Method:** sf1loop.py. Hessian H from plaquette-local central finite differences (step 1e-4: truncation ~h^2=1e-8, roundoff ~1e-16/h^2~1e-8) of the exact action in X coordinates; D built from the definition; Gamma1 = 1/2 logdet(H+DD^T) - logdet(D^TD); eta-derivative by central difference at +-0.01, +-0.02 (error ~h^2 Gamma''', Richardson used; the two steps differ by 1.1e-4 relative).
Size: 832 dynamical links, 1344 plaquettes, 577 gauge columns.

**Checks (all passed, predicates fixed in the docstring):** max|grad S at V| 3e-12; S(V)=S0 to 1e-13; max|HD| 1.6e-7 (<1e-6, FD noise); min eig(H+DD^T)=0.1457>0; min eig(D^TD)=0.196 (full rank).

**Failed predicate (my own defect):** sf1loop.py used k=+|4 dS0/deta|. S0 depends on (pi-2eta), so k is negative. Found by the grandchild's check, fixed by fixsign.py (separate result file result_R4_signfixed.json; result_R4.json keeps the wrong-sign c1=-0.312997 as run). Not a target defect.

**Grandchild T41 (released):** grandchild/ ; control 3.698130 ok. S(V) from plaquettes vs closed form differ 1.4e-14; k by FD of S = -37.6385819 (Richardson), |k| matches 24R^2 sin(pi/32) to 2.5e-11. Its predicate "k == +37.638582" failed on sign only (my brief's literal formula). I reread result.json and report.md.

**Not checked:** R=6; independent recomputation of Gamma1 (e.g. momentum-space); H by a second step size; the unique-minimum/zero-mode claim beyond rank of D.

**PCP:** python verify: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)". Rust verify last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

**Rerun:** `cd /home/user/z4-workers/d1-run/child; OMP_NUM_THREADS=1 python3 sf1loop.py 4 new_R4.json; python3 fixsign.py` (new filenames, files are never overwritten).

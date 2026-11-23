# SU(2) plaquette, 4^5, beta=0.4

- Control: <(1/2)Tr U> at beta=1 = I2(1)/I1(1) = 0.240194 (matches trapezoid quadrature to 3e-10). In control.txt.
- Measured P = 0.099383 +/- 0.000587 (binned, 10 bins of 10; naive error 0.000558). 100 thermalisation + 100 measurement sweeps, seed 12345.
- Leading strong coupling I2/I1 at 0.4 = 0.099340. Difference +4.3e-5 (0.07 sigma).
- Predicates: P1 control vs quadrature (<1e-6) PASS; P2 single-link sampler mean 0.23886(105) vs 0.24019 PASS; P3 |P-lead| < 5*sigma+3e-3 = 0.00593 PASS.
- Tolerance origin: higher-order corrections are expected ~O(u^5) times a combinatorial factor; 3e-3 is a generous guess, not derived. The agreement is much tighter than the tolerance, but only 100 sweeps with ~0.6e-3 error, so it does not test corrections.
- Failure history: first run (result_run1.txt) FAILED P3 (P=0.00066) because of a bug: all mu-links were updated simultaneously, but each plaquette holds two mu-links. Fixed with a parity checkerboard update, rerun as run2. Predicates were not changed.
- Rerun: `cd /home/user/z4-workers/c1-excl/child/grandchild && sed -i 's/TAG="run2"/TAG="run3"/' su2_plaq.py && OMP_NUM_THREADS=1 python3 su2_plaq.py` (result files open with 'x', so a new TAG is needed). Files: su2_plaq.py, result_run1.txt, result_run2.txt, notes.md.

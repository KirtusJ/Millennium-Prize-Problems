# notes
- Step 1: control.py (2D 2x2 torus brute force, 256 configs) -> control.txt = 0.091272; matches analytic -ln[(c^4-s^4)/(c^4+s^4)]. Predicate C1 met.
- Step 2: vortex.c written (predicates C2,P1-P4 in docstring). First run (before any production): D=2 L=2 beta=.5 n=8 -> F=0.091759+-0.001974 vs exact 0.091272: C2 met (0.25 sigma). Test run D=4 L=4 b=.3 n=5 -> out/test_trash.dat (smoke test only, not used).
- Step 3: grandchild returned (exact 3D L=2 enumeration): F(0.3)=0.0325242683, F(0.6)=0.6912790067. Added predicate C3 (declared after seeing code, before running it): my vortex D=3 L=2 within 3 sigma of these.
- Step 4: production done (run_all.sh), report.md written.

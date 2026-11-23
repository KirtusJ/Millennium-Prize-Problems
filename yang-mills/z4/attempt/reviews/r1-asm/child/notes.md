# notes
- Step0: first control attempt failed (scipy absent; pipeline left empty control.txt, kept as control_attempt1_empty.txt). Recomputed with numpy Gauss-Legendre (a=pi/2(1-cos t) substitution): c*=4.605413 (n=200 and 800 agree to 1e-12).
- Step1: admitted grandchild T161 (released after return). Grandchild: control c*=4.605413 OK; at beta=256 float64 gives lambda_e==lambda_o (diff ~4e-16 noise), m=0 => inf. This is a defect of my own planned float64 route (expectation), confirms need for decimal high precision. Main program run_beta.py uses decimal.
- Step2: first check beta64 run failed exit 1 (KeyError in Kd mirror loop: my bug, not target). Fixed loop order; rerun.
- Step3: beta64 v1 output had str()[:n] truncating Decimal exponents (own formatting bug; r,q floats were fine: r=3.93616,q=1.94719). results_beta64.json kept; fixed formatting, outputs now results_beta*_v2.json.
- Step4: analyze.py first run failed exit 1 (np.bool_ not JSON serializable; own bug) leaving partial analysis_attempt1_partial.json; fixed, rerun.
- Step5: all runs done, report.md written. verify PASS.

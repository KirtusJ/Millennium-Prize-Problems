# notes
- control.txt = -5 (1-2*3)
- hess.py run (check K1): P1-P5 all PASS but P5 symmetry check is vacuous: my gradient-differenced scheme uses the same 4 evaluations as the 4-point formula, so sym err = 0.0 exactly (my own design defect, not target). Writing hess2.py with different inner/outer steps for a real symmetry test.
- Sub-agent returned: eig -4.99999919 x3, 0.99999981 x9, control 8; matches.
- hess2.py: P6 sym 6.5e-11 PASS, P7 PASS

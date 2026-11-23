# notes
- control: e^-1 = 0.367879 written to control.txt
- ratio.py run1 (out1.txt): Rc=5.503975 (P0 ok). R: .4->5.469064, .2->6.513378, .1->5.738552, .05->5.550620, .025->5.515154. P1 ok all (relgrid ~1e-7). P4 trivially.
- FAILED predicate P3 (monotone |R-Rc| decrease): m=0.4 is closer to Rc (0.035) than m=0.2 (1.01). Own expectation wrong (non-monotone at coarse xi~2.5-5), not a target defect. From m<=0.2: |R-Rc| = 1.01,.23,.047,.011 decreasing.
- m=0.0125: R=5.506743 (out2.txt), |R-Rc|=0.0028; R2=30.3242. Rc^2=30.2937. Waiting for grandchild.
- report.md written; grandchild R agrees 3e-9; my rerun of grandchild main line timed out.
- addendum added

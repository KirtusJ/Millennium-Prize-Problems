step1: control 0.771937; read target, A3,A4*,grounding. Findings pending in report
step2: read all inputs; key findings: numerics3 line cites don't exist (188 lines); 'observable-normalization' path unsupported; Lu83 'same coefficients' overstated
step3: grandchild T106 done+released+rerun ok; check_sec.py v1 P10 passed wrongly (my parse bug: only whole-line comments); v2 fixes
step4: v2 result: met 9 failed 1 (P10 numerics3 trace lines 225-227,242,272 don't exist; 162-165,164 point to unrelated text). Writing report.
step5: report.md written, verify PASS

# notes
- control: -ln(I1(4)/I0(4)) = 0.146735 (midpoint quadrature 20000 pts, own python)
- wrote mc.py with predicates in docstring (before first run)
- U(1) beta=4: m=0.14690±0.00184 vs 0.146735: P1 PASS (acc 0.30). grandchild T68 released; its -ln(I1(8)/I0(8))=0.06695692, -ln(I2(8)/I0(8))=0.26632363 rerun by me with midpoint N=4000: 0.0669569167, 0.2663236278 agree
- SU2 b16: m=1.4396±0.0236 window t=1..4 (rule-selected), C ratios 7.8,4.4,3.3 not single-exponential (effective mass drifts down) -> window-sensitive; 124 s
- su2 b64 done, report.md written

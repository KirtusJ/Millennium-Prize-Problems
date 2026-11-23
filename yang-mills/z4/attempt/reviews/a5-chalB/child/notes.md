# notes
- Step 0 control done: control.txt =  $(see file). scipy/mpmath absent; numpy only.
- control.txt = 0.240194 (matches I2(1)/I1(1))
- tail.py run1 exceeded 1 min (nodes recomputed per call; my defect, not target). Killed; partial results_tail.csv kept. Rerun as tail2.py with cached nodes, same predicates.
- tail2.py ran OK (exit 0) but stdout was not retained by pcp check; reran identical as tail3.py with redirect to out_tail3.txt.
- tail3 results: 888/0/0 on H (P e^{t/8}<=2), C_emp=1.0 (t=0), P1,P2,P6 pass, r(beta) 0.92-1.66, sup|P-Q| halves with beta (1.1e-1 -> 4.5e-4). Subagent control 1.570796 correct.

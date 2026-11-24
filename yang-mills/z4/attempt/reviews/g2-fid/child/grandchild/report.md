# T246 report
Control I_1(1)=0.565159104 (control.txt) OK.
R(6)=0.762726075749; R'(6)=0.036885895498 (CF, 50+ digits, depth 200/400 agree).
Numeric diff: h=1e-4 -> 0.036885895506; h=1e-5 -> 0.036885895498; Richardson 0.036885895495 (agrees to ~3e-12).
Enclosure 0.036885895 < R'(6) < 0.036885896: PASS (P1 PASS, P2 PASS).
Rerun (remove control.txt, result.txt first, they use 'x'): cd /home/user/z4-workers/g2-fid/child/grandchild && python3 t246.py

# Result (direct 4D midpoint grid, k=pi(2j+1)/N-pi)
| N | G(0) | G(1) |
|16|0.5|0.068874548950|
|24|0.5 (1e-16)|0.068874729098|
|32|0.5|0.068874742893|
|48|0.5|0.068874745584|
G(0)=0.5 to 2e-16 (predicate 1e-10 passed). Im G(1) < 1e-16.
G(1) = 0.06887475 (extrapolated 0.0688747462 via N^-4 Richardson on 32,48), abs error est ~3e-9
(spread between N^-4 and N^-2 assumptions 1.5e-9; raw G(48) is 1e-9 from extrapolation).
Control: control.txt = 1.9999999999999998 (PASS).
Rerun (files open mode 'x', so delete/rename results.txt and control.txt first):
cd /home/user/z4-workers/a8-chalB2/child/grandchild && python3 control.py && python3 g4d.py

# Notes
- control.py -> control.txt: mean 4 sin^2(k/2) over 64 momenta = 2.000000 (pass), written first.
- run.py -> results.txt (mode "x"; delete results.txt before rerun). Seed 12345, N=2000, MC samples a_mu(k) directly, flow + theta applied, no covariance formula; exact = tr(T Sigma T^dag)/L^4, Sigma=I/A.
- Rerun: cd /home/user/z4-workers/r12-wild/child/grandchild && rm -f control.txt results.txt && python3 control.py && python3 run.py

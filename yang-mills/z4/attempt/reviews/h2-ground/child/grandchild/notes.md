# T97 notes
- control.txt: 0.004958 (-ln tanh 3).
- Method: exact-matrix Rayleigh-Ritz, basis a^i b^j c^k exp(-w(a+b)/2), k even, reduced variables (r1,r2,cos theta). Program rr.py, output results.txt.
- Checks: harmonic-oscillator test gives 3.0000000000; including odd k at N=6 gives identical energy to k-even (3.35649849).
- Result: E_best=3.35053305 (N=22, w=2.5, dim 1222, 600 kept after cond. cutoff 1e-12). Monotone decrease; last step 2.7e-9; omega spread 2.3e-6.
- Predicate AGREE=True (|diff| 5.5e-8 < TOL 2.3e-6). Honest error ~1e-7 (upper bound; ill-conditioning cutoff drops modes at N>=12 so the tail is not fully converged).
- Rerun: cd /home/user/z4-workers/h2-ground/child/grandchild && RESULTS=results2.txt python3 rr.py   (~95 s)

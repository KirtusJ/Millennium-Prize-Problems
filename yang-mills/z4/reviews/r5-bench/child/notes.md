# notes
- control: sum 1/n^4 = 1.08232323 (direct sum to 2e5 + tail; matches pi^4/90). control.txt written.
- pcp init done (method not pinned, expected).
- corr.py written with predicates P1-P3 in docstring before first run. Method: d on N^3 grid, N>=4nmax+1 so cyclic conv == exact linear conv; C via Parseval in real space; analytic dC/dt + FD check.
- run 1 (results_1.txt): P1 FAIL for t=0.1 (rel 7.2e-9, K 150->200) and t=0.05 (rel 4.9e-9, K 300->400). P2/P2b/P3 PASS. My docstring estimate of the truncation prefactor was too optimistic (poly(K) ~ K^4..5 gives ~1e-8 at tK=15-20, not <<1e-10). Tolerance NOT changed; instead extend K (t=0.1 add K=250, t=0.05 add K=500) and switch to rfft/irfft half-spectra to save memory for N=320.
- run 2 (results_2.txt): all predicates PASS (P1 rel <= 6e-11; P2 ~1e-15; P3 FD agreement ~7e-6, consistent with O(h^2)). Run 1 was exit 1 (check K1), run 2 exit 0 (check K2).

# notes
- control: sum k^2 (1..10) = 385
- init pcp done (method not found, expected). shell_check.py run via check K1, exit 0. Output: see results.jsonl
- shell_check.py: P1 156/156 met, 0 failed. P2 (sum_r w_r == (n^d-(n-1)^d)/d) failed 22/24: MY OWN wrong expectation (that is the last-shell value only; total over axis 1 is (n^d-1)/d by symmetry). Kept as failed predicate. Stray file 'x' (accidental rerun arg) removed.
- Admitted grandchild T219.
- shell_check2 (P2' corrected) K2: 24/24 ok. Waiting for grandchild T219.
- T219 released, verified, report.md written.

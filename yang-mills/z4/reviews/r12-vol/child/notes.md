# notes
- control.txt = 0.00028060 (1/(640 pi^1.5))
- Run 1 (pcp_c.py): exit 1, results.json truncated at predicates: my defect (np.bool_ not JSON serializable), not the target. Numbers before the crash were fine (N=48 C_pos=2.177968313057048, rel pos-vs-mom 4e-16). Kept as results_failed1_truncated.json.
- Fix: bool() casts, output results_v2.json (mode x). Rerun below.
- report.md written; grandchild rerun K3 exit 0 identical

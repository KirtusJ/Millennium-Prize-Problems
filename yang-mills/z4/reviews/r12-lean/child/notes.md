# notes
- control.txt written: 0.008138
- check.py written (predicates+tolerances in docstring), run via pcp check K1 -> results1.txt: all 0 fails.
- Sub-agent (grandchild/) F6 boundary: control ok, eq-point max rel diff 9.35e-48, perturbed lhs<rhs. I reread results.txt and reran in a scratch copy: identical output (pcp check K2).
- No predicate failed; no expectation failed. min_rel_slack negatives in F2/F3/F4b-upper/F6 are rounding noise inside tolerance (cancellation near 0 / equality).

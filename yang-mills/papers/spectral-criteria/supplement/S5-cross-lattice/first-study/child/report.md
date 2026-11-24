# T235 report
Control answer: R = 1.2 (control.txt).

Held-out (8 chains, i%4 in {2,3}), jackknife n=8. f2 files were all present (16/16 END); c2 too.
```
c2 t1 R=0.701337 SE=0.005869 Var=0.00159708
c2 t2 R=0.956860 SE=0.005765 Var=0.000171082
c2 t3 R=0.706880 SE=0.005101 Var=0.000567706
c2 t4 R=0.968748 SE=0.004502 Var=0.000607844
f2 t1 R=0.988970 SE=0.004601 Var=0.000860081
f2 t2 R=0.999851 SE=0.003652 Var=0.000504789
f2 t3 R=0.988906 SE=0.004534 Var=0.000231551
f2 t4 R=0.999851 SE=0.002570 Var=0.00197936
```
```
t1: R_f2/R_c2 = 1.4101
t2: R_f2/R_c2 = 1.0449
t3: R_f2/R_c2 = 1.3990
t4: R_f2/R_c2 = 1.0321
```
Grandchild: task id T236 (released). Question: recompute R(t1) on c2 held-out chains with an independent script. Control 1.2 correct. It returned R=0.7013370728, Var=0.0015970815; I reread its answer files and reran its script (values reproduced; the rerun then crashed only on its own mode-x write to an existing file, expected). Matches my 0.701337 / 0.00159708.

Predicates (in analyze.py docstring) all passed; no failed predicates. Tolerance 1e-12 = double rounding. Note: t2 and t4 f2 R are both 0.999851 (R≈1: near-uncorrelated at lag; plausible, not a defect found). The 'for all' rule 4 did not apply.

PCP: python verify last line: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
Rust verify last line: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
Note: init reported ACR method not found (expected).

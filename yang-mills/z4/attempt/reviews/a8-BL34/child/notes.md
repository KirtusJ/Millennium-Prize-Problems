# notes
- control.txt = 0.267949 (2-sqrt3 expected 0.267949). scipy NOT installed, no network: T2 will use own numpy BFGS (deviation from 'using scipy.optimize').
- T1 done: lambda=0.837722340, C_pp=0.291666667 (=7/24), 1.5Cpp=0.4375, lambda/16=0.0523576. Subagent (grandchild/) independently: control 0.585786438, lambda 0.837722340, Cpp 0.291666667, trace 7; I reran its prog.py: identical.
- T2 done (own BFGS, no scipy): c_eff min over 20 samples: b10 M1 0.18395 M3 0.26587; b100 M1 0.17472 M3 0.18291; b1000 M1 0.17380 M3 0.17462; all 120 cases >0 and >= lam/16=0.05236. files out/t2_beta*.txt
- T3 run1 (step 1.5/sqrt(beta)): means 0.442713(SE .001685) / 0.437663 / 0.437844 vs 0.4375; BUT acceptance only ~5%, my docstring expectation (30-60%) FAILED (own tuning error, not target defect). Rerunning as t3b with step 0.5/sqrt(beta); run1 files kept.
- report.md written; pcp verify PASS

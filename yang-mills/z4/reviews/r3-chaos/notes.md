# notes (r3-chaos)

- step0: control.txt = 0.272341 (-ln tanh 1).
- step1: PCP register pcp initialised. Sub-agent launched for M3/M4 in child/.
- step2: mutate.py written (22 mutations, predicates B0/A/K/T/M2 in docstring); running under pcp check.
- step3: child returned (M3: 5 caught, 2 tolerance mutations not caught; M4: only rerun+byte compare detects). Rerunning c_su2_2N2 and e_tolH_1e6 myself.
- step4: reran c_su2_2N2 (exit 1, expected) and e_tolH_1e6 (exit 0, JSON sha256 identical to input 24939c8d...) -> child claims confirmed.
- step4b: rerun c_su2_2N2 verdicts: H MET, P1 MET, P2 FAILED, P3 MET (matches child). Waiting on Lean job.
- step5: m1_result.json: B0 6/6 baseline OK; 19/19 FALSE-predicted mutations rejected (CAUGHT); T3 accepted-as-true; F1,C4,A3 true-but-rejected. M2: unused hc,hcC,hφ (TwoSided). sorry flag on mutants = sorryAx from failed elaboration, not a source sorry.
- step6: report.md written; verify PASS.

# notes
- control.txt=0.499997 (FD n=2000, box 10); predicate 0.5±1e-5 met (err 3.1e-6).
- T81 admitted for subagent (grandchild/), running in background.
- solve.py written, predicates in docstring.
- P1 FAILED: HO self-test 2.996948 vs 3 (err 3.05e-3 > 2e-3). My tolerance estimate was too optimistic (FD, dr=0.099); check dr^2 scaling below. Not a target defect.
- HO scaling: dr .195 err 1.195e-2, dr .0988 err 3.05e-3, ratio 3.9 => dr^2 OK (P1 failure = my tolerance only). Coarse real run R6 N40 nL6: 0+ 3.3356,5.6974; 0- 5.2839; 1+ 5.3119; 1- 7.0979 (unconverged). OMP threads=1 needed (earlier 69s was threading).
- final: E0 3.350533, E1 5.32475 (L odd, exch +), 0- 5.325497; report.md written

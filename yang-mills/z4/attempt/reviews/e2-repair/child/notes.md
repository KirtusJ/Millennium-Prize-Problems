# notes T233
- control.txt = 0.771937 (-ln tanh(1/2))
- data: 32 streams/dir, 1152 rows each, args token4 = hot.
- run1 (via pcp check) FAILED exit 1: numpy bool not JSON serializable (my bug, not data). left partial results.json (kept). run2 same bug, partial results_run2.json (kept). fixed with bool(); run3 -> results_run3.json
- run3 ok. P2 fails N-d0 r4 d=2.110 (measured; my 2-sigma expectation, not a defect). Next: grandchild
- grandchild T237 done+released; report.md written

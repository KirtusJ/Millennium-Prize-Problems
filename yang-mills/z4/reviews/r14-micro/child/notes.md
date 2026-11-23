# notes
- init done (method not found, expected). scipy absent -> Bessel by series.
- control.txt = 3.25
- recompute.py run (predicates in docstring, fixed before run); report.md written.
- Failed predicates (all defects of the claimed values -- rounding/truncation/arithmetic -- none from my own expectation; my pre-run expectation was only that A8 88 and Q0 percent looked suspect): A5 R(0) value 0.912 vs 0.913 and error 0.034 vs 0.033; A5 Q0 0.957 vs 0.956; A6 Q0 4.34% vs 4.4; A6 R(0) 2.63 vs 2.7; A6 R(l/6) 7.54 (ratio) / 6.98 (direct) vs 7.6; A8 89.3 vs 88, 31.6 vs 31.
- Grandchild (A13) returned m=1.1110143957, m/0.3690=3.0109; I reran its solve.py in scratch copy: identical output.

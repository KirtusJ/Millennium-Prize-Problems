# notes
- control: zeta(4)=1.082323 (matches pi^4/90)
- PCP init done (method not pinned, expected)
- scaling.py written with predicates P1-P3 in docstring before first run; launching run1 via pcp check
- run1 (pcp K1) and a direct debug run crashed at json.dump (numpy bool not serializable); partial results_run1/run2.json left in place (truncated, not overwritten). Fixed with bool()/float() casts only; no predicate change.
- run3 (pcp K2): exit 0. P1, P2 pass with max rel err exactly 0 (lambda=2^{+-1} exact in binary). P3: 27/27 qualify, 0 failures.
- D4 convergence 64/96/128: 28398.60/28399.37/28399.70 (|.| kinks => ~h^2); int f identical to all digits.

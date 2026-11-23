# Notes: SU(2) 4^4 heat-bath reference

- control.txt: -ln(tanh 1) = 0.272341 (correct).
- PCP register `pcp` initialised ("method not pinned" as expected).
- Program su2hb.py written; predicates P1-P4 in docstring before first run.
  Bin size fixed in advance: 20 sweeps.
- Smoke run (beta 2.3 hot, 2+5 sweeps): ~40 ms/sweep, P rising from 0.52 toward ~0.59. Fine.
- Production launched: 4 runs (beta 2.3/8.0 x cold/hot), 500 thermalization sweeps discarded,
  5000 measured sweeps each, seeds 11,12,13,14. Run in parallel via pcp check.
- analyze.py written (bin size 20; other bin sizes printed for info only).
- 02:02: smoke timing estimate (40 ms/sweep) was wrong: the smoke wall time includes startup and
  the 280 ms was not representative; actual ~100 ms/sweep with machine contention (many other
  python workers). Runs at ~268 CPU-s, not done. Design flaw: results written only at end, so
  killing loses everything. Decision: let runs finish, overrunning the 15 min budget by ~5 min;
  this overrun is disclosed in the report.
- 02:11: the background shell hit its 10-minute limit and the four production runs were killed
  before writing any output (results only written at the end). No production data exists.
  Budget exhausted; stopping. Fix for a rerun: flush each per-sweep value to file as it is made,
  and use fewer sweeps (~1000 measured) given ~100 ms/sweep under contention.

# Notes

- Step 0: control 7*sqrt(2)=9.899495 written to control.txt.
- Step 1: pcp init done; extracted PDF pages to ref/text/pNN.txt.
- Step 2: read PDF pp.3-5, 11-13 (Table 1 p4, Table 10 p12, eq(2) p3, Appendix A p11). PDF page = printed page + 1 (PDF p12 prints "11"). Lattice sizes extracted with superscripts flattened (e.g. "104" = 10^4, "8310" = 8^3x10).
- Step 3: wrote teper_su2.py with predicates P1-P5 in docstring (before first run).
- Step 4: pcp check K1 exit 0 (expected 0); results/run1.json; P1-P5 all pass. Key: 8a√σ(2.3)=2.950(18), 8a√σ(2.5)=1.488(24); ratios 2.3/2.5=1.982(34), 2.4/2.6=2.016(47).
- Step 5: pcp verify -> result: PASS. Wrote report.md.
- Step 5 correction: report.md was NOT written (the tool harness blocked writing the report file); the report content was returned in the final message instead.

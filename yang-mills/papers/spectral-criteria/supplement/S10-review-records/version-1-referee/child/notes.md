# notes
- control: I_1(1)=0.565159104 (exact series, 30 terms); mpmath/scipy/sympy absent -> own series with Fraction/decimal.
- s1_s2_s3.py run1: S1 PASS (3808 cases, 0 viol, max p/B=0.0650 at k=200,th=.001), bound-ratio identity exact (4e-16); S2 PASS (0.003072388, 0.156180437, 0.934803630); S3 PASS (72 cases 1.9e-15).
- grandchild T246 returned (completed); to reread/rerun.
- s4_s5.py run1: S4a PASS exact (p-q k^2=-1/48, p' k=-1/16, w' k=1/2), S4b PASS (1e-59), S5a PASS exact-rational enclosure, R'(6)=0.03688589549764222280; S5b PASS (decimal-60 substitutes mpmath, not installed).
- grandchild T246 reread and rerun in a scratch copy: identical output; R'(6)=0.036885895497642 agrees with mine to 15 digits.

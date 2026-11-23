# notes
- control.txt written (8).
- t37.py run (pcp check K1, exit 1). PASS: P1,P2 (U1 slope .5003),P3,P5a (Weyl norm .99975),P5b,P5c (Weyl slope 4.0008, c=V/s^4 -> 0.620),P6,P7 (ratio 99.5).
- FAIL P4 (direct SU3 slope, s in [.02,.12]): counts 0..471 of 4e6, slope nan. Cause = MY expectation (V~0.62 s^4 ~1e-7 at s=.02; window unresolvable). Not target defect. Kept; post-hoc P4b below (window chosen AFTER seeing failure).
- t37b P4b PASS (z within 1; slopes 3.939 direct vs 3.926 Weyl, window s .15-.5). Next: sub-agent.

# notes
- control: so(4) dim = 6 written
- step 2: read all three docs. Q1 draft (stronger): l.3 "proved in full" (source: steps 2,11 sketch; 7 CITED-2nd/CLAIMED); l.15/39/328 Lu77 T>=0 "a theorem" (source/challenge: Luscher CLAIMED, unread); l.397 H2 "proved" drops "one model family, not independently reviewed"; l.405 OS78 RP passes to limits (source: OS CLAIMED); l.15 ||T||<=1 added w/o proof; l.52-55 (C) generalized c=1/2 -> any c; l.241 P=4k+2 vs source 4k+1 (differs). Weaker: l.312 gap lemma |F(s)|<=e^-s F(0) (challenge repair); l.262 sigma_k<=(k!)^{b+1} vs b+eps; l.360/384 free field "analogue", qualifications; l.177 E4 formula "written by us".
- step 3: Q2 proof recheck: all five steps (i)-(v) follow on reading.
- step 4: grandchild T28 done+released; G1 failed (3.6e-3 at n<=1e4; my suggested bound too tight, not lemma defect; n<=1e5 gives 2.1e-5), G2 met (384). Reran: identical.
- step 5: q2.py run1 FAILED (b): my own bug (vacuous all(()) in sigma search); kept as out_q2.run1_failed.txt; q2b.py fixed. Also my PCP check 'grandchild-rerun' expected exit 1 wrongly (diff exit 0 = identical): own expectation error.
- step 6: report.md written

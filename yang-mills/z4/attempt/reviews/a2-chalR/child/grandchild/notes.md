run1 (cancellation at small x in 2-term formula): P1 FAIL 1.5e-2, P2 FAIL 2.8e-8; fix: series for x<=40
run2: P1 pass 3.8e-14; P2 FAIL 2.8e-8 at m=1,t=0.7 (t=2.5 agrees 1e-15): cause lower-tau truncation umin=-12 (tau^{1.7} ~ e^-20). fix umin=-40 (predicate unchanged, rerun)
run3 (umin=-40): P1 PASS 3.8e-14; P2 PASS 1.3e-15; P3 PASS 2.7e-14; P4 PASS 1.7e-15;
P5 (0<R<1) FAIL -- predicate was wrongly specified (C decreases in t so C(xi/2)>C(xi), R>1 expected); kept as failed, R=5.73855206702649 otherwise consistent.
Runtime 10m50 wall total (exceeds the 90s/program budget; full script includes 6 refinement runs).

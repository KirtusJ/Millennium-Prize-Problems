# T49 report (O(2) minimal box)
Control: O(2) has 2 components (control.txt = 2).

| Claim | Verdict | Evidence |
|---|---|---|
| (a) S=0 only at identity-type orbit | DEFECT in the claim's wording | Zero set = gauge orbit {in=h^-1, out=h}, h in O(2), NOT just identity. Patterns with min S<1e-8: exactly 2 of 256 (all det +1, all det -1). Gauge by h=diag(1,-1) gives S=0 (also by grandchild). Shell data does not force g=identity: h acts only at x0. |
| (a) local minima | STANDS (as found) | Distinct values found over 256 patterns x 3 starts: 0, 6, 10, 12, 14, 16. All-plus pattern, 200 starts: only 0 (no spurious local minima). |
| (b) smallest nonzero minimum | STANDS: 6 | Mixed pattern: each odd-parity plaquette has trace 0, so s=1 exactly (checked for all 256). minS = #odd plaquettes in 256/256 patterns. Single flipped link lies in 6 plaquettes -> S=6. Positive gap 6 (one link flipped). |

Setup facts: 24 plaquettes contain a free link; each free link is in 6.
Failed predicates: K1 (scipy missing) = environment defect, not target; fixed with own BFGS. Own expectation of 48 plaquettes (8x6) was wrong: plaquettes share two free links, 24 is right (scan P1 reports 24 and per-link 6; not a coded predicate).
Not checked: Hessian/second-order verification of minima (BFGS with |g|<1e-7 only); only 3 starts per pattern (all-plus 200); the analytic proof that even plaquettes can always be zeroed (numerics only, 256/256).
Delegated: independent recompute of gauge-transformed S (=0 for h=diag(1,-1) and R(0.7)F) and single-link S (=6, 6 plaquettes, incoming and outgoing). Control passed (O(2)=2, identity S=0). I reran gc.py in scratch: output identical. Task T50 admitted and released.
Files: scan.py, results_scan.txt, notes.md, grandchild/.
PCP: `pcp_os verify --ws pcp` last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)". pcpos verify last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
Rerun: `cd child; OMP_NUM_THREADS=1 python3 scan.py 3` (move results_scan.txt first); `python3 grandchild/gc.py` (move results.txt first).

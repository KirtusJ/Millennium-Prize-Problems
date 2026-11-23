# Report
Control (control.txt): 2.777778 (matches hand value 100/36).

## Verdicts (N=10^6, seed 20260101, check.py; results.json)
| Item | Verdict | Evidence |
|---|---|---|
| Pair bound 4g(u)g(w) >= p1²+p2²-p3²-(3/4)\|q\|² | STANDS | 0 violations; min(L-RHS) = -5.6e-17 abs (-1.5e-16 rel to \|p\|²+\|q\|²), i.e. rounding, at q=0, p3≈1e-6 (p=(-0.1826,-0.5875,-9.1e-7), q=0). Hand proof for q=0: slack = p3⁴/(\|p\|²) ≥ 0. |
| (i) exp identity | STANDS | exact algebra (\|u\|²+\|w\|²=2\|p\|²+\|q\|²/2); log-space max rel diff 2.6e-15, 0 violations |
| (ii) \|u\|\|w\| <= \|p\|²+\|q\|²/4 | STANDS | 0 violations, max excess 2.2e-16 rel (AM-GM; equality when \|u\|=\|w\|, 51837 samples within tol) |
| (iii) perp inequality | STANDS | 0 violations (Cauchy–Schwarz since u_perp·w_perp = \|q_perp\|²/4-\|p_perp\|²), tight when u_perp ∥ w_perp |
| (iv) 4g g >= \|p_perp\|⁴/\|p\|² - (3/4)\|q\|² | STANDS | 0 violations; min -2.3e-10 abs = -5.6e-16 rel (rounding at large scale, q=0) |

Violated anywhere? No. Tight? Yes at q=0 with p3=0 (L=RHS=p1²+p2² exactly; infimum 0 attained there, and at p=q=0). Not tight for q≠0 with p3=0: slack ≥ 0.458|q|² on 10^5 samples (tight.py). Counts: u=0 50260, w=0 50193, p_perp=0 119583, q=0 50078, nondegenerate 899547. "Tight" count (|d|≤tol): 47 for the main claim; 6120 with rel slack <1e-6. Worst case = the q=0, p3→0 point above.

## Tolerances
tol = 1e-12·(|p|²+|q|²): quantities scale with that; ~10³ ulps (2.2e-16) margin for sqrt/division/cancellation. (i) in log space, 1e-12·s·scale. Observed errors are ≤ ~6e-16 rel, so tolerance is generous.

## Failed predicates
- Run 'main' (K1): exit 1, SyntaxError (keyword names with "1e-6") — my own coding defect, not the target. Renamed; predicates unchanged; rerun K2 exit 0.
- Grandchild: none.

## Delegated question (grandchild/)
Boundary p_perp=0 small q, and q=λp, 200000 each. Control 2.777778 first. 0 violations both. A: L=ρ⁴/(|u||w|) ≥0 ≥ RHS, equality only at p=q=0. B: L=|λ²-4|h², tight at λ=0,p3=0 (derived by hand; not sampled — I covered it in tight.py). I reread findings and reran its check.py in rerun_gc/ (gc_rerun, exit 0): results.txt identical (diff SAME). Its B bound for all λ is numerical only.

## Not checked
No proof for general (p,q) of the pair bound (numeric only, random sampling, not adversarial optimisation); only 3 dims; no extreme scales beyond 1e±3 ratios (grandchild went to 1e-8).

## Rerun
cd /home/user/z4-workers/r13-volchal/child
(results files are mode "x"; remove results.json tight.txt first, and rerun_gc/results.txt)
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name main2 --expect-exit 0 -- python3 check.py
$P check --ws pcp --name tight --expect-exit 0 -- python3 tight.py
$P check --ws pcp --name gc_rerun --expect-exit 0 -- bash -c 'cd rerun_gc && python3 check.py'

## PCP OS
init: method not found (expected). Python verify last line: "A pass is not..." -> actual: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`.
Rust verify last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## Counts
Met: control, 5 items STANDS, delegation + reread + rerun. Failed: 1 own syntax-error run. Measured only: numeric sampling, no proofs beyond hand derivations noted.

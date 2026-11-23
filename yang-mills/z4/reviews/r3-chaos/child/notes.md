# notes (M3/M4 sub-worker)

## Step 0
control.txt = 0.272341 (matches known answer).

## Step 1
`pcp_os.py init pcp --principal principal --principal-name "Kirtus Justus"` -> workspace created, "method: not pinned" (expected).

## M3 reading
- Usage line `RERUN python -I two_dim_control.py <mpmath site directory>` matches how it is run (argv[1] appended to sys.path). OK.
- Observation: H checks the closed forms u1_closed/su2_closed against quadrature, but P1/P2 recompute M with their own inline mp.besseli calls (lines 101, 108). So a Bessel-order error in P1/P2 is NOT protected by H; only by P1/P2's own asymptotics.
- Input result json: all verdicts MET, all N qualify. Lean files: no reference to json/result (grep).

## Mutations & predictions (written before runs)
| name | line | prediction |
|---|---|---|
| a_bessel_P1 | 101 I_1 -> I_2 in U(1) M | P1 fails (M->~2, D grows, factors ~1/4) |
| a2_bessel_H | 62 u1_closed I_n -> I_{n+1} | H fails for all U(1) cases -> no U(1) qualify -> P1 fails too |
| b_beta_plus1 | 101 beta N^2 -> N^2+1 in U(1) M | P1 fails (M ~ 1/2 - 1/(4N^2) < 1/2) |
| c_su2_2N2 | 108 4N^2 -> 2N^2 | P2 fails (M -> 3/4, M-3/8 does not shrink) |
| d_asym_half | 124 k*d -> k*d/2 | P3 fails (ratio -> 2) |
| e_tolH_1e6 | 77 TOL_H *1e6 | nothing fails (NOT CAUGHT) |
| e2_tolP3_1e6 | 127 P3 tolerance *1e6 | nothing fails (NOT CAUGHT) |

## Baseline (K1)
runs/orig: exit 0, H/P1/P2/P3 all MET; output JSON byte-identical to input (sha256 24939c8d...9d0f both).

## Mutant runs (K2-K8) -- see report.md table. Surprises:
- c_su2_2N2 failed P2 via factors ~1.0 (M-3/8 tends to a constant), not via the sign test.
- e_tolH_1e6 and e2_tolP3_1e6 produce a JSON byte-identical to baseline (sha 24939c8d...), because tolerances are not recorded in the JSON and the actual residuals are far inside both bounds. Not detectable by any predicate or by byte comparison.

## M4 (K9-K13)
- m4/two_dim_control_result.json: line 197 (P1.M[1], N=8) 0.503963426... -> 0.503973426...
- Program never reads an existing result; it only refuses to overwrite (K13: copy beside mutated json -> "result file exists; refusing to overwrite", exit 1, content never inspected). Lean files: no reference to json/result/IO (grep rc=1). => nothing in input/ notices.
- Rerun in m4/rerun (K9, exit 0) + compare.py: vs mutated copy equal False (K10, exit 1); vs input equal True (K11).
- K12 was a mis-pathed command (../input from m4 resolves to child/input, nonexistent; exit 2 != expected 1). Nothing written; input/ sha unchanged. Left in the register as a recorded mismatch.

## verify
result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)

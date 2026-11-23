# Report (child)

**Control:** I = 1/sqrt(5) = **0.447214** (control.txt; midpoint quadrature agrees).

## G(n) in infinite volume (gquad.py -> gquad_result.json)
3D midpoint grid on (-pi,pi)^3, L = 32,64,128,256,512 points per axis (via symmetry). Convergence is O(L^-4), because the integrand has a |k| non-analyticity at k=0. The error estimate is the difference between the last two grids, 2.8e-11.
- G(0) = 0.5000000000019 (exact 0.5)
- G(1) = 0.06887474584
- G(2) = 0.01115271766

## Finite N (cov.py -> cov2_result.json). Link counts: 432 (N=4), 3000 (N=6), 10976 (N=8).
| N | C(p0,p0) | C(p0,p1) | C(p0,p2) |
|---|---|---|---|
| 4 | 0.4926748 | 0.0637384 | 0 (degenerate: p2 is on the shell, F=0) |
| 6 | 0.4991560 | 0.0681089 | 0.0102713 |
| 8 | 0.4997836 | 0.0686653 | 0.0109449 |
| inf | 0.5 | 0.0688747 | 0.0111527 |

CG (own bincount matvec, rel. tol 1e-11, 16–49 iterations) matches the dense solve to 5.6e-17 (N=4) and 4.7e-13 (N=6). |D g| = 8.9e-16.

## Questions
(a) Yes. C(p0,p0) rises 0.49267 < 0.49916 < 0.49978 and stays below G(0)=0.5. The gap to 0.5 is 7.3e-3, 8.4e-4, 2.2e-4. This is measured at three sizes only, so I make no claim about the rate.

(b) Yes, measured. |C^N(p0,p_n) - G(n)| decreases with N for n=0,1,2. For n=1 it is 5.1e-3, 7.7e-4, 2.1e-4. For n=2 it is 1.1e-2 (the degenerate N=4 zero), 8.8e-4, 2.1e-4. The finite-N values stay below G(n) in every case here.

(c) At N=6, C01 = 0.0681089. Take m_p0 = 1 and m_p1 = -0.0681089. Then Cov(F_p0^2, F_p1^2 | b) = 2 C01^2 + 4 m0 m1 C01 = -2 C01^2 = **-0.009278 < 0**.
Implication: the conditional law of the squared curvatures is not positively correlated for all boundary data. With zero conditional means the covariance is 2C^2 >= 0, but nonzero means with opposite sign (relative to C01) flip it. So there is no pointwise positive-correlation (FKG/Griffiths-type) inequality for F^2 conditional on boundary data. Any argument that needs it must use the means or the boundary data explicitly. **Not checked:** whether this pair of means is realised by some actual boundary data. Here the field is zero outside the box, so conditioning data is not shown to produce these means. This is an algebraic existence statement about the formula.

## Predicates
Predicates are in the docstrings of gquad.py and cov.py, written before the first run.
- Met: Q1, Q2 (2.8e-11), Q3 (G values decreasing); C1; C2; C3; C5; C6; C4 for n=0,1,2.
- Measured only: all of (a), (b) as stated; no theory tolerance exists for them.
- **Failed (run 1, cov_result.json, kept):** C2, C5 and C4(n=2). Cause: my own expectation. At N=4 the plaquette p2 sits at time 4 = N, on the shell, so all its links are 0. F_p2 is identically 0, the right-hand side is zero, and CG returned nan. This is not a target defect. I amended the docstring, made CG return 0 for a zero right-hand side, and reran (cov2_result.json). All predicates then passed. The N=4, n=2 entry is a degenerate zero, not evidence of convergence.
- Also failed (K2): the first cov.py run died on a leftover junk line of mine (IndexError). No result file was written.

## Grandchild
Asked: independently recompute G(0), G(1), G(2) by a direct 4D midpoint grid (not the 3D formula), with the known-answer control G(0)=0.5 first, in grandchild/.
Returned: control G(0) = 0.500000000000 (diff 0). L=32: G(1)=0.068874742893, G(2)=0.011152705816; L=24: 0.068874729098 and 0.011152650146. I reread grandchild/result.txt; it matches that return. Against my converged values the differences are G(1): 3.3e-9 and G(2): 1.2e-8, both within its own L-difference estimates (1.4e-8, 5.6e-8). The grandchild covered only the G values. The finite-N numbers were cross-checked by CG vs dense instead.

## PCP OS
Register created with `init`; method not found, as expected. Checks recorded: K1 gquad, K2 cov (exit 1, my bug), K3 cov_fixed (run-1 failure of predicates, exit 0), K4 cov_rerun.
- `$P verify --ws pcp` last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl` last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

## Rerun
Result files open with mode "x", so use fresh names:
```
cd child
python3 gquad.py gquad_result2.json
python3 cov.py cov3_result.json   # reads gquad_result.json
cd grandchild && rm control.txt result.txt && python3 g.py
```

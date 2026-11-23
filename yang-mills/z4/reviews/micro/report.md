# Micro-review of input/ (Z4 two-dim control), narrow cases C1-C8
Control: control.txt = 0.272341 (-ln tanh 1). Also equals Z_2 M(N=1) in my run, a cross-check of the program formulas.

## Verdict table
| Item | Verdict | Evidence |
|---|---|---|
| C1 rerun fresh dir, python -I | STANDS | `cmp` identical; SHA-256 24939c8d...9d0f for both (register check c1_rerun, exit 0) |
| C2 N=1,2,3: M>1/2, M>3/8, H | STANDS | U(1) M=0.80656, 0.58694, 0.53116; SU(2) M=0.41848, 0.38686, 0.38024; H qualifies 3 of 3 N per group (max rel diff 2.1e-31 SU(2) N=1, N=1 uses the w>=pi branch) |
| C3 k=2 for Z_4, Z_6 | STANDS | M/A: Z_4 1.000112, 1+4e-15, 1, 1 ; Z_6 0.8812, 0.99950, 1-1.9e-14, 1 at N=2,4,8,16. Leading error -(1+cos(2pi/n))e^{-N^2 d}; n=4 exact, error +e^{-2N^2}/3. Delegate and I agree. Slow at small N for n=6 (-12% at N=2). |
| C4 ratios at N=2,4,8,16; strictly decreasing from N=1 | STANDS | Z2 1.0000000375,1,1,1; Z3 0.998767,0.99999999998,1,1; Z5 0.951816,0.999979,1,1. Strictly decreasing for every integer N=1..16, all three n. Note: M/A at N=16 is 1 to ~1e-77 or better, so the 1e-6 tolerance is very loose; and ratio at N=1 is 1.0062/0.9284/1.1583 (not near 1). |
| C5 Scaling.lean edge cases | STANDS (README wording imprecise, not wrong) | see below; Edge.lean exit 0, 3 standard axioms |
| C6 README says (N+1)^2 | STANDS | README line "x = (N+1)^2, N = 0,1,2,..." states it. z2_physical_gap_le is NOT tight: LHS/RHS = 0.0465 (x=0.01), 0.5447 (x=1), 4.5e-7 (x=10); sup of LHS*(1+x) on grid 0.001..20 is 0.5999 at x=0.667. Slack factor >= 1.67 everywhere. |
| C7 README tables vs JSON | STANDS | every printed number checked: M(64) U(1) 0.500061048820, SU(2) 0.375011444266; factors 4.29,4.07,4.02,4.00 and 4.01,4.00,4.00,4.00; all 12 Z_n M values; "20 cases", "5 of 5". No outlier. One ambiguity: see failed/ambiguous list. |
| C8 README predicate table vs docstring | STANDS with 1 wording gap | H, P1, P2, P3 same, same tolerances (1e-25, [3,5], 1e-6), same windows, same counts (met 4, failed 0). Gaps: README P1 says "remainder shrinking" but the factor window applies to D=N^2(M-1/2)-1/4 not to M-1/2 (M-1/2 shrinks by 4.19 first, outside the numbers quoted); README P3 omits "N = 2,4,8,16" tested set. |

Counts: met 8, failed 0 (of the items), measured only 0. Defects: none found. Two wording points (C5, C8).

### C5 detail
- `lattice_gap_tendsto_zero`: proof is m = (m/a)*a -> M*0; uses only a->0, a n != 0. Negative a n and negative M or m are allowed and the conclusion holds (Edge.lean `neg_ok`: a=1/(n+1), m=-a, M=-1). README sentence says "a_n -> 0, a_n != 0 and m_n/a_n -> M for a real M", so it is true as written; only the section header "a_n > 0" is stronger than needed.
- `physical_gap_tendsto_atTop`: hypothesis `a -> nhdsWithin 0 (>0)` is an eventual statement: finitely many a n <= 0 (even = 0) are allowed. Genuinely negative tail breaks it: a=-1/(n+1), m=1 gives m/a -> -infinity (Edge.lean `neg_case`). So "from above" is needed, and README says it.
- `c <= m n` for all n is stronger than needed: eventually suffices (Edge.lean `phys_eventually`, proved, 3 standard axioms). README "for all n" is true, merely not minimal. Also hc : 0 < c is needed (c<=0 gives nothing).
- Not checked for meaning: whether m n can be negative physically (m = -log of operator norm ratio is >= 0 for a contraction).

## Hypotheses each statement uses (where stated)
- All numeric M(N): transfer eigenvalue = c_r(beta)^N, weight w = exp(beta(cos-1)), beta = N^2 (U(1), Z_n), 4N^2 (SU(2)); stated in input docstring and README section 2, explicitly NOT computed from a lattice (README "Not covered").
- Continuum values 1/2, 3/8: quoted (docstring).
- P3 asymptote: next-order term smaller (docstring); I derived it and the delegate checked it.
- Lean: Scaling hypotheses as in C5. FiniteGroupControl: Z_2 eigenvalue ratio = tanh beta, not formalized (README says so).

## Failed predicates (mine)
- My expectation Q6 "z2_physical_gap_le is tight (LHS/RHS>0.9)": failed everywhere, as I predicted: the bound is loose, not defective.
- My own expectation that the README factor list concerns M-1/2: wrong; it concerns D (program P1). Delegate's first run (320 digits, zn.py) failed its analytic-correction predicate at N=16 for n=3,4 through its own precision floor (M/A-1 < 1e-320); rerun zn2.py at 900 digits passed. Both kept in child/. Not a target defect.
- No predicate of the input failed in any of my reruns.

## Not checked
- Lattice derivation of eigenvalues c_r^N, continuum values, Wilson-loop reading, A4 cross-read, 4D statements, ACR, input's Lean compile (I did not rerun Scaling.lean / FiniteGroupControl.lean themselves, only read them; README reports exit 0), input's own register/pcp folder (absent from input/), Python 3.14/mpmath version differences.
- "From N=1" strictness: only integers 1..16 tested, not 17+ (monotonic decrease beyond is analytic, not tested).
- Same model family as director: agreement is not independent review.

## Delegated question (rule 7)
C3: "Z_n gap asymptote with k=2 for n=4,6 (and 3,5 sanity), N=2,4,8,16, derive leading correction." Child (child/, own register child/pcp, control 0.272341 written) returned k=2 correct, error formula -(1+cos(2pi/n))e^{-N^2 d} (n=4: +e^{-2N^2}/3). I reread child/report.md and independently computed the same ratios in micro_checks.py (Z4 err 1.1184e-4, 4.2214e-15; Z6 -0.11881, -5.0259e-4): equal. Child's verify: PASS. Run 1 failure noted above.

## Commands to rerun
```
set PYTHONUTF8=1
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py init pcp --principal principal --principal-name "Kirtus Justus"
python .../pcp_os.py check --ws pcp --name c1_rerun --expect-exit 0 -- bash c1.sh      # C1 (c1.sh uses fresh/)
python .../pcp_os.py check --ws pcp --name micro_checks --expect-exit 0 -- python -I micro_checks.py <mpmath site dir>   # C2,C3,C4,C6 -> micro_result.json
python .../pcp_os.py check --ws pcp --name lean_edge --expect-exit 0 -- bash -c 'cd /c/Users/donke/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean <abs>/Edge.lean'
python .../pcp_os.py verify --ws pcp
```
verify last line (before report written; rerun at end): see below.
verify last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"

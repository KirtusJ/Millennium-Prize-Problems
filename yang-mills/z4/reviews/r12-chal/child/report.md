# Report: theta bounds T1-T3

Control: sum exp(-pi m^2) = 1.086435 (control.txt; equals pi^(1/4)/Gamma(3/4)).

| Item | Verdict | Evidence |
|---|---|---|
| T1 (j=0) | STANDS | 241/241 grid points hold; max theta0/bound = 0.982. Proof: decreasing f, 2*sum_{m>=1} f <= 2*int_0^inf f. |
| T2 (j=1..4, constant 2) | STANDS | 964/964 cases hold; max ratio about 0.975. |
| T2 constant "2" needed? | 2 needed in general; 1 suffices only for small j | Constant 1 holds for all tested j<=4 (6001-pt grid), but fails for j=8 (gap/M=1.12), 12 (1.28), 20 (1.44), 30 (1.54). Constant 2 holds there (<=2). j>=8 is outside the requested range. |
| "integral + max" justification | STANDS (two-sided form) | Standard: for unimodal f on x>0, sum_{m>=1} f(m) <= int_0^inf f + max f. Doubling gives int_R f + 2*max, which is the "2". Gap/M approaches about 1.5 at j=30, below the proven 2. Unimodality verified in 1205/1205 cases (sign of f'). |
| T3, q=2 | STANDS (identity) | 3*th1*th0^2 equals the brute-force 3-D sum for n!=0 (13/13, rel 1e-9), so it is equality, not just >=. Bound-substituted version >= true value 241/241. |
| T3, q=4 identity | STANDS | 3*th2*th0^2+6*th1^2*th0 equals the brute-force sum (13/13). By hand: |n|^4 = sum n_i^4 + 2*sum_{i<j} n_i^2 n_j^2, with 3 pairs, giving the 6. Bound-substituted version >= true value 241/241. |

## Failed predicates
None in the requested ranges (met 100%). Constant-1 for j>=8 (informational, my own expectation was that it would hold; it did not). This is not a defect in T2, which claims constant 2.

## Not checked
- No rigorous (interval) arithmetic. Float64 with tolerance 1e-12*rhs, which is roundoff of sums of ~1e3 terms.
- Brute-force 3-D comparison only on 13 values c>=0.05 (cost); smaller c covered only by the product identity and the algebra.
- No pure-Python c<1e-3, no j>4 for T1/T3, and the constant-1 failure was tested at j=5,8,12,20,30 on c in [0.05,50] only.
- mpmath and numpy are absent, so no high precision.
- The grid is finite; "for all c" is not proved by it (T1 and T2 are proved by the argument above for the unimodal bound).

## Delegation
Question: independently recompute theta_2(0.01), theta_1(0.3), theta_0(0.01) by direct sum and by Poisson summation (analytic derivatives), with a known-answer control. Outcome: control 1.086435; values 132934.038818, 5.39340531265, 17.7245385091; the two methods agree to about 1e-15 relative. I reread the files and re-summed directly (m<400); it matched. Rerunning grandchild/run.py exits 1 only because its mode-"x" output files already exist.

## Counts
Met: P0 1205/1205, T1 241/241, T2 964/964, T3 q=2 13/13 plus 241/241, q=4 13/13 plus 241/241. Failed: 0. Measured only: constant-1 probe (P3 964/964 held, j<=4; failures at j>=8).

## PCP OS
- `$P verify --ws pcp` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Rust `pcpos verify pcp/register.jsonl` last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## Rerun
Files control.txt and grandchild/* use mode "x", so delete them or use a fresh directory first.
cd /home/user/z4-workers/r12-chal/child
python3 control.py; python3 main_test.py; python3 const1_probe.py; python3 const1_largej.py
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P check --ws pcp --name main_test --expect-exit 0 -- python3 main_test.py
$P verify --ws pcp; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl

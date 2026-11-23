# Report: R1(xi) = G(xi/2)/G(xi), lattice free scalar, 4D

Control: K_1(1) = 0.601907 (control.txt; trapezoid on exp(-x cosh t) cosh t).

## Verdict table
| Item | Verdict | Evidence |
|---|---|---|
| R1 bounded | STANDS | 6.58 (xi=4) down to 5.505 (xi=128); all in (1,10) |
| R1 -> 2K1(1/2)/K1(1) = 5.50397482 | STANDS | rel. deviation 1.96e-1, 7.6e-2, 1.37e-2, 3.2e-3, 7.9e-4, 1.96e-4 |
| R2 -> (continuum R1)^2 = 30.2938 | STANDS | R2(128) = 30.30562, rel. dev. about 3.9e-4 (R2 = R1^2 is an identity, not an independent check) |
| Deviation decreases with xi | STANDS | 5/5 consecutive pairs decrease; the last ratios approach 4, so the deviation goes like ~1/xi^2 |
| Quadrature accuracy | STANDS | N=80 and N=120 agree to <=1.8e-14 relative |
| Independent xi=16 check (Schwinger) | STANDS, tolerance 1e-6 | 5.5796296 vs mine 5.5796295, relative difference 2.4e-8, well inside the sub-agent's stated tolerance (1.05e-6, which is looser than its own predicate) |
| Dependence of the deviation on n/xi = 1/2 | NOT CHECKED | only the ratio n = xi/2 vs xi was run |

Table (N=120):

| xi | R1 | R2 | rel. dev. |
|---|---|---|---|
| 4 | 6.5835480452 | 43.34310486 | +1.961e-1 |
| 8 | 5.9212916240 | 35.06169450 | +7.582e-2 |
| 16 | 5.5796294697 | 31.13226502 | +1.375e-2 |
| 32 | 5.5215749393 | 30.48778981 | +3.198e-3 |
| 64 | 5.5083075465 | 30.34145203 | +7.872e-4 |
| 128 | 5.5050539532 | 30.30561903 | +1.961e-4 |

## Hypotheses used
- The integrand is smooth in k for M>0. I used Gauss-Legendre on the octant with the map k = pi s^4, which clusters nodes near k=0. This replaces spherical coordinates; the tolerance is the N=80 vs N=120 difference.
- The continuum value is taken from the formula given in the task, and I did not re-derive it.
- Full-cube integration with no truncation. By lattice symmetry the octant gives a factor of 8.

## Failed predicates
- Main program r1.py: none failed (P1-P6 met). P6 (R2 = R1^2) is an identity, so it is weak evidence.
- Sub-agent g4d.py: P2 failed. Its two resolutions agreed to 1.05e-6 against its fixed tolerance of 1e-6. This was a defect in its own quadrature, not of the target: only G(8) moved between its two resolutions. My rerun reproduced the same numbers. The failure is kept in grandchild/result_first.md and grandchild/result.md.

## What I did not check
- Other n/xi ratios, other observables, and the sign or size of the O(1/xi^2) coefficient beyond the numeric ratio.
- A fit of the asymptotic rate; I only observed ratios of about 4 between successive deviations.
- The continuum formula itself, and the PCP register beyond the verify lines.

## Delegated question and result
Sub-agent in grandchild/ with control I_0(1) = 1.266066 (met). It computed R1(16) by the Schwinger representation: 5.5796296064 (fine) and 5.5796354536 (coarse). Its P2 failed marginally (above). I reread g4d.py and result.md and reran it under `pcp check` (K2). The rerun reproduced the numbers exactly. It agrees with my k-space value 5.5796294697 to 2.4e-8.

## Rerun commands
```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 ctrl.py > control.txt        # control
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name r1 --expect-exit 0 -- python3 r1.py r1_result.txt   # remove r1_result.txt first (mode x)
cd grandchild && python3 g4d.py      # remove result.md first
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Last lines: Python verify: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)". Rust verify: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right." The `init` method-not-found message appeared as expected.

## Counts
- Met: control, P1-P6 of r1.py, the Schwinger control and P1/P3/P4 of g4d.py. (11 in total.)
- Failed: 1 (g4d.py P2).
- Measured only: R1/R2 table, deviation rates (~1/xi^2), R1(16) cross-check.

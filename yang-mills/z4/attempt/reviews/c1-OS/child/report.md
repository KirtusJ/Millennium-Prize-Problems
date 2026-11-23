# T7 report: Z^4 free massive field, continuum limit

Control: G_1(0) = 0.127112 (control.txt; Schwinger/Bessel method A and k4-analytic + 3D grid method B agree to <1e-8). First control run failed (exit 1, my own cutoff e^-14 lost 8e-7; fixed to e^-30, not a target defect).

## Numbers (method A, Schwinger integral with e^-2t I_n(2t) computed by periodic quadrature; S via K_1=int e^(-z cosh u) cosh u du)
| x | m | S_m(x) | S(x) | rel. error | 2G²/m⁴ rel. err (Wick) |
|---|---|---|---|---|---|
| (1,0,0,0) | 0.5 | 2.18474035e-02 | 1.52464883e-02 | 4.329e-01 | 1.053e+00 |
| (1,0,0,0) | 0.25 | 1.72243012e-02 | 1.52464883e-02 | 1.297e-01 | 2.763e-01 |
| (1,0,0,0) | 0.125 | 1.56225124e-02 | 1.52464883e-02 | 2.466e-02 | 4.993e-02 |
| (1,0,0,0) | 0.0625 | 1.53350636e-02 | 1.52464883e-02 | 5.810e-03 | 1.165e-02 |
| (.5,.5,.5,.5) | 0.5 | 1.23890202e-02 | 1.52464883e-02 | 1.874e-01 | 3.397e-01 |
| (.5,.5,.5,.5) | 0.25 | 1.44453720e-02 | 1.52464883e-02 | 5.254e-02 | 1.023e-01 |
| (.5,.5,.5,.5) | 0.125 | 1.50460142e-02 | 1.52464883e-02 | 1.315e-02 | 2.612e-02 |
| (.5,.5,.5,.5) | 0.0625 | 1.51966668e-02 | 1.52464883e-02 | 3.268e-03 | 6.525e-03 |
| (1,1,0,0) | 0.5 | 5.82113685e-03 | 5.62766380e-03 | 3.438e-02 | 6.994e-02 |
| (1,1,0,0) | 0.25 | 5.63199901e-03 | 5.62766380e-03 | 7.703e-04 | 1.541e-03 |
| (1,1,0,0) | 0.125 | 5.62372858e-03 | 5.62766380e-03 | 6.993e-04 | 1.398e-03 |
| (1,1,0,0) | 0.0625 | 5.62641241e-03 | 5.62766380e-03 | 2.224e-04 | 4.447e-04 |
| (2,0,0,0) | 0.5 | 2.15996226e-03 | 1.77142209e-03 | 2.193e-01 | 4.868e-01 |
| (2,0,0,0) | 0.25 | 1.84412529e-03 | 1.77142209e-03 | 4.104e-02 | 8.377e-02 |
| (2,0,0,0) | 0.125 | 1.78846729e-03 | 1.77142209e-03 | 9.622e-03 | 1.934e-02 |
| (2,0,0,0) | 0.0625 | 1.77562542e-03 | 1.77142209e-03 | 2.373e-03 | 4.751e-03 |

Method B (independent: k4 done analytically, 3D midpoint grid N=48/m) agrees with A for x=(1,0,0,0) and (.5)^4 at all m: max rel diff 1.05e-13 (8 cases).

## Predicates (fixed in main.py docstring before the first run; full output predicates.txt)
- P1 MET: 16/16 (x,m) cases have x/m integer (all qualify).
- P2 MET: A vs B < 1e-7 (measured 1e-13).
- P3 (error decreases as m halves) MET for all 4 points, but for (1,1,0,0) only barely (7.7e-4 -> 7.0e-4) because the signed error S_m-S changes sign between m=1/4 and 1/8 (+4.3e-6, -3.9e-6, -1.3e-6): measured fact.
- P4 (successive ratio in [3,5], i.e. ~m^2) MET for (.5)^4 (4.00, 4.02) and (2,0,0,0) (4.27, 4.06); FAILED for (1,0,0,0) (ratios 3.34, 5.26, 4.25; the 5.26 is outside [3,5], last is 4.25) and FAILED for (1,1,0,0) (44.6, 1.10, 3.14: sign change/cancellation). Failure = my expectation (tolerance [3,5] was a guess around 4), not a defect of the target; the m^2 trend is seen where no cancellation occurs. Order measured only down to m=1/16.
- P5 MET (rotation): |S_m(1,0,0,0)-S_m(.5^4)|/S = 6.2e-1, 1.8e-1, 3.8e-2, 9.1e-3 for m=1/2..1/16 (ratios 3.4, 4.8, 4.2): decreases ~m^2, <1e-2 at m=1/16. Same limit within lattice artefacts, confirmed numerically only down to m=1/16.
- P6 MET: Wick rel. error (m^-4*2G^2 vs 2S^2) ~ 2x the S error for all 4 points (e.g. (1,0,0,0): 1.05, 0.28, 5.0e-2, 1.2e-2), decreasing.
Claim S_m->S: supported numerically (errors fall to 0.2%-0.6% at m=1/16); not a proof.

## Grandchild
Task-graph id T11 (label c1-OS-grandchild, parent T7), admitted and released. Control given first: K_0(1)=0.4210244382 -> returned 0.421024438241 (pass). Question: K_1(1)/(4 pi^2) by two methods other than my cosh integral (power series; Wronskian with quadrature K_0). Returned 1.524648825162e-02 both, difference 0. I reread k1.py and reran it: identical output. My S(1,0,0,0)=0.015246488251616 agrees. Note its two methods share the I_0, I_1 series (only K_0 independent).

## Rerun
cd /home/user/z4-workers/c1-OS/child; (fresh dir needed: result files use mode x)
python3 control.py; python3 main.py; python3 evalpred.py; (cd grandchild && rm out.txt && python3 k1.py)
PCP: P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P verify --ws pcp ; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl

## PCP verify (last lines)
- python: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- rust: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

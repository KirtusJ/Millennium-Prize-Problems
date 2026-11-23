# T175 report

Control: integral_0^1 exp(-x^2) dx = 0.746824 (control.txt).

## Grid results (all predicates fixed in gridcheck.py docstring before first run; results.json)
| item | cases | grid points | met | failed | worst margin (measured) |
|---|---|---|---|---|---|
| A1 | 4 | 1600008 | 1600008 | 0 | -2.220e-16 |
| A2 | 4 | 1144006 | 1144006 | 0 | 1.000e-02 |
| A3 | 4 | 1600008 | 1600008 | 0 | 1.005e+00 |
| A4 | 4 | 8 | 8 | 0 | 2.817e-02 |
| B1a | 12 | 24000012 | 24000012 | 0 | 0.000e+00 |
| B1b | 12 | 24000012 | 24000012 | 0 | 9.415e-03 |
| B2 | 12 | 24000012 | 24000012 | 0 | 1.031e+01 |
| B3 | 12 | 22421192 | 22421192 | 0 | 1.000e-12 |
| C1 | 1 | 1656400 | 1656400 | 0 | 0.000e+00 |
| D1 | 1 | 200199 | 200199 | 0 | 0.000e+00 |
| D2 | 1 | 7407363 | 7407363 | 0 | 0.000e+00 |

Notes (measured only):
- Failed predicates: none, in any case. Nothing to attribute to my expectation or to the statement.
- A1 worst margin -2.2e-16 is double rounding (met under TOL=1e-12, which is a few thousand ulps of O(1) values). B3 "worst 1e-12" is the tolerance minus a measured difference of exactly 0. B1a worst 0 at a=0. C1/D1/D2 worst 0 occurs at D=0 / x=0 where both sides are 0.
- A3 used the analytic g'; central differences (h=1e-7) agree to <=9.4e-5 (eta=0.01, near the steep part), max |g'| = 1.99, 3.15, 6.31, 14.10 vs bounds 3.00, 4.74, 9.49, 21.21.
- A4 (c*=4.605413195): c_rho = 2.667426, 3.947568, 4.456390, 4.577243 for eta=0.5,0.2,0.05,0.01; lower bounds -0.836, 1.164, 2.885, 3.836. Margins: smallest 2.8e-2 (eta=0.01).
- Rule 4 hypothesis counts: B (tau/2<=pi/2, 3eta<=2, eps<=2): 12/12 cases qualify; C1: 40400/40400 (S2,D) cases have S2-D>0 and S2+d>0; A2: 4/4 etas have 3eta<=2; D: x in [0,1), c in 1..10 step 0.25 (37 values).
- Tolerances: 1e-12 = double-precision rounding allowance; B1 1e-9 = trapezoid error ~h^2 with h=7.9e-7; A4 1e-8 = quadrature allowance (composite Gauss-Legendre 4000x20 on a=t^2; scipy absent; sub-agent's Simpson agrees to 1e-9).
- Grids are finite samples, not proofs. Sample sizes: A 4e5 pts/eta, B 2e6 pts/case, C 400 S2 x 101 D x 41 d, D1 2e5+200 (to 1-x=1e-12), D2 37 c x same x.

## Sub-agent
Question: independently recompute c* and c_rho(eta=0.05) (Simpson with a=t^2 substitution) and check c*-pi*sqrt(6 eta) <= c_rho <= c*, after a known-answer control (int_0^pi sin = 2.000000, passed).
Task id: T176 (admitted and released via pcpos). Outcome: c*=4.605413195, c_rho=4.456390111, inequality true; I reread run.py and reran it in a copy (the original refused to overwrite, as intended): identical numbers; agrees with mine to <1e-9.

## Rerun commands
    cd /home/user/z4-workers/u1-gapA/child
    python3 gridcheck.py        # needs a fresh dir or delete results.json (mode "x")
    python3 mkreport.py         # table.md (mode "x")
    P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
    $P init pcp --principal principal --principal-name "Kirtus Justus"
    $P check --ws pcp --name gridcheck --expect-exit 0 -- python3 gridcheck.py
    $P verify --ws pcp
    /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl

## PCP OS verify (last lines)
- Python `verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- Rust `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right." (preceded by register file SHA-256 40d6e6e4cd44aa3d1f479f3df89628d277af7c4f29d850545adbf345a773e63e)
- `init` reported "method: not pinned / ACR implementation packet not found" (expected).

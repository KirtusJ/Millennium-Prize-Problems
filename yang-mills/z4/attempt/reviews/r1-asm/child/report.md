# T160 report: factor check (1D model)

Control: c* = 4.605413 (control.txt; first attempt left an empty file, kept as control_attempt1_empty.txt).
Method: lambda_e, lambda_o, the even eigenvector computed in python `decimal` at 77 to 189 digits (float64 cannot resolve Delta ~ exp(-c sqrt(beta)); grandchild confirmed, see below). Residual of inverse iteration <= 1e-46 .. 1e-161, below the predicate bound 10^-(prec-40).

| beta | N | -log m/sqrt(beta) =: r | q = (-log g(pi/2)+log g(0))/sqrt(beta) | 2q/r | min Tphi/(lam phi): S, window, kink |
|---|---|---|---|---|---|
| 64 | 52 | 3.9362 | 1.9472 | 0.989 | 1.568, 1.751, 3.363 |
| 256 | 100 | 4.1819 | 2.0735 | 0.992 | 1.488, 1.553, 3.022 |
| 1024 | 200 | 4.3350 | 2.1552 | 0.994 | 1.420, 1.451, 2.818 |
| 4096 | 404 | 4.4320 | 2.2081 | 0.996 | 1.373, 1.388, 2.693 |

c* = 4.6054, c*/2 = 2.3027 (Psi_tent(pi/2) by quadrature 2.30271).

| item | verdict | evidence |
|---|---|---|
| (a) -log m/sqrt(beta) -> c*, not 2c* | STANDS | r = 3.94, 4.18, 4.33, 4.43 rises toward 4.605; |r-c*| = 0.669, 0.424, 0.270, 0.173 decreasing; fit c + (a ln b + b0)/sqrt(beta) on last 3 gives c = 4.570 (0.8% off c*). 2c* = 9.21 is far away. |
| (b) q -> c*/2 | STANDS | q = 1.95, 2.07, 2.16, 2.21 -> 2.3027; deviations 0.356, 0.229, 0.147, 0.095; fit gives 2.285 (0.8% off). |
| (c) tent with eta=0.25 is a supersolution-direction T phi >= lam_e phi | STANDS (on S, window, kink) | ratios all >= 1.37 at all 4 betas (4/4 qualify, tolerance 1e-9). Margin shrinks with beta (S-min 1.57 -> 1.37), so not shown to hold uniformly as beta -> infinity; 4 betas only. Min on S at beta=4096 is at x=2.877 (far from kink); kink ratio is the largest (2.69). |
| (d) 2 sup_chain(-log g) ~ c* sqrt(beta) | STANDS | sup of -log g along the chain is attained at the kink x=pi/2 and equals q sqrt(beta); 2q/r = 0.989..0.996 -> 1, with r -> c*. So the factor is c* sqrt(beta), not 2 c* sqrt(beta). |

Caveat on (d): "sup_chain" is read as -log g at pi/2 relative to g(0) (the tent peak); I did not evaluate a maximum over an arbitrary chain of grid points from the eigenvector.

## Failed predicates / failed runs (all my own, none a defect of the target)
1. Control first attempt: scipy absent, pipeline wrote an empty control.txt (my expectation about the environment). Recomputed with numpy.
2. check K1 (beta64): exit 1, KeyError in mirrored-kernel loop (my coding bug). Fixed.
3. results_beta64.json: Decimal printed via str()[:n] truncated exponents (my formatting bug); r, q were right. Superseded by *_v2.json (v1 kept).
4. check K7 (analyze.py): numpy bool not JSON serializable (my bug); partial file kept as analysis_attempt1_partial.json.
5. Grandchild's plain float64 route: lambda_e == lambda_o to 1e-16, m = 0, r = inf at beta=256 (my expectation that float64 would do was wrong; that is why decimal was used).
No predicate on the physics (a)-(d) failed. The 3% fit tolerances were my guess, the fit has 3 parameters on 3 points (exactly determined), so it is weak evidence; the monotone approach is the stronger evidence.
Case counts: (a) 4/4 betas closer to c*; (b) 4/4 closer to c*/2; (c) 4/4 qualify on S, window, kink.

## Not checked
- beta > 4096; other eta; whether the ratio in (c) stays >= 1 as beta -> infinity (it decreases slowly).
- Existence/size of the poly prefactor (only fit-level evidence: a ~ -0.95 in r).
- Chain-wise g(z)g(z')T(z,z') bound itself; the inequality Delta >= poly * min_e ... was not tested.
- Kink window used only the +pi/2 kink (T symmetric under x -> -x).

## Grandchild
Question: independent beta=256 recomputation of -log m/sqrt(beta), known-answer control first. Admitted as T161 (--label r1-asm-grandchild --parent T160), released after return (RELEASED T161). Outcome: control c* = 4.605413 matched; main run in float64 gave lambda_e = lambda_o = 0.823739739329 (agrees with my decimal lambda_e = 0.82373973932947986), m = 0, r = inf, i.e. it did NOT independently reproduce r = 4.1819. I reread its files and reran grandchild/main.py: same output. So m at beta=256 is checked by one method only (mine); only lambda_e and the control are cross-confirmed.

## PCP OS
verify --ws pcp: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
pcpos verify pcp/register.jsonl (last line): `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
(init reported method not pinned / ACR packet not found, as expected. Checks K1 and K7 were exit 1 vs expected 0; recorded.)

## Rerun
cd /home/user/z4-workers/r1-asm/child
python3 cstar.py   # needs control.txt absent
python3 run_beta.py 64; python3 run_beta.py 256; python3 run_beta.py 1024; python3 run_beta.py 4096   # each ~0.3-9 s; outputs results_beta*_v2.json (mode x: remove old ones first)
python3 analyze.py   # analysis.json (mode x)
python3 grandchild/main.py
Counts as: met, failed, measured only (measured, not proven).

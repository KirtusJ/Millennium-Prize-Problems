# T227 report
Control: R^2 of (0,0),(1,1),(2,1),(3,3) = 0.852632 (control.txt; 20.25/23.75 by hand).

## Results (m = m_0; ddof 0; N=36864 pooled; jackknife se = sqrt((n-1)/n * sum(t_i-mean)^2))
| | b=0 | b=1 |
|---|---|---|
| rho (32 streams) | 0.0224141 | 0.0834115 |
| rho jackknife se (32) | 0.00403291 | 0.00557360 |
| R2_held (streams 16-31) | -0.0132590 | -0.00233129 |
| R2_held se (16, beta fixed) | 0.00209182 | 0.00175550 |
| R2_train (in-sample) | 0.0189070 | 0.0286924 |
| discarded directions | 0 | 0 |
(Train C_YY eig min/max: b0 0.0104/19.46, b1 0.0101/0.800 — well above the 1e-10 cutoff.)
Full-precision values: results.json. Negative R2_held means the TRAIN fit does worse than the HELD mean (overfit/no transfer); expected possibility, not a failure.

## Predicates (stated in analyze.py docstring before first run)
All passed: parse counts, N=36864, C_YY PSD (full and TRAIN pool, tol 1e-10*max = the task's cutoff), |rho|<=1 (tol 1e-12), R2_train in [0,1] (tol 1e-9), R2_held<=1, jackknife finite and >0. Failed predicates: none in the analysis.
One failed PCP check: K2 (grandchild rerun launched from child/ exit 1) — my own error: rho.py reads ../data relative to its cwd. Rerun as K3 from grandchild/ exit 0. Both are kept in the register.
"For all" predicates: none needed a per-case hypothesis test (only 2 blocks).

## Sub-agent (task T228, parent T227)
Question: recompute rho, block 0, no jackknife, streaming triangle sum with fsum, no full matrix. Control 0.852632 correct. Answer rho = 0.022414127551879784; I reread the code and reran it (identical); matches my 0.02241412755187925 to ~13 digits. T228 admitted and released (event 455/456).

## Not checked
- Layout/convention of smy (j*308+u) and m_0 = first component, taken from the task text (grandchild also could not check).
- Data not checked against raw measurements; only moments available. Blocks 2-7 not analysed. No tolerance study of cancellation in the R2 moment formula beyond the PSD/range predicates. m_1, m_2 unused.

## Rerun
cd child
python3 analyze.py   # results.json is mode 'x': remove/rename it first, or edit the path
cd grandchild && python3 -I rho.py new_result.txt
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl

## PCP verify (last lines)
- pcp_os.py verify: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right." (preceding line: result: PASS)
- pcpos verify: its last line returned was the same sentence; no separate verdict line was printed beyond it.

# SU(2) one-site 3D plaquette amplitudes A(a,b,c)

**Control:** ∫(tr U)^4 dU = **2** (control.txt; Catalan number; MC check 2.0014 ± 0.0016, within 4 SE).

## Results (mc.py, N = 4·10^6, seed 20240601, SE = sample std/√N, verdict at 4 SE)
| (a,b,c) | A | SE | verdict |
|---|---|---|---|
| 1/2,1/2,1/2 | 0.55573 | 0.00088 | positive |
| 1/2,1/2,1 | 0.41578 | 0.00101 | positive |
| 1/2,1,1/2 | 0.41579 | 0.00101 | positive |
| 1/2,1,1 | 0.35944 | 0.00117 | positive |
| 1,1/2,1/2 | 0.41647 | 0.00101 | positive |
| 1,1/2,1 | 0.36033 | 0.00117 | positive |
| 1,1,1/2 | 0.36032 | 0.00117 | positive |
| 1,1,1 | 0.40670 | 0.00136 | positive |

**A(1/2,1/2,1/2) = 0.5557 ± 0.0009.** The permutation-related entries agree within errors, as symmetry requires. These are MC estimates only, not exact values.

## Predicates (fixed in mc.py docstring before first run)
- P0 control E[(trU)^4]=2 within 4 SE: **met**.
- P1 sanity E[χ_a(commutator)] = 1/(2a+1) within 4 SE: **met** (a=1/2: 0.50066±0.00052; a=1: 0.33377±0.00060).
- P2 "for all 8 cases" sign decided at 4 SE: hypothesis tested per case; **8 of 8 cases qualify** (all positive, none compatible with zero).
- Tolerance: 4 SE from the CLT standard error. Nothing was tuned.
- **Failed first run:** `results.json` is a 70-byte partial file. The run exited 1 (check K1) because json could not serialize a numpy bool. This was a defect in my own program, not in the target. I kept the file. The fix was to write `results_v2.json` with the same seed, which gave K2 (exit 0). Output numbers are the same as in the first run's printout.

## Grandchild (grandchild/)
- Question: boundary case A(1/2,0,0) must equal 1/2, and A(1/2,1/2,0), with its own MC and seed 12345.
- Control: E[(trU)^2] = 1.00188 ± 0.00100, z = 1.88, passed.
- Result: A(1/2,0) = 0.49938 ± 0.00074 (z = -0.85, consistent with 1/2); A(1/2,1/2,0) = 0.50109 ± 0.00094, positive. It also noted the analytic value E[trU^4]/4 = 1/2.
- My check: I derived ∫dU2 χ_{1/2}(U1U2U1⁻¹U2⁻¹) = χ(U1)²/2. Conditioned on U1, P12 and P13 are independent, so A(1/2,1/2,0) = E[(trU1)^4]/4 = 1/2 exactly, which agrees.
- Rerun: I copied the scripts to grandchild_rerun/ and reran them. They gave identical numbers. PCP check K3 (exit 0) also ran.

## PCP OS
- `pcp_os.py verify --ws pcp`, last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`, last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
- Init reported the method as not found, as expected. Checks K1 (failed, exit 1), K2, K3 are in the register.

## Rerun
```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 mc.py   # needs results_v2.json removed first (mode "x"), or edit the filename
cd grandchild_rerun && python3 control.py && python3 task.py   # needs control.txt/report.md/results.json removed first
```

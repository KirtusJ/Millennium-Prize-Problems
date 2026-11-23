# T80 report

CONTROL: control.txt = 0.499997 (1-D HO, FD n=2000, box 10; predicate 0.5±1e-5 met, error 3.1e-6). Ran before anything else (the check record K1 only re-prints the file).

## Results (sine-DVR radial in r_i, orthonormal Legendre in L, own Lanczos; units: h as stated)
| quantity | value | convergence evidence |
|---|---|---|
| E_0 | **3.350533** (±2e-6) | sectors (L even, exchange +). Stable to 2e-6 over R=6,8,10; N=24..48; nL 8 vs 12 (nL 6 -> +2e-6). Independent sub-agent (different code, even-L only): 3.35053307, my rerun reproduced it exactly. FD code (solve.py) approaches it from below as dr->0 (3.3356 @dr .146, 3.3438 @dr .098, 3.3385 @R8 dr .13; unconverged, only a consistency check). |
| E_1 | **5.32475** (±3e-5) | sector (L odd, exchange +): N=48 R6 5.324771; N=64 R8 5.324760; nL 8->12 shifts about -4e-6 (N=32). |
| gap E_1-E_0 | **1.97422** (±3e-5) | |
| nearby levels | (L even, exch -) 5.325497 (stable in R, N, nL to 2e-5); (L even, exch +) 2nd 5.7254; (L odd, exch -) 7.115 (not converged in N) | |

Q2: E_1 state is exchange-SYMMETRIC (Y1<->Y2: +) and ODD under Y2 -> -Y2 (parity (-1)^L = -1, odd Legendre content, lowest L=1). Degeneracy: no exact degeneracy found, but it is NEAR-degenerate with the exchange-ANTISYMMETRIC, inversion-EVEN state at 5.325497 (splitting 7.4e-4, about 25x my error estimate; I did not prove it is not an exact degeneracy in the continuum limit, only that numerics separate them). Within each of the 4 symmetry sectors I computed 2 lowest eigenvalues, so degeneracy inside a sector would be missed by Lanczos (not checked beyond nev=2 Ritz values being distinct).

## Failed predicates (all mine, not target defects)
- P1 (solve.py FD, HO self-test 3.0 tol 2e-3): got 2.99695 (err 3.05e-3). Tolerance estimate too optimistic; error scales as dr^2 (dr .195 -> 1.2e-2, dr .099 -> 3.05e-3, ratio 3.9), so FD correct. Replaced by solve2.py (sine-DVR) with re-posed P1 tol 1e-6: got 3.0000000000000195 and 5.0000000000000115 (pass).
- P4 for the FD code: not met (dr, R not converged; last FD runs were killed by me; no FD Richardson done). FD numbers are only a consistency check.
- First E_1 numbers at N=32 (5.3196, sector 1+) were wrong by 5e-3: N-dependent in the odd-L sector (N=40 5.32248, N=48 5.32375, N=64 5.32476). Caught by convergence study; my expectation of N=32 sufficiency (taken from the sub-agent's even-L result) failed. Odd-L sector needs finer radial grid.
- Sub-agent's own failed predicates: residual 6e-6 for one run (iteration cap), nl>8 runs not finished.

## Not checked
No L-odd-sector estimate with N>64 or nL>12 at large N; 1-/second levels not converged; no check for exact degeneracy inside a sector; no analytic check of the (L=1) coupling; Dirichlet-box effect on the 1+ state only tested R=6 vs 8; FD Richardson not completed.

## Sub-agent
Question: independent E_0 only, with a different discretisation (sine-DVR + Legendre, own Lanczos), with 3-D HO control (1.5, got 1.5000000000000158). Task id T81 (admitted by `task-admit`, released by `task-release`, event 167 TASK_RELEASED). Outcome: E_0 = 3.35053 (rerun here gives 3.35053307), agrees with mine.

## Rerun
export OMP_NUM_THREADS=1
python3 control.py (mode x; delete control.txt first)
python3 solve.py --R 8 --N 80 --nL 3 --ho --sectors 0+ --tag ho1   (FD, slow, tag files are mode x)
python3 solve2.py --R 8 --N 32 --nL 8 --nev 2 --tag X          (all 4 sectors)
python3 solve2.py --R 8 --N 64 --nL 8 --nev 2 --sectors 1+ --tag Y
cd grandchild && python3 e0.py control; python3 e0.py 8 32 8
Every run was wrapped: `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name <n> --expect-exit 0 -- <cmd>` (K1..K17). Raw data in results/*.json, notes.md.

## Verify last lines
- python verify: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- rust verify: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

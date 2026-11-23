# Report (PCP child)

Control: sqrt(pi)/(640 pi^2) = 0.00028060 (control.txt). Grandchild control also 0.00028060.

## Results (N=48, t=0, s=0.005, l=1)
- **C = 2.177968313057 (position-space FFT; 2.177968313057048)**; momentum-space FFT-convolution cross-check 2.177968313057049
- int f^2 ≈ b^3 sum f^2 = 0.01879479225576
- ratio C s^(5/2) / (b^3 sum f^2) = 2.0485145e-4 (0.00020485144799891) — measured only, no expected value

## Predicates (fixed in pcp_c.py docstring before first run)
- P1 pos vs mom at N=48 rel<1e-10: MET (4.1e-16)
- P2 same at N=8: MET (1.3e-16)
- P3 max|Im D|/max|D|<=1e-12: MET (2.6e-16)
- P4 a(0)=0 and C>0: MET
- Ratio: measured only.
- Failed: run 1 (check K1) exit 1 — my defect: np.bool_ not JSON-serializable, results.json truncated (kept as results_failed1_truncated.json); numbers before crash identical to the final ones. Not a failure of the target or of an expectation.
- Caveat: P1 shares a(k) and f construction with the position-space code, so it tests the FFT algebra, not the formula transcription; the grandchild's independent brute force covers the formulas at N=8 only. N=48 itself is not brute-forced (511x... too large to be worth it).
- "Brillouin zone" index choice: n=N/2 vs -N/2 give the same khat^2 (sin^2), so FFT ordering is equivalent.
- register: method reported not found (expected).

## Grandchild (grandchild/)
Question: at N=8, same formulas, does a brute-force double sum over (k,k') (511x511, fhat by direct sum at actual n+n') equal the direct-sum position-space value?
Result: C_mom=3.44162704613096926, C_pos=3.44162704613179837, rel diff 2.4e-13 (tol 1e-10), agree. Control passed.
I reread run.py and reran it in grandchild_rerun/ via pcp check (K3, exit 0): identical output. My FFT code at N=8 gives 3.4416270461318 (C_pos) — consistent.

## Rerun
cd /home/user/z4-workers/r12-vol/child
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print('%.8f'%(math.sqrt(math.pi)/(640*math.pi**2)))"
OMP_NUM_THREADS=1 python3 pcp_c.py   # results_v2.json must not exist (mode x); rename results_v2.json in pcp_c.py to rerun elsewhere
cd grandchild && python3 run.py      # needs a fresh results.txt

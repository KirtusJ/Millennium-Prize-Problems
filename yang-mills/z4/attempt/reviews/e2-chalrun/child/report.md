# T51 report: c1(R;U(1)), d=4, eta=pi/4

**Control:** 1/(2cos(pi/8)) = 0.541196 (control.txt). Grandchild control cos(pi/3) = 0.500000.

| R | c1(R;U(1)) | error estimate | agrees with quoted (1e-6)? |
|---|---|---|---|
| 2 | 0.2287515 (0.228751482) | 3e-13 | yes (quoted 0.228751) |
| 3 | 0.2293161 (0.229316113) | 2e-12 | yes (0.229316) |
| 4 | 0.2330566 (0.233056564) | 3e-11 | yes (0.233057) |
| 5 | 0.2360589 (0.236058883) | 1e-10 | yes (0.236059) |
| 6 | 0.2382528 (0.238252786) | 9e-11 | yes (0.238253) |
| 7 | 0.2398783 (0.239878349) | 2e-10 | no quoted value |
| 8 | 0.2411188 (0.241118838) | 4e-10 | yes (0.241119) |

Error estimate = |trace formula - Richardson finite difference of Gamma1(eta)| (two independent routes). The
trace formula c1 = tr[A^-1 H_t]/(2N_t) was checked against -Gamma1'/k, not assumed.
The differences from the quoted values (1e-7 to 5e-7) are consistent with their 6-decimal rounding.

**Failed predicates:** none (P1-P7 all passed; every block count was full: Hermitian, H·D≈0 at max 5e-15, A positive
definite, min eigenvalue 0.034 at R=8). The H·D=0 and positive-definiteness conditions were hypotheses per block, and all
blocks qualified (8, 27, ..., 512 of the same number).
Note: a smoke run (R=2,3) before the real run wrote a results.txt that I deleted, since it was my own scratch run. The PCP-checked run created its own.

**Grandchild (T52, label e2-chalrun-child-grandchild):** independent dense real-space recomputation for R=2, own code
(grandchild/c1.py). Control 0.500000. c1 = 0.2287515 (Richardson FD) and c1_alt = 0.2287515, difference 2.5e-12; all 6 predicates
passed. I released T52, reread the files and reran it: same output. It matches my R=2 value.

**PCP OS:** last line of `pcp_os.py verify --ws pcp`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
(the preceding line is `result: PASS`). Last line of `pcpos verify pcp/register.jsonl`: the same text. Checks K1 (main run) and K2 (grandchild rerun) exit 0.

**Rerun:**
```
cd /home/user/z4-workers/e2-chalrun/child
export OMP_NUM_THREADS=1
mv results.txt results_old.txt   # the program refuses to overwrite
python3 c1_sf.py 2 3 4 5 6 7 8
cd grandchild && python3 c1.py
```

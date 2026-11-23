# r7-fix report: repair of the two_dim_control check (builder)

Control: control.txt = 0.272341 (-ln tanh 1). The published files are unchanged (sha256): input/two_dim_control.py da806965…8cc, input/two_dim_control_result.json 24939c8d…9d0f.
New files: two_dim_control_v2.py (53b1ac83…c7bf4) and two_dim_control_v2_result.json (f9fb2c75…e371).

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| R1(i) tolerances and windows written to the result, each with a one-phrase source; the table is hashed in the docstring and compared with the values in use | STANDS | v2 docstring has a 9-entry table and its sha256. The result has `tolerances` and `tolerance_table_sha256`. m6/m7 (code-only loosening) exit 2 with "in use != table" |
| R1(ii) four negative controls on every run, recorded; one that passes gives exit 2 | STANDS | K4: NC_H rel 1.0e-22 fails, NC_P1 factors ≈0.25, NC_P2 factors ≈1.0, NC_P3 1.00001 fails. In m6/m7, NC_H and NC_P3 pass, which gives exit 2 |
| R1(iii) `--verify <result.json>`: recompute, compare leaf by leaf, report the first difference, non-zero exit | STANDS | K5: 281 leaves, 0 differences, exit 0. K10: 1 difference at /P1/M[1], exit 3 |
| R1(iv) refuses to overwrite | STANDS | K3: exit 4, "refusing to overwrite" |
| R2 numbers shared with the published result are identical | STANDS | K6: 221 leaves compared (all 222 published leaves except `program`), 0 differences, published sha unchanged |
| R3 the 8 mutations of the chaos report are caught | STANDS | 8 of 8 caught (child). I reran 4 myself: m6 and m8 from my own copies (K9, K10), m4 and m7 from the child's files (K11, K12) |
| R4 limits of v2 | measured only | A consistent loosening TOL_P3 → 5e-6 in the table, the code and the hash gives exit 0 standalone (K7). Only `--verify` against a trusted stored result catches it (K8, exit 3) |
| v1 check design (the target) | DEFECT (confirmed, now repaired in v2) | Same finding as the chaos report. v1 also never reads a result file |

Counts (met, failed, measured only): **7, 0, 1** for the items above. Program checks in my register: 13 checks, K1–K13. 11 met their expected exit and 2 did not (K1, K2, my own defect, see §3).

### R3 table (anything not caught would be listed first: **none**)

| # | mutation | exit | caught by |
|---|---|---|---|
| m1 | P1 line I_1/I_0 → I_2/I_1 | 1 | P1 FAILED (M(64)=1.50018, factors ≈0.25) |
| m2 | u1_closed uses I_{n+1} | 1 | H FAILED, so no U(1) case qualifies and P1 FAILED |
| m3 | U(1) β = N²+1 | 1 | P1 FAILED (M(64)=0.499939 < 1/2) |
| m4 | SU(2) β = 2N² | 1 | P2 FAILED (M(64)=0.750046). **Rerun by me (K11)** |
| m5 | Z_n asymptote halved | 1 | P3 FAILED (ratio 2.0) |
| m6 | TOL_H × 1e6 | 2 | table/code mismatch, plus NC_H passed. **Rerun by me (K9)** |
| m7 | TOL_P3 × 1e6 | 2 | table/code mismatch, plus NC_P3 passed. **Rerun by me (K12)** |
| m8 | one digit changed in a result copy | 3 | `--verify`: first difference /P1/M[1] …884 vs …885. **Rerun by me (K10)** |

m6 and m7 now also change the result file (`tolerances.*.in_use`), so a byte comparison would catch them too.

## 2. Hypotheses each statement uses, and where stated
- H, P1, P2, P3: v2 docstring "PREDICATES" (copied unchanged from the v1 docstring, l.19–40). They use the character expansion and transfer-operator diagonalisation (v1 "WHAT IS COMPUTED"), heat-kernel continuum values 1/2 and 3/8, and mpmath besseli/quad accuracy at 40 and 400 digits.
- Tolerance sources: v2 docstring "TOLERANCE TABLE". TOL_H, DPS, WIN_LO/HI, TOL_P3, DPS_P3 and QUAD_CUT come from v1. NC_H_PERT = 1e-22 is my choice: 3 decades above TOL_H and 3 below TOL_H×1e6. NC_P3_OFF = 1e-5 is set by the task. The in-use/table comparison at 20 significant digits is my choice; the reason is in the docstring.
- R2 predicates C1–C3: docstring of compare_published.py, with tolerance zero (same expressions, same precision).
- "for all" (rule 4): H is tested per case. 20 of 20 cases qualify (U(1) 5 of 5, SU(2) 5 of 5), as in v1.

## 3. Failed predicates
- **K1 and K2 (v2 run 1 and its self-verify), exit 2, expected 0. My own defect, not the target's.** v2 set mp.dps = 40 after the tolerance constants, so TOL_H, TOL_P3 and the NC constants were computed at 15 digits (TOL_H = 1.0000000000000000385e-25). v1 sets the precision first. The new self-check caught this on its first run. The exact mpf equality I first used was also too strict (it trips at ulp level). Fix: set dps first, and compare at 20 significant digits. The run-1 program and its result are kept in attic/.
- The child's predictions were met in every case (8 of 8).
- Target: no predicate fails. The v1 design defect (loosened tolerances are invisible; a result file is never re-checked) is repaired in v2.

## 4. What I did not check, and what v2 still cannot catch (R4)
- **A consistent change** of table, hash and code is invisible to the self-check (K7). It is caught standalone only if it loosens a tolerance past its negative-control margin: TOL_H past 1e-22, TOL_P3 past 1e-5. Smaller loosenings, and any change to WIN_LO/WIN_HI, DPS, DPS_P3 or QUAD_CUT, are caught only by `--verify` against a trusted stored result (K8). The hash is a self-consistency check, not a signature. Whoever can edit the file can rehash it.
- **The NC constants themselves**: if NC_H_PERT and TOL_H are changed together (in table and hash too), nothing standalone catches it. Again only `--verify` does.
- **Errors common to the closed form and its check**: H checks only the helper closed forms. P1 and P2 make their own besseli calls. A wrong but self-consistent formula, or a besseli bug present in both H and P1, would pass. Examples: the U(1) and SU(2) conventions, the β trajectory, a wrong continuum value used in both the predicate and the physics. NC_P1 and NC_P2 test only one specific wrong variant each.
- **Errors in the predicate logic shared by controls and real runs**: if a predicate function were made too permissive in a way that also fails the four NCs, it would be caught. A change that keeps the specific NC inputs failing would not.
- `--verify` compares at the precision of the printed strings (5–30 digits). Changes below the printed digits are not seen.
- I did not mutate the `--verify` code, the self-check code or the refusal code (no mutation tests of the new mechanisms themselves).
- I did not check mpmath's correctness independently, nor the physics derivations (out of scope for this role).
- I did not rerun m1, m2, m3 or m5 myself. I checked their diffs only (single-line, as claimed). They remain the child's claims.

## 5. Delegated question and outcome
- **Delegated (child/):** R3. Seven single-line mutants of v2 in fresh directories, plus the changed-digit test against `--verify` (with a baseline), with predictions written before running.
- **Control question:** -ln tanh 1. The child answered 0.272341, which is correct.
- **What came back:** 8 of 8 caught, all predictions met, child PCP verify PASS (I reran it: PASS). **child/report.md is missing.** The child says the environment refused the file, and its content came in its final message. That is a deviation from the instruction.
- **My check:** the src copies are unchanged (sha matches). I diffed all 7 mutants (each one line, as specified) and the changed copy (one digit). I reran child m4 (K11: exit 1, P2 FAILED) and m7 (K12: exit 2, two defects), and independently built and ran m6 (K9) and m8 (K10). All agree with the child.

PCP verify (my register), last line:
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

## 6. Rerun commands (Git Bash, from C:/Users/donke/z4-workers/r7-fix, PYTHONUTF8=1)
```
P=C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py; SP=C:/Users/donke/AppData/Roaming/Python/Python314/site-packages
# v2 refuses to overwrite: run it in a fresh copy
mkdir -p fresh && cp two_dim_control_v2.py fresh/ && (cd fresh && python $P check --ws ../pcp --name fresh_v2 --expect-exit 0 -- python -I two_dim_control_v2.py $SP)
python $P check --ws pcp --name verify_v2 --expect-exit 0 -- python -I two_dim_control_v2.py $SP --verify two_dim_control_v2_result.json
python $P check --ws pcp --name refuse --expect-exit 4 -- python -I two_dim_control_v2.py $SP
mv compare_published_result.json compare_published_result.prev.json   # refuses to overwrite
python $P check --ws pcp --name r2 --expect-exit 0 -- python -I compare_published.py input/two_dim_control_result.json two_dim_control_v2_result.json
# mutants (each in a fresh dir; the mutated copies are in child/mut/mK/)
mkdir -p x4 && cp child/mut/m4/two_dim_control_v2.py x4/ && (cd x4 && python $P check --ws ../pcp --name x4 --expect-exit 1 -- python -I two_dim_control_v2.py $SP)
mkdir -p x7 && cp child/mut/m7/two_dim_control_v2.py x7/ && (cd x7 && python $P check --ws ../pcp --name x7 --expect-exit 2 -- python -I two_dim_control_v2.py $SP)
python $P check --ws pcp --name x8 --expect-exit 3 -- python -I two_dim_control_v2.py $SP --verify rerun/m8/changed.json
# R4 probe: r4/consistent/ (remove its result json first), expect 0 standalone and 3 with --verify ../../two_dim_control_v2_result.json
# child: cd child && rm -rf mut mutation_results.json && python $P check --ws pcp --name mutate --expect-exit 0 --timeout 7000 -- python -I mutate.py
python $P verify --ws pcp
```

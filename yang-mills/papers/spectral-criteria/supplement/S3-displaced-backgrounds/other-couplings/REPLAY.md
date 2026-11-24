# REPLAY — a2-mixb (T211)

All commands from `/home/user/z4-workers/a2-mixb`. Result directories must not exist beforehand (create_new / mode "x").
Each command was run through `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name <name> --expect-exit 0 -- <command>`; register pcp/register.jsonl.

## Build (rustc 1.97.0, edition 2021)
```
cd build
rustc --edition 2021 -O -o a2m src/a2/a2m.rs    # Q1 sampler: z1m6 with beta<8 guard removed + plaquette column
rustc --edition 2021 -O -o q2  src/a2/q2.rs     # Q2 sampler: unconditioned Wilson chain + marks
cd ..
```
build/z1m6 and build/g4_replicas are the prior worker's binaries (sources build/src/mine/z1m6.rs, build/src/ctl/replicas.rs; G4's wilson_mc.rs in build/g4/full-attempt/two-site-gap/).

## Control (prior programs)
```
python3 mkskel.py                                  # skeletons/d0.txt ... (prior convention)
python3 run.py ctl-d0 skeletons/d0.txt 6100001     # 8 streams: build/z1m6 fixed 3.276133577 <6100001+7919 i> <i%2> 576 576 6 6 12 skeletons/d0.txt results/ctl-d0/s<i>
python3 reduce.py ctl-d0                           # results/ctl-d0/summary.json
```
P4 (a2m == z1m6): `./q1_p4.sh` (results_p4/).

## Q1
```
python3 mkskel_q1.py                               # skeletons_q1/{d0,b6-k1,b6-k2,b6-k4,b12-k1,b12-k2,b12-k4,fix-k1,fix-k2,fix-k4}.txt
./q1_all.sh                                        # 14 runs, see table
python3 reduce_q1.py 6.0  q1-b6-<s> ...            # results_q1/<tag>/summary.json  (SUMMARY=<name> env var sets another output name)
python3 reduce_q1.py 12.0 q1-b12-<s> ...
```
`python3 run_q1.py <tag> <beta> <skeleton> <base> <burn>` runs `build/a2m fixed <beta> <base+7919 i> <i%2> <burn> 576 6 6 12 <skeleton> results_q1/<tag>/s<i>` for i = 0..7; exact lines in results_q1/<tag>/commands.txt.
Seeds: base = 7000001 + 100000 k, k = 0..13 in the order beta 6: d0, b6-k1, b6-k2, b6-k4, fix-k1, fix-k2, fix-k4; beta 12: d0, b12-k1, b12-k2, b12-k4, fix-k1, fix-k2, fix-k4. Burn 1152 (beta 6), 2304 (beta 12).
Rule reruns (doubled burn-in, base + 50000): `./after_q1.sh` runs `python3 run_q1.py q1-b6-b6-k4-r 6.0 skeletons_q1/b6-k4.txt 7350001 2304`;
`./rerun_b12.sh` runs `python3 run_q1.py q1-b12-b12-k4-r 12.0 skeletons_q1/b12-k4.txt 8050001 4608`, `... q1-b12-fix-k1-r 12.0 skeletons_q1/fix-k1.txt 8150001 4608`, `... q1-b12-fix-k2-r 12.0 skeletons_q1/fix-k2.txt 8250001 4608`.
Note: results_q1/q1-b6-fix-k4/summary.json was produced from partial data (my error, reduced while running) and is INVALID; the valid one is summary_full.json (`SUMMARY=summary_full.json python3 reduce_q1.py 6.0 q1-b6-fix-k4`).
Table: `python3 table_q1.py` (writes results_q1/table_<n>.md, next free n).

## Q2
```
python3 run_q2.py main 9100001     # 16 chains: build/q2 3.276133577 <9100001+7919 i> <i%2> 1000 30000 1 6 12 results_q2/main/c<i>
python3 reduce_q2.py main          # results_q2/main/summary.json, printed table
```
Exact lines in results_q2/main/commands.txt.

## Child (T212) rerun by the parent
```
python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name child-analyze-rerun --cwd child --expect-exit 0 -- python3 analyze.py prod_v1.json analysis_parent_rerun.txt
```
```
python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name child-prod-rerun --cwd child --expect-exit 0 -- python3 run.py prod_parent_rerun.json
python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name child-prod-rerun-analyze --cwd child --expect-exit 0 -- python3 analyze.py prod_parent_rerun.json analysis_parent_rerun2.txt
```
## Verify
```
python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

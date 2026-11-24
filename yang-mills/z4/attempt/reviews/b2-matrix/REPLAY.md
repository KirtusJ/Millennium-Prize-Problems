# REPLAY — b2-matrix (T217)

All commands from `/home/user/z4-workers/b2-matrix`. Result directories must not exist beforehand (create_new / mode "x").
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"

## Build
```
cd build
rustc --edition 2021 -O -o z1mx src/mine/z1mx.rs      # z1m6.rs + marks; diff in ../z1mx.diff
cd ..
```
(build/z1m6 is the prior worker's binary, used unchanged for the control.)

## Control (step 0, existing programs)
```
python3 mkskel.py
python3 run.py d0 skeletons/d0.txt 3100001 && python3 reduce.py d0       # 8 x 576, existing build/z1m6
```
## Checks of the extended sampler
```
build/z1mx gauge 4242 6 12 skeletons/d0.txt
build/z1mx gauge 4242 6 12 skeletons/d1.txt
mkdir -p results/p7
build/z1m6 fixed 3.276133577 3100001 0 576 64 6 6 12 skeletons/d0.txt results/p7/old
build/z1mx fixed 3.276133577 3100001 0 576 64 6 6 12 skeletons/d0.txt results/p7/new
cmp results/p7/old.csv results/p7/new.csv && cmp results/p7/old.colours.csv results/p7/new.colours.csv
```
## Production (32 streams x 1152; seed = base + 7919 i, hot = i % 2; train 0..15, held-out 16..31)
```
python3 prod.py M-d0 skeletons/d0.txt 8100001 && python3 analyze.py M-d0
python3 prod.py M-d1 skeletons/d1.txt 8300001 && python3 analyze.py M-d1
python3 supp.py M-d0 ; python3 supp.py M-d1
python3 clear.py                                                        # regenerates results/gen/chain.skel0.txt (prior record's clear skeleton)
python3 prod.py M-clear0 results/gen/chain.skel0.txt 8500001 && python3 analyze.py M-clear0 && python3 supp.py M-clear0
```
Exact sampler command lines: results/<tag>/commands.txt.
## Extra runs (outside the brief's minimal list)
```
cd build && rustc --edition 2021 -O -o z1mx2 src/mine/z1mx2.rs && rustc --edition 2021 -O -o z1mx3 src/mine/z1mx3.rs && cd ..
build/z1mx2 gauge 4242 6 12 skeletons/d0.txt ; build/z1mx3 gauge 4242 6 12 skeletons/d0.txt
python3 prod2.py X-d0 skeletons/d0.txt 8700001 && python3 analyze.py X-d0 && python3 supp2.py X-d0
python3 prod3.py Y-d0 skeletons/d0.txt 8900001 && python3 analyze.py Y-d0 && python3 supp3.py Y-d0
python3 prod3.py Y-d1 skeletons/d1.txt 9100001 && python3 analyze.py Y-d1 && python3 supp3.py Y-d1
python3 prod3.py Y-clear0 results/gen/chain.skel0.txt 9300001 && python3 analyze.py Y-clear0 && python3 supp3.py Y-clear0
```
## Child check (rerun of the child's program on the copied data)
```
mkdir childcheck && cp child/an.py child/an3.py childcheck/ && ln -s ../child/data childcheck/data
cd childcheck && python3 -I an3.py
```
## Raw data
results/<tag>/s<i>.X.csv (marks per measurement), s<i>.Dc.txt (24 per-colour n x n matrices, mean of (X'-X'')(X'-X'')^T/2),
s<i>.csv/.colours.csv/.meta.txt (original z1m6 outputs), analysis.json, C_D_train_held.txt, supp*.json.

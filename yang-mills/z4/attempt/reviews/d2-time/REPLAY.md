# REPLAY — d2-time (T226)
All commands from /home/user/z4-workers/d2-time. Result directories/files must not exist beforehand (mode "x" / create_new).
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos; G=/home/user/z4-work/graph/attempt.jsonl

## Control
python3 -c "import math;print('%.6f'%(-math.log(math.tanh(1))))"     # 0.272341

## Build (z1mx4 = prior binary, rebuilt byte-identical from build/src/c2/z1mx4.rs; z1mx5 = mine, diff in z1mx5.diff)
cd build && rustc --edition 2021 -O -o z1mx5 src/d2/z1mx5.rs && cd ..

## Skeletons and sampler checks
$P check --ws pcp --name mkskel --expect-exit 0 -- python3 mkskel.py                 # skeletons/d0.txt (prior program)
$P check --ws pcp --name clear --expect-exit 0 -- python3 clear.py                   # results/gen/chain.skel0.txt (40/60, kept 0,2,4)
$P check --ws pcp --name gauge_t_d0 --expect-exit 0 -- build/z1mx5 gauge_t 4242 6 12 skeletons/d0.txt     # T-P1, T-P2
build/z1mx5 gauge_t 4243 6 12 results/gen/chain.skel0.txt                            # same on clear (direct run)
$P check --ws pcp --name ctl5 --expect-exit 0 -- python3 ctl5.py        # K4: exit 1 (meta.txt prefix differs: my test design)
$P check --ws pcp --name ctl5b --expect-exit 0 -- python3 ctl5b.py      # T-P0b, T-P4

## Weights
weights/w_d0.txt: made by the inline script recorded in notes.md step 3 (prior_weights/w_L4.txt, w_L1.txt embedded, f4)
$P check --ws pcp --name fitw-clear --expect-exit 0 -- python3 fitw.py   # results/F-clear0 (= prior G-clear0 reproduction), weights/w_clear.txt

## Production (32 streams x 1152, fresh seeds)
$P check --ws pcp --name prodt-d0 --expect-exit 0 -- python3 prodt.py T-d0 skeletons/d0.txt weights/w_d0.txt 21100001
$P check --ws pcp --name prodt-clear --expect-exit 0 -- python3 prodt.py T-clear0 results/gen/chain.skel0.txt weights/w_clear.txt 21300001
Exact sampler lines: results/<tag>/commands.txt

## Analysis
$P check --ws pcp --name antime-d0 --expect-exit 0 -- python3 antime.py T-d0 weights/w_d0.txt
$P check --ws pcp --name antime-clear --expect-exit 0 -- python3 antime.py T-clear0 weights/w_clear.txt
python3 verdict.py    # applies the interpretation rule (prodt.py docstring) -> results/verdict.txt

## Child (T227)
$R task-admit $G --by principal --label d2-time-child --parent T226        # printed T227
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T227

## Register
$P verify --ws pcp
$R verify pcp/register.jsonl

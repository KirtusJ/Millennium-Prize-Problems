# REPLAY (f2-cross2, T239). Run from /home/user/z4-workers/f2-cross2. Result files are create-new: move old ones away first.
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"     # control 0.272341 -> control.txt
$P init pcp --principal principal --principal-name "Kirtus Justus"
rustc --edition 2021 -O -o src/cross2 src/cross2.rs                 # includes g4/wilson_mc.rs verbatim
# Q0 self-test (gauge + center flips), seeds 77, 78
$P check --ws pcp --name selftest-f --expect-exit 0 -- src/cross2 selftest 3.493705679 77 10 6 results/selftest-N10.txt
$P check --ws pcp --name selftest-c --expect-exit 0 -- src/cross2 selftest 3.196581051 78 5 4 results/selftest-N5.txt
# ensembles: 16 chains, chain i seed BASE+7919 i, hot = i%2, burn 500, NMEAS meas every 3 HB sweeps, 2 processes (src/run_ensemble2.sh)
$P check --ws pcp --name ens-c2 --timeout 900  --expect-exit 0 -- src/run_ensemble2.sh c2 3.196581051 5 10 6101307 2000
$P check --ws pcp --name ens-f2 --timeout 1800 --expect-exit 0 -- src/run_ensemble2.sh f2 3.493705679 10 20 6301307 2000
$P check --ws pcp --name ens-c4 --timeout 900  --expect-exit 0 -- src/run_ensemble2.sh c4 3.196581051 5 20 6201307 2000
#   (ens-f4: 16x2000 base 6401307 was killed after 2 chains by the session's 600 s background limit; results/f4 partial, unused, no PCP record)
$P check --ws pcp --name ens-f4b --timeout 2400 --expect-exit 0 -- src/run_ensemble2.sh f4b 3.493705679 10 40 6501307 1000
# child T242 (admitted under T239), reduction of c2 HELD per-chain matrices
$R task-admit $G --by principal --label f2-cross2-child --parent T239
mkdir -p child/data; for i in 2 3 6 7 10 11 14 15; do cp results/c2/chain-$i.txt child/data/; done     # child/PROMPT.txt as stored
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T242
mkdir -p scratch/childrerun; cp -r child/data child/control.txt scratch/childrerun/
$P check --ws pcp --name child-rerun --cwd scratch/childrerun --expect-exit 0 -- python3 -I /home/user/z4-workers/f2-cross2/child/analyze.py
$P check --ws pcp --name check-dirsum --expect-exit 0 -- python3 -I src/check_dirsum.py
set -o noclobber; python3 -I src/check_dirsum.py > results/check-dirsum.txt
# analysis (numpy only; deterministic, ratio search seed 239)
$P check --ws pcp --name analysis-2l --timeout 900 --expect-exit 0 -- python3 -I src/analysis2.py c2 f2 results/analysis-2l.txt
$P check --ws pcp --name analysis-null-c2c4 --expect-exit 0 -- python3 -I src/analysis2.py c2 c4 results/analysis-null-c2c4.txt
$P check --ws pcp --name analysis-4l --expect-exit 0 -- python3 -I src/analysis2.py c4 f4b results/analysis-4l.txt
$P check --ws pcp --name cross-eval --expect-exit 0 -- python3 -I src/cross_eval2.py c2 f2 c4 f4b results/cross-eval-2l-frozen-on-4l.txt
$P check --ws pcp --name analysis-null-f2f4b --expect-exit 0 -- python3 -I src/analysis2.py f2 f4b results/analysis-null-f2f4b.txt
# verification
$P verify --ws pcp ; $R verify pcp/register.jsonl

# REPLAY (e2-cross, T231). Run from /home/user/z4-workers/e2-cross. Result files are opened create-new: move old ones first.
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
# control
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"          # 0.272341
$P check --ws pcp --name control-reduce --expect-exit 0 -- python3 -I src/control_reduce.py
# build (includes g4/wilson_mc.rs verbatim)
rustc --edition 2021 -O -o src/cross src/cross.rs
# ensembles: 16 chains each, chain i: seed = BASE + 7919*i, hot = i%2, burn 500, 500 meas every 3 HB sweeps
#   src/cross BETA SEED HOT N T 500 500 3 results/LABEL/chain-i.txt
$P check --ws pcp --name ens-c2 --timeout 900  --expect-exit 0 -- src/run_ensemble.sh c2 3.196581051 5 10 5101307
$P check --ws pcp --name ens-c4 --timeout 900  --expect-exit 0 -- src/run_ensemble.sh c4 3.196581051 5 20 5201307
$P check --ws pcp --name ens-f2 --timeout 1200 --expect-exit 0 -- src/run_ensemble.sh f2 3.493705679 10 20 5301307
$P check --ws pcp --name ens-f4 --timeout 1800 --expect-exit 0 -- src/run_ensemble.sh f4 3.493705679 10 40 5401307
# analysis
$P check --ws pcp --name analysis-2l --expect-exit 0 -- python3 -I src/analysis.py c2 f2 results/analysis-2l.txt
$P check --ws pcp --name analysis-4l --expect-exit 0 -- python3 -I src/analysis.py c4 f4 results/analysis-4l.txt
$P check --ws pcp --name analysis-coarse-null --expect-exit 0 -- python3 -I src/analysis.py c2 c4 results/analysis-null-c2c4.txt
$P check --ws pcp --name analysis-fine-null --expect-exit 0 -- python3 -I src/analysis.py f2 f4 results/analysis-null-f2f4.txt
$P check --ws pcp --name cross-eval --expect-exit 0 -- python3 -I src/cross_eval.py results/cross-eval.txt
# child (T235) and its rerun
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$R task-admit $G --by principal --label e2-cross-child --parent T231
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T235
mkdir -p scratch/childrerun; $P check --ws pcp --name child-rerun --cwd scratch/childrerun --expect-exit 0 -- python3 -I /home/user/z4-workers/e2-cross/child/analyze.py c2 f2
# verification
$P verify --ws pcp ; $R verify pcp/register.jsonl

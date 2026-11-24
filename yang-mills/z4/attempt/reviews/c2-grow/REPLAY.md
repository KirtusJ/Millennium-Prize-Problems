# REPLAY — c2-grow (T223)
All commands from /home/user/z4-workers/c2-grow. Result directories/files must not exist beforehand (mode "x" / create_new).
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"

## Control
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control.txt 0.272341

## Build (rustc --edition 2021 -O; build/z1mx3 is the prior binary, used only for P8)
cd build && rustc --edition 2021 -O -o z1mx4 src/c2/z1mx4.rs && rustc --edition 2021 -O -o q3 src/c2/q3.rs && cd ..

## Skeletons and checks
python3 mkskel.py                         # skeletons/d0.txt (prior program)
python3 clear.py                          # results/gen/chain.skel0.txt (prior program; 40/60 at pi/4)
python3 faces.py                          # ring-1 / ring-2 face lists
build/z1mx4 gauge 4242 6 12 skeletons/d0.txt      # P6 + P9 (face holonomies)
python3 ctl4.py                           # P8: z1mx4 vs z1mx3

## Q1 production and analysis (32 streams x 1152; seed = base + 7919 i, hot = i % 2)
python3 prod4.py G-d0 skeletons/d0.txt 11100001
python3 prod4.py G-clear0 results/gen/chain.skel0.txt 11300001
python3 an4.py G-d0 ; python3 an4.py G-clear0
python3 swap4.py G-d0 ; python3 swap4.py G-clear0
Exact sampler lines: results/<tag>/commands.txt

## Child rerun
mkdir childcheck && cp child/analyze2.py childcheck/ && ln -s ../child/data childcheck/data && (cd childcheck && python3 -I analyze2.py)

## Q2 (16 chains x 2000 configs, 1000 burn cycles, gap 1; weights = L4 optimum at -I)
python3 run_q3.py main results/G-d0/w_L4.txt 12100001 2000
python3 an_q3.py main
Exact sampler lines: results_q2/main/cmds.list

## Register
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl

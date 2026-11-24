#!/bin/bash
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
D=/home/user/z4-workers/z1-mix6
cd $D
$P check --ws pcp --name run-clear0 --expect-exit 0 -- python3 $D/run.py clear0 $D/results/gen/chain.skel0.txt 5100001
$P check --ws pcp --name run-clear2 --expect-exit 0 -- python3 $D/run.py clear2 $D/results/gen/chain.skel2.txt 5200001
$P check --ws pcp --name run-clear4 --expect-exit 0 -- python3 $D/run.py clear4 $D/results/gen/chain.skel4.txt 5300001
$P check --ws pcp --name big-d0   --expect-exit 0 -- python3 $D/run_big.py L-d0   $D/skeletons/d0.txt   6100001
$P check --ws pcp --name big-d0.5 --expect-exit 0 -- python3 $D/run_big.py L-d0.5 $D/skeletons/d0.5.txt 6200001
$P check --ws pcp --name big-d1   --expect-exit 0 -- python3 $D/run_big.py L-d1   $D/skeletons/d1.txt   6300001
$P check --ws pcp --name big-d2   --expect-exit 0 -- python3 $D/run_big.py L-d2   $D/skeletons/d2.txt   6400001
$P check --ws pcp --name big-d4   --expect-exit 0 -- python3 $D/run_big.py L-d4   $D/skeletons/d4.txt   6500001

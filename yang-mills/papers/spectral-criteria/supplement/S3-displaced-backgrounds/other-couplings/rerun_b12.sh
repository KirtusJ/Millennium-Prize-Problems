#!/bin/bash
# rule reruns (doubled burn 4608, base + 50000) for beta-12 runs that failed a hot/cold check; runs after Q2.
cd /home/user/z4-workers/a2-mixb
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
until grep -q Q2DONE after_q1.log; do sleep 2; done
# original bases: b12-k4 = 7000001+100000*10, fix-k1 = +11, fix-k2 = +12
$P check --ws pcp --name run-q1-b12-b12-k4-r --expect-exit 0 -- python3 run_q1.py q1-b12-b12-k4-r 12.0 skeletons_q1/b12-k4.txt 8050001 4608
$P check --ws pcp --name run-q1-b12-fix-k1-r --expect-exit 0 -- python3 run_q1.py q1-b12-fix-k1-r 12.0 skeletons_q1/fix-k1.txt 8150001 4608
$P check --ws pcp --name run-q1-b12-fix-k2-r --expect-exit 0 -- python3 run_q1.py q1-b12-fix-k2-r 12.0 skeletons_q1/fix-k2.txt 8250001 4608
echo RERUN12DONE

#!/bin/bash
# runs after q1_all.sh: b6-k4 rerun (rule: doubled burn 2304, base 7300001+50000), then Q2 production.
cd /home/user/z4-workers/a2-mixb
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
until grep -q ALLDONE q1_all.log; do sleep 2; done
$P check --ws pcp --name run-q1-b6-b6-k4-r --expect-exit 0 -- python3 run_q1.py q1-b6-b6-k4-r 6.0 skeletons_q1/b6-k4.txt 7350001 2304
echo RERUNDONE
$P check --ws pcp --name run-q2-main --expect-exit 0 -- python3 run_q2.py main 9100001
echo Q2DONE

#!/bin/bash
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
cd /home/user/z4-workers/i1-mc3
if [ "$1" = F ]; then until [ -s runE.log ]; do sleep 3; done; $P check --ws pcp --name runF_childrerun_ctrlrerun --expect-exit 0 --timeout 1500 -- ./runF.sh > runF.log 2>&1
else until [ -s runD.log ]; do sleep 3; done; $P check --ws pcp --name runG_b16384_rerun64_256 --expect-exit 0 --timeout 1500 -- ./runG.sh > runG.log 2>&1; fi

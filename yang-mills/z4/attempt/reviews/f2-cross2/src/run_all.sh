#!/bin/bash
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
cd /home/user/z4-workers/e2-cross
$P check --ws pcp --name ens-c2 --timeout 900 --expect-exit 0 -- src/run_ensemble.sh c2 3.196581051 5 10 5101307
$P check --ws pcp --name ens-c4 --timeout 900 --expect-exit 0 -- src/run_ensemble.sh c4 3.196581051 5 20 5201307
$P check --ws pcp --name ens-f2 --timeout 1200 --expect-exit 0 -- src/run_ensemble.sh f2 3.493705679 10 20 5301307
$P check --ws pcp --name ens-f4 --timeout 1800 --expect-exit 0 -- src/run_ensemble.sh f4 3.493705679 10 40 5401307

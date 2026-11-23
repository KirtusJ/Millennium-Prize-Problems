#!/bin/bash
# second batch (decided after first-batch errors; predicates unchanged), 2 lanes x 1 core
export OMP_NUM_THREADS=1
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
cd /home/user/z4-workers/l1-mcw
lane1() {
 $P check --ws pcp --name prod-b1024e --expect-exit 0 -- python3 mcp.py 2 1024 136 4 300 2500 2 0 145 results/b1024e
 $P check --ws pcp --name prod-b1024f --expect-exit 0 -- python3 mcp.py 2 1024 136 4 300 2500 2 0 146 results/b1024f
 $P check --ws pcp --name prod-b256b --expect-exit 0 -- python3 mcp.py 2 256 88 16 200 1100 2 0 132 results/b256b
 $P check --ws pcp --name prod-b64b --expect-exit 0 -- python3 mcp.py 2 64 56 16 200 1500 2 0 122 results/b64b
}
lane2() {
 $P check --ws pcp --name prod-b1024g --expect-exit 0 -- python3 mcp.py 2 1024 136 4 300 2500 2 0 147 results/b1024g
 $P check --ws pcp --name prod-b1024h --expect-exit 0 -- python3 mcp.py 2 1024 136 4 300 2500 2 0 148 results/b1024h
 $P check --ws pcp --name prod-b256c --expect-exit 0 -- python3 mcp.py 2 256 88 16 200 1100 2 0 133 results/b256c
 $P check --ws pcp --name prod-b64c --expect-exit 0 -- python3 mcp.py 2 64 56 16 200 1500 2 0 123 results/b64c
}
lane1 > lane1b.log 2>&1 &
lane2 > lane2b.log 2>&1 &
wait

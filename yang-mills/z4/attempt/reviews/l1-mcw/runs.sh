#!/bin/bash
# two lanes, 1 core each (OMP_NUM_THREADS=1)
export OMP_NUM_THREADS=1
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
cd /home/user/z4-workers/l1-mcw
lane1() {
 $P check --ws pcp --name prod-b1024a --expect-exit 0 -- python3 mcp.py 2 1024 136 4 300 2500 2 0 141 results/b1024a
 $P check --ws pcp --name prod-b1024b --expect-exit 0 -- python3 mcp.py 2 1024 136 4 300 2500 2 0 142 results/b1024b
 $P check --ws pcp --name prod-b64 --expect-exit 0 -- python3 mcp.py 2 64 56 16 200 1500 2 0 121 results/b64
}
lane2() {
 $P check --ws pcp --name prod-b1024c --expect-exit 0 -- python3 mcp.py 2 1024 136 4 300 2500 2 0 143 results/b1024c
 $P check --ws pcp --name prod-b1024d --expect-exit 0 -- python3 mcp.py 2 1024 136 4 300 2500 2 0 144 results/b1024d
 $P check --ws pcp --name prod-b256 --expect-exit 0 -- python3 mcp.py 2 256 88 16 200 1100 2 0 131 results/b256
}
lane1 > lane1.log 2>&1 &
lane2 > lane2.log 2>&1 &
wait

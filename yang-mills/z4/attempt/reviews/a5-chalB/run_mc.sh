#!/bin/bash
# runs the six MC cases sequentially (1 core), each through the register
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
for L in 4 6; do for b in 4 8 16; do
  if [ $L = 4 ]; then NM=2000; else NM=1000; fi
  $P check --ws pcp --name mc4d-L$L-b$b --expect-exit 0 -- python3 mc4d.py $L $b 200 $NM $((1000+10*L+b)) mc_L${L}_b${b}.json
done; done

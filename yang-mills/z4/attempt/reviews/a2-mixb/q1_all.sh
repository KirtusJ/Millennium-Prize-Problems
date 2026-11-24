#!/bin/bash
# Q1 production: all runs in sequence, each through pcp check. Seeds base = 7000001 + 100000*k.
cd /home/user/z4-workers/a2-mixb
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
k=0
for b in 6.0 12.0; do
  if [ $b = 6.0 ]; then burn=1152; bt=b6; else burn=2304; bt=b12; fi
  for s in d0 $bt-k1 $bt-k2 $bt-k4 fix-k1 fix-k2 fix-k4; do
    base=$((7000001 + 100000*k)); k=$((k+1))
    tag=q1-$bt-$s
    $P check --ws pcp --name run-$tag --expect-exit 0 -- python3 run_q1.py $tag $b skeletons_q1/$s.txt $base $burn
  done
done
echo ALLDONE

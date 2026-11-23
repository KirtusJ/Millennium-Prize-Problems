#!/bin/bash
# runs all production cases; outputs opened with wx in vortex (fails if exist)
set -e
cd "$(dirname "$0")"
for b in 0.3 0.6; do
 ./vortex 3 2 $b 8 1 out/c3_3d_L2_b${b}_n8.dat
 for L in 2 3 4; do
  for n in 8 5; do ./vortex 4 $L $b $n 1 out/d4_L${L}_b${b}_n${n}.dat; done
 done
done

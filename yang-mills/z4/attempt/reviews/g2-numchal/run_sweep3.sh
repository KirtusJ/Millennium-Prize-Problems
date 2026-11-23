#!/bin/bash
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
set -e
while read b na nt nc k; do
  python3 nys.py spec $b $na $nt $nc $k results/spec_b${b}_na${na}_nt${nt}_nc${nc}.json
done <<LIST
512 180 24 1200 70
512 240 32 1300 70
1024 256 24 2200 70
1024 320 32 2300 70
LIST

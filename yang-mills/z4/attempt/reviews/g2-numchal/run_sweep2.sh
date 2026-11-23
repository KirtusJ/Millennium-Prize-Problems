#!/bin/bash
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
set -e
while read b na nt nc k; do
  python3 nys.py spec $b $na $nt $nc $k results/spec_b${b}_na${na}_nt${nt}_nc${nc}.json
done <<LIST
128 100 24 460 90
128 140 32 560 90
256 128 24 720 80
256 176 32 820 80
LIST

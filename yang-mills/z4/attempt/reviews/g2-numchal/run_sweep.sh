#!/bin/bash
# beta na nt nc k ; each beta at a base and a refined (na x1.5, nt x1.5, nc+100) resolution
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
set -e
while read b na nt nc k; do
  python3 nys.py spec $b $na $nt $nc $k results/spec_b${b}_na${na}_nt${nt}_nc${nc}.json
done <<LIST
2 32 16 200 100
2 48 24 300 100
4 32 16 200 100
4 48 24 300 100
8 40 16 220 100
8 60 24 320 100
16 48 16 240 100
16 72 24 340 100
32 64 20 270 100
32 96 30 370 100
64 80 24 330 100
64 120 36 430 100
LIST
